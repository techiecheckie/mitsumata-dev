image floormap_big = "gfx/map/floormap_big.jpg"
image room2 = "gfx/map/room2.png"

# temp
image block = "gfx/block.png" 

label room_selection:  

  show floormap_big at Position(xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) behind ui, mp_background, hp_background with dissolve
  
  # Create the buttons
  python:
    ui.frame(xpos=0.5, ypos=0.1, xanchor=0.5, yanchor=0.5)
    ui.textbutton("return", clicked=ui.returns("return"))
    
    ui.frame(xpos=412, ypos=215, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/map/room2_box.png", 
                   "gfx/map/room2_box_hover.png",
                   clicked=ui.returns("room2"))
  
  # Wait for the input
  $room = ui.interact()
  
  if room == "return":
    "(returning to main script)"
    hide floormap_big with dissolve
    return
  
  # Display a zoom animation (using hard coded values for now)
  show floormap_big:
    linear 2.0 xalign 0.4 yalign 0.0 zoom 3
  
  # Jump to the room label, passing the selected value as a parameter
  call room(room)
  
  # Zoom out and then fade out after it
  show floormap_big:
    linear 2.0 xalign 0.5 yalign 0.5 zoom 1
    linear 0.5 alpha 0.0
  
  "(returning to main script)"
  
  return
  
label room(room):  
  if room == "room2":
    show room2 behind ui:
      alpha 0.0
      anchor (0.5,0.5)
      xpos 0.5
      ypos 0.4
      
      pause 1.0
      
      linear 0.5 alpha 1.0

  # Search spots are spots that can be clicked on to get information or find 
  # items. They should be very lightly highlighted when scrolled over, and when
  # clicked, a small box explaining what is happening there should pop up, as 
  # well as whether or not there is an item in that spot. Search spots are 
  # usually light figures, drawers, beds, anything that isn't the wall or the 
  # floor can become a search spot.
  
  # Night options are labelled in the programming so that the proper items will 
  # go into the correct room on the correct night. Upon clicking Search, a map 
  # of the entire shrine will pop up and you may click on the room you wish to 
  # search. It will bring you to that room, which may trigger an event. If not, 
  # then clicking on search spots will trigger information about what you 
  # clicked, or you may receive an item or journal entry, which will go into 
  # your palm pilot inventory.
  
  # Not all items can be found during every nightly option, which is why they 
  # are labelled and numbered. Some items only appear on certain nights. Some 
  # items appear every night, but move positions. If possible, I'd like them to 
  # move positions at random.
  
  # TODO: check if any events have been triggered
  
  # TODO: the rest of this shite
  call search_room(room)
  
  show room2:
    linear 0.5 alpha 0.0
  
  return
  
# Test label for the room searching scene
label search_room(room):
  python:
    def place_searchables():
      ui.frame(xpos=0.5, ypos=0.1, xanchor=0.5, yanchor=0.5)
      ui.textbutton("return", clicked=ui.returns("return"))
    
      if room == "room2":
        ui.frame(xpos=432, ypos=217, xpadding=0, ypadding=0, background=None)
        ui.imagebutton("gfx/map/room2_container1.png",
                       "gfx/map/room2_container1_hover.png",
                       clicked=ui.returns("container1"))
                     
        ui.frame(xpos=234, ypos=218, xpadding=0, ypadding=0, background=None)
        ui.imagebutton("gfx/map/room2_container2.png",
                       "gfx/map/room2_container2_hover.png",
                       clicked=ui.returns("container2"))
  
  $place_searchables()
  $container = ui.interact()
  
  # Stay in the search screen until... something. For now we'll just do this:
  if container != "return":
    "(clicked on %(container)s, probably even unlocked an item or some other stuff...)"
    # Can't pass any parameters to jump, so we're using call here. Potential 
    # overflow error?
    call search_room(room)
  
  return
  