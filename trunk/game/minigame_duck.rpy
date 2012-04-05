init python:
    import itertools
    import math
    import pygame

    class HuntLevel( object ):
        def __init__( self, time_limit, max_birds, max_easy_birds,
                      max_medium_birds, max_hard_birds, spawn_time,
                      bird_speed, bird_scale ):
            super( HuntLevel, self ).__init__()

            self.time_limit       = time_limit
            self.max_birds        = max_birds
            self.max_easy_birds   = max_easy_birds
            self.max_medium_birds = max_medium_birds
            self.max_hard_birds   = max_hard_birds
            self.spawn_time       = spawn_time
            self.bird_speed       = bird_speed
            self.bird_scale       = bird_scale

    HUNT_LEVELS = [
        HuntLevel( time_limit       = 60,
                   max_birds        = (4, 10),
                   max_easy_birds   = (3, 7),
                   max_medium_birds = (0, 4),
                   max_hard_birds   = (0, 3),
                   spawn_time       = (0.75, 0.25),
                   bird_speed       = (80, 140),
                   bird_scale       = (1.0, 1.5) ),
        
        HuntLevel( time_limit       = 60,
                   max_birds        = (4, 10),
                   max_easy_birds   = (3, 7),
                   max_medium_birds = (0, 4),
                   max_hard_birds   = (0, 3),
                   spawn_time       = (0.75, 0.25),
                   bird_speed       = (80, 140),
                   bird_scale       = (1.0, 1.5) ),
        
        HuntLevel( time_limit       = 60,
                   max_birds        = (4, 10),
                   max_easy_birds   = (3, 7),
                   max_medium_birds = (0, 4),
                   max_hard_birds   = (0, 3),
                   spawn_time       = (0.75, 0.25),
                   bird_speed       = (80, 140),
                   bird_scale       = (1.0, 1.5) ),
                   
        HuntLevel( time_limit       = 60,
                   max_birds        = (4, 10),
                   max_easy_birds   = (3, 7),
                   max_medium_birds = (0, 4),
                   max_hard_birds   = (0, 3),
                   spawn_time       = (0.75, 0.25),
                   bird_speed       = (80, 140),
                   bird_scale       = (1.0, 1.5) )
        ]

    #### DESIGNERS: DO NOT CHANGE ANYTHING BEYOND THIS LINE ####

    # different states the Hunt Duck game can be in.
    HUNT_GAME_STATE_BEGIN     = "hunt_begin"
    HUNT_GAME_STATE_COUNTDOWN = "hunt_countdown"
    HUNT_GAME_STATE_PLAY      = "hunt_play"
    HUNT_GAME_STATE_END       = "hunt_end"

    # bird states.
    BIRD_STATE_DEAD   = "dead"
    BIRD_STATE_FLYING = "flying"

    # animation names.
    BIRD_ANIMATION_DEAD       = "dead"
    BIRD_ANIMATION_FLY_DOWN   = "fly_down"
    BIRD_ANIMATION_FLY_LEFT   = "fly_left"
    BIRD_ANIMATION_FLY_RIGHT  = "fly_right"
    BIRD_ANIMATION_FLY_UP     = "fly_up"
    BIRD_ANIMATION_SHOT_LEFT  = "shot_left"
    BIRD_ANIMATION_SHOT_RIGHT = "shot_right"
    BOOM_ANIMATION_FIRE       = "fire"

    # animation durations.  these divided into the number of frames that are
    # in the corresponding animation are the frames per second value passed to
    # the GameAnimation constructor.
    BOOM_FIRE_DURATION                 = 0.72
    BIRD_ANIMATION_DEAD_DURATION       = 0.25
    BIRD_ANIMATION_FLY_DOWN_DURATION   = 0.6
    BIRD_ANIMATION_FLY_LEFT_DURATION   = 0.6
    BIRD_ANIMATION_FLY_RIGHT_DURATION  = 0.6
    BIRD_ANIMATION_FLY_UP_DURATION     = 0.6
    BIRD_ANIMATION_SHOT_LEFT_DURATION  = 0.3
    BIRD_ANIMATION_SHOT_RIGHT_DURATION = 0.3

    # number of animation frames.
    NUMBER_BOOM_FIRE_FRAMES       = 18
    NUMBER_BIRD_DEAD_FRAMES       = 2
    NUMBER_BIRD_FLY_DOWN_FRAMES   = 4
    NUMBER_BIRD_FLY_LEFT_FRAMES   = 4
    NUMBER_BIRD_FLY_RIGHT_FRAMES  = 4
    NUMBER_BIRD_FLY_UP_FRAMES     = 4
    NUMBER_BIRD_SHOT_LEFT_FRAMES  = 2
    NUMBER_BIRD_SHOT_RIGHT_FRAMES = 2

    # prefab names.
    BOOM_TYPE        = "boom"
    EASY_BIRD_TYPE   = "easy_bird"
    MEDIUM_BIRD_TYPE = "medium_bird"
    HARD_BIRD_TYPE   = "hard_bird"

    # bird directions.
    BIRD_DIRECTION_DOWN  = "down"
    BIRD_DIRECTION_LEFT  = "left"
    BIRD_DIRECTION_RIGHT = "right"
    BIRD_DIRECTION_UP    = "up"

    # bird speed.
    BIRD_FALL_SPEED = 260

    # bird hit points.
    BIRD_HIT_POINTS = { EASY_BIRD_TYPE   : 1,
                        MEDIUM_BIRD_TYPE : 3,
                        HARD_BIRD_TYPE   : 5 }

    # bird score values.
    BIRD_SCORE_VALUES = { EASY_BIRD_TYPE   : 100,
                          MEDIUM_BIRD_TYPE : 350,
                          HARD_BIRD_TYPE   : 600 }

    # accuracy bonus.
    HUNT_BASE_ACCURACY_BONUS  = 500
    HUNT_EXTRA_ACCURACY_BONUS = 100

    # bird size in pixels.
    BIRD_ALIVE_SIZE = Size( 40, 40 )
    BIRD_DEAD_SIZE  = Size( 57, 57 )

    class DuckHunt( Minigame ):
        def __init__( self, level_number=1 ):
            super( DuckHunt, self ).__init__()
            hide_mouse()

            if level_number > len( HUNT_LEVELS ) or level_number <= 0:
                raise ValueError( "Invalid Hunt Duck level number %d.  "
                                  "Level number must be between 1 and %d." %
                                  (level_number, len( HUNT_LEVELS )) )

            # set up automated level difficulty parameters.
            level = HUNT_LEVELS[level_number - 1]

            self.time_remaining   = AutomatedInterpolator( level.time_limit,
                                                           0,
                                                           level.time_limit )
            self.bird_speed       = Randomizer( level.bird_speed[0],
                                                level.bird_speed[1] )
            self.bird_scale       = Randomizer( level.bird_scale[0],
                                                level.bird_scale[1] )
            self.spawn_time       = AutomatedInterpolator( level.spawn_time[0],
                                                           level.spawn_time[1],
                                                           level.time_limit )
            self.max_birds        = AutomatedInterpolator( level.max_birds[0],
                                                           level.max_birds[1],
                                                           level.time_limit )
            self.max_easy_birds   = AutomatedInterpolator( level.max_easy_birds[0],
                                                           level.max_easy_birds[1],
                                                           level.time_limit )
            self.max_medium_birds = AutomatedInterpolator( level.max_medium_birds[0],
                                                           level.max_medium_birds[1],
                                                           level.time_limit )
            self.max_hard_birds   = AutomatedInterpolator( level.max_hard_birds[0],
                                                           level.max_hard_birds[1],
                                                           level.time_limit )

            # setup game state.
            self.state          = HUNT_GAME_STATE_BEGIN
            self.time_limit     = level.time_limit
            self.base_score     = 0
            self.accuracy_bonus = 0
            self.number_clicks  = 0
            self.number_hits    = 0
            self.total_score    = 0
            self.bird_countdown = 1


            # set up entities.
            #self.background         = None
            self.player             = None
            self.booms              = []
            self.easy_birds         = []
            self.medium_birds       = []
            self.hard_birds         = []
            self.score_hud          = None
            self.start_screen_hud   = None
            self.stop_screen_hud    = None
            self.time_remaining_hud = None

            #self.create_background()
            self.create_player()
            self.create_birds()
            self.create_boom()
            self.create_huds()

        def quit( self ):
            super( DuckHunt, self ).quit()
            show_mouse()

        def create_background( self ):
            self.background             = GameObject()
            self.background["renderer"] = GameRenderer( GameImage( "gfx/duck_hunt/background.png" ) )

        def create_player( self ):
            self.player             = GameObject( "player" )
            self.player["renderer"] = GameRenderer( GameImage( "gfx/duck_hunt/cursor.png", Anchor.CENTER ) )

        def create_birds( self ):
            easy_bird = GameObject()
            easy_bird["collider"] = GameBoxCollider( BIRD_ALIVE_SIZE, Anchor.CENTER )
            easy_bird["renderer"] = GameRenderer()
            easy_bird["renderer"].add_animation( BIRD_ANIMATION_FLY_DOWN,
                                                 GameAnimation( [ GameImage( "gfx/duck_hunt/bird/down/bird_down-easy-%d.png" % frame_index, Anchor.CENTER )
                                                                  for frame_index in xrange( NUMBER_BIRD_FLY_DOWN_FRAMES ) ],
                                                                NUMBER_BIRD_FLY_DOWN_FRAMES / BIRD_ANIMATION_FLY_DOWN_DURATION ) )
            easy_bird["renderer"].add_animation( BIRD_ANIMATION_FLY_LEFT,
                                                 GameAnimation( [ GameImage( "gfx/duck_hunt/bird/left/bird_left-easy-%d.png" % frame_index, Anchor.CENTER )
                                                                  for frame_index in xrange( NUMBER_BIRD_FLY_LEFT_FRAMES ) ],
                                                                NUMBER_BIRD_FLY_LEFT_FRAMES / BIRD_ANIMATION_FLY_LEFT_DURATION ) )
            easy_bird["renderer"].add_animation( BIRD_ANIMATION_FLY_RIGHT,
                                                 GameAnimation( [ GameImage( "gfx/duck_hunt/bird/right/bird_right-easy-%d.png" % frame_index, Anchor.CENTER )
                                                                  for frame_index in xrange( NUMBER_BIRD_FLY_RIGHT_FRAMES ) ],
                                                                NUMBER_BIRD_FLY_RIGHT_FRAMES / BIRD_ANIMATION_FLY_RIGHT_DURATION ) )
            easy_bird["renderer"].add_animation( BIRD_ANIMATION_FLY_UP,
                                                 GameAnimation( [ GameImage( "gfx/duck_hunt/bird/up/bird_up-easy-%d.png" % frame_index, Anchor.CENTER )
                                                                  for frame_index in xrange( NUMBER_BIRD_FLY_UP_FRAMES ) ],
                                                                NUMBER_BIRD_FLY_UP_FRAMES / BIRD_ANIMATION_FLY_UP_DURATION ) )
            easy_bird["renderer"].add_animation( BIRD_ANIMATION_SHOT_LEFT,
                                                 GameAnimation( [ GameImage( "gfx/duck_hunt/bird/shot/bird_shot_left-easy-%d.png" % frame_index, Anchor.CENTER )
                                                                  for frame_index in xrange( NUMBER_BIRD_SHOT_LEFT_FRAMES ) ],
                                                                NUMBER_BIRD_SHOT_LEFT_FRAMES / BIRD_ANIMATION_SHOT_LEFT_DURATION ) )
            easy_bird["renderer"].add_animation( BIRD_ANIMATION_SHOT_RIGHT,
                                                 GameAnimation( [ GameImage( "gfx/duck_hunt/bird/shot/bird_shot_right-easy-%d.png" % frame_index, Anchor.CENTER )
                                                                  for frame_index in xrange( NUMBER_BIRD_SHOT_RIGHT_FRAMES ) ],
                                                                NUMBER_BIRD_SHOT_RIGHT_FRAMES / BIRD_ANIMATION_SHOT_RIGHT_DURATION ) )
            easy_bird["renderer"].add_animation( BIRD_ANIMATION_DEAD,
                                                 GameAnimation( [ GameImage( "gfx/duck_hunt/bird/dead/bird_dead-easy-%d.png" % frame_index, Anchor.CENTER )
                                                                  for frame_index in xrange( NUMBER_BIRD_DEAD_FRAMES ) ],
                                                                NUMBER_BIRD_DEAD_FRAMES / BIRD_ANIMATION_DEAD_DURATION ) )
            easy_bird["renderer"].set_collider_visible( False )
            PrefabFactory.add_prefab( EASY_BIRD_TYPE, easy_bird )

            medium_bird = GameObject()
            medium_bird["collider"] = GameBoxCollider( BIRD_ALIVE_SIZE, Anchor.CENTER )
            medium_bird["renderer"] = GameRenderer()
            medium_bird["renderer"].add_animation( BIRD_ANIMATION_FLY_DOWN,
                                                   GameAnimation( [ GameImage( "gfx/duck_hunt/bird/down/bird_down-medium-%d.png" % frame_index, Anchor.CENTER )
                                                                    for frame_index in xrange( NUMBER_BIRD_FLY_DOWN_FRAMES ) ],
                                                                  NUMBER_BIRD_FLY_DOWN_FRAMES / BIRD_ANIMATION_FLY_DOWN_DURATION ) )
            medium_bird["renderer"].add_animation( BIRD_ANIMATION_FLY_LEFT,
                                                   GameAnimation( [ GameImage( "gfx/duck_hunt/bird/left/bird_left-medium-%d.png" % frame_index, Anchor.CENTER )
                                                                    for frame_index in xrange( NUMBER_BIRD_FLY_LEFT_FRAMES ) ],
                                                                  NUMBER_BIRD_FLY_LEFT_FRAMES / BIRD_ANIMATION_FLY_LEFT_DURATION ) )
            medium_bird["renderer"].add_animation( BIRD_ANIMATION_FLY_RIGHT,
                                                   GameAnimation( [ GameImage( "gfx/duck_hunt/bird/right/bird_right-medium-%d.png" % frame_index, Anchor.CENTER )
                                                                    for frame_index in xrange( NUMBER_BIRD_FLY_RIGHT_FRAMES ) ],
                                                                  NUMBER_BIRD_FLY_RIGHT_FRAMES / BIRD_ANIMATION_FLY_RIGHT_DURATION ) )
            medium_bird["renderer"].add_animation( BIRD_ANIMATION_FLY_UP,
                                                   GameAnimation( [ GameImage( "gfx/duck_hunt/bird/up/bird_up-medium-%d.png" % frame_index, Anchor.CENTER )
                                                                    for frame_index in xrange( NUMBER_BIRD_FLY_UP_FRAMES ) ],
                                                                  NUMBER_BIRD_FLY_UP_FRAMES / BIRD_ANIMATION_FLY_UP_DURATION ) )
            medium_bird["renderer"].add_animation( BIRD_ANIMATION_SHOT_LEFT,
                                                   GameAnimation( [ GameImage( "gfx/duck_hunt/bird/shot/bird_shot_left-medium-%d.png" % frame_index, Anchor.CENTER )
                                                                    for frame_index in xrange( NUMBER_BIRD_SHOT_LEFT_FRAMES ) ],
                                                                  NUMBER_BIRD_SHOT_LEFT_FRAMES / BIRD_ANIMATION_SHOT_LEFT_DURATION ) )
            medium_bird["renderer"].add_animation( BIRD_ANIMATION_SHOT_RIGHT,
                                                   GameAnimation( [ GameImage( "gfx/duck_hunt/bird/shot/bird_shot_right-medium-%d.png" % frame_index, Anchor.CENTER )
                                                                    for frame_index in xrange( NUMBER_BIRD_SHOT_RIGHT_FRAMES ) ],
                                                                  NUMBER_BIRD_SHOT_RIGHT_FRAMES / BIRD_ANIMATION_SHOT_RIGHT_DURATION ) )
            medium_bird["renderer"].add_animation( BIRD_ANIMATION_DEAD,
                                                   GameAnimation( [ GameImage( "gfx/duck_hunt/bird/dead/bird_dead-medium-%d.png" % frame_index, Anchor.CENTER )
                                                                    for frame_index in xrange( NUMBER_BIRD_DEAD_FRAMES ) ],
                                                                  NUMBER_BIRD_DEAD_FRAMES / BIRD_ANIMATION_DEAD_DURATION ) )
            medium_bird["renderer"].set_collider_visible( False )
            PrefabFactory.add_prefab( MEDIUM_BIRD_TYPE, medium_bird )

            hard_bird = GameObject()
            hard_bird["collider"] = GameBoxCollider( BIRD_ALIVE_SIZE, Anchor.CENTER )
            hard_bird["renderer"] = GameRenderer()
            hard_bird["renderer"].add_animation( BIRD_ANIMATION_FLY_DOWN,
                                                 GameAnimation( [ GameImage( "gfx/duck_hunt/bird/down/bird_down-hard-%d.png" % frame_index, Anchor.CENTER )
                                                                  for frame_index in xrange( NUMBER_BIRD_FLY_DOWN_FRAMES ) ],
                                                                NUMBER_BIRD_FLY_DOWN_FRAMES / BIRD_ANIMATION_FLY_DOWN_DURATION ) )
            hard_bird["renderer"].add_animation( BIRD_ANIMATION_FLY_LEFT,
                                                 GameAnimation( [ GameImage( "gfx/duck_hunt/bird/left/bird_left-hard-%d.png" % frame_index, Anchor.CENTER )
                                                                  for frame_index in xrange( NUMBER_BIRD_FLY_LEFT_FRAMES ) ],
                                                                NUMBER_BIRD_FLY_LEFT_FRAMES / BIRD_ANIMATION_FLY_LEFT_DURATION ) )
            hard_bird["renderer"].add_animation( BIRD_ANIMATION_FLY_RIGHT,
                                                 GameAnimation( [ GameImage( "gfx/duck_hunt/bird/right/bird_right-hard-%d.png" % frame_index, Anchor.CENTER )
                                                                  for frame_index in xrange( NUMBER_BIRD_FLY_RIGHT_FRAMES ) ],
                                                                NUMBER_BIRD_FLY_RIGHT_FRAMES / BIRD_ANIMATION_FLY_RIGHT_DURATION ) )
            hard_bird["renderer"].add_animation( BIRD_ANIMATION_FLY_UP,
                                                 GameAnimation( [ GameImage( "gfx/duck_hunt/bird/up/bird_up-hard-%d.png" % frame_index, Anchor.CENTER )
                                                                  for frame_index in xrange( NUMBER_BIRD_FLY_UP_FRAMES ) ],
                                                                NUMBER_BIRD_FLY_UP_FRAMES / BIRD_ANIMATION_FLY_UP_DURATION ) )
            hard_bird["renderer"].add_animation( BIRD_ANIMATION_SHOT_LEFT,
                                                 GameAnimation( [ GameImage( "gfx/duck_hunt/bird/shot/bird_shot_left-hard-%d.png" % frame_index, Anchor.CENTER )
                                                                  for frame_index in xrange( NUMBER_BIRD_SHOT_LEFT_FRAMES ) ],
                                                                NUMBER_BIRD_SHOT_LEFT_FRAMES / BIRD_ANIMATION_SHOT_LEFT_DURATION ) )
            hard_bird["renderer"].add_animation( BIRD_ANIMATION_SHOT_RIGHT,
                                                 GameAnimation( [ GameImage( "gfx/duck_hunt/bird/shot/bird_shot_right-hard-%d.png" % frame_index, Anchor.CENTER )
                                                                  for frame_index in xrange( NUMBER_BIRD_SHOT_RIGHT_FRAMES ) ],
                                                                NUMBER_BIRD_SHOT_RIGHT_FRAMES / BIRD_ANIMATION_SHOT_RIGHT_DURATION ) )
            hard_bird["renderer"].add_animation( BIRD_ANIMATION_DEAD,
                                                 GameAnimation( [ GameImage( "gfx/duck_hunt/bird/dead/bird_dead-hard-%d.png" % frame_index, Anchor.CENTER )
                                                                  for frame_index in xrange( NUMBER_BIRD_DEAD_FRAMES ) ],
                                                                NUMBER_BIRD_DEAD_FRAMES / BIRD_ANIMATION_DEAD_DURATION ) )
            hard_bird["renderer"].set_collider_visible( False )
            PrefabFactory.add_prefab( HARD_BIRD_TYPE, hard_bird )

        def create_boom( self ):
            boom = GameObject()
            boom["renderer"] = GameRenderer()
            boom["renderer"].add_animation( BOOM_ANIMATION_FIRE,
                                            GameAnimation( [ GameImage( "gfx/duck_hunt/boom/boom-%d.png" % frame_index, Anchor.CENTER )
                                                             for frame_index in xrange( NUMBER_BOOM_FIRE_FRAMES ) ],
                                                           NUMBER_BOOM_FIRE_FRAMES / BOOM_FIRE_DURATION ) )
            boom["behavior"] = BoomBehavior()
            PrefabFactory.add_prefab( BOOM_TYPE, boom )

        def create_huds( self ):
            self.start_screen_hud             = GameObject()
            self.start_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/duck_hunt/start_screen.png" ) )
            self.start_screen_hud["transform"].set_position( 148, 50 )

            self.stop_screen_hud             = GameObject()
            self.stop_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/duck_hunt/stop_screen.png" ) )
            self.stop_screen_hud["transform"].set_position( 148, 50 )

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

            self.score_hud             = GameObject()
            self.score_hud["renderer"] = GameRenderer( GameText( self.get_score, Color( 255, 255, 255, 255 ) ) )
            self.score_hud["transform"].set_position( 400, 30 )

            self.time_remaining_hud = GameObject()
            self.time_remaining_hud["renderer"] = GameRenderer( GameText( self.get_time_remaining, Color( 255, 255, 255, 255 ) ) )
            self.time_remaining_hud["transform"].set_position( 30, 30 )

            self.top_border = GameObject()
            self.top_border["renderer"] = GameRenderer( GameImage( "gfx/backgrounds/minigame_bg_top_border.png" ) )
            self.top_border["transform"].set_position( 0, 0 )

            self.bottom_border = GameObject()
            self.bottom_border["renderer"] = GameRenderer( GameImage( "gfx/backgrounds/minigame_bg_bottom_border.png" ) )
            self.bottom_border["transform"].set_position( 0, 606 )

        def compute_accuracy_bonus( self ):
            self.accuracy_bonus = 0
            if self.number_clicks > 0:
                hit_percentage = float(self.number_hits) / self.number_clicks

                if hit_percentage >= 0.8:
                    self.accuracy_bonus += HUNT_BASE_ACCURACY_BONUS
                if hit_percentage >= 0.85:
                    self.accuracy_bonus += HUNT_EXTRA_ACCURACY_BONUS
                if hit_percentage >= 0.9:
                    self.accuracy_bonus += HUNT_EXTRA_ACCURACY_BONUS
                if hit_percentage >= 0.95:
                    self.accuracy_bonus += HUNT_EXTRA_ACCURACY_BONUS
                if hit_percentage >= 1:
                    self.accuracy_bonus += (2 * HUNT_EXTRA_ACCURACY_BONUS)

        def get_accuracy_bonus( self ):
            if self.accuracy_bonus == 0:
                return "%20d" % self.accuracy_bonus
            elif self.accuracy_bonus < 1000:
                return "%18d" % self.accuracy_bonus
            else:
                return "%16d" % self.accuracy_bonus

        def get_base_score( self ):
            if self.base_score < 1000:
                return "%20d" % self.base_score
            elif self.base_score < 10000:
                return "%18d" % self.base_score
            else:
                return "%16d" % self.base_score

        def get_score( self ):
            return "Score: %16d" % self.base_score

        def get_time_remaining( self ):
            return "Time Remaining: %d" %  self.time_remaining.get_ceil_value()

        def get_total_score( self ):
            if self.total_score < 1000:
                return "%20d" % self.total_score
            elif self.total_score < 10000:
                return "%18d" % self.total_score
            else:
                return "%16d" % self.total_score
                
        def get_result( self ):
            return self.total_score

        def is_out_of_bounds( self, bird ):
            bird_bounds    = bird["collider"].get_bounds()
            bird_direction = bird["behavior"].direction

            if bird_direction == BIRD_DIRECTION_DOWN:
                return bird_bounds.top > self.get_game_height()
            elif bird_direction == BIRD_DIRECTION_LEFT:
                return bird_bounds.right < 0
            elif bird_direction == BIRD_DIRECTION_RIGHT:
                return bird_bounds.left > self.get_game_width()
            elif bird_direction == BIRD_DIRECTION_UP:
                return bird_bounds.bottom < 0

        def on_bird_death( self, score_value ):
            self.base_score += score_value

        def spawn_bird( self, bird_type ):
            bird_lists = { EASY_BIRD_TYPE   : self.easy_birds,
                           MEDIUM_BIRD_TYPE : self.medium_birds,
                           HARD_BIRD_TYPE   : self.hard_birds }

            # create the new bird.
            speed     = self.bird_speed.get_value()
            scale     = self.bird_scale.get_value()
            direction = renpy.random.choice( [ BIRD_DIRECTION_DOWN,
                                               BIRD_DIRECTION_LEFT,
                                               BIRD_DIRECTION_RIGHT,
                                               BIRD_DIRECTION_UP ] )

            bird             = PrefabFactory.instantiate( bird_type )
            bird["behavior"] = BirdBehavior( direction, speed,
                                             BIRD_HIT_POINTS[bird_type],
                                             BIRD_SCORE_VALUES[bird_type],
                                             self.on_bird_death )

            half_width  = BIRD_ALIVE_SIZE.width / 2
            half_height = BIRD_ALIVE_SIZE.height / 2

            if direction == BIRD_DIRECTION_DOWN:
                x = renpy.random.randint( half_width, self.get_game_width() - half_width )
                y = -half_height
            elif direction == BIRD_DIRECTION_LEFT:
                x = self.get_game_width() + half_width
                y = renpy.random.randint( half_height, self.get_game_height() - half_height )
            elif direction == BIRD_DIRECTION_RIGHT:
                x = -half_width
                y = renpy.random.randint( half_height, self.get_game_height() - half_height )
            elif direction == BIRD_DIRECTION_UP:
                x = renpy.random.randint( half_width, self.get_game_width() - half_width )
                y = self.get_game_height() + half_height

            bird["transform"].set_position( x, y )
            bird["transform"].set_scale( scale )
            bird["behavior"].fly()
            bird_lists[bird_type].append( bird )

        def spawn_boom( self, x, y ):
            boom = PrefabFactory.instantiate( BOOM_TYPE, GameTransform( x, y ) )
            boom["behavior"] = BoomBehavior()
            boom["behavior"].fire()
            self.booms.append( boom )

        def get_displayables( self ):
            displayables = []
            #displayables.extend( self.background["renderer"].get_displayables() )
            displayables.extend( self.player["renderer"].get_displayables() )

            for bird in itertools.chain( self.easy_birds,
                                         self.medium_birds,
                                         self.hard_birds ):
                displayables.extend( bird["renderer"].get_displayables() )

            for boom in self.booms:
                displayables.extend( boom["renderer"].get_displayables() )

            displayables.extend( self.start_screen_hud["renderer"].get_displayables() )
            displayables.extend( self.stop_screen_hud["renderer"].get_displayables() )
            displayables.extend( self.time_remaining_hud["renderer"].get_displayables() )

            return displayables

        def render( self, blitter, clip_rect ):
            world_transform = self.get_world_transform()
            #self.background["renderer"].render( blitter, clip_rect, world_transform )

            if self.state == HUNT_GAME_STATE_BEGIN:
                self.start_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == HUNT_GAME_STATE_PLAY:
                for bird in itertools.chain( self.easy_birds,
                                             self.medium_birds,
                                             self.hard_birds ):
                    bird["renderer"].render( blitter, clip_rect, world_transform )

                for boom in self.booms:
                    boom["renderer"].render( blitter, clip_rect, world_transform )

                self.time_remaining_hud["renderer"].render( blitter, clip_rect, world_transform )
                self.score_hud["renderer"].render( blitter, clip_rect, world_transform )

            elif self.state == HUNT_GAME_STATE_END:
                self.stop_screen_hud["renderer"].render( blitter, clip_rect, world_transform )

            self.player["renderer"].render( blitter, clip_rect, world_transform )

            self.top_border["renderer"].render( blitter, clip_rect, world_transform )
            self.bottom_border["renderer"].render( blitter, clip_rect, world_transform )

        def update( self, delta_sec ):
            if self.state == HUNT_GAME_STATE_COUNTDOWN:
                pass
            elif self.state == HUNT_GAME_STATE_PLAY:
                # update automated parameters.
                self.time_remaining.update( delta_sec )
                self.spawn_time.update( delta_sec )
                self.max_birds.update( delta_sec )
                self.max_easy_birds.update( delta_sec )
                self.max_medium_birds.update( delta_sec )
                self.max_hard_birds.update( delta_sec )

                # update all gunshots.
                for boom in self.booms:
                    boom.update( delta_sec )

                # update all birds.
                for bird in itertools.chain( self.easy_birds,
                                             self.medium_birds,
                                             self.hard_birds ):
                    bird.update( delta_sec )

                # kill those birds that are outside the game screen.
                for bird in itertools.chain( self.easy_birds,
                                             self.medium_birds,
                                             self.hard_birds ):
                    if self.is_out_of_bounds( bird ):
                        bird.kill()

                # see if it's time to add a bird.
                self.bird_countdown -= delta_sec

                if (self.bird_countdown <= 0 and
                    self.time_remaining.get_value() > 0):
                    # get new countdown for next time.
                    self.bird_countdown = self.spawn_time.get_value()

                    # get which bird types are available.
                    bird_types          = []
                    number_easy_birds   = 0
                    number_medium_birds = 0
                    number_hard_birds   = 0

                    # check easy birds.
                    for bird in self.easy_birds:
                        if not bird["behavior"].is_shot_down():
                            number_easy_birds += 1

                    if number_easy_birds < self.max_easy_birds.get_truncated_value():
                        bird_types.append( EASY_BIRD_TYPE )

                    # check medium birds.
                    for bird in self.medium_birds:
                        if not bird["behavior"].is_shot_down():
                            number_medium_birds += 1

                    if number_medium_birds < self.max_medium_birds.get_truncated_value():
                        bird_types.append( MEDIUM_BIRD_TYPE )

                    # check hard birds.
                    for bird in self.hard_birds:
                        if not bird["behavior"].is_shot_down():
                            number_hard_birds += 1

                    if number_hard_birds < self.max_hard_birds.get_truncated_value():
                        bird_types.append( HARD_BIRD_TYPE )

                    number_birds = (number_easy_birds +
                                    number_medium_birds +
                                    number_hard_birds)

                    # only attempt to add a bird if there's a bird of a
                    # particular type that we can add.
                    if bird_types and number_birds < self.max_birds.get_truncated_value():
                        self.spawn_bird( renpy.random.choice( bird_types ) )

                # remove birds that have died.
                self.easy_birds[:]   = [ bird for bird in self.easy_birds if bird.is_alive() ]
                self.medium_birds[:] = [ bird for bird in self.medium_birds if bird.is_alive() ]
                self.hard_birds[:]   = [ bird for bird in self.hard_birds if bird.is_alive() ]

                # remove gunshots that have died.
                self.booms[:] = [ boom for boom in self.booms if boom.is_alive() ]

                # see if it's game over.
                if self.time_remaining.get_value() <= 0:
                    self.state = HUNT_GAME_STATE_END
                    self.compute_accuracy_bonus()
                    self.total_score = self.base_score + self.accuracy_bonus

#        def on_key_down( self, key ):
#            if key == pygame.K_ESCAPE:
#                self.quit()

        def on_mouse_move( self, mx, my ):
            # for whatever reason, Ren'Py sometimes gives (-1,-1) for the mouse
            # position when moving the cursor quickly outside the window.  to
            # avoid sudden movements, simply ignore mouse move events if we get
            # this coordinate.
            if mx != -1 and my != -1:
                if not self.is_in_clip_rect( mx, my ):
                    show_mouse()
                else:
                    hide_mouse()

                mx, my = self.transform_screen_to_world( mx, my )
                self.player["transform"].set_position( mx, my )

        def on_mouse_down( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == HUNT_GAME_STATE_PLAY:
                    mx, my = self.transform_screen_to_world( mx, my )
                    self.spawn_boom( mx, my )
                    self.number_clicks += 1

                    for bird in itertools.chain( self.easy_birds,
                                                 self.medium_birds,
                                                 self.hard_birds ):
                        if (bird["collider"].is_point_inside( mx, my ) and
                            not bird["behavior"].is_shot_down()):
                            bird["behavior"].shoot()
                            self.number_hits += 1

        def on_mouse_up( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == HUNT_GAME_STATE_BEGIN:
                    self.state = HUNT_GAME_STATE_PLAY
                elif self.state == HUNT_GAME_STATE_END:
                    self.quit()

    class BirdBehavior( GameComponent ):
        def __init__( self, direction, speed, number_hit_points, score_value,
                      on_death_callback ):
            self.direction         = direction
            self.speed             = speed
            self.x_velocity        = 0
            self.y_velocity        = 0
            self.number_hit_points = number_hit_points
            self.on_death_callback = on_death_callback
            self.score_value       = score_value

        def die( self ):
            self.state      = BIRD_STATE_DEAD
            self.direction  = BIRD_DIRECTION_DOWN
            self.x_velocity = 0
            self.y_velocity = BIRD_FALL_SPEED
            self.game_object["renderer"].play_animation( BIRD_ANIMATION_DEAD )
            self.game_object["collider"].set_size( BIRD_DEAD_SIZE )
            self.on_death_callback( self.score_value )

        def fly( self ):
            self.state = BIRD_STATE_FLYING

            if self.direction == BIRD_DIRECTION_DOWN:
                self.x_velocity = 0
                self.y_velocity = self.speed
                self.game_object["renderer"].play_animation( BIRD_ANIMATION_FLY_DOWN )
            elif self.direction == BIRD_DIRECTION_LEFT:
                self.x_velocity = -self.speed
                self.y_velocity = 0
                self.game_object["renderer"].play_animation( BIRD_ANIMATION_FLY_LEFT )
            elif self.direction == BIRD_DIRECTION_RIGHT:
                self.x_velocity = self.speed
                self.y_velocity = 0
                self.game_object["renderer"].play_animation( BIRD_ANIMATION_FLY_RIGHT )
            elif self.direction == BIRD_DIRECTION_UP:
                self.x_velocity = 0
                self.y_velocity = -self.speed
                self.game_object["renderer"].play_animation( BIRD_ANIMATION_FLY_UP )

        def is_shot_down( self ):
            if self.direction == BIRD_DIRECTION_RIGHT:
                renpy.log( "Right dead" )
            return self.state == BIRD_STATE_DEAD

        def shoot( self ):
            self.number_hit_points -= 1
            if self.number_hit_points == 0:
                self.die()
            else:
                if self.direction == BIRD_DIRECTION_DOWN:
                    self.game_object["renderer"].play_animation( BIRD_ANIMATION_SHOT_LEFT,
                                                                 loop_animation=False,
                                                                 on_animation_end=self.fly )
                elif self.direction == BIRD_DIRECTION_LEFT:
                    self.game_object["renderer"].play_animation( BIRD_ANIMATION_SHOT_LEFT,
                                                                 loop_animation=False,
                                                                 on_animation_end=self.fly )
                elif self.direction == BIRD_DIRECTION_RIGHT:
                    self.game_object["renderer"].play_animation( BIRD_ANIMATION_SHOT_RIGHT,
                                                                 loop_animation=False,
                                                                 on_animation_end=self.fly )
                elif self.direction == BIRD_DIRECTION_UP:
                    self.game_object["renderer"].play_animation( BIRD_ANIMATION_SHOT_RIGHT,
                                                                 loop_animation=False,
                                                                 on_animation_end=self.fly )

        def update( self, delta_sec ):
            if self.direction == BIRD_DIRECTION_RIGHT:
                renpy.log( "Right start: %s %s" % (self.game_object["transform"].x,
                                                   self.game_object["transform"].y) )
            self.game_object["transform"].x += self.x_velocity * delta_sec
            self.game_object["transform"].y += self.y_velocity * delta_sec
            if self.direction == BIRD_DIRECTION_RIGHT:
                renpy.log( "Right end: %s %s" % (self.game_object["transform"].x,
                                                 self.game_object["transform"].y) )

    class BoomBehavior( GameComponent ):
        def fire( self ):
            self.game_object["renderer"].play_animation( BOOM_ANIMATION_FIRE,
                                                         loop_animation=False,
                                                         on_animation_end=self.on_fire_end )

        def on_fire_end( self ):
            self.game_object.kill()
