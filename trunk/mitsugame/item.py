class Item():
  def __init__(self, id, name, description, locations, bonuses):
    self.id = id
    self.name = name
    self.description = description
    self.locations = locations
    self.bonuses = bonuses
    self.locked = True
       
  def get_id(self):
    return self.id
    
  def get_name(self):
    return self.name
    
  def get_description(self):
    return self.description
    
  def get_map_location(self, decision):
    for location in self.locations:
      if location["location"] == "map" and \
         location["decision"] == "any" or  \
         location["decision"] == decision:
        return location
    return None
    
  def unlock(self):
    print "Unlocked item: " + self.id + ", \"" + self.name + "\""
    self.locked = False
    
  def is_locked(self):
    return self.locked
    
  def is_available(self, decision, location):
    if not self.locked or self.locations == None:
      return False
      
    for loc in self.locations:
      if loc["location"] == location and \
         loc["decision"] == "any" or \
         loc["decision"] == decision:
        return True
    return False

  def get_bonuses(self):
    return self.bonuses
    
