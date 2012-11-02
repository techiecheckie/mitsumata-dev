init python:
    class MagicForceLevel( object ):
        def __init__( self, number_digits, correct_timeout, incorrect_timeout,
                      time_limit ):
            self.number_digits     = number_digits
            self.correct_timeout   = correct_timeout
            self.incorrect_timeout = incorrect_timeout
            self.time_limit        = time_limit

    MAGIC_FORCE_LEVELS = [
        MagicForceLevel( number_digits     = (1,4),
                         correct_timeout   = 0.15,
                         incorrect_timeout = 0.9,
                         time_limit        = 30 ),

        MagicForceLevel( number_digits     = (1,5),
                         correct_timeout   = 0.12,
                         incorrect_timeout = 0.7,
                         time_limit        = 30),

        MagicForceLevel( number_digits     = (1,6),
                         correct_timeout   = 0.12,
                         incorrect_timeout = 0.7,
                         time_limit        = 30),

        MagicForceLevel( number_digits     = (1,7),
                         correct_timeout   = 0.12,
                         incorrect_timeout = 0.7,
                         time_limit        = 30)
        ]

    #### DESIGNERS: DO NOT CHANGE ANYTHING BEYOND THIS LINE ####

    # different states the Hunt Duck game can be in.
    MAGIC_FORCE_GAME_STATE_BEGIN = "force_begin"
    MAGIC_FORCE_GAME_STATE_PLAY  = "force_play"
    MAGIC_FORCE_GAME_STATE_END   = "force_end"
    MAGIC_FORCE_GAME_STATE_PAUSE = "force_pause"

    # frameset names.
    NUMBER_FRAMESET_CORRECT   = "correct_number"
    NUMBER_FRAMESET_INCORRECT = "incorrect_number"

    RIKU_FRAMESET_IDLE          = "riku_idle"
    RIKU_FRAMESET_CHANNEL_START = "riku_start"
    RIKU_FRAMESET_CHANNEL_SQUAT = "riku_squat"
    RIKU_FRAMESET_CHANNEL_STAND = "riku_stand"
    RIKU_FRAMESET_BACKFIRED     = "riku_backfired"

    # animation names.
    RIKU_ANIMATION_POWERED = "riku_powered"
    RIKU_ANIMATION_TIRED   = "riku_tired"

    # animation durations.
    RIKU_ANIMATION_POWERED_DURATION = 0.2
    RIKU_ANIMATION_TIRED_DURATION   = 0.35

    # frameset durations.
    RIKU_CHANNEL_START_DURATION = 0.6
    RIKU_CHANNEL_SQUAT_DURATION = 1.2
    RIKU_CHANNEL_STAND_DURATION = 0.9
    RIKU_BACKFIRED_PERCENTAGE   = 0.25

    # number of animation frames.
    NUMBER_RIKU_POWERED_FRAMES = 2
    NUMBER_RIKU_TIRED_FRAMES   = 3

    # riku states.
    RIKU_STATE_IDLE          = "riku_idle"
    RIKU_STATE_CHANNEL_START = "riku_start"
    RIKU_STATE_CHANNEL_SQUAT = "riku_squat"
    RIKU_STATE_CHANNEL_STAND = "riku_stand"
    RIKU_STATE_POWERED       = "riku_powered"
    RIKU_STATE_BACKFIRED     = "rik_backfired"
    RIKU_STATE_TIRED         = "riku_tired"

    # points.
    MAGIC_FORCE_CORRECT_SCORE          = 100
    MAGIC_FORCE_BASE_COMPLETION_BONUS  = 300
    MAGIC_FORCE_EXTRA_COMPLETION_BONUS = 50

    # static locations and sizes.
    NUMBER_Y     = 200
    NUMBER_WIDTH = 96

    RIKU_X = 247
    RIKU_Y = 500

    class MagicForce( Minigame ):
        def __init__( self, level_number=1 ):
            super( MagicForce, self ).__init__()

            if level_number > len( MAGIC_FORCE_LEVELS ) or level_number <= 0:
                raise ValueError( "Invalid Magic Force level number %d.  Level "
                                  "number must be between 1 and %d." %
                                  (level_number, len( MAGIC_FORCE_LEVELS )) )

            # setup the level difficulty parameters.
            level = MAGIC_FORCE_LEVELS[level_number - 1]

            self.number_digits     = AutomatedInterpolator( level.number_digits[0],
                                                            level.number_digits[1],
                                                            level.time_limit )
            self.correct_timeout   = level.correct_timeout
            self.incorrect_timeout = level.incorrect_timeout
            self.time_remaining    = AutomatedInterpolator( level.time_limit,
                                                            0,
                                                            level.time_limit )

            self.level_number = level_number

            # setup the game state.
            self.state                = MAGIC_FORCE_GAME_STATE_BEGIN
            self.base_score           = 0
            self.completion_bonus     = 0
            self.total_score          = 0
            self.number_countdown     = 0
            self.current_number_index = 0
            self.number_correct       = 0

            # setup the entities.
            self.current_numbers    = []
            self.riku               = None
            self.start_screen_hud   = None
            self.stop_screen_hud    = None
            self.score_hud          = None
            self.time_remaining_hud = None
            self.instructions_hud   = None
            self.instructions_index = 0
            
            self.create_numbers()
            self.create_riku()
            self.create_huds()

            # get the first number.
            self.pick_numbers()

        def create_numbers( self ):
            for digit in xrange( 10 ):
                number = GameObject()
                number["renderer"] = GameRenderer( GameImage( "gfx/magic_force/numbers/number%d-default.png" % digit ) )
                number["renderer"].set_frame( NUMBER_FRAMESET_CORRECT, GameImage( "gfx/magic_force/numbers/number%d-correct.png" % digit ) )
                number["renderer"].set_frame( NUMBER_FRAMESET_INCORRECT, GameImage( "gfx/magic_force/numbers/number%d-incorrect.png" % digit ) )
                PrefabFactory.add_prefab( "number%d" % digit, number )

        def create_riku( self ):
            self.riku             = GameObject()
            self.riku["renderer"] = GameRenderer()
            self.riku["behavior"] = RikuBehavior( self.incorrect_timeout )
            self.riku["renderer"].set_frame( RIKU_FRAMESET_IDLE, GameImage( "gfx/magic_force/riku/riku-idle.png", Anchor.BOTTOM_LEFT ) )
            self.riku["renderer"].set_frame( RIKU_FRAMESET_CHANNEL_START, GameImage( "gfx/magic_force/riku/riku-channel_start.png", Anchor.BOTTOM_LEFT ) )
            self.riku["renderer"].set_frame( RIKU_FRAMESET_CHANNEL_SQUAT, GameImage( "gfx/magic_force/riku/riku-channel_squat.png", Anchor.BOTTOM_LEFT ) )
            self.riku["renderer"].set_frame( RIKU_FRAMESET_CHANNEL_STAND, GameImage( "gfx/magic_force/riku/riku-channel_stand.png", Anchor.BOTTOM_LEFT ) )
            self.riku["renderer"].set_frame( RIKU_FRAMESET_BACKFIRED, GameImage( "gfx/magic_force/riku/riku-backfired.png", Anchor.BOTTOM_LEFT ) )
            self.riku["renderer"].add_animation( RIKU_ANIMATION_POWERED,
                                                 GameAnimation( [ GameImage( "gfx/magic_force/riku/riku-powered%d.png" % frame_index, Anchor.BOTTOM_LEFT )
                                                                  for frame_index in xrange( NUMBER_RIKU_POWERED_FRAMES ) ],
                                                                NUMBER_RIKU_POWERED_FRAMES / RIKU_ANIMATION_POWERED_DURATION ) )
            self.riku["renderer"].add_animation( RIKU_ANIMATION_TIRED,
                                                 GameAnimation( [ GameImage( "gfx/magic_force/riku/riku-tired%d.png" % frame_index, Anchor.BOTTOM_LEFT )
                                                                  for frame_index in xrange( NUMBER_RIKU_TIRED_FRAMES ) ],
                                                                NUMBER_RIKU_TIRED_FRAMES / RIKU_ANIMATION_TIRED_DURATION ) )
            self.riku["transform"].set_position( RIKU_X, RIKU_Y )
            self.riku["transform"].set_scale( 2.0 )
            self.riku["behavior"].idle()

        def create_huds( self ):
            self.start_screen_hud             = GameObject()
            self.start_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/magic_force/start_screen.png" ) )
            self.start_screen_hud["transform"].set_position( 148, 50 )

            self.stop_screen_hud             = GameObject()
            self.stop_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/magic_force/stop_screen.png" ) )
            self.stop_screen_hud["transform"].set_position( 148, 50 )
            
            self.score_hud             = GameObject()
            self.score_hud["renderer"] = GameRenderer( GameText( self.get_score, Color( 255, 255, 255, 255 ) ) )
            self.score_hud["transform"].set_position( 400, 30 )
            
            instructions_1 = GameObject()
            instructions_1["renderer"] = GameRenderer( GameImage ( "gfx/magic_force/instructions_1.png" ) )
            instructions_1["transform"].set_position( 148, 50 )
            instructions_2 = GameObject()
            instructions_2["renderer"] = GameRenderer( GameImage ( "gfx/magic_force/instructions_2.png" ) )
            instructions_2["transform"].set_position( 148, 50 )
            instructions_3 = GameObject()
            instructions_3["renderer"] = GameRenderer( GameImage ( "gfx/magic_force/instructions_3.png" ) )
            instructions_3["transform"].set_position( 148, 50 )
            self.instructions = [instructions_1, instructions_2, instructions_3]
            
            high_score = GameObject()
            high_score["renderer"] = GameRenderer( GameText( self.get_high_score, Color( 255, 255, 255, 255 ) ) )
            high_score["transform"].set_position( 138, 313 )
            self.start_screen_hud.add_child( high_score )

            level = GameObject()
            level["renderer"] = GameRenderer( GameText( self.get_level_number, Color( 255, 255, 255, 255 ) ) )
            level["transform"].set_position( 138, 360 )
            self.start_screen_hud.add_child( level )

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

            self.time_remaining_hud             = GameObject()
            self.time_remaining_hud["renderer"] = GameRenderer( GameText( self.get_time_remaining, Color( 255, 255, 255, 255 ) ) )
            self.time_remaining_hud["transform"].set_position( 30, 30 )

        def pick_numbers( self ):
            # clear the current numbers.
            self.current_numbers = []

            # figure out where to position the individual numbers to that they
            # are centered on the screen.
            number_digits = self.number_digits.get_truncated_value()

            y = NUMBER_Y
            x = self.get_game_width() / 2 - NUMBER_WIDTH * number_digits / 2

            # create a string of numbers for the player to enter.
            for digit_index in xrange( number_digits ):
                if number_digits > 1 and digit_index != number_digits - 1:
                    digit = renpy.random.randint( 1, 9 )
                else:
                    digit = renpy.random.randint( 0, 9 )

                number             = PrefabFactory.instantiate( "number%d" % digit )
                number["behavior"] = NumberBehavior( digit )
                number["transform"].set_position( x + digit_index * NUMBER_WIDTH, y )
                self.current_numbers.append( number )

            # reset the current number index.
            self.current_number_index = 0

        def compute_completion_bonus( self ):
            self.completion_bonus = 0
            if self.number_correct > 30:
                self.completion_bonus += MAGIC_FORCE_BASE_COMPLETION_BONUS
            if self.number_correct > 35:
                self.completion_bonus += MAGIC_FORCE_EXTRA_COMPLETION_BONUS
            if self.number_correct > 40:
                self.completion_bonus += MAGIC_FORCE_EXTRA_COMPLETION_BONUS
            if self.number_correct > 45:
                self.completion_bonus += MAGIC_FORCE_EXTRA_COMPLETION_BONUS
            if self.number_correct > 50:
                self.completion_bonus += MAGIC_FORCE_EXTRA_COMPLETION_BONUS

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
            
        def get_level_number( self ):
            return "%20d" % self.level_number

        def get_displayables( self ):
            displayables = []
            displayables.extend( self.riku["renderer"].get_displayables() )
            for number in self.current_numbers:
                displayables.extend( number["renderer"].get_displayables() )
            
            displayables.extend( self.start_screen_hud["renderer"].get_displayables() )
            displayables.extend( self.stop_screen_hud["renderer"].get_displayables() )
            displayables.extend( self.score_hud["renderer"].get_displayables() )
            displayables.extend( self.time_remaining_hud["renderer"].get_displayables() )
            
            for instruction in self.instructions:
                displayables.extend( instruction["renderer"].get_displayables() )
            
            return displayables

        def render( self, blitter, clip_rect ):
            world_transform = self.get_world_transform()

            if self.state == MAGIC_FORCE_GAME_STATE_BEGIN:
                self.start_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == MAGIC_FORCE_GAME_STATE_END:
                self.stop_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == MAGIC_FORCE_GAME_STATE_PAUSE:
                self.instructions[self.instructions_index]["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == MAGIC_FORCE_GAME_STATE_PLAY:
                self.riku["renderer"].render( blitter, clip_rect, world_transform )
                for number in self.current_numbers:
                    number["renderer"].render( blitter, clip_rect, world_transform )

                self.time_remaining_hud["renderer"].render( blitter, clip_rect, world_transform )
                self.score_hud["renderer"].render( blitter, clip_rect, world_transform )

        def update( self, delta_sec ):
            if self.state == MAGIC_FORCE_GAME_STATE_PLAY:
                # update automated parameters.
                self.number_digits.update( delta_sec )
                self.time_remaining.update( delta_sec )

                # update riku.
                self.riku.update( delta_sec )

                if self.number_countdown >= 0:
                    self.number_countdown -= delta_sec
                    if self.number_countdown <= 0:
                        self.pick_numbers()

                # see if it's game over.
                if self.time_remaining.get_value() <= 0:
                    self.state = MAGIC_FORCE_GAME_STATE_END
                    self.compute_completion_bonus()
                    self.total_score = self.base_score + self.completion_bonus

        def on_key_down( self, key ):
            if self.state == MAGIC_FORCE_GAME_STATE_BEGIN:
                if key == pygame.K_h:
                    self.state = MAGIC_FORCE_GAME_STATE_PAUSE
                else:
                    self.state = MAGIC_FORCE_GAME_STATE_PLAY
                    self.riku["behavior"].channel_magic()
            elif (self.state == MAGIC_FORCE_GAME_STATE_PLAY and
                self.number_countdown <= 0):
                if key in (pygame.K_KP0, pygame.K_0,
                           pygame.K_KP1, pygame.K_1,
                           pygame.K_KP2, pygame.K_2,
                           pygame.K_KP3, pygame.K_3,
                           pygame.K_KP4, pygame.K_4,
                           pygame.K_KP5, pygame.K_5,
                           pygame.K_KP6, pygame.K_6,
                           pygame.K_KP7, pygame.K_7,
                           pygame.K_KP8, pygame.K_8,
                           pygame.K_KP9, pygame.K_9):
                    number = self.current_numbers[self.current_number_index]
                    if number["behavior"].is_digit_pressed( key ):
                        # correct number key was hit.  hightlight the correct
                        # number.  set our next number to check.  if we have
                        # checked all the numbers, set a countdown for when
                        # the next number will be displayed.
                        number["renderer"].set_frameset( NUMBER_FRAMESET_CORRECT )
                        self.current_number_index += 1

                        if self.current_number_index == len( self.current_numbers ):
                            self.number_countdown  = self.correct_timeout
                            self.number_correct   += 1
                            self.base_score       += MAGIC_FORCE_CORRECT_SCORE
                    else:
                        # wrong number key was hit.  highlight the incorrect
                        # number and set a countdown for when the next number
                        # will be displayed.
                        number["renderer"].set_frameset( NUMBER_FRAMESET_INCORRECT )
                        self.number_countdown = self.incorrect_timeout
                        self.riku["behavior"].backfire()
                elif key == pygame.K_h:
                    self.state = MAGIC_FORCE_GAME_STATE_PAUSE
            elif self.state == MAGIC_FORCE_GAME_STATE_PAUSE:
                self.show_next_instruction()

        def on_mouse_up( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == MAGIC_FORCE_GAME_STATE_BEGIN:
                    self.state = MAGIC_FORCE_GAME_STATE_PLAY
                    self.riku["behavior"].channel_magic()
                elif self.state == MAGIC_FORCE_GAME_STATE_PAUSE:
                    self.show_next_instruction()
                elif self.state == MAGIC_FORCE_GAME_STATE_END:
                    self.quit()
                    
        def show_next_instruction( self ):
            if self.instructions_index < len(self.instructions)-1:
                self.instructions_index += 1
            else:
                self.instructions_index = 0
                self.state = MAGIC_FORCE_GAME_STATE_PLAY
                self.riku["behavior"].channel_magic()

    class NumberBehavior( GameObject ):
        def __init__( self, digit ):
            valid_keys = { 0 : (pygame.K_KP0, pygame.K_0),
                           1 : (pygame.K_KP1, pygame.K_1),
                           2 : (pygame.K_KP2, pygame.K_2),
                           3 : (pygame.K_KP3, pygame.K_3),
                           4 : (pygame.K_KP4, pygame.K_4),
                           5 : (pygame.K_KP5, pygame.K_5),
                           6 : (pygame.K_KP6, pygame.K_6),
                           7 : (pygame.K_KP7, pygame.K_7),
                           8 : (pygame.K_KP8, pygame.K_8),
                           9 : (pygame.K_KP9, pygame.K_9) }

            self.valid_keys = valid_keys[digit]

        def is_digit_pressed( self, key ):
            return key in self.valid_keys

    class RikuBehavior( GameObject ):
        def __init__( self, incorrect_timeout ):
            self.state             = RIKU_STATE_IDLE
            self.frame_countdown   = 0
            self.incorrect_timeout = incorrect_timeout

        def update( self, delta_sec ):
            if self.state not in (RIKU_STATE_IDLE, RIKU_STATE_POWERED):
                self.frame_countdown -= delta_sec

            if self.state == RIKU_STATE_CHANNEL_START:
                if self.frame_countdown <= 0:
                    self.state           = RIKU_STATE_CHANNEL_SQUAT
                    self.frame_countdown = RIKU_CHANNEL_SQUAT_DURATION
                    self.game_object["renderer"].set_frameset( RIKU_FRAMESET_CHANNEL_SQUAT )
            elif self.state == RIKU_STATE_CHANNEL_SQUAT:
                if self.frame_countdown <= 0:
                    self.state           = RIKU_STATE_CHANNEL_STAND
                    self.frame_countdown = RIKU_CHANNEL_STAND_DURATION
                    self.game_object["renderer"].set_frameset( RIKU_FRAMESET_CHANNEL_STAND )
            elif self.state == RIKU_STATE_CHANNEL_STAND:
                if self.frame_countdown <= 0:
                    self.power_up()
            elif self.state == RIKU_STATE_BACKFIRED:
                if self.frame_countdown <= 0:
                    self.state           = RIKU_STATE_TIRED
                    self.frame_countdown = self.incorrect_timeout * (1.0 - RIKU_BACKFIRED_PERCENTAGE)
                    self.game_object["renderer"].play_animation( RIKU_ANIMATION_TIRED )
            elif self.state == RIKU_STATE_TIRED:
                if self.frame_countdown <= 0:
                    self.game_object["renderer"].stop_animation()
                    self.channel_magic()

        def idle( self ):
            self.state = RIKU_STATE_IDLE
            self.game_object["renderer"].set_frameset( RIKU_FRAMESET_IDLE )

        def channel_magic( self ):
            self.state           = RIKU_STATE_CHANNEL_START
            self.frame_countdown = RIKU_CHANNEL_START_DURATION
            self.game_object["renderer"].set_frameset( RIKU_FRAMESET_CHANNEL_START )

        def power_up( self ):
            self.state = RIKU_STATE_POWERED
            self.game_object["renderer"].play_animation( RIKU_ANIMATION_POWERED )

        def backfire( self ):
            self.state           = RIKU_STATE_BACKFIRED
            self.frame_countdown = self.incorrect_timeout * RIKU_BACKFIRED_PERCENTAGE
            self.game_object["renderer"].stop_animation()
            self.game_object["renderer"].set_frameset( RIKU_FRAMESET_BACKFIRED )
