init python:
  grid_x = 600
  grid_y = 200

image background_shop = "gfx/backgrounds/shop.png"

# shop_loop label. 
label shop_loop: 
  python: 
    button       = ""
    button_value = ""
    
    hide_main_ui()
    
    renpy.transition(dissolve)
    show_minigame_ui("background_shop", False)
    #config.overlay_functions.append(shop_buttons)
  
    while (True):
      # Did user select one of the items?
      if button == "item":
        if confirmation_window("buy item"):
          break
      elif button == "exit":
        break
      button = ui.interact()
      
    renpy.transition(dissolve)
    hide_minigame_ui("background_shop", False)
    #config.overlay_functions.remove(shop_buttons)
    
    show_main_ui()
  
  return
