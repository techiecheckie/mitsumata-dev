init python:
  import time

  renpy.image("flowerpot", "gfx/backgrounds/daygrass.jpg")

  GARDEN_GRID = [
    (MINIGAME_POS_X + 100, MINIGAME_POS_Y + 150),
    (MINIGAME_POS_X + 250, MINIGAME_POS_Y + 150),
    (MINIGAME_POS_X + 400, MINIGAME_POS_Y + 150),
    
    (MINIGAME_POS_X + 100, MINIGAME_POS_Y + 250),
    (MINIGAME_POS_X + 250, MINIGAME_POS_Y + 250),
    (MINIGAME_POS_X + 400, MINIGAME_POS_Y + 250),
    
    (MINIGAME_POS_X + 100, MINIGAME_POS_Y + 350),
    (MINIGAME_POS_X + 250, MINIGAME_POS_Y + 350),
    (MINIGAME_POS_X + 400, MINIGAME_POS_Y + 350)
  ]
  
  # temporary phase variables, will change once all the plant phases are clear
  PHASE_1 = 0
  PHASE_2 = 1
  PHASE_3 = 2
  PHASE_4 = 3

  
  # Garden's main method. Displays a field of grass and a few pieces of ground 
  # using the minigame ui.
  def show_garden():
    renpy.transition(dissolve)
    renpy.show("flowerpot", at_list = [Position(xpos=MINIGAME_POS_X-20, ypos=MINIGAME_POS_Y-40), Transform(anchor=(0.0, 0.0))], zorder=-1)
    
    current_time = time.time()
    update_garden(current_time)
    available_seeds = get_seeds()
    
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
    for i in range(0, len(persistent.garden)-1):
      plant = persistent.garden[i]
      if plant != None:
        plant_id    = plant[0]
        plant_phase = plant[1]
        plant_time  = plant[2]
        time_diff   = current_time - plant_time
        
        if time_diff >= 15*60:
          plant_phase += 1
          plant_time   = current_time
          
          # change the seed into a plant by replacing the last letter in its id
          # (aos --> aop)
          if plant[1] == PHASE_4:
            plant_id = plant_id[:2] + "p"
            # TODO: turning into a monster plant? (10% chance)
            
        persistent.garden[i] = (plant_id, plant_phase, plant_time)
        print plant[0], plant[1], plant[2], "time diff:", time_diff
              
    return 
  
  # Displays a grid of patches of earth and the seeds/plants that are growing in
  # them. 
  def show_plant_spots():
    print persistent.garden

    for i in range(0, len(GARDEN_GRID)):
      cell = GARDEN_GRID[i]
      
      # TODO: rather do image scaling before going through the array
      if persistent.garden[i] != None:
        normal_image = im.Scale("gfx/items/" + persistent.garden[i][0] + ".png", 80, 80)
        hover_image  = im.Scale("gfx/items/" + persistent.garden[i][0] + "_hover.png", 80, 80)
        
        ui.frame(xpos=cell[0], ypos=cell[1], background=None)
        ui.image(im.Scale("gfx/whack_a_mole/dirt.png", 80, 80))
      else:
        normal_image = im.Scale("gfx/whack_a_mole/dirt.png", 80, 80)
        hover_image  = im.Scale("gfx/whack_a_mole/dirt_hover.png", 80, 80)
        
      ui.frame(xpos=cell[0], ypos=cell[1], background=None)
      ui.imagebutton(normal_image,
                     hover_image,
                     clicked=ui.returns(i))
    
    return
  
  # Harverts the plant that was clicked, adding it into the user's inventory. 
  # Once a plant is harvested, the cell containing the item is cleared for new
  # seeds to be planted. 
  #
  # Not fully implemented yet. 
  def harvest(cell):
    plant = persistent.garden[cell]
    
    # temp
    # Check if the clicked item was a full grown plant, and if so, then add it
    # to the inventory (unlock)
    if plant[1] == PHASE_4:
      if plant[0] not in persistent.unlocked_items:
        persistent.unlocked_items.append(plant[0])
        print "Unlocked item", plant[0]
    else:
      print "Removed seed", plant[0]
    
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
             ypadding=40)
    ui.vbox()
    ui.text("Choose the seed you want to plant in this spot:")
    for seed in available_seeds:
      ui.textbutton(seed.get_name(), clicked=ui.returns(seed.get_id()), background=None)
    ui.textbutton("Cancel", clicked=ui.returns("cancel"), background=None)
    ui.close()
    
    seed_id = ui.interact()
    renpy.transition(dissolve)
    
    if seed_id != "cancel":
      persistent.garden[button] = (seed_id, PHASE_1, current_time)
      print "Planted seed", seed_id, "to spot", button
    
    return
    
