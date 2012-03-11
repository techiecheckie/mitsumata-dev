init python:
    class PlatformerLevel( object ):
        def __init__( self, time_limit, distance, obstacle_density ):
            self.time_limit       = time_limit
            self.distance         = distance
            self.obstacle_density = obstacle_density
            
    PLATFORMER_LEVELS = [
      # Level 1
      PlatformerLevel( time_limit       = 60,
                       distance         = 3000, 
                       obstacle_density = 50), # density: 0-100
      # Level 2
      PlatformerLevel( time_limit       = 60,
                       distance         = 4000, 
                       obstacle_density = 60),
      # Level 3
      PlatformerLevel( time_limit       = 60,
                       distance         = 4500, 
                       obstacle_density = 75),
      # Level 4
      PlatformerLevel( time_limit       = 60,
                       distance         = 5000, 
                       obstacle_density = 90)
    ]
    
    MAP_SEGMENTS = [
      [
        [ 3, 4, 3, 4, 3, 5, 3, 6, 8, 9, 2, 4, 3, 4, 3, 4, 3, 6, 8, 9, 2, 6, 8, 9, 2, 4, 3, 4, 3, 4, 3],
        [10,18,19,18,19,18,20,19,18,20,10,11,12,11,12,11,20,19,18,20,10,11,12,11,10,19,18,10,11,10,11],
        [21, 0, 0, 0, 0, 0, 0, 0, 0, 0,17,20,19,18,20,21, 0, 0, 0, 0,17,20,19,20,21, 0, 0,17,18,19,20]
      ]
    ]
    
    TILE_TYPES = [
      "grass-edge-1.png",  # 1
      "grass-edge-2.png",  # 2
      "grass-1.png",       # 3
      "grass-2.png",       # 4
      "grass-3.png",       # 5
      "grass-edge-3.png",  # 6
      "grass-edge-4.png",  # 7
      "water-1.png",       # 8
      "water-2.png",       # 9
      "dirt-1.png",        # 10
      "dirt-2.png",        # 11
      "dirt-3.png",        # 12
      "dirt-edge-1.png",   # 13
      "dirt-edge-2.png",   # 14
      "dirt-edge-3.png",   # 15
      "dirt-edge-4.png",   # 16
      "dirt-bottom-1.png", # 17
      "dirt-bottom-2.png", # 18
      "dirt-bottom-3.png", # 19
      "dirt-bottom-4.png", # 20
      "dirt-bottom-5.png", # 21
    ]
    
    OBSTACLE_TYPES = [
      "plant_1.png",
      "plant_2.png",
      "plant_3.png",
      "plant_4.png",
      "plant_5.png",
      "rock_1.png",
      "rock_2.png",
      "rock_3.png",
      "rock_4.png",
      "rock_5.png",
      "tree_1.png",
      "tree_2.png",
      "tree_3.png",
      "tree_4.png",
      "tree_5.png"
    ]
    
    # those that can be walked on
    WALKABLE_TILES  = [2,3,4,5,6]
    # those that can have an obstacle (no edge tiles or anything like that here)
    OBSTACLE_TILES  = [3,4,5]
    # those that can make you drown
    DROWNABLE_TILES = [8,9]
    
    RUN_SPEED      = 110
    JUMP_SPEED     = 150
    JUMP_DELAY     = 0.2
    MAX_FALL_SPEED = 200
    GRAVITY        = 200
    
    #### DESIGNERS: DO NOT CHANGE ANYTHING BEYOND THIS LINE ####

    # different states the game can be in.
    PLATFORMER_GAME_STATE_BEGIN     = "platf_begin"
    PLATFORMER_GAME_STATE_COUNTDOWN = "platf_countdown"
    PLATFORMER_GAME_STATE_PLAY      = "platf_play"
    PLATFORMER_GAME_STATE_END       = "platf_end"
    
    # runner states.
    RUNNER_STATE_RUNNING    = "running"
    RUNNER_STATE_JUMPING    = "jumping"
    RUNNER_STATE_ASCENDING  = "ascending"
    RUNNER_STATE_HOVERING   = "hovering"
    RUNNER_STATE_DESCENDING = "descending"
    RUNNER_STATE_LANDING    = "landing"
    RUNNER_STATE_DROWNING   = "drowning"
    RUNNER_STATE_FALLING    = "falling"
    
    # animation names.
    RUNNER_ANIMATION_RUN     = "run"
    RUNNER_ANIMATION_JUMP    = "jump"
    RUNNER_ANIMATION_ASCEND  = "ascend"
    RUNNER_ANIMATION_HOVER   = "hover"
    RUNNER_ANIMATION_DESCEND = "descend"
    RUNNER_ANIMATION_LAND    = "land"
    RUNNER_ANIMATION_DROWN   = "drown"
    RUNNER_ANIMATION_FALL    = "fall"

    # animation durations.  these divided into the number of frames that are
    # in the corresponding animation are the frames per second value passed to
    # the GameAnimation constructor.
    RUN_ANIMATION_DURATION     = 1.0
    JUMP_ANIMATION_DURATION    = 0.2
    ASCEND_ANIMATION_DURATION  = 0.5
    HOVER_ANIMATION_DURATION   = 0.5
    DESCEND_ANIMATION_DURATION = 0.5
    LAND_ANIMATION_DURATION    = 0.4
    DROWN_ANIMATION_DURATION   = 1.0
    FALL_ANIMATION_DURATION    = 1.5

    # number of animation frames.
    NUMBER_RUN_FRAMES     = 6
    NUMBER_JUMP_FRAMES    = 2
    NUMBER_ASCEND_FRAMES  = 2
    NUMBER_HOVER_FRAMES   = 1
    NUMBER_DESCEND_FRAMES = 2
    NUMBER_LAND_FRAMES    = 2
    NUMBER_DROWN_FRAMES   = 3
    NUMBER_FALL_FRAMES    = 7

    VIEW_WIDTH = 12
    VIEW_HEIGHT = 3

    # From the top of the minigame area
    GROUND_LEVEL = 415
   
    TILE_WIDTH  = 64
    TILE_HEIGHT = 64
    TILE_SIZE = Size( TILE_WIDTH, TILE_HEIGHT )
    
    # runner initial cell position
    CELL_X = 2
    CELL_Y = len(MAP_SEGMENTS[0])-3

    # Lacking a better name, this controls how far the next tile "protrudes" 
    # into the previous one (the one the player currently is in). Increasing
    # this number affects how soon the player bumps into objects or falls off 
    # cliffs.
    BUMPER = 5
    
    class Cell( GameObject ):
      def __init__( self, x, y ):
        super( Cell, self ).__init__()
        self.x = x
        self.y = y
        
        self.tile     = None
        self.obstacle = None

        self.walkable  = False
        self.drownable = False
        self.cleared   = False
    
    class Platformer( Minigame ):
        def __init__( self, level_number=1 ):
            super( Platformer, self ).__init__()
            
            self.level_number = level_number
            
            # setup the entities.
            self.start_screen_hud   = None
            self.stop_screen_hud    = None
            self.score_hud          = None
            self.time_remaining_hud = None
            
            self.map    = None
            self.tiles  = None
            self.runner = None
            
            if self.level_number > len( PLATFORMER_LEVELS ) or self.level_number <= 0:
                raise ValueError( "Invalid platformer level number %d.  Level "
                                  "number must be between 1 and %d." %
                                  (self.level_number, len( PLATFORMER_LEVELS )) )

            self.level = PLATFORMER_LEVELS[self.level_number - 1]

            self.time_remaining = AutomatedInterpolator( self.level.time_limit,
                                                         0,
                                                         self.level.time_limit )
            
            self.create_tiles()
            self.create_obstacles()
            self.create_runner()
            self.create_huds()
            self.create_map()
            self.create_backgrounds()
            
            self.start_game()
        
        def start_game( self ):
            self.state = PLATFORMER_GAME_STATE_BEGIN
            self.runner["behavior"].run()
            
        def create_huds( self ):
            self.start_screen_hud             = GameObject()
            self.start_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/platformer/start_screen.png" ) )
            self.start_screen_hud["transform"].set_position( 148, 50 )

            self.stop_screen_hud             = GameObject()
            self.stop_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/platformer/stop_screen.png" ) )
            self.stop_screen_hud["transform"].set_position( 148, 50 )

            distance_run             = GameObject()
            distance_run["renderer"] = GameRenderer( GameText( self.get_distance_run, Color( 255, 255, 255, 255 ) ) )
            distance_run["transform"].set_position( 120, 148 )
            self.stop_screen_hud.add_child( distance_run )
            
            distance_to_pass = GameObject()
            distance_to_pass["renderer"] = GameRenderer( GameText( self.get_distance, Color( 255, 255, 255, 255 ) ) )
            distance_to_pass["transform"].set_position( 120, 196 )
            self.stop_screen_hud.add_child( distance_to_pass )

            distance_left             = GameObject()
            distance_left["renderer"] = GameRenderer( GameText( self.get_distance, Color( 255, 255, 255, 255 ) ) )
            distance_left["transform"].set_position( 120, 323 )
            self.start_screen_hud.add_child( distance_left )
            
            time_left = GameObject()
            time_left["renderer"] = GameRenderer( GameText( self.get_time, Color( 255, 255, 255, 255 ) ) )
            time_left["transform"].set_position( 120, 353 )
            self.start_screen_hud.add_child( time_left )
            
            self.distance_left_hud             = GameObject()
            self.distance_left_hud["renderer"] = GameRenderer( GameText( self.get_distance_left, Color( 255, 255, 255, 255 ) ) )
            self.distance_left_hud["transform"].set_position( 400, 30 )

            self.time_remaining_hud             = GameObject()
            self.time_remaining_hud["renderer"] = GameRenderer( GameText( self.get_time_remaining, Color( 255, 255, 255, 255 ) ) )
            self.time_remaining_hud["transform"].set_position( 50, 30 )

            self.top_border = GameObject()
            self.top_border["renderer"] = GameRenderer( GameImage( "gfx/backgrounds/minigame_bg_top_border.png" ) )
            self.top_border["transform"].set_position( 0, 0 )
            
        def create_background( self ):
            self.background = GameObject()
            self.background["renderer"] = GameRenderer( GameImage( "gfx/platformer/background.jpg" ) )

        def create_tiles( self ):                
            self.tiles = []
                
            for tile_type in TILE_TYPES:
              tile = GameObject()
              tile["renderer"] = GameRenderer( GameImage( "gfx/platformer/tiles/" + tile_type ) )
              tile["transform"].set_scale( 0.5 )
              self.tiles.append( tile )
              
        def create_obstacles( self ):
            self.obstacles = []
            
            for obstacle_type in OBSTACLE_TYPES:
              obstacle = GameObject()
              obstacle["renderer"] = GameRenderer( GameImage( "gfx/platformer/obstacles/" + obstacle_type, Anchor.TOP_LEFT ) )
              obstacle["transform"].set_scale( 1.0 )
              self.obstacles.append( obstacle )

        def create_runner( self ): 
            runner = GameObject()
            runner["renderer"] = GameRenderer()
            runner["renderer"].add_animation( RUNNER_ANIMATION_RUN,
                                              GameAnimation( [ GameImage( "gfx/platformer/runner/riku_run-%d.png" % frame_index, Anchor.BOTTOM )
                                                               for frame_index in xrange( NUMBER_RUN_FRAMES ) ],
                                                             NUMBER_RUN_FRAMES / RUN_ANIMATION_DURATION ) )
            runner["renderer"].add_animation( RUNNER_ANIMATION_JUMP,
                                              GameAnimation( [ GameImage( "gfx/platformer/runner/riku_jump_start-%d.png" % frame_index, Anchor.BOTTOM )
                                                               for frame_index in xrange( NUMBER_JUMP_FRAMES ) ],
                                                             NUMBER_JUMP_FRAMES / JUMP_ANIMATION_DURATION ) )
            runner["renderer"].add_animation( RUNNER_ANIMATION_ASCEND,
                                              GameAnimation( [ GameImage( "gfx/platformer/runner/riku_jump_ascend-%d.png" % frame_index, Anchor.BOTTOM )
                                                               for frame_index in xrange( NUMBER_ASCEND_FRAMES ) ],
                                                             NUMBER_ASCEND_FRAMES / ASCEND_ANIMATION_DURATION ) )
            runner["renderer"].add_animation( RUNNER_ANIMATION_HOVER,
                                              GameAnimation( [ GameImage( "gfx/platformer/runner/riku_jump_hover-%d.png" % frame_index, Anchor.BOTTOM )
                                                               for frame_index in xrange( NUMBER_HOVER_FRAMES ) ],
                                                             NUMBER_HOVER_FRAMES / HOVER_ANIMATION_DURATION ) )
            runner["renderer"].add_animation( RUNNER_ANIMATION_DESCEND,
                                              GameAnimation( [ GameImage( "gfx/platformer/runner/riku_jump_descend-%d.png" % frame_index, Anchor.BOTTOM )
                                                               for frame_index in xrange( NUMBER_DESCEND_FRAMES ) ],
                                                             NUMBER_DESCEND_FRAMES / DESCEND_ANIMATION_DURATION ) )
            runner["renderer"].add_animation( RUNNER_ANIMATION_LAND,
                                              GameAnimation( [ GameImage( "gfx/platformer/runner/riku_jump_land-%d.png" % frame_index, Anchor.BOTTOM )
                                                               for frame_index in xrange( NUMBER_LAND_FRAMES ) ],
                                                             NUMBER_LAND_FRAMES / LAND_ANIMATION_DURATION ) )
            runner["renderer"].add_animation( RUNNER_ANIMATION_DROWN,
                                              GameAnimation( [ GameImage( "gfx/platformer/runner/riku_drown-%d.png" % frame_index, Anchor.BOTTOM )
                                                               for frame_index in xrange( NUMBER_DROWN_FRAMES ) ],
                                                             NUMBER_DROWN_FRAMES / DROWN_ANIMATION_DURATION ) )
            runner["renderer"].add_animation( RUNNER_ANIMATION_FALL,
                                              GameAnimation( [ GameImage( "gfx/platformer/runner/riku_fall-%d.png" % frame_index, Anchor.BOTTOM )
                                                               for frame_index in xrange( NUMBER_FALL_FRAMES ) ],
                                                             NUMBER_FALL_FRAMES / FALL_ANIMATION_DURATION ) )
            runner["transform"].set_scale( 1.0 )
            runner["behavior"] = RunnerBehavior( self )

            self.runner = runner
            
        def create_map( self ):
            self.map = []            
            segments = []
            
            # Calculate how many map segments are needed to cover the run distance
            map_length = 0
            while map_length < self.level.distance:
              index = random.randint(0,len(MAP_SEGMENTS)-1)
              segments.append(MAP_SEGMENTS[index])
              map_length += len(MAP_SEGMENTS[index][0]) * TILE_WIDTH

            # Fill the map array with cells
            for k in range(0, len(segments)):
              segment = segments[k]
              for y in range(0, len(segment)):
                if y >= len(self.map):
                  self.map.append([])
                for x in range(0, len(segment[y])):
                  tile_type = segment[y][x]
                
                  tile      = None
                  obstacle  = None
                  walkable  = False
                  drownable = False
                  if tile_type > 0:
                    tile = self.tiles[ tile_type - 1 ]
                    if tile_type in WALKABLE_TILES:
                      walkable = True
                    if tile_type in DROWNABLE_TILES:
                      drownable = True

                  if tile_type in OBSTACLE_TILES and x > 3:
                    if random.randint( 0, 100 ) <= self.level.obstacle_density:
                      # Because the obstacles are big and long, make sure there 
                      # are no obstacles in two consecutive tiles.                      
                      if (self.map[y][len(self.map[y])-1].obstacle == None and
                          self.map[y][len(self.map[y])-2].obstacle == None):
                        # Also, because the new obstacles are bigger than the 
                        # original ones, leave the tile next to an edge tile 
                        # empty too to make sure there's enough jumping space.
                          if x < len(segment[y])-1 and segment[y][x+1] != 6:
                            obstacle = self.obstacles[ random.randint( 0, len(OBSTACLE_TYPES)-1 ) ]
                            print x, len(segment[y])
                
                  cell = Cell( x*TILE_WIDTH + k*len(segment[0])*TILE_WIDTH, GROUND_LEVEL + y*TILE_HEIGHT )
                  cell.tile      = tile
                  cell.obstacle  = obstacle
                  cell.walkable  = walkable
                  cell.drownable = drownable
                
                  self.map[y].append( cell )
                  
            row = self.map[0]

        def create_backgrounds( self ):
            self.backgrounds = []

            mountains = GameObject()
            mountains["renderer"] = GameRenderer( GameImage( "gfx/platformer/backgrounds/6-bg.png" ) )
            mountains["transform"].set_position( 0, 0 )
            mountains["behavior"] = BackgroundBehavior( self.runner, 1, True )
            self.backgrounds.append( mountains )

            low_clouds = GameObject()
            low_clouds["renderer"] = GameRenderer( GameImage( "gfx/platformer/backgrounds/5-clouds.png" ) )
            low_clouds["transform"].set_position( 0, 0 )
            low_clouds["behavior"] = BackgroundBehavior( self.runner, 5, False )
            self.backgrounds.append( low_clouds )

            high_clouds = GameObject()
            high_clouds["renderer"] = GameRenderer( GameImage( "gfx/platformer/backgrounds/4-clouds.png" ) )
            high_clouds["transform"].set_position( 0, 0 )
            high_clouds["behavior"] = BackgroundBehavior( self.runner, 15, False )
            self.backgrounds.append( high_clouds )

            hills = GameObject()
            hills["renderer"] = GameRenderer( GameImage( "gfx/platformer/backgrounds/3-hills.png" ) )
            hills["transform"].set_position( 0, 0 )
            hills["behavior"] = BackgroundBehavior( self.runner, 6, True )
            self.backgrounds.append( hills )

            forest = GameObject()
            forest["renderer"] = GameRenderer( GameImage( "gfx/platformer/backgrounds/2-trees.png" ) )
            forest["transform"].set_position( 0, 0 )
            forest["behavior"] = BackgroundBehavior( self.runner, 10, True )
            self.backgrounds.append( forest )

            foreground = GameObject()
            foreground["renderer"] = GameRenderer( GameImage( "gfx/platformer/backgrounds/1-foreground.png" ) )
            foreground["transform"].set_position( 0, 0 )
            foreground["behavior"] = BackgroundBehavior( self.runner, 20, True )
            self.backgrounds.append( foreground )

        def get_time_remaining( self ):
            return "Time remaining: %d" % self.time_remaining.get_ceil_value()

        def get_distance_left( self ):
            return "Distance left: %d" % ( self.level.distance - self.runner["behavior"].distance )
                
        def get_distance( self ):
            return "%20d" % self.level.distance
            
        def get_time( self ):
            return "%20d" % self.level.time_limit
                
        def get_distance_run( self ):
            return "%20d" % self.runner["behavior"].distance
            
        def get_result( self ):
            return int(self.runner["behavior"].distance)

        def render( self, blitter, clip_rect ):
            world_transform = self.get_world_transform()
            #self.background["renderer"].render( blitter, clip_rect, world_transform )

            for layer in self.backgrounds:
              layer["renderer"].render( blitter, clip_rect, world_transform )
            
            cell_x = self.runner["behavior"].cell_x-3
            
            for y in range(0, VIEW_HEIGHT):
              for x in range(cell_x, cell_x + VIEW_WIDTH + 1):
                # Dirty +1 increase added to have the new, bigger obstacles drawn
                # off screen.
                  
                cell = self.map[y][x]
                if cell.tile != None:
                  cell.tile["transform"].x = cell.x - self.runner["behavior"].distance
                  cell.tile["transform"].y = cell.y - TILE_HEIGHT/2
                  cell.tile["renderer"].render( blitter, clip_rect, world_transform )
                
                cell = self.map[y][x-1]
                if cell.obstacle != None:
                  cell.obstacle["transform"].x = cell.x - self.runner["behavior"].distance
                  cell.obstacle["transform"].y = cell.y - TILE_HEIGHT
                  cell.obstacle["renderer"].render( blitter, clip_rect, world_transform )

            if self.state == PLATFORMER_GAME_STATE_BEGIN:
                self.start_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == PLATFORMER_GAME_STATE_PLAY:
                self.time_remaining_hud["renderer"].render( blitter, clip_rect, world_transform )
                self.distance_left_hud["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == PLATFORMER_GAME_STATE_END:
                self.stop_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == PLATFORMER_GAME_STATE_PAUSE:
                self.stop_screen_hud["renderer"].render( blitter, clip_rect, world_transform )

            self.runner["renderer"].render( blitter, clip_rect, world_transform )

            self.top_border["renderer"].render( blitter, clip_rect, world_transform )

        def update( self, delta_sec ):
            if self.state == PLATFORMER_GAME_STATE_PLAY:
              self.time_remaining.update( delta_sec )
  
              self.runner.update( delta_sec )

              for layer in self.backgrounds:
                layer.update( delta_sec )
              
              if self.time_remaining.get_value() <= 0 \
                  or self.runner["behavior"].dead \
                  or self.runner["behavior"].distance >= self.level.distance:
                self.state = PLATFORMER_GAME_STATE_END
                

        def on_key_down( self, key ):
            if key == pygame.K_ESCAPE:
                self.quit()
        
            if self.state == PLATFORMER_GAME_STATE_PLAY:
              if key == pygame.K_SPACE:
                self.runner["behavior"].jump()

        def on_mouse_up( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
              if self.state == PLATFORMER_GAME_STATE_BEGIN:
                self.state = PLATFORMER_GAME_STATE_PLAY
              elif self.state == PLATFORMER_GAME_STATE_END:
                self.quit()

    class RunnerBehavior( GameComponent ):
        def __init__( self, platformer ):
            super( RunnerBehavior, self ).__init__()
            self.platformer = platformer
            
        def run( self ):
            self.game_object["transform"].set_position( CELL_X * TILE_WIDTH, GROUND_LEVEL + CELL_Y * TILE_HEIGHT )
            self.cell_x = CELL_X
            self.cell_y = CELL_Y
            self.cell = self.platformer.map[CELL_Y][CELL_X]
            
            self.x_velocity = RUN_SPEED
            self.y_velocity = 0
            self.y_offset   = 0
            
            self.distance     = 0
            self.sub_distance = 0
            
            self.delay_counter = 0
            
            self.jump_requested = False
            self.dead = False
        
            self.state = RUNNER_STATE_RUNNING
            self.game_object["renderer"].play_animation( RUNNER_ANIMATION_RUN )
            
        def jump( self ):
            if self.state == RUNNER_STATE_RUNNING or self.state == RUNNER_STATE_LANDING:
              self.jump_requested = True
        
        def update( self, delta_sec ):
            distance = self.x_velocity * delta_sec
            self.sub_distance += distance
            self.distance     += distance
            
            update_cell = False
            
            # Running to the next tile yet?
            if self.sub_distance + BUMPER >= TILE_WIDTH:
              self.sub_distance -= TILE_WIDTH
              self.cell_x += 1
              update_cell = True
            
            self.y_offset += self.y_velocity * delta_sec
            
            # Vertical stuff was used in the old version where it was possible
            # to move verticaly too rather than running straight all the time.
            # Now it merely checks if you've fallen down and there's water in
            # the current tile. Most likely all of the stuff below could (should)
            # be rewritten/simplified now that there's no need for any vertical
            # tile changing anymore. --> TODO?
            if self.y_offset >= TILE_HEIGHT:
              self.y_offset = 0
              self.cell_y += 1
              update_cell = True
            elif self.y_offset <= -TILE_HEIGHT:
              self.y_offset = 0
              self.cell_y -= 1
              update_cell = True
            
            self.game_object["transform"].y += self.y_velocity * delta_sec
            
            if update_cell and self.cell_y < VIEW_HEIGHT:
              self.cell = self.platformer.map[self.cell_y][self.cell_x]
                
            # state checks follow
                
            if self.state == RUNNER_STATE_RUNNING:
              if self.cell.tile == None or not self.cell.walkable:
                self.state = RUNNER_STATE_DESCENDING
                self.game_object["renderer"].play_animation( RUNNER_ANIMATION_DESCEND )
              else:
                if self.cell.obstacle != None and not self.cell.cleared:
                  self.state = RUNNER_STATE_FALLING
                  self.game_object["renderer"].play_animation( RUNNER_ANIMATION_FALL )
                  self.cell.cleared = True
                  self.x_velocity = 0
                elif self.jump_requested:
                  self.delay_counter += delta_sec
                  if self.delay_counter >= JUMP_DELAY:
                    self.state = RUNNER_STATE_JUMPING
                    self.game_object["renderer"].play_animation( RUNNER_ANIMATION_JUMP )
                    self.x_velocity = 0
                    self.delay_counter = 0
                    self.jump_requested = False
                
            elif self.state == RUNNER_STATE_JUMPING:
              self.delay_counter += delta_sec
              if self.delay_counter >= JUMP_ANIMATION_DURATION:
                self.state = RUNNER_STATE_ASCENDING
                self.game_object["renderer"].play_animation( RUNNER_ANIMATION_ASCEND )
                self.x_velocity = RUN_SPEED
                self.y_velocity = -JUMP_SPEED
                
            elif self.state == RUNNER_STATE_ASCENDING:
              self.y_velocity += GRAVITY * delta_sec
              # show hover animation when climbing slowly enough
              if self.y_velocity > -50:
                self.state = RUNNER_STATE_HOVERING
                self.game_object["renderer"].play_animation( RUNNER_ANIMATION_HOVER )
                
            elif self.state == RUNNER_STATE_HOVERING:
              self.y_velocity += GRAVITY * delta_sec
              # show descending animation when falling fast enough (if hovering)
              if self.y_velocity > 50:
                self.state = RUNNER_STATE_DESCENDING
                self.game_object["renderer"].play_animation( RUNNER_ANIMATION_DESCEND )
                
            elif self.state == RUNNER_STATE_DESCENDING:
              # TODO: clean this mess
              
              # free fall
              #if self.cell.tile == None:
              if self.y_velocity < MAX_FALL_SPEED:
                self.y_velocity += GRAVITY * delta_sec
              
              # more free fall
              if not self.cell.walkable:
                # drown if the tile is water and the player has fallen down enough
                if self.cell.drownable and self.y_offset >= TILE_HEIGHT/4:
                  self.state = RUNNER_STATE_DROWNING
                  self.game_object["renderer"].play_animation( RUNNER_ANIMATION_DROWN )
                  self.x_velocity = 0
                  self.y_velocity = 0
                
                else:
                  if self.y_velocity < MAX_FALL_SPEED:
                    self.y_velocity += GRAVITY * delta_sec
              else:
                # 
                if self.y_offset >= 0:
                  self.state = RUNNER_STATE_LANDING
                  self.game_object["renderer"].play_animation( RUNNER_ANIMATION_LAND )
                  self.game_object["transform"].y = GROUND_LEVEL + self.cell_y*TILE_HEIGHT
                  self.x_velocity = 0
                  self.y_velocity = 0
                  
              # the runner has fallen off the screen
              if self.cell_y > VIEW_HEIGHT:
                self.dead = True
              
            elif self.state == RUNNER_STATE_LANDING:
              self.delay_counter += delta_sec
              if self.delay_counter >= LAND_ANIMATION_DURATION:
                self.state = RUNNER_STATE_RUNNING
                self.game_object["renderer"].play_animation( RUNNER_ANIMATION_RUN )
                self.x_velocity = RUN_SPEED
                self.delay_counter = 0
                
            elif self.state == RUNNER_STATE_DROWNING:
              self.delay_counter += delta_sec
              if self.delay_counter > 3:
                self.dead = True
                self.delay_counter = 0
                
            elif self.state == RUNNER_STATE_FALLING:
              self.delay_counter += delta_sec
              if self.delay_counter >= FALL_ANIMATION_DURATION:
                self.state = RUNNER_STATE_RUNNING
                self.game_object["renderer"].play_animation( RUNNER_ANIMATION_RUN )
                self.x_velocity = RUN_SPEED                
                self.delay_counter = 0

    class BackgroundBehavior( GameComponent ):
        def __init__( self, runner, pps, follow_runner ):
            super( BackgroundBehavior, self ).__init__()
            self.runner = runner
            self.pps = pps
            self.follow_runner = follow_runner

        def update( self, delta_sec ):
            if self.follow_runner:
              if self.runner["behavior"].x_velocity > 0:
                self.game_object["transform"].x -= self.pps * delta_sec
            else:
              self.game_object["transform"].x -= self.pps * delta_sec
