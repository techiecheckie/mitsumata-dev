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

        def __init__( self, x, y, anchor_type=None ):
            self.x    = x
            self.y    = y
            self.type = anchor_type

        @staticmethod
        def create( anchor_type, size ):
            if anchor_type == Anchor.BOTTOM:
                return Anchor( size.width / 2, size.height, Anchor.BOTTOM )
            elif anchor_type == Anchor.BOTTOM_LEFT:
                return Anchor( 0, size.height, Anchor.BOTTOM_LEFT )
            elif anchor_type == Anchor.BOTTOM_RIGHT:
                return Anchor( size.width, size.height, Anchor.BOTTOM_RIGHT )
            elif anchor_type == Anchor.CENTER:
                return Anchor( size.width / 2, size.height / 2, Anchor.CENTER )
            elif anchor_type == Anchor.LEFT:
                return Anchor( 0, size.height / 2, Anchor.LEFT )
            elif anchor_type == Anchor.RIGHT:
                return Anchor( size.width, size.height / 2, Anchor.RIGHT )
            elif anchor_type == Anchor.TOP:
                return Anchor( size.width / 2, 0, Anchor.TOP )
            elif anchor_type == Anchor.TOP_LEFT:
                return Anchor( 0, 0, Anchor.TOP_LEFT )
            elif anchor_type == Anchor.TOP_RIGHT:
                return Anchor( size.width, 0, Anchor.TOP_RIGHT )

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

        def get_ceil_value( self ):
            return math.ceil( self.get_value() )

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
        DEFAULT_FRAMESET = "default"

        def __init__( self, default_frames=None, frame_rate=0, timing_info=None ):
            super( GameAnimation, self ).__init__()
            if default_frames:
                if isinstance( default_frames, collections.Sequence ):
                    default_frames = default_frames
                else:
                    default_frames = [ default_frames ]
            else:
                default_frames = []

            self.frames           = { GameAnimation.DEFAULT_FRAMESET : default_frames }
            self.current_frameset = GameAnimation.DEFAULT_FRAMESET
            self.current_frame    = 0
            self.elapsed_time     = 0
            self.loop_animation   = True
            self.on_animation_end = None
            self.frame_rate       = frame_rate

            if not timing_info and frame_rate:
                frame_duration = 1.0 / frame_rate
                self.timing_info = [ frame_duration ] * len( default_frames )
            else:
                self.timing_info = timing_info

        def get_displayables( self ):
            displayables = []
            for frameset in self.frames:
                for frame in self.frames[frameset]:
                    displayables.extend( frame.get_displayables() )
            return displayables

        def set_frames( self, frameset, frames ):
            self.frames[frameset] = frames
            if not self.timing_info and self.frame_rate:
                self.timing_info = [ 1.0 / self.frame_rate ] * len( frames )

        def set_frameset( self, frameset ):
            if frameset not in self.frames:
                raise ValueError( "Invalid frameset %s.  Not a recognized "
                                  "frameset name." % frameset )
            self.current_frameset = frameset

        def set_looping( self, loop_animation ):
            self.loop_animation = loop_animation

        def set_on_animation_end( self, on_animation_end ):
            self.on_animation_end = on_animation_end

        def reset( self ):
            self.elapsed_time  = 0
            self.current_frame = 0

        def update( self, delta_sec ):
            number_frames = len( self.frames[self.current_frameset] )

            if self.timing_info:
                self.elapsed_time += delta_sec
                while self.elapsed_time >= self.timing_info[self.current_frame]:
                    self.elapsed_time  -= self.timing_info[self.current_frame]
                    self.current_frame  = self.current_frame + 1
                    if self.current_frame >= number_frames:
                        self.current_frame = (self.current_frame % number_frames
                                              if self.loop_animation
                                              else number_frames - 1)
                        if self.on_animation_end:
                            self.on_animation_end()

        def get_current_frame( self ):
            frames = self.frames[self.current_frameset]
            return frames[self.current_frame]

    class GameAnimator( object ):
        def __init__( self ):
            super( GameAnimator, self ).__init__()
            self.animations            = {}
            self.current_animation     = None
            self.current_frameset      = GameAnimation.DEFAULT_FRAMESET
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
                            user_on_animation_end=None, frameset=None ):
            frameset                   = frameset or self.current_frameset
            self.user_on_animation_end = user_on_animation_end
            self.current_animation     = self.animations[name]
            self.current_animation.reset()
            self.current_animation.set_looping( loop_animation )
            self.current_animation.set_frameset( frameset )

        def stop_animation( self ):
            self.current_animation = None

        def set_frameset( self, frameset ):
            self.current_frameset = frameset
            if self.current_animation:
                self.current_animation.set_frameset( frameset )

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
            width  = self.size.width * transform.scale
            height = self.size.height * transform.scale
            anchor = self.anchor
            image  = im.Scale( self.image, width, height )

            if anchor.type:
                anchor = Anchor.create( anchor.type, Size( width, height ) )

            if is_flipped:
                image = im.Flip( image, horizontal=True )
                x     = transform.x + anchor.x - width + 1
                y     = transform.y + anchor.y - height + 1
            else:
                x = transform.x - anchor.x
                y = transform.y - anchor.y

            blitter.blit( get_blitter( image ), (x, y) )

    class GameRect( object ):
        def __init__( self, size, color, anchor=None ):
            super( GameRect, self ).__init__()
            self.size  = size
            self.color = color

            if isinstance( anchor, Anchor ):
                self.anchor = anchor
            else:
                self.anchor = Anchor.create( anchor or Anchor.TOP_LEFT, self.size )

        def get_displayables( self ):
            return []

        def render( self, blitter, transform, is_flipped=False ):
            bounds = self.get_bounds( transform )
            blitter.canvas().rect( self.color,
                                   (bounds.left,
                                    bounds.top,
                                    bounds.right - bounds.left + 1,
                                    bounds.bottom - bounds.top + 1) )

        def get_bounds( self, transform ):
            width  = self.size.width
            height = self.size.height
            anchor = self.anchor

            if anchor.type:
                anchor = Anchor.create( anchor.type, Size( width, height ) )

            left   = transform.x - anchor.x
            top    = transform.y - anchor.y
            right  = left + width - 1
            bottom = top + height - 1

            return Bounds( left, top, right, bottom )

    class GameText( object ):
        def __init__( self, text_callback, color=None ):
            super( GameText, self ).__init__()
            self.color         = color or Color( 0, 0, 0, 255 )
            self.text_callback = (text_callback
                                  if hasattr( text_callback, "__call__" )
                                  else lambda : str( text_callback ))

        def get_displayables( self ):
            return []

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

    class Randomizer( object ):
        def __init__( self, min_value, max_value ):
            self.min_value = min_value
            self.max_value = max_value

        def get_value( self ):
            return renpy.random.uniform( self.min_value, self.max_value )

        def get_integral_value( self ):
            return renpy.random.randint( self.min_value, self.max_value )

    class Size( object ):
        def __init__( self, width, height ):
            super( Size, self ).__init__()
            self.width  = width
            self.height = height

    class StagedValue( object ):
        def __init__( self, stages ):
            super( StagedValue, self ).__init__()
            self.stages       = stages
            self.elapsed_time = 0

        def update( self, delta_sec ):
            self.elapsed_time += delta_sec

        def get_value( self ):
            current_value = None

            for cutoff, value in self.stages:
                if self.elapsed_time >= cutoff:
                    current_value = value
                else:
                    break

            if not current_value:
                raise ValueError( "No staged value defined at time %s." %
                                  self.elapsed_time )
            return current_value

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

    # low tolerance picked for use in game object movements per frame.  this
    # is accurate enough for pixel locations.
    def almost_equal( a, b, tolerance=1e-2 ):
        if abs( a - b ) < tolerance:
            return True
        return abs( (a - b) / (b if abs(b) > abs(a) else a) ) <= tolerance

    def sign( number ):
        if number == 0:
            return 0
        return 1 if number > 0 else -1
