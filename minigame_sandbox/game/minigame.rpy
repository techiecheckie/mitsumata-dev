init python:
    import collections
    import copy
    import math
    import time

    import pygame

    def run_minigame( game_type, *args, **kwds ):
        try:
            driver = MinigameDriver( game_type( *args, **kwds ) )
            ui.add( driver )
            ui.interact( suppress_overlay=True, suppress_underlay=True )
        except:
            # make sure no matter what happens we can always see our mouse.
            show_mouse()
            raise

    def hide_mouse():
        renpy.game.less_mouse = True

    def show_mouse():
        renpy.game.less_mouse = False

    Size = collections.namedtuple( "Size", [ "width", "height" ] )
    Color = collections.namedtuple( "Color", [ "red", "green", "blue", "alpha" ] )
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
        LEFT_MOUSE_BUTTON  = 1
        RIGHT_MOUSE_BUTTON = 2

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

        def on_mouse_move( self, mx, my ):
            pass

        def on_mouse_down( self, mx, my, button ):
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

    class GameAnimation( object ):
        def __init__( self, frames, frame_rate=0 ):
            super( GameAnimation, self ).__init__()
            self.frames         = ( [ frames ]
                                    if not isinstance( frames, collections.Sequence )
                                    else (frames or []) )
            self.frame_duration = 1.0 / frame_rate if frame_rate > 0 else 0
            self.current_frame  = 0
            self.elapsed_time   = 0
            self.loop_animation = True

        def get_displayables( self ):
            displayables = []
            for frame in self.frames:
                displayables.extend( frame.get_displayables() )
            return displayables

        def set_looping( self, loop_animation ):
            self.loop_animation = loop_animation

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
                        self.current_frame = self.current_frame % len( self.frames )
                        if not self.loop_animation:
                            # return that we're done animating.
                            return True

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

        def play_animation( self, name, loop_animation=True ):
            self.current_animation = self.animations[name]
            self.current_animation.reset()
            self.current_animation.set_looping( loop_animation )

        def stop_animation( self ):
            self.current_animation = None

        def update( self, delta_sec ):
            if self.current_animation:
                if self.current_animation.update( delta_sec ):
                    self.current_animation = None

        def get_current_frame( self ):
            if self.current_animation:
                return self.current_animation.get_current_frame()

    class GameRenderer( GameComponent ):
        def __init__( self, frame=None, animations=None, initial_animation=None ):
            super( GameRenderer, self ).__init__()
            self.frame              = frame
            self.animator           = GameAnimator()
            self.bounds_overlay     = None
            self.is_overlay_visible = False
            self.is_flipped         = False

            if animations:
                for name in animations:
                    self.animator.add_animation( name, animations[name] )
                if initial_animation:
                    self.animator.play_animation( initial_animation )

        def flip( self ):
            self.is_flipped = not self.is_flipped

        def set_bounds_overlay( self, overlay ):
            self.bounds_overlay = overlay

        def add_animation( self, name, animation ):
            self.animator.add_animation( name, animation )

        def stop_animation( self ):
            self.animator.stop_animation()

        def is_playing_animation( self ):
            return self.animator.get_current_frame() is not None

        def play_animation( self, name, loop_animation=True ):
            self.animator.play_animation( name, loop_animation )

        def set_overlay_visible( self, is_overlay_visible ):
            self.is_overlay_visible = is_overlay_visible

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
                frame.render( blitter, transform, self.is_flipped )

            for child in self.game_object.children:
                for renderer in child.get_components( GameRenderer ):
                    renderer.render( blitter, transform )

            if self.bounds_overlay and self.is_overlay_visible:
                self.bounds_overlay.render( blitter )

    class GameBoxCollider( GameComponent ):
        def __init__( self, size, anchor=None ):
            super( GameBoxCollider, self ).__init__()
            self.size       = size
            self.is_flipped = False

            if isinstance( anchor, Anchor ):
                self.anchor = anchor
            else:
                self.anchor = Anchor.create( anchor or Anchor.TOP_LEFT, self.size )

        def is_point_inside( self, x, y ):
            left, top, right, bottom = self.get_bounds()
            return left <= x <= right and top <= y <= bottom

        def get_bounds( self ):
            if self.is_flipped:
                left   = self.game_object["transform"].x + self.anchor.x - self.size.width + 1
                top    = self.game_object["transform"].y + self.anchor.y - self.size.height + 1
                right  = left + self.size.width - 1
                bottom = top + self.size.height - 1
            else:
                left   = self.game_object["transform"].x - self.anchor.x
                top    = self.game_object["transform"].y - self.anchor.y
                right  = left + self.size.width - 1
                bottom = top + self.size.height - 1

            return Bounds( left, top, right, bottom )

        def flip( self ):
            self.is_flipped = not self.is_flipped

        def is_box_overlapping( self, box ):
            my_bounds    = self.get_bounds()
            their_bounds = box.get_bounds()
            # two rects DON'T overlap if:
            #
            #     my_bounds.left > their_bounds.right OR
            #     my_bounds.right < their_bounds.left OR
            #     my_bounds.top > their_bounds.bottom OR
            #     my_bounds.bottom < their_bounds.top
            #
            # so, negating that will get us a condition for testing if they
            # do overlap, which is:
            return (my_bounds.left <= their_bounds.right and
                    my_bounds.right >= their_bounds.left and
                    my_bounds.top <= their_bounds.bottom and
                    my_bounds.bottom >= their_bounds.top)

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

        def translate( self, dx, dy ):
            self.x += dx
            self.y += dy

        def set_position( self, x, y ):
            self.x = x
            self.y = y

        def get_world_transform( self ):
            transform = self
            if self.game_object.parent:
                transform = transform + self.game_object.parent["transform"]
            return transform

    class GameObject( object ):
        STATE_ALIVE = "alive"
        STATE_DEAD  = "dead"

        def __init__( self, name=None ):
            super( GameObject, self ).__init__()
            self.name         = name
            self.components   = {}
            self.parent       = None
            self.children     = []
            self.state        = GameObject.STATE_ALIVE
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

        def get_child( self, name ):
            for child in self.children:
                if child.name == name:
                    return child

        def update( self, delta_sec ):
            for component in self.components.itervalues():
                if hasattr( component, "update" ):
                    component.update( delta_sec )

            for child in self.children:
                child.update( delta_sec )

        def kill( self ):
            self.state = GameObject.STATE_DEAD

        def is_alive( self ):
            return self.state == GameObject.STATE_ALIVE

    class PrefabFactory( object ):
        prefabs = {}

        @staticmethod
        def add_prefab( name, prefab ):
            PrefabFactory.prefabs[name] = prefab

        @staticmethod
        def instantiate( name, transform=None ):
            instance = copy.deepcopy( PrefabFactory.prefabs[name] )
            if transform:
                instance["transform"] = transform
            return instance

    class BoomBehavior( GameComponent ):
        def update( self, delta_sec ):
            if not self.game_object["renderer"].is_playing_animation():
                self.game_object.kill()

    class SmallBirdBehavior( GameComponent ):
        def __init__( self ):
            super( SmallBirdBehavior, self ).__init__()
            self.velocity = 220

        def update( self, delta_sec ):
            self.game_object["transform"].x += (delta_sec * self.velocity)

        def flip( self ):
            self.velocity *= -1

        def shoot( self ):
            self.game_object.kill()
            return True

        def get_value( self ):
            return 10

    class BigBirdBehavior( GameComponent ):
        def __init__( self ):
            super( BigBirdBehavior, self ).__init__()
            self.velocity   = 170
            self.hit_points = 2

        def update( self, delta_sec ):
            self.game_object["transform"].x += (delta_sec * self.velocity)

        def flip( self ):
            self.velocity *= -1

        def shoot( self ):
            renpy.log( "HP: %d" % self.hit_points )
            self.hit_points -= 1
            return self.hit_points == 0

        def get_value( self ):
            return 20

    class PlayerBehavior( GameObject ):
        def __init__( self ):
            super( PlayerBehavior, self ).__init__()
            self.score = 0

        def increment_score( self, points ):
            self.score += points

        def get_score( self ):
            return "{color=#000000}Score: %d{/color}" % self.score

    class DuckHunt( Minigame ):
        FIRE_ZONE_HEIGHT_FRACTION = 3.0 / 5.0

        def __init__( self ):
            super( DuckHunt, self ).__init__()
            hide_mouse()

            self.background = None
            self.player     = None
            self.fire_zone  = None
            self.booms      = []
            self.birds      = []
            self.huds       = []

            self.bird_countdown = 1

            self.create_background()
            self.create_player()
            self.create_birds()
            self.create_boom()
            self.create_colliders()
            self.create_cursor()
            self.create_hud()

        def quit( self ):
            super( DuckHunt, self ).quit()
            show_mouse()

        def create_background( self ):
            self.background             = GameObject()
            self.background["renderer"] = GameRenderer( GameImage( "gfx/duck_hunt/background.png" ) )

        def create_player( self ):
            self.player             = GameObject( "player" )
            self.player["renderer"] = GameRenderer( GameImage( "gfx/duck_hunt/gun.png", Anchor.BOTTOM ) )
            self.player["transform"].set_position( renpy.config.screen_width / 2,
                                                   renpy.config.screen_height )
            self.player["behavior"] = PlayerBehavior()

        def create_birds( self ):
            small_bird = GameObject( "small_bird" )
            small_bird["renderer"] = GameRenderer()
            small_bird["renderer"].add_animation( "flying", GameAnimation( [ GameImage( "gfx/duck_hunt/small_bird/small_bird-%d.png" % frame_index, Anchor.CENTER )
                                                                             for frame_index in xrange( 4 ) ], 8 ) )
            small_bird["collider"] = GameBoxCollider( Size( 50, 30 ), Anchor.CENTER )
            small_bird["renderer"].set_bounds_overlay( BoxOverlay( small_bird["collider"], Color( 0, 255, 0, 100 ) ) )
            small_bird["renderer"].set_overlay_visible( False )
            small_bird["behavior"] = SmallBirdBehavior()
            PrefabFactory.add_prefab( "small_bird", small_bird )

            big_bird = GameObject( "big_bird" )
            big_bird["renderer"] = GameRenderer()
            big_bird["renderer"].add_animation( "flying", GameAnimation( [ GameImage( "gfx/duck_hunt/big_bird/big_bird-%d.png" % frame_index, Anchor.CENTER )
                                                                           for frame_index in xrange( 8 ) ], 8 ) )
            big_bird["collider"] = GameBoxCollider( Size( 90, 35 ), Anchor.CENTER )
            big_bird["renderer"].set_bounds_overlay( BoxOverlay( big_bird["collider"], Color( 0, 255, 0, 100 ) ) )
            big_bird["renderer"].set_overlay_visible( False )
            big_bird["behavior"] = BigBirdBehavior()
            PrefabFactory.add_prefab( "big_bird", big_bird )

        def create_cursor( self ):
            self.cursor = GameObject( "cursor" )
            self.cursor["renderer"] = GameRenderer( GameImage( "gfx/duck_hunt/cursor.png", Anchor.CENTER ) )

        def create_colliders( self ):
            self.fire_zone             = GameObject( "fire_zone" )
            zone_size                  = Size( renpy.config.screen_width,
                                               renpy.config.screen_height *
                                               DuckHunt.FIRE_ZONE_HEIGHT_FRACTION - 50 )
            self.fire_zone["renderer"] = GameRenderer()
            self.fire_zone["collider"] = GameBoxCollider( zone_size )
            self.fire_zone["transform"].set_position( 0, 50 )
            self.fire_zone["renderer"].set_bounds_overlay( BoxOverlay( self.fire_zone["collider"], Color( 255, 0, 0, 100 ) ) )
            self.fire_zone["renderer"].set_overlay_visible( False )

        def create_boom( self ):
            boom = GameObject( "boom" )
            boom["renderer"] = GameRenderer()
            boom["renderer"].add_animation( "fire", GameAnimation( [ GameImage( "gfx/duck_hunt/boom/boom-%d.png" % frame_index, Anchor.CENTER )
                                                                     for frame_index in xrange( 18 ) ], 25 ) )
            boom["behavior"] = BoomBehavior()
            PrefabFactory.add_prefab( "boom", boom )

        def create_hud( self ):
            score_hud = GameObject( "score_hud" )
            score_hud["renderer"] = GameRenderer( GameText( self.player["behavior"].get_score ) )
            score_hud["transform"].set_position( 10, 10 )

            self.huds.append( score_hud )

        def get_displayables( self ):
            displayables = []
            displayables.extend( self.background["renderer"].get_displayables() )
            displayables.extend( self.player["renderer"].get_displayables() )

            for bird in self.birds:
                displayables.extend( bird["renderer"].get_displayables() )

            for boom in self.booms:
                displayables.extend( boom["renderer"].get_displayables() )

            displayables.extend( self.cursor["renderer"].get_displayables() )
            return displayables

        def render( self, blitter ):
            world_transform = GameTransform()
            self.background["renderer"].render( blitter, world_transform )
            self.player["renderer"].render( blitter, world_transform )

            for bird in self.birds:
                bird["renderer"].render( blitter, world_transform )

            for boom in self.booms:
                boom["renderer"].render( blitter, world_transform )

            self.fire_zone["renderer"].render( blitter, world_transform )

            self.cursor["renderer"].render( blitter, world_transform )

            for hud in self.huds:
                hud["renderer"].render( blitter, world_transform )

        def update( self, delta_sec ):
            # see if it's time to add a bird.
            self.bird_countdown -= delta_sec
            if self.bird_countdown <= 0:
                if len( self.birds ) < 5:
                    bird_type = renpy.random.choice( [ "small_bird", "big_bird" ] )
                    direction = renpy.random.choice( [ "RTL", "LTR" ] )
                    bird      = PrefabFactory.instantiate( bird_type )
                    bird["renderer"].play_animation( "flying" )

                    bounds              = self.fire_zone["collider"].get_bounds()
                    bird["transform"].x = 0
                    bird["transform"].y = math.floor( renpy.random.uniform( bounds.top + bird["collider"].size.height,
                                                                            bounds.bottom - bird["collider"].size.height ) )
                    if direction == "RTL":
                        bird["transform"].x = renpy.config.screen_width
                        bird["renderer"].flip()
                        bird["collider"].flip()
                        bird["behavior"].flip()

                    self.birds.append( bird )
                self.bird_countdown = renpy.random.uniform( 0.8, 1.2 )

            # prune out the dead gun shots and update those that are still alive.
            self.booms[:] = [ boom for boom in self.booms if boom.is_alive() ]
            for boom in self.booms:
                boom.update( delta_sec )

            # prune out the dead birds and update those that are still alive.
            self.birds[:] = [ bird for bird in self.birds if bird.is_alive() ]
            for bird in self.birds:
                bird.update( delta_sec )
                if not self.fire_zone["collider"].is_box_overlapping( bird["collider"] ):
                    renpy.log( "Kill bird (%s)" % delta_sec )
                    bird.kill()

        def on_key_down( self, key ):
            if key == pygame.K_ESCAPE:
                self.quit()

        def on_mouse_move( self, mx, my ):
            # for whatever reason, Ren'Py sometimes gives (-1,-1) for the mouse
            # position when moving the cursor quickly outside the window.  to
            # avoid sudden movements, simply ignore mouse move events if we get
            # this coordinate.
            if mx != -1 and my != -1:
                self.player["transform"].x = mx
                self.cursor["transform"].set_position( mx, my )

        def on_mouse_down( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.fire_zone["collider"].is_point_inside( mx, my ):
                    boom = PrefabFactory.instantiate( "boom", GameTransform( mx, my ) )
                    boom["renderer"].play_animation( "fire", False )
                    self.booms.append( boom )

                    for bird in self.birds:
                        if (bird["collider"].is_point_inside( mx, my ) and
                            bird["behavior"].shoot()):
                            bird.kill()
                            self.player["behavior"].increment_score( bird["behavior"].get_value() )
