init python:
  DESCRIPTION_POS_X = 60
  DESCRIPTION_POS_Y = 110
  DESCRIPTION_WIDTH = 250
  
  MINIGAME_MAIN_DESCRIPTION = "Insert main description here."
  
  GAME_DESCRIPTIONS = {
    "mole" : "Use the keypad or mouse to hit the moles.\n\nPress esc to quit the game.",
    "cell" : "Use the mouse to click on the infected cells.",
    "platformer" : "Use spacebar to jump over obstacles and pits.\n\nPress esc to quit the game.",
    "duck" : "Use the mouse to shoot the birds.\n\nPress esc to quit the game.",
    "force" : "Use the keypad or keys 0-9 to type the numbers as they appear.\n\nPress esc to quit the game.",
    "power" : "Click the mouse to select the correct target and the amount of power while the arrows are moving.\n\nPress esc to quit the game.",
    "squats" : "As the marker passes over each lit section, hit the correct arrow key (down, left, or up).\n\nPress esc to quit the game.",
    "gears" : "Use the mouse to drag cogs and lock them on axles.\n\nPress esc to quit the game.",
    "garden" : "Insert description here. \n\nLorem ipsum dolor sit amet."
  }
  
  # config.overlay_functions.append(show_description) "fix"
  CURRENT_DESCRIPTION = "asdasdf"
  
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
    show_minigame_ui(background)
  
    while True:      
      for y in range(0, MINIGAME_GRID_ROWS):
        for x in range(0, MINIGAME_GRID_COLS):
          index = y * MINIGAME_GRID_COLS + x
          if index >= len(persistent.unlocked_minigames):
            break
            
          minigame = persistent.unlocked_minigames[index]
          
          ui.frame(xpos=MINIGAME_GRID_X + x * MINIGAME_CELL_SIZE, 
                   ypos=MINIGAME_GRID_Y + y * MINIGAME_CELL_SIZE,
                   background=None)
          ui.imagebutton("gfx/buttons/minigame_" + minigame + ".png",
                         "gfx/buttons/minigame_" + minigame + "_hover.png",
                         clicked=ui.returns(minigame))
    
      ui.frame(xpos=DESCRIPTION_POS_X, 
               ypos=DESCRIPTION_POS_Y, 
               xmaximum=DESCRIPTION_WIDTH, 
               background=None)
      ui.text(MINIGAME_MAIN_DESCRIPTION)
    
      button = ui.interact()
      if button == "exit":
        break
      else:
        renpy.hide(background)
        
        show_description(GAME_DESCRIPTIONS[button])
        
        # exception
        if button == "garden":
          show_garden()
        else:
          score = run(button)
          update_high_score(button, score)
          
        renpy.show(background, zorder=-1)
        
    hide_minigame_ui(background)
     
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
    score = run_minigame( game_type = choose_game(name),
                          x=MINIGAME_POS_X, 
                          y=MINIGAME_POS_Y,
                          game_width=MINIGAME_WIDTH,
                          game_height=MINIGAME_HEIGHT,
                          level_number = persistent.minigame_levels[name] )
    
    return score
  
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
    show_minigame_ui(None)
    show_description(GAME_DESCRIPTIONS[name])
    
    # exception
    if name == "garden":
      show_garden()
      score = 0
    else:   
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
    
    hide_minigame_ui(None)
    #config.overlay_functions.remove(show_description)
    
    return score >= score_to_pass

    
  def show_description(description):
    ui.frame(xpos=DESCRIPTION_POS_X, 
             ypos=DESCRIPTION_POS_Y, 
             xmaximum=DESCRIPTION_WIDTH, 
             background=None)
    ui.text(description)
    
    return
