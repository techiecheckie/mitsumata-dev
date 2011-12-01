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
                       obstacle_density = 70),
      # Level 4
      PlatformerLevel( time_limit       = 60,
                       distance         = 5000, 
                       obstacle_density = 90)
    ]
    
    MAP_SEGMENTS = [
      [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 3, 4, 3, 6, 8, 9, 2, 4, 3, 4, 3, 6, 8, 9, 2, 6, 8, 9, 2, 4, 3, 4, 3],
        [10,18,20,19,18,20,10,11,12,11,12,10,18,20,10,11,12,11,10,19,18,10,11],
        [21, 0, 0, 0, 0, 0,17,20,19,18,20,21, 0, 0,17,20,19,20,21, 0, 0,17,20]
      ]
    ]
    
    '''
      [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3,10,21, 0, 0, 0, 0, 1, 2, 4, 6, 7],
        [ 1, 2, 3, 6, 8, 9, 2, 3, 6, 7,17,18,21, 0, 1, 2, 4, 6, 7,17,10,15, 0],
        [ 0,13,12,11,10,11,10,12,15, 0, 0, 0, 0, 0, 0,13,10,16, 0, 0,13,16, 0]
      ],
      [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 6, 7],
        [ 0, 0, 0, 1, 2, 6, 8, 9, 2, 6, 8, 9, 2, 3, 4, 3, 4, 3, 6, 7,17,21, 0],
        [ 1, 2, 3, 4,11,10,11,10,11,10,12,10,11,10,11,11,12,11,15, 0, 0, 0, 0],
        [ 0,13,12,10,12,10,11,10,12,10,11,10,11,12,11,10,11,12,16, 0, 0, 0, 0]
      ],
      [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 6, 7],
        [ 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 2, 6, 8, 9, 2, 3, 4, 3,11,16, 0],
        [ 0, 0, 0, 1, 2, 3, 4,12,11,10,11,12,11,10,11,12,11,10,11,12,11,15, 0],
        [ 1, 2, 3, 4,11,12,18,19,20,19,18,19,20,19,18,19,20,19,12,11,10,21, 0],
        [ 0,13,10,18,19,21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,17,10,21, 0, 0]
      ],
      [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 6, 8, 9, 2, 6, 7, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 3, 5,10,11,12,19,18,21, 0, 0, 0, 0],
        [ 0, 0, 0, 1, 2, 6, 7, 0,17,19,18,19,20,19,18,21, 0, 0, 0, 0, 0, 0, 0],
        [ 1, 2, 6, 7,17,21, 0, 1, 2, 3, 6, 8, 9, 2, 6, 8, 9, 2, 4, 3, 4, 6, 7],
        [ 0,17,21, 1, 2, 3, 6, 7,13,10,11,10,12,11,10,12,11,10,11,10,11,14, 0],
        [ 1, 2, 3, 4,11,12,21, 0,17,19,18,10,11,12,11,12,10,11,18,19,18,21, 0],
        [ 0,13,10,12,10,16, 0, 0, 0, 0, 0,17,18,19,20,19,18,21, 0, 0, 0, 0, 0]
      ]
      '''
    
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
      "plant1.png",
      "plant2.png",
      "plant3.png",
      "plant4.png",
      "plant5.png",
      "plant6.png",
      "plant7.png",
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
    VIEW_HEIGHT = 10
   
    TILE_WIDTH  = 64
    TILE_HEIGHT = 64
    TILE_SIZE = Size( TILE_WIDTH, TILE_HEIGHT )
    
    # runner initial cell position
    CELL_X = 2
    CELL_Y = len(MAP_SEGMENTS[0])-3
    
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
                raise ValueError( "Invalid Magic Power level number %d.  Level "
                                  "number must be between 1 and %d." %
                                  (self.level_number, len( PLATFORMER_LEVELS )) )

            self.level = PLATFORMER_LEVELS[self.level_number - 1]

            self.time_remaining = AutomatedInterpolator( self.level.time_limit,
                                                         0,
                                                         self.level.time_limit )
            
            self.create_background()
            self.create_tiles()
            self.create_obstacles()
            self.create_runner()
            self.create_huds()
            self.create_map()
            
            self.start_game()
        
        def start_game( self ):
            self.state = PLATFORMER_GAME_STATE_BEGIN
            self.runner["behavior"].run()
            
        def create_huds( self ):
            self.start_screen_hud             = GameObject()
            self.start_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/platformer/start_screen.png" ) )
            self.start_screen_hud["transform"].set_position( 138, 50 )

            self.stop_screen_hud             = GameObject()
            self.stop_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/platformer/stop_screen.png" ) )
            self.stop_screen_hud["transform"].set_position( 138, 50 )

            distance_run             = GameObject()
            distance_run["renderer"] = GameRenderer( GameText( self.get_distance_run, Color( 255, 255, 255, 255 ) ) )
            distance_run["transform"].set_position( 185, 159 )
            self.stop_screen_hud.add_child( distance_run )

            distance_left             = GameObject()
            distance_left["renderer"] = GameRenderer( GameText( self.get_distance, Color( 255, 255, 255, 255 ) ) )
            distance_left["transform"].set_position( 185, 193 )
            self.stop_screen_hud.add_child( distance_left )         
            self.start_screen_hud.add_child( distance_left )
            
            self.distance_left_hud             = GameObject()
            self.distance_left_hud["renderer"] = GameRenderer( GameText( self.get_distance_left, Color( 255, 255, 255, 255 ) ) )
            self.distance_left_hud["transform"].set_position( 340, 10 )

            self.time_remaining_hud             = GameObject()
            self.time_remaining_hud["renderer"] = GameRenderer( GameText( self.get_time_remaining, Color( 255, 255, 255, 255 ) ) )
            self.time_remaining_hud["transform"].set_position( 10, 10 )
            
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
              obstacle["renderer"] = GameRenderer( GameImage( "gfx/platformer/obstacles/" + obstacle_type ) )
              obstacle["transform"].set_scale( 0.7 )
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
            
            map_length = 0
            while map_length < self.level.distance:
              index = random.randint(0,len(MAP_SEGMENTS)-1)
              segments.append(MAP_SEGMENTS[index])
              map_length += len(MAP_SEGMENTS[index][0]) * TILE_WIDTH

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

                  if tile_type in OBSTACLE_TILES and x > 2:
                    if random.randint( 0, 100 ) <= self.level.obstacle_density:
                      # make sure there are no three obstacles in a row
                      if self.map[y][len(self.map[y])-1].obstacle == None or self.map[y][len(self.map[y])-2].obstacle == None:
                        obstacle = self.obstacles[ random.randint( 0, len(OBSTACLE_TYPES)-1 ) ]
                
                  cell = Cell( x*TILE_WIDTH + k*len(segment[0])*TILE_WIDTH, y*TILE_HEIGHT )
                  cell.tile      = tile
                  cell.obstacle  = obstacle
                  cell.walkable  = walkable
                  cell.drownable = drownable
                
                  self.map[y].append( cell )
                  
            row = self.map[0]
            #print len(self.map), len(self.map[0]), len(self.map[0])*TILE_WIDTH

        def get_time_remaining( self ):
            return "Time remaining: %d" % self.time_remaining.get_ceil_value()

        def get_distance_left( self ):
            return "Distance left: %d" % ( self.level.distance - self.runner["behavior"].distance )
                
        def get_distance( self ):
            return "%20d" % self.level.distance
                
        def get_distance_run( self ):
            return "%20d" % self.runner["behavior"].distance
            
        def get_result( self ):
            return int(self.runner["behavior"].distance)

        def render( self, blitter, clip_rect ):
            world_transform = self.get_world_transform()
            self.background["renderer"].render( blitter, clip_rect, world_transform )
            
            cell_x = self.runner["behavior"].cell_x-2
            
            for y in range(0, VIEW_HEIGHT):
              for x in range(cell_x, cell_x + VIEW_WIDTH):
                  
                cell = self.map[y][x]
                if cell.tile != None:
                  cell.tile["transform"].x = cell.x - self.runner["behavior"].distance
                  cell.tile["transform"].y = cell.y - TILE_HEIGHT/2
                  cell.tile["renderer"].render( blitter, clip_rect, world_transform )
                  
                if cell.obstacle != None:
                  cell.obstacle["transform"].x = cell.x - self.runner["behavior"].distance
                  cell.obstacle["transform"].y = cell.y - TILE_HEIGHT
                  cell.obstacle["renderer"].render( blitter, clip_rect, world_transform )

            if self.state == PLATFORMER_GAME_STATE_BEGIN:
                self.runner["renderer"].render( blitter, clip_rect, world_transform )
                self.start_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == PLATFORMER_GAME_STATE_PLAY:
                self.time_remaining_hud["renderer"].render( blitter, clip_rect, world_transform )
                self.distance_left_hud["renderer"].render( blitter, clip_rect, world_transform )
                self.runner["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == PLATFORMER_GAME_STATE_END:
                self.runner["renderer"].render( blitter, clip_rect, world_transform )
                self.stop_screen_hud["renderer"].render( blitter, clip_rect, world_transform )
            elif self.state == PLATFORMER_GAME_STATE_PAUSE:
                self.runner["renderer"].render( blitter, clip_rect, world_transform )
                self.stop_screen_hud["renderer"].render( blitter, clip_rect, world_transform )

        def update( self, delta_sec ):
            if self.state == PLATFORMER_GAME_STATE_PLAY:
              self.time_remaining.update( delta_sec )
  
              self.runner.update( delta_sec )
              
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
            self.game_object["transform"].set_position( CELL_X * TILE_WIDTH, CELL_Y * TILE_HEIGHT )
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
            
            if self.sub_distance >= TILE_WIDTH:
              self.sub_distance -= TILE_WIDTH
              self.cell_x += 1
              update_cell = True
            
            self.y_offset += self.y_velocity * delta_sec
            
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
                  self.game_object["transform"].y = self.cell_y*TILE_HEIGHT
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
