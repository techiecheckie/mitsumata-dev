init python:
    import itertools
    import math

    class CellLevel( object ):
        def __init__( self, infected_idle_time, healthy_idle_time ):
            self.infected_idle_time = infected_idle_time
            self.healthy_idle_time  = healthy_idle_time

    CELL_LEVELS = [
        CellLevel( infected_idle_time = (0.6, 0.85),
                   healthy_idle_time  = (0.7, 0.9) )
        ]

    #### DESIGNERS: DO NOT CHANGE ANYTHING BEYOND THIS LINE ####

    # different states the Cells game can be in.
    CELLS_GAME_STATE_BEGIN = "cells_begin"
    CELLS_GAME_STATE_PLAY  = "cells_play"
    CELLS_GAME_STATE_END   = "cells_end"

    # timing stuff.
    CELLS_END_GAME_COUNTDOWN = 2.75

    # frameset names.
    HEALTHY_FRAMESET  = "healthy"
    INFECTED_FRAMESET = "infected"

    # animation names.
    CELL_ANIMATION_PULSE  = "pulse"
    CELL_ANIMATION_ATTACK = "attack"

    # animation durations.  these divided into the number of frames that are
    # in the corresponding animation are the frames per second value passed to
    # the GameAnimation constructor.
    CELL_ANIMATION_PULSE_DURATION  = 0.45
    CELL_ANIMATION_ATTACK_DURATION = 0.8

    # number of animation frames.
    NUMBER_CELL_PULSE_FRAMES  = 3
    NUMBER_CELL_ATTACK_FRAMES = 12

    # prefab names.
    CELL_TYPE = "cell"

    # cell types.
    HEALTHY_CELL_TYPE  = "healthy"
    INFECTED_CELL_TYPE = "infected"

    # how fast cells multiply.
    HEALTHY_GROWTH_RATE         = 0.7
    INFECTED_STAGE1_GROWTH_RATE = 0.5
    INFECTED_STAGE2_GROWTH_RATE = 0.3
    INFECTED_STAGE3_GROWTH_RATE = 0.1

    INFECTED_STAGE1_GROWTH_RATE_DURATION = 20
    INFECTED_STAGE2_GROWTH_RATE_DURATION = 40

    # how long an infection takes
    INFECT_DURATION        = 1.0
    NUMBER_INFECT_TOGGLES  = 15
    INFECT_TOGGLE_DURATION = INFECT_DURATION / NUMBER_INFECT_TOGGLES

    # how fast a cell moves on either axis in pixels per second.
    CELL_SPEED = 70

    # cell states.
    CELL_STATE_IDLE           = "idle"
    CELL_STATE_MOVING         = "moving"
    CELL_STATE_PARENT_GROWING = "parent_growing"
    CELL_STATE_CHILD_GROWING  = "child_growing"
    CELL_STATE_INFECTED       = "infected"
    CELL_STATE_INFECTING      = "infecting"
    CELL_STATE_RETRACTING     = "retracting"
    CELL_STATE_DYING          = "dying"

    # static locations and dimensions.
    PETRI_DISH_X = 17
    PETRI_DISH_Y = 0

    GRID_OFFSET_X = 52
    GRID_OFFSET_Y = 74

    GRID_CELL_WIDTH  = 48
    GRID_CELL_HEIGHT = 48

    CELL_COLLIDER_WIDTH  = 38
    CELL_COLLIDER_HEIGHT = 38

    NUMBER_GRID_ROWS = 9
    NUMBER_GRID_COLS = 10

    MAX_VALID_SLOTS = 68

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

        def get_cells( self, row, col ):
            index = col + row * NUMBER_GRID_COLS
            return self.slots[index].cells

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

        # non-infected neighbors are either free slots or slots that have
        # healthy cells in the idle state that are either to the left or right
        # of the given coordinate.  we make the rule that you can't infect
        # something that's currently completing an action (growing or moving).
        def get_noninfected_neighbors( self, row, col ):
            neighbors = []
            slots     = self.slots

            # up.
            if row > 0:
                up_row   = row - 1
                up_col   = col
                up_index = up_col + up_row * NUMBER_GRID_COLS
                if slots[up_index].is_valid:
                    for cell in slots[up_index].cells:
                        if (cell.type == INFECTED_CELL_TYPE or
                            cell.state != CELL_STATE_IDLE):
                            break
                    else:
                        neighbors.append( (up_row, up_col) )
#                if slots[up_index].is_valid and not slots[up_index].cells:
#                    neighbors.append( (up_row, up_col) )

            # right.
            if col < (NUMBER_GRID_COLS - 1):
                right_row   = row
                right_col   = col + 1
                right_index = right_col + right_row * NUMBER_GRID_COLS
                if slots[right_index].is_valid:
                    for cell in slots[right_index].cells:
                        if (cell.type == INFECTED_CELL_TYPE or
                            cell.state != CELL_STATE_IDLE):
                            break
                    else:
                        neighbors.append( (right_row, right_col) )

            # down.
            if row < (NUMBER_GRID_ROWS - 1):
                down_row   = row + 1
                down_col   = col
                down_index = down_col + down_row * NUMBER_GRID_COLS
                if slots[down_index].is_valid:
                    for cell in slots[down_index].cells:
                        if (cell.type == INFECTED_CELL_TYPE or
                            cell.state != CELL_STATE_IDLE):
                            break
                    else:
                        neighbors.append( (down_row, down_col) )
#                if slots[down_index].is_valid and not slots[down_index].cells:
#                    neighbors.append( (down_row, down_col) )

            # left.
            if col > 0:
                left_row   = row
                left_col   = col - 1
                left_index = left_col + left_row * NUMBER_GRID_COLS
                if slots[left_index].is_valid:
                    for cell in slots[left_index].cells:
                        if (cell.type == INFECTED_CELL_TYPE or
                            cell.state != CELL_STATE_IDLE):
                            break
                    else:
                        neighbors.append( (left_row, left_col) )

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

            self.infected_idle_time   = Randomizer( level.infected_idle_time[0],
                                                    level.infected_idle_time[1] )
            self.healthy_idle_time    = Randomizer( level.healthy_idle_time[0],
                                                    level.healthy_idle_time[1] )
            self.infected_growth_rate = StagedValue( [ (0,                                    INFECTED_STAGE1_GROWTH_RATE),
                                                       (INFECTED_STAGE1_GROWTH_RATE_DURATION, INFECTED_STAGE2_GROWTH_RATE),
                                                       (INFECTED_STAGE2_GROWTH_RATE_DURATION, INFECTED_STAGE3_GROWTH_RATE) ] )
            self.healthy_growth_rate  = StagedValue( [ (0, HEALTHY_GROWTH_RATE) ] )

            # setup game state.
            self.state         = CELLS_GAME_STATE_BEGIN
            self.elapsed_time  = 0
            self.end_countdown = CELLS_END_GAME_COUNTDOWN

            # setup entities.
            self.dish             = None
            self.healthy_cells    = []
            self.infected_cells   = []
            self.grid             = Grid()
            self.start_screen_hud = None
            self.stop_screen_hud  = None
            self.elapsed_time_hud = None

            self.create_dish()
            self.create_cells()
            self.create_huds()

            # XXX: remove me.
            self.spawn_cell( HEALTHY_CELL_TYPE )
            self.spawn_cell( INFECTED_CELL_TYPE )

        def create_dish( self ):
            self.dish             = GameObject()
            self.dish["renderer"] = GameRenderer( GameImage( "gfx/cells/petri_dish.png" ) )
            self.dish["transform"].set_position( PETRI_DISH_X, PETRI_DISH_Y )

        def create_cells( self ):
            pulse_animation = GameAnimation( frame_rate=(NUMBER_CELL_PULSE_FRAMES /
                                                         CELL_ANIMATION_PULSE_DURATION) )

            pulse_animation.set_frames( HEALTHY_FRAMESET,
                                        [ GameImage( "gfx/cells/human/cell-human-%d.png" % frame_index, Anchor.CENTER )
                                          for frame_index in xrange( NUMBER_CELL_PULSE_FRAMES ) ] )
            pulse_animation.set_frames( INFECTED_FRAMESET,
                                        [ GameImage( "gfx/cells/ai/cell-ai-%d.png" % frame_index, Anchor.CENTER )
                                          for frame_index in xrange( NUMBER_CELL_PULSE_FRAMES ) ] )

            cell             = GameObject()
            cell["renderer"] = GameRenderer()
            cell["collider"] = GameBoxCollider( Size( CELL_COLLIDER_WIDTH,
                                                      CELL_COLLIDER_HEIGHT ),
                                                Anchor.CENTER )
            cell["renderer"].add_animation( CELL_ANIMATION_PULSE, pulse_animation )
            cell["renderer"].add_animation( CELL_ANIMATION_ATTACK,
                                            GameAnimation( [ GameImage( "gfx/cells/ai/cell-ai-attack-%d.png" % frame_index, Anchor( 79, 77 ) )
                                                             for frame_index in xrange( NUMBER_CELL_ATTACK_FRAMES ) ],
                                                           NUMBER_CELL_ATTACK_FRAMES / CELL_ANIMATION_ATTACK_DURATION ) )
            cell["renderer"].set_collider_visible( False )
            PrefabFactory.add_prefab( CELL_TYPE, cell )

        def create_huds( self ):
            self.start_screen_hud             = GameObject()
            self.start_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/cells/start_screen.png" ) )
            self.start_screen_hud["transform"].set_position( 138, 50 )

            self.stop_screen_hud             = GameObject()
            self.stop_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/cells/stop_screen.png" ) )
            self.stop_screen_hud["transform"].set_position( 138, 50 )

            self.elapsed_time_hud             = GameObject()
            self.elapsed_time_hud["renderer"] = GameRenderer( GameText( self.get_elapsed_time ) )
            self.elapsed_time_hud["transform"].set_position( 10, 10 )

        def get_elapsed_time( self ):
            minutes = math.floor( self.elapsed_time / 60 )
            seconds = math.floor( self.elapsed_time - minutes * 60 )
            return "Elapsed Time: %d:%02d" % (minutes, seconds)

        def spawn_cell( self, cell_type, slot=None, state=None ):
            # if a slot wasn't given, get a random available one.  return
            # early if we can't get one.
            if not slot:
                slot = self.grid.get_free_slot()
                if not slot:
                    return

            # create the new cell.
            cell = PrefabFactory.instantiate( CELL_TYPE )

            # set the appropriate behavior depending on whether this is a
            # healthy or infected cell.
            if cell_type == HEALTHY_CELL_TYPE:
                cell["behavior"] = CellBehavior( cell_type,
                                                 self.grid,
                                                 self.healthy_idle_time,
                                                 self.healthy_growth_rate,
                                                 self.spawn_cell,
                                                 state )
                cell["renderer"].play_animation( CELL_ANIMATION_PULSE,
                                                 frameset=HEALTHY_FRAMESET )
                self.healthy_cells.append( cell )
            else:
                cell["behavior"] = CellBehavior( cell_type,
                                                 self.grid,
                                                 self.infected_idle_time,
                                                 self.infected_growth_rate,
                                                 self.spawn_cell,
                                                 state )
                cell["renderer"].play_animation( CELL_ANIMATION_PULSE,
                                                 frameset=INFECTED_FRAMESET )
                self.infected_cells.append( cell )

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

            return cell

        def get_displayables( self ):
            displayables = []
            for cell in itertools.chain( self.healthy_cells, self.infected_cells ):
                displayables.extend( cell["renderer"].get_displayables() )
            displayables.extend( self.dish["renderer"].get_displayables() )
            return displayables

        def render( self, blitter ):
            world_transform = self.get_world_transform()
            self.dish["renderer"].render( blitter, world_transform )

            if self.state == CELLS_GAME_STATE_BEGIN:
                self.start_screen_hud["renderer"].render( blitter, world_transform )
            elif self.state == CELLS_GAME_STATE_PLAY:
                cell_transform = GameTransform( world_transform.x +
                                                self.dish["transform"].x +
                                                GRID_OFFSET_X,
                                                world_transform.y +
                                                self.dish["transform"].y +
                                                GRID_OFFSET_Y )
                for cell in itertools.chain( self.infected_cells, self.healthy_cells ):
                    cell["renderer"].render( blitter, cell_transform )
            elif self.state == CELLS_GAME_STATE_END:
                self.stop_screen_hud["renderer"].render( blitter, world_transform )

            self.elapsed_time_hud["renderer"].render( blitter, world_transform )

        def update( self, delta_sec ):
            if self.state == CELLS_GAME_STATE_PLAY:
                self.elapsed_time += delta_sec

                # update the growth rate.
                self.infected_growth_rate.update( delta_sec )

                # update all cells.
                for cell in itertools.chain( self.infected_cells, self.healthy_cells ):
                    cell.update( delta_sec )

                # remove dead cells.
                self.healthy_cells[:]  = [ cell for cell in self.healthy_cells if cell.is_alive() ]
                self.infected_cells[:] = [ cell for cell in self.infected_cells if cell.is_alive() ]

                # healthy cells that have become infected need to be removed
                # from the healthy list and moved to the infected list.
                for cell in self.healthy_cells:
                    if cell["behavior"].type == INFECTED_CELL_TYPE:
                        self.infected_cells.append( cell )

                self.healthy_cells[:] = [ cell for cell in self.healthy_cells
                                          if cell["behavior"].type == HEALTHY_CELL_TYPE ]

                # see if it's game over.  add a little delay between detecting
                # the end game condition and the actual display of the final
                # score screen.
                if (len( self.healthy_cells ) == MAX_VALID_SLOTS or
                    len( self.healthy_cells ) == 0):
                    self.end_countdown -= delta_sec
                    if self.end_countdown <= 0:
                        self.state = CELLS_GAME_STATE_END

        def on_key_down( self, key ):
            if key == pygame.K_ESCAPE:
                self.quit()

        def on_mouse_up( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == CELLS_GAME_STATE_BEGIN:
                    self.state = CELLS_GAME_STATE_PLAY
                elif self.state == CELLS_GAME_STATE_END:
                    self.quit()

        def on_mouse_down( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == CELLS_GAME_STATE_PLAY:
                    # translate the mouse position to something that can be
                    # used to determine if the mouse is over a grid cell.
                    world_transform = self.get_world_transform()
                    x = mx - world_transform.x - self.dish["transform"].x - GRID_OFFSET_X
                    y = my - world_transform.y - self.dish["transform"].y - GRID_OFFSET_Y

                    for cell in itertools.chain( self.healthy_cells, self.infected_cells ):
                        if cell["collider"].is_point_inside( x, y ):
                            cell["behavior"].hit()
                            break

    class CellBehavior( GameComponent ):
        def __init__( self, cell_type, grid, idle_time, growth_rate,
                      spawn_cell, state=None ):
            super( CellBehavior, self ).__init__()
            self.state          = state or CELL_STATE_IDLE
            self.type           = cell_type
            self.grid           = grid
            self.slot           = None
            self.target_slot    = None
            self.parent         = None
            self.spawn_cell     = spawn_cell
            self.idle_time      = idle_time
            self.growth_rate    = growth_rate
            self.infect_timeout = 0
            self.move_timeout   = self.idle_time.get_value()
            self.grow_timeout   = self.growth_rate.get_value()

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
            at_target = False

            # get the appropriate target depending on whether we're retracting
            # or just moving/infecting.  if we're retracting, we're moving
            # back towards our original slot.
            if self.state == CELL_STATE_RETRACTING:
                target_row, target_col = self.slot
            else:
                target_row, target_col = self.target_slot

            # figure out which we have to go to reach our target and update
            # our position.
            tx, ty  = get_slot_position( target_row, target_col )
            sx      = self.game_object["transform"].x
            sy      = self.game_object["transform"].y

            # adjust our target if we're infecting.  in this case, we're
            # moving only halfway towards the target slot.
            if self.state == CELL_STATE_INFECTING:
                tx = (tx + sx) / 2
                ty = (ty + sy) / 2

            dx  = tx - sx
            dy  = ty - sy
            sx += sign( dx ) * delta_sec * CELL_SPEED
            sy += sign( dy ) * delta_sec * CELL_SPEED

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

        def infect( self, idle_time, growth_rate ):
            self.state          = CELL_STATE_INFECTED
            self.type           = INFECTED_CELL_TYPE
            self.idle_time      = idle_time
            self.growth_rate    = growth_rate
            self.infect_timeout = INFECT_DURATION

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
            #   * infecting
            #   * growing
            #   * chilling
            if self.state == CELL_STATE_DYING:
                if self.slot:
                    row, col = self.slot
                    self.grid.remove_cell( self, row, col )
                if self.target_slot:
                    row, col = self.target_slot
                    self.grid.remove_cell( self, row, col )
                self.game_object.kill()
            elif self.state == CELL_STATE_MOVING:
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
            elif self.state == CELL_STATE_INFECTING:
                pass
            elif self.state == CELL_STATE_RETRACTING:
                pass
            elif self.state == CELL_STATE_INFECTED:
                self.infect_timeout -= delta_sec

                # do a cheesy flash effect while we're being infected.
                toggle_number = math.trunc( self.infect_timeout / INFECT_TOGGLE_DURATION )

                if toggle_number % 2 == 0:
                    self.game_object["renderer"].set_animation_frameset( INFECTED_FRAMESET )
                else:
                    self.game_object["renderer"].set_animation_frameset( HEALTHY_FRAMESET )

                if self.infect_timeout <= 0:
                    self.game_object["renderer"].set_animation_frameset( INFECTED_FRAMESET )
                    self.state = CELL_STATE_IDLE
                    self.reset_move_timeout()
                    self.reset_grow_timeout()
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
                    # we do different things depending on whether we are a
                    # healthy or infected cell.
                    row, col  = self.slot

                    if self.type == HEALTHY_CELL_TYPE:
                        # healthy cells simply move to a free cell near them.
                        neighbors = self.grid.get_free_neighbors( row, col )

                        # do something only if we have a free slot.
                        if neighbors:
                            target_slot = renpy.random.choice( neighbors )
                            self.state  = CELL_STATE_MOVING
                            self.set_target_slot( target_slot )
                        else:
                            # we can't move because all neighbor slots are
                            # occupied.  reset the move timeout and try to
                            # move again later.
                            self.reset_move_timeout()
                    else:
                        # infected cells will either try to move to a free
                        # cell or infect a neighboring healthy cell.
                        neighbors = self.grid.get_noninfected_neighbors( row, col )

                        # do something only if we can move or infect.
                        if neighbors:
                            trow, tcol = renpy.random.choice( neighbors )
                            cells      = self.grid.get_cells( trow, tcol )

                            if cells:
                                # there should be EXACTLY one healthy cell in
                                # the target we picked.
                                cells[0].infect( self.idle_time, self.growth_rate )
                                cells[0].set_parent( self )
                                self.state = CELL_STATE_INFECTING
                                self.game_object["renderer"].play_animation( CELL_ANIMATION_ATTACK,
                                                                             loop_animation=False,
                                                                             on_animation_end=self.finish_infecting,
                                                                             frameset=GameAnimation.DEFAULT_FRAMESET )
                            else:
                                # we picked an empty slot.  just move to it
                                # like we would if we were healthy.
                                self.state = CELL_STATE_MOVING
                                self.set_target_slot( (trow, tcol) )
                        else:
                            # we can't move or infect because all neighbor
                            # slots are occupied by our friends.  reset the
                            # move timeout and try to move again later.
                            self.reset_move_timeout()

        def hit( self ):
            self.state = CELL_STATE_DYING

        def finish_infecting( self ):
            self.state = CELL_STATE_IDLE
            self.game_object["renderer"].play_animation( CELL_ANIMATION_PULSE,
                                                         frameset=INFECTED_FRAMESET )
            self.reset_move_timeout()
