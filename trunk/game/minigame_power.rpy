init python:
    class MagicPowerLevel( object ):
        def __init__( self, time_limit, marker_speed, misfire_timeout,
                      near_shot_timeout, middle_shot_timeout, far_shot_timeout ):
            self.time_limit          = time_limit
            self.marker_speed        = marker_speed
            self.misfire_timeout     = misfire_timeout
            self.near_shot_timeout   = near_shot_timeout
            self.middle_shot_timeout = middle_shot_timeout
            self.far_shot_timeout    = far_shot_timeout

    MAGIC_POWER_LEVELS = [
        MagicPowerLevel( time_limit          = 60,
                         marker_speed        = 300,
                         misfire_timeout     = 1.0,
                         near_shot_timeout   = 0.25,
                         middle_shot_timeout = 0.5,
                         far_shot_timeout    = 0.75 ),

        MagicPowerLevel( time_limit          = 60,
                         marker_speed        = 325,
                         misfire_timeout     = 0.8,
                         near_shot_timeout   = 0.23,
                         middle_shot_timeout = 0.4,
                         far_shot_timeout    = 0.7 )
        ]

    #### DESIGNERS: DO NOT CHANGE ANYTHING BEYOND THIS LINE ####

    # different states the Hunt Duck game can be in.
    MAGIC_POWER_GAME_STATE_BEGIN = "power_begin"
    MAGIC_POWER_GAME_STATE_PLAY  = "power_play"
    MAGIC_POWER_GAME_STATE_END   = "power_end"

    # framesets.
    POWER_TARGET_NEAR_UNDAMAGED_FRAMESET   = "near_undamaged"
    POWER_TARGET_MIDDLE_UNDAMAGED_FRAMESET = "middle_undamaged"
    POWER_TARGET_FAR_UNDAMAGED_FRAMESET    = "far_undamaged"
    POWER_TARGET_NEAR_DAMAGED_FRAMESET     = "near_damaged"
    POWER_TARGET_MIDDLE_DAMAGED_FRAMESET   = "middle_damaged"
    POWER_TARGET_FAR_DAMAGED_FRAMESET      = "far_damaged"

    MESSAGE_CHARGING_FRAMESET  = "message_charging"
    MESSAGE_FIRING_FRAMESET    = "message_firing"
    MESSAGE_HIT_FRAMESET       = "message_hit"
    MESSAGE_MISS_FRAMESET      = "message_miss"
    MESSAGE_DESTROYED_FRAMESET = "message_destroyed"
    MESSAGE_MISFIRE_FRAMESET   = "message_misfire"

    # points.
    EASY_TARGET_POINT_VALUE   = 100
    MEDIUM_TARGET_POINT_VALUE = 300
    HARD_TARGET_POINT_VALUE   = 500

    # hit points.
    EASY_TARGET_HIT_POINTS   = 1
    MEDIUM_TARGET_HIT_POINTS = 3
    HARD_TARGET_HIT_POINTS   = 5

    # prefabs.
    POWER_TARGET_TYPE = "power_target"

    # target types.
    TARGET_TYPE_NEAR   = "near_target"
    TARGET_TYPE_MIDDLE = "middle_target"
    TARGET_TYPE_FAR    = "far_target"

    # shot types.
    MISFIRE_SHOT_TYPE = "misfire_shot"
    NEAR_SHOT_TYPE    = "near_shot"
    MIDDLE_SHOT_TYPE  = "middle_shot"
    FAR_SHOT_TYPE     = "far_shot"

    # marker states.
    MARKER_STATE_IDLE   = "marker_idle"
    MARKER_STATE_MOVING = "marker_moving"
    MARKER_STATE_FROZEN = "marker_frozen"

    FORCE_BAR_X = 20
    FORCE_BAR_Y = 295
    POWER_BAR_X = 500
    POWER_BAR_Y = 295

    # 84 is the offset from the left edge of the bar image to the left edge of
    # the bar marker.
    FORCE_MARKER_X = 84 + FORCE_BAR_X
    POWER_MARKER_X = 84 + POWER_BAR_X

    # 64 is offset from top of the bar image to the top black bar the marker
    # moves along.  150 is half the height of the bar image, to account for
    # the fact that FORCE_BAR_Y is anchored in the middle of the bar image.
    # 176 is the height of the bar the bar maker moves along.
    FORCE_MARKER_MIN_Y = 64 + FORCE_BAR_Y - 150
    FORCE_MARKER_MAX_Y = FORCE_MARKER_MIN_Y + 176
    POWER_MARKER_MIN_Y = 64 + POWER_BAR_Y - 150
    POWER_MARKER_MAX_Y = POWER_MARKER_MIN_Y + 176

    POWER_TARGET_X = 324
    POWER_TARGET_Y = 296

    # 57 is the height of each section on the force bar.
    FORCE_MIN_NEAR_RANGE = FORCE_MARKER_MIN_Y
    FORCE_MAX_NEAR_RANGE = FORCE_MIN_NEAR_RANGE + 57

    FORCE_MIN_MIDDLE_RANGE = FORCE_MAX_NEAR_RANGE
    FORCE_MAX_MIDDLE_RANGE = FORCE_MIN_MIDDLE_RANGE + 57

    FORCE_MIN_FAR_RANGE = FORCE_MAX_MIDDLE_RANGE
    FORCE_MAX_FAR_RANGE = FORCE_MIN_FAR_RANGE + 57

    # 12 is the height of the super hit section.  24 is the height of the
    # perfect hit section.  47 is the height of the ok hit section.  91
    # is the height of the misfire section.
    POWER_MIN_SUPER_HIT = POWER_MARKER_MIN_Y
    POWER_MAX_SUPER_HIT = POWER_MIN_SUPER_HIT + 12

    POWER_MIN_PERFECT_HIT = POWER_MAX_SUPER_HIT
    POWER_MAX_PERFECT_HIT = POWER_MIN_PERFECT_HIT + 24

    POWER_MIN_OK_HIT = POWER_MAX_PERFECT_HIT
    POWER_MAX_OK_HIT = POWER_MIN_OK_HIT + 47

    POWER_MIN_MISFIRE = POWER_MAX_OK_HIT
    POWER_MAX_MISFIRE = POWER_MIN_MISFIRE + 91

    class MagicPower( Minigame ):
        def __init__( self, level_number=1 ):
            super( MagicPower, self ).__init__()

            if level_number > len( MAGIC_POWER_LEVELS ) or level_number <= 0:
                raise ValueError( "Invalid Magic Power level number %d.  Level "
                                  "number must be between 1 and %d." %
                                  (level_number, len( MAGIC_POWER_LEVELS )) )

            # setup the level difficulty parameters.
            level = MAGIC_POWER_LEVELS[level_number - 1]

            self.time_remaining = AutomatedInterpolator( level.time_limit,
                                                         0,
                                                         level.time_limit )

            # setup the game state.
            self.state               = MAGIC_POWER_GAME_STATE_BEGIN
            self.base_score          = 0
            self.total_score         = 0
            self.misfire_timeout     = level.misfire_timeout
            self.near_shot_timeout   = level.near_shot_timeout
            self.middle_shot_timeout = level.middle_shot_timeout
            self.far_shot_timeout    = level.far_shot_timeout
            self.action_countdown    = 0

            # setup the entities.
            self.background         = None
            self.start_screen_hud   = None
            self.stop_screen_hud    = None
            self.score_hud          = None
            self.time_remaining_hud = None
            self.message_hud        = None
            self.force_bar          = None
            self.force_marker       = None
            self.power_bar          = None
            self.power_marker       = None
            self.target             = None
            self.shot_type          = None

            self.create_background()
            self.create_huds()
            self.create_bars( level )
            self.create_target()

            self.spawn_target()

        def create_background( self ):
            self.background             = GameObject()
            self.background["renderer"] = GameRenderer( GameImage( "gfx/magic_power/background.jpg" ) )

        def create_huds( self ):
            self.start_screen_hud             = GameObject()
            self.start_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/magic_power/start_screen.png" ) )
            self.start_screen_hud["transform"].set_position( 138, 50 )

            self.stop_screen_hud             = GameObject()
            self.stop_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/magic_power/stop_screen.png" ) )
            self.stop_screen_hud["transform"].set_position( 138, 50 )

            base_score             = GameObject()
            base_score["renderer"] = GameRenderer( GameText( self.get_base_score, Color( 255, 255, 255, 255 ) ) )
            base_score["transform"].set_position( 185, 159 )
            self.stop_screen_hud.add_child( base_score )

            total_score             = GameObject()
            total_score["renderer"] = GameRenderer( GameText( self.get_total_score, Color( 255, 255, 255, 255 ) ) )
            total_score["transform"].set_position( 185, 320 )
            self.stop_screen_hud.add_child( total_score )

            self.score_hud             = GameObject()
            self.score_hud["renderer"] = GameRenderer( GameText( self.get_score, Color( 255, 255, 255, 255 ) ) )
            self.score_hud["transform"].set_position( 400, 10 )

            self.time_remaining_hud             = GameObject()
            self.time_remaining_hud["renderer"] = GameRenderer( GameText( self.get_time_remaining, Color( 255, 255, 255, 255 ) ) )
            self.time_remaining_hud["transform"].set_position( 10, 10 )

            self.message_hud = GameObject()
            self.message_hud["renderer"] = GameRenderer()
            self.message_hud["renderer"].set_frame( MESSAGE_CHARGING_FRAMESET, GameText( lambda : "Charging", Color( 255, 255, 255, 255 ) ) )
            self.message_hud["renderer"].set_frame( MESSAGE_FIRING_FRAMESET, GameText( lambda : "Firing", Color( 255, 255, 255, 255 ) ) )
            self.message_hud["renderer"].set_frame( MESSAGE_HIT_FRAMESET, GameText( lambda : "Hit", Color( 255, 255, 255, 255 ) ) )
            self.message_hud["renderer"].set_frame( MESSAGE_MISS_FRAMESET, GameText( lambda : "Miss", Color( 255, 255, 255, 255 ) ) )
            self.message_hud["renderer"].set_frame( MESSAGE_DESTROYED_FRAMESET, GameText( lambda : "Destroyed", Color( 255, 255, 255, 255 ) ) )
            self.message_hud["renderer"].set_frame( MESSAGE_MISFIRE_FRAMESET, GameText( lambda : "Misfire", Color( 255, 255, 255, 255 ) ) )
            self.message_hud["transform"].set_position( 10, 40 )

        def create_bars( self, level ):
            self.force_bar             = GameObject()
            self.force_bar["renderer"] = GameRenderer( GameImage( "gfx/magic_power/force_bar.png", Anchor.LEFT ) )
            self.force_bar["transform"].set_position( FORCE_BAR_X, FORCE_BAR_Y )

            self.force_marker             = GameObject()
            self.force_marker["renderer"] = GameRenderer( GameImage( "gfx/magic_power/marker.png", Anchor.LEFT ) )
            self.force_marker["behavior"] = MagicPowerMarkerBehavior( FORCE_MARKER_MIN_Y, FORCE_MARKER_MAX_Y,
                                                                      level.marker_speed )
            self.force_marker["transform"].set_position( FORCE_MARKER_X, FORCE_MARKER_MAX_Y )

            self.power_bar             = GameObject()
            self.power_bar["renderer"] = GameRenderer( GameImage( "gfx/magic_power/power_bar.png", Anchor.LEFT ) )
            self.power_bar["transform"].set_position( POWER_BAR_X, POWER_BAR_Y )

            self.power_marker             = GameObject()
            self.power_marker["renderer"] = GameRenderer( GameImage( "gfx/magic_power/marker.png", Anchor.LEFT ) )
            self.power_marker["behavior"] = MagicPowerMarkerBehavior( POWER_MARKER_MIN_Y, POWER_MARKER_MAX_Y,
                                                                      level.marker_speed )
            self.power_marker["transform"].set_position( POWER_MARKER_X, POWER_MARKER_MAX_Y )

        def create_target( self ):
            target             = GameObject()
            target["renderer"] = GameRenderer()
            target["renderer"].set_frame( POWER_TARGET_NEAR_UNDAMAGED_FRAMESET, GameImage( "gfx/magic_power/near_target-undamaged.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_MIDDLE_UNDAMAGED_FRAMESET, GameImage( "gfx/magic_power/middle_target-undamaged.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_FAR_UNDAMAGED_FRAMESET, GameImage( "gfx/magic_power/far_target-undamaged.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_NEAR_DAMAGED_FRAMESET, GameImage( "gfx/magic_power/near_target-damaged.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_MIDDLE_DAMAGED_FRAMESET, GameImage( "gfx/magic_power/middle_target-damaged.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_FAR_DAMAGED_FRAMESET, GameImage( "gfx/magic_power/far_target-damaged.png", Anchor.CENTER ) )
            PrefabFactory.add_prefab( POWER_TARGET_TYPE, target )

        def spawn_target( self ):
            target_type = renpy.random.choice( [ TARGET_TYPE_NEAR,
                                                 TARGET_TYPE_MIDDLE,
                                                 TARGET_TYPE_FAR ] )
            number_hit_points = renpy.random.choice( [ EASY_TARGET_HIT_POINTS,
                                                       MEDIUM_TARGET_HIT_POINTS,
                                                       HARD_TARGET_HIT_POINTS ] )

            if number_hit_points == EASY_TARGET_HIT_POINTS:
                point_value = EASY_TARGET_POINT_VALUE
            elif number_hit_points == MEDIUM_TARGET_HIT_POINTS:
                point_value = MEDIUM_TARGET_POINT_VALUE
            elif number_hit_points == HARD_TARGET_HIT_POINTS:
                point_value = HARD_TARGET_POINT_VALUE

            self.target             = PrefabFactory.instantiate( POWER_TARGET_TYPE )
            self.target["behavior"] = PowerTargetBehavior( target_type, number_hit_points, point_value )
            self.target["behavior"].update_frameset()
            self.target["transform"].set_position( POWER_TARGET_X, POWER_TARGET_Y )

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
            displayables.extend( self.score_hud["renderer"].get_displayables() )
            displayables.extend( self.time_remaining_hud["renderer"].get_displayables() )
            displayables.extend( self.force_bar["renderer"].get_displayables() )
            displayables.extend( self.force_marker["renderer"].get_displayables() )
            displayables.extend( self.power_bar["renderer"].get_displayables() )
            displayables.extend( self.power_marker["renderer"].get_displayables() )
            if self.target:
                displayables.extend( self.target["renderer"].get_displayables() )
            return displayables

        def render( self, blitter, clip_rect ):
            world_transform = self.get_world_transform()
            self.background["renderer"].render( blitter, clip_rect, world_transform )

            if self.state == MAGIC_POWER_GAME_STATE_BEGIN:
                self.start_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == MAGIC_POWER_GAME_STATE_PLAY:
                self.force_bar["renderer"].render( blitter, clip_rect, world_transform )
                self.force_marker["renderer"].render( blitter, clip_rect, world_transform )
                self.power_bar["renderer"].render( blitter, clip_rect, world_transform )
                self.power_marker["renderer"].render( blitter, clip_rect, world_transform )
                self.message_hud["renderer"].render( blitter, clip_rect, world_transform )
                if self.target:
                    self.target["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == MAGIC_POWER_GAME_STATE_END:
                self.stop_screen_hud["renderer"].render( blitter, clip_rect, world_transform )

            self.time_remaining_hud["renderer"].render( blitter, clip_rect, world_transform )
            self.score_hud["renderer"].render( blitter, clip_rect, world_transform )

        def update( self, delta_sec ):
            if self.state == MAGIC_POWER_GAME_STATE_PLAY:
                # update automated parameters.
                self.time_remaining.update( delta_sec )

                # update entities.
                self.force_marker.update( delta_sec )
                self.power_marker.update( delta_sec )

                if self.action_countdown > 0:
                    self.action_countdown -= delta_sec

                if self.action_countdown <= 0 and self.shot_type is not None:
                    if self.target:
                        power_position = self.power_marker["transform"].y

                        if POWER_MIN_SUPER_HIT <= power_position < POWER_MAX_SUPER_HIT:
                            damage = 3
                        elif POWER_MIN_PERFECT_HIT <= power_position < POWER_MAX_PERFECT_HIT:
                            damage = 1
                        elif POWER_MIN_OK_HIT <= power_position < POWER_MAX_OK_HIT:
                            damage = 0.5

                        if (self.shot_type == NEAR_SHOT_TYPE and
                            self.target["behavior"].type == TARGET_TYPE_NEAR or
                            self.shot_type == MIDDLE_SHOT_TYPE and
                            self.target["behavior"].type == TARGET_TYPE_MIDDLE or
                            self.shot_type == FAR_SHOT_TYPE and
                            self.target["behavior"].type == TARGET_TYPE_FAR):
                            self.target["behavior"].hit( damage )
                            self.message_hud["renderer"].set_frameset( MESSAGE_HIT_FRAMESET )


                            if self.target["behavior"].number_hit_points <= 0:
                                self.message_hud["renderer"].set_frameset( MESSAGE_DESTROYED_FRAMESET )
                                self.base_score += self.target["behavior"].get_point_value()
                                self.spawn_target()
                        elif self.shot_type != MISFIRE_SHOT_TYPE:
                            self.message_hud["renderer"].set_frameset( MESSAGE_MISS_FRAMESET )

                    self.shot_type = None
                    self.force_marker["behavior"].reset()
                    self.power_marker["behavior"].reset()
                elif (self.force_marker["behavior"].state == MARKER_STATE_FROZEN and
                      self.power_marker["behavior"].state == MARKER_STATE_FROZEN and
                      self.shot_type is None):
                    # check for misfire.
                    force_position = self.force_marker["transform"].y
                    power_position = self.power_marker["transform"].y

                    if POWER_MIN_MISFIRE <= power_position < POWER_MAX_MISFIRE:
                        self.message_hud["renderer"].set_frameset( MESSAGE_MISFIRE_FRAMESET )
                        self.action_countdown = self.misfire_timeout
                        self.shot_type        = MISFIRE_SHOT_TYPE
                    else:
                        # we didn't misfire.  we're shooting something.
                        self.message_hud["renderer"].set_frameset( MESSAGE_FIRING_FRAMESET )
                        if FORCE_MIN_NEAR_RANGE <= force_position < FORCE_MAX_NEAR_RANGE:
                            self.action_countdown = self.near_shot_timeout
                            self.shot_type        = NEAR_SHOT_TYPE
                        elif FORCE_MIN_MIDDLE_RANGE <= force_position < FORCE_MAX_MIDDLE_RANGE:
                            self.action_countdown = self.middle_shot_timeout
                            self.shot_type        = MIDDLE_SHOT_TYPE
                        elif FORCE_MIN_FAR_RANGE <= force_position < FORCE_MAX_FAR_RANGE:
                            self.action_countdown = self.far_shot_timeout
                            self.shot_type        = FAR_SHOT_TYPE

                # see if it's game over.
                if self.time_remaining.get_value() <= 0:
                    self.state = MAGIC_POWER_GAME_STATE_END
                    self.total_score = self.base_score

        def on_key_down( self, key ):
            if key == pygame.K_ESCAPE:
                self.quit()

        def on_mouse_up( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == MAGIC_POWER_GAME_STATE_BEGIN:
                    self.state = MAGIC_POWER_GAME_STATE_PLAY
                elif self.state == MAGIC_POWER_GAME_STATE_END:
                    self.quit()

        def on_mouse_down( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == MAGIC_POWER_GAME_STATE_PLAY:
                    if self.force_marker["behavior"].state == MARKER_STATE_IDLE:
                        self.message_hud["renderer"].set_frameset( MESSAGE_CHARGING_FRAMESET )
                        self.force_marker["behavior"].activate()
                    elif self.force_marker["behavior"].state == MARKER_STATE_MOVING:
                        self.force_marker["behavior"].freeze()
                        self.power_marker["behavior"].activate()
                    elif self.power_marker["behavior"].state == MARKER_STATE_MOVING:
                        self.power_marker["behavior"].freeze()

    class MagicPowerMarkerBehavior( GameComponent ):
        def __init__( self, min_value, max_value, speed ):
            super( MagicPowerMarkerBehavior, self ).__init__()
            self.min_value = min_value
            self.max_value = max_value
            self.speed     = -speed
            self.state     = MARKER_STATE_IDLE

        def update( self, delta_sec ):
            if self.state == MARKER_STATE_MOVING:
                y = self.game_object["transform"].y + delta_sec * self.speed
                if y > self.max_value:
                    y = self.max_value - (y - self.max_value)
                    self.speed *= -1
                elif y < self.min_value:
                    y = self.min_value + (self.min_value - y)
                    self.speed *= -1
                self.game_object["transform"].y = y

        def activate( self ):
            self.state = MARKER_STATE_MOVING

        def freeze( self ):
            self.state = MARKER_STATE_FROZEN

        def reset( self ):
            self.state = MARKER_STATE_IDLE
            self.speed = -abs( self.speed )
            self.game_object["transform"].y = self.max_value

    class PowerTargetBehavior( GameComponent ):
        def __init__( self, target_type, number_hit_points, point_value ):
            super( PowerTargetBehavior, self ).__init__()
            self.type              = target_type
            self.max_hit_points    = number_hit_points
            self.number_hit_points = number_hit_points
            self.point_value       = point_value

        def hit( self, damage ):
            self.number_hit_points -= damage
            self.update_frameset()

        def get_point_value( self ):
            return self.point_value

        def update_frameset( self ):
            if self.type == TARGET_TYPE_NEAR:
                if self.number_hit_points < self.max_hit_points:
                    self.game_object["renderer"].set_frameset( POWER_TARGET_NEAR_DAMAGED_FRAMESET )
                else:
                    self.game_object["renderer"].set_frameset( POWER_TARGET_NEAR_UNDAMAGED_FRAMESET )
            elif self.type == TARGET_TYPE_MIDDLE:
                if self.number_hit_points < self.max_hit_points:
                    self.game_object["renderer"].set_frameset( POWER_TARGET_MIDDLE_DAMAGED_FRAMESET )
                else:
                    self.game_object["renderer"].set_frameset( POWER_TARGET_MIDDLE_UNDAMAGED_FRAMESET )
            elif self.type == TARGET_TYPE_FAR:
                if self.number_hit_points < self.max_hit_points:
                    self.game_object["renderer"].set_frameset( POWER_TARGET_FAR_DAMAGED_FRAMESET )
                else:
                    self.game_object["renderer"].set_frameset( POWER_TARGET_FAR_UNDAMAGED_FRAMESET )
