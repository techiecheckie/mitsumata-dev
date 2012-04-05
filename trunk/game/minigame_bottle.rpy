init python:
  renpy.image("winerack", "gfx/bottles/winerack.jpg")
    
  WINERACK_BOTTLE_LOCATIONS = [
    ( 98, 55),
    (231, 58),
    (366, 55),
    (480, 60),
    
    (116,244),
    (234,242),
    (362,243),
    (477,247),
    
    (107,436),
    (246,434),
    (377,437),
    (490,436)
  ]
  
  BOTTLES_CONFIRMATION = "Are you sure you want to select this bottle?\n\n"
  BOTTLES_RIDDLE = """{size=-3}
  One is at the 12
  Twelve is at the 1
  Three, Six, and Nine are
  correctly done.
  Two heads to 4
  Four heads to 8
  Five goes twice
  Ten is half late
  Number Eight ends the race
  And goes in the last spot
  on this face.
  
  From there your answer is
  easy at least
  Just choose the one North
  between South and East.
  {/size}"""

  def show_bottles():
    renpy.transition(dissolve)
    renpy.show("winerack",
               zorder=0,
               at_list = [Position(xpos=MINIGAME_POS_X, ypos=MINIGAME_POS_Y), 
                          Transform(anchor=(0.0, 0.0))])

    while True:
      # Riddle
      ui.frame(xpos=DESCRIPTION_POS_X, ypos=DESCRIPTION_POS_Y, background=None)
      ui.text(BOTTLES_RIDDLE)
      
      # Bottles
      for i in range(0,12):
        location = WINERACK_BOTTLE_LOCATIONS[i]
        ui.frame(xpos=MINIGAME_POS_X + location[0], 
                 ypos=MINIGAME_POS_Y + location[1], 
                 background=None,
                 xpadding=0,
                 ypadding=0)
        ui.imagebutton("gfx/bottles/bottle" + str(i+1) + ".png",
                       "gfx/bottles/bottle" + str(i+1) + "_hover.png",
                       clicked=ui.returns(i+1))
      
      # Shelf to cover to lower part of the highest bottles
      ui.frame(xpos=MINIGAME_POS_X + 41, 
               ypos=MINIGAME_POS_Y + 208, 
               background=None, 
               xpadding=0, 
               ypadding=0)
      ui.image("gfx/bottles/shelf.jpg")
    
      button = ui.interact(clear=False)
         
      if button == "exit":
        break
      else:
        # Confirm selection dialog
        renpy.transition(dissolve)
        ui.frame(xpos=MINIGAME_POS_X+50, 
                 ypos=MINIGAME_POS_Y+150, 
                 background="gfx/textbox.png",
                 xpadding=40,
                 ypadding=40,
                 xmaximum=520)
        ui.vbox()
        ui.text("{size=-2}" + BOTTLES_CONFIRMATION + "{/size}")
        ui.textbutton("{size=-2}" + YES + "{/size}", clicked=ui.returns("ok"), xfill=True)
        ui.textbutton("{size=-2}" + NO + "{/size}", clicked=ui.returns("cancel"), xfill=True)
        ui.close()
        
        confirm = ui.interact()
        renpy.transition(dissolve)
        
        if confirm == "ok":
          break
    
    # See if the correct choice was made
    if button == 2:
      #if "sake" not in persistent.unlocked_items:
      #  persistent.unlocked_items.append("sake")
      unlock_item("sake", False)
      
      item = inventory.get_item("sake")
      
      # Item unlocked message
      renpy.transition(dissolve)
      ui.frame(xmaximum=480, 
               xpadding=40, ypadding=40, 
               xpos=0.5, ypos=0.5, 
               xanchor=304, yanchor=95, 
               background="gfx/textbox_2.png")
        
      ui.hbox(spacing=40)
      ui.text("{size=-2}You found an item: " + item.get_name() + "\n\n" + item.get_description() + "{/size}")
      ui.image(im.Scale("gfx/items/" + item.get_id() + ".png", 100, 100))
      ui.close()
      
      show_invisible_button("full")
    
    renpy.transition(dissolve)
    renpy.hide("winerack")
    ui.clear()
    
    return
