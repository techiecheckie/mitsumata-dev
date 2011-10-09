init python:
    import math
    import pygame
    import time

    # map of pygame event types to a string describing them.
    PYGAME_EVENT_NAMES = { pygame.QUIT            : "Quit",
                           pygame.ACTIVEEVENT     : "Active Event",
                           pygame.KEYDOWN         : "Key Down",
                           pygame.KEYUP           : "Key Up",
                           pygame.MOUSEMOTION     : "Mouse Motion",
                           pygame.MOUSEBUTTONUP   : "Mouse Button Up",
                           pygame.MOUSEBUTTONDOWN : "Mouse Button Down",
                           pygame.JOYAXISMOTION   : "Joystick Axis Motion",
                           pygame.JOYBALLMOTION   : "Joystick Ball Motion",
                           pygame.JOYBUTTONUP     : "Joystick Button Up",
                           pygame.JOYBUTTONDOWN   : "Joystick Button Down",
                           pygame.VIDEORESIZE     : "Video Resize",
                           pygame.VIDEOEXPOSE     : "Video Expose",
                           pygame.USEREVENT       : "User Event" }

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

    # different states the whack a mole game can be in.
    MOLE_STATE_BEGIN = "mole_begin"
    MOLE_STATE_PLAY  = "mole_play"
    MOLE_STATE_END   = "mole_end"

    # different states each mole can be in.
    MOLE_ANIM_STATE_EMERGE   = "mole_emerge"
    MOLE_ANIM_STATE_IDLE     = "mole_idle"
    MOLE_ANIM_STATE_SUBMERGE = "mole_submerge"
    MOLE_ANIM_STATE_BURIED   = "mole_buried"

    # messages displayed for each of the whack a mole game states.
    STATE_MESSAGES = { MOLE_STATE_BEGIN : "Click anywhere to begin!",
                       MOLE_STATE_PLAY  : "GO! Whack them moles!",
                       MOLE_STATE_END   : "Game over!\nClick quit to exit." }

    # stores info on a visible mole.
    class Mole( object ):
        def __init__( self, cell, duration ):
            self.cell         = cell
            self.duration     = duration
            self.elapsed_time  = 0
            self.current_frame = 0
            self.state         = MOLE_ANIM_STATE_EMERGE

            # constants.  the start, stop, and number of frames are relative
            # to the WhackAMole.mole_frames list.  specifically, it assumes
            # that mole_frames stores frames 1 through 11 of the mole
            # animation, meaning frame indices are offset by 1.
            self.EMERGE_DURATION          = 0.7
            self.EMERGE_START_FRAME_INDEX = 0
            self.EMERGE_STOP_FRAME_INDEX  = 11
            self.NUMBER_EMERGE_FRAMES     = (self.EMERGE_STOP_FRAME_INDEX -
                                             self.EMERGE_START_FRAME_INDEX + 1)

            # submerge animation starts on frame number 8, which corresponds to
            # index 7 in WhackAMole.mole_frames.
            self.SUBMERGE_DURATION          = 0.5
            self.SUBMERGE_START_FRAME_INDEX = 7
            self.SUBMERGE_STOP_FRAME_INDEX  = 0
            self.NUMBER_SUBMERGE_FRAMES     = (self.SUBMERGE_START_FRAME_INDEX -
                                               self.SUBMERGE_STOP_FRAME_INDEX + 1)

        # returns True if the mole is buried and should be removed from the
        # game's list of active moles.
        def update( self, time_delta ):
            self.elapsed_time  += time_delta

            if self.state == MOLE_ANIM_STATE_EMERGE:
                frame_offset       = math.trunc( self.elapsed_time /
                                                 self.EMERGE_DURATION *
                                                 (self.NUMBER_EMERGE_FRAMES - 1) )
                self.current_frame = self.EMERGE_START_FRAME_INDEX + frame_offset

                if self.elapsed_time >= self.EMERGE_DURATION:
                    self.state        = MOLE_ANIM_STATE_IDLE
                    self.elapsed_time = 0
            elif self.state == MOLE_ANIM_STATE_IDLE:
                if self.elapsed_time >= self.duration:
                    self.state        = MOLE_ANIM_STATE_SUBMERGE
                    self.elapsed_time = 0
            elif self.state == MOLE_ANIM_STATE_SUBMERGE:
                # NOTE: since we play the animation in reverse, we subtract the
                #       offset this time around.
                frame_offset       = math.trunc( self.elapsed_time /
                                                 self.SUBMERGE_DURATION *
                                                 (self.NUMBER_SUBMERGE_FRAMES - 1) )
                self.current_frame = self.SUBMERGE_START_FRAME_INDEX - frame_offset

                if self.elapsed_time >= self.SUBMERGE_DURATION:
                    self.state = MOLE_ANIM_STATE_BURIED
            elif self.state == MOLE_ANIM_STATE_BURIED:
                return True

    # an image button that can be used inside a Ren'Py minigame where
    # ui.interact() has been called with suppress_overlay = True.
    class MinigameButton( renpy.Displayable ):
        def __init__( self, image, x, y, visible=True, **kwds ):
            super( MinigameButton, self ).__init__( **kwds )

            self.image   = image
            self.x       = x
            self.y       = y
            self.visible = visible
            image_render = renpy.render( self.image, 0, 0, 0, 0 )
            image_size   = image_render.get_size()
            self.width   = image_size[0]
            self.height  = image_size[1]

        # draw the ui button using the given renpy.Render object.
        def draw( self, render, st, at ):
            image_render = renpy.render( self.image, 0, 0, st, at )
            render.blit( image_render, (self.x, self.y) )

        # boiler plate.
        def visit( self ):
            return [ self.image ]

        # returns True if the button is visible and the mouse is clicked inside
        # its bounds.
        def is_clicked( self, mx, my ):
            if not self.visible:
                return False

            left   = self.x
            top    = self.y
            right  = left + self.width
            bottom = top + self.height

            return left <= mx <= right and top <= my <= bottom

    # computes ranges for AutomatedRange based on the absolute extent of a
    # parameter and the desired width and distance of the sliding window that
    # will move over those values.
    def compute_range( absolute_min, absolute_max, width_percentage, alpha ):
        range_width  = (absolute_max - absolute_min) * width_percentage / 100.0
        range_middle = absolute_min * (1.0 - alpha) + absolute_max * alpha
        range_min    = range_middle - range_width / 2.0
        range_max    = range_middle + range_width / 2.0

        # make sure we don't fall outside the absolute min and max values.
        return ( max( range_min, absolute_min ), min( range_max, absolute_max ) )

    # automated range of parameter values.
    class AutomatedRange( object ):
        def __init__( self, name, initial_min, initial_max,
                      final_min, final_max, duration ):
            super( AutomatedRange, self ).__init__()
            self.name         = name
            self.initial_min  = initial_min
            self.initial_max  = initial_max
            self.min_distance = final_min - initial_min
            self.max_distance = final_max - initial_max
            self.range_min    = initial_min
            self.range_max    = initial_max
            self.duration     = duration
            self.elapsed_time = 0

            renpy.log( "INITIALIZING %s: (%.3f, %.3f) -> (%.3f, %.3f)" %
                       (self.name, initial_min, initial_max, final_min, final_max) )

        def update( self, delta_time ):
            self.elapsed_time += delta_time
            ratio              = self.elapsed_time / self.duration
            self.range_min     = self.initial_min + self.min_distance * ratio
            self.range_max     = self.initial_max + self.max_distance * ratio

        def get_value( self ):
            value = renpy.random.uniform( self.range_min, self.range_max )
            renpy.log( "(%s) Value: %.3f   Elapsed: %s   Min: %.3f   Max: %.3f" %
                       (self.name, value, self.elapsed_time,
                        self.range_min, self.range_max) )
            return value

    # displayable used for implementing the whack a mole minigame.
    class WhackAMole( renpy.Displayable ):
        # idea is difficulty = 0 is the easiest, difficult = 1 is the hardest.
        def __init__( self, initial_difficulty=0.5, final_difficulty=0.5, **kwds ):
            super( WhackAMole, self ).__init__( **kwds )

            # how long the game will last in seconds.
            GAME_DURATION = 30

            # game state.
            self.seconds_remaining = GAME_DURATION
            self.state             = MOLE_STATE_BEGIN
            self.score             = 0
            self.active_moles      = []
            self.final_score       = 0

            # difficulty controls.  each control defines an absolute min value
            # and an absolute max value.  this percentage controls how much
            # the difficulty varies as a function of a fixed percent of the
            # range of valid values for that control.
            DIFFICULTY_VARIANCE = 30

            # the maximum number of moles that can be on the game board at a time.
            MAX_ACTIVE_MOLES_CONTROL_MIN = 1
            MAX_ACTIVE_MOLES_CONTROL_MAX = 5

            initial_range = compute_range( MAX_ACTIVE_MOLES_CONTROL_MIN,
                                           MAX_ACTIVE_MOLES_CONTROL_MAX,
                                           DIFFICULTY_VARIANCE,
                                           initial_difficulty )
            final_range   = compute_range( MAX_ACTIVE_MOLES_CONTROL_MIN,
                                           MAX_ACTIVE_MOLES_CONTROL_MAX,
                                           DIFFICULTY_VARIANCE,
                                           final_difficulty )

            self.max_active_moles = AutomatedRange( "max_active_moles",
                                                    initial_range[0], initial_range[1],
                                                    final_range[0], final_range[1],
                                                    GAME_DURATION )

            # the amount of time until the next mole appears on the board.
            # because this range decreases as we get more difficult, use the
            # inverse of the given difficulties.
            MOLE_SPAWN_TIME_CONTROL_MIN  = 0.25
            MOLE_SPAWN_TIME_CONTROL_MAX  = 0.75

            initial_range = compute_range( MOLE_SPAWN_TIME_CONTROL_MIN,
                                           MOLE_SPAWN_TIME_CONTROL_MAX,
                                           DIFFICULTY_VARIANCE,
                                           1 - initial_difficulty )
            final_range   = compute_range( MOLE_SPAWN_TIME_CONTROL_MIN,
                                           MOLE_SPAWN_TIME_CONTROL_MAX,
                                           DIFFICULTY_VARIANCE,
                                           1 - final_difficulty )

            self.mole_spawn_time = AutomatedRange( "mole_spawn_time",
                                                   initial_range[0], initial_range[1],
                                                   final_range[0], final_range[1],
                                                   GAME_DURATION )

            # the amount of time a mole stays on the screen after it has fully
            # finished its emerged animation.  because this range decreases as
            # we get more difficult, use the inverse of the given
            # difficulties.
            MOLE_DURATION_TIME_CONTROL_MIN = 0.35
            MOLE_DURATION_TIME_CONTROL_MAX = 1.6

            initial_range = compute_range( MOLE_DURATION_TIME_CONTROL_MIN,
                                           MOLE_DURATION_TIME_CONTROL_MAX,
                                           DIFFICULTY_VARIANCE,
                                           1 - initial_difficulty )
            final_range   = compute_range( MOLE_DURATION_TIME_CONTROL_MIN,
                                           MOLE_DURATION_TIME_CONTROL_MAX,
                                           DIFFICULTY_VARIANCE,
                                           1 - final_difficulty )

            self.mole_duration_time = AutomatedRange( "mole_duration_time",
                                                      initial_range[0], initial_range[1],
                                                      final_range[0], final_range[1],
                                                      GAME_DURATION )

            # timing state.
            self.last_time      = 0
            self.mole_countdown = 0

            # image assets.
            self.sprite_manager = SpriteManager()
            self.background     = Image( "gfx/backgrounds/whack_a_mole_bg.png" )
            self.mole_frames    = [ Image( "gfx/animated/mole/mole_1.png" ),
                                    Image( "gfx/animated/mole/mole_2.png" ),
                                    Image( "gfx/animated/mole/mole_3.png" ),
                                    Image( "gfx/animated/mole/mole_4.png" ),
                                    Image( "gfx/animated/mole/mole_5.png" ),
                                    Image( "gfx/animated/mole/mole_6.png" ),
                                    Image( "gfx/animated/mole/mole_7.png" ),
                                    Image( "gfx/animated/mole/mole_8.png" ),
                                    Image( "gfx/animated/mole/mole_9.png" ),
                                    Image( "gfx/animated/mole/mole_10.png" ),
                                    Image( "gfx/animated/mole/mole_11.png" ),
                                    Image( "gfx/animated/mole/mole_12.png" ) ]
            self.dirt           = self.mole_frames[0]

            # Get a render object so we can use ren'py to figure out the size
            # of each of art assets.
            background_render = renpy.render( self.background, 0, 0, 0, 0 )
            background_size   = background_render.get_size()
            mole_render       = renpy.render( self.dirt, 0, 0, 0, 0 )
            mole_size         = mole_render.get_size()

            # size and position constants.
            self.BACKGROUND_WIDTH  = background_size[0]
            self.BACKGROUND_HEIGHT = background_size[1]
            self.BACKGROUND_LEFT   = 370
            self.BACKGROUND_TOP    = 115

            self.MOLE_WIDTH  = mole_size[0]
            self.MOLE_HEIGHT = mole_size[1]

            self.NUMBER_ROWS    = 3
            self.NUMBER_COLUMNS = 3

            self.TEXT_LEFT = 60
            self.TEXT_TOP  = 100

            # ui assets.
            self.quit_button = MinigameButton( Image( "gfx/quit_button.png" ),
                                               self.TEXT_LEFT, self.TEXT_TOP + 100,
                                               False )

        # boiler plate needed by Displayable class.  just returns all children
        # displayables.
        #
        # XXX: I don't know how important it is to get ALL displayables used in
        #      this list.  Trying to track the Text displayables given how
        #      transient they are seems more of a pain than it may be worth.
        def visit( self ):
            children = [ self.background ]
            children.extend( self.mole_frames )
            return children

        # event handler.  handles mouse clicks, updates the game board, and
        # stops the game once time has run out.
        def event( self, e, x, y, st ):
            if self.state == MOLE_STATE_BEGIN:
                # start the game after the player clicks to start.
                if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                    self.state          = MOLE_STATE_PLAY
                    self.last_time      = time.time()
                    self.mole_countdown = self.mole_spawn_time.get_value()
            elif self.state == MOLE_STATE_END:
                # leave the game once the player clicks.
                #if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                #    if self.quit_button.is_clicked( x, y ):
                #        return self.score
                self.final_score = self.score
                return
            elif self.state == MOLE_STATE_PLAY:
                # update the countdown timers.
                current_time            = time.time()
                time_delta              = current_time - self.last_time
                self.last_time          = current_time
                self.seconds_remaining -= time_delta
                self.mole_countdown    -= time_delta

                # automate the difficulty parameters.
                self.max_active_moles.update( time_delta )
                self.mole_spawn_time.update( time_delta )
                self.mole_duration_time.update( time_delta )

                # list of moles to add and remove this frame.
                moles_to_add    = []
                moles_to_remove = []

                # see if it's time to add another mole.
                if self.mole_countdown <= 0 and self.seconds_remaining > 0:
                    # don't exceed the max we can have on the screen at a time.
                    if len( self.active_moles ) + 1 < self.max_active_moles.get_value():
                        mole = self.create_mole()
                        moles_to_add.append( self.create_mole() )

                    # reset when we try to add another mole.
                    self.mole_countdown = self.mole_spawn_time.get_value()

                # update active moles and remove those that are buried.
                for mole in self.active_moles:
                    if mole.update( time_delta ):
                        moles_to_remove.append( mole )

                for mole in moles_to_remove:
                    self.active_moles.remove( mole )

                for mole in moles_to_add:
                    self.active_moles.append( mole )

                # see if we hit a mole.
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    mole = self.get_mole_at_mouse( x, y )
                    if mole:
                        self.active_moles.remove( mole )
                        self.score += 1

                # stop the game if there's no more time.  make sure to show
                # the quit button at this time, and remove any visible moles.
                if self.seconds_remaining <= 0:
                    self.state               = MOLE_STATE_END
                    self.quit_button.visible = True
                    self.active_moles        = []

            # continually render and update.
            renpy.redraw( self, 0 )
            renpy.timeout( 0 )

        # creates a new mole to add to the game board.
        def create_mole( self ):
            # keep trying to find a free cell.
            cell = self.get_random_cell()
            while self.is_cell_active( cell ):
                cell = self.get_random_cell()

            duration = self.mole_duration_time.get_value()
            return Mole( cell, duration )

        # gets a random cell in the game board as a (row, col) tuple.
        def get_random_cell( self ):
            return (renpy.random.randint( 0, self.NUMBER_ROWS - 1),
                    renpy.random.randint( 0, self.NUMBER_COLUMNS - 1))

        # returns True if a mole is occupying the given cell.  otherwise False.
        def is_cell_active( self, cell ):
            for mole in self.active_moles:
                if cell == mole.cell:
                    return True
            return False

        # returns the Mole object under the given mouse position or None if
        # there is no Mole currently.
        def get_mole_at_mouse( self, mx, my ):
            for mole in self.active_moles:
                position = CELL_POSITIONS[mole.cell]
                left     = self.BACKGROUND_LEFT + position[0]
                top      = self.BACKGROUND_TOP + position[1]
                right    = left + self.MOLE_WIDTH
                bottom   = top + self.MOLE_HEIGHT
                if left <= mx <= right and top <= my <= bottom:
                    return mole

        # renders the game.
        def render( self, width, height, st, at ):
            render = renpy.Render( width, height )

            # render the background.
            background_render = renpy.render( self.background, 1024, 768, st, at )
            render.blit( background_render, (self.BACKGROUND_LEFT, self.BACKGROUND_TOP) )

            # render the timer.
            timer_text   = Text( "Time Remaining: %d" % self.seconds_remaining )
            timer_render = renpy.render( timer_text, renpy.config.screen_width,
                                         renpy.config.screen_height, st, at )
            render.blit( timer_render, (self.TEXT_LEFT, self.TEXT_TOP) )

            # render the score.
            score_text   = Text( "Score: %d" % self.score )
            score_render = renpy.render( score_text, renpy.config.screen_width,
                                         renpy.config.screen_height, st, at )
            render.blit( score_render, (self.TEXT_LEFT, self.TEXT_TOP + 24) )

            # render state-sensitive message.
            message_text   = Text( STATE_MESSAGES[self.state] )
            message_render = renpy.render( message_text, renpy.config.screen_width,
                                           renpy.config.screen_height, st, at )
            render.blit( message_render, (self.TEXT_LEFT, self.TEXT_TOP + 48) )

            # render the quit button if it's visible.
            #if self.quit_button.visible:
            #    self.quit_button.draw( render, st, at )

            # render each dirt mound.
            dirt_render = renpy.render( self.dirt, 0, 0, st, at )
            for position in CELL_POSITIONS.values():
                x = self.BACKGROUND_LEFT + position[0]
                y = self.BACKGROUND_TOP + position[1]
                render.blit( dirt_render, (x,y) )

            # render the moles on screen.
            for mole in self.active_moles:
                position    = CELL_POSITIONS[mole.cell]
                x           = self.BACKGROUND_LEFT + position[0]
                y           = self.BACKGROUND_TOP + position[1]
                mole_render = renpy.render( self.mole_frames[mole.current_frame],
                                            0, 0, st, at )
                render.blit( mole_render, (x,y) )

            return render
            
        def get_final_score(self):
          return self.final_score

    # Minigame starts here.  Change this label to start and the start label in
    # script.rpy to something else to test this out.
    def start_mole_game():
      # the first parameter is the initial relative difficulty.  the second
        # is the final relative difficulty.  for both values, 0 is the easiest,
        # and 1 is the hardest.
        whack = WhackAMole( 0.15, 0.95 )
        ui.add( whack )
        #result = ui.interact( suppress_overlay=True, suppress_underlay=True )
        ui.interact()
        # Could do update_stats(whack.get_final_score()) or something similar here
        # to see if the user has finished the game (succesfully) and if the stats
        # should be updated. For now this'll just print the final score.

        return whack.get_final_score()