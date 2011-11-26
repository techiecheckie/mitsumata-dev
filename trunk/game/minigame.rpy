init python:
  DESCRIPTION_POS_X = 60
  DESCRIPTION_POS_Y = 110
  DESCRIPTION_WIDTH = 250
  
  GAME_DESCRIPTIONS = {
    "mole" : "Insert description here. \n\nLorem ipsum dolor sit amet.",
    "cell" : "Insert description here. \n\nLorem ipsum dolor sit amet.",
    "platformer" : "Insert description here. \n\nLorem ipsum dolor sit amet.",
    "duck" : "Insert description here. \n\nLorem ipsum dolor sit amet.",
    "force" : "Insert description here. \n\nLorem ipsum dolor sit amet.",
    "power" : "Insert description here. \n\nLorem ipsum dolor sit amet mole.",
    "squats" : "Insert description here. \n\nLorem ipsum dolor sit amet mole.",
    "gears" : "Insert description here. \n\nLorem ipsum dolor sit amet mole."
  }
  
  MINIGAME_POS_X  = 365
  MINIGAME_POS_Y  = 114
  MINIGAME_WIDTH  = 648
  MINIGAME_HEIGHT = 593
  
  MINIGAME_GRID_X    = 400
  MINIGAME_GRID_Y    = 200
  MINIGAME_CELL_SIZE = 150
  MINIGAME_GRID_COLS = 4
  MINIGAME_GRID_ROWS = 2 

  def show_minigame_screen():
    button       = ""
    button_value = ""

    background = "bg riroom"
    show_minigame_ui(background, False)
  
    while True:      
      for y in range(0, MINIGAME_GRID_ROWS):
        for x in range(0, MINIGAME_GRID_COLS):
          index = y * MINIGAME_GRID_COLS + x
          if index > len(persistent.unlocked_minigames):
            break
            
          minigame = persistent.unlocked_minigames[index]
          
          ui.frame(xpos=MINIGAME_GRID_X + x * MINIGAME_CELL_SIZE, 
                   ypos=MINIGAME_GRID_Y + y * MINIGAME_CELL_SIZE,
                   background=None)
          ui.imagebutton("gfx/buttons/minigame_" + minigame + ".png",
                         "gfx/buttons/minigame_" + minigame + "_hover.png",
                         clicked=ui.returns(minigame))
    
      button = ui.interact()
      if button == "exit":
        break
      else:
        score = run(button)
        update_high_score(button, score)
        
    hide_minigame_ui(background, False)
     
    return

    
  def choose_game(name):
    if name == "mole":
      game = WhackAMole
    elif name == "cell":
      game = Cells
    elif name == "platformer":
      game = Platformer
    elif name == "duck":
      game = DuckHunt
    elif name == "force":
      game = MagicForce
    elif name == "power":
      game = MagicPower
    elif name == "squats":
      game = Squats
    elif name == "gears":
      game = Gears
    
    return game
  
  
  def run(name):
    show_description(GAME_DESCRIPTIONS[name])
    score = run_minigame( game_type = choose_game(name),
                          x=MINIGAME_POS_X, 
                          y=MINIGAME_POS_Y,
                          game_width=MINIGAME_WIDTH,
                          game_height=MINIGAME_HEIGHT )
                          # level_number = persistent.minigame_level[name] )
  
  
  def update_high_score(game, score):
    print "Got", score, "points."
    if game in persistent.minigame_scores:
      print "Old score:", persistent.minigame_scores[game]
      if score > persistent.minigame_scores[game]:
        persistent.minigame_scores[game] = score
    else:
      persistent.minigame_scores[game] = score
      
      
  # running minigames without starting the pda first
  def minigame(name, level, score_to_pass):
    show_minigame_ui(None, False)
    
    show_description(GAME_DESCRIPTIONS[name])
    
    score = run_minigame(game_type = choose_game(name), 
                         x=MINIGAME_POS_X, 
                         y=MINIGAME_POS_Y,
                         game_width=MINIGAME_WIDTH,
                         game_height=MINIGAME_HEIGHT,
                         level_number = level)
    update_high_score(name, score)
    
    # update max level? (when playing through the PDA)
    # current_level = persistent.minigame_level[name]
    # if score >= score_to_pass and current_level < level:
    #   persistent.minigame_level[name] = level
    
    hide_minigame_ui(None, False)
    
    return score >= score_to_pass

    
  def show_description(desc):
    ui.frame(xpos=DESCRIPTION_POS_X, 
             ypos=DESCRIPTION_POS_Y, 
             xmaximum=DESCRIPTION_WIDTH, 
             background=None)
    ui.text(desc)