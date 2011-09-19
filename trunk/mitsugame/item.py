class Item():
  def __init__(self, id, name, description, decisions):
    self.id = id
    self.name = name
    self.description = description
    self.decisions = decisions.split(",")
    
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
    
  def has_decision(self, decision):
    if "any" in self.decisions:
      return True
    else:
      return decision in self.decisions