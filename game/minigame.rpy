init python:

  def show_minigame_screen():
    button       = ""
    button_value = ""

    background = "bg riroom"
    show_minigame_ui(background, False)
  
    while True:
      ui.frame(xpos=0.4, ypos=0.2)
      ui.vbox()
      for minigame in persistent.unlocked_minigames:
        ui.imagebutton("gfx/buttons/minigame_" + minigame + ".png",
                       "gfx/buttons/minigame_" + minigame + "_hover.png",
                       clicked=ui.returns(minigame))
      ui.close()
    
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
    #elif name == "power":
    #  game = MagicPower
    #elif name == "squats":
    #  game = Squats
    
    return game
  
  
  def run(name):
    score = run_minigame( game_type = choose_game(name),
                          x=357, y=64,
                          game_width=650,
                          game_height=650 )
                          # level_number = persistent.minigame_level[name] )
  
  
  def update_high_score(game, score):
    if game in persistent.minigame_scores:
      print "Comparing old score"
      if score > persistent.minigame_scores[game]:
        persistent.minigame_scores[game] = score
        print "New high score"
    else:
      persistent.minigame_scores[game] = score
      print "Putting new score"
      
      
  # running minigames without starting the pda first
  def minigame(name, level, score_to_pass):
    show_minigame_ui(None, False)
    
    score = run_minigame(game_type = choose_game(name), 
                         x=357, y=64,
                         game_width=650,
                         game_height=650,
                         level_number = level)
    update_high_score(name, score)
    
    # update max level? (when playing through the PDA)
    # current_level = persistent.minigame_level[name]
    # if score >= score_to_pass and current_level < level:
    #   persistent.minigame_level[name] = level
    
    hide_minigame_ui(None, False)
    
    return score >= score_to_pass
