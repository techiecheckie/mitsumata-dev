init python:
    
  from mitsugame.persistent_manager import Persistent_manager

    
  def shop_buttons():
    # item1 button
    ui.frame(xpos=68,ypos=133, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/items/generic_item.png", 
                   "gfx/items/generic_item_hover.png",
                   clicked=ui.returns(("buy_item", "item1_id")))
  
    # iitem2 button
    ui.frame(xpos=138,ypos=133, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/items/generic_item.png", 
                   "gfx/items/generic_item_hover.png",
                   clicked=ui.returns(("buy_item", "item2_id")))

    # exit shop
    ui.frame(xpos=42,ypos=709, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/shop_exit.png", 
                   "gfx/buttons/shop_exit_hover.png", 
                   clicked=ui.returns(("exit", "")))
    

image background_shop = "gfx/backgrounds/shop.png"

# shop_loop label. 
label shop_loop: 
  python:    
    button = ""
    button_value = ""
    
    hide_main_ui()
    
    renpy.transition(dissolve)
    renpy.show("background_shop")
    config.overlay_functions.append(shop_buttons)
  
    while (True):
      if button == "exit":
        break
        # buy confirmation
      elif button == "buy_item" :
              ui.frame(xpos=0.4, ypos=0.4)
              ui.vbox()
              ui.text("Are you sure you want to buy"+button_value+"?") 
              ui.textbutton("Yes", clicked=ui.returns(("", button_value)), xminimum=65)
              ui.textbutton("No", clicked=ui.returns(("", "")), xminimum=65)
              ui.close()
      button, button_value = ui.interact()
      
      # Is this a correct way to add item to inventory after buying?
      #
      # if persistent_manager.has_item(button_value) == False:
      #    persistent_manager.add_item(button_value)
          
      
      
    renpy.transition(dissolve)
    renpy.hide("background_shop")
    config.overlay_functions.remove(shop_buttons)
  
    show_main_ui(hp, mp)
  
  return
