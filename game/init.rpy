init python:
  from mitsugame.inventory import Inventory
  from mitsugame.journal_manager import Journal_manager
  import time

  if persistent.unlocked_items == None:
    persistent.unlocked_items = []
  if persistent.unlocked_journals == None:
    persistent.unlocked_journals = []
  if persistent.unlocked_minigames == None:
    persistent.unlocked_minigames = []
  if persistent.minigame_scores == None:
    persistent.minigame_scores = {}
  if persistent.minigame_levels == None:
    persistent.minigame_levels = {}
  if persistent.garden == None:
    persistent.garden = [None]*9 #[None]*len(GARDEN_GRID)
  
  inventory = Inventory(persistent)
  journal_manager = Journal_manager(persistent)
  
  # New game default values
  HP     = 0
  MP     = 0
  CLICKS = 30
  decision = "0"
  pda      = False
  
  # Used in counting the phases of the plants/seeds growing in the garden
  START_TIME = time.time()
  
  # testing stuff begins
  print ""
  
  pda = True
  # current unlocked minigames
  persistent.unlocked_minigames = []
  persistent.unlocked_minigames.append("mole")
  persistent.unlocked_minigames.append("cell")
  persistent.unlocked_minigames.append("platformer")
  persistent.unlocked_minigames.append("duck")
  persistent.unlocked_minigames.append("force")
  persistent.unlocked_minigames.append("power")
  persistent.unlocked_minigames.append("squats")
  persistent.unlocked_minigames.append("gears")
  persistent.unlocked_minigames.append("garden")
  persistent.unlocked_minigames.append("lock")
  persistent.unlocked_minigames.append("bottles")
  
  # current scores
  persistent.minigame_scores["mole"]       = 0
  persistent.minigame_scores["cell"]       = 0
  persistent.minigame_scores["platformer"] = 0
  persistent.minigame_scores["duck"]       = 0
  persistent.minigame_scores["force"]      = 0
  persistent.minigame_scores["power"]      = 0
  persistent.minigame_scores["squats"]     = 0
  persistent.minigame_scores["gears"]      = 0
  
  # current levels
  persistent.minigame_levels["mole"]       = 1
  persistent.minigame_levels["cell"]       = 1
  persistent.minigame_levels["platformer"] = 1
  persistent.minigame_levels["duck"]       = 1
  persistent.minigame_levels["force"]      = 1
  persistent.minigame_levels["power"]      = 1
  persistent.minigame_levels["squats"]     = 1
  persistent.minigame_levels["gears"]      = 2
  persistent.minigame_levels["lock"]       = 1
  
  # current unlocked items
  persistent.unlocked_items = []
  persistent.unlocked_items.append("knife")
  persistent.unlocked_items.append("pda")
  persistent.unlocked_items.append("map")
  persistent.unlocked_items.append("garden")
  persistent.unlocked_items.append("aos")
  persistent.unlocked_items.append("bos")
  persistent.unlocked_items.append("ice")
  persistent.unlocked_items.append("rose")
  persistent.unlocked_items.append("cake")
  persistent.unlocked_items.append("gun")
  persistent.unlocked_items.append("gift")
  #persistent.unlocked_items.append("decor")
  persistent.unlocked_items.append("bircake")
  persistent.unlocked_items.append("key")
  persistent.unlocked_items.append("radio")
  #persistent.unlocked_items.append("parts")
  persistent.unlocked_items.append("blue")
  
  # current unlocked journals
  persistent.unlocked_journals = []
  persistent.unlocked_journals.append("Riku:001")
  persistent.unlocked_journals.append("Riku:002")
  persistent.unlocked_journals.append("Riku:004")
  persistent.unlocked_journals.append("Roman:005")
  persistent.unlocked_journals.append("Susa:019")
  persistent.unlocked_journals.append("Susa:017")
  persistent.unlocked_journals.append("Susa:020")

  # current plants growing in the garden
  persistent.garden = [None]*9
  
  # Appends the item id to the persistent unlocked_items list and displays 
  # information about the unlocked item by calling the function show_item_unlock
  def unlock_item(item_id):
    if item_id not in persistent.unlocked_items:
      persistent.unlocked_items.append(item_id)
    
    item = inventory.get_item(item_id)
    show_item_unlock(item)
    
    return
  
  # Appens the combined journal_id + entry_id to the persistent unlocked_journals
  # list and displays information about the unlocked entry by calling the function
  # show_entry_unlock
  def unlock_entry(journal_id, entry_id):
    new_id = journal_id + ":" + entry_id
    if new_id not in persistent.unlocked_journals:
      persistent.unlocked_journals.append(new_id)
    
    journal = journal_manager.get_journal(journal_id)
    entry   = journal.get_entry(entry_id)
    show_entry_unlock(journal, entry)
    
    return
    
  # Appends the minigame's name to the persistent unlocked_minigames list.
  def unlock_minigame(minigame):
    if minigame not in persistent.unlocked_minigames:
      persistent.unlocked_minigames.append(minigame)
      
    return
  
  # Main stat update function. Uses the variables returned by get_item_bonuses() 
  # and get_minigame_bonuses() functions to count stat values. 
  def update_stats():
    hp     = 0
    mp     = 0
    clicks = 0
    #battle_crit_chance  = 0
    #battle_melee_damage = 0
    #battle_magic_damage = 0
  
    (item_hp, item_mp, item_clicks) = get_item_bonuses()
    hp += item_hp
    mp += item_mp
    clicks += item_clicks
    
    (mini_hp, mini_mp) = get_minigame_bonuses()
    hp += mini_hp
    mp += mini_mp

    global HP
    global MP
    global CLICKS

    HP     = hp
    MP     = mp
    CLICKS = clicks
    
    print "Bonuses: item_hp", item_hp, "item_mp", item_mp, "mini_hp", mini_hp, "mini_mp", mini_mp
    
    return
  
  # Loops through the unlocked items, adding their bonuses (if any, see items.xml
  # and look for <bonuses> elements) to local stat variables, which are then
  # returned to the main stat update function.
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
  # These local variables are then returned to the main stat update function.
  def get_minigame_bonuses():
    hp = 0
    mp = 0
  
    for game in persistent.unlocked_minigames:
      if MINIGAME_BONUSES.has_key(game):
        game_bonuses = MINIGAME_BONUSES[game]
        for bonus_row in game_bonuses:
          if persistent.minigame_scores[game] >= bonus_row[0]:
            for i in range(1, len(bonus_row)):
              if bonus_row[i][0] == "hp":
                hp += bonus_row[i][1]
              elif bonus_row[i][0] == "mp":
                mp += bonus_row[i][1]
            break
      else:
        #print "No game", game, "in MINIGAME_BONUSES"
        pass
    
    return (hp,mp)
