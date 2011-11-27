image background_shop = "gfx/backgrounds/shop.png"

init python:
  SHOP_ICON_X = 500
  SHOP_ICON_Y = 200
  SHOP_ROWS   = 3
  SHOP_COLS   = 3
  SHOP_CELL_WIDTH  = 120
  SHOP_CELL_HEIGHT = 120
  
  def add_items(items):
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

# shop_loop label. 
label shop_loop: 
  python: 
    button = ""
    items = inventory.get_items(decision, "shop") 
    
    hide_main_ui()
    renpy.transition(dissolve)
    show_minigame_ui("background_shop")
    
    while (True):
      add_items(items)

      # Did user select one of the items?
      if button == "exit":
        break
      elif button != "":
        if confirmation_window("buy item"):
          if button.get_id() not in persistent.unlocked_items:
            persistent.unlocked_items.append(button.get_id())
            #update_stats()
          break
      button = ui.interact()
    
    ui.clear()
    renpy.transition(dissolve)
    hide_minigame_ui("background_shop")
    show_main_ui()
  
  return
