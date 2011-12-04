init python:
  import time

  renpy.image("flowerpot", "gfx/backgrounds/daygrass.jpg")

  GARDEN_GRID = [
    (MINIGAME_POS_X + 120, MINIGAME_POS_Y + 170),
    (MINIGAME_POS_X + 270, MINIGAME_POS_Y + 170),
    (MINIGAME_POS_X + 420, MINIGAME_POS_Y + 170),
    
    (MINIGAME_POS_X + 120, MINIGAME_POS_Y + 270),
    (MINIGAME_POS_X + 270, MINIGAME_POS_Y + 270),
    (MINIGAME_POS_X + 420, MINIGAME_POS_Y + 270),
    
    (MINIGAME_POS_X + 120, MINIGAME_POS_Y + 370),
    (MINIGAME_POS_X + 270, MINIGAME_POS_Y + 370),
    (MINIGAME_POS_X + 420, MINIGAME_POS_Y + 370)
  ]
  
  GARDEN_CELL_SIZE = 80
 
  GARDEN_PHASE_DURATION = 15

  
  # Garden's main method. Displays a field of grass and a few pieces of ground 
  # using the minigame ui.
  def show_garden():
    renpy.transition(dissolve)
    renpy.show("flowerpot", at_list = [Position(xpos=MINIGAME_POS_X-20, ypos=MINIGAME_POS_Y-40), Transform(anchor=(0.0, 0.0))], zorder=-1)
    
    current_time    = time.time()
    inform_withered = update_garden(current_time)
    available_seeds = get_seeds()
    
    # 
    if inform_withered == True:
      renpy.transition(dissolve)
      ui.frame(xpos=MINIGAME_POS_X+50, 
               ypos=MINIGAME_POS_Y+150, 
               background="gfx/textbox.png",
               xpadding=40,
               ypadding=40,
               xmaximum=490)
      ui.hbox(spacing=40)    
      ui.text("Some of your plants had withered and were automatically removed.\n\nClick to continue")
      ui.close()
      
      # Minigame area sized invisible button
      ui.frame(xpos=MINIGAME_POS_X,
               ypos=MINIGAME_POS_Y,
               background=None,
               xmaximum=MINIGAME_WIDTH,
               ymaximum=MINIGAME_HEIGHT)
      ui.textbutton("", clicked=ui.returns(""), 
                    xfill=True, yfill=True,
                    background=None)
      ui.interact()
      renpy.transition(dissolve)
    
    # Wait for clicks on the patches of ground or the minigame main ui buttons.
    # If a clicked patch contains a seed/plant, a harvest dialog(?) is displayed
    # Otherwise a planting dialog (list of plantable seeds) is displayed.
    while True:
      show_plant_spots()
      button = ui.interact()
         
      if button == "exit":
        break
      else:
        if button != "":
          if persistent.garden[button] != None:
            harvest(button)
          else:
            show_planting_dialog(available_seeds, button, current_time)
      
    renpy.transition(dissolve)
    renpy.hide("flowerpot")
    ui.clear()
    
    return
  
  # Returns a list of plantable seeds. Plantable seeds are items that have been
  # unlocked before and have their id listed in persistent.unlocked_items
  def get_seeds():
    seeds = []
    for id in persistent.unlocked_items:
      item = inventory.get_item(id)
      if item.get_name().endswith("Seed"):
        seeds.append(item)
    
    return seeds
  
  # Updates the phase of the planted seeds. This method checks if 15 minutes
  # have passed since the planting and then updates the plant's growth phase
  # accordingly (TODO). When a plant is updated (phase++), the plant's time is 
  # set to the current time (given as a parameter) and the id gets updated to
  # match the current state (currently only the last phase, the full grown
  # flower phase, is recognized).
  def update_garden(current_time):
    inform_withered = False
    for i in range(0, len(persistent.garden)):
      plant = persistent.garden[i]
      if plant != None:
        plant_id    = plant[0]
        plant_time  = plant[1]
        time_diff   = int(current_time - START_TIME)
        plant_time += time_diff - plant_time
        phase       = int(plant_time/GARDEN_PHASE_DURATION)
        
        #time_diff   = current_time - plant_time
        #phase = int(time_diff/GARDEN_PHASE_DURATION)
        
        #print phase, plant_time
        
        print " ", plant_id, "in phase", phase, time_diff, plant_time
        
        # phase 0 (seed)      (aos)
        # phase 1             (aos1) tms.
        # phase 2             (aos2) tms.
        # phase 3 (plant)     (aop)
        # phase 4 (withered?) (aow) tms.
        
        if phase == 0:
          # first phase
          pass
        elif phase == 1:
          # mid phase 1
          pass
        elif phase == 2:
          # mid phase 2
          pass
        elif phase > 2 and phase < 5:
          # full grown plant
          plant_id = plant_id[:2] + "p"
        else:
          # withered?
          # Remove plant and inform the user that all the plants that have died
          # have been removed from the garden.
          inform_withered = True
        
        # There should be a 10% chance of the plant turning into a monster plant.
        # Change the graphics (plant_id etc.) or just inform the user when
        # harvesting?
        if inform_withered:
          persistent.garden[i] = None
        else:            
          persistent.garden[i] = (plant_id, plant_time)
              
    return inform_withered
  
  # Displays a grid of patches of earth and the seeds/plants that are growing in
  # them. 
  def show_plant_spots():
    for i in range(0, len(GARDEN_GRID)):
      cell = GARDEN_GRID[i]
      
      # TODO: rather do image scaling before going through the array
      if persistent.garden[i] != None:
        normal_image = im.Scale("gfx/items/" + persistent.garden[i][0] + ".png", 
                                GARDEN_CELL_SIZE, GARDEN_CELL_SIZE)
        hover_image  = im.Scale("gfx/items/" + persistent.garden[i][0] + "_hover.png", 
                                GARDEN_CELL_SIZE, GARDEN_CELL_SIZE)
        
        ui.frame(xpos=cell[0], ypos=cell[1], background=None)
        ui.image(im.Scale("gfx/whack_a_mole/dirt.png", 
                          GARDEN_CELL_SIZE, GARDEN_CELL_SIZE))
      else:
        normal_image = im.Scale("gfx/whack_a_mole/dirt.png", 
                                GARDEN_CELL_SIZE, GARDEN_CELL_SIZE)
        hover_image  = im.Scale("gfx/whack_a_mole/dirt_hover.png", 
                                GARDEN_CELL_SIZE, GARDEN_CELL_SIZE)
        
      ui.frame(xpos=cell[0], ypos=cell[1], background=None)
      ui.imagebutton(normal_image,
                     hover_image,
                     clicked=ui.returns(i))
    
    return
  
  # Harvests the plant that was clicked, adding it into the user's inventory. 
  # Once a plant is harvested, the cell containing the item is cleared for new
  # seeds to be planted.
  def harvest(cell):
    plant = persistent.garden[cell]
    
    renpy.transition(dissolve)
    ui.frame(xpos=MINIGAME_POS_X+50, 
             ypos=MINIGAME_POS_Y+150, 
             background="gfx/textbox.png",
             xpadding=40,
             ypadding=40,
             xmaximum=520)
    ui.vbox()
    ui.text("Harvest plant?\n\n")
    ui.textbutton("Ok", clicked=ui.returns("ok"), xfill=True)
    ui.textbutton("Cancel", clicked=ui.returns("cancel"), xfill=True)
    ui.close()
    
    button = ui.interact()
    renpy.transition(dissolve)
    
    if button == "cancel": return
    
    # Check if the clicked item was a full grown plant, and if so, then add it
    # to the inventory (and display the item info)
    if plant[0].endswith("p"):
      if plant[0] not in persistent.unlocked_items:
        persistent.unlocked_items.append(plant[0])
        
        item = inventory.get_item(plant[0])
        
        # Item info box
        ui.frame(xpos=MINIGAME_POS_X+50, 
                 ypos=MINIGAME_POS_Y+150, 
                 background="gfx/textbox.png",
                 xpadding=40,
                 ypadding=40,
                 xmaximum=520)
        ui.hbox(spacing=40)    
        ui.image(im.Scale("gfx/items/" + item.get_id() + ".png", 75, 75))
        ui.text(item.get_description() + "\n\nClick to continue")
        ui.close()
        
        # Minigame area sized invisible button
        ui.frame(xpos=MINIGAME_POS_X,
                 ypos=MINIGAME_POS_Y,
                 background=None,
                 xmaximum=MINIGAME_WIDTH,
                 ymaximum=MINIGAME_HEIGHT)
        ui.textbutton("", clicked=ui.returns(""), 
                      xfill=True, yfill=True,
                      background=None)
        ui.interact()
        renpy.transition(dissolve)
    
    ui.clear()
    
    persistent.garden[cell] = None
    
    return
  
  # Displays a dialog on top of the garden, giving the user the possibility to
  # choose the type of the seed that should be planted.
  def show_planting_dialog(available_seeds, button, current_time):
    renpy.transition(dissolve)
    ui.frame(xpos=MINIGAME_POS_X+50, 
             ypos=MINIGAME_POS_Y+150, 
             background="gfx/textbox.png",
             xpadding=40,
             ypadding=40,
             xmaximum=520)
    ui.vbox()
    ui.text("Choose the seed you want to plant in this spot\n\nAvailable seeds:")
    for seed in available_seeds:
      ui.textbutton(seed.get_name(), clicked=ui.returns(seed.get_id()), xfill=True)
    ui.textbutton("Cancel", clicked=ui.returns("cancel"), xfill=True)
    ui.close()
    
    seed_id = ui.interact()
    renpy.transition(dissolve)
    
    if seed_id != "cancel":
      persistent.garden[button] = (seed_id, 0)
      print "Planted seed", seed_id, "to spot", button
    
    return
