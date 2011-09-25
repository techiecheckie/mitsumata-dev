class Item():
  def __init__(self, id, name, description, locations):
    self.id = id
    self.name = name
    self.description = description
    self.locations = locations
    self.current_stash = None
    
    self.locked = True
   
  def get_id(self):
    return self.id
    
  def get_name(self):
    return self.name
    
  def get_description(self):
    return self.description
    
  def unlock(self):
    self.locked = False
    
  def is_locked(self):
    return self.locked
    
  # <location decision="5" room="soume" stash="any" />
  # <location decision="7" room="any" stash="any" />
  #   -->
  # self.locations[
  #   ["5", "soume", "any"],
  #   ["4", "any", "any"]
  # ]
  def is_available(self, decision, room):
    for location in self.locations:
      if location[0] == "any" or location[0] == decision:
        if location[1] == "any" or location[1] == room:
          self.current_stash = location[2]
          return True
    return False
    
  def get_current_stash(self):
    return self.current_stash