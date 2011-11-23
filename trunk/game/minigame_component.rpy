init -50 python:
    import copy

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

    class GameComponent( object ):
        def __init__( self, game_object=None ):
            super( GameComponent, self ).__init__()
            self.game_object = game_object

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
            scale  = self.game_object["transform"].scale
            width  = self.size.width * scale
            height = self.size.height * scale
            anchor = self.anchor

            if anchor.type:
                anchor = Anchor.create( anchor.type, Size( width, height ) )

            if self.is_flipped:
                left   = self.game_object["transform"].x + anchor.x - width + 1
                top    = self.game_object["transform"].y + anchor.y - height + 1
                right  = left + width - 1
                bottom = top + height - 1
            else:
                left   = self.game_object["transform"].x - anchor.x
                top    = self.game_object["transform"].y - anchor.y
                right  = left + width - 1
                bottom = top + height - 1

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

        def set_size( self, size ):
            self.size = size

    class GameRenderer( GameComponent ):
        DEFAULT_FRAMESET = "default"

        def __init__( self, default_frame=None, animations=None,
                      initial_animation=None ):
            super( GameRenderer, self ).__init__()
            self.current_frameset         = GameRenderer.DEFAULT_FRAMESET
            self.frames                   = { GameRenderer.DEFAULT_FRAMESET : default_frame }
            self.animator                 = GameAnimator()
            self.collider_color           = Color( 0, 255, 255, 100 )
            self.is_collider_visible      = False
            self.is_flipped               = False

            if animations:
                for name in animations:
                    self.animator.add_animation( name, animations[name] )
                if initial_animation:
                    self.animator.play_animation( initial_animation )

        def set_collider_visible( self, is_visible ):
            self.is_collider_visible = is_visible

        def set_collider_color( self, collider_color ):
            self.collider_color = collider_color

        def set_frame( self, frameset, frame ):
            self.frames[frameset] = frame

        def set_frameset( self, frameset ):
            if frameset not in self.frames:
                raise ValueError( "Invalid frameset %s.  Not a recognized "
                                  "frameset name." )
            self.current_frameset = frameset

        def set_animation_frameset( self, frameset ):
            self.animator.set_frameset( frameset )

        def flip( self ):
            self.is_flipped = not self.is_flipped

        def add_animation( self, name, animation ):
            self.animator.add_animation( name, animation )

        def stop_animation( self ):
            self.animator.stop_animation()

        def is_playing_animation( self ):
            return self.animator.get_current_frame() is not None

        def play_animation( self, name, loop_animation=True,
                            on_animation_end=None, frameset=None ):
            self.animator.play_animation( name, loop_animation,
                                          on_animation_end, frameset )

        def get_displayables( self ):
            displayables = []
            for frameset in self.frames:
                if self.frames[frameset]:
                    displayables.extend( self.frames[frameset].get_displayables() )
            displayables.extend( self.animator.get_displayables() )
            return displayables

        def update( self, delta_sec ):
            self.animator.update( delta_sec )

        def render( self, blitter, clip_rect, world_transform ):
            frame     = (self.animator.get_current_frame() or
                         self.frames[self.current_frameset])
            transform = self.game_object["transform"] + world_transform

            if frame:
                frame.render( blitter, clip_rect, transform, self.is_flipped )

            for child in self.game_object.children:
                for renderer in child.get_components( GameRenderer ):
                    renderer.render( blitter, clip_rect, transform )

            if self.is_collider_visible:
                self.render_collider( blitter, clip_rect, world_transform )

        def render_collider( self, blitter, clip_rect, world_transform ):
            collider = self.game_object["collider"]

            if isinstance( collider, GameBoxCollider ):
                bounds = collider.get_bounds()

                left   = bounds.left + world_transform.x
                right  = bounds.right + world_transform.x
                top    = bounds.top + world_transform.y
                bottom = bounds.bottom + world_transform.y

                if left > (clip_rect[0] + clip_rect[2]):
                    return
                if right < clip_rect[0]:
                    return
                if top > (clip_rect[1] + clip_rect[3]):
                    return
                if bottom < clip_rect[1]:
                    return

                left   = max( left, clip_rect[0] )
                right  = min( right, clip_rect[0] + clip_rect[2] )
                top    = max( top, clip_rect[1] )
                bottom = min( bottom, clip_rect[1] + clip_rect[3] )

                blitter.canvas().rect( self.collider_color,
                                       (left,
                                        top,
                                        right - left + 1,
                                        bottom - top + 1) )

    class GameTransform( GameComponent ):
        def __init__( self, x=0, y=0, scale=1.0 ):
            super( GameTransform, self ).__init__()
            self.x     = x
            self.y     = y
            self.scale = float( scale )

        def __add__( self, other ):
            return GameTransform( self.x + other.x,
                                  self.y + other.y,
                                  self.scale )

        def translate( self, dx, dy ):
            self.x += dx
            self.y += dy

        def set_scale( self, scale ):
            self.scale = scale

        def set_position( self, x, y ):
            self.x = x
            self.y = y

        def get_world_transform( self ):
            transform = self
            if self.game_object.parent:
                transform = transform + self.game_object.parent["transform"]
            return transform
