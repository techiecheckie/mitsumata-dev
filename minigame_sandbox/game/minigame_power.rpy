init python:
    class MagicPowerLevel( object ):
        def __init__( self, time_limit ):
            self.time_limit = time_limit

    MAGIC_POWER_LEVELS = [
        MagicPowerLevel( time_limit = 60 )
        ]

    #### DESIGNERS: DO NOT CHANGE ANYTHING BEYOND THIS LINE ####

    # different states the Hunt Duck game can be in.
    MAGIC_POWER_GAME_STATE_BEGIN = "power_begin"
    MAGIC_POWER_GAME_STATE_PLAY  = "power_play"
    MAGIC_POWER_GAME_STATE_END   = "power_end"

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
            self.state       = MAGIC_POWER_GAME_STATE_BEGIN
            self.base_score  = 0
            self.total_score = 0

            # setup the entities.
            self.start_screen_hud   = None
            self.stop_screen_hud    = None
            self.score_hud          = None
            self.time_remaining_hud = None

            self.create_huds()

        def create_huds( self ):
            self.start_screen_hud             = GameObject()
            self.start_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/magic_power/start_screen.png" ) )
            self.start_screen_hud["transform"].set_position( 138, 50 )

            self.stop_screen_hud             = GameObject()
            self.stop_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/magic_power/stop_screen.png" ) )
            self.stop_screen_hud["transform"].set_position( 138, 50 )

            base_score             = GameObject()
            base_score["renderer"] = GameRenderer( GameText( self.get_base_score ) )
            base_score["transform"].set_position( 185, 159 )
            self.stop_screen_hud.add_child( base_score )

            total_score             = GameObject()
            total_score["renderer"] = GameRenderer( GameText( self.get_total_score ) )
            total_score["transform"].set_position( 185, 320 )
            self.stop_screen_hud.add_child( total_score )

            self.score_hud             = GameObject()
            self.score_hud["renderer"] = GameRenderer( GameText( self.get_score ) )
            self.score_hud["transform"].set_position( 400, 10 )

            self.time_remaining_hud             = GameObject()
            self.time_remaining_hud["renderer"] = GameRenderer( GameText( self.get_time_remaining ) )
            self.time_remaining_hud["transform"].set_position( 10, 10 )

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

        def get_displayables( self ):
            displayables = []
            displayables.extend( self.score_hud["renderer"].get_displayables() )
            displayables.extend( self.time_remaining_hud["renderer"].get_displayables() )
            return displayables

        def render( self, blitter ):
            world_transform = self.get_world_transform()

            if self.state == MAGIC_POWER_GAME_STATE_BEGIN:
                self.start_screen_hud["renderer"].render( blitter, world_transform )
            elif self.state == MAGIC_POWER_GAME_STATE_PLAY:
                pass
            elif self.state == MAGIC_POWER_GAME_STATE_END:
                self.stop_screen_hud["renderer"].render( blitter, world_transform )

            self.time_remaining_hud["renderer"].render( blitter, world_transform )
            self.score_hud["renderer"].render( blitter, world_transform )

        def update( self, delta_sec ):
            if self.state == MAGIC_POWER_GAME_STATE_PLAY:
                # update automated parameters.
                self.time_remaining.update( delta_sec )

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
