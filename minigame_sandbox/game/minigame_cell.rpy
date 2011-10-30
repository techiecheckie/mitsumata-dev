init python:
    import itertools

    class CellLevel( object ):
        def __init__( self, ai_move_countdown, human_move_countdown ):
            self.ai_move_countdown    = ai_move_countdown
            self.human_move_countdown = human_move_countdown

    CELL_LEVELS = [
        CellLevel( ai_move_countdown    = (0.6, 0.85),
                   human_move_countdown = (0.7, 0.9) )
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

    # how fast a cell moves on either axis in pixels per second.
    CELL_SPEED = 70

    # static locations and dimensions.
    PETRI_DISH_X = 53
    PETRI_DISH_Y = 41

    GRID_CELL_WIDTH  = 48
    GRID_CELL_HEIGHT = 48

    NUMBER_GRID_ROWS = 11
    NUMBER_GRID_COLS = 11

    def convert_grid_cell( grid_cell ):
        x = grid_cell[1] * GRID_CELL_WIDTH + GRID_CELL_WIDTH / 2
        y = grid_cell[0] * GRID_CELL_HEIGHT + GRID_CELL_HEIGHT / 2
        return (x, y)

    class Cells( Minigame ):
        def __init__( self, level_number=1 ):
            super( Cells, self ).__init__()

            if level_number > len( CELL_LEVELS ) or level_number <= 0:
                raise ValueError( "Invalid Cell level number %d.  Level "
                                  "number must be between 1 and %d." %
                                  (level_number, len( CELL_LEVELS )) )

            # set up automated level difficulty parameters.
            level = CELL_LEVELS[level_number - 1]

            self.ai_move_countdown    = Randomizer( level.ai_move_countdown[0],
                                                    level.ai_move_countdown[1] )
            self.human_move_countdown = Randomizer( level.human_move_countdown[0],
                                                    level.human_move_countdown[1] )

            # setup entities.
            self.background      = None
            self.dish            = None
            self.human_cells     = []
            self.ai_cells        = []
            self.grid            = {}
            # self.available_cells = [                      (0,4), (0,5), (0,6),
            #                                 (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8),
            #                          (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8), (2,9),
            #                          (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9),
            #                          (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9),
            #                          (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9),
            #                          (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9),
            #                          (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9),
            #                          (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9),
            #                                 (9,2), (9,3), (9,4), (9,5), (9,6), (9,7), (9,8),
            #                                             (10,4), (10,5), (10,6) ]

            self.create_background()
            self.create_dish()
            self.create_cells()

            # build the grid of cells that game cells can roam on.
            self.build_grid()

            # XXX: remove me.
            self.spawn_cell( HUMAN_CELL_TYPE )
            self.spawn_cell( HUMAN_CELL_TYPE )
            self.spawn_cell( HUMAN_CELL_TYPE )
            self.spawn_cell( HUMAN_CELL_TYPE )

        def create_background( self ):
            self.background             = GameObject()
            self.background["renderer"] = GameRenderer( GameImage( "gfx/cells/background.png" ) )

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

        def build_grid( self ):
            for row in xrange( NUMBER_GRID_ROWS ):
                for col in xrange( NUMBER_GRID_COLS ):
                    self.grid[(row, col)] = GridCellState()

            # the following locations are outside the list of grid cells that
            # a game cell can occupy.
            self.grid[(0,0)].occupied  = True
            self.grid[(0,1)].occupied  = True
            self.grid[(0,2)].occupied  = True
            self.grid[(0,3)].occupied  = True
            self.grid[(0,7)].occupied  = True
            self.grid[(0,8)].occupied  = True
            self.grid[(0,9)].occupied  = True
            self.grid[(0,10)].occupied = True

            self.grid[(1,0)].occupied  = True
            self.grid[(1,1)].occupied  = True
            self.grid[(1,9)].occupied  = True
            self.grid[(1,10)].occupied = True

            self.grid[(2,0)].occupied  = True
            self.grid[(2,10)].occupied = True

            self.grid[(3,0)].occupied  = True
            self.grid[(3,10)].occupied = True

            self.grid[(4,0)].occupied  = True
            self.grid[(4,10)].occupied = True

            self.grid[(6,0)].occupied  = True
            self.grid[(6,10)].occupied = True

            self.grid[(7,0)].occupied  = True
            self.grid[(7,10)].occupied = True

            self.grid[(8,0)].occupied  = True
            self.grid[(8,10)].occupied = True

            self.grid[(9,0)].occupied  = True
            self.grid[(9,1)].occupied  = True
            self.grid[(9,9)].occupied  = True
            self.grid[(9,10)].occupied = True

            self.grid[(10,0)].occupied  = True
            self.grid[(10,1)].occupied  = True
            self.grid[(10,2)].occupied  = True
            self.grid[(10,3)].occupied  = True
            self.grid[(10,7)].occupied  = True
            self.grid[(10,8)].occupied  = True
            self.grid[(10,9)].occupied  = True
            self.grid[(10,10)].occupied = True

        def spawn_cell( self, cell_type ):
            available_cells = []

            # get all available cells.
            for grid_cell in self.grid:
                if not self.grid[grid_cell].occupied:
                    available_cells.append( grid_cell )

            # do we have any available cells?  if not, don't do anything.
            if not available_cells:
                return

            # get a random unoccupied cell and populate it.
            grid_cell        = renpy.random.choice( available_cells )
            cell             = PrefabFactory.instantiate( cell_type )
            cell["behavior"] = CellBehavior( self.grid,
                                             self.human_move_countdown
                                             if cell_type == HUMAN_CELL_TYPE
                                             else self.ai_move_countdown )
            cell["behavior"].set_grid_cell( grid_cell )
            cell["renderer"].play_animation( CELL_ANIMATION_PULSE )

            if cell_type == HUMAN_CELL_TYPE:
                self.human_cells.append( cell )
            else:
                self.ai_cells.append( cell )

        def get_displayables( self ):
            displayables = []
            displayables.extend( self.background["renderer"].get_displayables() )

            for cell in itertools.chain( self.human_cells, self.ai_cells ):
                displayables.extend( cell["renderer"].get_displayables() )

            displayables.extend( self.dish["renderer"].get_displayables() )

            return displayables

        def render( self, blitter ):
            world_transform = self.get_world_transform()
            self.background["renderer"].render( blitter, world_transform )

            cell_transform = world_transform + self.dish["transform"]
            for cell in itertools.chain( self.ai_cells, self.human_cells ):
                cell["renderer"].render( blitter, cell_transform )

            self.dish["renderer"].render( blitter, world_transform )

        def update( self, delta_sec ):
            # update all cells.
            for cell in itertools.chain( self.ai_cells, self.human_cells ):
                cell.update( delta_sec )

        def on_key_down( self, key ):
            if key == pygame.K_ESCAPE:
                self.quit()

    class CellBehavior( GameComponent ):
        def __init__( self, game_grid, move_countdown ):
            super( CellBehavior, self ).__init__()
            self.game_grid        = game_grid
            self.grid_cell        = None
            self.target_grid_cell = None
            self.move_countdown   = move_countdown
            self.move_timeout     = self.move_countdown.get_value()

        def move_to_grid_cell( self, grid_cell ):
            self.target_grid_cell              = grid_cell
            self.game_grid[grid_cell].occupied = True

        def set_grid_cell( self, grid_cell ):
            x, y = convert_grid_cell( grid_cell )
            self.game_object["transform"].set_position( x, y )
            self.grid_cell                     = grid_cell
            self.game_grid[grid_cell].occupied = True

        def update( self, delta_sec ):
            self.move_timeout -= delta_sec

            if self.target_grid_cell:
                tx, ty = convert_grid_cell( self.target_grid_cell )
                sx     = self.game_object["transform"].x
                sy     = self.game_object["transform"].y
                dx     = tx - sx
                dy     = ty - sy

                renpy.log( "Delta sec %s" % delta_sec )

                sx += sign( dx ) * delta_sec * CELL_SPEED
                sy += sign( dy ) * delta_sec * CELL_SPEED

                renpy.log( "Target: (%s, %s).  New place: (%s, %s)" %
                           (tx,ty,sx,sy) )

                if almost_equal( sx, tx ) and almost_equal( sy, ty ):
                    sx = tx
                    sy = ty
                    self.game_grid[self.grid_cell].occupied = False

                    self.grid_cell        = self.target_grid_cell
                    self.target_grid_cell = None
                    self.move_timeout     = self.move_countdown.get_value()
                    renpy.log( "Reached target.  Moving again in %s seconds" % self.move_timeout )

                self.game_object["transform"].set_position( sx, sy )
            elif self.move_timeout <= 0:
                renpy.log( "Moving" )
                # look in all directions and see if we can move to any of the cells.
                available_cells = []

                # cell to the left.
                row = max( 0, self.grid_cell[0] - 1 )
                col = self.grid_cell[1]
                if not self.game_grid[(row, col)].occupied:
                    available_cells.append( (row, col) )

                # cell to the right.
                row = min( NUMBER_GRID_ROWS - 1, self.grid_cell[0] + 1 )
                col = self.grid_cell[1]
                if not self.game_grid[(row, col)].occupied:
                    available_cells.append( (row, col) )

                # cell above.
                row = self.grid_cell[0]
                col = max( 0, self.grid_cell[1] - 1 )
                if not self.game_grid[(row, col)].occupied:
                    available_cells.append( (row, col) )

                # cell below.
                row = self.grid_cell[0]
                col = min( NUMBER_GRID_COLS - 1, self.grid_cell[1] + 1 )
                if not self.game_grid[(row, col)].occupied:
                    available_cells.append( (row, col) )

                # do something only if we don't have a free cell.
                if available_cells:
                    target_cell = renpy.random.choice( available_cells )
                    renpy.log( "Moving to %s" % (target_cell,) )
                    self.move_to_grid_cell( target_cell )
                else:
                    # we're not moving, so reset the move timeout and try
                    # moving again later.
                    self.move_timeout = self.move_countdown.get_value()
                    renpy.log( "Failed to move.  Moving again in %s seconds" % self.move_timeout )

    class GridCellState( object ):
        def __init__( self ):
            self.occupied = False
