init python:
  def show_minigame_screen():
    button = ""
    button_value = ""

    background = "bg riroom"
    show_minigame_ui(background, False)
  
    while True:
      # A temporary button to start the molegame
      ui.frame(xpos=0.4, ypos=0.2)
      ui.textbutton("Whack-a-mole", ui.returns("molegame"))
    
      button = ui.interact()
      if button == "exit":
        break
      elif button == "molegame":
        score = run_minigame( WhackAMole, 370, 115 )
        # And do something with it...

    hide_minigame_ui(background, False)
     
    return