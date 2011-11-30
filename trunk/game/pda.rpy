init python:
  
  from mitsugame.inventory import Inventory
  from mitsugame.journal_manager import Journal_manager

  # Item/journal icon/contents (grid) starting positions
  PDA_ICON_X = 270
  PDA_ICON_Y = 100
  PDA_CONTENT_X = 430
  PDA_CONTENT_Y = 100
  
  # icon size will be 150x150, so here's a slight padding
  PDA_ITEM_CELL_WIDTH  = 160
  PDA_ITEM_CELL_HEIGHT = 160
  
  PDA_JOURNAL_CELL_WIDTH  = 150
  PDA_JOURNAL_CELL_HEIGHT = 200
  
  # item/journal grid
  PDA_COLS = 4
  PDA_ROWS = 3
  
  def pda_buttons():
    renpy.transition(Dissolve(0.5))
    # inventory button
    ui.frame(xpos=68,ypos=133, xpadding=0, ypadding=0, background=None)
    ui.imagebutton(im.Scale("gfx/transparent.png", 96, 96),
                   "gfx/buttons/button_inventory_hover.png",
                   clicked=ui.returns(("inventory", "change state")))
    
    # journal button
    ui.frame(xpos=67,ypos=246, xpadding=0, ypadding=0, background=None)
    ui.imagebutton(im.Scale("gfx/transparent.png", 96, 96),
                   "gfx/buttons/button_journal_hover.png", 
                   clicked=ui.returns(("journal manager", "change state")))
                   
    # power button
    ui.frame(xpos=43,ypos=49, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/button_power.png", 
                   "gfx/buttons/button_power_hover.png", 
                   clicked=ui.returns(("exit", "")))
    
    # training button
    ui.frame(xpos=66,ypos=502, xpadding=0, ypadding=0, background=None)
    if len(persistent.unlocked_minigames) > 0:
      ui.imagebutton(im.Scale("gfx/transparent.png", 96, 96),
                     "gfx/buttons/button_train_hover.png", 
                     clicked=ui.returns(("minigame", "")))
    else:
      ui.image("gfx/buttons/button_train_disabled.png")
                   
    # bonus button
    ui.frame(xpos=68,ypos=622, xpadding=0, ypadding=0, background=None)
    ui.image("gfx/buttons/button_bonus_disabled.png")
    
    # right arrow
    ui.frame(xpos=113,ypos=361, xpadding=0, ypadding=0, background=None)
    if right_arrow:
      ui.imagebutton("gfx/buttons/button_arrow_right.png", 
                     "gfx/buttons/button_arrow_right_hover.png", 
                     clicked=ui.returns(("scroll", "next")))
    else:
      ui.image("gfx/buttons/button_arrow_right_disabled.png")
    
    #left arrow
    ui.frame(xpos=32,ypos=361, xpadding=0, ypadding=0, background=None)
    if left_arrow:
      ui.imagebutton("gfx/buttons/button_arrow_left.png", 
                     "gfx/buttons/button_arrow_left_hover.png", 
                     clicked=ui.returns(("scroll", "prev")))
    else:
      ui.image("gfx/buttons/button_arrow_left_disabled.png")
    
    # PDA screen gloss
    ui.frame(xpos=195, ypos=44, background=None)
    ui.image("gfx/backgrounds/PDA_gloss.png")
    
    
  # Displays the inventory. The content (an item grid or a screen showing more 
  # specific item information) is based on what button was previously pressed. 
  def show_inventory(items, button, button_value, page):
    if button == "inventory" or button == "scroll":
      
      for y in range(0, PDA_ROWS):
        for x in range(0, PDA_COLS):
          index = (page * PDA_COLS * PDA_ROWS) +  y * PDA_COLS + x
          if index >= len(items):
            break
            
          item = items[index]
          
          x_pos = PDA_ICON_X + x * PDA_ITEM_CELL_WIDTH
          y_pos = PDA_ICON_Y + y * PDA_ITEM_CELL_HEIGHT
          
          ui.frame(xpos=x_pos, ypos=y_pos, 
                   xpadding=0, ypadding=0, 
                   background=None)
          ui.imagebutton("gfx/items/" + item.get_id() + ".png", 
                         "gfx/items/" + item.get_id() + "_hover.png", 
                         clicked=ui.returns(("item", item)))
      
    elif button == "item":
      item = button_value
      ui.frame(xpos=PDA_ICON_X, ypos=PDA_ICON_Y, 
               xpadding=0, ypadding=0, 
               background=None)
      ui.imagebutton("gfx/items/" + item.get_id() + ".png",
                     "gfx/items/" + item.get_id() + "_hover.png",
                     clicked=ui.returns(("inventory", "")))
      
      ui.frame(xpos=PDA_CONTENT_X, ypos=PDA_CONTENT_Y, 
               xpadding=0, ypadding=0, 
               xmaximum=550, xminimum=550,
               background=None)
      ui.text(button_value.get_description()) # button_value == item
      
      
  # Displays the journal manager. Just like the inventory part, this one uses 
  # the button to decide what should be displayed.
  def show_journal_manager(journals, button, button_value, page):
    if button == "journal manager":
      for y in range(0, PDA_ROWS):
        for x in range(0, PDA_COLS):
          index = y * PDA_COLS + x
          if index >= len(journals):
            break
            
          journal = journals[index]
          
          x_pos = PDA_ICON_X + x * PDA_JOURNAL_CELL_WIDTH
          y_pos = PDA_ICON_Y + y * PDA_JOURNAL_CELL_HEIGHT
          
          ui.frame(xpos=x_pos, ypos=y_pos, xpadding=0, ypadding=0)
          
          # unnecessary complexity, but oh well..
          journal_unlocked = False
          for id in persistent.unlocked_journals:
            if id.startswith(journal.get_id()):
              journal_unlocked = True
              break
              
          if not journal_unlocked:
            ui.image("gfx/journals/" + journal.get_id() + "_disabled.png")
          else:
            ui.imagebutton("gfx/journals/" + journal.get_id() + ".png", 
                           "gfx/journals/" + journal.get_id() + "_hover.png", 
                           clicked=ui.returns(("journal", journal)))
           
    # Display the journal's titles 
    elif button == "journal":
      journal = button_value
      
      if journal != None:
        ui.frame(xpos=PDA_ICON_X, ypos=PDA_ICON_Y, xpadding=0, ypadding=0)
        ui.imagebutton("gfx/journals/" + journal.get_id() + ".png",
                       "gfx/journals/" + journal.get_id() + "_hover.png",
                       clicked=ui.returns(("journal manager", "")))
      
        entries = button_value.get_entries()
        
        ui.frame(xpos=PDA_CONTENT_X, ypos=PDA_CONTENT_Y)
        ui.vbox()
        for entry in entries:
          for id in persistent.unlocked_journals:
            if id == journal.get_id() + ":" + entry.get_id():
              ui.textbutton(entry.get_title(), clicked=ui.returns(("entry", (journal, entry))))
              break
        ui.close()
        
    # Display the entry's contents
    elif button == "entry":
      # button_value == tuple
      journal = button_value[0]
      entry = button_value[1]
      
      ui.frame(xpos=PDA_ICON_X, ypos=PDA_ICON_Y, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/journals/" + journal.get_id() + ".png",
                     "gfx/journals/" + journal.get_id() + ".png",
                     clicked=ui.returns(("journal", journal)))
      
      ui.frame(xpos=PDA_CONTENT_X, ypos=PDA_CONTENT_Y, 
               xpadding=0, ypadding=0, 
               xmaximum=520, xminimum=520,
               background=None)
      ui.vbox()
      ui.text(entry.get_title())
      ui.text(entry.get_text())        
      ui.close()
     
     
        
image pda_bg = "gfx/backgrounds/PDA_base.png"
image pda_glow = "gfx/backgrounds/PDA_glow.png"

# PDA loop label. 
label pda_loop: 
  python:
    hide_main_ui()

    journals = journal_manager.get_journals()    
    items    = inventory.get_unlocked_items()
    
    left_arrow  = False
    right_arrow = False
    page        = 0
    max_page    = len(items)/(PDA_COLS*PDA_ROWS)
    
    button       = ""
    button_value = ""
    
    renpy.transition(dissolve)
    renpy.show("pda_bg")
    renpy.show("pda_glow", at_list = [Position(xpos=159, ypos=9), Transform(anchor=(0.0, 0.0))])
    config.overlay_functions.append(pda_buttons)
  
    while (True):
      if button == "exit":
        break
      elif button == "minigame":
        renpy.transition(dissolve)
        renpy.hide("pda_bg")
        renpy.hide("pda_glow")
        config.overlay_functions.remove(pda_buttons)
        
        show_minigame_screen()
        
        renpy.transition(dissolve)
        renpy.show("pda_bg")
        renpy.show("pda_glow", at_list = [Position(xpos=159, ypos=9), Transform(anchor=(0.0, 0.0))])
        config.overlay_functions.append(pda_buttons)
        
      elif button_value == "change state":
        if button == "inventory":
          inventory.change_state()
          journal_manager.disable()
        else:
          journal_manager.change_state()
          inventory.disable()
        page       = 0
        left_arrow = False
        if inventory.is_enabled() and len(items) > PDA_COLS * PDA_ROWS:
          right_arrow = True
        else:
          right_arrow = False
        
      elif button == "scroll":
        if button_value == "next":
          page += 1
          if page == max_page:
            right_arrow = False
          left_arrow = True
        else:
          page -= 1
          if page == 0:
            left_arrow = False
          right_arrow = True
          
        
      # Do display stuff
      if inventory.is_enabled():
        show_inventory(items, button, button_value, page)
      elif journal_manager.is_enabled():
        show_journal_manager(journals, button, button_value, page)
    
      #print "waiting for input..."
      button, button_value = ui.interact()
      #print "", button, ":", button_value
      
    renpy.transition(dissolve)
    renpy.hide("pda_bg")
    renpy.hide("pda_glow")
    config.overlay_functions.remove(pda_buttons)
  
    show_main_ui()
  
  return
