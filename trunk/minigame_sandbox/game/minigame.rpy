init python:
    import collections
    import time

    import pygame

    Anchor = collections.namedtuple( "Anchor", [ "x", "y" ] )
    Size   = collections.namedtuple( "Size", [ "width", "height" ] )

    Anchor.BOTTOM       = "BOTTOM"
    Anchor.BOTTOM_LEFT  = "BOTTOM_LEFT"
    Anchor.BOTTOM_RIGHT = "BOTTOM_RIGHT"
    Anchor.CENTER       = "CENTER"
    Anchor.LEFT         = "LEFT"
    Anchor.RIGHT        = "RIGHT"
    Anchor.TOP          = "TOP"
    Anchor.TOP_LEFT     = "TOP_LEFT"
    Anchor.TOP_RIGHT    = "TOP_RIGHT"

    def get_blitter( displayable ):
        return renpy.render( displayable, renpy.config.screen_width,
                             renpy.config.screen_height, 0, 0 )

    def get_image_size( image ):
        image_blitter = get_blitter( image )
        return Size( *image_blitter.get_size() )

    def apply_anchor( transform, anchor, size ):
        if anchor == Anchor.BOTTOM:
            return GameTransform( transform.x - size.width / 2,
                                  transform.y - size.height )
        elif anchor == Anchor.BOTTOM_LEFT:
            return GameTransform( transform.x,
                                  transform.y - size.height )
        elif anchor == Anchor.BOTTOM_RIGHT:
            return GameTransform( transform.x - size.width,
                                  transform.y - size.height )
        elif anchor == Anchor.CENTER:
            return GameTransform( transform.x - size.width / 2,
                                  transform.y - size.height / 2 )
        elif anchor == Anchor.LEFT:
            return GameTransform( transform.x,
                                  transform.y - size.height / 2 )
        elif anchor == Anchor.RIGHT:
            return GameTransform( transform.x - size.width,
                                  transform.y - size.height / 2 )
        elif anchor == Anchor.TOP:
            return GameTransform( transform.x - size.width / 2,
                                  transform.y )
        elif anchor == Anchor.TOP_LEFT:
            return GameTransform( transform.x,
                                  transform.y )
        elif anchor == Anchor.TOP_RIGHT:
            return GameTransform( transform.x - size.width,
                                  transform.y )
        else:
            return GameTransform( transform.x - anchor.x,
                                  transform.y - anchor.y )

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

    class MinigameDriver( renpy.Displayable ):
        def __init__( self, game, *args, **kwargs ):
            super( MinigameDriver, self ).__init__( *args, **kwargs )
            self.game_timer = None
            self.game       = game

        def visit( self ):
            return self.game.get_displayables()

        def render( self, width, height, shown_time, animation_time ):
            blitter = renpy.Render( width, height )
            self.game.render( blitter )
            return blitter

        def event( self, e, mx, my, shown_time ):
            # on the first update, only create the game timer.
            if not self.game_timer:
                self.game_timer = GameTimer()
                self.game_timer.reset()
                return

            # update the time and get the latest time delta.
            delta_sec = self.game_timer.tick()

            # handle input.
            if e.type == pygame.KEYDOWN:
                self.game.on_key_down( e.key )
            elif e.type == pygame.KEYUP:
                self.game.on_key_up( e.key )

            # update the game.
            self.game.update( delta_sec )

            # check to see if we need to quit.
            if self.game.is_requesting_quit():
                return self.get_game_result()

            # prod Ren'Py so that we continually draw and update the game.
            renpy.redraw( self, 0 )
            renpy.timeout( 0 )

        def get_game_result( self ):
            return self.game.get_result()

    class Minigame( object ):
        def __init__( self ):
            super( Minigame, self ).__init__()
            self.is_quitting = False

        def get_displayables( self ):
            return []

        def render( self, blitter ):
            pass

        def update( self, delta_sec ):
            pass

        def quit( self ):
            self.is_quitting = True

        def is_requesting_quit( self ):
            return self.is_quitting

        def get_result( self ):
            return 0

        def on_key_down( self, key ):
            pass

        def on_key_up( self, key ):
            pass

    class LogGame( Minigame ):
        def __init__( self ):
            super( LogGame, self ).__init__()

        def on_key_down( self, key ):
            renpy.log( "Key down: %s" % pygame.key.name( key ) )
            if key == pygame.K_ESCAPE:
                self.quit()

        def on_key_up( self, key ):
            renpy.log( "Key up: %s" % pygame.key.name( key ) )

    class GameComponent( object ):
        def __init__( self, game_object=None ):
            super( GameComponent, self ).__init__()
            self.game_object = game_object

    class GameFrame( object ):
        def __init__( self, image_filename, anchor=None ):
            super( GameFrame, self ).__init__()
            self.image  = Image( image_filename )
            self.size   = get_image_size( self.image )
            self.anchor = anchor or Anchor.TOP_LEFT

        def get_displayables( self ):
            return [ self.image ]

        def render( self, blitter, transform ):
            image_blitter = get_blitter( self.image )
            transform      = apply_anchor( transform, self.anchor, self.size )
            blitter.blit( image_blitter, (transform.x, transform.y) )

    class GameAnimation( object ):
        def __init__( self, frames, frame_rate=0 ):
            super( GameAnimation, self ).__init__()
            self.frames         = ( [ frames ]
                                    if not isinstance( frames, collections.Sequence )
                                    else (frames or []) )
            self.frame_duration = 1.0 / frame_rate if frame_rate > 0 else 0
            self.current_frame  = 0
            self.elapsed_time   = 0

        def get_displayables( self ):
            displayables = []
            for frame in self.frames:
                displayables.extend( frame.get_displayables() )
            return displayables

        def update( self, delta_sec ):
            if self.frame_duration > 0:
                self.elapsed_time += delta_sec
                while self.elapsed_time >= self.frame_duration:
                    self.elapsed_time  -= self.frame_duration
                    self.current_frame  = (self.current_frame + 1) % len( self.frames )

        def get_current_frame( self ):
            return self.frames[self.current_frame]

    class GameAnimator( object ):
        def __init__( self ):
            super( GameAnimator, self ).__init__()
            self.animations        = {}
            self.current_animation = None

        def get_displayables( self ):
            displayables = []
            for animation in self.animations.itervalues():
                displayables.extend( animation.get_displayables() )
            return displayables

        def add_animation( self, name, animation ):
            self.animations[name] = animation

        def set_animation( self, name ):
            self.current_animation = self.animations[name]

        def update( self, delta_sec ):
            if self.current_animation:
                self.current_animation.update( delta_sec )

        def get_current_frame( self ):
            if self.current_animation:
                return self.current_animation.get_current_frame()

    class GameRenderer( GameComponent ):
        def __init__( self, frame=None, animations=None, initial_animation=None ):
            super( GameRenderer, self ).__init__()
            self.frame    = frame
            self.animator = GameAnimator()

            if animations:
                for name in animations:
                    self.animator.add_animation( name, animations[name] )
                if initial_animation:
                    self.animator.set_animation( initial_animation )

        def get_displayables( self ):
            displayables = []
            if self.frame:
                displayables.extend( self.frame.get_displayables() )
            displayables.extend( self.animator.get_displayables() )
            return displayables

        def update( self, delta_sec ):
            self.animator.update( delta_sec )

        def render( self, blitter, world_transform ):
            frame     = self.animator.get_current_frame() or self.frame
            transform = self.game_object["transform"] + world_transform

            if frame:
                frame.render( blitter, transform )

            for child in self.game_object.children:
                for renderer in child.get_components( GameRenderer ):
                    renderer.render( blitter, transform )

    class GameTransform( GameComponent ):
        def __init__( self, x=0, y=0, angle=0 ):
            super( GameTransform, self ).__init__()
            self.x     = x
            self.y     = y
            self.angle = angle

        def __add__( self, other ):
            return GameTransform( self.x + other.x,
                                  self.y + other.y,
                                  self.angle + other.angle )

        def set_position( self, x, y ):
            self.x = x
            self.y = y

        def get_world_transform( self ):
            transform = self
            if self.game_object.parent:
                transform = transform + self.game_object.parent["transform"]
            return transform

    class GameObject( object ):
        def __init__( self ):
            super( GameObject, self ).__init__()
            self.components   = {}
            self.parent       = None
            self.children     = []
            self["transform"] = GameTransform()

        def __getitem__( self, key ):
            component = self.components.get( key )
            if component:
                return component
            raise KeyError( "Failed to get component %s.  Does not exist." )

        def __setitem__( self, key, value ):
            value.game_object    = self
            self.components[key] = value

        def get_components( self, component_type ):
            return [ component
                     for component in self.components.itervalues()
                     if isinstance( component, component_type ) ]

        def add_child( self, child ):
            child.parent = self
            self.children.append( child )

        def update( self, delta_sec ):
            for component in self.components.itervalues():
                if hasattr( component, "update" ):
                    component.update( delta_sec )

            for child in self.children:
                child.update( delta_sec )

    class DuckHunt( Minigame ):
        def __init__( self ):
            super( DuckHunt, self ).__init__()
            self.create_background()
            self.create_player()

        def create_background( self ):
            self.background             = GameObject()
            self.background["renderer"] = GameRenderer( GameFrame( "gfx/duck_hunt/background.png" ) )

        def create_player( self ):
            self.player             = GameObject()
            self.player["renderer"] = GameRenderer( GameFrame( "gfx/duck_hunt/player_body.png" ) )

            back_arm             = GameObject()
            back_arm["renderer"] = GameRenderer( GameFrame( "gfx/duck_hunt/player_back_arm.png", Anchor( 1, 5 ) ) )
            back_arm["transform"].set_position( 14, 46 )

            front_arm             = GameObject()
            front_arm["renderer"] = GameRenderer( GameFrame( "gfx/duck_hunt/player_front_arm.png", Anchor( 1, 1 ) ) )
            front_arm["transform"].set_position( 14, 46 )

            back_leg             = GameObject()
            back_leg["renderer"] = GameRenderer( GameFrame( "gfx/duck_hunt/player_back_leg_1.png", Anchor( 1, 1 ) ) )
            back_leg["transform"].set_position( 14, 74 )

            front_leg             = GameObject()
            front_leg["renderer"] = GameRenderer( GameFrame( "gfx/duck_hunt/player_front_leg_1.png", Anchor( 10, 0 ) ) )
            front_leg["transform"].set_position( 15, 73 )

            self.player.add_child( back_arm )
            self.player.add_child( front_arm )
            self.player.add_child( back_leg )
            self.player.add_child( front_leg )

            self.player["transform"].set_position( 330, 460 )

        def get_displayables( self ):
            displayables = []
            displayables.extend( self.background["renderer"].get_displayables() )
            displayables.extend( self.player["renderer"].get_displayables() )
            return displayables

        def render( self, blitter ):
            world_transform = GameTransform()
            self.background["renderer"].render( blitter, world_transform )
            self.player["renderer"].render( blitter, world_transform )

        def update( self, delta_sec ):
            self.player.update( delta_sec )

        def on_key_down( self, key ):
            if key == pygame.K_ESCAPE:
                self.quit()
