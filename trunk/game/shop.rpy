init python:
  renpy.image("shop_background", "gfx/backgrounds/Store.png")

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
    button = ""
    items = inventory.get_items(decision, "shop") 
    
    hide_main_ui()
    renpy.transition(dissolve)
    show_minigame_ui("shop_background")
    
    while (True):
      create_grid(items)
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
          if button.get_id() not in persistent.unlocked_items:
            persistent.unlocked_items.append(button.get_id())
            update_stats()
            update_minigame_ui(HP, MP)
            renpy.pause(1.0)
          break
    
    ui.clear()
    renpy.transition(dissolve)
    hide_minigame_ui("background_shop")
    show_main_ui()
  
  return
