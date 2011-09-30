image map = "gfx/backgrounds/map.png"
image riku_room = "gfx/backgrounds/Hall1.jpg"
image roman_room = "gfx/backgrounds/Hall1.jpg"
image soume_room = "gfx/backgrounds/Hall1.jpg"
image susa_room = "gfx/backgrounds/Hall1.jpg"
image hallway1 = "gfx/backgrounds/Hall1.jpg"
image hallway2 = "gfx/backgrounds/Hall1.jpg"
image kitchen = "gfx/backgrounds/Kitchen.jpg"
image bathroom = "gfx/backgrounds/Hall1.jpg"
image library = "gfx/backgrounds/Hall1.jpg"

init python:
  import random
  from mitsugame.item import Item
  
  # Places items in random stashes. stash_count is the amount of stashes in 
  # the selected room
  def stash_items(stashes, hideables):   
    randomly_placeables = []
    stashed_item_count = 0
    
    print "  Placing items with predefined locations:"
    for item in hideables:
      stash = item.get_current_stash()
      if stash != "any":
        stashes[stash] = item
        hideables.remove(item)
        stashed_item_count += 1
        print "    Placed", item.get_name(), "to", stash
        
    print "  Placing the rest of the items (if any) to any locations available:"
    for stash in stashes:
      if len(hideables) == 0:
        break
        
      if stashes[stash] == None:
        item = hideables.pop()
        stashes[stash] = item
        print "    Placed", item.get_name(), "to", stash 

  def show_stash_info(stashes, stash_name):
    if stashes[stash_name] != None:
      item = stashes.get(stash_name)
      
      inventory.unlock_item(item.get_id())
      info = "You found item '" + item.get_name() + "'."  
      
      # Clear the hiding place
      stashes[stash_name] = None
    else:
      info = "You found nothing."
      
    show_info_box(info + "\n\n (Click to hide)")    
  
  def show_tidbit_info(tidbit_name):
    info = "(Default extra clickable. Nothing special here yet.) \n\n (Click to hide)"
    
    show_info_box(info)
    
  def show_info_box(info):
    # Creates the info box    
    ui.detached()
    infobox = ui.frame(xpos=267, ypos=177, xmaximum=534, ymaximum=353, xpadding=40, ypadding=40, background="gfx/textbox.png")
    ui.vbox()
    ui.text(info)
    ui.close()
    
    # Creates a textbutton covering the whole infobox, sort of making the info box a clickable one 
    ui.detached()
    infobox_close = ui.frame(xpos=267, ypos=177, xmaximum=534, ymaximum=353, background=None)
    ui.textbutton("", xfill=True, yfill=True, background=None, clicked=ui.returns("close"))
    
    # Add the elements to the ui stack, and wait for the user to click on the box to make it disappear
    ui.add(infobox)
    ui.add(infobox_close)
    button = ""
    while button != "close":
      button = ui.interact(clear=False, suppress_overlay=True)
    ui.remove(infobox)
    ui.remove(infobox_close)
  
  
  
# The main label. Displays the room selection screen.
label nightly_search:  
  show map

  $overlays = []
  
  python:
    # Return button
    overlays.append(ui.frame(xpos=0.5, ypos=0.1, xanchor=0.5, yanchor=0.5))
    ui.textbutton("return", clicked=ui.returns("return"))
  
    # Riku's room
    overlays.append(ui.frame(xpos=266, ypos=205, xmaximum=98, ymaximum=73, xpadding=0, ypadding=0, background=None))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("riku"))
                   
    # Roman's room
    overlays.append(ui.frame(xpos=449, ypos=204, xmaximum=85, ymaximum=85, xpadding=0, ypadding=0, background=None))
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("roman"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("roman"))
    
    # Soume's room    
    overlays.append(ui.frame(xpos=265, ypos=328, xmaximum=93, ymaximum=95, xpadding=0, ypadding=0, background=None))
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("soume"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("soume"))
    
    # Susa's room
    overlays.append(ui.frame(xpos=387, ypos=318, xmaximum=171, ymaximum=88, xpadding=0, ypadding=0, background=None))
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("susa"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("susa"))
    
    # Hallway 1
    overlays.append(ui.frame(xpos=385, ypos=296, xmaximum=176, ymaximum=15, xpadding=0, ypadding=0, background=None))
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("hallway1"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("hallway1"))
    
    # Hallway 2
    overlays.append(ui.frame(xpos=685, ypos=366, xmaximum=17, ymaximum=158, xpadding=0, ypadding=0, background=None))
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("hallway2"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("hallway2"))
    
    # Kitchen
    overlays.append(ui.frame(xpos=464, ypos=437, xmaximum=77, ymaximum=83, xpadding=0, ypadding=0, background=None))
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("kitchen"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("kitchen"))
    
    # Bathroom
    overlays.append(ui.frame(xpos=588, ypos=387, xmaximum=91, ymaximum=115, xpadding=0, ypadding=0, background=None))
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("bathroom"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("bathroom"))
    
    # Library    
    overlays.append(ui.frame(xpos=549, ypos=542, xmaximum=233, ymaximum=64, xpadding=0, ypadding=0, background=None))
    #ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns("library"))
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns("library"))
  
  with dissolve
  
  # Without this the buttons will disappear once the dissolve above has finished (le fu?)
  # Guess how long it took to figure this out...
  python:
    for overlay in overlays:
      ui.add(overlay)
  
  $room = ui.interact()
  
  if room != "return":
    hide map 
    $ui.clear()
    with dissolve
    
    call show_room(room)
    
    if event_triggered == False:
      jump nightly_search
    else:
      return
  
  hide map
  $ui.clear()
  with dissolve
  
  return


  
label show_room(room):
  $print "Entering room " + room + ", decision " + decision + "..."

  call run_event(decision, room)
  if event_triggered == True:
    $print "  Triggered an event. Returning to main script..."
    return
  else:
    $print "  No event triggered. Continuing..."
    
  # Get the locked items (that match the decision and room)
  $hideables = inventory.get_available_items(decision, room)
  $print "    Hid", len(hideables), "items."
  
  $overlays = []

  # Stash items and activate the room specific overlays
  if room == "riku":
    # Define the empty local stashes
    $stashes = {"closet": None, "cupboard": None, "carpet": None, "bed": None}
    
    # Populate the stashes
    $stash_items(stashes, hideables)
    
    # Show the room
    show riku_room
    
    python:
      # Stashes
      # Riku's bed
      overlays.append(ui.frame(xpos=340, ypos=620, xpadding=0, ypadding=0, background=None))
      ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns(("stash","bed")))
    
      # Riku's closet
      overlays.append(ui.frame(xpos=120, ypos=300, xpadding=0, ypadding=0, background=None))
      ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns(("stash","closet")))
  
      # Riku's carpet
      overlays.append(ui.frame(xpos=520, ypos=500, xpadding=0, ypadding=0, background=None))
      ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns(("stash","carpet")))
  
      # Riku's cupboard
      overlays.append(ui.frame(xpos=720, ypos=200, xpadding=0, ypadding=0, background=None))
      ui.imagebutton("gfx/block.png", "gfx/block_hover.png", clicked=ui.returns(("stash","cupboard")))      
      
      # Static clickables
      # Test clickable
      overlays.append(ui.frame(xpos=320, ypos=200, xmaximum=50, ymaximum=200, xpadding=0, ypadding=0))
      ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(("tidbit","")))
  elif room == "roman":
    #$stashes = {}
    #$stash_items(stashes, hideables)
    show roman_room
    #$config.overlay_functions.append(roman_overlays)
  elif room == "soume":
    #$stash_items(4)
    show soume_room
  elif room == "susa":
    #$stash_items(4)
    show susa_room
  elif room == "hallway1":
    #$stash_items(4)
    show hallway1
  elif room == "hallway2":
    #$stash_items(4)    
    show hallway2
  elif room == "kitchen":
    #$stash_items(4)
    show kitchen
  elif room == "bathroom":
    #$stash_items(4)
    show bathroom
  elif room == "library":
    #$stash_items(4)
    show library
  
  # Return button
  $overlays.append(ui.frame(xpos=0.5, ypos=0.1, xanchor=0.5, yanchor=0.5))
  $ui.textbutton("return", clicked=ui.returns(("return", "")))
  
  # Show everything with a fade-in
  with dissolve
  
  python:
    # Restore the overlays after the dissolve
    for overlay in overlays:
      ui.add(overlay)
  
    # Wait for user input in a loop
    clicked_type, clicked_name = ui.interact(clear=False)
    while True:
      if clicked_type == "return":
        break
      elif clicked_type == "stash":
        show_stash_info(stashes, clicked_name)
      else:
        show_tidbit_info(clicked_name)
      clicked_type, clicked_name = ui.interact(clear=False)
    
    # When done with the loop, remove all the overlays by clearing the ui stack
    ui.clear()
  
  hide riku_room
  hide roman_room
  hide soume_room
  hide susa_room
  hide hallway1
  hide hallway2
  hide kitchen
  hide bathroom
  hide library
  with dissolve
  
  return