init python:
    import itertools

    class CellLevel( object ):
        def __init__( self, ai_idle_time, human_idle_time ):
            self.ai_idle_time    = ai_idle_time
            self.human_idle_time = human_idle_time

    CELL_LEVELS = [
        CellLevel( ai_idle_time    = (0.6, 0.85),
                   human_idle_time = (0.7, 0.9) )
        ]

    #### DESIGNERS: DO NOT CHANGE ANYTHING BEYOND THIS LINE ####

    # animation names.
    CELL_ANIMATION_PULSE = "pulse"

    # animation durations.  these divided into the number of frames that are
    # in the corresponding animation are the frames per second value passed to
    # the GameAnimation constructor.
    CELL_ANIMATION_PULSE_DURATION = 0.45

    # number of animation frames.
    NUMBER_CELL_PULSE_FRAMES = 3

    # prefab names.
    AI_CELL_TYPE    = "ai_cell"
    HUMAN_CELL_TYPE = "human_cell"

    # how fast cells multiply.
    HUMAN_GROWTH_RATE     = 2
    AI_STAGE1_GROWTH_RATE = 0.5
    AI_STAGE2_GROWTH_RATE = 0.3
    AI_STAGE3_GROWTH_RATE = 0.1

    AI_STAGE1_GROWTH_RATE_DURATION = 20
    AI_STAGE2_GROWTH_RATE_DURATION = 40

    # how fast a cell moves on either axis in pixels per second.
    CELL_SPEED = 70

    # cell states.
    CELL_STATE_IDLE           = "idle"
    CELL_STATE_MOVING         = "moving"
    CELL_STATE_PARENT_GROWING = "parent_growing"
    CELL_STATE_CHILD_GROWING  = "child_growing"

    # static locations and dimensions.
    PETRI_DISH_X = 17
    PETRI_DISH_Y = 0

    GRID_OFFSET_X = 52
    GRID_OFFSET_Y = 74

    GRID_CELL_WIDTH  = 48
    GRID_CELL_HEIGHT = 48

    NUMBER_GRID_ROWS = 9
    NUMBER_GRID_COLS = 10

    def get_slot_position( row, col ):
        x = col * GRID_CELL_WIDTH + GRID_CELL_WIDTH / 2
        y = row * GRID_CELL_HEIGHT + GRID_CELL_HEIGHT / 2
        return (x, y)

    class GridSlot( object ):
        def __init__( self ):
            self.is_valid = True
            self.cells    = []

    class Grid( object ):
        def __init__( self ):
            self.slots = [ GridSlot() for index in xrange( NUMBER_GRID_ROWS *
                                                           NUMBER_GRID_COLS ) ]

            invalid_locations = [ (0,0), (0,1), (0,2), (0,7), (0,8), (0,9),
                                  (1,0), (1,1), (1,9),
                                  (2,0), (2,9),
                                  (3,0),
                                  (6,0), (6,9),
                                  (7,0), (7,1), (7,9),
                                  (8,0), (8,1), (8,2), (8,8), (8,9) ]

            for row, col in invalid_locations:
                index = col + row * NUMBER_GRID_COLS
                self.slots[index].is_valid = False

            self.free_slots = [ (row, col)
                                for row in xrange( NUMBER_GRID_ROWS )
                                for col in xrange( NUMBER_GRID_COLS )
                                if (row, col) not in invalid_locations ]

#            renpy.log( "%s" % self.free_slots )

        def add_cell( self, cell, row, col ):
            index = col + row * NUMBER_GRID_COLS
#            renpy.log( "Adding (%s, %s)" % (row, col) )
#            renpy.log( "Slot cells: %s" % self.slots[index].cells )
#            renpy.log( "Free slots: %s" % self.free_slots )
            self.slots[index].cells.append( cell )
            self.free_slots.remove( (row, col) )

        def remove_cell( self, cell, row, col ):
            index = col + row * NUMBER_GRID_COLS
#            renpy.log( "Removing (%s, %s)" % (row, col) )
#            renpy.log( "Slot cells: %s" % self.slots[index].cells )
#            renpy.log( "Free slots: %s" % self.free_slots )
            self.slots[index].cells.remove( cell )
            self.free_slots.append( (row, col) )

        def get_free_neighbors( self, row, col ):
            neighbors = []
            slots     = self.slots

            # up.
            if row > 0:
                up_row   = row - 1
                up_col   = col
                up_index = up_col + up_row * NUMBER_GRID_COLS
                if slots[up_index].is_valid and not slots[up_index].cells:
                    neighbors.append( (up_row, up_col) )

            # right.
            if col < (NUMBER_GRID_COLS - 1):
                right_row   = row
                right_col   = col + 1
                right_index = right_col + right_row * NUMBER_GRID_COLS
                if slots[right_index].is_valid and not slots[right_index].cells:
                    neighbors.append( (right_row, right_col) )

            # down.
            if row < (NUMBER_GRID_ROWS - 1):
                down_row   = row + 1
                down_col   = col
                down_index = down_col + down_row * NUMBER_GRID_COLS
                if slots[down_index].is_valid and not slots[down_index].cells:
                    neighbors.append( (down_row, down_col) )

            # left.
            if col > 0:
                left_row   = row
                left_col   = col - 1
                left_index = left_col + left_row * NUMBER_GRID_COLS
                if slots[left_index].is_valid and not slots[left_index].cells:
                    neighbors.append( (left_row, left_col) )

#            renpy.log( "Free neighbords for (%s, %s): %s" % (row, col, neighbors) )
            return neighbors

        def get_free_slot( self ):
            return renpy.random.choice( self.free_slots ) if self.free_slots else None

    class Cells( Minigame ):
        def __init__( self, level_number=1 ):
            super( Cells, self ).__init__()

            if level_number > len( CELL_LEVELS ) or level_number <= 0:
                raise ValueError( "Invalid Cell level number %d.  Level "
                                  "number must be between 1 and %d." %
                                  (level_number, len( CELL_LEVELS )) )

            # set up automated level difficulty parameters.
            level = CELL_LEVELS[level_number - 1]

            self.ai_idle_time      = Randomizer( level.ai_idle_time[0],
                                                 level.ai_idle_time[1] )
            self.human_idle_time   = Randomizer( level.human_idle_time[0],
                                                 level.human_idle_time[1] )
            self.ai_growth_rate    = StagedValue( [ (0,                              AI_STAGE1_GROWTH_RATE),
                                                    (AI_STAGE1_GROWTH_RATE_DURATION, AI_STAGE2_GROWTH_RATE),
                                                    (AI_STAGE2_GROWTH_RATE_DURATION, AI_STAGE3_GROWTH_RATE) ] )
            self.human_growth_rate = StagedValue( [ (0, HUMAN_GROWTH_RATE) ] )

            # setup game state.
            self.elapsed_time = 0

            # setup entities.
            self.dish        = None
            self.human_cells = []
            self.ai_cells    = []
            self.grid        = Grid()

            self.create_dish()
            self.create_cells()

            # XXX: remove me.
            self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )

            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )

            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )

            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )
            # self.spawn_cell( HUMAN_CELL_TYPE )

        def create_dish( self ):
            self.dish             = GameObject()
            self.dish["renderer"] = GameRenderer( GameImage( "gfx/cells/petri_dish.png" ) )
            self.dish["transform"].set_position( PETRI_DISH_X, PETRI_DISH_Y )

        def create_cells( self ):
            human_cell = GameObject()
            human_cell["renderer"] = GameRenderer()
            human_cell["renderer"].add_animation( CELL_ANIMATION_PULSE,
                                                  GameAnimation( [ GameImage( "gfx/cells/human/cell-human-%d.png" % frame_index, Anchor.CENTER )
                                                                   for frame_index in xrange( NUMBER_CELL_PULSE_FRAMES ) ],
                                                                 NUMBER_CELL_PULSE_FRAMES / CELL_ANIMATION_PULSE_DURATION ) )
            PrefabFactory.add_prefab( HUMAN_CELL_TYPE, human_cell )

            ai_cell = GameObject()
            ai_cell["renderer"] = GameRenderer()
            ai_cell["renderer"].add_animation( CELL_ANIMATION_PULSE,
                                               GameAnimation( [ GameImage( "gfx/cells/ai/cell-ai-%d.png" % frame_index, Anchor.CENTER )
                                                                for frame_index in xrange( NUMBER_CELL_PULSE_FRAMES ) ],
                                                              NUMBER_CELL_PULSE_FRAMES / CELL_ANIMATION_PULSE_DURATION ) )
            PrefabFactory.add_prefab( AI_CELL_TYPE, ai_cell )

        def spawn_cell( self, cell_type, slot=None, state=None ):
            # if a slot wasn't given, get a random available one.  return
            # early if we can't get one.
            if not slot:
                slot = self.grid.get_free_slot()
                if not slot:
                    return

            # create the new cell.
            cell = PrefabFactory.instantiate( cell_type )

            # set the appropriate behavior depending on whether this is a
            # human or AI cell.
            if cell_type == HUMAN_CELL_TYPE:
                cell["behavior"] = CellBehavior( cell_type,
                                                 self.grid,
                                                 self.human_idle_time,
                                                 self.human_growth_rate,
                                                 self.spawn_cell,
                                                 state )
                self.human_cells.append( cell )
            else:
                cell["behavior"] = CellBehavior( cell_type,
                                                 self.grid,
                                                 self.ai_idle_time,
                                                 self.ai_growth_rate,
                                                 self.spawn_cell,
                                                 state )
                self.ai_cells.append( cell )

            # if the state of the cell being created is the child growing
            # state, then we don't want to call set_slot() because that will
            # attempt to modify the grid's set of free cells, which could
            # possibly cause corrupted grid state or (even worse) crash.
            # instead, we use the slot to derive the initial position of the
            # cell and simply set that.
            if state == CELL_STATE_CHILD_GROWING:
                row, col = slot
                x, y     = get_slot_position( row, col )
                cell["transform"].set_position( x,y )
            else:
                cell["behavior"].set_slot( slot )

            cell["renderer"].play_animation( CELL_ANIMATION_PULSE )
            return cell

        def get_displayables( self ):
            displayables = []

            for cell in itertools.chain( self.human_cells, self.ai_cells ):
                displayables.extend( cell["renderer"].get_displayables() )

            displayables.extend( self.dish["renderer"].get_displayables() )

            return displayables

        def render( self, blitter ):
            world_transform = self.get_world_transform()
            self.dish["renderer"].render( blitter, world_transform )

            cell_transform = GameTransform( world_transform.x +
                                            self.dish["transform"].x +
                                            GRID_OFFSET_X,
                                            world_transform.y +
                                            self.dish["transform"].y +
                                            GRID_OFFSET_Y )
            for cell in itertools.chain( self.ai_cells, self.human_cells ):
                cell["renderer"].render( blitter, cell_transform )

        def update( self, delta_sec ):
            self.elapsed_time += delta_sec
#            renpy.log( "Start update (%s)" % self.elapsed_time )

            # update the growth rate.
            self.ai_growth_rate.update( delta_sec )

            # update all cells.
            for cell in itertools.chain( self.ai_cells, self.human_cells ):
                cell.update( delta_sec )

#            renpy.log( "End update\n\n" )

        def on_key_down( self, key ):
            if key == pygame.K_ESCAPE:
                self.quit()

        def on_mouse_down( self, mx, my, button ):
            renpy.log( "Mouse down" )

    class CellBehavior( GameComponent ):
        def __init__( self, cell_type, grid, idle_time, growth_rate,
                      spawn_cell, state=None ):
            super( CellBehavior, self ).__init__()
            self.state        = state or CELL_STATE_IDLE
            self.type         = cell_type
            self.grid         = grid
            self.slot         = None
            self.target_slot  = None
            self.parent       = None
            self.spawn_cell   = spawn_cell
            self.idle_time    = idle_time
            self.growth_rate  = growth_rate
            self.move_timeout = self.idle_time.get_value()
            self.grow_timeout = self.growth_rate.get_value()

        def reset_grow_timeout( self ):
            self.grow_timeout = self.growth_rate.get_value()

        def reset_move_timeout( self ):
            self.move_timeout = self.idle_time.get_value()

        def set_slot( self, slot ):
            row, col = slot

            # update the grid.
            if self.slot:
                old_row, old_col = self.slot
                self.grid.remove_cell( self, old_row, old_col )
            self.grid.add_cell( self, row, col )

            # update the internal slot state and set this cell's new position.
            self.slot = slot
            x, y      = get_slot_position( row, col )
            self.game_object["transform"].set_position( x, y )

        def set_parent( self, parent ):
            self.parent = parent

        def set_target_slot( self, target_slot ):
            row, col = target_slot

            # target slots get flagged as occupied in the grid so that no
            # other cell tries to move into it.
            if self.target_slot:
                old_row, old_col = self.target_slot
                self.grid.remove_cell( self, old_row, old_col )
            self.grid.add_cell( self, row, col )

            # update the internal target state.
            self.target_slot = target_slot

        def move_towards_target( self, delta_sec ):
            at_target              = False
            target_row, target_col = self.target_slot

            # figure out which we have to go to reach our target and update
            # our position.
            tx, ty  = get_slot_position( target_row, target_col )
            sx      = self.game_object["transform"].x
            sy      = self.game_object["transform"].y
            dx      = tx - sx
            dy      = ty - sy
            sx     += sign( dx ) * delta_sec * CELL_SPEED
            sy     += sign( dy ) * delta_sec * CELL_SPEED

            if almost_equal( sx, tx ) and almost_equal( sy, ty ):
                # we're pretty much on our target destination.  set the new
                # position to be exactly equal to our target's position in
                # order to avoid drift due to floating point errors
                # accumulated over time.
                sx        = tx
                sy        = ty
                at_target = True

            # set the new position and return whether we reached our target.
            self.game_object["transform"].set_position( sx, sy )
            return at_target

        def on_grow_complete( self ):
            self.state = CELL_STATE_IDLE
            self.reset_grow_timeout()

        def update( self, delta_sec ):
            self.move_timeout -= delta_sec
            self.grow_timeout -= delta_sec

#            renpy.log( "Updating %s (state=%s, slot=%s, target=%s)" %
#                       (self, self.state, self.slot, self.target_slot) )

            # perform actions in this order of importance:
            #
            #   * moving
            #   * growing
            #   * chilling
            if self.state == CELL_STATE_MOVING:
                # move towards the target.
                if self.move_towards_target( delta_sec ):
                    # we reached the target.  tell the grid our previous slot
                    # is now free and unset our target.  then go back to the
                    # idle state.
                    row, col         = self.slot
                    self.slot        = self.target_slot
                    self.target_slot = None
                    self.state       = CELL_STATE_IDLE
                    self.grid.remove_cell( self, row, col )
                    self.reset_move_timeout()
            elif self.state == CELL_STATE_CHILD_GROWING:
                # move towards the target.
                if self.move_towards_target( delta_sec ):
                    # we reached the target.  set our slot to be our target,
                    # unset our target and then go back to the idle state.
                    self.slot        = self.target_slot
                    self.target_slot = None
                    self.state       = CELL_STATE_IDLE
                    self.reset_grow_timeout()

                    # tell our parent that we are done growing.
                    self.parent.on_grow_complete()
                    self.parent = None
            elif self.state == CELL_STATE_IDLE:
                # see if it's time to grow.  if it isn't, see if it's time to
                # move.  otherwise just continue waiting until it's time to do
                # something.
                if self.grow_timeout <= 0:
                    # figure out which slots we can grow into.
                    row, col  = self.slot
                    neighbors = self.grid.get_free_neighbors( row, col )

                    # do something only if we have a free slot.
                    if neighbors:
                        target_slot = renpy.random.choice( neighbors )
                        self.state  = CELL_STATE_PARENT_GROWING

                        child_cell = self.spawn_cell( self.type, self.slot,
                                                      CELL_STATE_CHILD_GROWING )
                        child_cell["behavior"].set_target_slot( target_slot )
                        child_cell["behavior"].set_parent( self )
                    else:
                        # we couldn't grow because all neighbor slots are
                        # occupied.  reset the grow timeout and try to grow
                        # again later.
                        self.reset_grow_timeout()
                elif self.move_timeout <= 0:
                    # figure out which slots we can move to.
                    row, col  = self.slot
                    neighbors = self.grid.get_free_neighbors( row, col )

                    # do something only if we have a free slot.
                    if neighbors:
                        target_slot = renpy.random.choice( neighbors )
                        self.state  = CELL_STATE_MOVING
                        self.set_target_slot( target_slot )
                    else:
                        # we can't move because all neighbor slots are
                        # occupied.  reset the move timeout and try to move
                        # again later.
                        self.reset_move_timeout()
