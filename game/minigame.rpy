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
                            
        # if minigame_level == this and score > that
        #   unlock some bonus?
        
        print score

    hide_minigame_ui(background, False)
     
    return
  
  def run(button):
    if button == "mole":
      game = WhackAMole
    elif button == "cell":
      game = Cells
    elif button == "platformer":
      game = Platformer
      
    score = run_minigame( game_type=game,
                          x=357, y=64,
                          game_width=650,
                          game_height=650 )
    
    return score    
  
  # running minigames without starting the pda first
  def minigame(game, level):
    show_minigame_ui(None, False)
    score = run_minigame(game_type = game, 
                         x=357, y=64,
                         game_width=650,
                         game_height=650,
                         level_number = level)
    hide_minigame_ui(None, False)
    return score
    
