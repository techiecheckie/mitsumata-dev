init python:
    class SquatsLevel( object ):
        def __init__( self, time_limit, initial_marker_speed, max_marker_speed,
                      segment_height, tired_timeout, level_number ):
            self.time_limit           = time_limit
            self.initial_marker_speed = initial_marker_speed
            self.max_marker_speed     = max_marker_speed
            self.segment_height       = segment_height
            self.tired_timeout        = tired_timeout
            self.level_number         = level_number

    SQUATS_LEVELS = [
        SquatsLevel( time_limit           = 30,
                     initial_marker_speed = 100,
                     max_marker_speed     = 150,
                     segment_height       = 30,
                     tired_timeout        = 1,
                     level_number         = 1),
                     
        SquatsLevel( time_limit           = 30,
                     initial_marker_speed = 120,
                     max_marker_speed     = 180,
                     segment_height       = 25,
                     tired_timeout        = 1,
                     level_number         = 2),
                     
        SquatsLevel( time_limit           = 30,
                     initial_marker_speed = 140,
                     max_marker_speed     = 200,
                     segment_height       = 20,
                     tired_timeout        = 1,
                     level_number         = 3),
                     
        SquatsLevel( time_limit           = 30,
                     initial_marker_speed = 160,
                     max_marker_speed     = 220,
                     segment_height       = 20,
                     tired_timeout        = 1,
                     level_number         = 4)
        ]

    #### DESIGNERS: DO NOT CHANGE ANYTHING BEYOND THIS LINE ####

    # different states the Strength game can be in.
    SQUATS_GAME_STATE_BEGIN = 1
    SQUATS_GAME_STATE_PLAY  = 2
    SQUATS_GAME_STATE_END   = 3
    SQUATS_GAME_STATE_PAUSE = 4

    RIKU_ANIMATION_TIRED   = "riku_tired"
    RIKU_ANIMATION_TIRED_DURATION = 0.35
    NUMBER_RIKU_TIRED_FRAMES   = 3

    SEGMENT_FRAMESET_ACTIVE   = "segment_active"
    SEGMENT_FRAMESET_INACTIVE = "segment_inactive"

    # riku states.
    RIKU_STATE_LIFTING = 1
    RIKU_STATE_TIRED   = 2
    
    # Riku lifting animation framesets for timing the animation with the marker movement
    RIKU_LIFTING_FRAMESET_1 = 1
    RIKU_LIFTING_FRAMESET_2 = 2
    RIKU_LIFTING_FRAMESET_3 = 3
    RIKU_LIFTING_FRAMESET_4 = 4

    SQUATS_BAR_X = 20
    SQUATS_BAR_Y = 295
    SQUATS_BAR_HEIGHT = 173
    SQUATS_BAR_WIDTH = 10

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

    # 61 is the offset from the left edge of the bar image to the left edge of
    # one of the target segments in the bar.
    SQUATS_SEGMENT_X = SQUATS_BAR_X + 61
    SQUATS_SEGMENT_Y = SQUATS_BAR_Y 

    class Squats( Minigame ):
        def __init__( self, level_number=1 ):
            super( Squats, self ).__init__()

            if level_number > len( SQUATS_LEVELS ) or level_number <= 0:
                raise ValueError( "Invalid Magic Power level number %d.  Level "
                                  "number must be between 1 and %d." %
                                  (level_number, len( SQUATS_LEVELS )) )

            # setup the level difficulty parameters.
            self.level = SQUATS_LEVELS[level_number - 1]
            self.time_remaining = AutomatedInterpolator( self.level.time_limit,
                                                         0,
                                                         self.level.time_limit )

            # setup the game state.
            self.state = SQUATS_GAME_STATE_BEGIN
            self.score = 0

            # setup the entities.
            self.start_screen_hud     = None
            self.stop_screen_hud      = None
            self.score_hud            = None
            self.time_remaining_hud   = None
            self.bar                  = None
            self.bar_segments         = None
            self.bar_segment_active   = False
            self.marker               = None
            self.riku                 = None
            self.instructions         = None
            self.instructions_hud     = None
            self.instructions_index   = 0

            self.create_huds()
            self.create_bar( self.level )
            self.create_riku( self.level )

        def create_huds( self ):
            self.start_screen_hud             = GameObject()
            self.start_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/squats/start_screen.png" ) )
            self.start_screen_hud["transform"].set_position( 148, 50 )

            self.stop_screen_hud             = GameObject()
            self.stop_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/squats/stop_screen.png" ) )
            self.stop_screen_hud["transform"].set_position( 148, 50 )
            
            instructions_1 = GameObject()
            instructions_1["renderer"] = GameRenderer( GameImage ( "gfx/squats/instructions_1.png" ) )
            instructions_1["transform"].set_position( 148, 50 )
            instructions_2 = GameObject()
            instructions_2["renderer"] = GameRenderer( GameImage ( "gfx/squats/instructions_2.png" ) )
            instructions_2["transform"].set_position( 148, 50 )
            self.instructions = [ instructions_1, instructions_2 ]
            
            high_score = GameObject()
            high_score["renderer"] = GameRenderer( GameText( self.get_high_score, Color( 255, 255, 255, 255 ) ) )
            high_score["transform"].set_position( 138, 313 )
            self.start_screen_hud.add_child( high_score )

            level = GameObject()
            level["renderer"] = GameRenderer( GameText( self.get_level_number, Color( 255, 255, 255, 255 ) ) )
            level["transform"].set_position( 138, 360 )
            self.start_screen_hud.add_child( level )
            
            hits_total             = GameObject()
            hits_total["renderer"] = GameRenderer( GameText( self.get_hits_total, Color( 255, 255, 255, 255 ) ) )
            hits_total["transform"].set_position( 200, 163 )
            self.stop_screen_hud.add_child( hits_total )

            green_hits = GameObject()
            green_hits["renderer"] = GameRenderer( GameText( self.get_green_hits, Color( 255, 255, 255, 255 )))
            green_hits["transform"].set_position( 200, 210 )
            self.stop_screen_hud.add_child( green_hits )
            
            orange_hits = GameObject()
            orange_hits["renderer"] = GameRenderer( GameText( self.get_orange_hits, Color( 255, 255, 255, 255 )))
            orange_hits["transform"].set_position( 200, 233 )
            self.stop_screen_hud.add_child( orange_hits )

            red_hits = GameObject()
            red_hits["renderer"] = GameRenderer( GameText( self.get_red_hits, Color( 255, 255, 255, 255 )))
            red_hits["transform"].set_position( 200, 257 )
            self.stop_screen_hud.add_child( red_hits )
            
            total_score             = GameObject()
            total_score["renderer"] = GameRenderer( GameText( self.get_total_score, Color( 255, 255, 255, 255 ) ) )
            total_score["transform"].set_position( 200, 325 )
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

            self.bar_segments = []
            
            green_segment = GameObject()
            green_segment["renderer"] = GameRenderer()
            green_segment["renderer"].set_frame( SEGMENT_FRAMESET_INACTIVE,
                                                    GameRect( Size( SQUATS_BAR_WIDTH, level.segment_height ),
                                                              Color( 0, 100, 0, 255 ),
                                                              Anchor.LEFT ) )
            green_segment["renderer"].set_frame( SEGMENT_FRAMESET_ACTIVE,
                                                    GameRect( Size( SQUATS_BAR_WIDTH, level.segment_height ),
                                                              Color( 0, 235, 0, 255 ),
                                                              Anchor.LEFT ) )
            green_segment["renderer"].set_frameset( SEGMENT_FRAMESET_INACTIVE )
            green_segment["behavior"] = SegmentBehavior( level.segment_height, 50 )
            green_segment["transform"].set_position( SQUATS_SEGMENT_X, SQUATS_SEGMENT_Y )
            self.bar_segments.append( green_segment )
            
            orange_segment = GameObject()
            orange_segment["renderer"] = GameRenderer()
            orange_segment["renderer"].set_frame( SEGMENT_FRAMESET_INACTIVE,
                                                    GameRect( Size( SQUATS_BAR_WIDTH, level.segment_height * 3),
                                                              Color( 200, 145, 0, 255 ),
                                                              Anchor.LEFT ) )
            orange_segment["renderer"].set_frame( SEGMENT_FRAMESET_ACTIVE,
                                                    GameRect( Size( SQUATS_BAR_WIDTH, level.segment_height * 3),
                                                              Color( 235, 235, 0, 255 ),
                                                              Anchor.LEFT ) )
            orange_segment["renderer"].set_frameset( SEGMENT_FRAMESET_INACTIVE )
            orange_segment["behavior"] = SegmentBehavior( level.segment_height * 3, 25 )
            orange_segment["transform"].set_position( SQUATS_SEGMENT_X, SQUATS_SEGMENT_Y )
            self.bar_segments.append( orange_segment )
            
            red_segment = GameObject()
            red_segment["renderer"] = GameRenderer()
            red_segment["renderer"].set_frame( SEGMENT_FRAMESET_INACTIVE,
                                                    GameRect( Size( SQUATS_BAR_WIDTH, SQUATS_BAR_HEIGHT),
                                                              Color( 200, 0, 0, 255 ),
                                                              Anchor.LEFT ) )
            red_segment["renderer"].set_frame( SEGMENT_FRAMESET_ACTIVE,
                                                    GameRect( Size( SQUATS_BAR_WIDTH, SQUATS_BAR_HEIGHT),
                                                              Color( 235, 0, 0, 255 ),
                                                              Anchor.LEFT ) )
            red_segment["renderer"].set_frameset( SEGMENT_FRAMESET_INACTIVE )
            red_segment["behavior"] = SegmentBehavior( SQUATS_BAR_HEIGHT, 0 )
            red_segment["transform"].set_position( SQUATS_SEGMENT_X, SQUATS_SEGMENT_Y )
            self.bar_segments.append( red_segment )

            self.marker             = GameObject()
            self.marker["renderer"] = GameRenderer( GameImage( "gfx/squats/marker.png", Anchor.LEFT ) )
            self.marker["behavior"] = MarkerBehavior( self, level.initial_marker_speed, level.max_marker_speed )
            self.marker["transform"].set_position( SQUATS_MARKER_X, SQUATS_MARKER_MAX_Y )

        def create_riku( self, level ):
            self.riku             = GameObject()
            self.riku["behavior"] = SquatsRikuBehavior( self, level.tired_timeout )
            self.riku["renderer"] = GameRenderer( GameImage( "gfx/squats/riku/riku.png", Anchor.BOTTOM ) )
            self.riku["renderer"].set_frame( RIKU_LIFTING_FRAMESET_1, GameImage( "gfx/squats/riku/riku-lifting0.png", Anchor.BOTTOM ) )
            self.riku["renderer"].set_frame( RIKU_LIFTING_FRAMESET_2, GameImage( "gfx/squats/riku/riku-lifting1.png", Anchor.BOTTOM ) )
            self.riku["renderer"].set_frame( RIKU_LIFTING_FRAMESET_3, GameImage( "gfx/squats/riku/riku-lifting2.png", Anchor.BOTTOM ) )
            self.riku["renderer"].set_frame( RIKU_LIFTING_FRAMESET_4, GameImage( "gfx/squats/riku/riku-lifting3.png", Anchor.BOTTOM ) )
            self.riku["renderer"].add_animation( RIKU_ANIMATION_TIRED,
                                                 GameAnimation( [ GameImage( "gfx/squats/riku/riku-tired%d.png" % frame_index, Anchor.BOTTOM )
                                                                  for frame_index in xrange( NUMBER_RIKU_TIRED_FRAMES ) ],
                                                                NUMBER_RIKU_TIRED_FRAMES / RIKU_ANIMATION_TIRED_DURATION ) )
            self.riku["transform"].set_position( SQUATS_RIKU_X, SQUATS_RIKU_Y )
            self.riku["transform"].set_scale( 2.0 )

        def get_score( self ):
            return "Score: %4d" % self.score
        
        def get_total_score( self ):
            return "%4d" % self.score

        def get_time_remaining( self ):
            return "Time Remaining: %d" %  self.time_remaining.get_ceil_value()
        
        def get_hits_total( self ):
            hits = 0
            for bar_segment in self.bar_segments:
                hits += bar_segment["behavior"].get_hits()
            return "%4d" % hits
        
        def get_green_hits( self ):
            bar_segment = self.bar_segments[0]
            return "%4d  (%2d pts)" % (bar_segment["behavior"].get_hits(), bar_segment["behavior"].get_score())
        
        def get_orange_hits( self ):
            bar_segment = self.bar_segments[1]
            return "%4d  (%2d pts)" % (bar_segment["behavior"].get_hits(), bar_segment["behavior"].get_score())
        
        def get_red_hits( self ):
            bar_segment = self.bar_segments[2]
            return "%4d  (%2d pts)" % (bar_segment["behavior"].get_hits(), bar_segment["behavior"].get_score())
            
        def get_level_number( self ):
            return "%20d" % self.level.level_number

        def get_displayables( self ):
            displayables = []
            displayables.extend( self.riku["renderer"].get_displayables() )
            displayables.extend( self.bar["renderer"].get_displayables() )
            displayables.extend( self.marker["renderer"].get_displayables() )
            displayables.extend( self.score_hud["renderer"].get_displayables() )
            displayables.extend( self.time_remaining_hud["renderer"].get_displayables() )
            displayables.extend( self.start_screen_hud["renderer"].get_displayables() )
            displayables.extend( self.stop_screen_hud["renderer"].get_displayables() )
            
            for bar_segment in self.bar_segments:
                displayables.extend( bar_segment["renderer"].get_displayables() )
            
            for instruction in self.instructions:
                displayables.extend( instruction["renderer"].get_displayables() )
            
            return displayables

        def render( self, blitter, clip_rect ):
            world_transform = self.get_world_transform()

            self.riku["renderer"].render( blitter, clip_rect, world_transform )
            self.bar["renderer"].render( blitter, clip_rect, world_transform )
            for bar_segment in reversed(self.bar_segments):
                bar_segment["renderer"].render( blitter, clip_rect, world_transform )
            self.marker["renderer"].render( blitter, clip_rect, world_transform )
            
            self.time_remaining_hud["renderer"].render( blitter, clip_rect, world_transform )
            self.score_hud["renderer"].render( blitter, clip_rect, world_transform )

            if self.state == SQUATS_GAME_STATE_BEGIN:
                self.start_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == SQUATS_GAME_STATE_PAUSE:
                self.instructions[self.instructions_index]["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == SQUATS_GAME_STATE_END:
                self.stop_screen_hud["renderer"].render( blitter, clip_rect, world_transform )

        def update( self, delta_sec ):
            if self.state == SQUATS_GAME_STATE_PLAY:
                # update automated parameters.
                self.time_remaining.update( delta_sec )

                # update entities.
                self.marker.update( delta_sec )
                self.riku.update( delta_sec )

                # see if it's game over.
                if self.time_remaining.get_value() <= 0:
                    self.state = SQUATS_GAME_STATE_END

        def on_key_down( self, key ):
            if self.state == SQUATS_GAME_STATE_BEGIN:
                if key == pygame.K_h:
                    self.state = SQUATS_GAME_STATE_PAUSE
                else:
                    self.state = SQUATS_GAME_STATE_PLAY
            elif self.state == SQUATS_GAME_STATE_PLAY:
                if (key == pygame.K_SPACE and not self.riku["behavior"].is_tired() and not self.bar_segment_active):
                    for bar_segment in self.bar_segments:
                        if bar_segment["behavior"].is_in_bounds( self.marker["transform"].y ):
                            score = bar_segment["behavior"].get_score()
                            if score == 0:
                                self.riku["behavior"].tire()
                                self.marker["behavior"].freeze()
                            bar_segment["behavior"].activate()
                            self.bar_segment_active = True
                            self.score += score
                            return
                elif key == pygame.K_h:
                    self.state = SQUATS_GAME_STATE_PAUSE
            elif self.state == SQUATS_GAME_STATE_PAUSE:
                self.show_next_instruction()

        def on_mouse_up( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == SQUATS_GAME_STATE_BEGIN:
                    self.state = SQUATS_GAME_STATE_PLAY
                elif self.state == SQUATS_GAME_STATE_END:
                    self.quit()
                elif self.state == SQUATS_GAME_STATE_PAUSE:
                    self.show_next_instruction()
                    
        def show_next_instruction( self ):
            if self.instructions_index < len(self.instructions)-1:
                self.instructions_index += 1
            else:
                self.instructions_index = 0
                self.state = SQUATS_GAME_STATE_PLAY

        def deactivate_bar_segments( self ):
            for bar_segment in self.bar_segments:
                bar_segment["behavior"].deactivate()
            self.bar_segment_active = False
                
        def release_marker( self ):
            self.deactivate_bar_segments()
            self.marker["behavior"].release()
            
        def get_marker_phase( self ):
            return self.marker["behavior"].get_phase()

    class MarkerBehavior( GameComponent ):
        def __init__( self, main, initial_speed, max_speed ):
            super( MarkerBehavior, self ).__init__()
            self.main          = main
            self.initial_speed = initial_speed
            self.max_speed     = max_speed
            self.speed         = initial_speed
            self.acceleration  = 100
            self.velocity      = 1
            self.phase_size    = (SQUATS_MARKER_MAX_Y - SQUATS_MARKER_MIN_Y) / 4
            self.frozen        = False

        def update( self, delta_sec ):
            if self.frozen:
                return
            
            dv         = self.acceleration * delta_sec
            self.speed = min( self.speed + dv, self.max_speed )
            dy         = self.velocity * self.speed * delta_sec
            y          = self.game_object["transform"].y - dy
            
            if y < SQUATS_MARKER_MIN_Y:
                y = SQUATS_MARKER_MIN_Y
                self.velocity *= -1
                self.main.deactivate_bar_segments()
            elif y > SQUATS_MARKER_MAX_Y:
                y = SQUATS_MARKER_MAX_Y
                self.velocity *= -1
                self.main.deactivate_bar_segments()
                
            self.game_object["transform"].y = y
        
        def get_phase( self ):
            if self.game_object["transform"].y <= SQUATS_MARKER_MIN_Y + self.phase_size / 2:
                return 4
            elif self.game_object["transform"].y <= SQUATS_MARKER_MIN_Y + self.phase_size * 2:
                return 3
            elif self.game_object["transform"].y <= SQUATS_MARKER_MIN_Y + self.phase_size * 3 + self.phase_size / 2:
                return 2
            else:
                return 1
                
        def freeze( self ):
            self.game_object["transform"].y = SQUATS_MARKER_MAX_Y
            self.frozen = True
            
        def release( self ):
            self.frozen = False

    class SegmentBehavior( GameComponent ):
        def __init__( self, height, score ):
            super( SegmentBehavior, self ).__init__()
            self.half_height = height / 2
            self.score       = score
            self.active      = False
            self.hits        = 0

        def activate( self ):
            self.active = True
            self.hits += 1
            self.game_object["renderer"].set_frameset( SEGMENT_FRAMESET_ACTIVE )

        def deactivate( self ):
            self.active = False
            self.game_object["renderer"].set_frameset( SEGMENT_FRAMESET_INACTIVE )
            
        def is_active( self ):
            return self.active

        def is_in_bounds( self, y ):
            min_y = self.game_object["transform"].y - self.half_height
            max_y = self.game_object["transform"].y + self.half_height
            return min_y <= y <= max_y
        
        def get_score( self ):
            return self.score
        
        def get_hits( self ):
            return self.hits

    class SquatsRikuBehavior():
        def __init__( self, main, tired_timeout ):
            self.main          = main
            self.state         = RIKU_STATE_LIFTING
            self.tired_timeout = tired_timeout
            self.countdown     = 0
            self.current_phase = 1

        def update( self, delta_sec ):
            if self.state == RIKU_STATE_TIRED:
                self.countdown -= delta_sec
                if self.countdown <= 0:
                    self.state = RIKU_STATE_LIFTING
                    self.game_object["renderer"].stop_animation()
                    self.game_object["renderer"].set_frameset( RIKU_LIFTING_FRAMESET_1 )
                    self.main.release_marker()
            else:
                phase = self.main.get_marker_phase()
                if phase != self.current_phase:
                    if phase == 1:
                        self.game_object["renderer"].set_frameset( RIKU_LIFTING_FRAMESET_1 )
                    elif phase == 2:
                        self.game_object["renderer"].set_frameset( RIKU_LIFTING_FRAMESET_2 )
                    elif phase == 3:
                        self.game_object["renderer"].set_frameset( RIKU_LIFTING_FRAMESET_3 )
                    else:
                        self.game_object["renderer"].set_frameset( RIKU_LIFTING_FRAMESET_4 )
                
                    self.current_phase = phase

        def tire( self ):
            self.state     = RIKU_STATE_TIRED
            self.countdown = self.tired_timeout
            self.game_object["renderer"].play_animation( RIKU_ANIMATION_TIRED )

        def is_tired( self ):
            return self.state == RIKU_STATE_TIRED
