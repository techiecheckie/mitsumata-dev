image map = "gfx/backgrounds/map_new_1.jpg"
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
        
  def check_stash(stashes, stash_id):
    if stashes[stash_id] != None:
      item = stashes.get(stash_id)
      
      inventory.unlock_item(item.get_id())
      info = "You found item '" + item.get_name() + "'."  
      
      # Clear the hiding place
      stashes[stash_id] = None
      
    else:
      info = "You found nothing."
      
    # Temporary confirmation dialog
    ui.frame(xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5)
    ui.vbox()
    ui.text(info)
    ui.textbutton("Ok", clicked=ui.returns(""))
    ui.close()
    
    ui.interact()
          
  def riku_overlays():
    # Riku's bed
    ui.frame(xpos=340, ypos=620, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png",
                   "gfx/block_hover.png",
                   clicked=ui.returns("bed"))
    
    # Riku's closet
    ui.frame(xpos=120, ypos=300, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png",
                   "gfx/block_hover.png",
                   clicked=ui.returns("closet"))
  
    # Riku's carpet
    ui.frame(xpos=520, ypos=500, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png",
                   "gfx/block_hover.png",
                   clicked=ui.returns("carpet"))
  
    # Riku's cupboard
    ui.frame(xpos=720, ypos=200, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png",
                   "gfx/block_hover.png",
                   clicked=ui.returns("cupboard"))
                   
  def hallway1_overlays():
    # the table on the left
    #ui.at(fadein(1.0))
    ui.frame(xpos=240, ypos=620, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png",
                   "gfx/block_hover.png",
                   clicked=ui.returns("asdf"))
                    
    # lamp 1
    #ui.at(fadein(1.0))
    ui.frame(xpos=520, ypos=100, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png",
                   "gfx/block_hover.png",
                   clicked=ui.returns("qwer"))
    
    # lamp 2
    #ui.at(fadein(1.0))
    ui.frame(xpos=520, ypos=200, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png",
                   "gfx/block_hover.png",
                   clicked=ui.returns("zxcv"))
                   
  def return_overlay():
    # Temporary return button for all the screens
    ui.frame(xpos=0.5, ypos=0.1, xanchor=0.5, yanchor=0.5)
    ui.textbutton("return", clicked=ui.returns("return"))
  

# The main label. Displays the room selection screen.
label nightly_search:
  call hide_ui

  # Show the room selection map
  show map with dissolve # at Position(xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5)
  
  # Clickable room icons
  python:
    ui.frame(xpos=0.5, ypos=0.1, xanchor=0.5, yanchor=0.5)
    ui.textbutton("return", clicked=ui.returns("return"))
    
    # Riku's room
    ui.frame(xpos=274, ypos=235, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png", 
                   "gfx/block_hover.png",
                   clicked=ui.returns("riku"))
                   
    # Roman's room
    ui.frame(xpos=452, ypos=234, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png", 
                   "gfx/block_hover.png",
                   clicked=ui.returns("roman"))
    
    # Soume's room    
    ui.frame(xpos=282, ypos=353, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png", 
                   "gfx/block_hover.png",
                   clicked=ui.returns("soume"))
    
    # Susa's room
    ui.frame(xpos=429, ypos=359, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png", 
                   "gfx/block_hover.png",
                   clicked=ui.returns("susa"))
    
    # Hallway 1
    ui.frame(xpos=428, ypos=296, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png", 
                   "gfx/block_hover.png",
                   clicked=ui.returns("hallway1"))
    
    # Hallway 2
    ui.frame(xpos=686, ypos=398, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png", 
                   "gfx/block_hover.png",
                   clicked=ui.returns("hallway2"))
    
    # Kitchen
    ui.frame(xpos=604, ypos=442, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png", 
                   "gfx/block_hover.png",
                   clicked=ui.returns("kitchen"))
    
    # Bathroom
    ui.frame(xpos=461, ypos=474, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png", 
                   "gfx/block_hover.png",
                   clicked=ui.returns("bathroom"))
    
    # Library    
    ui.frame(xpos=642, ypos=561, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png", 
                   "gfx/block_hover.png",
                   clicked=ui.returns("library"))
     
  # Wait for the input
  $room = ui.interact()
  
  if room != "return":
    call show_room(room)
  
  hide map with dissolve
  call show_ui
 
  return
  
# Prepares a room for displaying. Basically this label places all the available
# items (read: locked & available during the night/decision) in random stashes 
# all around the room, preparing everything for the recursive show_room label.
label show_room(room):
  python:
    # This value actually comes from somewhere else
    decision = "3"
    
    # Get the locked items (that match the decision and room) for hiding
    print "Building a list of locked items and entries to hide (decision " + decision + ", room " + room + "...)"
    hideables = inventory.get_available_items(decision, room)
    #entries = journal_manager.get_locked_entries(hideables, room)
    #print "  Found", len(items), "items and", len(entries), "entries."
    print "  Found", len(hideables), "hideable items."
    
  # Stash items and activate the room specific overlays
  if room == "riku":
    # TODO: launch an event (if any)
    
    # Define the empty local stashes
    $stashes = {"closet": None, "cupboard": None, "carpet": None, "bed": None}
    # Populate the stashes
    $stash_items(stashes, hideables)
    # Display background
    show riku_room
    # Add clickables as overlays
    $config.overlay_functions.append(riku_overlays)
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
  
  $config.overlay_functions.append(return_overlay)
  with dissolve
  
  # First wait for user input, then do it in a loop  
  $clicked = ui.interact()
  while clicked != "return":
    $check_stash(stashes, clicked)
    $clicked = ui.interact()
  
  # Most likely not the best way to remove the room's overlays, but what the hell,
  # I don't know shite.
  if room == "riku":
    $config.overlay_functions.remove(riku_overlays)
  #elif room == "roman":
  #  $config.overlay_functions.remove(roman_overlays)
  #elif room == "soume":
  #  $config.overlay_functions.remove(soume_overlays)
  #elif room == "susa":
  #  $config.overlay_functions.remove(susa_overlays)
  elif room == "hallway1":
    $config.overlay_functions.remove(hallway1_overlays)
  #elif room == "hallway2":
  #  $config.overlay_functions.remove(hallway2_overlays)
  #elif room == "kitchen":
  #  $config.overlay_functions.remove(kitchen_overlays)
  #elif room == "bathroom":
  #  $config.overlay_functions.remove(bathroom_overlays)
  #elif room == "library":
  #  $config.overlay_functions.remove(library_overlays)
    
  $config.overlay_functions.remove(return_overlay)

  # Hide all the displayed images when done.
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