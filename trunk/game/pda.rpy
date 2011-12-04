init python:
  
  from mitsugame.inventory import Inventory
  from mitsugame.journal_manager import Journal_manager

  # Item/journal icon/contents (grid) starting positions
  PDA_ICON_X = 270
  PDA_ICON_Y = 100
  PDA_CONTENT_X = 430
  PDA_CONTENT_Y = 110
  
  # icon size will be 150x150, so here's a slight padding
  PDA_ITEM_CELL_WIDTH  = 160
  PDA_ITEM_CELL_HEIGHT = 200
  
  # same here
  PDA_JOURNAL_CELL_WIDTH  = 150
  PDA_JOURNAL_CELL_HEIGHT = 200
  
  # item/journal grid
  PDA_COLS = 4
  PDA_ROWS = 3
  
  # preload inventory images
  items = inventory.get_inventory_items()
  for item in items:
    id = item.get_id()
    renpy.image("item_" + id,            "gfx/items/" + id + ".png")
    renpy.image("item_" + id + "_hover", "gfx/items/" + id + "_hover.png")
    
  # preload journal images
  journals = journal_manager.get_journals()
  for journal in journals:
    id = journal.get_id()
    renpy.image("journal_" + id,               "gfx/journals/" + id + ".png")
    renpy.image("journal_" + id + "_hover",    "gfx/journals/" + id + "_hover.png")
    renpy.image("journal_" + id + "_disabled", "gfx/journals/" + id + "_disabled.png")
    
  # create a transparent hover image for the item/journal icons
  renpy.image("pda_transparent", im.Scale("gfx/transparent.png", 150, 150))
  
  # this one is for the main menu buttons on the left
  renpy.image("pda_menu_transparent", im.Scale("gfx/transparent.png", 96, 96))
  
  renpy.image("pda_bg", "gfx/backgrounds/PDA_base.png")
  renpy.image("pda_glow", "gfx/backgrounds/PDA_glow.png")
 
  '''
  PDA buttons
  '''
  def pda_buttons():
    renpy.transition(Dissolve(0.5))
    # inventory button
    ui.frame(xpos=68,ypos=133, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("pda_menu_transparent",
                   "gfx/buttons/button_inventory_hover.png",
                   clicked=ui.returns(("inventory", None)))
    
    # journal button
    ui.frame(xpos=67,ypos=246, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("pda_menu_transparent",
                   "gfx/buttons/button_journal_hover.png", 
                   clicked=ui.returns(("journals", None)))
                   
    # power button
    ui.frame(xpos=43,ypos=49, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/button_power.png", 
                   "gfx/buttons/button_power_hover.png", 
                   clicked=ui.returns(("exit", None)))
    
    # training button
    ui.frame(xpos=66,ypos=502, xpadding=0, ypadding=0, background=None)
    if len(persistent.unlocked_minigames) > 0:
      ui.imagebutton("pda_menu_transparent",
                     "gfx/buttons/button_train_hover.png", 
                     clicked=ui.returns(("minigame", None)))
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
  def show_inventory(items, values, page):
    if values[0] == "inventory" or values[0] == "scroll":
      # Hide all the items (stupid workaround for hiding the items on other pages
      # when scrolling through the item list)
      #for item in items:
      #  renpy.hide("item_" + item.get_id())
    
      # Loop through the visible items, placing them in a grid formation
      for y in range(0, PDA_ROWS):
        for x in range(0, PDA_COLS):
          index = (page * PDA_COLS * PDA_ROWS) +  y * PDA_COLS + x
          if index >= len(items):
            break
          item = items[index]
          
          if x == 0 and y == 0:
            slide_delay = 0.0
          else:
            slide_delay = 1.0
          
          x_pos = PDA_ICON_X + x * PDA_ITEM_CELL_WIDTH
          y_pos = PDA_ICON_Y + y * PDA_ITEM_CELL_HEIGHT
          
          # Normal image. Doing it this way because we need a separate image to
          # be able to move it around later (that, and because I know of no other
          # way to do it.
          renpy.show("item_" + item.get_id(), 
                     at_list = [Position(xpos=x_pos, ypos=y_pos), 
                                Transform(anchor=(0.0,0.0))])

          # Hover frame with invisible normal image and proper hover image
          ui.frame(xpos=x_pos, ypos=y_pos, xpadding=0, ypadding=0, background=None)
          ui.imagebutton("pda_transparent", 
                         "item_" + item.get_id() + "_hover",
                         clicked=ui.returns(("item", item, slide_delay)))
      
    elif values[0] == "item":
      # values = ("item", Item, slide_delay)
      item = values[1]
 
      # First hide all the other images
      for displayed_item in items:
        if displayed_item != item:
          renpy.hide("item_" + displayed_item.get_id())
      
      renpy.show("item_" + item.get_id(), 
                 at_list = [pda_slide(PDA_ICON_X, PDA_ICON_Y)])
                 
      renpy.pause(values[2])

      ui.frame(xpos=PDA_ICON_X, ypos=PDA_ICON_Y, xpadding=0, ypadding=0, background=None)
      ui.imagebutton("pda_transparent", 
                     "item_" + item.get_id() + "_hover",
                     clicked=ui.returns(("inventory", "")))
      
      ui.frame(xpos=PDA_CONTENT_X, ypos=PDA_CONTENT_Y, 
               xpadding=0, ypadding=0, 
               xmaximum=520, xminimum=550,
               background=None)
      ui.text(item.get_name() + "\n\n" + item.get_description())
      
      
  # Displays the journal manager. Just like the inventory part, this one uses 
  # the button to decide what should be displayed.
  def show_journals(journals, values):
    if values[0] == "journals":
      for y in range(0, PDA_ROWS):
        for x in range(0, PDA_COLS):
          index = y * PDA_COLS + x
          if index >= len(journals):
            break
            
          journal = journals[index]
          
          if x == 0 and y == 0:
            slide_delay = 0.0
          else:
            slide_delay = 1.0
          
          x_pos = PDA_ICON_X + x * PDA_JOURNAL_CELL_WIDTH
          y_pos = PDA_ICON_Y + y * PDA_JOURNAL_CELL_HEIGHT
          
          renpy.show("journal_" + journal.get_id(), 
                     at_list = [Position(xpos=x_pos, ypos=y_pos), 
                                Transform(anchor=(0.0,0.0))])
          
          # Unnecessary complexity, but oh well..
          # This goes through the ids in persistent.unlocked_journals and checks
          # if any of those ids (xx:yy) match this journal's id (xx)
          journal_unlocked = False
          for id in persistent.unlocked_journals:
            if id.startswith(journal.get_id()):
              journal_unlocked = True
              break
          
          if not journal_unlocked:
            # Display the lock icon
            renpy.show("journal_" + journal.get_id() + "_disabled",
                       at_list = [Position(xpos=x_pos, ypos=y_pos), 
                                  Transform(anchor=(0.0,0.0))])
          else:
            # Display a clickable frame
            ui.frame(xpos=x_pos, ypos=y_pos, xpadding=0, ypadding=0, background=None)
            ui.imagebutton("pda_transparent", 
                           "journal_" + journal.get_id() + "_hover", 
                           clicked=ui.returns(("journal", journal, slide_delay)))
           
    elif values[0] == "journal":
      # Display the journal's titles 
      # values = ("journal", Journal, slide_delay)
      journal = values[1]
      entries = journal.get_entries()
      
      # Hide all the other images
      for displayed_journal in journals:
        if displayed_journal != journal:
          renpy.hide("journal_" + displayed_journal.get_id())
          renpy.hide("journal_" + displayed_journal.get_id() + "_disabled")
      
      renpy.show("journal_" + journal.get_id(), 
                 at_list = [pda_slide(PDA_ICON_X, PDA_ICON_Y)])
                 
      renpy.pause(values[2])
      
      ui.frame(xpos=PDA_ICON_X, ypos=PDA_ICON_Y, xpadding=0, ypadding=0, background=None)
      ui.imagebutton("pda_transparent",
                     "gfx/journals/" + journal.get_id() + "_hover.png",
                     clicked=ui.returns(("journals", "")))
      
      ui.frame(xpos=PDA_CONTENT_X, ypos=PDA_CONTENT_Y, background=None)
      ui.vbox()
      for entry in entries:
        for id in persistent.unlocked_journals:
          if id == journal.get_id() + ":" + entry.get_id():
            ui.textbutton(entry.get_title(), clicked=ui.returns(("entry", journal, entry)))
            break
      ui.close()
        
    # Display the entry's contents
    elif values[0] == "entry":
      journal = values[1]
      entry   = values[2]
      
      ui.frame(xpos=PDA_ICON_X, ypos=PDA_ICON_Y, xpadding=0, ypadding=0, background=None)
      ui.imagebutton("journal_" + journal.get_id(),
                     "journal_" + journal.get_id() + "_hover",
                     clicked=ui.returns(("journal", journal, 0)))
      
      ui.frame(xpos=PDA_CONTENT_X, ypos=PDA_CONTENT_Y, 
               xpadding=0, ypadding=0, 
               xmaximum=520, xminimum=520,
               background=None)
      ui.text(entry.get_title() + "\n" + entry.get_text())

  def hide_inventory(items):
    if inventory.is_enabled() == False:
      for item in items:
        renpy.hide("item_" + item.get_id())
        
  def hide_journals(journals):
    if journal_manager.is_enabled() == False:
      for journal in journals:
        renpy.hide("journal_" + journal.get_id())
        renpy.hide("journal_" + journal.get_id() + "_disabled")

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
    
    values = []
    
    renpy.transition(dissolve)
    renpy.show("pda_bg")
    renpy.show("pda_glow", at_list = [Position(xpos=159, ypos=9), Transform(anchor=(0.0, 0.0))])
    config.overlay_functions.append(pda_buttons)
  
    while (True):
      #print "waiting for input..."
      values = ui.interact()
      #print values
      
      if values[0] == "inventory" and values[1] == None:
        inventory.change_state()
        journal_manager.disable()
        hide_journals(journals)
        hide_inventory(items)
        if inventory.is_enabled():
          page = 0
          if max_page > 0:
            right_arrow = True
      elif values[0] == "journals" and values[1] == None:
        journal_manager.change_state()  
        inventory.disable()
        hide_inventory(items)
        hide_journals(journals)
      elif values[0] == "minigame":
        # hide everything PDA related and display the minigame ui instead
        renpy.transition(dissolve)
        renpy.hide("pda_bg")
        renpy.hide("pda_glow")
        config.overlay_functions.remove(pda_buttons)
        
        show_minigame_screen()
        
        renpy.transition(dissolve)
        renpy.show("pda_bg")
        renpy.show("pda_glow", at_list = [Position(xpos=159, ypos=9), Transform(anchor=(0.0, 0.0))])
        config.overlay_functions.append(pda_buttons)
      elif values[0] == "exit":
        break
      elif values[0] == "scroll":
        if values[1] == "next":
          page += 1
          if page == max_page:
            right_arrow = False
          left_arrow = True
          
          previous_page = page-1
          previous_page_start_index = previous_page * PDA_COLS * PDA_ROWS
          previous_page_end_index   = page * PDA_COLS * PDA_ROWS
          for i in range(previous_page_start_index, previous_page_end_index):
            if i == len(items):
              break
            renpy.hide("item_" + items[i].get_id())
        else:
          page -= 1
          if page == 0:
            left_arrow = False
          right_arrow = True
          
          next_page = page+1
          next_page_start_index = next_page * PDA_COLS * PDA_ROWS
          next_page_end_index   = (next_page+1) * PDA_COLS * PDA_ROWS
          for i in range(next_page_start_index, next_page_end_index):
            if i == len(items):
              break
            renpy.hide("item_" + items[i].get_id())
      
      if inventory.is_enabled():
        show_inventory(items, values, page)
      elif journal_manager.is_enabled():
        show_journals(journals, values)
      
    renpy.transition(dissolve)
    renpy.hide("pda_bg")
    renpy.hide("pda_glow")
    config.overlay_functions.remove(pda_buttons)
  
    show_main_ui()
  
  return
