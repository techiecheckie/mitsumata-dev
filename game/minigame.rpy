init python:
  renpy.image("bg_gears", "gfx/gears/background.jpg")
  renpy.image("bg_cells", "gfx/cells/petri_dish.jpg")
  renpy.image("bg_dgro", "gfx/backgrounds/daygrass.jpg")
  renpy.image("bg_dsky", "gfx/backgrounds/daysky.jpg")
  renpy.image("bg_mini", "gfx/backgrounds/whitescr.jpg")
  renpy.image("bg_blackscr", "gfx/backgrounds/blackscr.png")

  DESCRIPTION_POS_X = 60
  DESCRIPTION_POS_Y = 110
  DESCRIPTION_WIDTH = 250
  
  # default description displayed by the method show_description()
  MINIGAME_DESCRIPTION = ""

  MINIGAME_MAIN_DESCRIPTION = "Insert main description here."
  MINIGAME_STAT_BONUS_UNLOCKED = "Your new highscore unlocked new stat bonuses:"
  
  GAME_DESCRIPTIONS = {
    "mole" : "Agility:\n\nUse the keypad or mouse to hit the moles.",
    "cell" : "Cells:\n\nUse the mouse to click on the infected cells.",
    "platformer" : "Use the spacebar to jump over obstacles and pits.",
    "duck" : "Hunting:\n\nUse the mouse to shoot the birds.",
    "force" : "Magic force:\n\nUse the keypad or keys 0-9 to type the numbers as they appear.",
    "power" : "Magic control:\n\nClick the mouse to aim and set the amount of power while the arrows are moving.",
    "squats" : "Strength:\n\nWait for the marker to move over the green area and press the spacebar to help Riku time his efforts.",
    "gears" : "Gears:\n\nUse the mouse to drag cogs and lock them on axles.",
    "garden" : "Gardening:\n\nInsert description here..",
    # Lock and bottles have their own level-based descriptions, no need to fill.
    "lock" : "",
    "bottles" : ""
  }
  
  MINIGAME_POS_X  = 363
  MINIGAME_POS_Y  = 90
  MINIGAME_WIDTH  = 646
  MINIGAME_HEIGHT = 630
  
  MINIGAME_GRID_X    = 380
  MINIGAME_GRID_Y    = 180
  MINIGAME_CELL_SIZE = 150
  MINIGAME_GRID_COLS = 4
  MINIGAME_GRID_ROWS = 3 
  
  # TODO fill in the rest
  # Bonus format: (required points, (stat, amount), (stat, amount), ...),
  # eg. with two bonuses: (5000, ("hp", 300), ("mp", 200))
  #     with one bonus:   (3000, ("hp", 150))
  MINIGAME_BONUSES = {
    "mole" : [
      (5000, ("hp", 300), ("mp", 200)),
      (3000, ("hp", 200), ("mp", 100)),
      (1000, ("hp", 100), ("mp", 100))
    ],
    "cell" : [
      (5000, ("hp", 200)),
      (3000, ("hp", 100))
    ],
    "platformer" : [],
    "duck" : [],
    "force" : [],
    "power" : [],
    "squats" : [
      (1000, ("hp", 100)),
      (500, ("hp", 50))
    ],
    "gears" : [],
    "garden" : [],
    "lock" : [],
    "bottles" : []
  }

  # Displays the minigame screen, filling the grid with available (unlocked)
  # minigames in the order they've been acquired.
  def show_minigame_screen():
    button       = ""
    button_value = ""

    show_minigame_ui("bg_mini", True)
    
    minigame_keys = persistent.unlocked_minigames.keys()
  
    while True:
      set_description(MINIGAME_MAIN_DESCRIPTION)

      for y in range(0, MINIGAME_GRID_ROWS):
        for x in range(0, MINIGAME_GRID_COLS):
          index = y * MINIGAME_GRID_COLS + x
          if index >= len(minigame_keys):
            break
          
          ui.frame(xpos=MINIGAME_GRID_X + x * MINIGAME_CELL_SIZE, 
                   ypos=MINIGAME_GRID_Y + y * MINIGAME_CELL_SIZE,
                   background=None)
          ui.imagebutton("gfx/buttons/minigame_" + minigame_keys[index] + ".png",
                         "gfx/buttons/minigame_" + minigame_keys[index] + "_hover.png",
                         clicked=ui.returns(minigame_keys[index]))

      button = ui.interact()
      if button == "exit":
        break
      else:
        #renpy.hide("bg_mini")
        
        set_description(GAME_DESCRIPTIONS[button])
        
        if button == "garden":
          show_garden()
        elif button == "lock":
          show_lock()
        elif button == "bottles":
          show_bottles()
        else:
          score = run(button)
          update_high_score(button, score)
          
        renpy.show("bg_mini")
    
    config.overlay_functions.remove(minigame_description)
    hide_minigame_ui("bg_mini")
     
    return

  # Returns a game instance and a background based on the name that was given.
  def get_game(name):
    if name == "mole":
      game = WhackAMole
      bg   = "bg_dgro"
    elif name == "cell":
      game = Cells
      bg   = "bg_cells"
    elif name == "platformer":
      game = Platformer
      bg   = "bg_blackscr"
    elif name == "duck":
      game = DuckHunt
      bg   = "bg_dsky"
    elif name == "force":
      game = MagicForce
      bg   = "bg_dgro"
    elif name == "power":
      game = MagicPower
      bg   = "bg_dgro"
    elif name == "squats":
      game = Squats
      bg   = "bg_dgro"
    elif name == "gears":
      game = Gears
      bg   = "bg_gears"
    else:
      # Potential crash when returning None values?
      game = None
      bg = None
    
    return game, bg
  
  # Runs a minigame and returns its score. 
  def run(name):
    (game, bg) = get_game(name)
    renpy.show(bg, at_list=[Position(xpos=MINIGAME_POS_X, 
                                     ypos=MINIGAME_POS_Y), 
                            Transform(anchor=(0.0,0.0))])
    config.overlay_functions.remove(minigame_ui_buttons)
    
    score = run_minigame( game_type=game,
                          x=MINIGAME_POS_X, 
                          y=MINIGAME_POS_Y,
                          game_width=MINIGAME_WIDTH,
                          game_height=MINIGAME_HEIGHT,
                          game_high_score=persistent.unlocked_minigames[name][0],
                          level_number=persistent.unlocked_minigames[name][1] )
                          
    config.overlay_functions.append(minigame_ui_buttons)
    renpy.hide(bg)
    
    return score
  
  # Updates highscores stored in persistent.unlocked_minigames[game]. If the
  # value returned by the minigame as parameter 'score' is higher than the
  # current value stored in the persistent dictionary, this method loops through
  # the game's bonuses (MINIGAME_BONUSES[game], above), looking for new (stat)
  # bonuses to unlock. 
  def update_high_score(game, score):
    print "Got", score, "points, old score", persistent.unlocked_minigames[game][0]
    
    if score > persistent.unlocked_minigames[game][0]:
      old_score = persistent.unlocked_minigames[game][0]
      persistent.unlocked_minigames[game][0] = score

      # To make sure we're not giving the same bonuses more than once, a 
      # comparison of (new_score_row < old_score_row) must be done. This happens 
      # by comparing the new and old score values to the ones listed in the 
      # minigame's bonus arrays' first indices, e.g.
      #   "mole" : [ (5000, ("hp", 300), ...), (3000, ("hp", 200), ...), ... ] 
      new_score_row = len(MINIGAME_BONUSES[game])
      old_score_row = new_score_row

      game_bonuses = MINIGAME_BONUSES[game]
      for i in range(0, len(game_bonuses)):
        if score >= game_bonuses[i][0]:
          new_score_row = i
          break
          
      for i in range(0, len(game_bonuses)):
        if old_score >= game_bonuses[i][0]:
          old_score_row = i
          break
      
      if new_score_row < old_score_row:
        bonus_row = game_bonuses[new_score_row]
      
        renpy.transition(dissolve)
        ui.frame(xpos=MINIGAME_POS_X+50, 
                 ypos=MINIGAME_POS_Y+150, 
                 background="gfx/textbox.png",
                 xpadding=40,
                 ypadding=40,
                 xmaximum=530)
        ui.vbox()
        ui.text("{size=-2}" + MINIGAME_STAT_BONUS_UNLOCKED + "{/size}")
        for i in range(1, len(bonus_row)):
          ui.text("{size=-2}    +" + str(bonus_row[i][1]) + " " + bonus_row[i][0] + "{/size}") 
        ui.close()
        
        show_invisible_button("mini")
        renpy.pause(0.5)
      
        update_stats()
        update_minigame_ui(HP, MP)
    
    return

  # Starts a minigame without having to call the PDA first. Compares the value
  # returned by the minigame, returning boolean score >= score_to_pass.
  def minigame(name, level, score_to_pass, background, exit_enabled):
    game = get_game(name)[0]
  
    hide_main_ui()
    show_minigame_ui(background, exit_enabled)
    set_description(GAME_DESCRIPTIONS[name])
    
    config.overlay_functions.remove(minigame_ui_buttons)
    
    if name == "garden":
      show_garden()
      score = 0
    elif name == "lock":
      score = show_lock()
    elif name == "bottles":
      show_bottles()
      score = 0
    else:
      score = run_minigame(game_type=game, 
                           x=MINIGAME_POS_X, 
                           y=MINIGAME_POS_Y,
                           game_width=MINIGAME_WIDTH,
                           game_height=MINIGAME_HEIGHT,
                           game_high_score=persistent.unlocked_minigames[name][0],
                           level_number=level)
      update_high_score(name, score)
    
    config.overlay_functions.append(minigame_ui_buttons)
    
    hide_minigame_ui(background)
    config.overlay_functions.remove(minigame_description)
    show_main_ui()
    
    return score >= score_to_pass

  # Sets the current minigame description. Using a global variable here, because 
  # overlay functions can't take any parameters, and we need a way to modify the 
  # description displayed in the left (parchment) part of the screen.
  def set_description(description):
    global MINIGAME_DESCRIPTION
    MINIGAME_DESCRIPTION = description

    if minigame_description not in config.overlay_functions:
      config.overlay_functions.append(minigame_description)

    return
    
  # An UI element method that's appended to Renpy's UI stack (or whatever it is
  # called), removing the need of having to do this repeatedly in, say, the
  # garden, where Renpy interactions tend to clear all the screen elements after
  # a mouse click.
  def minigame_description():
    ui.frame(xpos=DESCRIPTION_POS_X, 
             ypos=DESCRIPTION_POS_Y, 
             xmaximum=DESCRIPTION_WIDTH, 
             background=None)
    ui.text("{size=-3}" + MINIGAME_DESCRIPTION + "{/size}")
    
    return
