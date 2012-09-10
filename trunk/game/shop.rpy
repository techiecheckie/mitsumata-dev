init python:
  renpy.image("shop_background", "gfx/backgrounds/Store.png")

  # Shop grid settings
  SHOP_ICON_X = 500
  SHOP_ICON_Y = 200
  SHOP_ROWS   = 3
  SHOP_COLS   = 3
  SHOP_CELL_WIDTH  = 120
  SHOP_CELL_HEIGHT = 120
  
  def create_grid(items):
    for y in range(0, SHOP_ROWS):
      for x in range(0, SHOP_COLS):
        index = y * SHOP_COLS + x
        if index >= len(items):
          break
            
        item = items[index]
          
        x_pos = SHOP_ICON_X + x * SHOP_CELL_WIDTH
        y_pos = SHOP_ICON_Y + y * SHOP_CELL_HEIGHT
          
        ui.frame(xpos=x_pos, ypos=y_pos, xpadding=0, ypadding=0)
        ui.imagebutton(im.Scale("gfx/items/" + item.get_id() + ".png", 100, 100), 
                       im.Scale("gfx/items/" + item.get_id() + "_hover.png", 100, 100), 
                       clicked=ui.returns(item))

label shop_loop: 
  python: 
    items = inventory.get_items(decision, "store") 
    
    hide_main_ui()
    show_minigame_ui("shop_background", False)
    
    if len(items) == 0:
      show_message("DEBUG: No shop items for decision value %s. Press any key to continue." % decision, "large")
    else:    
      while True:
        create_grid(items)
        
        # Shop text
        ui.frame(xpos=DESCRIPTION_POS_X, ypos=DESCRIPTION_POS_Y, background=None)
        ui.text("Shop message")
        
        button = ui.interact(clear=False)
  
        if button == "exit":
          break
        elif button != "":
          # Display item information and confirmation buttons in a box
          renpy.transition(dissolve)
          ui.frame(xpos=MINIGAME_POS_X+50, 
                   ypos=MINIGAME_POS_Y+150, 
                   background="gfx/textbox.png",
                   xpadding=40,
                   ypadding=40,
                   xmaximum=530)
          
          ui.hbox(spacing=20)
          ui.image(im.Scale("gfx/items/" + button.get_id() + ".png", 100, 100))
          ui.text("{size=-3}" + button.get_name() + "\n\n" + button.get_description() + "\n\n{/size}")
          ui.close()
          
          ui.frame(xpos=MINIGAME_POS_X + 50,
                   ypos=MINIGAME_POS_Y + 300,
                   background=None,
                   xpadding=40,
                   ypadding=40,
                   xmaximum=530)
          ui.vbox()
          ui.text("\n\n{size=-3}Are you sure you want to buy this item?{/size}")
          ui.textbutton("Ok", clicked=ui.returns(True), xfill=True)
          ui.textbutton("Cancel", clicked=ui.returns(False), xfill=True)
          ui.close()
          
          accepted = ui.interact()
          renpy.transition(dissolve)
          
          if accepted:
            create_grid(items)
            renpy.transition(dissolve)
            ui.frame(xpos=MINIGAME_POS_X+50, 
                     ypos=MINIGAME_POS_Y+150, 
                     background="gfx/textbox.png",
                     xpadding=40,
                     ypadding=40,
                     xmaximum=530)
            ui.hbox(spacing=20)
            ui.image(im.Scale("gfx/items/" + button.get_id() + ".png", 100, 100))
            ui.text("{size=-3}Item bought: " + button.get_name() + ".\n\nThe shopkeeper waves you goodbye as you leave the store.{/size}")
            ui.close()
          
            show_invisible_button("full")
        
            unlock_item(button.get_id(), False)
            update_stats()
            update_minigame_ui(HP, MP)
          
            break
    
    ui.clear()
    hide_minigame_ui("shop_background")
    show_main_ui()
  
  return
