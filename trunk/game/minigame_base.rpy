# Below defines the main interface for a minigame.  Minigames are made by
# creating a class that inherits from the Minigame class and implementing.  To
# run the minigame, call the run_minigame() function and pass it in the name
# of the class that implements your minigame like so:
#
#    class MyCoolGame( Minigame ):
#        def __init__( self, *args, **kwds ):
#            super( MyCoolGame, self ).__init__()
#
#        def render( self, blitter ):
#            # ...put your rendering code here...
#
#        def update( self, delta_sec ):
#            # ...put your game logic here...
#
#     run_minigame( MyCoolGame )
#
# This will create a new instance of your minigame and run it until your game
# calls its quit() method.  Once the quit() method has been called, the
# minigame will shutdown, and control will return back to the rest of the
# Ren'Py game.
#
# To make implementing minigames easier and make up for some of Ren'Pys
# shortcomings, a number of utility classes and functions have been
# implemented in the minigame_utility module.  Also, a game entity/component
# framework has been (partially) implemented in the minigame_component module.
# The component classes located there can help make implementing game entities
# (e.g., players, enemies, items to pick up/shoot, etc) easier by providing
# components that can provide basic animation, collision detection, timing,
# etc. support.  Check them out, and note its a work in progress as new
# functionality is needed.

init -50 python:
    import pygame

    class MinigameDriver( renpy.Displayable ):
        def __init__( self, game, *args, **kwargs ):
            super( MinigameDriver, self ).__init__( *args, **kwargs )
            self.game_timer = None
            self.game       = game

        def visit( self ):
            return self.game.get_displayables()

        def render( self, width, height, shown_time, animation_time ):
            blitter   = renpy.Render( width, height )
            clip_rect = self.game.get_clip_rect()
            self.game.render( blitter, clip_rect )
            return blitter

        def event( self, e, mx, my, shown_time ):
            # on the first update, only create the game timer.
            if not self.game_timer:
                self.game_timer = GameTimer()
                self.game_timer.reset()
            else:
                # update the time and get the latest time delta.
                delta_sec = self.game_timer.tick()

                # handle input.
                if e.type == pygame.KEYDOWN:
                    self.game.on_key_down( e.key )
                elif e.type == pygame.KEYUP:
                    self.game.on_key_up( e.key )
                elif e.type == pygame.MOUSEMOTION:
                    self.game.on_mouse_move( mx, my )
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    self.game.on_mouse_down( mx, my, e.button )
                elif e.type == pygame.MOUSEBUTTONUP:
                    self.game.on_mouse_up( mx, my, e.button )

                # update the game.
                self.game.update( delta_sec )

                # check to see if we need to quit.
                if self.game.is_requesting_quit():
                    return self.get_game_result()

            # prod Ren'Py so that we continually draw and update the game.
            #
            # NOTE: previously timeout was set to 0 just like the redraw
            #       command, but apparently this causes MAJOR contention with
            #       renpy when the number of items to render and update on the
            #       screen at once.  like, so much that it causes renpy to
            #       never do any subsequent rendering.  to fix this, peg the
            #       logic update at 60 fps, and just draw as fast as possible.
            renpy.redraw( self, 0 )
            renpy.timeout( 1.0 / 60.0 )

        def get_game_result( self ):
            return self.game.get_result()

    class Minigame( object ):
        LEFT_MOUSE_BUTTON  = 1
        RIGHT_MOUSE_BUTTON = 2

        def __init__( self ):
            super( Minigame, self ).__init__()
            self.is_quitting = False
            self.origin      = (0, 0)
            self.width       = 0
            self.height      = 0
            self.high_score  = 0

        def get_displayables( self ):
            return []

        def get_clip_rect( self ):
            return (self.origin[0], self.origin[1],
                    self.width, self.height)

        def is_in_clip_rect( self, x, y ):
            clip_rect = self.get_clip_rect()
            return (clip_rect[0] <= x <= (clip_rect[0] + clip_rect[2]) and
                    clip_rect[1] <= y <= (clip_rect[1] + clip_rect[3]))

        def get_game_width( self ):
            return self.width

        def get_game_height( self ):
            return self.height

        def get_origin( self ):
            return self.origin

        def get_origin_x( self ):
            return self.origin[0]

        def get_origin_y( self ):
            return self.origin[1]

        def get_world_transform( self ):
            return GameTransform( self.origin[0], self.origin[1] )

        def set_game_width( self, width ):
            self.width = width

        def set_game_height( self, height ):
            self.height = height
            
        def set_high_score( self, score ):
            self.high_score = score

        def set_origin( self, x, y ):
            self.origin = (x, y )

        def transform_screen_to_world( self, x, y ):
            return (x - self.origin[0],
                    y - self.origin[1])

        def clear_screen( self, blitter, color=None ):
            color = color or Color( 0, 0, 0, 255 )
            blitter.canvas().rect( color,
                                   (self.origin[0], self.origin[1],
                                    self.width, self.height) )

        def render( self, blitter, clip_rect ):
            pass

        def update( self, delta_sec ):
            pass

        def quit( self ):
            self.is_quitting = True

        def is_requesting_quit( self ):
            return self.is_quitting

        def get_result( self ):
            return 0
            
        def get_high_score( self ):
            return "%20d" % self.high_score

        def on_key_down( self, key ):
            pass

        def on_key_up( self, key ):
            pass

        def on_mouse_move( self, mx, my ):
            pass

        def on_mouse_down( self, mx, my, button ):
            pass

        def on_mouse_up( self, mx, my, button ):
            pass

    def run_minigame( game_type,
                      x=0, y=0,
                      game_width=renpy.config.screen_width,
                      game_height=renpy.config.screen_height,
                      game_high_score=0,
                      *args, **kwds ):
        try:
            game   = game_type( *args, **kwds )
            driver = MinigameDriver( game )
            game.set_origin( x, y )
            game.set_game_width( game_width )
            game.set_game_height( game_height )
            game.set_high_score( game_high_score )
            ui.add( driver )
            ui.interact( suppress_underlay=True )
            return driver.get_game_result()
        except:
            # make sure no matter what happens we can always see our mouse.
            show_mouse()
            raise
