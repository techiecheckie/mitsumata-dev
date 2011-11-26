init python:
  from mitsugame.inventory import Inventory
  from mitsugame.journal_manager import Journal_manager

  if persistent.unlocked_items == None:
    persistent.unlocked_items = []
  if persistent.unlocked_journals == None:
    persistent.unlocked_journals = []
  if persistent.unlocked_minigames == None:
    persistent.unlocked_minigames = []
  if persistent.minigame_scores == None:
    persistent.minigame_scores = {}
  
  inventory = Inventory(persistent)
  journal_manager = Journal_manager(persistent)
  
  # New game default values
  hp    = 0
  mp    = 0
  tries = 3
  decision = "0"
  pda      = False
  
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
  
  persistent.minigame_scores["mole"]       = 0
  persistent.minigame_scores["cell"]       = 0
  persistent.minigame_scores["platformer"] = 0
  persistent.minigame_scores["duck"]       = 0
  persistent.minigame_scores["force"]      = 0
  persistent.minigame_scores["power"]      = 0
  persistent.minigame_scores["squats"]     = 0
  persistent.minigame_scores["gears"]      = 0
  
  persistent.unlocked_items = []
  persistent.unlocked_items.append("knife")
  persistent.unlocked_items.append("pda")
  persistent.unlocked_items.append("map")
  persistent.unlocked_items.append("garden")
  
  persistent.unlocked_journals = []
  persistent.unlocked_journals.append("Riku:002")
  
