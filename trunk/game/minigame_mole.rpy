﻿init python:
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
    CELL_POSITIONS = { (0,0) : (80, 72),
                       (0,1) : (286, 74),
                       (0,2) : (495, 72),
                       (1,0) : (79, 227),
                       (1,1) : (284, 235),
                       (1,2) : (506, 244),
                       (2,0) : (80, 421),
                       (2,1) : (282, 424),
                       (2,2) : (509, 424) }

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
                       MOLE_STATE_END   : "Game over!" }

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

    # displayable used for implementing the whack a mole minigame.
    class WhackAMole( renpy.Displayable ):
        def __init__( self, **kwds ):
            super( WhackAMole, self ).__init__( **kwds )

            # game state.
            self.seconds_remaining = 15
            self.state             = MOLE_STATE_BEGIN
            self.score             = 0
            self.active_moles      = []

            # difficulty controls.
            self.MAX_ACTIVE_MOLES       = 3
            self.MIN_MOLE_SPAWN_TIME    = 0.35
            self.MAX_MOLE_SPAWN_TIME    = 0.75
            self.MIN_MOLE_DURATION_TIME = 0.8
            self.MAX_MOLE_DURATION_TIME = 1.6

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

            # ui assets.
            self.quit_button = MinigameButton( Image( "gfx/quit_button.png" ),
                                               0, 100, False )

            # get a render object so we can use ren'py to figure out the size
            # of each of art assets.
            background_render = renpy.render( self.background, 0, 0, 0, 0 )
            background_size   = background_render.get_size()

            # size and position constants.
            self.BACKGROUND_WIDTH  = background_size[0]
            self.BACKGROUND_HEIGHT = background_size[1]
            self.BACKGROUND_LEFT   = 320
            self.BACKGROUND_TOP    = 100

            self.MOLE_WIDTH  = 60
            self.MOLE_HEIGHT = 60

            self.NUMBER_ROWS    = 3
            self.NUMBER_COLUMNS = 3

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
                    self.mole_countdown = self.get_next_mole_countdown()
            elif self.state == MOLE_STATE_END:
                # leave the game once the player hits the quit button.
                if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                    if self.quit_button.is_clicked( x, y ):
                        return self.score
            elif self.state == MOLE_STATE_PLAY:
                # update the countdown timers.
                current_time            = time.time()
                time_delta              = current_time - self.last_time
                self.last_time          = current_time
                self.seconds_remaining -= time_delta
                self.mole_countdown    -= time_delta

                # list of moles to add and remove this frame.
                moles_to_add    = []
                moles_to_remove = []

                # see if it's time to add another mole.
                if self.mole_countdown <= 0 and self.seconds_remaining > 0:
                    # don't exceed the max we can have on the screen at a time.
                    if len( self.active_moles ) != self.MAX_ACTIVE_MOLES:
                        mole = self.create_mole()
                        moles_to_add.append( self.create_mole() )

                    # reset when we try to add another mole.
                    self.mole_countdown = self.get_next_mole_countdown()

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

            duration = self.get_random_mole_duration()
            return Mole( cell, duration )

        # gets the time to wait before trying to add another mole.
        def get_next_mole_countdown( self ):
            return renpy.random.uniform( self.MIN_MOLE_SPAWN_TIME,
                                         self.MAX_MOLE_SPAWN_TIME )

        # get the amount of time a mole will stay full emerged before going
        # back into the board.
        def get_random_mole_duration( self ):
            return renpy.random.uniform( self.MIN_MOLE_DURATION_TIME,
                                         self.MAX_MOLE_DURATION_TIME )

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
            background_render = renpy.render( self.background, 0, 0, st, at )
            render.blit( background_render, (self.BACKGROUND_LEFT, self.BACKGROUND_TOP) )

            # render the timer.
            timer_text   = Text( "Time Remaining: %d" % self.seconds_remaining )
            timer_render = renpy.render( timer_text, renpy.config.screen_width,
                                         renpy.config.screen_height, st, at )
            render.blit( timer_render, (0, 0) )

            # render the score.
            score_text   = Text( "Score: %d" % self.score )
            score_render = renpy.render( score_text, renpy.config.screen_width,
                                         renpy.config.screen_height, st, at )
            render.blit( score_render, (0, 24) )

            # render state-sensitive message.
            message_text   = Text( STATE_MESSAGES[self.state] )
            message_render = renpy.render( message_text, renpy.config.screen_width,
                                           renpy.config.screen_height, st, at )
            render.blit( message_render, (0, 48) )

            # render the quit button if it's visible.
            if self.quit_button.visible:
                self.quit_button.draw( render, st, at )

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

# Minigame starts here.  Change this label to start and the start label in
# script.rpy to something else to test this out.
label mole_game:
    window hide None

    python:
        whack = WhackAMole()
        ui.add( whack )
        result = ui.interact( suppress_overlay=True, suppress_underlay=True )

    scene mole

    window show None
    return
