label show_map:
  # A dict containing the rooms and their items
  $rooms = { 
    "riroom" : { "backpack":None, "ball1":None, "ball2":None, "blanket":None, "books":None, "clothes":None, "trophy_big":None, "trophy_medium":None, "trophy_small":None},
    "soroom" : { "blanket":None, "brush":None, "bucket":None, "clothes":None, "flower_blue":None, "flower_cactus":None, "flower_red":None, "flower_white":None, "hairclips":None, "jewelry":None, "mirror":None, "paperbag":None, "vines":None }, 
    "suroom" : { "blanket":None, "console":None, "drawer":None, "lamp":None, "mirror":None, "poster1":None, "poster2":None, "tv":None }, 
    "roroom" : { "blanket":None, "cupboard":None, "doll":None, "hat":None, "jacket":None, "lamp":None, "magazines":None, "plant1":None, "plant2":None, "poster1":None, "poster2":None, "rack":None, "statue1":None, "statue2":None, "statue3":None },       
    "kitchen" : { "hood" : None, "sink" : None, "pots1" : None, "pots2" : None, "pots3" : None, "pots4" : None },
    "lib" : { "shelves1" : None, "shelves2" : None, "books1" : None, "books2" : None, "books3" : None, "books4" : None , "labkit" : None},
    "hall1" : { "flower" : None, "phone" : None },
    "hall2" : { "flower" : None, "phone" : None, "table" : None },
    # TODO
    "bathroom" : { "stash1" : None, "stash2" : None, "stash3" : None }
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
    
    clicks_left = CLICKS
       
  # Start the map screen loop. 
  while (clicks_left > 0):
    $show_clicks(clicks_left)  
    $show_room_icons(decision)
      
    $room = ui.interact(suppress_overlay=True)
    # Temporary return check
    if room != "return":
      # See if an event should happen when entering the room
      call run_event
      # Break the loop if an event happened. (... set tries to 0 because Renpy
      # doesn't understand words like "break" and such)
      if event_triggered:
        $clicks_left = 0
      else:
       $clicks_left = show_room(room, decision, clicks_left, rooms[room])
    else:
     $clicks_left = 0
     
  if not event_triggered:
    # Display a message box before returning to the script
    $show_clicks(clicks_left)
    $renpy.pause(0.2)
    $show_message("(\"0 clicks left\" message)", "large")
    
  $renpy.transition(dissolve)
  $renpy.hide("map")
  $show_main_ui()  
  $update_stats(MAIN_UI)
  
  return
  
init python:
  import random
  from mitsugame.item import Item
  
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
    
  def show_room(room, decision, clicks_left, items):   
    renpy.transition(dissolve)
    renpy.show("bg " + room, zorder=1)
    # room background names defined in script.rpy
    
    while (clicks_left > 0):
      show_room_clickables(room)
      show_clicks(clicks_left)
      
      selection = ui.interact(suppress_overlay=True, clear=False)
      if selection == "return":
        break
      else:
        clicks_left = show_info(selection, items, clicks_left)
      
    renpy.transition(dissolve)
    renpy.hide("bg " + room)
    ui.clear()
    
    return clicks_left
    
  def show_room_clickables(room):
    if room == "riroom":
      # backpack
      ui.frame(xpos=638, ypos=454, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/riroom/backpack.png",
                     "gfx/map/riroom/backpack_hover.png",
                     clicked=ui.returns(("stash", "backpack")))
                     
      # ball1
      ui.frame(xpos=876, ypos=401, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/riroom/ball1.png",
                     "gfx/map/riroom/ball1_hover.png",
                     clicked=ui.returns(("stash", "ball1")))
                     
      # ball2
      ui.frame(xpos=78, ypos=556, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/riroom/ball2.png",
                     "gfx/map/riroom/ball2_hover.png",
                     clicked=ui.returns(("stash", "ball2")))
                     
      # blanket
      ui.frame(xpos=234, ypos=573, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/riroom/blanket.png",
                     "gfx/map/riroom/blanket_hover.png",
                     clicked=ui.returns(("stash", "blanket")))
                     
      # books
      ui.frame(xpos=852, ypos=583, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/riroom/books.png",
                     "gfx/map/riroom/books_hover.png",
                     clicked=ui.returns(("stash", "books")))
                     
      # clothes
      ui.frame(xpos=208, ypos=519, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/riroom/clothes.png",
                     "gfx/map/riroom/clothes_hover.png",
                     clicked=ui.returns(("stash", "clothes")))
     
      # trophy_big
      ui.frame(xpos=748, ypos=335, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/riroom/trophy_big.png",
                     "gfx/map/riroom/trophy_big_hover.png",
                     clicked=ui.returns(("stash", "trophy_big")))
                     
      # trophy_medium
      ui.frame(xpos=799, ypos=344, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/riroom/trophy_medium.png",
                     "gfx/map/riroom/trophy_medium_hover.png",
                     clicked=ui.returns(("stash", "trophy_medium")))
                     
      # trophy_small
      ui.frame(xpos=728, ypos=348, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/riroom/trophy_small.png",
                     "gfx/map/riroom/trophy_small_hover.png",
                     clicked=ui.returns(("stash", "trophy_small")))
                     
      
    elif room == "roroom":    
      # blanket
      ui.frame(xpos=234, ypos=573, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/blanket.png",
                     "gfx/map/roroom/blanket_hover.png",
                     clicked=ui.returns(("stash", "blanket")))
      
      # cupboard
      ui.frame(xpos=561, ypos=403, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/cupboard.png",
                     "gfx/map/roroom/cupboard_hover.png",
                     clicked=ui.returns(("stash", "cupboard")))
      
      # doll               
      ui.frame(xpos=883, ypos=501, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/doll.png",
                     "gfx/map/roroom/doll_hover.png",
                     clicked=ui.returns(("stash", "doll")))
      
      # jacket
      ui.frame(xpos=104, ypos=248, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/jacket.png",
                     "gfx/map/roroom/jacket_hover.png",
                     clicked=ui.returns(("stash", "jacket")))
      
      # rack               
      ui.frame(xpos=54, ypos=262, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/rack.png",
                     "gfx/map/roroom/rack_hover.png",
                     clicked=ui.returns(("stash", "rack")))

      # hat
      ui.frame(xpos=30, ypos=268, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/hat.png",
                     "gfx/map/roroom/hat_hover.png",
                     clicked=ui.returns(("stash", "hat")))
                     
      # magazines
      ui.frame(xpos=597, ypos=628, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/magazines.png",
                     "gfx/map/roroom/magazines_hover.png",
                     clicked=ui.returns(("stash", "magazines")))
                     
      # plant1
      ui.frame(xpos=640, ypos=296, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/plant1.png",
                     "gfx/map/roroom/plant1_hover.png",
                     clicked=ui.returns(("stash", "plant1")))
                     
      # plant2
      ui.frame(xpos=443, ypos=367, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/plant2.png",
                     "gfx/map/roroom/plant2_hover.png",
                     clicked=ui.returns(("stash", "plant2")))
      
      # poster1               
      ui.frame(xpos=571, ypos=253, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/poster1.png",
                     "gfx/map/roroom/poster1_hover.png",
                     clicked=ui.returns(("stash", "poster1")))
                     
      # poster2
      ui.frame(xpos=762, ypos=210, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/poster2.png",
                     "gfx/map/roroom/poster2_hover.png",
                     clicked=ui.returns(("stash", "poster2")))
                     
      # lamp
      ui.frame(xpos=721, ypos=331, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/lamp.png",
                     "gfx/map/roroom/lamp_hover.png",
                     clicked=ui.returns(("stash", "lamp")))                     
                           
      # statue1
      ui.frame(xpos=830, ypos=325, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/statue1.png",
                     "gfx/map/roroom/statue1_hover.png",
                     clicked=ui.returns(("stash", "statue1")))
                     
      # statue2
      ui.frame(xpos=796, ypos=354, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/statue2.png",
                     "gfx/map/roroom/statue2_hover.png",
                     clicked=ui.returns(("stash", "statue2")))
                     
      # statue3
      ui.frame(xpos=876, ypos=331, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/roroom/statue3.png",
                     "gfx/map/roroom/statue3_hover.png",
                     clicked=ui.returns(("stash", "statue3")))
      
    elif room == "soroom":
      # blanket
      ui.frame(xpos=234, ypos=573, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/soroom/blanket.png",
                     "gfx/map/soroom/blanket_hover.png",
                     clicked=ui.returns(("stash", "blanket")))
                     
      # vines
      ui.frame(xpos=544, ypos=3, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/soroom/vines.png",
                     "gfx/map/soroom/vines_hover.png",
                     clicked=ui.returns(("stash", "vines")))
      
      # brush
      ui.frame(xpos=637, ypos=651, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/soroom/brush.png",
                     "gfx/map/soroom/brush_hover.png",
                     clicked=ui.returns(("stash", "brush")))
                     
      # bucket
      ui.frame(xpos=37, ypos=449, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/soroom/bucket.png",
                     "gfx/map/soroom/bucket_hover.png",
                     clicked=ui.returns(("stash", "bucket")))
                     
      # clothes
      ui.frame(xpos=286, ypos=629, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/soroom/clothes.png",
                     "gfx/map/soroom/clothes_hover.png",
                     clicked=ui.returns(("stash", "clothes")))
                     
      # mirror
      ui.frame(xpos=810, ypos=215, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/soroom/mirror.png",
                     "gfx/map/soroom/mirror_hover.png",
                     clicked=ui.returns(("stash", "mirror")))
                                          
      # flower_blue
      ui.frame(xpos=752, ypos=310, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/soroom/flower_blue.png",
                     "gfx/map/soroom/flower_blue_hover.png",
                     clicked=ui.returns(("stash", "flower_blue")))
                     
      # flower_cactus
      ui.frame(xpos=787, ypos=334, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/soroom/flower_cactus.png",
                     "gfx/map/soroom/flower_cactus_hover.png",
                     clicked=ui.returns(("stash", "flower_cactus")))
                     
      # flower_red
      ui.frame(xpos=446, ypos=351, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/soroom/flower_red.png",
                     "gfx/map/soroom/flower_red_hover.png",
                     clicked=ui.returns(("stash", "flower_red")))
                     
      # flower_white
      ui.frame(xpos=499, ypos=391, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/soroom/flower_white.png",
                     "gfx/map/soroom/flower_white_hover.png",
                     clicked=ui.returns(("stash", "flower_white")))
                     
      # hairclips
      ui.frame(xpos=597, ypos=674, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/soroom/hairclips.png",
                     "gfx/map/soroom/hairclips_hover.png",
                     clicked=ui.returns(("stash", "hairclips")))
      
      # jewelry
      ui.frame(xpos=878, ypos=356, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/soroom/jewelry.png",
                     "gfx/map/soroom/jewelry_hover.png",
                     clicked=ui.returns(("stash", "jewelry")))
                     
      # paperbag
      ui.frame(xpos=911, ypos=495, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/soroom/paperbag.png",
                     "gfx/map/soroom/paperbag_hover.png",
                     clicked=ui.returns(("stash", "paperbag")))
      
    elif room == "suroom":
      # Blanket
      ui.frame(xpos=234, ypos=573, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/suroom/blanket.png",
                     "gfx/map/suroom/blanket_hover.png",
                     clicked=ui.returns(("stash", "blanket")))

      # Console
      ui.frame(xpos=713, ypos=493, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/suroom/console.png",
                     "gfx/map/suroom/console_hover.png",
                     clicked=ui.returns(("stash", "console")))

      # Drawer
      ui.frame(xpos=597, ypos=416, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/suroom/drawer.png",
                     "gfx/map/suroom/drawer_hover.png",
                     clicked=ui.returns(("stash", "drawer")))

      # Lamp
      ui.frame(xpos=482, ypos=465, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/suroom/lamp.png",
                     "gfx/map/suroom/lamp_hover.png",
                     clicked=ui.returns(("stash", "lamp")))

      # Mirror
      ui.frame(xpos=871, ypos=203, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/suroom/mirror.png",
                     "gfx/map/suroom/mirror_hover.png",
                     clicked=ui.returns(("stash", "mirror")))

      # Poster 1
      ui.frame(xpos=586, ypos=246, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/suroom/poster1.png",
                     "gfx/map/suroom/poster1_hover.png",
                     clicked=ui.returns(("stash", "poster1")))

      # Poster 2
      ui.frame(xpos=7, ypos=224, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/suroom/poster2.png",
                     "gfx/map/suroom/poster2_hover.png",
                     clicked=ui.returns(("stash", "poster2")))

      # TV
      ui.frame(xpos=729, ypos=293, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/suroom/tv.png",
                     "gfx/map/suroom/tv_hover.png",
                     clicked=ui.returns(("stash", "tv")))

    elif room == "kitchen":
      # Cooker hood
      ui.frame(xpos=273, ypos=0, background=None, xpadding=0, ypadding=0)
      ui.imagebutton(im.Scale("gfx/transparent.png", 431, 314),
                     "gfx/map/kitchen/KitchenCabinets1.png",
                     clicked=ui.returns(("stash", "hood")))
      
      # Sink
      ui.frame(xpos=893, ypos=429, background=None, xpadding=0, ypadding=0)
      ui.imagebutton(im.Scale("gfx/transparent.png", 131, 339),
                     "gfx/map/kitchen/KitchenCabinets2.png",
                     clicked=ui.returns(("stash", "sink")))
      
      # Hanging pots (pots1)
      ui.frame(xpos=842, ypos=0, background=None, xpadding=0, ypadding=0)
      ui.imagebutton(im.Scale("gfx/transparent.png", 182, 341),
                     "gfx/map/kitchen/KitchenPots1.png",
                     clicked=ui.returns(("stash", "pots1")))
      
      # Small pot (pots2)
      ui.frame(xpos=326, ypos=408, background=None, xpadding=0, ypadding=0)
      ui.imagebutton(im.Scale("gfx/transparent.png", 77, 53),
                     "gfx/map/kitchen/KitchenPots2.png",
                     clicked=ui.returns(("stash", "pots2")))
      
      # Large pot (pots3)
      ui.frame(xpos=424, ypos=391, background=None, xpadding=0, ypadding=0)
      ui.imagebutton(im.Scale("gfx/transparent.png", 98, 92),
                     "gfx/map/kitchen/KitchenPots3.png",
                     clicked=ui.returns(("stash", "pots3")))
      
      # Frying pan + pot (pots4)
      ui.frame(xpos=544, ypos=406, background=None, xpadding=0, ypadding=0)
      ui.imagebutton(im.Scale("gfx/transparent.png", 131, 339),
                     "gfx/map/kitchen/KitchenPots4.png",
                     clicked=ui.returns(("stash", "pots4")))
                     
    elif room == "lib":
      # Shelves 1
      ui.frame(xpos=0, ypos=270, background=None, xpadding=0, ypadding=0)
      ui.imagebutton(im.Scale("gfx/transparent.png", 261, 491),
                     "gfx/map/library/LibraryShelves1.png",
                     clicked=ui.returns(("stash", "shelves1")))
                     
      # Shelves 2
      ui.frame(xpos=802, ypos=279, background=None, xpadding=0, ypadding=0)
      ui.imagebutton(im.Scale("gfx/transparent.png", 222, 483),
                     "gfx/map/library/LibraryShelves2.png",
                     clicked=ui.returns(("stash", "shelves2")))
    
      # Books 1
      ui.frame(xpos=448, ypos=446, background=None, xpadding=0, ypadding=0)
      ui.imagebutton(im.Scale("gfx/transparent.png", 255, 68),
                     "gfx/map/library/LibraryBooks1.png",
                     clicked=ui.returns(("stash", "books1")))

      # Books 2
      ui.frame(xpos=47, ypos=577, background=None, xpadding=0, ypadding=0)
      ui.imagebutton(im.Scale("gfx/transparent.png", 206, 187),
                     "gfx/map/library/LibraryBooks2.png",
                     clicked=ui.returns(("stash", "books2")))
      
      # Books 3
      ui.frame(xpos=252, ypos=565, background=None, xpadding=0, ypadding=0)
      ui.imagebutton(im.Scale("gfx/transparent.png", 534, 203),
                     "gfx/map/library/LibraryBooks3.png",
                     clicked=ui.returns(("stash", "books3")))
                     
      # Books 4
      ui.frame(xpos=790, ypos=614, background=None, xpadding=0, ypadding=0)
      ui.imagebutton(im.Scale("gfx/transparent.png", 211, 131),
                     "gfx/map/library/LibraryBooks4.png",
                     clicked=ui.returns(("stash", "books4")))
                     
      # lab kit
      ui.frame(xpos=435, ypos=369, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/library/labkit.png",
                     "gfx/map/library/labkit_hover.png",
                     clicked=ui.returns(("stash", "labkit")))
                     
    elif room == "hall1":
      # flower
      ui.frame(xpos=172, ypos=316, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/hall1/flower.png",
                     "gfx/map/hall1/flower_hover.png",
                     clicked=ui.returns(("stash", "flower")))
                     
      # phone
      ui.frame(xpos=79, ypos=489, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/hall1/phone.png",
                     "gfx/map/hall1/phone_hover.png",
                     clicked=ui.returns(("stash", "phone")))
    elif room == "hall2":
      # table
      ui.frame(xpos=12, ypos=502, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/hall2/table.png",
                     "gfx/map/hall2/table_hover.png",
                     clicked=ui.returns(("stash", "table")))
    
      # flower
      ui.frame(xpos=142, ypos=279, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/hall2/flower.png",
                     "gfx/map/hall2/flower_hover.png",
                     clicked=ui.returns(("stash", "flower")))
                     
      # phone
      ui.frame(xpos=79, ypos=512, background=None, xpadding=0, ypadding=0)
      ui.imagebutton("gfx/map/hall2/phone.png",
                     "gfx/map/hall2/phone_hover.png",
                     clicked=ui.returns(("stash", "phone")))
 
    # Return button
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("Return", clicked=ui.returns("return"))
    
    return
    
  def show_info(selection, items, clicks_left):
    # FIXME: something returns 0 as selection when clicking at nothing, so find
    # out what that is and fix that.
    if selection == 0:
      return clicks_left
    
    # First, check what info should be displayed
    if selection[0] == "tidbit":
      message = "You found a tidbit."
    else:
      item = items[selection[1]]
      if item == None:
        message = "You found nothing of interest."
        show_message(message, "medium")
      else:
        message = "You found an item: " + item.get_name() + "\n"
        
        renpy.transition(dissolve)
        ui.frame(xmaximum=480, 
                 xpadding=40, ypadding=40, 
                 xpos=0.5, ypos=0.5, 
                 xanchor=304, yanchor=95, 
                 background="gfx/textbox_2.png")
        
        ui.hbox(spacing=40)
        ui.text("You found an item: " + item.get_name() + "\n\n" + item.get_description())
        ui.image(im.Scale("gfx/items/" + item.get_id() + ".png", 100, 100))
        ui.close()
    
        # Full screen hidden button, "click anywhere to continue" kind
        ui.frame(xpos=0, ypos=0, background=None)
        ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
        ui.interact()
        renpy.transition(dissolve)
        
        if item.get_id() not in persistent.unlocked_items:
          persistent.unlocked_items.append(item.get_id())
        print "Unlocked item", item.get_id()
        
        items[selection[1]] = None
        
        clicks_left -= 1      
    
    return clicks_left
