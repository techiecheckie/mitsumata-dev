image floormap_big = "gfx/map/floormap_big.jpg"
image hall1 = "gfx/backgrounds/Hall1.jpg"
image kitchen = "gfx/backgrounds/Kitchen.jpg"

init python:
  import random

# The main label. Displays the room selection screen.
label room_selection:
  call hide_ui

  # Show the room selection map
  show floormap_big at Position(xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) behind ui, mp_background, hp_background with dissolve
  
  # Create the clickable rooms (just one for now)
  python:
    ui.frame(xpos=0.5, ypos=0.1, xanchor=0.5, yanchor=0.5)
    ui.textbutton("return", clicked=ui.returns("return"))
    
    ui.frame(xpos=412, ypos=215, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png", 
                   "gfx/block_hover.png",
                   clicked=ui.returns("hall1"))
                   
    ui.frame(xpos=512, ypos=315, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/block.png", 
                   "gfx/block_hover.png",
                   clicked=ui.returns("hall2"))
  
  # Wait for the input
  $room = ui.interact()
  
  if room != "return":
    # Display a zoom animation, focusing on room that was clicked (using hard 
    # coded values for now, is this effect even necessary?)
    show floormap_big:
      linear 2.0 xalign 0.4 yalign 0.0 zoom 3
  
    # Jump to the room label, passing the selected value as a parameter
    call prepare_room(room)
  
  # When we are done with the searching scene, zoom out and fade out after it
  show floormap_big:
    linear 2.0 xalign 0.5 yalign 0.5 zoom 1
    linear 0.5 alpha 0.0
  
  call show_ui
 
  return
  
# Prepares a room for displaying. Basically this label places all the available
# items (read: locked & available during the night/decision) in random stashes 
# all around the room, preparing everything for the recursive show_room label.
#
# TODO: event triggering (if any), journal entry unlocking?
label prepare_room(room):
  python:
    # Get the locked items (that match the night/decision id) for hiding
    print "Building a list of locked items to hide (using night/decision value 3)..."
    items = inventory.get_locked_items("3")
    print "  Found", len(items), "locked items"
    
    # Create/clear the stash list
    stashes = {}
  
    # "Places" items in random stashes (= clickable objects, these are defined 
    # in label show_room below).
    # stash_count is the amount of stashes in the selected room
    def stash_items(stash_count):
      stashed_item_count = 0
    
      for item in items:
        # Break the loop if all the stashes have been filled
        if stashed_item_count >= stash_count:
          break
        
        # Randomize the stash (keeps on creating a random id as long as it 
        # keeps giving an id that has been used already)
        while (True):
          stash_id = random.randint(1,stash_count)
          if not stashes.has_key(stash_id):
            print "    Placed item", item.get_id(), "to stash", stash_id
            stashes[stash_id] = item
            stashed_item_count += 1
            break
  
  # Display the room's background 
  if room == "hall1":
    show hall1 behind ui:
      alpha 0.0
      pause 1.0
      linear 0.5 alpha 1.0
    
    # Puts the available items in stashes in the room. 
    $stash_items(3)
    
  elif room == "hall2":
    show kitchen behind ui:
      alpha 0.0
      pause 1.0
      linear 0.5 alpha 1.0
      
    $stash_items(5)
      
  # Show the room with the clickable objects
  call show_room(room)
  
  hide hall1
  hide hall2
  hide kitchen
  with dissolve
  
  return

# A recursive label that creates/re-places the room's clickable objects. The
# values the buttons return are used as stash ids
label show_room(room):
  if room == "hall1":
    # the table on the left
    $ui.frame(xpos=240, ypos=620, xpadding=0, ypadding=0, background=None)
    $ui.imagebutton("gfx/block.png",
                    "gfx/block_hover.png",
                    clicked=ui.returns(1))
                    
    # lamp 1
    $ui.frame(xpos=520, ypos=100, xpadding=0, ypadding=0, background=None)
    $ui.imagebutton("gfx/block.png",
                    "gfx/block_hover.png",
                    clicked=ui.returns(2))
    
    # lamp 2
    $ui.frame(xpos=520, ypos=200, xpadding=0, ypadding=0, background=None)
    $ui.imagebutton("gfx/block.png",
                    "gfx/block_hover.png",
                    clicked=ui.returns(3))
  elif room == "hall2":
    # some stash 1
    $ui.frame(xpos=340, ypos=620, xpadding=0, ypadding=0, background=None)
    $ui.imagebutton("gfx/block.png",
                    "gfx/block_hover.png",
                    clicked=ui.returns(1))
    
    # some stash 2
    $ui.frame(xpos=120, ypos=300, xpadding=0, ypadding=0, background=None)
    $ui.imagebutton("gfx/block.png",
                    "gfx/block_hover.png",
                    clicked=ui.returns(2))
    
    # some stash 3
    $ui.frame(xpos=520, ypos=500, xpadding=0, ypadding=0, background=None)
    $ui.imagebutton("gfx/block.png",
                    "gfx/block_hover.png",
                    clicked=ui.returns(3))
    # some stash 4
    $ui.frame(xpos=720, ypos=200, xpadding=0, ypadding=0, background=None)
    $ui.imagebutton("gfx/block.png",
                    "gfx/block_hover.png",
                    clicked=ui.returns(3))
  
  # etc. This label might get a bit big...
                    
  # Temporary return button for all the screens
  $ui.frame(xpos=0.5, ypos=0.1, xanchor=0.5, yanchor=0.5)
  $ui.textbutton("return", clicked=ui.returns(0))
  
  # Again, wait for the user input. If the button being pressed wasn't the 
  # return button, a check is being done to see if the clicked object had an
  # item hidden in it. After that a recursive call to this same label is made.
  $item = ui.interact()
  if item > 0:
    call check_stash(item)
    call show_room(room)
  
  return

label check_stash(stash_id):
  python:  
    if stashes.has_key(stash_id):
      item = stashes.get(stash_id)
      
      # Unlock the item
      inventory.unlock_item(item.get_id())
      
      # Clear the hiding place
      del stashes[stash_id]
      
      text = "You found item ", item.get_name(), "."
    else:
      text = "You found nothing."
    
    # Temporary confirmation dialog
    ui.frame(xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5)
    ui.vbox()
    ui.text(text)
    ui.textbutton("Ok", clicked=ui.returns(""))
    ui.close()
    
    # Wait for the user to click "ok"
    ui.interact()
    
  return