init python:

  renpy.image("lock", "gfx/lock/lock.jpg")

#It should say the riddle when in that parchment area, btw. I'll send the images 
#later this evening.

#Start in the Middle of Winter.
#Jump to the First of Spring.
#Head to the End of Summer.
#On the Cusp of Autumn's Wing.

#The bottom four slots won't be used with this.

#The answer will be Jan, Mar, Aug, and Sept, in that order, in the top slots on the lock.
  LOCK_RIDDLES = [
    "Start in the Middle of Winter.\n\nJump To the First of Spring.\n\nHead to the End of Summer.\n\nOn the Cusp of Autumn's Wing."
  ]
  
  def show_lock():
    renpy.transition(dissolve)
    renpy.show("lock", at_list = [Position(xpos=MINIGAME_POS_X, ypos=MINIGAME_POS_Y-40), Transform(anchor=(0.0, 0.0))], zorder=-1)
    
    while True:
      ui.frame(xpos=DESCRIPTION_POS_X, ypos=DESCRIPTION_POS_Y, background=None)
      ui.text("{size=-3}" + LOCK_RIDDLES[0] + "{/size}")
    
      button = ui.interact()
         
      if button == "exit":
        break
      else:
        pass
    
    renpy.transition(dissolve)
    renpy.hide("lock")
    ui.clear()
    
    
    
    return