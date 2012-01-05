init python:
    import math
    import pygame

    GEAR_L_SIZE = Size(106,106)
    GEAR_M_SIZE = Size(85,86)
    GEAR_S_SIZE = Size(70,70)
    
    AXLE_WIDTH  = 22
    AXLE_HEIGHT = 22
    
    # The (starting point of) gear area on the right side of the screen.
    GEAR_AREA = (450, 60)
    GEAR_AREA_SPACING = (65, 65)
    
    # How far a released (mouse up) gear can be for it to snap to an axle.
    SNAP_DISTANCE = 35
    
    # (x, y, required gear size to complete, (optinal flag) locked)
    #
    # The order doesn't really matter here, but having them in a descending order
    # (top to bottom) makes it easier to find and adjust the correct coordinates
    LEVELS = [
        [ # level 1
         (282, 245, GEAR_L_SIZE),         
         (140, 392, GEAR_L_SIZE),

         (334, 137, GEAR_M_SIZE, "locked"),
         (162, 481, GEAR_M_SIZE, "locked"),
         (200, 284, GEAR_M_SIZE),         

         (262, 161, GEAR_S_SIZE),
         (216, 356, GEAR_S_SIZE)
        ],
        [ # level 2
         (322, 332, GEAR_L_SIZE),         
         (119, 361, GEAR_L_SIZE),

         (335, 140, GEAR_M_SIZE, "locked"),
         (162, 482, GEAR_M_SIZE, "locked"),
         (274, 198, GEAR_M_SIZE),
         (346, 242, GEAR_M_SIZE),         
         (200, 410, GEAR_M_SIZE),

         (250, 288, GEAR_S_SIZE),
         (192, 319, GEAR_S_SIZE),
         
         (128, 144, None),    
         (173, 215, None),     
         (106, 269, None),         
         (245, 351, None),  
         (365, 439, None),
         (277, 482, None)
        ],
        [ # level 3
         (164, 274, GEAR_L_SIZE, "locked"),         
         (349, 231, GEAR_L_SIZE),
         (145, 374, GEAR_L_SIZE),
         (250, 460, GEAR_L_SIZE),

         (335, 141, GEAR_M_SIZE, "locked"),
         (161, 484, GEAR_M_SIZE, "locked"),         
         (179, 151, GEAR_M_SIZE),
         (235, 352, GEAR_M_SIZE),         
         
         (122, 200, GEAR_S_SIZE),
         (234, 205, GEAR_S_SIZE),         
         (267, 263, GEAR_S_SIZE),
         (305, 381, GEAR_S_SIZE),
         (334, 440, GEAR_S_SIZE),

         (247, 146, None),         
         (101, 316, None),         
         (308, 326, None),         
         (203, 408, None),         
         (349, 514, None)
        ],
        [ # level 4
         (242, 309, GEAR_L_SIZE, "locked"),
         (122, 241, GEAR_L_SIZE),
         (142, 340, GEAR_L_SIZE),

         (335, 138, GEAR_M_SIZE, "locked"),
         (162, 485, GEAR_M_SIZE, "locked"),
         (171, 165, GEAR_M_SIZE),
         (357, 314, GEAR_M_SIZE),
         (332, 395, GEAR_M_SIZE),
         (233, 449, GEAR_M_SIZE),
         
         (355, 468, GEAR_S_SIZE, "locked"),
         (260, 131, GEAR_S_SIZE),
         (239, 195, GEAR_S_SIZE),
         (309, 255, GEAR_S_SIZE),
         (295, 494, GEAR_S_SIZE),

         (106, 142, None),
         (302, 198, None),
         (199, 221, None),
         (367, 250, None),         
         ( 85, 310, None),
         (274, 379, None),
         (179, 415, None)
        ],
        [ # level 5
         (280, 273, GEAR_L_SIZE),
         (182, 378, GEAR_L_SIZE),
         
         (335, 139, GEAR_M_SIZE, "locked"),
         (325, 352, GEAR_M_SIZE, "locked"),
         (163, 480, GEAR_M_SIZE, "locked"),
         (368, 219, GEAR_M_SIZE),
         (168, 277, GEAR_M_SIZE),
         
         (149, 206, GEAR_S_SIZE, "locked"),
         (188, 152, GEAR_S_SIZE),
         (236, 200, GEAR_S_SIZE),
         (377, 295, GEAR_S_SIZE),
         (111, 328, GEAR_S_SIZE),
         (111, 424, GEAR_S_SIZE),
         
         (236, 133, None),
         (118, 155, None),
         (300, 198, None),
         ( 99, 254, None),
         (220, 315, None),
         (233, 430, None),
         (332, 435, None),
         (268, 476, None),
         (356, 510, None)
        ]
    ]
    
    GEARS_GAME_STATE_BEGIN = "begin"
    GEARS_GAME_STATE_PLAY  = "play"
    GEARS_GAME_STATE_END   = "end"
    
    class Axle(GameObject):
      def __init__(self, x, y, required_size):
        super(Axle,self).__init__()
        
        self.x = x
        self.y = y
        self.gear = None
        self.required_size = required_size

      def get_position(self):
        return self.x, self.y
        
      def get_required_size(self):
        return self.required_size
        
      def get_gear(self):
        return self.gear
          
      def set_gear(self, gear):
        self.gear = gear
        
      def clear_gear(self):
        self.gear.set_axle(None)
        self.gear = None
        
        
    class Gear(GameObject):
      def __init__(self, x, y, size):
        super(Gear,self).__init__()
    
        self.x = x
        self.y = y
        self.size = size
        self.axle = None
        self.locked = False
        
      def get_id(self):
        return self.id

      def get_size(self):
        return self.size
        
      def set_position(self, position):
        self.x = position[0]
        self.y = position[1]
      
      def set_locked(self, locked):
        self.locked = locked
        
      def get_locked(self):
        return self.locked
        
      def get_axle(self):
        return self.axle
        
      def set_axle(self, axle):
        self.axle = axle
        self.axle.set_gear(self)
        
      def clear_axle(self):
        if self.axle != None:
          self.axle.set_gear(None)
          self.axle = None
        

    class Gears( Minigame ):                
        def __init__( self, level_number=1 ):
            super( Gears, self ).__init__()
            self.level_number = level_number
            self.create_game()

        def create_game(self):
            self.selected_gear = None
            self.axles = []
            self.gears = []
            
            level = LEVELS[self.level_number-1]
            
            self.state = GEARS_GAME_STATE_BEGIN

            #self.create_background()
            self.create_huds()            
            self.create_axles(level)
            self.create_gears(level)


        def create_background( self ):
            self.background = GameObject()
            self.background["renderer"] = GameRenderer(GameImage("gfx/gears/background.jpg"))
            
            
        def create_huds( self ):
            self.start_screen_hud             = GameObject()
            self.start_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/gears/start_screen.png" ) )
            self.start_screen_hud["transform"].set_position( 138, 50 )

            self.stop_screen_hud             = GameObject()
            self.stop_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/gears/stop_screen.png" ) )
            self.stop_screen_hud["transform"].set_position( 138, 50 )


        def create_axles(self, level):
            # (312,  96, GEAR_M_SIZE, "locked") | (237, 118, GEAR_S_SIZE),
            for data in level:
                x = data[0]
                y = data[1]
                size = data[2]
            
                axle = Axle(x, y, size)
                axle["renderer"] = GameRenderer(GameImage("gfx/gears/axle.png"))
                axle["transform"].set_position(x - AXLE_WIDTH/2, y - AXLE_HEIGHT/2)
                
                if len(data) == 4:
                    gear = Gear(0, 0, size)
                    
                    if size == GEAR_L_SIZE:
                        img = "gear_l"
                    elif size == GEAR_M_SIZE:
                        img = "gear_m"
                    else:
                        img = "gear_s"

                    axle.set_gear(gear)                    
                    gear.set_locked(True)
                    gear.set_axle(axle)
                    gear["transform"].set_position(x - size.width/2, y - size.height/2)
                    gear["renderer"] = GameRenderer(GameImage("gfx/gears/perma" + img + ".png"))
                    gear["collider"] = GameBoxCollider(size)
                    self.gears.append(gear)
                    
                self.axles.append(axle)

        
        def create_gears(self, level):
            # initial placement
            accum_x = 0
            accum_y = 0

            for data in level:
                if data[2] != None:
                
                  if len(data) == 3:              
                    if data[2] == GEAR_L_SIZE:
                        img = "gear_l"
                    elif data[2] == GEAR_M_SIZE:
                        img = "gear_m"
                    else:
                        img = "gear_s"
                    
                    x = GEAR_AREA[0] + accum_x
                    y = GEAR_AREA[1] + accum_y
                    
                    accum_y += data[2].height                    
                    if y > 500:
                        accum_x += 100
                        accum_y = 0
                        
                    gear = Gear(x, y, data[2])
                    gear["renderer"] = GameRenderer(GameImage("gfx/gears/" + img + ".png"))
                    gear["transform"].set_position(x, y)
                    gear["collider"] = GameBoxCollider(data[2])
                    self.gears.append(gear)
                    
                    
        def render( self, blitter, clip_rect ):
            world_transform = self.get_world_transform()

            #self.background["renderer"].render( blitter, clip_rect, world_transform )

            for axle in self.axles:
              axle["renderer"].render(blitter, clip_rect, world_transform)
            
            for gear in self.gears:
              gear["renderer"].render(blitter, clip_rect, world_transform)
            
            if self.state == GEARS_GAME_STATE_BEGIN:
              self.start_screen_hud["renderer"].render( blitter, clip_rect, world_transform )                
            elif self.state == GEARS_GAME_STATE_END:
              self.stop_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            
            
        def get_gear_at_position( self, x, y ):
            for gear in self.gears:
              if gear["collider"].is_point_inside( x, y ):
                return gear
            
            
        def on_key_down( self, key ):
            if key == pygame.K_ESCAPE:
              self.quit()


        def on_mouse_down( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
              if self.state == GEARS_GAME_STATE_BEGIN:
                self.state = GEARS_GAME_STATE_PLAY
              elif self.state == GEARS_GAME_STATE_PLAY:
                mx, my = self.transform_screen_to_world(mx,my)
                gear = self.get_gear_at_position(mx,my)
                if gear and not gear.get_locked():
                  self.selected_gear = gear
              elif self.state == GEARS_GAME_STATE_END:
                self.quit()
                

        def on_mouse_up( self, mx, my, button ):
            if self.state == GEARS_GAME_STATE_PLAY:
              if self.selected_gear != None:
                mx, my = self.transform_screen_to_world(mx,my)
                
                potential_axle = None
                
                # see if any of the axles are close enough for snapping
                for axle in self.axles:
                  ax, ay = axle.get_position()
                  dx, dy = mx-ax, my-ay
                  distance = math.sqrt(dx*dx + dy*dy)
                  
                  if distance < SNAP_DISTANCE:
                    potential_axle = axle
                    break
                 
                # check for overlapping axles and gears, and if none found,
                # insert the selected gear into the potential axle
                if potential_axle != None and potential_axle.get_gear() == None:
                  fits = True
                  
                  for axle in self.axles:
                    if axle != potential_axle:
                      bx, by = axle.get_position()
                      dx, dy = bx-ax, by-ay
                      
                      # ignore the axles that are way too far
                      if dx < 100 and dy < 100:
                        gear = axle.get_gear()
                        
                        if gear != None:
                          size = gear.get_size()
                          distance = math.sqrt(dx*dx + dy*dy)
                          distance -= size.width/2
                          distance -= self.selected_gear.get_size().width/2
                          
                          # allow a small overlap, but if it's too big, break the
                          # loop and don't even try placing the gear anywhere
                          if distance < -5:
                            fits = False
                            break
                  
                  if fits:
                    self.selected_gear.clear_axle()
                    self.selected_gear.set_axle(potential_axle)
                            
                    x = potential_axle.get_position()[0] - self.selected_gear.get_size().width/2
                    y = potential_axle.get_position()[1] - self.selected_gear.get_size().height/2
                            
                    self.selected_gear.set_position((x,y))
                    self.selected_gear["transform"].set_position(x, y)
                      
                    self.selected_gear = None
                    self.check_if_complete()
                    
                    return
                    
                # The gear didn't fit, so toss it back to the area on the right 
                # side of the screen
                if mx < GEAR_AREA[0] or mx > GEAR_AREA[0] + 200:
                  x = GEAR_AREA[0] + GEAR_L_SIZE.width/2
                else:
                  x = mx

                if my > 500 or my < 0:
                  y = GEAR_AREA[1]
                else:
                  y = my

                x -= self.selected_gear.get_size().width/2
                y -= self.selected_gear.get_size().height/2

                self.selected_gear.set_position((x, y))
                self.selected_gear["transform"].set_position(x, y)
                self.selected_gear.clear_axle()                
                self.selected_gear = None

            
        def on_mouse_move( self, mx, my ):
            if self.selected_gear:
                mx, my = self.transform_screen_to_world(mx,my)
                gear = self.selected_gear
                gear.clear_axle()
                gear["transform"].set_position(mx - gear.get_size().width/2, my - gear.get_size().height/2) 
            

        def check_if_complete(self):
            for gear in self.gears:
              axle = gear.get_axle()
              if axle == None or axle.get_required_size() != gear.get_size():
                return
                
            self.state = GEARS_GAME_STATE_END
            
        def get_result( self ):
            return self.level_number * 1000
