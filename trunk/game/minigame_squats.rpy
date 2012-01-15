init python:
    class SquatsLevel( object ):
        def __init__( self, time_limit, initial_marker_speed, max_marker_speed,
                      number_bonus1_reps, number_bonus2_reps, number_bonus3_reps,
                      segment_height, tired_timeout ):
            self.time_limit           = time_limit
            self.initial_marker_speed = initial_marker_speed
            self.max_marker_speed     = max_marker_speed
            self.number_bonus1_reps   = number_bonus1_reps
            self.number_bonus2_reps   = number_bonus2_reps
            self.number_bonus3_reps   = number_bonus3_reps
            self.segment_height       = segment_height
            self.tired_timeout        = tired_timeout

    SQUATS_LEVELS = [
        SquatsLevel( time_limit           = 60,
                     initial_marker_speed = 50,
                     max_marker_speed     = 160,
                     number_bonus1_reps   = 30,
                     number_bonus2_reps   = 40,
                     number_bonus3_reps   = 50,
                     segment_height       = 25,
                     tired_timeout        = 1 )
        ]

    #### DESIGNERS: DO NOT CHANGE ANYTHING BEYOND THIS LINE ####

    # different states the Hunt Duck game can be in.
    SQUATS_GAME_STATE_BEGIN = "power_begin"
    SQUATS_GAME_STATE_PLAY  = "power_play"
    SQUATS_GAME_STATE_END   = "power_end"

    RIKU_ANIMATION_LIFTING = "riku_lifting"
    RIKU_ANIMATION_TIRED   = "riku_tired"

    RIKU_ANIMATION_LIFTING_END_FRAME_DURATION    = 0.25
    RIKU_ANIMATION_LIFTING_MIDDLE_FRAME_DURATION = 0.15
    RIKU_ANIMATION_TIRED_DURATION                = 0.35

    NUMBER_RIKU_LIFTING_IMAGES = 4
    NUMBER_RIKU_TIRED_FRAMES   = 3

    SEGMENT_FRAMESET_ACTIVE   = "segment_active"
    SEGMENT_FRAMESET_INACTIVE = "segment_inactive"

    # point values.
    SQUATS_REP_POINT_VALUE   = 100
    SQUATS_COMPLETION_BONUS1 = 300
    SQUATS_COMPLETION_BONUS2 = 500
    SQUATS_COMPLETION_BONUS3 = 1000

    # riku states.
    RIKU_STATE_LIFTING = "riku_lifting"
    RIKU_STATE_TIRED   = "riku_tired"

    SQUATS_SEGMENT_WIDTH = 9
    SQUATS_SEGMENT_COLOR = Color( 0, 215, 0, 255 )

    SQUATS_BAR_X = 20
    SQUATS_BAR_Y = 295

    # 80 is half the height of the riku image after it has been scaled up by 2x.
    SQUATS_RIKU_X = 327
    SQUATS_RIKU_Y = SQUATS_BAR_Y + 80

    # 84 is the offset from the left edge of the bar image to the left edge of
    # the bar marker.
    SQUATS_MARKER_X = 84 + SQUATS_BAR_X

    # 64 is offset from top of the bar image to the top black bar the marker
    # moves along.  150 is half the height of the bar image, to account for
    # the fact that SQUATS_BAR_Y is anchored in the middle of the bar image.
    # 176 is the height of the bar the bar maker moves along.
    SQUATS_MARKER_MIN_Y = 64 + SQUATS_BAR_Y - 150
    SQUATS_MARKER_MAX_Y = SQUATS_MARKER_MIN_Y + 176

    # 62 is the offset from the left edge of the bar image to the left edge of
    # one of the target segments in the bar.
    SQUATS_SEGMENT_X  = 62 + SQUATS_BAR_X
    SQUATS_SEGMENT_Y1 = SQUATS_MARKER_MIN_Y + 1 * 176 / 7
    SQUATS_SEGMENT_Y2 = SQUATS_MARKER_MIN_Y + 3 * 176 / 7
    SQUATS_SEGMENT_Y3 = SQUATS_MARKER_MIN_Y + 5 * 176 / 7

    SQUATS_SEGMENT_INDEX_TOP    = 0
    SQUATS_SEGMENT_INDEX_MIDDLE = 1
    SQUATS_SEGMENT_INDEX_BOTTOM = 2

    class Squats( Minigame ):
        def __init__( self, level_number=1 ):
            super( Squats, self ).__init__()

            if level_number > len( SQUATS_LEVELS ) or level_number <= 0:
                raise ValueError( "Invalid Magic Power level number %d.  Level "
                                  "number must be between 1 and %d." %
                                  (level_number, len( SQUATS_LEVELS )) )

            # setup the level difficulty parameters.
            level = SQUATS_LEVELS[level_number - 1]

            self.time_remaining = AutomatedInterpolator( level.time_limit,
                                                         0,
                                                         level.time_limit )

            # setup the game state.
            self.state              = SQUATS_GAME_STATE_BEGIN
            self.base_score         = 0
            self.completion_bonus   = 0
            self.total_score        = 0
            self.number_bonus1_reps = level.number_bonus1_reps
            self.number_bonus2_reps = level.number_bonus2_reps
            self.number_bonus3_reps = level.number_bonus3_reps

            # setup the entities.
            #self.background           = None
            self.start_screen_hud     = None
            self.stop_screen_hud      = None
            self.score_hud            = None
            self.time_remaining_hud   = None
            self.bar                  = None
            self.bar_segments         = []
            self.active_segment_index = None
            self.riku                 = None

            #self.create_background()
            self.create_huds()
            self.create_bar( level )
            self.create_riku( level )

        def create_background( self ):
            self.background             = GameObject()
            self.background["renderer"] = GameRenderer( GameImage( "gfx/squats/background.jpg" ) )

        def create_huds( self ):
            self.start_screen_hud             = GameObject()
            self.start_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/squats/start_screen.png" ) )
            self.start_screen_hud["transform"].set_position( 148, 50 )

            self.stop_screen_hud             = GameObject()
            self.stop_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/squats/stop_screen.png" ) )
            self.stop_screen_hud["transform"].set_position( 148, 50 )

            base_score             = GameObject()
            base_score["renderer"] = GameRenderer( GameText( self.get_base_score, Color( 255, 255, 255, 255 ) ) )
            base_score["transform"].set_position( 185, 159 )
            self.stop_screen_hud.add_child( base_score )

            completion_bonus             = GameObject()
            completion_bonus["renderer"] = GameRenderer( GameText( self.get_completion_bonus, Color( 255, 255, 255, 255 ) ) )
            completion_bonus["transform"].set_position( 185, 251 )
            self.stop_screen_hud.add_child( completion_bonus )

            total_score             = GameObject()
            total_score["renderer"] = GameRenderer( GameText( self.get_total_score, Color( 255, 255, 255, 255 ) ) )
            total_score["transform"].set_position( 185, 320 )
            self.stop_screen_hud.add_child( total_score )

            self.score_hud             = GameObject()
            self.score_hud["renderer"] = GameRenderer( GameText( self.get_score, Color( 255, 255, 255, 255 ) ) )
            self.score_hud["transform"].set_position( 400, 30 )

            self.time_remaining_hud             = GameObject()
            self.time_remaining_hud["renderer"] = GameRenderer( GameText( self.get_time_remaining, Color( 255, 255, 255, 255 ) ) )
            self.time_remaining_hud["transform"].set_position( 30, 30 )

        def create_bar( self, level ):
            self.bar             = GameObject()
            self.bar["renderer"] = GameRenderer( GameImage( "gfx/squats/bar.png", Anchor.LEFT ) )
            self.bar["transform"].set_position( SQUATS_BAR_X, SQUATS_BAR_Y )

            for segment_y, target_key, successor_index in ( (SQUATS_SEGMENT_Y1, pygame.K_UP, SQUATS_SEGMENT_INDEX_BOTTOM),
                                                            (SQUATS_SEGMENT_Y2, pygame.K_LEFT, SQUATS_SEGMENT_INDEX_TOP),
                                                            (SQUATS_SEGMENT_Y3, pygame.K_DOWN, SQUATS_SEGMENT_INDEX_MIDDLE) ):
                bar_segment = GameObject()
                bar_segment["renderer"] = GameRenderer()
                bar_segment["behavior"] = SegmentBehavior( level.segment_height, target_key, successor_index )
                bar_segment["renderer"].set_frame( SEGMENT_FRAMESET_INACTIVE,
                                                   GameRect( Size( SQUATS_SEGMENT_WIDTH, level.segment_height ),
                                                             Color( 0, 100, 0, 255 ),
                                                             Anchor.TOP_LEFT ) )
                bar_segment["renderer"].set_frame( SEGMENT_FRAMESET_ACTIVE,
                                                   GameRect( Size( SQUATS_SEGMENT_WIDTH, level.segment_height ),
                                                             Color( 0, 235, 0, 255 ),
                                                             Anchor.TOP_LEFT ) )
                bar_segment["renderer"].set_frameset( SEGMENT_FRAMESET_INACTIVE )
                bar_segment["transform"].set_position( SQUATS_SEGMENT_X, segment_y )
                self.bar_segments.append( bar_segment )

            self.bar_segments[SQUATS_SEGMENT_INDEX_BOTTOM]["behavior"].activate()
            self.active_segment_index = SQUATS_SEGMENT_INDEX_BOTTOM

            self.marker             = GameObject()
            self.marker["renderer"] = GameRenderer( GameImage( "gfx/squats/marker.png", Anchor.LEFT ) )
            self.marker["behavior"] = MarkerBehavior( SQUATS_MARKER_MIN_Y, SQUATS_MARKER_MAX_Y,
                                                      level.initial_marker_speed, level.max_marker_speed )
            self.marker["transform"].set_position( SQUATS_MARKER_X, SQUATS_MARKER_MAX_Y )

        def create_riku( self, level ):
            lifting_images                                   = [ GameImage( "gfx/squats/riku/riku-lifting%d.png" % image_index, Anchor.BOTTOM )
                                                                 for image_index in xrange( NUMBER_RIKU_LIFTING_IMAGES ) ]
            lifting_frames                                   = lifting_images[0:-1] + lifting_images[NUMBER_RIKU_LIFTING_IMAGES - 1:0:-1]
            lifting_timing                                   = [ None ] * len( lifting_frames )
            lifting_timing[0]                                = RIKU_ANIMATION_LIFTING_END_FRAME_DURATION
            lifting_timing[-1]                               = RIKU_ANIMATION_LIFTING_END_FRAME_DURATION
            lifting_timing[NUMBER_RIKU_LIFTING_IMAGES - 1]   = RIKU_ANIMATION_LIFTING_END_FRAME_DURATION
            lifting_timing[1:NUMBER_RIKU_LIFTING_IMAGES - 1] = [ RIKU_ANIMATION_LIFTING_MIDDLE_FRAME_DURATION ] * (NUMBER_RIKU_LIFTING_IMAGES - 2)
            lifting_timing[NUMBER_RIKU_LIFTING_IMAGES:-1]    = [ RIKU_ANIMATION_LIFTING_MIDDLE_FRAME_DURATION ] * (NUMBER_RIKU_LIFTING_IMAGES - 2)

            self.riku             = GameObject()
            self.riku["renderer"] = GameRenderer( GameImage( "gfx/squats/riku/riku.png", Anchor.BOTTOM ) )
            self.riku["behavior"] = SquatsRikuBehavior( level.tired_timeout )
            self.riku["renderer"].add_animation( RIKU_ANIMATION_LIFTING,
                                                 GameAnimation( lifting_frames,
                                                                timing_info=lifting_timing ) )
            self.riku["renderer"].add_animation( RIKU_ANIMATION_TIRED,
                                                 GameAnimation( [ GameImage( "gfx/squats/riku/riku-tired%d.png" % frame_index, Anchor.BOTTOM )
                                                                  for frame_index in xrange( NUMBER_RIKU_TIRED_FRAMES ) ],
                                                                NUMBER_RIKU_TIRED_FRAMES / RIKU_ANIMATION_TIRED_DURATION ) )
            self.riku["transform"].set_position( SQUATS_RIKU_X, SQUATS_RIKU_Y )
            self.riku["transform"].set_scale( 2.0 )

        def compute_scores( self ):
            number_reps = self.base_score / SQUATS_REP_POINT_VALUE

            if number_reps >= self.number_bonus3_reps:
                self.completion_bonus += SQUATS_COMPLETION_BONUS3
            elif number_reps >= self.number_bonus2_reps:
                self.completion_bonus += SQUATS_COMPLETION_BONUS2
            elif number_reps >= self.number_bonus1_reps:
                self.completion_bonus += SQUATS_COMPLETION_BONUS1

            self.total_score = self.base_score + self.completion_bonus

        def get_score( self ):
            return "Score: %16d" % self.base_score

        def get_time_remaining( self ):
            return "Time Remaining: %d" %  self.time_remaining.get_ceil_value()

        def get_base_score( self ):
            if self.base_score < 1000:
                return "%20d" % self.base_score
            elif self.base_score < 10000:
                return "%18d" % self.base_score
            else:
                return "%16d" % self.base_score

        def get_completion_bonus( self ):
            if self.completion_bonus == 0:
                return "%20d" % self.completion_bonus
            elif self.completion_bonus < 1000:
                return "%18d" % self.completion_bonus
            else:
                return "%16d" % self.completion_bonus

        def get_total_score( self ):
            if self.total_score < 1000:
                return "%20d" % self.total_score
            elif self.total_score < 10000:
                return "%18d" % self.total_score
            else:
                return "%16d" % self.total_score
                
        def get_result( self ):
            return self.total_score

        def get_displayables( self ):
            displayables = []
            displayables.extend( self.riku["renderer"].get_displayables() )
            displayables.extend( self.bar["renderer"].get_displayables() )
            displayables.extend( self.marker["renderer"].get_displayables() )
            displayables.extend( self.score_hud["renderer"].get_displayables() )
            displayables.extend( self.time_remaining_hud["renderer"].get_displayables() )
            return displayables

        def render( self, blitter, clip_rect ):
            world_transform = self.get_world_transform()
            #self.background["renderer"].render( blitter, clip_rect, world_transform )

            self.riku["renderer"].render( blitter, clip_rect, world_transform )

            self.bar["renderer"].render( blitter, clip_rect, world_transform )
            for bar_segment in self.bar_segments:
                bar_segment["renderer"].render( blitter, clip_rect, world_transform )
            self.marker["renderer"].render( blitter, clip_rect, world_transform )

            if self.state == SQUATS_GAME_STATE_BEGIN:
                self.start_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == SQUATS_GAME_STATE_PLAY:
                self.time_remaining_hud["renderer"].render( blitter, clip_rect, world_transform )
                self.score_hud["renderer"].render( blitter, clip_rect, world_transform )

            elif self.state == SQUATS_GAME_STATE_END:
                self.stop_screen_hud["renderer"].render( blitter, clip_rect, world_transform )

        def update( self, delta_sec ):
            if self.state == SQUATS_GAME_STATE_PLAY:
                # update automated parameters.
                self.time_remaining.update( delta_sec )

                # update entities.
                self.riku.update( delta_sec )
                self.marker.update( delta_sec )

                # see if it's game over.
                if self.time_remaining.get_value() <= 0:
                    self.state = SQUATS_GAME_STATE_END
                    self.compute_scores()

        def on_key_down( self, key ):
            if key == pygame.K_ESCAPE:
                self.quit()

            if self.state == SQUATS_GAME_STATE_PLAY:
                if (key in (pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN) and
                    not self.riku["behavior"].is_tired()):
                    active_segment = self.bar_segments[self.active_segment_index]

                    if (active_segment["behavior"].is_in_bounds( self.marker["transform"].y ) and
                        key == active_segment["behavior"].target_key):
                        successor_index           = active_segment["behavior"].successor_index
                        successor_segment         = self.bar_segments[successor_index]
                        self.active_segment_index = successor_index
                        active_segment["behavior"].deactivate()
                        successor_segment["behavior"].activate()

                        if successor_index == SQUATS_SEGMENT_INDEX_BOTTOM:
                            self.base_score += SQUATS_REP_POINT_VALUE
                    else:
                        self.riku["behavior"].tire()
                        active_segment["behavior"].deactivate()
                        self.bar_segments[SQUATS_SEGMENT_INDEX_BOTTOM]["behavior"].activate()
                        self.active_segment_index = SQUATS_SEGMENT_INDEX_BOTTOM

        def on_mouse_up( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == SQUATS_GAME_STATE_BEGIN:
                    self.state = SQUATS_GAME_STATE_PLAY
                    self.riku["renderer"].play_animation( RIKU_ANIMATION_LIFTING,
                                                          loop_animation=True )
                elif self.state == SQUATS_GAME_STATE_END:
                    self.quit()

    class MarkerBehavior( GameComponent ):
        def __init__( self, min_value, max_value, initial_speed, max_speed ):
            super( MarkerBehavior, self ).__init__()
            self.min_value     = min_value
            self.max_value     = max_value
            self.initial_speed = initial_speed
            self.max_speed     = max_speed
            self.speed         = initial_speed
            self.acceleration  = 200

        def update( self, delta_sec ):
            dv         = self.acceleration * delta_sec
            self.speed = min( self.speed + dv, self.max_speed )
            dy         = self.speed * delta_sec
            y          = self.game_object["transform"].y - dy
            # if y > self.max_value:
            #     y = self.max_value - (y - self.max_value)
            #     self.velocity *= -1
            # elif y < self.min_value:
            #     y = self.min_value + (self.min_value - y)
            #     self.velocity *= -1
            if y < self.min_value:
                y          = self.max_value
                self.speed = self.initial_speed
            self.game_object["transform"].y = y

    class SegmentBehavior( GameComponent ):
        def __init__( self, height, target_key, successor_index ):
            super( SegmentBehavior, self ).__init__()
            self.height          = height
            self.target_key      = target_key
            self.successor_index = successor_index

        def activate( self ):
            self.game_object["renderer"].set_frameset( SEGMENT_FRAMESET_ACTIVE )

        def deactivate( self ):
            self.game_object["renderer"].set_frameset( SEGMENT_FRAMESET_INACTIVE )

        def is_in_bounds( self, y ):
            min_y = self.game_object["transform"].y
            max_y = min_y + self.height
            return min_y <= y <= max_y

    class SquatsRikuBehavior():
        def __init__( self, tired_timeout ):
            self.state         = RIKU_STATE_LIFTING
            self.tired_timeout = tired_timeout
            self.countdown     = 0

        def update( self, delta_sec ):
            if self.state == RIKU_STATE_TIRED:
                self.countdown -= delta_sec
                if self.countdown <= 0:
                    self.state = RIKU_STATE_LIFTING
                    self.game_object["renderer"].play_animation( RIKU_ANIMATION_LIFTING )

        def tire( self ):
            self.state     = RIKU_STATE_TIRED
            self.countdown = self.tired_timeout
            self.game_object["renderer"].play_animation( RIKU_ANIMATION_TIRED )

        def is_tired( self ):
            return self.state == RIKU_STATE_TIRED
