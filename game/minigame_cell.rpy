init python:
    import itertools
    import math

    class CellLevel( object ):
        def __init__( self, initial_healthy, mutation_probability, 
                            duplication_probability, mutation_cooldown, 
                            mutation_duration, cell_action_timeout, 
                            post_mutation_timeout, level_number ):
            self.initial_healthy         = initial_healthy
            self.mutation_probability    = mutation_probability
            self.duplication_probability = duplication_probability
            self.mutation_cooldown      = mutation_cooldown
            self.mutation_duration       = mutation_duration
            self.cell_action_timeout     = cell_action_timeout
            self.post_mutation_timeout   = post_mutation_timeout
            self.level_number            = level_number

    # Level settings definitions for the Cells minigame:
    #
    #    initial_healthy         - Number of cells in the beginning.
    #
    #    mutation_probability    - How likely it is for a cell to start mutating.
    #                              Mutation happens spontaneously, but only if 
    #                              the amount of healthy cells is more than
    #                              MIN_HEALTHY_CELLS. This is to prevent the few
    #                              existing cells from mutating right in the 
    #                              beginning of the game.
    #
    #    duplication_propability - How likely it is for a cell to start creating
    #                              duplicates of itself. The created duplicates
    #                              are always of the same level as the one being
    #                              duplicated.
    #
    #    mutation_cooldown       - The amount of time in seconds that must pass 
    #                              before the next spontaneous mutation can happen. 
    #                              Setting this too low results in blood and tears
    #                              as the dish fills with infected cells faster
    #                              than you can kill them.
    #
    #    mutation_duration       - How long the mutation phase lasts (in seconds).
    #
    #    cell_action_timeout     - How long the cell stays idle after performing
    #                              an action such as moving or infecting.
    #
    #    post_mutation_timeout   - How long the cell stays idle after the mutation
    #                              completes. Settings this to zero results in
    #                              wild, highly uncontrollable mutation waves.
    CELL_LEVELS = [
        CellLevel( initial_healthy         = 3,
                   mutation_probability    = 10,
                   duplication_probability = 50,
                   mutation_cooldown       = 2,
                   mutation_duration       = 2,
                   cell_action_timeout     = 2,
                   post_mutation_timeout   = 0.5,
                   level_number            = 1 ),
                   
        CellLevel( initial_healthy         = 3,
                   mutation_probability    = 20,
                   duplication_probability = 50,
                   mutation_cooldown       = 2,
                   mutation_duration       = 2,
                   cell_action_timeout     = 2,
                   post_mutation_timeout   = 0.5,
                   level_number            = 2 ),
        
        CellLevel( initial_healthy         = 4,
                   mutation_probability    = 30,
                   duplication_probability = 50,
                   mutation_cooldown       = 2,
                   mutation_duration       = 2,
                   cell_action_timeout     = 2,
                   post_mutation_timeout   = 0.5,
                   level_number            = 3 ),
                   
        CellLevel( initial_healthy         = 4,
                   mutation_probability    = 30,
                   duplication_probability = 50,
                   mutation_cooldown       = 1,
                   mutation_duration       = 2,
                   cell_action_timeout     = 2,
                   post_mutation_timeout   = 0.2,
                   level_number            = 4 ),
        ]
        
    CELLS_HIT_POINTS_HEALTHY = 1
    CELLS_HIT_POINTS_EASY    = 1
    CELLS_HIT_POINTS_MEDIUM  = 3
    CELLS_HIT_POINTS_HARD    = 5
    
    CELLS_SCORE_HEALTHY = -100
    CELLS_SCORE_EASY    = 100
    CELLS_SCORE_MEDIUM  = 250
    CELLS_SCORE_HARD    = 500
    
    CELLS_COMPLETION_BONUS = 1000

    #### DESIGNERS: DO NOT CHANGE ANYTHING BEYOND THIS LINE ####
    
    # prefab names.
    CELL_TYPE = "cell"
    
    # cell types.
    CELLS_TYPE_HEALTHY = 1
    CELLS_TYPE_EASY    = 2
    CELLS_TYPE_MEDIUM  = 3
    CELLS_TYPE_HARD    = 4
    
    # property dict keys
    CELLS_PROP_HIT_POINTS = 1
    CELLS_PROP_FRAMESET   = 2
    CELLS_PROP_SCORE      = 3
    CELLS_PROP_MUTATES_TO = 4
        
    CELLS_PROPERTIES = {
        CELLS_TYPE_HEALTHY : {
            CELLS_PROP_HIT_POINTS : CELLS_HIT_POINTS_HEALTHY,
            CELLS_PROP_SCORE      : CELLS_SCORE_HEALTHY,
            CELLS_PROP_FRAMESET   : 1,
            CELLS_PROP_MUTATES_TO : CELLS_TYPE_EASY
        },
        
        CELLS_TYPE_EASY : {
            CELLS_PROP_HIT_POINTS : CELLS_HIT_POINTS_EASY,
            CELLS_PROP_SCORE      : CELLS_SCORE_EASY,
            CELLS_PROP_FRAMESET   : 2,
            CELLS_PROP_MUTATES_TO : CELLS_TYPE_MEDIUM
        },
        
        CELLS_TYPE_MEDIUM : {
            CELLS_PROP_HIT_POINTS : CELLS_HIT_POINTS_MEDIUM,
            CELLS_PROP_SCORE      : CELLS_SCORE_MEDIUM,
            CELLS_PROP_FRAMESET   : 3,
            CELLS_PROP_MUTATES_TO : CELLS_TYPE_HARD
        },
        
        CELLS_TYPE_HARD : {
            CELLS_PROP_HIT_POINTS : CELLS_HIT_POINTS_HARD,
            CELLS_PROP_SCORE      : CELLS_SCORE_HARD,
            CELLS_PROP_FRAMESET   : 4,
            CELLS_PROP_MUTATES_TO : None
        }
    }

    # different states the Cells game can be in.
    CELLS_GAME_STATE_BEGIN = 1
    CELLS_GAME_STATE_PLAY  = 2
    CELLS_GAME_STATE_WAIT  = 3
    CELLS_GAME_STATE_END   = 4
    CELLS_GAME_STATE_PAUSE = 5

    # how long the game waits before the end screen is shown
    CELLS_END_GAME_COUNTDOWN = 2.75

    # animation names.
    CELL_ANIMATION_PULSE  = 1
    CELL_ANIMATION_ATTACK = 2

    # animation durations.  these divided into the number of frames that are
    # in the corresponding animation are the frames per second value passed to
    # the GameAnimation constructor.
    CELL_ANIMATION_PULSE_DURATION  = 0.45
    CELL_ANIMATION_ATTACK_DURATION = 0.8

    # number of animation frames.
    NUMBER_CELL_PULSE_FRAMES  = 3
    NUMBER_CELL_ATTACK_FRAMES = 12

    # how long an infection animation flash phase takes
    INFECT_TOGGLE_DURATION = 0.1

    # cell states.
    CELL_STATE_IDLE           = 1
    CELL_STATE_MOVING         = 2
    CELL_STATE_INFECTING      = 3
    CELL_STATE_DYING          = 4
    CELL_STATE_MUTATING       = 5

    # static locations and dimensions.
    PETRI_DISH_X = 17
    PETRI_DISH_Y = 0

    GRID_OFFSET_X = 82
    GRID_OFFSET_Y = 104

    GRID_CELL_WIDTH  = 48
    GRID_CELL_HEIGHT = 48

    CELL_COLLIDER_WIDTH  = 45
    CELL_COLLIDER_HEIGHT = 45

    CELLS_GRID_ROWS = 9
    CELLS_GRID_COLS = 10

    CELLS_MAX_VALID_SLOTS = 67
    
    # The minimum amount of healthy cells before spontaneous mutation can happen
    MIN_HEALTHY_CELLS = 3


    class GridSlot( object ):
        def __init__( self, x, y ):
            self.x = x
            self.y = y
            self.is_valid = True
            self.cells    = []
            
        def get_position( self ):
            return self.x, self.y


    class Grid( object ):
        def __init__( self ):
            self.slots = []
            for y in xrange(CELLS_GRID_ROWS):
                for x in range(CELLS_GRID_COLS):
                    self.slots.append(GridSlot(x,y))

            invalid_locations = [ (0,0), (0,1), (0,2), (0,7), (0,8), (0,9),
                                  (1,0), (1,1), (1,8), (1,9),
                                  (2,0), (2,9),
                                  (3,0),
                                  (6,0), (6,9),
                                  (7,0), (7,1), (7,9),
                                  (8,0), (8,1), (8,2), (8,8), (8,9) ]

            for row, col in invalid_locations:
                index = col + row * CELLS_GRID_COLS
                self.slots[index].is_valid = False
                self.slots[index].cells = None

        def get_free_neighbors( self, slot ):
            neighbors = []
            slots     = self.slots
            col, row  = slot.get_position()

            # up.
            if row > 0:
                up_row   = row - 1
                up_col   = col
                up_index = up_col + up_row * CELLS_GRID_COLS
                if slots[up_index].is_valid and not slots[up_index].cells:
                    neighbors.append( slots[up_index] )

            # right.
            if col < (CELLS_GRID_COLS - 1):
                right_row   = row
                right_col   = col + 1
                right_index = right_col + right_row * CELLS_GRID_COLS
                if slots[right_index].is_valid and not slots[right_index].cells:
                    neighbors.append( slots[right_index] )

            # down.
            if row < (CELLS_GRID_ROWS - 1):
                down_row   = row + 1
                down_col   = col
                down_index = down_col + down_row * CELLS_GRID_COLS
                if slots[down_index].is_valid and not slots[down_index].cells:
                    neighbors.append( slots[down_index] )

            # left.
            if col > 0:
                left_row   = row
                left_col   = col - 1
                left_index = left_col + left_row * CELLS_GRID_COLS
                if slots[left_index].is_valid and not slots[left_index].cells:
                    neighbors.append( slots[left_index] )

            return neighbors

        # non-infected neighbors are either free slots or slots that have
        # healthy cells in the idle state that are either to the left or right
        # of the given coordinate.  we make the rule that you can't infect
        # something that's currently completing an action (growing or moving).
        def get_noninfected_neighbors( self, slot ):
            neighbors = []
            slots     = self.slots
            col, row  = slot.get_position()

            # up.
            if row > 0:
                up_row   = row - 1
                up_col   = col
                up_index = up_col + up_row * CELLS_GRID_COLS
                if slots[up_index].is_valid:
                    for cell in slots[up_index].cells:
                        if not cell.is_infectable():
                            break
                    else:
                        neighbors.append( slots[up_index] )

            # right.
            if col < (CELLS_GRID_COLS - 1):
                right_row   = row
                right_col   = col + 1
                right_index = right_col + right_row * CELLS_GRID_COLS
                if slots[right_index].is_valid:
                    for cell in slots[right_index].cells:
                        if not cell.is_infectable():
                            break
                    else:
                        neighbors.append( slots[right_index] )

            # down.
            if row < (CELLS_GRID_ROWS - 1):
                down_row   = row + 1
                down_col   = col
                down_index = down_col + down_row * CELLS_GRID_COLS
                if slots[down_index].is_valid:
                    for cell in slots[down_index].cells:
                        if not cell.is_infectable():
                            break
                    else:
                        neighbors.append( slots[down_index] )

            # left.
            if col > 0:
                left_row   = row
                left_col   = col - 1
                left_index = left_col + left_row * CELLS_GRID_COLS
                if slots[left_index].is_valid:
                    for cell in slots[left_index].cells:
                        if not cell.is_infectable():
                            break
                    else:
                        neighbors.append( slots[left_index] )

            return neighbors

        def get_free_slot( self ):
            # "Try x times, then..." <-- not nice, but it usually does the trick here.
            for i in xrange(0, 10):
                slot = random.choice( self.slots )
                if slot.is_valid and (slot.cells == None or len(slot.cells) == 0):
                    return slot
            renpy.log("Cells warning: couldn't find a free slot!")
            return None


    class Cells( Minigame ):
        def __init__( self, level_number=1 ):
            super( Cells, self ).__init__()

            if level_number > len( CELL_LEVELS ) or level_number <= 0:
                raise ValueError( "Invalid Cell level number %d.  Level "
                                  "number must be between 1 and %d." %
                                  (level_number, len( CELL_LEVELS )) )

            # set up automated level difficulty parameters.
            self.level = CELL_LEVELS[level_number - 1]

            # setup game state.
            self.state            = CELLS_GAME_STATE_BEGIN
            self.elapsed_time     = 0
            self.completion_bonus = 0
            self.total_score      = 0
            self.end_countdown    = CELLS_END_GAME_COUNTDOWN

            # setup entities.
            self.active_cells       = []
            self.removables         = []
            self.healthy_cells      = 0
            self.mutating_cells     = 0
            self.mutation_cooldown  = 0
            self.grid               = Grid()
            self.start_screen_hud   = None
            self.stop_screen_hud    = None
            self.elapsed_time_hud   = None
            self.instructions       = None
            self.instructions_index = 0

            self.create_cells()
            self.create_huds()
            
            self.mouse_click_x = -1
            self.mouse_click_y = -1
            self.mouse_clicked = False
            
            self.cell_hits = {
                CELLS_TYPE_HEALTHY : 0,
                CELLS_TYPE_EASY    : 0,
                CELLS_TYPE_MEDIUM  : 0,
                CELLS_TYPE_HARD    : 0
            }
            self.cell_hits_count = 0

            # spawn the initial cells.
            for i in xrange( self.level.initial_healthy ):
                self.spawn_cell( CELLS_TYPE_HEALTHY )

        def create_cells( self ):
            pulse_animation = GameAnimation( frame_rate=(NUMBER_CELL_PULSE_FRAMES /
                                                         CELL_ANIMATION_PULSE_DURATION) )

            pulse_animation.set_frames( CELLS_PROPERTIES[CELLS_TYPE_HEALTHY][CELLS_PROP_FRAMESET],
                                        [ GameImage( "gfx/cells/human/cell-human-%d.png" % frame_index, Anchor.CENTER )
                                          for frame_index in xrange( NUMBER_CELL_PULSE_FRAMES ) ] )
            pulse_animation.set_frames( CELLS_PROPERTIES[CELLS_TYPE_EASY][CELLS_PROP_FRAMESET],
                                        [ GameImage( "gfx/cells/ai/cell-ai-%d-easy.png" % frame_index, Anchor.CENTER )
                                          for frame_index in xrange( NUMBER_CELL_PULSE_FRAMES ) ] )
            pulse_animation.set_frames( CELLS_PROPERTIES[CELLS_TYPE_MEDIUM][CELLS_PROP_FRAMESET],
                                        [ GameImage( "gfx/cells/ai/cell-ai-%d-medium.png" % frame_index, Anchor.CENTER )
                                          for frame_index in xrange( NUMBER_CELL_PULSE_FRAMES ) ] )
            pulse_animation.set_frames( CELLS_PROPERTIES[CELLS_TYPE_HARD][CELLS_PROP_FRAMESET],
                                        [ GameImage( "gfx/cells/ai/cell-ai-%d-hard.png" % frame_index, Anchor.CENTER )
                                          for frame_index in xrange( NUMBER_CELL_PULSE_FRAMES ) ] )

            attack_animation = GameAnimation( frame_rate=(NUMBER_CELL_ATTACK_FRAMES /
                                                          CELL_ANIMATION_ATTACK_DURATION) )

            attack_animation.set_frames( CELLS_PROPERTIES[CELLS_TYPE_EASY][CELLS_PROP_FRAMESET],
                                         [ GameImage( "gfx/cells/ai/cell-ai-attack-%d-easy.png" % frame_index, Anchor( 79, 77 ) )
                                           for frame_index in xrange( NUMBER_CELL_ATTACK_FRAMES ) ] )
            attack_animation.set_frames( CELLS_PROPERTIES[CELLS_TYPE_MEDIUM][CELLS_PROP_FRAMESET],
                                         [ GameImage( "gfx/cells/ai/cell-ai-attack-%d-medium.png" % frame_index, Anchor( 79, 77 ) )
                                           for frame_index in xrange( NUMBER_CELL_ATTACK_FRAMES ) ] )
            attack_animation.set_frames( CELLS_PROPERTIES[CELLS_TYPE_HARD][CELLS_PROP_FRAMESET],
                                         [ GameImage( "gfx/cells/ai/cell-ai-attack-%d-hard.png" % frame_index, Anchor( 79, 77 ) )
                                           for frame_index in xrange( NUMBER_CELL_ATTACK_FRAMES ) ] )

            cell             = GameObject()
            cell["renderer"] = GameRenderer()
            cell["collider"] = GameBoxCollider( Size( CELL_COLLIDER_WIDTH,
                                                      CELL_COLLIDER_HEIGHT ),
                                                Anchor.CENTER )
            cell["renderer"].add_animation( CELL_ANIMATION_PULSE, pulse_animation )
            cell["renderer"].add_animation( CELL_ANIMATION_ATTACK, attack_animation )
            cell["renderer"].set_collider_visible( False )
            PrefabFactory.add_prefab( CELL_TYPE, cell )

        def create_huds( self ):
            self.start_screen_hud             = GameObject()
            self.start_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/cells/start_screen.png" ) )
            self.start_screen_hud["transform"].set_position( 148, 50 )

            self.stop_screen_hud             = GameObject()
            self.stop_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/cells/stop_screen.png" ) )
            self.stop_screen_hud["transform"].set_position( 148, 50 )
            
            instructions_1 = GameObject()
            instructions_1["renderer"] = GameRenderer( GameImage( "gfx/cells/instructions_1.png" ) )
            instructions_1["transform"].set_position( 148, 50 )
            instructions_2 = GameObject()
            instructions_2["renderer"] = GameRenderer( GameImage( "gfx/cells/instructions_2.png" ) )
            instructions_2["transform"].set_position( 148, 50 )
            self.instructions = [instructions_1, instructions_2]
            
            high_score = GameObject()
            high_score["renderer"] = GameRenderer( GameText( self.get_high_score, Color( 255, 255, 255, 255 ) ) )
            high_score["transform"].set_position( 138, 313 )
            self.start_screen_hud.add_child( high_score )

            level = GameObject()
            level["renderer"] = GameRenderer( GameText( self.get_level_number, Color( 255, 255, 255, 255 ) ) )
            level["transform"].set_position( 138, 360 )
            self.start_screen_hud.add_child( level )
            
            cell_hits = GameObject()
            cell_hits["renderer"] = GameRenderer( GameText( self.get_cell_hit_count, Color( 255, 255, 255, 255 ) ) )
            cell_hits["transform"].set_position( 135, 114 )
            self.stop_screen_hud.add_child( cell_hits )
            
            easy_cell_hits = GameObject()
            easy_cell_hits["renderer"] = GameRenderer( GameText( self.get_easy_cell_hit_count, Color( 255, 255, 255, 255 ) ) )
            easy_cell_hits["transform"].set_position( 195, 161 )
            self.stop_screen_hud.add_child( easy_cell_hits )
            
            medium_cell_hits = GameObject()
            medium_cell_hits["renderer"] = GameRenderer( GameText( self.get_medium_cell_hit_count, Color( 255, 255, 255, 255 ) ) )
            medium_cell_hits["transform"].set_position( 195, 184 )
            self.stop_screen_hud.add_child( medium_cell_hits )
            
            hard_cell_hits = GameObject()
            hard_cell_hits["renderer"] = GameRenderer( GameText( self.get_hard_cell_hit_count, Color( 255, 255, 255, 255 ) ) )
            hard_cell_hits["transform"].set_position( 195, 207 )
            self.stop_screen_hud.add_child( hard_cell_hits )
            
            healthy_cell_hits = GameObject()
            healthy_cell_hits["renderer"] = GameRenderer( GameText( self.get_healthy_cell_hit_count, Color( 255, 255, 255, 255 ) ) )
            healthy_cell_hits["transform"].set_position( 195, 230 )
            self.stop_screen_hud.add_child( healthy_cell_hits )

            completion_bonus             = GameObject()
            completion_bonus["renderer"] = GameRenderer( GameText( self.get_completion_bonus, Color( 255, 255, 255, 255 ) ) )
            completion_bonus["transform"].set_position( 135, 323 )
            self.stop_screen_hud.add_child( completion_bonus )

            total_score             = GameObject()
            total_score["renderer"] = GameRenderer( GameText( self.get_total_score, Color( 255, 255, 255, 255 ) ) )
            total_score["transform"].set_position( 135, 369 )
            self.stop_screen_hud.add_child( total_score )

            self.elapsed_time_hud             = GameObject()
            self.elapsed_time_hud["renderer"] = GameRenderer( GameText( self.get_elapsed_time, Color( 255, 255, 255, 255 ) ) )
            self.elapsed_time_hud["transform"].set_position( 30, 30 )

        def compute_scores( self ):
            if self.healthy_cells > 0:
                self.completion_bonus = CELLS_COMPLETION_BONUS
            else:
                self.completion_bonus = 0
                
            base_score = 0
            base_score += self.cell_hits[CELLS_TYPE_EASY]    * CELLS_SCORE_EASY
            base_score += self.cell_hits[CELLS_TYPE_MEDIUM]  * CELLS_SCORE_MEDIUM
            base_score += self.cell_hits[CELLS_TYPE_HARD]    * CELLS_SCORE_HARD
            base_score += self.cell_hits[CELLS_TYPE_HEALTHY] * CELLS_SCORE_HEALTHY
                
            self.total_score = base_score + self.completion_bonus
            
        def get_cell_hit_count( self ):
            return "%20d" % self.cell_hits_count
            
        def get_hits_string( self, cell_type, score ):
            return "%2d  (%4d pts)" % ( self.cell_hits[cell_type], score )
            
        def get_easy_cell_hit_count( self ):
            return self.get_hits_string( CELLS_TYPE_EASY, CELLS_SCORE_EASY )
             
        def get_medium_cell_hit_count( self ):
            return self.get_hits_string( CELLS_TYPE_MEDIUM, CELLS_SCORE_MEDIUM )
            
        def get_hard_cell_hit_count( self ):
            return self.get_hits_string( CELLS_TYPE_HARD, CELLS_SCORE_HARD )
            
        def get_healthy_cell_hit_count( self ):
            return self.get_hits_string( CELLS_TYPE_HEALTHY, CELLS_SCORE_HEALTHY )

        def get_completion_bonus( self ):
            return "%20d" % self.completion_bonus

        def get_total_score( self ):
            return "%20d" % self.total_score

        def get_elapsed_time( self ):
            minutes = math.floor( self.elapsed_time / 60 )
            seconds = math.floor( self.elapsed_time - minutes * 60 )
            return "Elapsed Time: %d:%02d" % (minutes, seconds)
            
        def get_level_number( self ):
            return "%20d" % self.level.level_number

        def spawn_cell( self, cell_type, slot=None):
            # if a slot wasn't given, get a random available one.  return
            # early if we can't get one.
            if slot == None:
                slot = self.grid.get_free_slot()
                if not slot:
                    return

            # create the new cell.
            cell = PrefabFactory.instantiate( CELL_TYPE )                    

            # set the appropriate behavior depending on whether this is a
            # healthy or infected cell.
            cell_properties = CELLS_PROPERTIES[cell_type]
            hit_points      = cell_properties[CELLS_PROP_HIT_POINTS]
            frameset        = cell_properties[CELLS_PROP_FRAMESET]
            
            if cell_type == CELLS_TYPE_HEALTHY:
                self.inc_healthy_cell_count(1)
            
            cell["behavior"] = CellBehavior( self, cell_type, hit_points, CELL_STATE_IDLE)
            cell["behavior"].slot = slot
            cell["transform"].set_position(
                slot.x * GRID_CELL_WIDTH + GRID_CELL_WIDTH / 2,
                slot.y * GRID_CELL_HEIGHT + GRID_CELL_HEIGHT / 2)
            cell["renderer"].play_animation( CELL_ANIMATION_PULSE, frameset=frameset )

            slot.cells.append( cell["behavior"] )

            self.active_cells.append( cell )

            return cell

        def get_displayables( self ):
            displayables = []
            
            displayables.extend( self.start_screen_hud["renderer"].get_displayables() )
            displayables.extend( self.stop_screen_hud["renderer"].get_displayables() )
            displayables.extend( self.elapsed_time_hud["renderer"].get_displayables() )
            
            for instruction in self.instructions:
                displayables.extend( instruction["renderer"].get_displayables() )
            
            return displayables

        def render( self, blitter, clip_rect ):
            world_transform = self.get_world_transform()

            if self.state == CELLS_GAME_STATE_BEGIN:
                self.start_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == CELLS_GAME_STATE_END:
                self.stop_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            else:
                cell_transform = GameTransform( world_transform.x +
                                                GRID_OFFSET_X,
                                                world_transform.y +
                                                GRID_OFFSET_Y )
                for cell in self.active_cells:
                    cell["renderer"].render( blitter, clip_rect, cell_transform )

                if self.state == CELLS_GAME_STATE_PAUSE:
                    self.instructions[self.instructions_index]["renderer"].render( blitter, clip_rect, world_transform )
                else:
                    self.elapsed_time_hud["renderer"].render( blitter, clip_rect, world_transform )

        def update( self, delta_sec ):
            if self.state == CELLS_GAME_STATE_PLAY:
                self.elapsed_time += delta_sec
                
                if self.mutation_cooldown > 0:
                    self.mutation_cooldown -= delta_sec
                
                # update all cells.
                for cell in self.active_cells:
                    # Perform appropriate collision checks if necessary.
                    if self.mouse_clicked and cell["collider"].is_point_inside(self.mouse_click_x, self.mouse_click_y):
                        cell["behavior"].hit()
                        if cell["behavior"].hit_points <= 0:
                            self.inc_hits( cell["behavior"] )
                            self.removables.append( cell )
                            cell["behavior"].die()
                        self.mouse_clicked = False
                    
                    cell.update( delta_sec )
                
                # Remove any dead cells.
                if len(self.removables) > 0:
                    for removable in self.removables:
                        self.active_cells.remove(removable)
                        
                    del self.removables[:]
                    
                # Reset mouse to make sure the event is consumed during this update.
                self.mouse_clicked = False

                # see if it's game over.  add a little delay between detecting
                # the end game condition and the actual display of the final
                # score screen.                
                if self.healthy_cells == CELLS_MAX_VALID_SLOTS or self.healthy_cells == 0:
                    self.end_countdown -= delta_sec
                    if self.end_countdown <= 0:
                        self.compute_scores()
                        self.state = CELLS_GAME_STATE_END

        def on_key_down( self, key ):
            if key == pygame.K_h:
                self.state = CELLS_GAME_STATE_PAUSE

        def on_mouse_up( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == CELLS_GAME_STATE_BEGIN:
                    self.state = CELLS_GAME_STATE_PLAY
                elif self.state == CELLS_GAME_STATE_END:
                    self.quit()
                elif self.state == CELLS_GAME_STATE_PAUSE:
                    if self.instructions_index < len(self.instructions)-1:
                        self.instructions_index += 1
                    else:
                        self.instructions_index = 0
                        self.state = CELLS_GAME_STATE_PLAY

        def on_mouse_down( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == CELLS_GAME_STATE_PLAY:
                    # translate the mouse position to something that can be
                    # used to determine if the mouse is over a grid cell.
                    world_transform = self.get_world_transform()
                    self.mouse_click_x = mx - world_transform.x - GRID_OFFSET_X
                    self.mouse_click_y = my - world_transform.y - GRID_OFFSET_Y
                    self.mouse_clicked = True
            
        def inc_healthy_cell_count( self, value ):
            self.healthy_cells += value
            
        def inc_mutating_cell_count( self, value ):
            self.mutating_cells += value
            self.mutation_cooldown = self.level.mutation_cooldown
        
        def can_mutate( self ):
            # Allow spontaneous mutation only if there are more than MIN_HEALTHY_CELLS
            # (to make sure the few starting cells won't mutate right in the beginning)
            # and if enough time has passed since the previous mutation (prevents
            # simultaneos mutation waves from happening). The last part makes sure
            # no mutations happen once the end conditions have been met and the 
            # counter has started to run.
            return (self.healthy_cells > MIN_HEALTHY_CELLS and 
                    self.mutation_cooldown <= 0 and 
                    self.end_countdown == CELLS_END_GAME_COUNTDOWN)
        
        def inc_hits( self, cell ):
            if cell.state == CELL_STATE_MUTATING:
                cell_type = CELLS_PROPERTIES[cell.type][CELLS_PROP_MUTATES_TO]
            else:
                cell_type = cell.type

            self.cell_hits[cell_type] += 1
            self.cell_hits_count      += 1


    class CellBehavior( GameComponent ):
        def __init__( self, main, cell_type, number_hit_points, state=None):
            super( CellBehavior, self ).__init__()
            self.state                = state or CELL_STATE_IDLE
            self.type                 = cell_type
            self.hit_points           = number_hit_points
            self.slot                 = None
            self.target_slot          = None
            self.grid                 = main.grid
            self.spawn_cell           = main.spawn_cell
            self.can_mutate           = main.can_mutate
            self.level                = main.level
            self.inc_mutating_cell_count = main.inc_mutating_cell_count
            self.inc_healthy_cell_count  = main.inc_healthy_cell_count

            self.timeout_counter = 0
            self.reset_timeout_counter( self.level.cell_action_timeout )
            
            # Sprite transformation variables
            self.vx = 0
            self.vy = 0
            self.dx = 0
            self.dy = 0

        def reset_timeout_counter( self, timeout ):
            self.timeout_counter = timeout

        def set_target_slot( self, target_slot ):
            # target slots get flagged as occupied in the grid so that no
            # other cell tries to move into it.
            self.target_slot = target_slot
            self.target_slot.cells.append( self )
            
            x1, y1 = self.slot.get_position()
            x2, y2 = self.target_slot.get_position()
            
            self.vx = x2 - x1
            self.vy = y2 - y1
            self.dx = 0
            self.dy = 0
                            
            self.state  = CELL_STATE_MOVING

        # A cell can
        #     1) mutate spontaneously (if type is below CELL_TYPE_HARD),
        #     2) create a duplicate of itself,
        #     3) infect neighbors, or
        #     4) move (if any space).
        # The selected action depends on what the probabilities are and what the
        # randomizer spits out in the beginning of each idle state update.
        def update( self, delta_sec ):
            if self.state == CELL_STATE_IDLE:
                if self.timeout_counter > 0:
                    self.timeout_counter -= delta_sec
                    return
                
                rand_value = random.randint(0, 100)
                
                if rand_value <= self.level.mutation_probability and self.can_mutate():
                    if self.type != CELLS_TYPE_HARD:
                        self.state = CELL_STATE_MUTATING
                        self.timeout_counter = self.level.mutation_duration
                        self.inc_mutating_cell_count(1)
                        
                elif rand_value <= self.level.duplication_probability:
                    # figure out which slots we can grow into.
                    neighbors = self.grid.get_free_neighbors( self.slot )

                    # Duplicate only if we have a free slot.
                    if neighbors:
                        target_slot = renpy.random.choice( neighbors )

                        child_cell = self.spawn_cell( self.type, self.slot )
                        child_cell["behavior"].set_target_slot( target_slot )
                        self.reset_timeout_counter( self.level.cell_action_timeout )
                        
                else:
                    # Infected cells try to infect their neighbors by default, but
                    # if none available they just move around like healthy cells do.
                    if self.type != CELLS_TYPE_HEALTHY:
                        neighbors = self.grid.get_noninfected_neighbors( self.slot )
                        if neighbors:
                            target_slot = renpy.random.choice( neighbors )
                            target_cells = target_slot.cells
                            if len(target_cells) > 0:
                                target_cells[0].state = CELL_STATE_MUTATING
                                target_cells[0].timeout_counter = self.level.mutation_duration
                                
                                self.game_object["renderer"].play_animation( CELL_ANIMATION_ATTACK,
                                                                             loop_animation=False,
                                                                             on_animation_end=self.finish_infecting,
                                                                             frameset=CELLS_PROPERTIES[self.type][CELLS_PROP_FRAMESET] )
                                self.state = CELL_STATE_INFECTING
                                return

                    # healthy cells simply move to a free cell near them.
                    neighbors = self.grid.get_free_neighbors( self.slot )

                    # do something only if we have a free slot.
                    if neighbors:
                        target_slot = renpy.random.choice( neighbors )
                        self.set_target_slot( target_slot )
                    else:
                        # we can't move because all neighbor slots are
                        # occupied.  reset the move timeout and try to
                        # move again later.
                        self.reset_timeout_counter( self.level.cell_action_timeout ) 
                        
            elif self.state == CELL_STATE_MOVING:
                self.dx += self.vx * delta_sec 
                self.dy += self.vy * delta_sec 
                
                if abs(self.dx) >= 1 or abs(self.dy) >= 1:
                    # Stop movement & update state if moved the width/height of a grid cell.
                    self.dx = 0
                    self.dy = 0
                    
                    self.slot.cells.remove( self )
                    self.slot = self.target_slot
                    
                    self.target_slot = None
                    
                    self.state = CELL_STATE_IDLE
                    self.reset_timeout_counter( self.level.cell_action_timeout )
                    
                x = (self.slot.x + self.dx) * GRID_CELL_WIDTH + GRID_CELL_WIDTH / 2
                y = (self.slot.y + self.dy) * GRID_CELL_HEIGHT + GRID_CELL_HEIGHT / 2
                self.game_object["transform"].set_position( x, y )
                
            elif self.state == CELL_STATE_MUTATING:
                self.timeout_counter -= delta_sec

                # do a cheesy flash effect while we're being infected.
                toggle_number = math.trunc( self.timeout_counter / INFECT_TOGGLE_DURATION )

                current_properties  = CELLS_PROPERTIES[self.type]
                mutation_properties = CELLS_PROPERTIES[current_properties[CELLS_PROP_MUTATES_TO]]
                frameset_from       = current_properties[CELLS_PROP_FRAMESET]
                frameset_to         = mutation_properties[CELLS_PROP_FRAMESET]

                if toggle_number % 2 == 0:
                    self.game_object["renderer"].set_animation_frameset( frameset_to )
                else:
                    self.game_object["renderer"].set_animation_frameset( frameset_from )

                if self.timeout_counter <= 0:
                    self.game_object["renderer"].set_animation_frameset( frameset_to )
                    
                    if self.type == CELLS_TYPE_HEALTHY:
                        self.inc_healthy_cell_count(-1)
                    
                    self.type       = current_properties[CELLS_PROP_MUTATES_TO]
                    self.hit_points = mutation_properties[CELLS_PROP_HIT_POINTS]
                    
                    self.state = CELL_STATE_IDLE
                    self.reset_timeout_counter( self.level.post_mutation_timeout )
                    self.inc_mutating_cell_count(-1)
                    
            elif self.state == CELL_STATE_DYING:
                # Free any slots occupied by this cell before killing the object.
                if self.slot and self in self.slot.cells:
                    self.slot.cells.remove( self )
                if self.target_slot and self in self.target_slot.cells:
                    self.target_slot.cells.remove( self )
            
                if self.type == CELLS_TYPE_HEALTHY:
                    self.inc_healthy_cell_count(-1)
                if self.state == CELL_STATE_MUTATING:
                    self.inc_mutating_cell_count(-1)
                self.game_object.kill()
            
            elif self.state == CELL_STATE_INFECTING:
                # Wait for the attack animation to finish.
                pass
                
        def finish_infecting( self ):
            self.state = CELL_STATE_IDLE
            self.game_object["renderer"].play_animation( CELL_ANIMATION_PULSE,
                                                         frameset=CELLS_PROPERTIES[self.type][CELLS_PROP_FRAMESET] )
            self.reset_timeout_counter( self.level.cell_action_timeout )
            
        def hit( self ):
            self.hit_points -= 1
            
        def die( self ):
            self.state = CELL_STATE_DYING
        
        def is_infectable( self ):
            # How about letting higher level cells infect/upgrade their lower level neighbors...?
            return self.type == CELLS_TYPE_HEALTHY and self.state == CELL_STATE_IDLE
