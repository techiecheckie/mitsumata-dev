init python:
  import time

  persistent.last_time = time.time()

  renpy.image("flowerpot",   "gfx/backgrounds/daygrass.jpg")
  renpy.image("hole",        "gfx/garden/garden_dirt_0.png")
  renpy.image("hole_hover",  "gfx/garden/garden_dirt_0.png")
  renpy.image("dirt",        "gfx/garden/garden_dirt_1.png")
  renpy.image("dirt_hover",  "gfx/garden/garden_dirt_1.png")
  renpy.image("plant",       "gfx/garden/garden_dirt_2.png")
  renpy.image("plant_hover", "gfx/garden/garden_dirt_2.png")

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
 
  GARDEN_PHASE_DURATION = 15*60

  
  # Garden's main method. Displays a field of grass and a few pieces of ground 
  # using the minigame ui.
  def show_garden():
    renpy.transition(dissolve)
    renpy.show("flowerpot", at_list = [Position(xpos=MINIGAME_POS_X-20, ypos=MINIGAME_POS_Y-40), Transform(anchor=(0.0, 0.0))], zorder=0)
    
    current_time         = time.time()
    inform_withered      = update_garden(current_time)
    persistent.last_time = current_time

    available_seeds = get_seeds()
    
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
      
      show_invisible_button("mini")
    
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
  
  # Updates the phase of the planted seeds. A phase lasts for 15 minutes, and
  # if a seed has reached phase 3, it will turn into a full grown plant. If
  # too much time has passed since the planting (phase >= 5), the plant will
  # wither and be marked for automatic removal.
  def update_garden(current_time):
    inform_withered = False

    for i in range(0, len(persistent.garden)):
      plant = persistent.garden[i]
      if plant != None:
        plant_id    = plant[0]
        plant_time  = plant[1]
        growth_time = plant[2]
        growth_time += (current_time - persistent.last_time)
        plant_phase = int(growth_time/GARDEN_PHASE_DURATION)

        #print " ", plant_id, "in phase", plant_phase, "after growing for", growth_time
        
        # phase 0 (seed)
        # phase 1
        # phase 2
        # phase 3  (plant)
        # phase 5+ (withered)
        
        if plant_phase >= 5:
          # Withered. Remove the plant and inform the user that all the plants 
          # that have died have been removed from the garden.
          inform_withered = True
          persistent.garden[i] = None
        else:
          if (plant_phase > 2):
            # Full grown plant, change id from seed to plant (e.g. aos --> aop)
            plant_id = plant_id[:2] + "p"
          persistent.garden[i] = (plant_id, plant_time, growth_time, plant_phase)
        
        # There should be a 10% chance of the plant turning into a monster plant.
        # Change the graphics (plant_id etc.) or just inform the user when
        # harvesting?

    return inform_withered
  
  # Displays a grid of patches of earth and the seeds/plants that are growing in
  # them. 
  def show_plant_spots():
    for i in range(0, len(GARDEN_GRID)):
      cell = GARDEN_GRID[i]
      plant = persistent.garden[i]

      if plant == None:
        normal_image = "hole"
        hover_image = "hole_hover"
      else:
        if plant[3] > 2:
          normal_image = "plant"
          hover_image = "plant_hover"
        else:
          normal_image = "dirt"
          hover_image = "dirt_hover"

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
    item_seed  = inventory.get_item(plant[0])
    item_plant = inventory.get_item(plant[0][:2] + "p")

    if plant[3] < 3:
      info_string    = "The seed of a " + item_plant.get_name() + "\n\n"
    
      bonuses = item_plant.get_bonuses()
      if bonuses != None:
        bonuses_string = "Once harvested, it'll give you: "
        bonus_keys = bonuses.keys()
        for bonus_key in bonus_keys:
          bonuses_string += "\n    " + bonuses[bonus_key] + " " + bonus_key
        bonuses_string += "."
      else:
        bonuses_string = ""
    
      time_left = int((GARDEN_PHASE_DURATION*3 - plant[2])/60)
      if time_left < 0:
        time_left = 0
      time_string = "\n\nTime left: about " + str(time_left) + " minutes"

      # Item info box
      renpy.transition(dissolve)
      ui.frame(xpos=MINIGAME_POS_X+50, 
               ypos=MINIGAME_POS_Y+150, 
               background="gfx/textbox.png",
               xpadding=60,
               ypadding=60,
               xmaximum=520)
      ui.hbox(spacing=40)    
      ui.image(im.Scale("gfx/items/" + item_seed.get_id() + ".png", 75, 75))
      ui.text("{size=-3}" + info_string + bonuses_string + time_string + "{/size}")
      ui.close()

      show_invisible_button("mini")
      
    else:
      # Item info box
      renpy.transition(dissolve)
      ui.frame(xpos=MINIGAME_POS_X+50, 
               ypos=MINIGAME_POS_Y+150, 
               background="gfx/textbox.png",
               xpadding=40,
               ypadding=40,
               xmaximum=520)
      ui.hbox(spacing=40)    
      ui.image(im.Scale("gfx/items/" + item_plant.get_id() + ".png", 75, 75))
      ui.text("{size=-3}You harvested " + item_plant.get_name() + ".{/size}")
      ui.close()

      show_invisible_button("mini")

      if plant[0] not in persistent.unlocked_items:
        persistent.unlocked_items.append(plant[0])
        
        # Item info box
        ui.frame(xpos=MINIGAME_POS_X+50, 
                 ypos=MINIGAME_POS_Y+150, 
                 background="gfx/textbox.png",
                 xpadding=40,
                 ypadding=40,
                 xmaximum=520)
        ui.hbox(spacing=40)    
        ui.image(im.Scale("gfx/items/" + item_plant.get_id() + ".png", 75, 75))
        ui.text("{size=-3}" + item_plant.get_description() + "{/size}")
        ui.close()
        
        show_invisible_button("mini")

      persistent.garden[cell] = None
    
    ui.clear()
    
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
    ui.text("{size=-3}Choose the seed you want to plant in this spot\n\nAvailable seeds:{/size}")
    for seed in available_seeds:
      ui.textbutton("{size=-3}" + seed.get_name() + "{/size}", clicked=ui.returns(seed.get_id()), xfill=True)
    ui.textbutton("{size=-3}Cancel{/size}", clicked=ui.returns("cancel"), xfill=True)
    ui.close()
    
    seed_id = ui.interact()
    renpy.transition(dissolve)
    
    if seed_id != "cancel":
      # (seed_id, time of planting, time since planting, current phase)
      persistent.garden[button] = (seed_id, time.time(), 0, 0)
      print "Planted seed", seed_id, "to spot", button
    
    return
