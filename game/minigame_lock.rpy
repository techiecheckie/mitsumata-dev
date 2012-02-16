init python:

  renpy.image("lock", "gfx/lock/lock.jpg")
  renpy.image("lock_transparent", im.Scale("gfx/transparent.png", 71, 81))
  renpy.image("lock_hover", "gfx/lock/lock_button_hover.png")
  renpy.image("lock_reflection", "gfx/lock/lock_button_reflection.png")
  
  LOCK_BUTTON_POSITIONS = [
    (118, 309),
    (225, 310),
    (332, 310),
    (439, 310),
    
    (118, 419),
    (225, 419),
    (332, 419),
    (439, 419)
  ]
  
  LOCK_LEVELS = [
    (4, (1,3,8,9), "Start in the Middle of Winter.\n\nJump To the First of Spring.\n\nHead to the End of Summer.\n\nOn the Cusp of Autumn's Wing."),
    (6, (1,2,3,4,5,6), "Another test riddle")
  ]
  
  def show_lock():
    #level = persistent.unlocked_minigames["lock"][1]
    level = 2
    level_settings = LOCK_LEVELS[level-1]
    numbers = [1]*level_settings[0]
    score = 0
  
    renpy.transition(dissolve)
    renpy.show("lock", 
               zorder=-1,
               at_list = [Position(xpos=MINIGAME_POS_X, ypos=MINIGAME_POS_Y), 
                          Transform(anchor=(0.0, 0.0))])
    
    while True:
      ui.frame(xpos=DESCRIPTION_POS_X, ypos=DESCRIPTION_POS_Y, background=None)
      ui.text("{size=-3}" + level_settings[2] + "{/size}")
      
      for i in range(0, 8):
        position = LOCK_BUTTON_POSITIONS[i]
        if i < len(numbers):
          ui.frame(xpos=MINIGAME_POS_X + position[0], ypos=MINIGAME_POS_Y + position[1], background=None, xpadding=0, ypadding=0)
          ui.image("gfx/lock/number_" + str(numbers[i]) + ".png")
        
          ui.frame(xpos=MINIGAME_POS_X + position[0], ypos=MINIGAME_POS_Y + position[1], background=None, xpadding=0, ypadding=0)
          ui.imagebutton("lock_transparent",
                         "lock_hover",
                         clicked=ui.returns(i))
        
        ui.frame(xpos=MINIGAME_POS_X + position[0], ypos=MINIGAME_POS_Y + position[1], background=None, xpadding=0, ypadding=0)
        ui.image("gfx/lock/lock_button_reflection.png")
    
      button = ui.interact()
         
      if button == "exit":
        break
      else:
        number = numbers[button]
        number += 1
        if number > 12:
          number = 1
        numbers[button] = number
        
        solved = True
        for i in range(0, len(numbers)):
          if numbers[i] != level_settings[1][i]:
            solved = False
            break
            
        if solved:
          renpy.transition(dissolve)
          renpy.transition(dissolve)
          ui.frame(xpos=MINIGAME_POS_X+50, 
                   ypos=MINIGAME_POS_Y+150, 
                   background="gfx/textbox.png",
                   xpadding=40,
                   ypadding=40,
                   xmaximum=520)
          ui.text("You found the right combination and managed to open the lock.\n\nClick to continue.")
          
          # Full screen hidden button, "click anywhere to continue" kind
          ui.frame(xpos=0, ypos=0, background=None)
          ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
      
          ui.interact()
          renpy.transition(dissolve)
          
          score = 1
          
          break
          

    renpy.transition(dissolve)
    renpy.hide("lock")
    ui.clear()
    
    return score
