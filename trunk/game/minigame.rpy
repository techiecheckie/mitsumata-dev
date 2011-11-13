init python:
  def show_minigame_screen():
    button = ""
    button_value = ""

    background = "bg riroom"
    show_minigame_ui(background, False)
  
    while True:
      ui.frame(xpos=0.4, ypos=0.2)
      ui.vbox()
      if minigame_mole:
        ui.textbutton("Whack-a-mole", ui.returns(WhackAMole))
      else:
        ui.text("Whack-a-mole")
      if minigame_cell:
        ui.textbutton("Cell", ui.returns(Cells))
      else:
        ui.text("Cell")
      if minigame_platformer:
        ui.textbutton("Platformer", ui.returns(Platformer))
      else:
        ui.text("Platformer")
      ui.close()
    
      button = ui.interact()
      if button == "exit":
        break
      else:
        score = run_minigame( game_type=button,
                              x=357, y=64,
                              game_width=650,
                              game_height=650 )
                            
        # if minigame_level == this and score > that
        #   unlock some bonus?
        
        print score

    hide_minigame_ui(background, False)
     
    return
  
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
    
