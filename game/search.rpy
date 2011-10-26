label show_map:
  # A dict containing the rooms and their items (as mentioned in the GDD)
  $rooms = { 
    "riroom" : { "equipment" : None, "clothes" : None, "trophies" : None, "posters" : None },
    "soroom" : { "plants" : None, "vines" : None, "hairclips" : None, "jewelry" : None, "nailpolish" : None, "clothes" : None }, 
    "suroom" : { "tv" : None, "games" : None, "burner" : None, "scrolls" : None }, 
    "roroom" : { "sculpture" : None, "plant1" : None, "plant2" : None }
    
    #"hall1" : { "stash1" : None, "stash2" : None }, 
    #"hall2" : { "stash1" : None, "stash2" : None, "stash3" : None }, 
    #"kitchen" : { "stash1" : None, "stash2" : None, "stash3" : None }, 
    #"bathroom" : { "stash1" : None, "stash2" : None, "stash3" : None }, 
    #"lib" : { "stash1" : None, "stash2" : None, "stash3" : None } 
  }

  # A list of items that match the decision value
  $items = inventory.get_items(decision, "map") 
  
  python:  
    # If an item has a place set (items.xml) for this decision, put that item
    # in the room where it is supposed to be. Otherwise randomize the room
    for item in items:
      location = item.get_map_location(decision)
      
      if location["room"] != "any":
        stash_list = rooms[location["room"]]
        stash_keys = stash_list.keys()

        # Place the item to the first free stash. If the item has a stash set
        # for the current decision, ignore that for now.
        for stash_key in stash_keys:
          if stash_list[stash_key] == None:
            stash_list[stash_key] = item
            break
            
      else:     
        # Try randomizing the spot three times before breaking the loop.
        #
        # Could do something smarter here, like removing full stashes from the 
        # list or even putting the items to the first available stash, but 
        # that'll have to be seen to later.
        rand_attempts = 3
        while (rand_attempts > 0):
          # Get a random room key
          room_key = rooms.keys()[random.randint(0, len(rooms)-1)]
          # Get its stash list and grab a random stash key from it
          stashes = rooms[room_key]
          stash_key = stashes.keys()[random.randint(0, len(stashes)-1)]
          # Place the item in the stash (if it is empty, otherwise try again)
          if stashes[stash_key] == None:
            stashes[stash_key] = item
            break
            
          rand_attempts -= 1
        
    renpy.transition(dissolve)
    renpy.show("map")
    hide_main_ui()
       
    current_tries = tries
       
  # Start the map screen loop. 
  while (current_tries > 0):
    $show_tries(current_tries)  
    $show_room_icons(decision)
      
    $room = ui.interact(suppress_overlay=True)
    # Temporary return check
    if room != "return":
      # See if an event should happen when entering the room
      call run_event
      # Break the loop if an event happened. (... set tries to 0 because Renpy
      # doesn't understand words like "break" and such)
      if event_triggered:
        $current_tries = 0
      else:
       $current_tries = show_room(room, decision, tries, rooms[room])
    else:
     $current_tries = 0
    
  # Display a message box before returning to the script
  $show_tries(tries)
  $renpy.pause(0.2)
  
  if event_triggered:
    $message = "(Post-event message)"
  else:
    $message = "(\"0 tries left\" message)"
    
  $show_message(message, "large")
    
  $renpy.transition(dissolve)
  $renpy.hide("map")
  $show_main_ui()  
  
  return
  
init python:
  import random
  from mitsugame.item import Item
  
  # Displays the amount of tries/clicks the player has.
  def show_tries(current_tries):
    ui.frame(xpos=25, ypos=723, xmaximum=50, ymaximum=50, background=None)
    ui.text('%d' % current_tries, xfill=True, yfill=True)
      
    return
    
  def show_room_icons(decision):
    # Riku's room
    ui.frame(xpos=262, ypos=202, xmaximum=98, ymaximum=73, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/map/room_riku.png", "gfx/map/room_riku_hover.png", clicked=ui.returns("riroom"))
                   
    # Roman's room
    ui.frame(xpos=445, ypos=202, xmaximum=85, ymaximum=85, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/map/room_roman.png", "gfx/map/room_roman_hover.png", clicked=ui.returns("roroom"))

    # Kitchen
    ui.frame(xpos=343, ypos=429, xmaximum=77, ymaximum=83, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/map/room_kitchen.png", "gfx/map/room_kitchen_hover.png", clicked=ui.returns("kitchen"))
    
    # Soume's room    
    ui.frame(xpos=265, ypos=323, xmaximum=93, ymaximum=95, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/map/room_soume.png", "gfx/map/room_soume_hover.png", clicked=ui.returns("soroom"))
    
    # Susa's room
    ui.frame(xpos=383, ypos=312, xmaximum=171, ymaximum=88, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/map/room_susa.png", "gfx/map/room_susa_hover.png", clicked=ui.returns("suroom"))
    
    # Hallway 1
    ui.frame(xpos=385, ypos=295, xmaximum=176, ymaximum=15, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/map/room_hall1.png", "gfx/map/room_hall1_hover.png", clicked=ui.returns("hall1"))
    
    # Hallway 2
    ui.frame(xpos=686, ypos=383, xmaximum=17, ymaximum=158, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/map/room_hall2.png", "gfx/map/room_hall2_hover.png", clicked=ui.returns("hall2"))

    # Bathroom
    if decision == "0":
      ui.frame(xpos=566, ypos=382, xmaximum=91, ymaximum=115, xpadding=0, ypadding=0, background=None)
      ui.imagebutton("gfx/map/room_bathroom.png", "gfx/map/room_bathroom_hover.png", clicked=ui.returns("bathroom"))
    
    # Library    
    ui.frame(xpos=546, ypos=523, xmaximum=233, ymaximum=64, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/map/room_library.png", "gfx/map/room_library_hover.png", clicked=ui.returns("lib"))
    
    # Return
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("Temporary cancel button", clicked=ui.returns("return"))
    
    return
    
  def show_room(room, decision, current_tries, items):   
    renpy.transition(dissolve)
    renpy.show("bg " + room, zorder=1)
    # room background names defined in script.rpy
    
    while (current_tries > 0):
      show_room_clickables(room)
      show_tries(tries)
      
      selection = ui.interact(suppress_overlay=True, clear=False)
      if selection == "return":
        break
      else:
        current_tries = show_info(selection, items, current_tries)
      
    renpy.transition(dissolve)
    renpy.hide("bg " + room)
    ui.clear()
    
    return current_tries
    
  def show_room_clickables(room):
    if room == "riroom":
      # Riku room item containers
      #"riroom" : { "equipment" : None, "clothes" : None, "trophies" : None, "posters" : None },

      # Cupboard
      ui.frame(xpos=100, ypos=100, background=None)
      ui.textbutton("item", clicked=ui.returns(("stash", "equipment")))
      
      # Closet
      ui.frame(xpos=200, ypos=100, background=None)
      ui.textbutton("item", clicked=ui.returns(("stash", "clothes")))
      
      # Bed
      ui.frame(xpos=300, ypos=100, background=None)
      ui.textbutton("item", clicked=ui.returns(("stash", "trophies")))
      
      # Bed
      ui.frame(xpos=400, ypos=100, background=None)
      ui.textbutton("item", clicked=ui.returns(("stash", "posters")))
      
      # ...
      
      # Riku room tidbit containers
      ui.frame(xpos=100, ypos=200, background=None)
      ui.textbutton("tidbit", clicked=ui.returns(("tidbit", "1")))
 
      ui.frame(xpos=200, ypos=200, background=None)
      ui.textbutton("tidbit", clicked=ui.returns(("tidbit", "2")))
      
    elif room == "roroom":    
      #"roroom" : { "stash1" : None, "stash2" : None }, 
      pass
    elif room == "suroom":
      #"soroom" : { "plants" : None, "vines" : None, "hairclips" : None, "jewelry" : None, "nailpolish" : None, "clothes" : None } 
      pass
 
    # Return button
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("Return", clicked=ui.returns("return"))
    
    return
    
  def show_info(selection, items, current_tries):
    # First, check what info should be displayed
    if selection[0] == "tidbit":
      message = "You found a tidbit."
    else:
      item = items[selection[1]]
      if item == None:
        message = "You found nothing of interest."
      else:
        message = "You found an item." + "\n\n" + item.get_name()
        item.unlock()
        update_stats(item.get_bonuses())
        
        items[selection[1]] = None
        
      
      # Not every click is going to reduce this number, but this works just
      # fine for now
      current_tries -= 1
  
    # Show the info box
    # show_message_window(message)
    
    show_message(message, "large")
    
    return current_tries
