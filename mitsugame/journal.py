class Journal():
  def __init__(self, id): 
    self.id = id
    self.entries = []
  
  def add_entry(self, entry):
    self.entries.append(entry)

  def get_entries(self):
    return self.entries
    
  def get_entry(self, id):
    for entry in self.entries:
      if entry.get_id() == id:
        return entry
    return None
    
  def get_id(self):
    return self.id
