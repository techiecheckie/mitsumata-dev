image bg gears = "gfx/gears/background.jpg"
image bg cells = "gfx/cells/petri_dish.jpg"

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
    "power" : "Click the mouse to aim and set the amount of power while the arrows are moving.\n\nPress esc to quit the game.",
    "squats" : "As the marker passes over each lit section, hit the correct arrow key (down, left, or up).\n\nPress esc to quit the game.",
    "gears" : "Use the mouse to drag cogs and lock them on axles.\n\nPress esc to quit the game.",
    "garden" : "Insert description here. \n\nLorem ipsum dolor sit amet.",
    "lock" : "",
    "bottles" : ""
  }
  
  CURRENT_DESCRIPTION = ""
  
  MINIGAME_POS_X  = 363
  MINIGAME_POS_Y  = 112
  MINIGAME_WIDTH  = 648
  MINIGAME_HEIGHT = 598
  
  MINIGAME_GRID_X    = 380
  MINIGAME_GRID_Y    = 180
  MINIGAME_CELL_SIZE = 150
  MINIGAME_GRID_COLS = 4
  MINIGAME_GRID_ROWS = 3 
  
  MINIGAME_BONUSES = {
    "mole" : [
      (5000, ("hp", 300), ("mp", 200)),
      (3000, ("hp", 200), ("mp", 100)),
      (1000, ("hp", 100), ("mp", 100))
    ],
    "cell" : [
      (5000, ("hp", 200)),
      (3000, ("hp", 100))
    ]
  }

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
        
        if button == "garden":
          show_garden()
        elif button == "bottles":
          show_bottles()
        elif button == "lock":
          score = show_lock(persistent.minigame_levels["lock"])
        else:
          score = run(button)
          update_high_score(button, score)
          
        renpy.show(background, zorder=-1)
        
    hide_minigame_ui(background)
     
    return

    
  def choose_game(name):
    if name == "mole":
      game = WhackAMole
      bg   = "bg dgro"
    elif name == "cell":
      game = Cells
      bg   = "bg cells"
    elif name == "platformer":
      game = Platformer
      bg   = "bg dgro"
    elif name == "duck":
      game = DuckHunt
      bg   = "bg dsky"
    elif name == "force":
      game = MagicForce
      bg   = "bg dgro"
    elif name == "power":
      game = MagicPower
      bg   = "bg dgro"
    elif name == "squats":
      game = Squats
      bg   = "bg dgro"
    elif name == "gears":
      game = Gears
      bg   = "bg gears"
    
    return game, bg
  
  
  def run(name):
    (game, bg) = choose_game(name)
    renpy.show(bg, at_list=[Position(xpos=MINIGAME_POS_X, 
                                     ypos=MINIGAME_POS_Y-40), 
                            Transform(anchor=(0.0,0.0))], 
                            zorder=-1)
    score = run_minigame( game_type = game,
                          x=MINIGAME_POS_X, 
                          y=MINIGAME_POS_Y,
                          game_width=MINIGAME_WIDTH,
                          game_height=MINIGAME_HEIGHT,
                          level_number = persistent.minigame_levels[name] )
    
    return score
  
  def update_high_score(game, score):
    print "Got", score, "points, old score", persistent.minigame_scores[game]
    
    if score > persistent.minigame_scores[game]:
      old_score = persistent.minigame_scores[game]
      persistent.minigame_scores[game] = score

      score_row     = 10
      old_score_row = 10

      game_bonuses = MINIGAME_BONUSES[game]
      for i in range(0, len(game_bonuses)):
        if score >= game_bonuses[i][0]:
          score_row = i
          break
          
      for i in range(0, len(game_bonuses)):
        if old_score >= game_bonuses[i][0]:
          old_score_row = i
          break
          
      if score_row < old_score_row:
        renpy.transition(dissolve)
        ui.frame(xpos=MINIGAME_POS_X+50, 
                 ypos=MINIGAME_POS_Y+150, 
                 background="gfx/textbox.png",
                 xpadding=40,
                 ypadding=40,
                 xmaximum=530)
        ui.vbox()
        ui.text("{size=-2}Your new highscore unlocked new stat bonuses:{/size}")
        bonus_row = game_bonuses[score_row]
        for i in range(1, len(bonus_row)):
          ui.text("{size=-2}    +" + str(bonus_row[i][1]) + " " + bonus_row[i][0] + "{/size}") 
        ui.close()
    
        # Full screen hidden button, "click anywhere to continue" kind
        ui.frame(xpos=0, ypos=0, background=None)
        ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
        ui.interact()
        renpy.transition(dissolve)
      
        update_stats()
        update_minigame_ui(HP, MP)
    
    return
      
  # running minigames without starting the pda first
  def minigame(name, level, score_to_pass):
    show_minigame_ui(None)
    show_description(GAME_DESCRIPTIONS[name])
    
    # exception
    if name == "garden":
      show_garden()
      score = 0
    elif name == "lock":
      score = show_lock(level)
    elif name == "bottles":
      show_bottles()
      score = 0
    else:   
      (game, bg) = choose_game(name)
      renpy.show(bg, at_list=[Position(xpos=MINIGAME_POS_X-20, 
                                       ypos=MINIGAME_POS_Y-40), 
                              Transform(anchor=(0.0,0.0))], 
                              zorder=-1)
      score = run_minigame(game_type = game, 
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
    
    return score >= score_to_pass

    
  def show_description(description):
    ui.frame(xpos=DESCRIPTION_POS_X, 
             ypos=DESCRIPTION_POS_Y, 
             xmaximum=DESCRIPTION_WIDTH, 
             background=None)
    ui.text(description)
    
    return
