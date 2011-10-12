label show_map:
  # A dict containing the rooms and their items
  $rooms = { 
    "riroom" : { "cupboard" : None, "closet" : None, "bed" : None }, 
    "roroom" : { "stash1" : None, "stash2" : None }, 
    "soroom" : { "stash1" : None, "stash2" : None, "stash3" : None }, 
    "suroom" : { "stash1" : None, "stash2" : None, "stash3" : None }, 
    "hall1" : { "stash1" : None, "stash2" : None }, 
    "hall2" : { "stash1" : None, "stash2" : None, "stash3" : None }, 
    "kitchen" : { "stash1" : None, "stash2" : None, "stash3" : None }, 
    "bathroom" : { "stash1" : None, "stash2" : None, "stash3" : None }, 
    "lib" : { "stash1" : None, "stash2" : None, "stash3" : None } 
  }

  # A list of items that match the decision value
  $items = inventory.get_available_items(decision)
  
  python:  
    # If an item has a place set (items.xml) for this decision, put that item
    # in the room where it is supposed to be. Otherwise randomize the room
    for item in items:
      #  location [0]          [1]            [2]
      # <location decision="1" room="riroom"  stash="any" />
      location = item.get_location(decision)
      if location[1] != "any":
        stash_list = rooms[location[1]]
        keys = stash_list.keys()
        for key in keys:
          if stash_list[key] == None:
            stash_list[key] = item
            break
        
        
      else:
        random_item_list = rooms[rooms.keys()[random.randint(0, len(rooms)-1)]]
        #random_item_list.append(item)
        
    renpy.transition(dissolve)
    renpy.show("map")
    
    # See how many tries the player has (TODO)
    tries = 3
    
  # Start the map screen loop. 
  while (tries > 0):
    $show_tries(tries)  
    $show_room_icons(decision)
      
    $room = ui.interact(suppress_overlay=True)
    # Temporary return check
    if room != "return":
      # See if an event should happen when entering the room
      call run_event
      # Break the loop if an event happened. (... set tries to 0 because Renpy
      # doesn't understand words like "break" and such)
      if event_triggered:
        $tries = 0
      else:
       $tries = show_room(room, decision, tries, rooms[room])
    else:
     $tries = 0
    
  # Display a message box before returning to the script
  $show_tries(tries)
  $renpy.pause(0.2)
    
  $renpy.transition(dissolve)
  $renpy.show("textbox", at_list=[Position(xpos=0.5, ypos=0.5), Transform(anchor=(0.5,0.5))])
  $show_tries(tries)
    
  $ui.frame(xpos=0.3, ypos=0.35, background=None)
  if event_triggered:
    $message = "(Post-event message)"
  else:
    $message = "(\"0 tries left\" message)"
  $ui.text(message + "\n\nClick to continue...")
    
  $ui.frame(xpos=0, ypos=0, background=None)
  $ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
  $ui.interact(suppress_overlay=True)
    
  $renpy.transition(dissolve)
  $renpy.hide("textbox")
  $renpy.hide("map")
    
  return
  
init python:
  import random
  from mitsugame.item import Item
  
  # Displays the amount of tries/clicks the player has.
  def show_tries(tries):
    ui.frame(xpos=25, ypos=723, xmaximum=50, ymaximum=50, background=None)
    ui.text('%d' % tries, xfill=True, yfill=True)
      
    return
    
  def show_room_icons(decision):
    # Riku's room
    ui.frame(xpos=266, ypos=205, xmaximum=98, ymaximum=73, xpadding=0, ypadding=0, background=None)
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("riroom"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("riroom"))
                   
    # Roman's room
    ui.frame(xpos=449, ypos=204, xmaximum=85, ymaximum=85, xpadding=0, ypadding=0, background=None)
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("roroom"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("roroom"))
    
    # Soume's room    
    ui.frame(xpos=265, ypos=328, xmaximum=93, ymaximum=95, xpadding=0, ypadding=0, background=None)
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("soroom"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("soroom"))
    
    # Susa's room
    ui.frame(xpos=387, ypos=318, xmaximum=171, ymaximum=88, xpadding=0, ypadding=0, background=None)
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("suroom"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("suroom"))
    
    # Hallway 1
    ui.frame(xpos=385, ypos=296, xmaximum=176, ymaximum=15, xpadding=0, ypadding=0, background=None)
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("hall1"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("hall1"))
    
    # Hallway 2
    ui.frame(xpos=685, ypos=366, xmaximum=17, ymaximum=158, xpadding=0, ypadding=0, background=None)
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("hall2"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("hall2"))
    
    # Kitchen
    ui.frame(xpos=464, ypos=437, xmaximum=77, ymaximum=83, xpadding=0, ypadding=0, background=None)
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("kitchen"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("kitchen"))
    
    # Bathroom
    if decision == "something":
      ui.frame(xpos=588, ypos=387, xmaximum=91, ymaximum=115, xpadding=0, ypadding=0, background=None)
      #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("bathroom"))
      ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("bathroom"))
    
    # Library    
    ui.frame(xpos=549, ypos=542, xmaximum=233, ymaximum=64, xpadding=0, ypadding=0, background=None)
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("lib"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("lib"))
    
    # Return
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("Temporary cancel button", clicked=ui.returns("return"))
    
    return
    
  def show_room(room, decision, tries, items):   
    renpy.transition(dissolve)
    renpy.show("bg " + room)
    # room background names defined in script.rpy
    
    while (tries > 0):
      show_room_clickables(room)
      show_tries(tries)
      
      selection = ui.interact(suppress_overlay=True, clear=False)
      if selection == "return":
        break
      else:
        tries = show_info(selection, items, tries)
      
    renpy.transition(dissolve)
    renpy.hide("bg " + room)
    ui.clear()
    
    return tries
    
  def show_room_clickables(room):
    if room == "riroom":
      # Riku room item containers
      # Cupboard
      ui.frame(xpos=100, ypos=100, background=None)
      ui.textbutton("item", clicked=ui.returns(("stash", "cupboard")))
      
      # Closet
      ui.frame(xpos=200, ypos=100, background=None)
      ui.textbutton("item", clicked=ui.returns(("stash", "closet")))
      
      # Bed
      ui.frame(xpos=300, ypos=100, background=None)
      ui.textbutton("item", clicked=ui.returns(("stash", "bed")))
      
      # ...
      
      # Riku room tidbit containers
      ui.frame(xpos=100, ypos=200, background=None)
      ui.textbutton("tidbit", clicked=ui.returns(("tidbit", "1")))
 
      ui.frame(xpos=200, ypos=200, background=None)
      ui.textbutton("tidbit", clicked=ui.returns(("tidbit", "2")))
      
    elif room == "roroom":
      pass
    elif room == "suroom":
      pass
 
    # Return button
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("Return", clicked=ui.returns("return"))
    
    return
    
  def show_info(selection, items, tries):
    # First, check what info should be displayed
    if selection[0] == "tidbit":
      message = "You found a tidbit box.\n\nTidbits are listed in tidbits.xml,\nand are waiting for implementation."
    else:
      item = items[selection[1]]
      if item == None:
        message = "You found nothing of interest"
      else:
        message = "You found an item!\n\nItem name: " + item.get_name()
        item.unlock()
        items[selection[1]] = None
      
      # Not every click is going to reduce this number, but this works just
      # fine for now
      tries -= 1
  
    # Show the info box
    renpy.transition(dissolve)
    renpy.show("textbox", at_list=[Position(xpos=0.5, ypos=0.5), Transform(anchor=(0.5,0.5))])
    
    ui.frame(xpos=0.3, ypos=0.3, background=None)
    ui.text(message + "\n\n(Click to continue.)")
    
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
    ui.interact(suppress_overlay=True)
    
    renpy.transition(dissolve)
    renpy.hide("textbox")
    
    return tries