init python:
  
  from mitsugame.inventory import Inventory
  from mitsugame.journal_manager import Journal_manager
  from mitsugame.persistent_manager import Persistent_manager

  button = ""
  button_value = ""

  # Item/journal icon/contents positions (TODO, etc.)
  icon_x = 270
  icon_y = 100
  content_x = 370
  content_y = 100
    
  def enable_main_buttons():
    # inventory button
    ui.frame(xpos=68,ypos=133, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/button_inventory.png", 
                   "gfx/buttons/button_inventory_hover.png", 
                   clicked=ui.returns(("inventory", "change state")))
    
    # journal button
    ui.frame(xpos=67,ypos=246, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/button_journal.png", 
                   "gfx/buttons/button_journal_hover.png", 
                   clicked=ui.returns(("journal manager", "change state")))
                   
    # power button
    ui.frame(xpos=43,ypos=49, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/button_power.png", 
                   "gfx/buttons/button_power_hover.png", 
                   clicked=ui.returns(("exit", "")))
    
    # training button
    ui.frame(xpos=66,ypos=502, xpadding=0, ypadding=0, background=None)
    ui.image("gfx/buttons/button_train_disabled.png")
    #ui.imagebutton("gfx/buttons/button_train.png", 
    #               "gfx/buttons/button_train_hover.png", 
    #               clicked=ui.returns(("train", "")))
                   
    # bonus button
    ui.frame(xpos=68,ypos=622, xpadding=0, ypadding=0, background=None)
    ui.image("gfx/buttons/button_bonus_disabled.png")
    #ui.imagebutton("gfx/buttons/button_bonus.png", 
    #               "gfx/buttons/button_bonus_hover.png", 
    #               clicked=ui.returns(("bonus", "")))
    
    # right arrow
    ui.frame(xpos=113,ypos=361, xpadding=0, ypadding=0, background=None)
    ui.image("gfx/buttons/button_arrow_right_disabled.png")
    #ui.imagebutton("gfx/buttons/button_bonus.png", 
    #               "gfx/buttons/button_bonus_hover.png", 
    #               clicked=ui.returns(("bonus", "")))
    
    # left arrow
    ui.frame(xpos=32,ypos=361, xpadding=0, ypadding=0, background=None)
    ui.image("gfx/buttons/button_arrow_left_disabled.png")
    #ui.imagebutton("gfx/buttons/button_bonus.png", 
    #               "gfx/buttons/button_bonus_hover.png", 
    #               clicked=ui.returns(("bonus", "")))
    
  # Displays the inventory. The content (an item grid or a screen showing more 
  # specific item information) is based on what button was previously pressed. 
  #
  # TODO: proper grid and info placement, etc. Transitions, too. And proper item
  # icons.
  def show_inventory():
    if button == "inventory":
      items = inventory.get_items()

      ui.frame(xpos=icon_x, ypos=icon_y, xpadding=0, ypadding=0)
      ui.grid(cols=3, rows=1, xfill=False, yfill=False, transpose=False, xmaximum = 400)
      for item in items:
        if item.is_locked():
          ui.image("gfx/items/generic_item_disabled.png")
        else:        
          ui.imagebutton("gfx/items/generic_item.png", 
                         "gfx/items/generic_item_hover.png", 
                         clicked=ui.returns(("item", item.get_id())))
      ui.close()
    elif button == "item":
      item = inventory.get_item(button_value)

      ui.frame(xpos=icon_x, ypos=icon_y, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/items/generic_item.png",
                     "gfx/items/generic_item_hover.png",
                     clicked=ui.returns(("inventory", "")))
      
      ui.frame(xpos=content_x, ypos=content_y, xpadding=0, ypadding=0, xmaximum=550, xminimum=550)
      ui.text(item.get_description())
      
      
  # Displays the journal manager. Just like the inventory part, this one uses 
  # the button to decide what should be displayed.
  #
  # TODO: proper placement, use proper journal icons
  def show_journal_manager():
    # Display the journal icons
    if button == "journal manager":
      journals = journal_manager.get_journals()
        
      ui.frame(xpos=icon_x, ypos=icon_y, xpadding=0, ypadding=0)
      ui.grid(cols=3, rows=1, xfill=False, yfill=False, transpose=False, xmaximum = 400)
      for journal in journals:
        if journal.is_locked():
          ui.image("gfx/buttons/journal_char.png")
        else:
          ui.imagebutton("gfx/buttons/journal_char" + journal.get_id() + ".png", 
                         "gfx/buttons/journal_char_hover.png", 
                         clicked=ui.returns(("journal", journal.get_id())))
      ui.close()
      
    # Display the journal's titles 
    elif button == "journal":
      journal = journal_manager.get_journal(button_value)
      if journal != None:
        ui.frame(xpos=icon_x, ypos=icon_y, xpadding=0, ypadding=0)
        ui.imagebutton("gfx/buttons/journal_char" + journal.get_id() + ".png",
                       "gfx/buttons/journal_char_hover.png",
                       clicked=ui.returns(("journal manager", "")))
      
        entries = journal.get_entries()
        
        ui.frame(xpos=content_x, ypos=content_y)
        ui.vbox()
        for entry in entries:
          if not entry.is_locked():
            ui.textbutton(entry.get_title(), clicked=ui.returns(("entry", entry.get_id())))
        ui.close()
        
    # Display the entry's contents
    elif button == "entry":
      journal = journal_manager.get_selected_journal()
      entry = journal.get_entry(button_value)
      
      ui.frame(xpos=icon_x, ypos=icon_y, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/buttons/journal_char" + journal.get_id() + ".png",
                     "gfx/buttons/journal_char_hover.png",
                     clicked=ui.returns(("journal", journal.get_id())))
      
      ui.frame(xpos=content_x, ypos=content_y, xpadding=0, ypadding=0, xmaximum=520, xminimum=520)
      ui.text(entry.get_text())

        
image background_pda = "gfx/backgrounds/palm_pilot_bg.png"        


# PDA loop label. 
label pda_loop:
  show background_pda
  while (True):
    $enable_main_buttons()

    # Do button stuff
    if button == "exit":
      return
    elif button == "inventory":
      if button_value == "change state":
        $inventory.change_state()
        $journal_manager.disable()
    elif button == "journal manager":
      if button_value == "change state":
        $journal_manager.change_state()
        $inventory.disable()
    
    # Do display stuff
    if inventory.is_enabled():
      $show_inventory()
    elif journal_manager.is_enabled():
      $show_journal_manager()
    
    #$print "waiting for input..."
    $button, button_value = ui.interact()
    #$print "", button, ":", button_value