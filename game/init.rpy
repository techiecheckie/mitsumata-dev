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
  HP     = 350
  MP     = 50
  CLICKS = 30
  decision = "0"
  pda      = False
  
  # Used in counting the phases of the plants/seeds growing in the garden
  START_TIME = time.time()
  
  # testing stuff begins
  print ""
  
  pda = True
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
  
  persistent.minigame_scores["mole"]       = 0
  persistent.minigame_scores["cell"]       = 0
  persistent.minigame_scores["platformer"] = 0
  persistent.minigame_scores["duck"]       = 0
  persistent.minigame_scores["force"]      = 0
  persistent.minigame_scores["power"]      = 0
  persistent.minigame_scores["squats"]     = 0
  persistent.minigame_scores["gears"]      = 0
  
  persistent.minigame_levels["mole"]       = 1
  persistent.minigame_levels["cell"]       = 1
  persistent.minigame_levels["platformer"] = 1
  persistent.minigame_levels["duck"]       = 1
  persistent.minigame_levels["force"]      = 1
  persistent.minigame_levels["power"]      = 1
  persistent.minigame_levels["squats"]     = 1
  persistent.minigame_levels["gears"]      = 2
  
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
  persistent.unlocked_items.append("parts")
  persistent.unlocked_items.append("blue")
  
  persistent.unlocked_journals = []
  persistent.unlocked_journals.append("Riku:001")
  persistent.unlocked_journals.append("Riku:002")
  persistent.unlocked_journals.append("Riku:004")
  persistent.unlocked_journals.append("Roman:005")
  persistent.unlocked_journals.append("Susa:019")

  persistent.garden = [None]*9
