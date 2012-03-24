label show_map:
  # Grab the current max click amount the player can use.
  $clicks_left = CLICKS + BONUS_CLICKS
  # A list of items that match the decision value.
  $items = inventory.get_items(decision, "map")
  # Hide the items in stashes all around the house.
  $hide_items(items)
        
  $renpy.transition(dissolve)
  $renpy.show("map")
  $hide_main_ui()
  
  # Start the map screen loop. 
  while (clicks_left > 0):
    $show_clicks(clicks_left)  
    $show_room_icons(decision)
      
    $room = ui.interact(suppress_overlay=True)
    # Temporary return check
    if room != "return":
      # See if an event should happen when entering the room
      call run_event
      # Break the loop if an event happened (= set tries to 0 because Renpy
      # doesn't understand words like "break" and such)
      if event_triggered:
        $clicks_left = 0
      else:
        $clicks_left = show_room(room, clicks_left)
    else:
     $clicks_left = 0
     
  if not event_triggered:
    # Display a message box before returning to the script
    $show_clicks(clicks_left)
    $renpy.pause(0.2)
    $show_message(SEARCH_END, "large")
    
  $renpy.transition(dissolve)
  $renpy.hide("map")
  $show_main_ui()  
  $update_stats()
  
  return
  
init python:
  import random
  from mitsugame.item import Item
  import xml.etree.ElementTree as xml
  
  # A dict containing all the rooms and their clickables
  CLICKABLES = {}
  # A tree containing all the room elements listed in rooms.xml
  ROOMS_XML = xml.parse(renpy.loader.transfn("../rooms.xml")).findall("room")
  
  # Some search messages for easier modification. Will have to do something "centralized" for all of
  # the messages used throughout the game, especially if there'll be some need to translate all this 
  # stuff to Japanese. 
  SEARCH_PROMPT = "Do you wish to take a closer look at this item?"
  YES = "Yes"
  NO  = "No"
  FOUND_NOTHING = "You found nothing of interest."
  FOUND_ITEM = "You found an item: "
  SEARCH_END = "'0 clicks left' message)"
  
  # Populates the CLICKABLES dict with clickables listed in rooms.xml. The elements in the
  # CLICKABLES dict are sub-dicts containing lists of all the clickables specified for that room.
  # Basically, the format is 
  #   CLICKABLES = { 
  #     "riroom" : { "stash_id" : {"click_count" : 0, "item": None }, "stash_id" : { ... } },
  #     "soroom" : { "misc_id"  : {"click_count" : 0               }, "stash_id" : { ... } },
  #     ...
  #   }
  # where each stash dict contains the click count and the possible item, and each misc clickable
  # contains only the click count. The click counts are used to control whether the player should
  # be allowed to search that stash again or if the misc clickable should display some other message
  # (defined in rooms.xml as description elements).
  def create_clickables():
    for room_node in ROOMS_XML:
      room_clickables_list = {}
      item_nodes = room_node.getchildren()
      for item_node in item_nodes:
        if item_node.tag == "stash":
          clickable_data = { "click_count" : 0, "item" : None }
        else:
          clickable_data = { "click_count" : 0 }
        room_clickables_list[item_node.get("id")] = clickable_data
          
      CLICKABLES[room_node.get("id")] = room_clickables_list
      
  def reset_clickables():
    room_keys = CLICKABLES.keys()
    for room_key in room_keys:
      clickable_keys = CLICKABLES[room_key].keys()
      for clickable_key in clickable_keys:
        clickable_data = CLICKABLES[room_key][clickable_key]
        clickable_data["click_count"] = 0
        if "item" in clickable_data:
          clickable_data["item"] = None
    return
  
  # Places items in different stashes all around the house based on what location values
  # they have been given in items.xml matching the current decision (nightly choice). 
  # Possible values for attributes "room" and "stash" are listed in rooms.xml, but they
  # can also be given "any" values. Any items with "any" values in either "room" or "stash"
  # are randomly placed, either randomizing the room AND stash, or only the stash. Currently
  # randomization is being tried for a maximum of three times, after which the item will be
  # ignored for the current search session (= not placed anywhere because all the stashes
  # were occupied). This could be easily remedied by re-randomizing the room, too, but nah,
  # that'll have to wait for later.
  def hide_items(items):
    if len(CLICKABLES.keys()) == 0:
      create_clickables()
    else:
      reset_clickables()
  
    # Grab the room keys for later use in item placement randomization
    room_keys = CLICKABLES.keys()
    
    for item in items:
      # Get the item's location information set in items.xml
      location = item.get_map_location(decision)
      
      # Randomize the room if the location is set to "any", else don't.
      if location["room"] != "any":
        room = CLICKABLES[location["room"]]
        
        # If the item is set to some specific stash, place it there, else randomize the stash
        if location["stash"] != "any":
          room[location["stash"]]["item"] = item
          print "Placed", item.get_name(), "to", location["room"], location["stash"]
        else:
          # Randomize the stash and grab the key for debugging purposes
          clickable_key = randomize_clickable(room, item)
          print "Randomly placed", item.get_name(), "to", location["room"], clickable_key
          
      else:
        # Randomize the room
        room_number = random.randint(0, len(room_keys)-1)
        room = CLICKABLES[room_keys[room_number]]
        
        # Randomize the stash and grab the key for debugging purposes
        clickable_key = randomize_clickable(room, item)
        print "Completely randomly placed", item.get_name(), "to", room_keys[room_number], clickable_key
    
    return
  
  # Places an item to one of the room's stashes, randomly choosing the stash until the item
  # fits into one of the stashes (= stash ain't occupied). Current implementation has been
  # set to fail if all three attempts to stash the item have been used. Items that fail are
  # then ignored for the rest of the search session.
  def randomize_clickable(room, item):
    clickable_keys = room.keys()
    rand_attempts = 3
    
    while rand_attempts > 0:
      # Randomize the stash
      clickable_number = random.randint(0, len(clickable_keys)-1)
      clickable_data = room[clickable_keys[clickable_number]]
      # Place the item in the stash if it ain't occupied, else roll again
      if "item" in clickable_data.keys() and clickable_data["item"] == None:
        room[clickable_keys[clickable_number]]["item"] = item
        return clickable_keys[clickable_number]
      
      print "  Clickable", clickable_keys[clickable_number], "occupied, trying again..."
      rand_attempts -= 1
    
    return "None, randomization failed"
  
  # Displays the amount of tries/clicks the player has.
  def show_clicks(clicks_left):
    ui.frame(xpos=25, ypos=723, xmaximum=50, ymaximum=50, background=None)
    ui.text('%d' % clicks_left, xfill=True, yfill=True)
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

    # Bathroom, TODO-note --> decision == "0" ??
    if decision == "7":
      ui.frame(xpos=566, ypos=382, xmaximum=91, ymaximum=115, xpadding=0, ypadding=0, background=None)
      ui.imagebutton("gfx/map/room_bathroom.png", "gfx/map/room_bathroom_hover.png", clicked=ui.returns("bathroom"))
    
    # Library    
    ui.frame(xpos=546, ypos=523, xmaximum=233, ymaximum=64, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/map/room_library.png", "gfx/map/room_library_hover.png", clicked=ui.returns("library"))
    
    return
    
  # Displays the room, selecting the proper background for the room and populating the screen
  # with clickables.
  def show_room(room, clicks_left):   
    renpy.transition(dissolve)
    # Room background names are defined in script.rpy.
    renpy.show("bg " + room, zorder=1)
    
    # Grab all the room's item nodes for clickables creation.
    item_nodes = None
    for room_node in ROOMS_XML:
      if room_node.get("id") == room:
        item_nodes = room_node.getchildren()
        break
    
    # Start the loop, repeating as long as there are clicks left or the player presses the
    # exit button to change the room.
    while (clicks_left > 0):
      show_room_clickables(room, item_nodes)
      show_clicks(clicks_left)
      
      selection = ui.interact(suppress_overlay=True, clear=False)
      if selection == "return":
        break
      else:
        clicks_left = show_info(selection, room, item_nodes, clicks_left)
        ui.clear()
      
    renpy.transition(dissolve)
    renpy.hide("bg " + room)
    ui.clear()
    
    return clicks_left
  
  # Creates clickables to the room using the info read from rooms.xml. There can be two
  # different kind of clickables: ones that can be searched (stashes) and ones that just
  # display maybe not-so-relevant information about the world. The information clickables
  # are invisible clickables, while stashes are the ones that highlight on mouse hover.
  def show_room_clickables(room, item_nodes):
    for item_node in item_nodes:
      id = item_node.get("id")
      x = int(item_node.get("x"))
      y = int(item_node.get("y"))
      
      if item_node.tag == "stash":
        ui.frame(xpos=x, ypos=y, background=None, xpadding=0, ypadding=0)
        ui.imagebutton("gfx/map/" + room + "/" + id + ".png",
                       "gfx/map/" + room + "/" + id + "_hover.png",
                       clicked=ui.returns(("stash", id)))
      else:
        xmax = int(item_node.get("xmax"))
        ymax = int(item_node.get("ymax"))
        
        ui.frame(xpos=x, ypos=y, xmaximum=xmax, ymaximum=ymax, background=None)
        ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(("misc", id)), background=None)
                     
    # Return button
    ui.frame(xpos=0, ypos=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_exit.png", "gfx/buttons/minigame_exit_hover.png", clicked=ui.returns("return"))
    
    return
  
  def show_info(selection, room, item_nodes, clicks_left):
    # FIXME: something returns 0 as selection when clicking at nothing, so find
    # out what that is and do something about it.
    if selection == 0:
      return clicks_left
    
    # Separate the info that came with the click
    (clickable_type, clickable_id) = selection
    # Use that info to get the clickable from the dict
    clickable_data = CLICKABLES[room][clickable_id]
    
    # Grab the clickable's rooms.xml node from the items sub-tree containing all the descriptions.
    selected_item_node = None
    for item_node in item_nodes:
      if item_node.get("id") == clickable_id:
        selected_item_node = item_node
        break 
    
    # Select the right description for the clickable. Two types: stashes have just the default one,
    # misc ones have several. The one that's supposed to be displayed depends on how many clicks
    # the misc clickable has already received.
    description = None
    if clickable_type == "stash":
      description = selected_item_node.text
    else:
      description_nodes = selected_item_node.findall("description")
      for description_node in description_nodes:
        click_count = int(description_node.get("level"))
        if clickable_data["click_count"] < click_count or description_node == description_nodes[len(description_nodes)-1]:
          description = description_node.text
          break
      
    # Display an info box about the clickable.
    renpy.transition(dissolve)
    ui.frame(xmaximum=520, 
             xpadding=40, ypadding=40, 
             xpos=0.5, ypos=0.5,
             xanchor = 265, yanchor=175,
             background="gfx/textbox.png")
    ui.vbox()
    ui.text("{size=-2}" + description + "{/size}")
    
    print "Clickable data:", clickable_data
    
    # Don't bother displaying search prompts if the clickable was a misc clickable or if the player
    # has already taken a look at the stash clickable.
    if clickable_data["click_count"] > 0 or clickable_type == "misc":
      ui.close()
      # Full screen hidden button, "click anywhere to continue" kind.
      ui.frame(xpos=0, ypos=0, background=None)
      ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("no"), background=None)
      clickable_data["click_count"] += 1
    else:
      ui.text("{size=-2}\n" + SEARCH_PROMPT + "{/size}")
      ui.textbutton("{size=-2}" + YES + "{/size}", clicked=ui.returns("yes"), xfill=True)
      ui.textbutton("{size=-2}" + NO + "{/size}", clicked=ui.returns("no"), xfill=True)
      ui.close()
      
    answer = ui.interact(clear=False)
    
    if answer == "yes":
      if clickable_data["item"] == None:
        show_message(FOUND_NOTHING, "large")
      else:
        item = clickable_data["item"]
      
        renpy.transition(dissolve)
        ui.frame(xmaximum=420, 
                 xpadding=40, ypadding=40, 
                 xpos=0.5, ypos=0.5,
                 xanchor = 265, yanchor=175,
                 background="gfx/textbox.png")
        
        ui.hbox(spacing=40)
        ui.text("{size=-2}" + FOUND_ITEM + item.get_name() + "\n\n" + item.get_description() + "{/size}")
        ui.image(im.Scale("gfx/items/" + item.get_id() + ".png", 100, 100))
        ui.close()
    
        show_invisible_button("full")
        
        # Do a silent unlock because we've displayed the item information already.
        unlock_item(item.get_id(), False)
        # Finally, clear the stash.
        clickable_data["item"] = None
      
      # Increase the stash's click count so that we know the player has searched this place before.
      clickable_data["click_count"] += 1
      
      # And reduce the overall click count so that the search event might end someday soon.
      clicks_left -= 1
    
    return clicks_left
