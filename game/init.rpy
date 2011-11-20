init python:
  # Moving stuff from the main script here 
  def init():
    print ""

    if persistent.unlocked_items == None:
      persistent.unlocked_items = []
    if persistent.unlocked_journals == None:
      persistent.unlocked_journals = []
    if persistent.unlocked_minigames == None:
      persistent.unlocked_minigames = []
  
    inventory = Inventory(persistent)
    journal_manager = Journal_manager(persistent)
  
    # New game default values
    hp    = 0
    mp    = 0
    tries = 3
  
    decision = "0"

    pda = False
