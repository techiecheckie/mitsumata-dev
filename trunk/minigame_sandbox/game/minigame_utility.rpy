init -50 python:
    import collections
    import copy
    import math
    import time

    Color  = collections.namedtuple( "Color", [ "red", "green", "blue", "alpha" ] )
    Bounds = collections.namedtuple( "Bounds", [ "left", "top", "right", "bottom" ] )

    class Anchor:
        BOTTOM       = "BOTTOM"
        BOTTOM_LEFT  = "BOTTOM_LEFT"
        BOTTOM_RIGHT = "BOTTOM_RIGHT"
        CENTER       = "CENTER"
        LEFT         = "LEFT"
        RIGHT        = "RIGHT"
        TOP          = "TOP"
        TOP_LEFT     = "TOP_LEFT"
        TOP_RIGHT    = "TOP_RIGHT"

        def __init__( self, x, y ):
            self.x = x
            self.y = y

        @staticmethod
        def create( anchor_type, size ):
            if anchor_type == Anchor.BOTTOM:
                return Anchor( size.width / 2, size.height )
            elif anchor_type == Anchor.BOTTOM_LEFT:
                return Anchor( 0, size.height )
            elif anchor_type == Anchor.BOTTOM_RIGHT:
                return Anchor( size.width, size.height )
            elif anchor_type == Anchor.CENTER:
                return Anchor( size.width / 2, size.height / 2 )
            elif anchor_type == Anchor.LEFT:
                return Anchor( 0, size.height / 2 )
            elif anchor_type == Anchor.RIGHT:
                return Anchor( size.width, size.height / 2 )
            elif anchor_type == Anchor.TOP:
                return Anchor( size.width / 2, 0 )
            elif anchor_type == Anchor.TOP_LEFT:
                return Anchor( 0, 0 )
            elif anchor_type == Anchor.TOP_RIGHT:
                return Anchor( size.width, 0 )

    class AutomatedInterpolator( object ):
        def __init__( self, min_value, max_value, duration ):
            super( AutomatedInterpolator, self ).__init__()
            self.min_value    = min_value
            self.max_value    = max_value
            self.duration     = float( duration )
            self.elapsed_time = float( 0 )

        def update( self, delta_sec ):
            self.elapsed_time += delta_sec

        def get_value( self ):
            alpha = self.elapsed_time / self.duration
            return self.min_value * (1 - alpha) + self.max_value * alpha

        def get_truncated_value( self ):
            return math.trunc( self.get_value() )

    class BoxOverlay( object ):
        def __init__( self, box, color ):
            self.box   = box
            self.color = color

        def render( self, blitter ):
            bounds = self.box.get_bounds()

            blitter.canvas().rect( self.color,
                                   (bounds.left, bounds.top,
                                    bounds.right - bounds.left + 1,
                                    bounds.bottom - bounds.top + 1) )

    class GameAnimation( object ):
        def __init__( self, frames, frame_rate=0 ):
            super( GameAnimation, self ).__init__()
            self.frames           = ( [ frames ]
                                      if not isinstance( frames, collections.Sequence )
                                      else (frames or []) )
            self.frame_duration   = 1.0 / frame_rate if frame_rate > 0 else 0
            self.current_frame    = 0
            self.elapsed_time     = 0
            self.loop_animation   = True
            self.on_animation_end = None

        def get_displayables( self ):
            displayables = []
            for frame in self.frames:
                displayables.extend( frame.get_displayables() )
            return displayables

        def set_looping( self, loop_animation ):
            self.loop_animation = loop_animation

        def set_on_animation_end( self, on_animation_end ):
            self.on_animation_end = on_animation_end

        def reset( self ):
            self.elapsed_time  = 0
            self.current_frame = 0

        def update( self, delta_sec ):
            if self.frame_duration > 0:
                self.elapsed_time += delta_sec
                while self.elapsed_time >= self.frame_duration:
                    self.elapsed_time  -= self.frame_duration
                    self.current_frame  = self.current_frame + 1
                    if self.current_frame >= len( self.frames ):
                        self.current_frame = (self.current_frame % len( self.frames )
                                              if self.loop_animation
                                              else len( self.frames ) - 1)
                        if self.on_animation_end:
                            self.on_animation_end()

        def get_current_frame( self ):
            return self.frames[self.current_frame]

    class GameAnimator( object ):
        def __init__( self ):
            super( GameAnimator, self ).__init__()
            self.animations            = {}
            self.current_animation     = None
            self.user_on_animation_end = None

        def get_displayables( self ):
            displayables = []
            for animation in self.animations.itervalues():
                displayables.extend( animation.get_displayables() )
            return displayables

        def add_animation( self, name, animation ):
            animation.set_on_animation_end( self.on_animation_end )
            self.animations[name] = animation

        def play_animation( self, name, loop_animation=True,
                            user_on_animation_end=None ):
            self.user_on_animation_end = user_on_animation_end
            self.current_animation     = self.animations[name]
            self.current_animation.reset()
            self.current_animation.set_looping( loop_animation )

        def stop_animation( self ):
            self.current_animation = None

        def on_animation_end( self ):
            if not self.current_animation.loop_animation:
                self.stop_animation()
            if self.user_on_animation_end:
                self.user_on_animation_end()

        def update( self, delta_sec ):
            if self.current_animation:
                self.current_animation.update( delta_sec )

        def get_current_frame( self ):
            if self.current_animation:
                return self.current_animation.get_current_frame()

    class GameImage( object ):
        def __init__( self, image_filename, anchor=None ):
            super( GameImage, self ).__init__()
            self.image  = Image( image_filename )
            self.size   = get_image_size( self.image )

            if isinstance( anchor, Anchor ):
                self.anchor = anchor
            else:
                self.anchor = Anchor.create( anchor or Anchor.TOP_LEFT, self.size )

        def __deepcopy__( self, memo ):
            copied        = copy.copy( self )
            copied.size   = copy.deepcopy( self.size, memo )
            copied.anchor = copy.deepcopy( self.anchor, memo )
            return copied

        def get_displayables( self ):
            return [ self.image ]

        def render( self, blitter, transform, is_flipped=False ):
            image = self.image

            if is_flipped:
                image = im.Flip( image, horizontal=True )
                x     = transform.x + self.anchor.x - self.size.width + 1
                y     = transform.y + self.anchor.y - self.size.height + 1
            else:
                x = transform.x - self.anchor.x
                y = transform.y - self.anchor.y

            blitter.blit( get_blitter( image ), (x, y) )

    class GameText( object ):
        def __init__( self, text_callback, color=None ):
            super( GameText, self ).__init__()
            self.color         = color or Color( 0, 0, 0, 255 )
            self.text_callback = (text_callback
                                  if hasattr( text_callback, "__call__" )
                                  else lambda : str( text_callback ))

        def render( self, blitter, transform, is_flipped=False ):
            text = Text( self.text_callback() )
            if is_flipped:
                text = im.Flip( text, horizontal=True )

            blitter.blit( get_blitter( text ),
                          (transform.x, transform.y) )

    class GameTimer( object ):
        def __init__( self ):
            super( GameTimer, self ).__init__()
            self.current_time = 0
            self.delta_time   = 0

        def tick( self ):
            previous_time = self.current_time
            self.current_time = time.time()
            self.delta_time   = self.current_time - previous_time
            return self.delta_time

        def reset( self ):
            self.current_time = time.time()

    class Size( object ):
        def __init__( self, width, height ):
            super( Size, self ).__init__()
            self.width  = width
            self.height = height

    def get_blitter( displayable ):
        return renpy.render( displayable, renpy.config.screen_width,
                             renpy.config.screen_height, 0, 0 )

    def get_image_size( image ):
        image_blitter = get_blitter( image )
        return Size( *image_blitter.get_size() )

    def hide_mouse():
        renpy.game.less_mouse = True

    def show_mouse():
        renpy.game.less_mouse = False

