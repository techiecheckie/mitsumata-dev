init python:
  renpy.image("shop_background", "gfx/backgrounds/Store.png")
  
  SHOP_MESSAGE = "Insert shop message here."
  SHOP_CONFIRMATION = "Are you sure you want to buy this item?"
  SHOP_ACCEPT = "Ok"
  SHOP_DECLINE = "Cancel"
  SHOP_BOUGHT = "Item bought:"
  SHOP_LEAVING = "The shopkeeper waves you goodbye as you leave the store."

  # Shop grid settings
  SHOP_ICON_X = 500
  SHOP_ICON_Y = 200
  SHOP_ROWS   = 3
  SHOP_COLS   = 3
  SHOP_CELL_WIDTH  = 120
  SHOP_CELL_HEIGHT = 120
  
  # Creates a 3x3 grid of clickable items representing the shop's collection of
  # currently available items for the player to choose from.
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
    # Disable the rollback feature to stop the player from being able to go back
    # and think again about entering the shop. (Move to the script instead? Strange
    # things can/will happen if enabled, so might as well do it here, too.)
    config.rollback_enabled = False
  
    # Grab the items from the inventory that are supposed to be offered during this
    # decision.
    items = inventory.get_items(decision, "store") 
    
    # Display the minigame ui with shop background and disabled exit button.
    hide_main_ui()
    show_minigame_ui("shop_background", False)
    
    if len(items) == 0:
      show_message("DEBUG: No shop items for decision value %s. Press any key to continue." % decision, "large")
    else:    
      # Create the shop grid using the available item list.
      create_grid(items)
      # Put some text to the left side of the minigame ui. Contents?
      ui.frame(xpos=DESCRIPTION_POS_X, ypos=DESCRIPTION_POS_Y, background=None)
      ui.text("{size=-3}" + SHOP_MESSAGE + "{/size}")
      
      # Repeat until the player has decided to buy an item.
      while True:
        # Wait for user input.
        button = ui.interact(clear=False)
  
        # Display item information and buy confirmation buttons in the same box.
        renpy.transition(dissolve)
        buy_confirmation = ui.frame(xpos=MINIGAME_POS_X+50, 
                 ypos=MINIGAME_POS_Y+150, 
                 background="gfx/textbox.png",
                 xpadding=40,
                 ypadding=40,
                 xmaximum=530)
 
        ui.vbox()
        ui.hbox(spacing=20)
        ui.null(height=190)
        ui.image(im.Scale("gfx/items/" + button.get_id() + ".png", 100, 100))
        ui.text("{size=-3}" + button.get_name() + "\n\n" + button.get_description() + "{/size}")
        ui.close()
        ui.text("{size=-3}" + SHOP_CONFIRMATION + "{/size}")
        ui.textbutton(SHOP_ACCEPT, clicked=ui.returns(True), xfill=True)
        ui.textbutton(SHOP_DECLINE, clicked=ui.returns(False), xfill=True)
        ui.close()

        # Wait for the player to press either "Ok" or "Cancel", ignoring any other
        # buttons (like the other items in the background. Yes, they're still active...) 
        while True:
          accepted = ui.interact(clear=False, suppress_overlay = True)
          if accepted == True or accepted == False:
            break
        
        renpy.transition(dissolve)
        ui.remove(buy_confirmation)
        
        if accepted:
          # Display some "post-payment" message to the player to make sure they know
          # what they've bought.
          ui.frame(xpos=MINIGAME_POS_X+50, 
                   ypos=MINIGAME_POS_Y+150, 
                   background="gfx/textbox.png",
                   xpadding=40,
                   ypadding=40,
                   xmaximum=530)
          ui.hbox(spacing=20)
          ui.null(height=190)
          ui.image(im.Scale("gfx/items/" + button.get_id() + ".png", 100, 100))
          ui.text("{size=-3}" + SHOP_BOUGHT + " " + button.get_name() + ".\n\n" + SHOP_LEAVING + "{/size}")
          ui.close()
          
          # Make sure the player has to click before proceeding.
          show_invisible_button("full")
  
          # Do the necessary updates and unlocks (if any) before breaking the shop loop.     
          unlock_item(button.get_id(), False)
          update_stats()
          update_minigame_ui(HP, MP)
             
          break

    ui.clear()
    hide_minigame_ui("shop_background")
    show_main_ui()
    
    config.rollback_enabled = True
  return
