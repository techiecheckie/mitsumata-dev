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

    class GameRenderer( GameComponent ):
        DEFAULT_FRAMESET = "default"

        def __init__( self, default_frame=None, animations=None,
                      initial_animation=None ):
            super( GameRenderer, self ).__init__()
            self.current_frameset         = "default"
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

        def flip( self ):
            self.is_flipped = not self.is_flipped

        def add_animation( self, name, animation ):
            self.animator.add_animation( name, animation )

        def stop_animation( self ):
            self.animator.stop_animation()

        def is_playing_animation( self ):
            return self.animator.get_current_frame() is not None

        def play_animation( self, name, loop_animation=True,
                            on_animation_end=None ):
            self.animator.play_animation( name, loop_animation,
                                          on_animation_end )

        def get_displayables( self ):
            displayables = []
            for frameset in self.frames:
                if self.frames[frameset]:
                    displayables.extend( self.frames[frameset].get_displayables() )
            displayables.extend( self.animator.get_displayables() )
            return displayables

        def update( self, delta_sec ):
            self.animator.update( delta_sec )

        def render( self, blitter, world_transform ):
            frame     = (self.animator.get_current_frame() or
                         self.frames[self.current_frameset])
            transform = self.game_object["transform"] + world_transform

            if frame:
                frame.render( blitter, transform, self.is_flipped )

            for child in self.game_object.children:
                for renderer in child.get_components( GameRenderer ):
                    renderer.render( blitter, transform )

            if self.is_collider_visible:
                self.render_collider( blitter )

        def render_collider( self, blitter ):
            collider = self.game_object["collider"]

            if isinstance( collider, GameBoxCollider ):
                bounds = collider.get_bounds()
                blitter.canvas().rect( self.collider_color,
                                       (bounds.left, bounds.top,
                                        bounds.right - bounds.left + 1,
                                        bounds.bottom - bounds.top + 1) )

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
