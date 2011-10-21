init python:
    import math
    import pygame

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

    class BoomBehavior( GameComponent ):
        def update( self, delta_sec ):
            if not self.game_object["renderer"].is_playing_animation():
                self.game_object.kill()

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
            small_bird["renderer"].set_collider_visible( True )
            small_bird["behavior"] = SmallBirdBehavior()
            PrefabFactory.add_prefab( "small_bird", small_bird )

            big_bird = GameObject( "big_bird" )
            big_bird["renderer"] = GameRenderer()
            big_bird["renderer"].add_animation( "flying", GameAnimation( [ GameImage( "gfx/duck_hunt/big_bird/big_bird-%d.png" % frame_index, Anchor.CENTER )
                                                                           for frame_index in xrange( 8 ) ], 8 ) )
            big_bird["collider"] = GameBoxCollider( Size( 90, 35 ), Anchor.CENTER )
            big_bird["renderer"].set_collider_visible( True )
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
            self.fire_zone["renderer"].set_collider_visible( True )

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

    class PlayerBehavior( GameObject ):
        def __init__( self ):
            super( PlayerBehavior, self ).__init__()
            self.score = 0

        def increment_score( self, points ):
            self.score += points

        def get_score( self ):
            return "{color=#000000}Score: %d{/color}" % self.score

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
