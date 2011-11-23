init python:
    import collections
    import itertools
    import math
    import pygame

    class MoleLevel( object ):
        def __init__( self, time_limit, max_moles, max_easy_moles,
                      max_medium_moles, max_hard_moles, spawn_time,
                      mole_duration ):
            super( MoleLevel, self ).__init__()

            self.time_limit       = time_limit
            self.max_moles        = max_moles
            self.max_easy_moles   = max_easy_moles
            self.max_medium_moles = max_medium_moles
            self.max_hard_moles   = max_hard_moles
            self.spawn_time       = spawn_time
            self.mole_duration    = mole_duration

    # Define the settings that affect the difficulty for each Whack-A-Mole
    # level.  The settings for each level are described as follows:
    #
    #     time_limit       - The length of the game in seconds.
    #
    #     max_moles        - Pair of numbers describing the number of moles
    #                        that can appear at once on the board, regardless
    #                        of their difficulty.  The first number of the max
    #                        number of moles that appear at the beginning of
    #                        the game, and the second number is the max number
    #                        that can appear at the end of the game.  Larger
    #                        number makes the game more difficult.
    #
    #     max_easy_moles   - Pair of numbers describing the number of "easy"
    #                        moles that appear at once on the board.  The first
    #                        first number is the number of these moles that
    #                        can appear at once at the beginning of the game,
    #                        and the second number is the number that can appear
    #                        at the end of the game.  Larger numbers make the
    #                        game more difficult.
    #
    #     max_medium_moles - Pair of numbers describing the number of "medium"
    #                        moles that appear at once on the board.  The first
    #                        first number is the number of these moles that
    #                        can appear at once at the beginning of the game,
    #                        and the second number is the number that can appear
    #                        at the end of the game.  Larger numbers make the
    #                        game more difficult.
    #
    #     max_hard_moles   - Pair of numbers describing the number of "hard"
    #                        moles that appear at once on the board.  The first
    #                        first number is the number of these moles that
    #                        can appear at once at the beginning of the game,
    #                        and the second number is the number that can appear
    #                        at the end of the game.  Larger numbers make the
    #                        game more difficult.
    #
    #     spawn_time       - Pair of numbers describing how often a new mole
    #                        appears on the game board, in seconds.  The first
    #                        number is the mole spawn time at the start of the
    #                        game, and the second number is mole spawn time at
    #                        the end of the game.  Smaller numbers make the game
    #                        more difficult.
    #
    #     mole_duration    - Pair of numbers describing how long a mole stays on
    #                        screen before it disappears, in seconds.  Thie first
    #                        number is the mole's duration at the beginning of
    #                        the game, and the second number is the mole's
    #                        duration at the end of the game.  Smaller numbers
    #                        make the game more difficult.
    #
    # Additional levels can be created by creating new MoleLevel entries and
    # filling in the values for each of its settings.
    MOLE_LEVELS = [
        # Level 1
        MoleLevel( time_limit       = 60,
                   max_moles        = (2, 8),
                   max_easy_moles   = (3, 5),
                   max_medium_moles = (0, 4),
                   max_hard_moles   = (0, 3),
                   spawn_time       = (0.75, 0.25),
                   mole_duration    = (1.6, 0.36) )
        ]

    #### DESIGNERS: DO NOT CHANGE ANYTHING BEYOND THIS LINE ####

    # different states the whack a mole game can be in.
    MOLE_GAME_STATE_BEGIN = "mole_begin"
    MOLE_GAME_STATE_PLAY  = "mole_play"
    MOLE_GAME_STATE_END   = "mole_end"

    # mole states.
    MOLE_STATE_DEAD       = "dead"
    MOLE_STATE_DYING      = "dying"
    MOLE_STATE_EMERGING   = "emerging"
    MOLE_STATE_IDLE       = "idle"
    MOLE_STATE_SUBMERGING = "submerging"
    MOLE_STATE_BURIED     = "buried"

    # animation names.
    MOLE_ANIMATION_DEAD     = "dead"
    MOLE_ANIMATION_EMERGE   = "emerge"
    MOLE_ANIMATION_SUBMERGE = "submerge"

    # frameset names.
    MOLE_FRAMESET_DEAD = "dead"

    # animation durations.  these divided into the number of frames that are
    # in the corresponding animation are the frames per second value passed to
    # the GameAnimation constructor.
    MOLE_ANIMATION_DEAD_DURATION     = 0.2
    MOLE_ANIMATION_EMERGE_DURATION   = 0.7
    MOLE_ANIMATION_SUBMERGE_DURATION = 0.35

    # duration a dead mole stays on screen.
    MOLE_DEAD_DURATION = 0.6

    # number of animation frames.
    NUMBER_DEAD_FRAMES     = 3
    NUMBER_EMERGE_FRAMES   = 10
    NUMBER_SUBMERGE_FRAMES = 4

    # prefab names.
    EASY_MOLE_TYPE   = "easy_mole"
    MEDIUM_MOLE_TYPE = "medium_mole"
    HARD_MOLE_TYPE   = "hard_mole"

    # mole hit points.
    MOLE_HIT_POINTS = { EASY_MOLE_TYPE   : 1,
                        MEDIUM_MOLE_TYPE : 3,
                        HARD_MOLE_TYPE   : 5 }

    # mole score values.
    MOLE_SCORE_VALUES = { EASY_MOLE_TYPE   : 100,
                          MEDIUM_MOLE_TYPE : 350,
                          HARD_MOLE_TYPE   : 600 }

    # accuracy bonus.
    MOLE_BASE_ACCURACY_BONUS  = 500
    MOLE_EXTRA_ACCURACY_BONUS = 100

    # game dimensions.
    NUMBER_ROWS    = 3
    NUMBER_COLUMNS = 3
    NUMBER_CELLS   = NUMBER_ROWS * NUMBER_COLUMNS

    # mole size in pixels.
    MOLE_SIZE = Size( 64, 60 )

    # pixel position of the upper left corner for each mole in the 3x3 grid
    # relative to the upper left corner of the whack a mole background image.
    CELL_POSITIONS = { (0,0) : (74, 83),
                       (0,1) : (283, 82),
                       (0,2) : (496, 82),
                       (1,0) : (75, 237),
                       (1,1) : (284, 248),
                       (1,2) : (504, 256),
                       (2,0) : (80, 441),
                       (2,1) : (280, 438),
                       (2,2) : (508, 443) }

    # misc. debug stuff.
    BOX_OVERLAY_COLOR = Color( 0, 0, 255, 100 )

    class WhackAMole( Minigame ):
        def __init__( self, level_number=1 ):
            super( WhackAMole, self ).__init__()

            if level_number > len( MOLE_LEVELS ) or level_number <= 0:
                raise ValueError( "Invalid Whack-a-Mole level number %d.  "
                                  "Level number must be between 1 and %d." %
                                  (level_number, len( MOLE_LEVELS )) )

            # set up automated level difficulty parameters.
            level = MOLE_LEVELS[level_number - 1]

            self.time_remaining   = AutomatedInterpolator( level.time_limit,
                                                           0,
                                                           level.time_limit )
            self.spawn_time       = AutomatedInterpolator( level.spawn_time[0],
                                                           level.spawn_time[1],
                                                           level.time_limit )
            self.max_moles        = AutomatedInterpolator( level.max_moles[0],
                                                           level.max_moles[1],
                                                           level.time_limit )
            self.max_easy_moles   = AutomatedInterpolator( level.max_easy_moles[0],
                                                           level.max_easy_moles[1],
                                                           level.time_limit )
            self.max_medium_moles = AutomatedInterpolator( level.max_medium_moles[0],
                                                           level.max_medium_moles[1],
                                                           level.time_limit )
            self.max_hard_moles   = AutomatedInterpolator( level.max_hard_moles[0],
                                                           level.max_hard_moles[1],
                                                           level.time_limit )
            self.mole_duration    = AutomatedInterpolator( level.mole_duration[0],
                                                           level.mole_duration[1],
                                                           level.time_limit )

            # set up game state.
            self.state          = MOLE_GAME_STATE_BEGIN
            self.time_limit     = level.time_limit
            self.base_score     = 0
            self.accuracy_bonus = 0
            self.number_clicks  = 0
            self.number_hits    = 0
            self.total_score    = 0
            self.mole_countdown = 0
            self.occupied_cells = []

            # set up entities.
            self.background         = None
            self.dirt_piles         = []
            self.easy_moles         = []
            self.medium_moles       = []
            self.hard_moles         = []
            self.score_hud          = None
            self.start_screen_hud   = None
            self.stop_screen_hud    = None
            self.time_remaining_hud = None

            self.create_background()
            self.create_moles()
            self.create_dirt()
            self.create_huds()

        def create_background( self ):
            self.background = GameObject()
            self.background["renderer"] = GameRenderer( GameImage( "gfx/whack_a_mole/background.png" ) )

        def create_moles( self ):
            # easy moles.
            easy_mole             = GameObject()
            easy_mole["collider"] = GameBoxCollider( MOLE_SIZE )
            easy_mole["renderer"] = GameRenderer( GameImage( "gfx/whack_a_mole/mole/mole-easy-static.png" ) )
            easy_mole["renderer"].add_animation( MOLE_ANIMATION_EMERGE,
                                                 GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole-easy-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                  for frame_index in xrange( NUMBER_EMERGE_FRAMES ) ],
                                                                NUMBER_EMERGE_FRAMES / MOLE_ANIMATION_EMERGE_DURATION ) )
            easy_mole["renderer"].add_animation( MOLE_ANIMATION_SUBMERGE,
                                                 GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole-easy-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                  for frame_index in reversed( xrange( NUMBER_SUBMERGE_FRAMES ) ) ],
                                                                NUMBER_SUBMERGE_FRAMES / MOLE_ANIMATION_SUBMERGE_DURATION ) )
            easy_mole["renderer"].add_animation( MOLE_ANIMATION_DEAD,
                                                 GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole_dead-easy-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                  for frame_index in xrange( NUMBER_DEAD_FRAMES ) ],
                                                                NUMBER_DEAD_FRAMES / MOLE_ANIMATION_DEAD_DURATION ) )
            easy_mole["renderer"].set_frame( MOLE_FRAMESET_DEAD, GameImage( "gfx/whack_a_mole/mole/mole_dead-easy.png" ) )
            easy_mole["renderer"].set_collider_visible( False )
            PrefabFactory.add_prefab( EASY_MOLE_TYPE, easy_mole )

            # medium moles.
            medium_mole             = GameObject()
            medium_mole["collider"] = GameBoxCollider( MOLE_SIZE )
            medium_mole["renderer"] = GameRenderer( GameImage( "gfx/whack_a_mole/mole/mole-medium-static.png" ) )
            medium_mole["renderer"].add_animation( MOLE_ANIMATION_EMERGE,
                                                   GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole-medium-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                    for frame_index in xrange( NUMBER_EMERGE_FRAMES ) ],
                                                                  NUMBER_EMERGE_FRAMES / MOLE_ANIMATION_EMERGE_DURATION ) )
            medium_mole["renderer"].add_animation( MOLE_ANIMATION_SUBMERGE,
                                                   GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole-medium-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                    for frame_index in reversed( xrange( NUMBER_SUBMERGE_FRAMES ) ) ],
                                                                  NUMBER_SUBMERGE_FRAMES / MOLE_ANIMATION_SUBMERGE_DURATION ) )
            medium_mole["renderer"].add_animation( MOLE_ANIMATION_DEAD,
                                                   GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole_dead-medium-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                    for frame_index in xrange( NUMBER_DEAD_FRAMES ) ],
                                                                  NUMBER_DEAD_FRAMES / MOLE_ANIMATION_DEAD_DURATION ) )
            medium_mole["renderer"].set_frame( MOLE_FRAMESET_DEAD, GameImage( "gfx/whack_a_mole/mole/mole_dead-medium.png" ) )
            medium_mole["renderer"].set_collider_visible( False )
            PrefabFactory.add_prefab( MEDIUM_MOLE_TYPE, medium_mole )

            # hard moles.
            hard_mole             = GameObject()
            hard_mole["collider"] = GameBoxCollider( MOLE_SIZE )
            hard_mole["renderer"] = GameRenderer( GameImage( "gfx/whack_a_mole/mole/mole-hard-static.png" ) )
            hard_mole["renderer"].add_animation( MOLE_ANIMATION_EMERGE,
                                                 GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole-hard-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                  for frame_index in xrange( NUMBER_EMERGE_FRAMES ) ],
                                                                NUMBER_EMERGE_FRAMES / MOLE_ANIMATION_EMERGE_DURATION ) )
            hard_mole["renderer"].add_animation( MOLE_ANIMATION_SUBMERGE,
                                                 GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole-hard-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                  for frame_index in reversed( xrange( NUMBER_SUBMERGE_FRAMES ) ) ],
                                                                NUMBER_SUBMERGE_FRAMES / MOLE_ANIMATION_SUBMERGE_DURATION ) )
            hard_mole["renderer"].add_animation( MOLE_ANIMATION_DEAD,
                                                 GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole_dead-hard-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                  for frame_index in xrange( NUMBER_DEAD_FRAMES ) ],
                                                                NUMBER_DEAD_FRAMES / MOLE_ANIMATION_DEAD_DURATION ) )
            hard_mole["renderer"].set_frame( MOLE_FRAMESET_DEAD, GameImage( "gfx/whack_a_mole/mole/mole_dead-hard.png" ) )
            hard_mole["renderer"].set_collider_visible( False )
            PrefabFactory.add_prefab( HARD_MOLE_TYPE, hard_mole )

        def create_dirt( self ):
            dirt             = GameObject()
            dirt["renderer"] = GameRenderer( GameImage( "gfx/whack_a_mole/dirt.png" ) )
            PrefabFactory.add_prefab( "dirt", dirt )

            for position in CELL_POSITIONS.itervalues():
                transform = GameTransform( *position )
                dirt_pile = PrefabFactory.instantiate( "dirt", transform )
                self.dirt_piles.append( dirt_pile )

        def create_huds( self ):
            self.score_hud             = GameObject()
            self.score_hud["renderer"] = GameRenderer( GameText( self.get_score, Color( 255, 255, 255, 255 ) ) )
            self.score_hud["transform"].set_position( 400, 10 )

            self.start_screen_hud             = GameObject()
            self.start_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/whack_a_mole/start_screen.png" ) )
            self.start_screen_hud["transform"].set_position( 138, 50 )

            self.stop_screen_hud             = GameObject()
            self.stop_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/whack_a_mole/stop_screen.png" ) )
            self.stop_screen_hud["transform"].set_position( 138, 50 )

            base_score             = GameObject()
            base_score["renderer"] = GameRenderer( GameText( self.get_base_score, Color( 255, 255, 255, 255 ) ) )
            base_score["transform"].set_position( 185, 159 )
            self.stop_screen_hud.add_child( base_score )

            accuracy_bonus             = GameObject()
            accuracy_bonus["renderer"] = GameRenderer( GameText( self.get_accuracy_bonus, Color( 255, 255, 255, 255 ) ) )
            accuracy_bonus["transform"].set_position( 185, 251 )
            self.stop_screen_hud.add_child( accuracy_bonus )

            total_score             = GameObject()
            total_score["renderer"] = GameRenderer( GameText( self.get_total_score, Color( 255, 255, 255, 255 ) ) )
            total_score["transform"].set_position( 185, 320 )
            self.stop_screen_hud.add_child( total_score )

            self.time_remaining_hud = GameObject()
            self.time_remaining_hud["renderer"] = GameRenderer( GameText( self.get_time_remaining, Color( 255, 255, 255, 255 ) ) )
            self.time_remaining_hud["transform"].set_position( 10, 10 )

        def compute_accuracy_bonus( self ):
            self.accuracy_bonus = 0
            if self.number_clicks > 0:
                hit_percentage = float(self.number_hits) / self.number_clicks

                if hit_percentage >= 0.8:
                    self.accuracy_bonus += MOLE_BASE_ACCURACY_BONUS
                if hit_percentage >= 0.85:
                    self.accuracy_bonus += MOLE_EXTRA_ACCURACY_BONUS
                if hit_percentage >= 0.9:
                    self.accuracy_bonus += MOLE_EXTRA_ACCURACY_BONUS
                if hit_percentage >= 0.95:
                    self.accuracy_bonus += MOLE_EXTRA_ACCURACY_BONUS
                if hit_percentage >= 1:
                    self.accuracy_bonus += (2 * MOLE_EXTRA_ACCURACY_BONUS)

        def get_accuracy_bonus( self ):
            if self.accuracy_bonus == 0:
                return "%20d" % self.accuracy_bonus
            elif self.accuracy_bonus < 1000:
                return "%18d" % self.accuracy_bonus
            else:
                return "%16d" % self.accuracy_bonus

        def get_available_cell( self ):
            while True:
                cell = self.get_random_cell()
                if cell not in self.occupied_cells:
                    return cell

        def get_base_score( self ):
            if self.base_score < 1000:
                return "%20d" % self.base_score
            elif self.base_score < 10000:
                return "%18d" % self.base_score
            else:
                return "%16d" % self.base_score

        def get_total_score( self ):
            if self.total_score < 1000:
                return "%20d" % self.total_score
            elif self.total_score < 10000:
                return "%18d" % self.total_score
            else:
                return "%16d" % self.total_score

        def get_cell( self, x, y ):
            position = (x, y)
            for cell in CELL_POSITIONS:
                if CELL_POSITIONS[cell] == position:
                    return cell

        def get_mole_at_cell( self, cell ):
            position = CELL_POSITIONS[cell]
            moles    = itertools.chain( self.easy_moles,
                                        self.medium_moles,
                                        self.hard_moles )

            for mole in moles:
                if (mole["transform"].x == position[0] and
                    mole["transform"].y == position[1]):
                    return mole

        def get_mole_at_position( self, x, y ):
            moles = itertools.chain( self.easy_moles,
                                     self.medium_moles,
                                     self.hard_moles )

            for mole in moles:
                if mole["collider"].is_point_inside( x, y ):
                    return mole

        def get_random_cell( self ):
            return (renpy.random.randint( 0, NUMBER_ROWS - 1),
                    renpy.random.randint( 0, NUMBER_COLUMNS - 1))

        def get_score( self ):
            return "Score: %16d" % self.base_score

        def get_time_remaining( self ):
            return "Time Remaining: %d" %  self.time_remaining.get_ceil_value()

        def on_mole_death( self, score_value ):
            self.base_score += score_value

        def remove_dead_moles( self, moles ):
            # free cells that are no longer occupied.
            for mole in moles:
                if not mole.is_alive():
                    cell = self.get_cell( mole["transform"].x,
                                          mole["transform"].y )
                    self.occupied_cells.remove( cell )

            # update the list with only those moles that are alive.
            moles[:] = [ mole for mole in moles if mole.is_alive() ]

        def spawn_mole( self, mole_type ):
            # clean way to pull the right list to add the new mole to.
            mole_lists = { EASY_MOLE_TYPE   : self.easy_moles,
                           MEDIUM_MOLE_TYPE : self.medium_moles,
                           HARD_MOLE_TYPE   : self.hard_moles }

            # create the new mole.
            cell             = self.get_available_cell()
            mole             = PrefabFactory.instantiate( mole_type )
            mole["behavior"] = MoleBehavior( MOLE_HIT_POINTS[mole_type],
                                             self.mole_duration.get_value(),
                                             MOLE_SCORE_VALUES[mole_type],
                                             self.on_mole_death )
            mole["behavior"].emerge()
            mole["transform"].set_position( *CELL_POSITIONS[cell] )
            mole_lists[mole_type].append( mole )
            self.occupied_cells.append( cell )

        def get_displayables( self ):
            displayables = []
            displayables.extend( self.background["renderer"].get_displayables() )

            for dirt in self.dirt_piles:
                displayables.extend( dirt["renderer"].get_displayables() )

            moles = itertools.chain( self.easy_moles,
                                     self.medium_moles,
                                     self.hard_moles )

            for mole in moles:
                displayables.extend( mole["renderer"].get_displayables() )

            displayables.extend( self.start_screen_hud["renderer"].get_displayables() )
            displayables.extend( self.stop_screen_hud["renderer"].get_displayables() )
            displayables.extend( self.time_remaining_hud["renderer"].get_displayables() )

            return displayables

        def get_result( self ):
            return self.total_score

        def update( self, delta_sec ):
            if self.state == MOLE_GAME_STATE_PLAY:
                # update automated parameters.
                self.time_remaining.update( delta_sec )
                self.spawn_time.update( delta_sec )
                self.max_moles.update( delta_sec )
                self.max_easy_moles.update( delta_sec )
                self.max_medium_moles.update( delta_sec )
                self.max_hard_moles.update( delta_sec )
                self.mole_duration.update( delta_sec )

                # update all moles.
                moles = itertools.chain( self.easy_moles,
                                         self.medium_moles,
                                         self.hard_moles )

                for mole in moles:
                    mole.update( delta_sec )

                # see if it's time to add a mole.
                self.mole_countdown -= delta_sec

                if (self.mole_countdown <= 0 and
                    self.time_remaining.get_value() > 0):
                    # get new countdown for next time.
                    self.mole_countdown = self.spawn_time.get_value()

                    # get which mole type are available.
                    mole_types = []

                    if len( self.easy_moles ) < self.max_easy_moles.get_truncated_value():
                        mole_types.append( EASY_MOLE_TYPE )
                    if len( self.medium_moles ) < self.max_medium_moles.get_truncated_value():
                        mole_types.append( MEDIUM_MOLE_TYPE )
                    if len( self.hard_moles ) < self.max_hard_moles.get_truncated_value():
                        mole_types.append( HARD_MOLE_TYPE )

                    number_moles = (len( self.easy_moles ) +
                                    len( self.medium_moles ) +
                                    len( self.hard_moles ))

                    # only attempt add a mole if there's a free cell and there's
                    # a mole of a particular type we can add.
                    if mole_types and number_moles < self.max_moles.get_truncated_value():
                        self.spawn_mole( renpy.random.choice( mole_types ) )

                # remove moles that have died.
                self.remove_dead_moles( self.easy_moles )
                self.remove_dead_moles( self.medium_moles )
                self.remove_dead_moles( self.hard_moles )

                # see if it's game over.
                if self.time_remaining.get_value() <= 0:
                    self.state = MOLE_GAME_STATE_END
                    self.compute_accuracy_bonus()
                    self.total_score = self.base_score + self.accuracy_bonus

        def render( self, blitter, clip_rect ):
            world_transform = self.get_world_transform()
            self.background["renderer"].render( blitter, clip_rect, world_transform )

            self.time_remaining_hud["renderer"].render( blitter, clip_rect, world_transform )
            self.score_hud["renderer"].render( blitter, clip_rect, world_transform )

            for dirt_pile in self.dirt_piles:
                dirt_pile["renderer"].render( blitter, clip_rect, world_transform )

            if self.state == MOLE_GAME_STATE_BEGIN:
                self.start_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == MOLE_GAME_STATE_PLAY:
                moles = itertools.chain( self.easy_moles,
                                         self.medium_moles,
                                         self.hard_moles )

                for mole in moles:
                    mole["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == MOLE_GAME_STATE_END:
                self.stop_screen_hud["renderer"].render( blitter, clip_rect, world_transform )

        def on_key_down( self, key ):
            if key == pygame.K_ESCAPE:
                self.quit()

            if self.state == MOLE_GAME_STATE_PLAY:
                mole = None

                if key == pygame.K_KP1 or key == pygame.K_z:
                    mole = self.get_mole_at_cell( (2,0) )
                elif key == pygame.K_KP2 or key == pygame.K_x:
                    mole = self.get_mole_at_cell( (2,1) )
                elif key == pygame.K_KP3 or key == pygame.K_c:
                    mole = self.get_mole_at_cell( (2,2) )
                elif key == pygame.K_KP4 or key == pygame.K_a:
                    mole = self.get_mole_at_cell( (1,0) )
                elif key == pygame.K_KP5 or key == pygame.K_s:
                    mole = self.get_mole_at_cell( (1,1) )
                elif key == pygame.K_KP6 or key == pygame.K_d:
                    mole = self.get_mole_at_cell( (1,2) )
                elif key == pygame.K_KP7 or key == pygame.K_q:
                    mole = self.get_mole_at_cell( (0,0) )
                elif key == pygame.K_KP8 or key == pygame.K_w:
                    mole = self.get_mole_at_cell( (0,1) )
                elif key == pygame.K_KP9 or key == pygame.K_e:
                    mole = self.get_mole_at_cell( (0,2) )

                self.number_clicks += 1

                if mole and not mole["behavior"].is_whacked():
                    mole["behavior"].hit()
                    self.number_hits += 1

        def on_mouse_down( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == MOLE_GAME_STATE_PLAY:
                    mx, my = self.transform_screen_to_world( mx, my )
                    mole   = self.get_mole_at_position( mx, my )
                    self.number_clicks += 1
                    if mole and not mole["behavior"].is_whacked():
                        mole["behavior"].hit()
                        self.number_hits += 1

        def on_mouse_up( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == MOLE_GAME_STATE_BEGIN:
                    self.state = MOLE_GAME_STATE_PLAY
                elif self.state == MOLE_GAME_STATE_END:
                    self.quit()

    class MoleBehavior( GameComponent ):
        def __init__( self, number_hit_points, duration, score_value,
                      on_death_callback ):
            super( MoleBehavior, self ).__init__()
            self.state             = MOLE_STATE_BURIED
            self.idle_remaining    = duration
            self.dead_countdown    = 0
            self.on_death_callback = on_death_callback
            self.number_hit_points = number_hit_points
            self.score_value       = score_value

        def die( self ):
            self.state = MOLE_STATE_DYING
            self.game_object["renderer"].play_animation( MOLE_ANIMATION_DEAD,
                                                         loop_animation=False,
                                                         on_animation_end=self.on_dead_end )
            self.on_death_callback( self.score_value )

        def emerge( self ):
            self.state = MOLE_STATE_EMERGING
            self.game_object["renderer"].play_animation( MOLE_ANIMATION_EMERGE,
                                                         loop_animation=False,
                                                         on_animation_end=self.on_emerge_end )

        def hit( self ):
            self.number_hit_points -= 1
            if self.number_hit_points == 0:
                self.die()

        def is_whacked( self ):
            return self.state == MOLE_STATE_DEAD or self.state == MOLE_STATE_DYING

        def on_dead_end( self ):
            self.state          = MOLE_STATE_DEAD
            self.dead_countdown = MOLE_DEAD_DURATION
            self.game_object["renderer"].set_frameset( MOLE_FRAMESET_DEAD )

        def on_emerge_end( self ):
            self.state = MOLE_STATE_IDLE

        def on_submerge_end( self ):
            self.game_object.kill()

        def submerge( self ):
            self.state = MOLE_STATE_SUBMERGING
            self.game_object["renderer"].play_animation( MOLE_ANIMATION_SUBMERGE,
                                                         loop_animation=False,
                                                         on_animation_end=self.on_submerge_end )

        def update( self, delta_sec ):
            if self.state == MOLE_STATE_IDLE:
                self.idle_remaining -= delta_sec
                if self.idle_remaining <= 0:
                    self.submerge()
            elif self.state == MOLE_STATE_DEAD:
                self.dead_countdown -= delta_sec
                if self.dead_countdown <= 0:
                    self.game_object.kill()
