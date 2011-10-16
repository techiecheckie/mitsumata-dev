init python:
    import collections
    import math
    import pygame

    class MoleLevel( object ):
        def __init__( self, time_limit, max_easy_moles, max_medium_moles,
                      max_hard_moles, spawn_time, mole_duration ):
            super( MoleLevel, self ).__init__()

            self.time_limit       = time_limit
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
                   max_easy_moles   = (1, 1),
                   max_medium_moles = (0, 0),
                   max_hard_moles   = (0, 0),
                   spawn_time       = (0.75, 0.25),
                   mole_duration    = (1.6, 0.36) )
        ]

    #### DESIGNERS: DO NOT CHANGE ANYTHING BEYOND THIS LINE ####

    # different states the whack a mole game can be in.
    MOLE_GAME_STATE_BEGIN = "mole_begin"
    MOLE_GAME_STATE_PLAY  = "mole_play"
    MOLE_GAME_STATE_END   = "mole_end"

    # mole states.
    MOLE_STATE_EMERGING   = "emerging"
    MOLE_STATE_IDLE       = "idle"
    MOLE_STATE_SUBMERGING = "submerging"
    MOLE_STATE_BURIED     = "buried"

    # animation names.
    MOLE_ANIMATION_EMERGE   = "emerge"
    MOLE_ANIMATION_SUBMERGE = "submerge"

    # animation durations.  the inverse of these are the animations frames per
    # second value passed to the GameAnimation constructor.
    MOLE_ANIMATION_EMERGE_DURATION   = 0.7
    MOLE_ANIMATION_SUBMERGE_DURATION = 0.35

    # number of animation frames.
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

    # game dimensions.
    NUMBER_ROWS    = 3
    NUMBER_COLUMNS = 3
    NUMBER_CELLS   = NUMBER_ROWS * NUMBER_COLUMNS

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

    class WhackAMole( Minigame ):
        def __init__( self, level_number=1 ):
            super( WhackAMole, self ).__init__()

            if level_number > len( MOLE_LEVELS ) or level_number <= 0:
                raise ValueError( "Invalid Whack-a-Mole level number %d.  "
                                  "Level number must be between 1 and %d." %
                                  (level_number, len( MOLE_LEVELS )) )

            # set up automated level difficulty parameters.
            level = MOLE_LEVELS[level_number - 1]

            self.time_remaining   = AutomatedInterpolator( 0,
                                                           level.time_limit,
                                                           level.time_limit )
            self.spawn_time       = AutomatedInterpolator( level.spawn_time[0],
                                                           level.spawn_time[1],
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

            # set up game state.
            self.state          = MOLE_GAME_STATE_BEGIN
            self.score          = 0
            self.final_score    = 0
            self.mole_countdown = 0
            self.occupied_cells = []

            # set up entities.
            self.background   = None
            self.dirt_piles   = []
            self.easy_moles   = []
            self.medium_moles = []
            self.hard_moles   = []

            self.create_background()
            self.create_moles()
            self.create_dirt()

        def create_background( self ):
            self.background = GameObject()
            self.background["renderer"] = GameRenderer( GameImage( "gfx/whack_a_mole/background.png" ) )

        def create_moles( self ):
            # easy moles.
            easy_mole             = GameObject()
            easy_mole["renderer"] = GameRenderer( GameImage( "gfx/whack_a_mole/mole/mole-static.png" ) )
            easy_mole["renderer"].add_animation( MOLE_ANIMATION_EMERGE,
                                                 GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                  for frame_index in xrange( NUMBER_EMERGE_FRAMES ) ],
                                                                NUMBER_EMERGE_FRAMES / MOLE_ANIMATION_EMERGE_DURATION ) )
            easy_mole["renderer"].add_animation( MOLE_ANIMATION_SUBMERGE,
                                                 GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                  for frame_index in reversed( xrange( NUMBER_SUBMERGE_FRAMES ) ) ],
                                                                NUMBER_SUBMERGE_FRAMES / MOLE_ANIMATION_SUBMERGE_DURATION ) )
            PrefabFactory.add_prefab( EASY_MOLE_TYPE, easy_mole )

            # medium moles.
            medium_mole             = GameObject()
            medium_mole["renderer"] = GameRenderer( GameImage( "gfx/whack_a_mole/mole/mole-static.png" ) )
            medium_mole["renderer"].add_animation( MOLE_ANIMATION_EMERGE,
                                                   GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                    for frame_index in xrange( NUMBER_EMERGE_FRAMES ) ],
                                                                  NUMBER_EMERGE_FRAMES / MOLE_ANIMATION_EMERGE_DURATION ) )
            medium_mole["renderer"].add_animation( MOLE_ANIMATION_SUBMERGE,
                                                   GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                    for frame_index in reversed( xrange( NUMBER_SUBMERGE_FRAMES ) ) ],
                                                                  NUMBER_SUBMERGE_FRAMES / MOLE_ANIMATION_SUBMERGE_DURATION ) )
            PrefabFactory.add_prefab( MEDIUM_MOLE_TYPE, medium_mole )

            # hard moles.
            hard_mole             = GameObject()
            hard_mole["renderer"] = GameRenderer( GameImage( "gfx/whack_a_mole/mole/mole-static.png" ) )
            hard_mole["renderer"].add_animation( MOLE_ANIMATION_EMERGE,
                                                 GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                  for frame_index in xrange( NUMBER_EMERGE_FRAMES ) ],
                                                                NUMBER_EMERGE_FRAMES / MOLE_ANIMATION_EMERGE_DURATION ) )
            hard_mole["renderer"].add_animation( MOLE_ANIMATION_SUBMERGE,
                                                 GameAnimation( [ GameImage( "gfx/whack_a_mole/mole/mole-%d.png" % frame_index, Anchor.TOP_LEFT )
                                                                  for frame_index in reversed( xrange( NUMBER_SUBMERGE_FRAMES ) ) ],
                                                                NUMBER_SUBMERGE_FRAMES / MOLE_ANIMATION_SUBMERGE_DURATION ) )
            PrefabFactory.add_prefab( HARD_MOLE_TYPE, hard_mole )

        def create_dirt( self ):
            dirt             = GameObject()
            dirt["renderer"] = GameRenderer( GameImage( "gfx/whack_a_mole/dirt.png" ) )
            PrefabFactory.add_prefab( "dirt", dirt )

            for position in CELL_POSITIONS.itervalues():
                transform = GameTransform( *position )
                dirt_pile = PrefabFactory.instantiate( "dirt", transform )
                self.dirt_piles.append( dirt_pile )

        def get_available_cell( self ):
            while True:
                cell = self.get_random_cell()
                if cell not in self.occupied_cells:
                    return cell

        def get_random_cell( self ):
            return (renpy.random.randint( 0, NUMBER_ROWS - 1),
                    renpy.random.randint( 0, NUMBER_COLUMNS - 1))

        def spawn_mole( self, mole_type ):
            # clean way to pull the right list to add the new mole to.
            mole_lists = { EASY_MOLE_TYPE   : self.easy_moles,
                           MEDIUM_MOLE_TYPE : self.medium_moles,
                           HARD_MOLE_TYPE   : self.hard_moles }

            # create the new mole.
            cell             = self.get_available_cell()
            mole             = PrefabFactory.instantiate( mole_type )
            mole["behavior"] = MoleBehavior( MOLE_HIT_POINTS[mole_type] )
            mole["behavior"].emerge()
            mole["transform"].set_position( *CELL_POSITIONS[cell] )
            mole_lists[mole_type].append( mole )
            self.occupied_cells.append( cell )

        def get_displayables( self ):
            displayables = []
            displayables.extend( self.background["renderer"].get_displayables() )
            return displayables

        def update( self, delta_sec ):
            if self.state != MOLE_GAME_STATE_PLAY:
                # update automated parameters.
                self.time_remaining.update( delta_sec )
                self.spawn_time.update( delta_sec )
                self.max_easy_moles.update( delta_sec )
                self.max_medium_moles.update( delta_sec )
                self.max_hard_moles.update( delta_sec )

                # update all moles.
                for mole in self.easy_moles:
                    mole.update( delta_sec )

                for mole in self.medium_moles:
                    mole.update( delta_sec )

                for mole in self.hard_moles:
                    mole.update( delta_sec )

                # remove moles that have died.
                self.easy_moles[:]   = [ mole for mole in self.easy_moles if mole.is_alive() ]
                self.medium_moles[:] = [ mole for mole in self.medium_moles if mole.is_alive() ]
                self.hard_moles[:]   = [ mole for mole in self.hard_moles if mole.is_alive() ]

                # see if it's time to add a mole.
                self.mole_countdown -= delta_sec

                if (self.mole_countdown <= 0 and
                    self.time_remaining.get_value() > 0):
                    # get which mole type are available.
                    mole_types = []

                    if len( self.easy_moles ) < self.max_easy_moles.get_value():
                        mole_types.append( EASY_MOLE_TYPE )
                    if len( self.medium_moles ) < self.max_medium_moles.get_value():
                        mole_types.append( MEDIUM_MOLE_TYPE )
                    if len( self.hard_moles ) < self.max_hard_moles.get_value():
                        mole_types.append( HARD_MOLE_TYPE )

                    number_moles = (len( self.easy_moles ) +
                                    len( self.medium_moles ) +
                                    len( self.hard_moles ))

                    # only attempt add a mole if there's a free cell and there's
                    # a mole of a particular type we can add.
                    if mole_types and number_moles < NUMBER_CELLS:
                        self.spawn_mole( renpy.random.choice( mole_types ) )

        def render( self, blitter ):
            world_transform = GameTransform()
            self.background["renderer"].render( blitter, world_transform )

            for dirt_pile in self.dirt_piles:
                dirt_pile["renderer"].render( blitter, world_transform )

            for mole in self.easy_moles:
                mole["renderer"].render( blitter, world_transform )

            for mole in self.medium_moles:
                mole["renderer"].render( blitter, world_transform )

            for mole in self.hard_moles:
                mole["renderer"].render( blitter, world_transform )

        def on_key_down( self, key ):
            if key == pygame.K_ESCAPE:
                self.quit()

        def on_mouse_up( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == MOLE_GAME_STATE_BEGIN:
                    self.state          = MOLE_GAME_STATE_PLAY
                    self.mole_countdown = self.spawn_time.get_value()

    class MoleBehavior( GameComponent ):
        def __init__( self, number_hit_points ):
            super( MoleBehavior, self ).__init__()
            self.state             = MOLE_STATE_BURIED
            self.idle_timeout      = 0
            self.number_hit_points = number_hit_points

        def emerge( self ):
            self.state = MOLE_STATE_EMERGING
            self.game_object["renderer"].play_animation( MOLE_ANIMATION_EMERGE,
                                                         loop_animation=False,
                                                         on_animation_end=self.on_emerge_end )

        def on_emerge_end( self ):
            self.state = MOLE_STATE_IDLE
            self.idle_timeout = 2

        def on_submerge_end( self ):
            self.game_object.kill()

        def submerge( self ):
            self.state = MOLE_STATE_SUBMERGING
            self.game_object["renderer"].play_animation( MOLE_ANIMATION_SUBMERGE,
                                                         loop_animation=False,
                                                         on_animation_end=self.on_submerge_end )

        def update( self, delta_sec ):
            if self.state == MOLE_STATE_IDLE:
                self.idle_timeout -= delta_sec
                if self.idle_timeout <= 0:
                    self.submerge()
