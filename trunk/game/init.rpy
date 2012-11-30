init python:
  from mitsugame.inventory import Inventory
  from mitsugame.journal_manager import Journal_manager
  import time
  
  # Persistent values stored in the special persistent object:
  #
  # Unlocked items
  #   Enabling PDA icon highlight (False for items that haven't been checked yet):
  #     persistent.unlocked_items["knife"] = False
  #   See the correct item names in items.xml.
  #
  # Unlocked journals
  #   Same as items, but the dict item contains info about the unlocked journal
  #   entries, too.
  #     persistent.unlocked_journals["Susa"] = [False, "019", "017"]
  #   See the correct journal & entry values in journal.xml.
  #
  # Unlocked minigames
  #   Same as before, but without icon blink flags for checked status. Each 
  #   minigame dict item contains the current high score and level values.
  #     persistent.unlocked_minigames["mole"] = [0, 1]
  #   See the correct minigame names in minigames.rpy.
  
  # Create new persistent dicts if they don't already exist.
  #if persistent.unlocked_items == None:
  persistent.unlocked_items = {}
  #if persistent.unlocked_journals == None:
  persistent.unlocked_journals = {}
  if persistent.unlocked_minigames == None:
    persistent.unlocked_minigames = {}
    # Unlock a few minigames for the demo. Remove when done.
    persistent.unlocked_minigames["cell"]   = [0, 1]
    persistent.unlocked_minigames["squats"] = [0, 1]
    persistent.unlocked_minigames["duck"]   = [0, 1]
  if persistent.garden == None:
    persistent.garden = [None]*9 #[None]*len(GARDEN_GRID)
  
  inventory = Inventory(persistent)
  journal_manager = Journal_manager(persistent)
  
  # To simplify the usage of inventory.item_unlocked(id). 
  # (Is this necessary anymore?)
  item_unlocked = inventory.item_unlocked
  
  # New game default values. Main stat values should only be modified through the
  # script file ($HP+=50 etc.) and the bonus values left untouched. Stat bonuses
  # are item and minigame rewards.
  HP           = 0
  MP           = 0
  CLICKS       = 5
  BONUS_HP     = 0
  BONUS_MP     = 0
  BONUS_CLICKS = 0
  
  # Nightly decision value. Determines the items and random encounters used in
  # the map screen.
  decision = "0"
  
  # The UI's PDA button lock status. Disabled by default until unlocked in the script.
  pda = False
  
  # Used in counting the phases of the plants/seeds growing in the garden
  START_TIME = time.time()
  
  # Methods
  
  # Appends the item id to the persistent unlocked_items list and displays 
  # information about the unlocked item by calling the function show_item_unlock
  def unlock_item(item_id, show_messages):
    item = inventory.get_item(item_id)
    if (item != None):
      persistent.unlocked_items[item_id] = False
      if show_messages:
        show_item_unlock(item)
    else:
      message = "Warning: item '%s' not found" % entry_id
      show_message(message, "medium")
      renpy.log(message)
    
    update_stats()
    
    return
  
  # Removes the item id from the persistent unlocked_items list.
  def lock_item(item_id, show_messages):
    del persistent.unlocked_items[item_id]
    return
  
  # Appends entry_id to the journal specific array located in persistent.unlocked_journals dict.
  def unlock_entry(journal_id, entry_id, show_messages):
    journal = journal_manager.get_journal(journal_id)
    if (journal != None):
      entry = journal.get_entry(entry_id)
      if (entry != None):
        if (journal_id in persistent.unlocked_journals):
          journal_array = persistent.unlocked_journals[journal_id]
          journal_array[0] = False
          if (entry_id not in journal_array):
            journal_array.append(entry_id)
        else:
          journal_array = [False, entry_id]
          
        persistent.unlocked_journals[journal_id] = journal_array
        
        if (show_messages):
          show_entry_unlock(journal, entry)
      else:
        message = "Warning: entry '%s' not found." % entry_id
        show_message(message, "medium")
        renpy.log(message)
    else:
      message = "Warning: journal '%s' not found" % journal_id
      show_message(message, "medium")
      renpy.log(message)
    
    return
    
  # Appends the minigame's name to the persistent unlocked_minigames list.
  def unlock_minigame(minigame):
    if minigame not in persistent.unlocked_minigames:
      persistent.unlocked_minigames.append(minigame)
      
    return
  
  # Main stat update function. Uses the variables returned by get_item_bonuses() 
  # and get_minigame_bonuses() functions to recount bonus stat values. The bonus
  # values are usually added to the main stats (HP/MP/CLICKS) when, say, entering
  # combat.
  def update_stats():
    global BONUS_HP
    global BONUS_MP
    global BONUS_CLICKS
    
    BONUS_HP     = 0
    BONUS_MP     = 0
    BONUS_CLICKS = 0
    #battle_crit_chance  = 0
    #battle_melee_damage = 0
    #battle_magic_damage = 0
  
    (item_hp, item_mp, item_clicks) = get_item_bonuses()
    BONUS_HP += item_hp
    BONUS_MP += item_mp
    BONUS_CLICKS += item_clicks
    
    (mini_hp, mini_mp) = get_minigame_bonuses()
    BONUS_HP += mini_hp
    BONUS_MP += mini_mp
    
    renpy.log("Base values: HP %s, MP %s, CLICKS %s" % (HP, MP, CLICKS))
    renpy.log("Recounted bonus values: BONUS_HP %s, BONUS_MP %s, BONUS_CLICKS %s" % (BONUS_HP, BONUS_MP, BONUS_CLICKS))
    
    return
  
  # Loops through the unlocked items, adding their bonuses (if any, see items.xml
  # and look for <bonuses> elements) to local stat variables, which are then
  # returned to update_stats() function above.
  def get_item_bonuses():
    hp     = 0
    mp     = 0
    clicks = 0
    
    items  = inventory.get_unlocked_items()
    for item in items:
      bonuses = item.get_bonuses()
      if bonuses != None:
        if bonuses.has_key("hp"):
          hp += int(bonuses["hp"])
        if bonuses.has_key("mp"):
          mp += int(bonuses["mp"])
        if bonuses.has_key("clicks"):
          clicks += int(bonuses["clicks"])

    return (hp, mp, clicks)
  
  # Loops through the unlocked minigames, matching their names to the bonus rows
  # listed in minigame.rpy, and adding any found bonuses to local stat variables.
  # These local variables are then returned to update_stats() function above.
  def get_minigame_bonuses():
    hp = 0
    mp = 0
  
    minigame_keys = persistent.unlocked_minigames.keys()
    
    for key in minigame_keys:
      if MINIGAME_BONUSES.has_key(key):
        game_bonuses = MINIGAME_BONUSES[key]
        for bonus_row in game_bonuses:
          if persistent.unlocked_minigames[key][0] >= bonus_row[0]:
            for i in range(1, len(bonus_row)):
              if bonus_row[i][0] == "hp":
                hp += bonus_row[i][1]
              elif bonus_row[i][0] == "mp":
                mp += bonus_row[i][1]
            break
      else:
        renpy.log("No game %s in MINIGAME_BONUSES" % key)
    
    return (hp,mp)
  
  # Unlocks a bonus (clickable element?) in the bonus section of the main menu.
  # The bonus section is hidden by default until one item that unlocks one of
  # the bonus sub-menus is unlocked (item = item, journal, minigame bonus, or
  # ending). Feels rather... clumsy, and it probably is just that, but it will
  # also probably be redefined once the details of the bonus section are laid
  # out.
  def unlock_bonus(bonus_area, bonus_id):
    if (bonus_area not in persistent.bonus.keys()):
      renpy.log("No bonus area '%s' found." % bonus_area)
      return
      
    if (bonus_id not in persistent.bonus[bonus_area]):
      persistent.bonus[bonus_area].append(bonus_id)
      persistent.bonus[bonus_area][0] = True
      persistent.bonus["unlocked"]    = True
