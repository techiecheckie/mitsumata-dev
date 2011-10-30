init python:
    import collections
    import itertools
    import math
    import pygame
    
    GEAR_L_SIZE = Size(133,131)
    GEAR_M_SIZE = Size(106,105)
    GEAR_S_SIZE = Size(85,84)
    
    AXLE_WIDTH  = 23
    AXLE_HEIGHT = 24
    
    GEAR_AREA = (400, 40)
    GEAR_AREA_SPACING = (65, 65)
    
    SNAP_DISTANCE = 35
    
    LEVELS = [
        [
         (312,  96, GEAR_M_SIZE, "locked"),
         (237, 118, GEAR_S_SIZE),
         (257, 202, GEAR_L_SIZE),
         (170, 249, GEAR_M_SIZE),
         (190, 318, GEAR_S_SIZE),
         (105, 345, GEAR_L_SIZE),
         (131, 436, GEAR_M_SIZE, "locked")          
        ],
        [
         ( 90,  99, None),
         (306,  95, GEAR_M_SIZE, "locked"),
         (236, 154, GEAR_M_SIZE),
         (139, 175, None),
         (317, 198, GEAR_M_SIZE),
         ( 67, 231, None),
         (215, 249, GEAR_S_SIZE),
         (157, 283, GEAR_S_SIZE),
         (295, 296, GEAR_L_SIZE),
         (212, 316, None),
         ( 80, 328, GEAR_L_SIZE),
         (169, 378, GEAR_M_SIZE),
         (338, 408, None),
         (126, 453, GEAR_M_SIZE, "locked"),
         (248, 457, None)
        ],
        [
         (145, 100, GEAR_M_SIZE),
         (213, 102, None),
         (305,  98, GEAR_M_SIZE, "locked"),
         ( 82, 158, GEAR_S_SIZE),
         (204, 165, GEAR_S_SIZE),
         (323, 198, GEAR_L_SIZE),
         (235, 224, GEAR_S_SIZE),
         (126, 236, GEAR_L_SIZE, "locked"),
         ( 60, 282, None),
         (278, 291, None),
         (202, 320, GEAR_M_SIZE),
         (101, 346, GEAR_L_SIZE),
         (276, 349, GEAR_S_SIZE),
         (168, 378, None),
         (308, 407, GEAR_S_SIZE),
         (222, 432, GEAR_L_SIZE),
         (123, 457, GEAR_M_SIZE, "locked"),
         (317, 489, None)
        ],
        [
         (215, 277, GEAR_L_SIZE, "locked"),
         ( 91, 214, GEAR_L_SIZE),
         (110, 323, GEAR_L_SIZE),

         (311, 101, GEAR_M_SIZE, "locked"),
         (133, 449, GEAR_M_SIZE, "locked"),
         (141, 129, GEAR_M_SIZE),
         (338, 281, GEAR_M_SIZE),
         (315, 366, GEAR_M_SIZE),
         (211, 407, GEAR_M_SIZE),
         
         (334, 439, GEAR_S_SIZE, "locked"),
         (232,  94, GEAR_S_SIZE),
         (215, 157, GEAR_S_SIZE),
         (289, 219, GEAR_S_SIZE),
         (269, 461, GEAR_S_SIZE),

         ( 70, 105, None),
         (278, 164, None),
         (170, 187, None),
         (347, 220, None),
         (170, 187, None),
         ( 51, 278, None),
         (249, 349, None),
         (147, 387, None)
        ],
        [
         (246, 236, GEAR_L_SIZE),
         (148, 345, GEAR_L_SIZE),
         
         (306,  98, GEAR_M_SIZE, "locked"),
         (302, 324, GEAR_M_SIZE, "locked"),
         (126, 451, GEAR_M_SIZE, "locked"),
         (337, 181, GEAR_M_SIZE),
         (132, 239, GEAR_M_SIZE),
         
         (111, 166, GEAR_S_SIZE, "locked"),
         (153, 111, GEAR_S_SIZE),
         (202, 160, GEAR_S_SIZE),
         (350, 260, GEAR_S_SIZE),
         ( 72, 293, GEAR_S_SIZE),
         ( 72, 391, GEAR_S_SIZE),
         
         (201,  90, None),
         ( 80, 114, None),
         (268, 157, None),
         (201,  90, None),
         ( 60, 217, None),
         (186, 281, None),
         (199, 400, None),
         (300, 405, None),
         (235, 447, None),
         (327, 483, None)
        ]
    ]
    
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
            
            self.selected_gear = None
            self.axles = []
            self.gears = []
            
            level = LEVELS[level_number-1]

            self.create_background()            
            self.create_axles(level)
            self.create_gears(level)


        def create_background( self ):
            self.background = GameObject()
            self.background["renderer"] = GameRenderer(GameImage("gfx/gears/background.jpg"))


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
                    #gear.set_locked(True)
                    gear.set_axle(axle)
                    gear["transform"].set_position(x - size.width/2, y - size.height/2)
                    gear["renderer"] = GameRenderer(GameImage("gfx/gears/" + img + "_.png"))
                    gear["collider"] = GameBoxCollider(size)
                    self.gears.append(gear)
                    
                self.axles.append(axle)

        
        
        def create_gears(self, level):
            # "grid" placement
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
                    if y > 400:
                        accum_x += 100
                        accum_y = 0
                        
                    gear = Gear(x, y, data[2])
                    gear["renderer"] = GameRenderer(GameImage("gfx/gears/" + img + ".png"))
                    gear["transform"].set_position(x, y)
                    gear["collider"] = GameBoxCollider(data[2], Anchor.CENTER)
                    self.gears.append(gear)
                    
                    
        def render( self, blitter ):
            world_transform = self.get_world_transform()
            self.background["renderer"].render( blitter, world_transform )
            
            for axle in self.axles:
                axle["renderer"].render(blitter, world_transform)
            
            for gear in self.gears:
                gear["renderer"].render(blitter, world_transform)
            
            
        def get_gear_at_position( self, x, y ):
            for gear in self.gears:
                if gear["collider"].is_point_inside( x, y ):
                    return gear
            
            
        def on_key_down( self, key ):
            if key == pygame.K_ESCAPE:
                self.quit()


        def on_mouse_down( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                mx, my = self.transform_screen_to_world(mx,my)
                gear = self.get_gear_at_position(mx,my)
                if gear and not gear.get_locked():
                    self.selected_gear = gear


        def on_mouse_up( self, mx, my, button ):
            if self.selected_gear:
                gear = self.selected_gear
                mx, my = self.transform_screen_to_world(mx,my)
                
                for axle in self.axles:
                  ax, ay = axle.get_position()
                  dx, dy = mx-ax, my-ay
                  distance = math.sqrt(dx*dx + dy*dy)
                  if distance < SNAP_DISTANCE and axle.get_gear() == None:
                    enough_space = True
                    
                    # Check if any of the nearby axles have gears that could overlap
                    for another_axle in self.axles:
                      if another_axle != axle:
                        bx, by = another_axle.get_position()
                        dx, dy = bx-ax, by-ay
                        if dx < 100 and dy < 100:
                          another_gear = another_axle.get_gear()
                          if another_gear:
                            size = another_gear.get_size()
                            distance = math.sqrt(dx*dx + dy*dy)
                            
                            distance -= (0.75*size.width)/2
                            distance -= (0.75*self.selected_gear.get_size().width)/2
                            
                            if distance < 0:
                              enough_space = False
                              break                   

                    if not enough_space:
                      break
                    else:
                      self.selected_gear.clear_axle()
                      self.selected_gear.set_axle(axle)
                      
                      x = axle.get_position()[0] - self.selected_gear.get_size().width/2
                      y = axle.get_position()[1] - self.selected_gear.get_size().height/2
                      
                      self.selected_gear.set_position((x,y))
                      self.selected_gear["transform"].set_position(x, y)
                      
                      self.selected_gear = None
                      self.check_if_complete()
                      
                      return
                      
                # Toss the gear back to the grid area (though now they just stack there)
                self.selected_gear.clear_axle()
                self.selected_gear.set_position((400, 40))
                self.selected_gear["transform"].set_position(400, 40)
                self.selected_gear = None
                
                return
            
        def on_mouse_move( self, mx, my ):
            if self.selected_gear:
                mx, my = self.transform_screen_to_world(mx,my)
                gear = self.selected_gear
                gear["transform"].set_position(mx - gear.get_size().width/2, my - gear.get_size().height/2) 
            
        def check_if_complete(self):
            for gear in self.gears:
              axle = gear.get_axle()
              if axle == None or axle.get_required_size() != gear.get_size():
                return
                    
            print "You won!"

