init python:
    class MagicPowerLevel( object ):
        def __init__( self, time_limit, marker_speed ):
            self.time_limit          = time_limit
            self.marker_speed        = marker_speed

    MAGIC_POWER_LEVELS = [
        MagicPowerLevel( time_limit          = 60,
                         marker_speed        = 300 ),

        MagicPowerLevel( time_limit          = 60,
                         marker_speed        = 325 ),
                         
        MagicPowerLevel( time_limit          = 60,
                         marker_speed        = 350 ),
                         
        MagicPowerLevel( time_limit          = 60,
                         marker_speed        = 375 ),
                         
        MagicPowerLevel( time_limit          = 60,
                         marker_speed        = 400 )
        ]

    #### DESIGNERS: DO NOT CHANGE ANYTHING BEYOND THIS LINE ####

    # different states the Hunt Duck game can be in.
    MAGIC_POWER_GAME_STATE_BEGIN = "power_begin"
    MAGIC_POWER_GAME_STATE_PLAY  = "power_play"
    MAGIC_POWER_GAME_STATE_END   = "power_end"

    MESSAGE_CHARGING_FRAMESET  = "message_charging"
    MESSAGE_FIRING_FRAMESET    = "message_firing"
    MESSAGE_HIT_FRAMESET       = "message_hit"
    MESSAGE_MISS_FRAMESET      = "message_miss"
    MESSAGE_DESTROYED_FRAMESET = "message_destroyed"
    MESSAGE_MISFIRE_FRAMESET   = "message_misfire"

    # prefabs.
    POWER_TARGET_TYPE = "power_target"

    # hit points.
    EASY_TARGET_HIT_POINTS   = 1
    MEDIUM_TARGET_HIT_POINTS = 3
    HARD_TARGET_HIT_POINTS   = 5
    
    # points.
    EASY_TARGET_POINT_VALUE   = 100
    MEDIUM_TARGET_POINT_VALUE = 300
    HARD_TARGET_POINT_VALUE   = 500

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

    POWER_TARGET_EASY_NEAR_UNDAMAGED_FRAMESET   = "green_near_undamaged"
    POWER_TARGET_EASY_NEAR_DAMAGED_FRAMESET     = "green_near_damaged"
    POWER_TARGET_EASY_NEAR_DESTROYED_FRAMESET   = "green_near_destroyed"
    POWER_TARGET_EASY_MIDDLE_UNDAMAGED_FRAMESET = "green_middle_undamaged"
    POWER_TARGET_EASY_MIDDLE_DAMAGED_FRAMESET   = "green_middle_damaged"
    POWER_TARGET_EASY_MIDDLE_DESTROYED_FRAMESET = "green_middle_destroyed"
    POWER_TARGET_EASY_FAR_UNDAMAGED_FRAMESET    = "green_far_undamaged"
    POWER_TARGET_EASY_FAR_DAMAGED_FRAMESET      = "green_far_damaged"
    POWER_TARGET_EASY_FAR_DESTROYED_FRAMESET    = "green_far_destroyed"
    
    POWER_TARGET_MEDIUM_NEAR_UNDAMAGED_FRAMESET   = "yellow_near_undamaged"
    POWER_TARGET_MEDIUM_NEAR_DAMAGED_FRAMESET     = "yellow_near_damaged"
    POWER_TARGET_MEDIUM_NEAR_DESTROYED_FRAMESET   = "yellow_near_destroyed"
    POWER_TARGET_MEDIUM_MIDDLE_UNDAMAGED_FRAMESET = "yellow_middle_undamaged"
    POWER_TARGET_MEDIUM_MIDDLE_DAMAGED_FRAMESET   = "yellow_middle_damaged"
    POWER_TARGET_MEDIUM_MIDDLE_DESTROYED_FRAMESET = "yellow_middle_destroyed"
    POWER_TARGET_MEDIUM_FAR_UNDAMAGED_FRAMESET    = "yellow_far_undamaged"
    POWER_TARGET_MEDIUM_FAR_DAMAGED_FRAMESET      = "yellow_far_damaged"
    POWER_TARGET_MEDIUM_FAR_DESTROYED_FRAMESET    = "yellow_far_destroyed"
    
    POWER_TARGET_HARD_NEAR_UNDAMAGED_FRAMESET   = "blue_near_undamaged"
    POWER_TARGET_HARD_NEAR_DAMAGED_FRAMESET     = "blue_near_damaged"
    POWER_TARGET_HARD_NEAR_DESTROYED_FRAMESET   = "blue_near_destroyed"
    POWER_TARGET_HARD_MIDDLE_UNDAMAGED_FRAMESET = "blue_middle_undamaged"
    POWER_TARGET_HARD_MIDDLE_DAMAGED_FRAMESET   = "blue_middle_damaged"
    POWER_TARGET_HARD_MIDDLE_DESTROYED_FRAMESET = "blue_middle_destroyed"
    POWER_TARGET_HARD_FAR_UNDAMAGED_FRAMESET    = "blue_far_undamaged"
    POWER_TARGET_HARD_FAR_DAMAGED_FRAMESET      = "blue_far_damaged"
    POWER_TARGET_HARD_FAR_DESTROYED_FRAMESET    = "blue_far_destroyed"
    
    POWER_TARGET_X = 324
    POWER_TARGET_Y = 296
    
    # target types.
    TARGET_TYPE_EASY   = "green"
    TARGET_TYPE_MEDIUM = "yellow"
    TARGET_TYPE_HARD   = "blue"
    
    TARGET_DISTANCE_NEAR   = "near_target"
    TARGET_DISTANCE_MIDDLE = "middle_target"
    TARGET_DISTANCE_FAR    = "far_target"
    
    TARGET_SIZE = { TARGET_DISTANCE_NEAR   : 104,
                    TARGET_DISTANCE_MIDDLE : 80,
                    TARGET_DISTANCE_FAR    : 56 }
    
    TARGET_HIT_POINTS = { TARGET_TYPE_EASY   : 1,
                          TARGET_TYPE_MEDIUM : 3,
                          TARGET_TYPE_HARD   : 5 }
    
    POWER_TARGET_DISTANCE = { TARGET_DISTANCE_NEAR   : 0,
                              TARGET_DISTANCE_MIDDLE : 30,
                              TARGET_DISTANCE_FAR    : 60 }

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
    
    # Fireball variables
    FIREBALL_ANIMATION_FLY       = "fly"
    FIREBALL_ANIMATION_DURATION  = 0.2
    
    FIREBALL_FLY_FRAMES          = 2
    FIREBALL_FLY_DURATION_FAR    = 1.0
    FIREBALL_FLY_DURATION_MEDIUM = 0.6
    FIREBALL_FLY_DURATION_NEAR   = 0.4
    
    FIREBALL_STATE_IDLE          = "fireball_idle"
    FIREBALL_STATE_FLYING        = "fireball_flying"
    
    FIREBALL_VELOCITY            = 400
    
    FIREBALL_INITIAL_Y           = MINIGAME_HEIGHT + 40
    FIREBALL_INITIAL_X           = MINIGAME_WIDTH/2
    
    FIREBALL_SUPER_HIT_AOE   = 0.1 # 0.1*target_area
    FIREBALL_PERFECT_HIT_AOE = 0.3
    FIREBALL_OK_HIT_AOE      = 0.8

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

            # setup the entities.
            #self.background         = None
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
            self.fireball           = None

            #self.create_background()
            self.create_huds()
            self.create_bars( level )
            self.create_target()
            self.create_fireball()

            self.spawn_target()

        def create_background( self ):
            self.background             = GameObject()
            self.background["renderer"] = GameRenderer( GameImage( "gfx/magic_power/background.jpg" ) )

        def create_huds( self ):
            self.start_screen_hud             = GameObject()
            self.start_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/magic_power/start_screen.png" ) )
            self.start_screen_hud["transform"].set_position( 148, 50 )

            self.stop_screen_hud             = GameObject()
            self.stop_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/magic_power/stop_screen.png" ) )
            self.stop_screen_hud["transform"].set_position( 148, 50 )

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
            self.score_hud["transform"].set_position( 400, 30 )

            self.time_remaining_hud             = GameObject()
            self.time_remaining_hud["renderer"] = GameRenderer( GameText( self.get_time_remaining, Color( 255, 255, 255, 255 ) ) )
            self.time_remaining_hud["transform"].set_position( 30, 30 )

            self.message_hud = GameObject()
            self.message_hud["renderer"] = GameRenderer()
            self.message_hud["renderer"].set_frame( MESSAGE_CHARGING_FRAMESET, GameText( lambda : "Charging", Color( 255, 255, 255, 255 ) ) )
            self.message_hud["renderer"].set_frame( MESSAGE_FIRING_FRAMESET, GameText( lambda : "Firing", Color( 255, 255, 255, 255 ) ) )
            self.message_hud["renderer"].set_frame( MESSAGE_HIT_FRAMESET, GameText( lambda : "Hit", Color( 255, 255, 255, 255 ) ) )
            self.message_hud["renderer"].set_frame( MESSAGE_MISS_FRAMESET, GameText( lambda : "Miss", Color( 255, 255, 255, 255 ) ) )
            self.message_hud["renderer"].set_frame( MESSAGE_DESTROYED_FRAMESET, GameText( lambda : "Destroyed", Color( 255, 255, 255, 255 ) ) )
            self.message_hud["renderer"].set_frame( MESSAGE_MISFIRE_FRAMESET, GameText( lambda : "Misfire", Color( 255, 255, 255, 255 ) ) )
            self.message_hud["transform"].set_position( 30, 60 )

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
            
            target["renderer"].set_frame( POWER_TARGET_EASY_NEAR_UNDAMAGED_FRAMESET, GameImage( "gfx/magic_power/green_near_target_undamaged.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_EASY_NEAR_DAMAGED_FRAMESET,   GameImage( "gfx/magic_power/green_near_target_damaged.png",   Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_EASY_NEAR_DESTROYED_FRAMESET, GameImage( "gfx/magic_power/green_near_target_destroyed.png", Anchor.CENTER ) )            
            target["renderer"].set_frame( POWER_TARGET_EASY_MIDDLE_UNDAMAGED_FRAMESET, GameImage( "gfx/magic_power/green_middle_target_undamaged.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_EASY_MIDDLE_DAMAGED_FRAMESET,   GameImage( "gfx/magic_power/green_middle_target_damaged.png",   Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_EASY_MIDDLE_DESTROYED_FRAMESET, GameImage( "gfx/magic_power/green_middle_target_destroyed.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_EASY_FAR_UNDAMAGED_FRAMESET, GameImage( "gfx/magic_power/green_far_target_undamaged.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_EASY_FAR_DAMAGED_FRAMESET,   GameImage( "gfx/magic_power/green_far_target_damaged.png",   Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_EASY_FAR_DESTROYED_FRAMESET, GameImage( "gfx/magic_power/green_far_target_destroyed.png", Anchor.CENTER ) )

            target["renderer"].set_frame( POWER_TARGET_MEDIUM_NEAR_UNDAMAGED_FRAMESET, GameImage( "gfx/magic_power/yellow_near_target_undamaged.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_MEDIUM_NEAR_DAMAGED_FRAMESET,   GameImage( "gfx/magic_power/yellow_near_target_damaged.png",   Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_MEDIUM_NEAR_DESTROYED_FRAMESET, GameImage( "gfx/magic_power/yellow_near_target_destroyed.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_MEDIUM_MIDDLE_UNDAMAGED_FRAMESET, GameImage( "gfx/magic_power/yellow_middle_target_undamaged.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_MEDIUM_MIDDLE_DAMAGED_FRAMESET,   GameImage( "gfx/magic_power/yellow_middle_target_damaged.png",   Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_MEDIUM_MIDDLE_DESTROYED_FRAMESET, GameImage( "gfx/magic_power/yellow_middle_target_destroyed.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_MEDIUM_FAR_UNDAMAGED_FRAMESET, GameImage( "gfx/magic_power/yellow_far_target_undamaged.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_MEDIUM_FAR_DAMAGED_FRAMESET,   GameImage( "gfx/magic_power/yellow_far_target_damaged.png",   Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_MEDIUM_FAR_DESTROYED_FRAMESET, GameImage( "gfx/magic_power/yellow_far_target_destroyed.png", Anchor.CENTER ) )
            
            target["renderer"].set_frame( POWER_TARGET_HARD_NEAR_UNDAMAGED_FRAMESET, GameImage( "gfx/magic_power/blue_near_target_undamaged.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_HARD_NEAR_DAMAGED_FRAMESET,   GameImage( "gfx/magic_power/blue_near_target_damaged.png",   Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_HARD_NEAR_DESTROYED_FRAMESET, GameImage( "gfx/magic_power/blue_near_target_destroyed.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_HARD_MIDDLE_UNDAMAGED_FRAMESET, GameImage( "gfx/magic_power/blue_middle_target_undamaged.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_HARD_MIDDLE_DAMAGED_FRAMESET,   GameImage( "gfx/magic_power/blue_middle_target_damaged.png",   Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_HARD_MIDDLE_DESTROYED_FRAMESET, GameImage( "gfx/magic_power/blue_middle_target_destroyed.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_HARD_FAR_UNDAMAGED_FRAMESET, GameImage( "gfx/magic_power/blue_far_target_undamaged.png", Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_HARD_FAR_DAMAGED_FRAMESET,   GameImage( "gfx/magic_power/blue_far_target_damaged.png",   Anchor.CENTER ) )
            target["renderer"].set_frame( POWER_TARGET_HARD_FAR_DESTROYED_FRAMESET, GameImage( "gfx/magic_power/blue_far_target_destroyed.png", Anchor.CENTER ) )

            PrefabFactory.add_prefab( POWER_TARGET_TYPE, target )
            
        def create_fireball( self ):
            fireball = GameObject()
            fireball["renderer"] = GameRenderer()
            fireball["renderer"].add_animation( FIREBALL_ANIMATION_FLY, 
                GameAnimation( [ GameImage( "gfx/magic_power/fireball-%d.png" % frame_index, Anchor.CENTER )
                                 for frame_index in xrange( FIREBALL_FLY_FRAMES ) ],
                               FIREBALL_FLY_FRAMES / FIREBALL_ANIMATION_DURATION ) )
            fireball["transform"].set_position( FIREBALL_INITIAL_X, FIREBALL_INITIAL_Y)
            fireball["behavior"] = FireballBehavior(self)
            self.fireball = fireball

        def spawn_target( self ):
            target_difficulty = renpy.random.choice( [ TARGET_TYPE_EASY,
                                                       TARGET_TYPE_MEDIUM,
                                                       TARGET_TYPE_HARD ] )
        
            target_distance = renpy.random.choice( [ TARGET_DISTANCE_NEAR,
                                                     TARGET_DISTANCE_MIDDLE,
                                                     TARGET_DISTANCE_FAR ] )

            number_hit_points = TARGET_HIT_POINTS[ target_difficulty ]

            if number_hit_points == EASY_TARGET_HIT_POINTS:
                point_value = EASY_TARGET_POINT_VALUE
            elif number_hit_points == MEDIUM_TARGET_HIT_POINTS:
                point_value = MEDIUM_TARGET_POINT_VALUE
            elif number_hit_points == HARD_TARGET_HIT_POINTS:
                point_value = HARD_TARGET_POINT_VALUE

            self.target             = PrefabFactory.instantiate( POWER_TARGET_TYPE )
            self.target["behavior"] = PowerTargetBehavior( self, target_difficulty, target_distance, number_hit_points, point_value )
            self.target["behavior"].update_frameset()
            self.target["transform"].set_position( POWER_TARGET_X, POWER_TARGET_Y - POWER_TARGET_DISTANCE[target_distance])

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
            displayables.extend( self.fireball["renderer"].get_displayables() )
            return displayables

        def render( self, blitter, clip_rect ):
            world_transform = self.get_world_transform()
            #self.background["renderer"].render( blitter, clip_rect, world_transform )

            self.force_bar["renderer"].render( blitter, clip_rect, world_transform )
            self.force_marker["renderer"].render( blitter, clip_rect, world_transform )
            self.power_bar["renderer"].render( blitter, clip_rect, world_transform )
            self.power_marker["renderer"].render( blitter, clip_rect, world_transform )

            if self.state == MAGIC_POWER_GAME_STATE_BEGIN:
                self.start_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == MAGIC_POWER_GAME_STATE_PLAY:
                self.message_hud["renderer"].render( blitter, clip_rect, world_transform )
                self.time_remaining_hud["renderer"].render( blitter, clip_rect, world_transform )
                self.score_hud["renderer"].render( blitter, clip_rect, world_transform )

                if self.target:
                    self.target["renderer"].render( blitter, clip_rect, world_transform )
                
                self.fireball["renderer"].render( blitter, clip_rect, world_transform )
                
            elif self.state == MAGIC_POWER_GAME_STATE_END:
                self.stop_screen_hud["renderer"].render( blitter, clip_rect, world_transform )

        def update( self, delta_sec ):
            if self.state == MAGIC_POWER_GAME_STATE_PLAY:
                # update automated parameters.
                self.time_remaining.update( delta_sec )
                
                if self.fireball["behavior"].state == FIREBALL_STATE_FLYING:
                  self.fireball.update( delta_sec )
                
                # update entities.
                self.force_marker.update( delta_sec )
                self.power_marker.update( delta_sec )

                if (self.fireball["behavior"].state == FIREBALL_STATE_IDLE and
                    self.force_marker["behavior"].state == MARKER_STATE_FROZEN and
                    self.power_marker["behavior"].state == MARKER_STATE_FROZEN):
                    
                    aim_y    = self.force_marker["transform"].y
                    target_y = self.target["transform"].y
                    diff_y = abs(aim_y - target_y)
                    
                    distance_from_target = diff_y/TARGET_SIZE[self.target["behavior"].distance]
                    
                    if distance_from_target <= FIREBALL_SUPER_HIT_AOE:
                      damage = 3
                    elif distance_from_target <= FIREBALL_PERFECT_HIT_AOE:
                      damage = 1
                    elif distance_from_target <= FIREBALL_OK_HIT_AOE:
                      damage = 0.5
                    else:
                      damage = 0
                    
                    # (how far the marker is from the top)/(bar size)
                    power = abs(self.power_marker["transform"].y - POWER_MARKER_MAX_Y)/176
                    
                    damage *= power
                    
                    self.fireball["behavior"].fly(self.target,
                                                  self.force_marker["transform"].y, 
                                                  damage)
                                                  
                    self.message_hud["renderer"].set_frameset( MESSAGE_FIRING_FRAMESET )
                
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
                    if self.target["behavior"].number_hit_points <= 0:
                        self.spawn_target()
                    elif self.force_marker["behavior"].state == MARKER_STATE_IDLE:
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
        def __init__( self, main, target_difficulty, target_distance, number_hit_points, point_value ):
            super( PowerTargetBehavior, self ).__init__()
            self.main              = main
            self.difficulty        = target_difficulty
            self.distance          = target_distance
            self.max_hit_points    = number_hit_points
            self.number_hit_points = number_hit_points
            self.point_value       = point_value

        def hit( self, damage ):
            self.number_hit_points -= damage
            self.update_frameset()
            
            if self.number_hit_points <= 0:
                message_frameset = MESSAGE_DESTROYED_FRAMESET
                self.main.base_score += self.point_value
            else:
              if damage > 0:
                  message_frameset = MESSAGE_HIT_FRAMESET
              else:
                  message_frameset = MESSAGE_MISS_FRAMESET
            self.main.message_hud["renderer"].set_frameset( message_frameset )
            

        def get_point_value( self ):
            return self.point_value

        def update_frameset( self ):
            # copy-paste because I'm feeling lazy
            if self.difficulty == TARGET_TYPE_EASY:
                if self.number_hit_points <= 0:
                    if self.distance == TARGET_DISTANCE_NEAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_EASY_NEAR_DESTROYED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_MIDDLE:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_EASY_MIDDLE_DESTROYED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_FAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_EASY_FAR_DESTROYED_FRAMESET )
                elif self.number_hit_points < self.max_hit_points:
                    if self.distance == TARGET_DISTANCE_NEAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_EASY_NEAR_DAMAGED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_MIDDLE:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_EASY_MIDDLE_DAMAGED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_FAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_EASY_FAR_DAMAGED_FRAMESET )
                else:
                    if self.distance == TARGET_DISTANCE_NEAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_EASY_NEAR_UNDAMAGED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_MIDDLE:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_EASY_MIDDLE_UNDAMAGED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_FAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_EASY_FAR_UNDAMAGED_FRAMESET )
                        
            elif self.difficulty == TARGET_TYPE_MEDIUM:
                if self.number_hit_points <= 0:
                    if self.distance == TARGET_DISTANCE_NEAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_MEDIUM_NEAR_DESTROYED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_MIDDLE:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_MEDIUM_MIDDLE_DESTROYED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_FAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_MEDIUM_FAR_DESTROYED_FRAMESET )
                elif self.number_hit_points < self.max_hit_points:
                    if self.distance == TARGET_DISTANCE_NEAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_MEDIUM_NEAR_DAMAGED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_MIDDLE:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_MEDIUM_MIDDLE_DAMAGED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_FAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_MEDIUM_FAR_DAMAGED_FRAMESET )
                else:
                    if self.distance == TARGET_DISTANCE_NEAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_MEDIUM_NEAR_UNDAMAGED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_MIDDLE:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_MEDIUM_MIDDLE_UNDAMAGED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_FAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_MEDIUM_FAR_UNDAMAGED_FRAMESET )
                        
            elif self.difficulty == TARGET_TYPE_HARD:
                if self.number_hit_points <= 0:
                    if self.distance == TARGET_DISTANCE_NEAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_HARD_NEAR_DESTROYED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_MIDDLE:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_HARD_MIDDLE_DESTROYED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_FAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_HARD_FAR_DESTROYED_FRAMESET )
                elif self.number_hit_points < self.max_hit_points:
                    if self.distance == TARGET_DISTANCE_NEAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_HARD_NEAR_DAMAGED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_MIDDLE:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_HARD_MIDDLE_DAMAGED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_FAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_HARD_FAR_DAMAGED_FRAMESET )
                else:
                    if self.distance == TARGET_DISTANCE_NEAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_HARD_NEAR_UNDAMAGED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_MIDDLE:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_HARD_MIDDLE_UNDAMAGED_FRAMESET )
                    elif self.distance == TARGET_DISTANCE_FAR:
                        self.game_object["renderer"].set_frameset( POWER_TARGET_HARD_FAR_UNDAMAGED_FRAMESET )

    class FireballBehavior( GameComponent ):
        def __init__( self, main ):
            self.state          = FIREBALL_STATE_IDLE
            self.main           = main
            self.target         = None
            self.aim_y          = 0
            self.damage         = 0
            self.scale_distance = 0
            
        def fly( self, target, aim_y, damage ):
            self.state  = FIREBALL_STATE_FLYING
            self.target = target
            self.aim_y  = aim_y
            self.damage = damage
            self.game_object["renderer"].play_animation( FIREBALL_ANIMATION_FLY )
            
        def update( self, delta_sec ):
            self.game_object["transform"].y -= FIREBALL_VELOCITY * delta_sec
            
            # something to scale the fireball down a bit while it's on its way
            self.scale_distance += FIREBALL_VELOCITY * delta_sec
            if self.scale_distance >= 65:
              self.game_object["transform"].scale -= 0.1
              self.scale_distance = 0
            
            # hit the target and reset the fireball
            if self.game_object["transform"].y <= self.aim_y:
                self.target["behavior"].hit(self.damage)
                self.reset()
            
        def reset( self ):
            self.state = FIREBALL_STATE_IDLE
            self.game_object["transform"].y = FIREBALL_INITIAL_Y
            self.game_object["transform"].set_scale(1.0)

            self.main.force_marker["behavior"].reset()
            self.main.power_marker["behavior"].reset()