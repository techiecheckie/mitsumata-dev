init python:
    class PlatformerLevel( object ):
        def __init__( self, time_limit ):
            self.time_limit = time_limit

    PLATFORMER_LEVELS = [
        PlatformerLevel( time_limit = 60 )
        ]

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
    RUNNER_STATE_FALLING    = "falling"
    RUNNER_STATE_DROWNING   = "drowning"
    
    # animation names.
    RUNNER_ANIMATION_RUN     = "run"
    RUNNER_ANIMATION_JUMP    = "jump"
    RUNNER_ANIMATION_ASCEND  = "ascend"
    RUNNER_ANIMATION_HOVER   = "hover"
    RUNNER_ANIMATION_DESCEND = "descend"
    RUNNER_ANIMATION_LAND    = "land"
    RUNNER_ANIMATION_FALL    = "fall"
    RUNNER_ANIMATION_DROWN   = "drown"

    # animation durations.  these divided into the number of frames that are
    # in the corresponding animation are the frames per second value passed to
    # the GameAnimation constructor.
    RUN_ANIMATION_DURATION     = 1.0
    JUMP_ANIMATION_DURATION    = 0.2
    ASCEND_ANIMATION_DURATION  = 0.5
    HOVER_ANIMATION_DURATION   = 0.5
    DESCEND_ANIMATION_DURATION = 0.5
    LAND_ANIMATION_DURATION    = 0.4
    FALL_ANIMATION_DURATION    = 1.0
    DROWN_ANIMATION_DURATION   = 1.0

    # number of animation frames.
    NUMBER_RUN_FRAMES     = 6
    NUMBER_JUMP_FRAMES    = 2
    NUMBER_ASCEND_FRAMES  = 2
    NUMBER_HOVER_FRAMES   = 1
    NUMBER_DESCEND_FRAMES = 2
    NUMBER_LAND_FRAMES    = 2
    NUMBER_FALL_FRAMES    = 4
    NUMBER_DROWN_FRAMES   = 3
    
    RUN_SPEED      = 110
    JUMP_SPEED     = 170
    JUMP_DELAY     = 0.3
    MAX_FALL_SPEED = 300
    GRAVITY        = 200

    VIEW_WIDTH = 12
    VIEW_HEIGHT = 10
    
    VIEW = [
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0]
           ]
    
    # testmap
    MAP = [
           [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [ 0, 1, 2, 6, 7, 0, 0, 0, 0, 1, 2, 3,10,21, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 6, 7, 0, 0, 0, 0, 0, 0, 0],
           [ 3, 4, 3, 6, 8, 9, 2, 3, 6, 7,17,18,21, 0, 1, 2, 4, 3, 4, 3, 4, 3, 4, 3, 6, 8, 9, 2, 3, 4, 3, 4, 3, 3, 4, 3, 6, 8, 9, 2, 3, 4, 3, 4, 3],
           [11,11,11,11,11,11,11,11,16, 0, 0, 0, 0, 0, 0,17,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11]
          ]

    TILES = [
            ("grass-edge-1.png", False),  # 1
            ("grass-edge-2.png", True),   # 2
            ("grass-1.png", True),        # 3
            ("grass-2.png", True),        # 4
            ("grass-3.png", True),        # 5
            ("grass-edge-3.png", True),   # 6
            ("grass-edge-4.png", False),  # 7
            ("water-1.png", False),       # 8
            ("water-2.png", False),       # 9
            ("dirt-1.png", False),        # 10
            ("dirt-2.png", False),        # 11
            ("dirt-3.png", False),        # 12
            ("dirt-edge-1.png", False),   # 13
            ("dirt-edge-2.png", False),   # 14
            ("dirt-edge-3.png", False),   # 15
            ("dirt-edge-4.png", False),   # 16
            ("dirt-bottom-1.png", False), # 17
            ("dirt-bottom-2.png", False), # 18
            ("dirt-bottom-3.png", False), # 19
            ("dirt-bottom-4.png", False), # 20
            ("dirt-bottom-5.png", False)  # 21
            ]
   
    TILE_WIDTH  = 64
    TILE_HEIGHT = 64
    TILE_SIZE = Size( TILE_WIDTH, TILE_HEIGHT )
   
    WATER_TILES = [8,9]    
    
    # runner initial cell position
    CELL_X = 1
    CELL_Y = len(VIEW)-2
    
    class Tile( GameObject ):
      def __init__( self, tile_type, solid ):
        super( Tile, self ).__init__()
        self.tile_type = tile_type
        self.solid = solid
        
      def is_walkable( self ):
        return self.solid
    
    class Platformer( Minigame ):
        def __init__( self, level_number=1 ):
            super( Platformer, self ).__init__()

            if level_number > len( PLATFORMER_LEVELS ) or level_number <= 0:
                raise ValueError( "Invalid Magic Power level number %d.  Level "
                                  "number must be between 1 and %d." %
                                  (level_number, len( PLATFORMER_LEVELS )) )

            # setup the level difficulty parameters.
            level = PLATFORMER_LEVELS[level_number - 1]

            self.time_remaining = AutomatedInterpolator( level.time_limit,
                                                         0,
                                                         level.time_limit )

            # setup the game state.
            self.state       = PLATFORMER_GAME_STATE_BEGIN
            self.base_score  = 0
            self.total_score = 0

            # setup the entities.
            self.start_screen_hud   = None
            self.stop_screen_hud    = None
            self.score_hud          = None
            self.time_remaining_hud = None
            
            # temp, going to be removed later
            self.x_offset = 0
            self.x = 0

            self.create_tiles()
            self.create_runner()
            self.create_huds()

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
            
            # runner sprite positioning, one to the right and up from the bottom left corner
            runner_x = CELL_X * TILE_WIDTH
            runner_y = CELL_Y * TILE_HEIGHT - TILE_HEIGHT/2
            
            runner["transform"].set_position( runner_x, runner_y )
            runner["transform"].set_scale( 1.0 )
            runner["behavior"] = RunnerBehavior( runner_x, runner_y )
            runner["behavior"].run()
            self.runner = runner
            
        def create_tiles( self ):
            for y in range(0,len(MAP)):
              for x in range(0,len(MAP[y])):
                tile_value = MAP[y][x]
                if tile_value > 0:
                  tile_data = TILES[tile_value-1]
                  # TODO: use references rather than creating new objects
                  tile = Tile(tile_value, tile_data[1])
                  tile["renderer"] = GameRenderer( GameImage( "gfx/platformer/tiles/" + tile_data[0], Anchor.CENTER ) )
                  tile["collider"] = GameBoxCollider( TILE_SIZE, Anchor.CENTER )
                  #tile["renderer"].set_collider_visible( True )
                  tile["transform"].set_scale( 0.5 )
                  tile["transform"].set_position( x*TILE_WIDTH + TILE_WIDTH/2, y*TILE_HEIGHT )
                else:
                  tile = None
                    
                MAP[y][x] = tile
            
            # populate the view
            for y in range(0, VIEW_HEIGHT):
              for x in range(0, VIEW_WIDTH):
                VIEW[y][x] = MAP[y][x]
        
        def create_huds( self ):
            self.start_screen_hud             = GameObject()
            self.start_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/platformer/start_screen.png" ) )
            self.start_screen_hud["transform"].set_position( 138, 50 )

            self.stop_screen_hud             = GameObject()
            self.stop_screen_hud["renderer"] = GameRenderer( GameImage( "gfx/platformer/stop_screen.png" ) )
            self.stop_screen_hud["transform"].set_position( 138, 50 )

            base_score             = GameObject()
            base_score["renderer"] = GameRenderer( GameText( self.get_base_score ) )
            base_score["transform"].set_position( 185, 159 )
            self.stop_screen_hud.add_child( base_score )

            total_score             = GameObject()
            total_score["renderer"] = GameRenderer( GameText( self.get_total_score ) )
            total_score["transform"].set_position( 185, 320 )
            self.stop_screen_hud.add_child( total_score )

            self.score_hud             = GameObject()
            self.score_hud["renderer"] = GameRenderer( GameText( self.get_score ) )
            self.score_hud["transform"].set_position( 400, 10 )

            self.time_remaining_hud             = GameObject()
            self.time_remaining_hud["renderer"] = GameRenderer( GameText( self.get_time_remaining ) )
            self.time_remaining_hud["transform"].set_position( 10, 10 )

        def get_score( self ):
            return "Score: %16d" % self.base_score

        def get_time_remaining( self ):
            return "Time Remaining: %d" %  self.time_remaining.get_ceil_value()

        def get_base_score( self ):
            if self.base_score < 1000:
                return "%20d" % self.base_score
            elif self.base_score < 10000:
                return "%18d" % self.base_score
            else:
                return "%16d" % self.base_score

        def get_total_score( self ):
            if self.total_score < 1000:
                return "%20d" % self.total_score
            elif self.total_score < 10000:
                return "%18d" % self.total_score
            else:
                return "%16d" % self.total_score

        def render( self, blitter ):
            world_transform = self.get_world_transform()

            for y in range(0,VIEW_HEIGHT):
              for x in range(0,VIEW_WIDTH):
                tile = VIEW[y][x]
                if tile != None:
                  tile["renderer"].render( blitter, world_transform )

            if self.state == PLATFORMER_GAME_STATE_BEGIN:
                self.runner["renderer"].render( blitter, world_transform )
                self.start_screen_hud["renderer"].render( blitter, world_transform )
            elif self.state == PLATFORMER_GAME_STATE_PLAY:
                self.runner["renderer"].render( blitter, world_transform )
            elif self.state == PLATFORMER_GAME_STATE_END:
                self.runner["renderer"].render( blitter, world_transform )
                self.stop_screen_hud["renderer"].render( blitter, world_transform )
            
            self.time_remaining_hud["renderer"].render( blitter, world_transform )
            self.score_hud["renderer"].render( blitter, world_transform )

        def update( self, delta_sec ):
            if self.state == PLATFORMER_GAME_STATE_PLAY:
                self.time_remaining.update( delta_sec )
  
                self.runner.update( delta_sec )
            
                # TODO: clean this mess up
                
                self.x_offset += self.runner["behavior"].x_velocity * delta_sec
                if self.x_offset >= TILE_WIDTH:    
                  self.x_offset -= TILE_WIDTH
                  self.x += 1
              
                  # update the view array
                  for y in range(0, VIEW_HEIGHT):
                    for x in range(0, VIEW_WIDTH):
                      map_x = x + self.x
                      
                      # if running out of map, start displaying tiles from the beginning
                      if map_x >= len(MAP[y]):
                        map_x -= len(MAP[y])
                        self.x -= len(MAP[y])
                        
                      tile = MAP[y][map_x]
                      if tile != None:
                        tile["transform"].set_position( x*TILE_WIDTH + TILE_WIDTH/2, y*TILE_HEIGHT )
                      VIEW[y][x] = tile

                # translate
                for y in range(0, VIEW_HEIGHT):
                  for x in range(0, VIEW_WIDTH):
                    tile = VIEW[y][x]
                    if tile != None:
                      tile["transform"].x -= self.runner["behavior"].x_velocity * delta_sec
                
                if self.time_remaining.get_value() <= 0 or self.runner["behavior"].is_dead():
                    self.state = PLATFORMER_GAME_STATE_END
                    self.total_score = self.base_score

        def on_key_down( self, key ):
            if key == pygame.K_ESCAPE:
                self.quit()
            elif key == pygame.K_SPACE:
                self.runner["behavior"].jump()

        def on_mouse_up( self, mx, my, button ):
            if button == Minigame.LEFT_MOUSE_BUTTON:
                if self.state == PLATFORMER_GAME_STATE_BEGIN:
                    self.state = PLATFORMER_GAME_STATE_PLAY
                elif self.state == PLATFORMER_GAME_STATE_END:
                    self.quit()

    class RunnerBehavior( GameComponent ):
        def __init__( self, x, y ):
            super( RunnerBehavior, self ).__init__()
            self.state = RUNNER_STATE_RUNNING
            
            # sprite position
            self.x = x
            self.y = y
            self.x_offset = 0
            self.y_offset = 0
            
            self.cell_x = CELL_X + 1
            self.cell_y = CELL_Y
            self.current_tile = VIEW[self.cell_y][self.cell_x]
            
            self.y_velocity = 0
            self.x_velocity = RUN_SPEED
            
            self.jump_requested = False
            self.dead = False
            
            self.delay_counter = 0
            
        def run( self ):
            self.state = RUNNER_STATE_RUNNING
            self.game_object["renderer"].play_animation( RUNNER_ANIMATION_RUN )
            
        def jump( self ):
            #self.state = RUNNER_STATE_RUNNING
            self.jump_requested = True
            #self.delay_counter = 0
            
        def is_dead( self ):
            return self.dead
        
        def update( self, delta_sec ):
            self.x_offset += self.x_velocity * delta_sec
            self.y_offset += self.y_velocity * delta_sec
            self.game_object["transform"].y += self.y_velocity * delta_sec
            
            update_cell = False
            
            if self.x_offset >= TILE_WIDTH/3:
              self.x_offset -= TILE_WIDTH
              update_cell = True
            
            if self.y_offset > TILE_HEIGHT:
              self.y_offset = 0
              self.cell_y += 1
              update_cell = True
            elif self.y_offset < -TILE_HEIGHT:
              self.y_offset = 0
              self.cell_y -= 1
              update_cell = True
            
            if update_cell:
              if self.cell_y < VIEW_HEIGHT:
                self.current_tile = VIEW[self.cell_y][self.cell_x]
                
            # state checks follow
                
            if self.state == RUNNER_STATE_RUNNING:
              if self.current_tile == None or not self.current_tile.solid:
                self.state = RUNNER_STATE_DESCENDING
                self.game_object["renderer"].play_animation( RUNNER_ANIMATION_DESCEND )
              else:
                if self.jump_requested:
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
              
              if self.current_tile == None:
                if self.y_velocity < MAX_FALL_SPEED:
                  self.y_velocity += GRAVITY * delta_sec
              elif not self.current_tile.solid:
                if self.current_tile.tile_type in WATER_TILES and self.y_offset >= TILE_HEIGHT/4:
                  self.state = RUNNER_STATE_DROWNING
                  self.game_object["renderer"].play_animation( RUNNER_ANIMATION_DROWN )
                else:
                  if self.y_velocity < MAX_FALL_SPEED:
                    self.y_velocity += GRAVITY * delta_sec
              else:
                if self.y_offset >= 0:
                  self.state = RUNNER_STATE_LANDING
                  self.game_object["renderer"].play_animation( RUNNER_ANIMATION_LAND )
                
                  # reset runner's y position
                  self.game_object["transform"].y = self.cell_y*TILE_HEIGHT - TILE_HEIGHT/2
                  
              # the runner has fallen off the screen
              if self.cell_y > VIEW_HEIGHT:
                self.dead = True
              
            elif self.state == RUNNER_STATE_LANDING:
              self.y_velocity = 0
              self.x_velocity = 0
              self.delay_counter += delta_sec
              if self.delay_counter >= LAND_ANIMATION_DURATION:
                self.state = RUNNER_STATE_RUNNING
                self.game_object["renderer"].play_animation( RUNNER_ANIMATION_RUN )
                
                self.x_velocity = RUN_SPEED
                self.delay_counter = 0
                
            elif self.state == RUNNER_STATE_DROWNING:
              self.y_velocity = 0
              self.x_velocity = 0
              self.delay_counter += delta_sec
              if self.delay_counter > 3:
                self.dead = True
                self.delay_counter = 0
