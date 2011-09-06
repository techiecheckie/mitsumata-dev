from journal_entry import Journal_entry
import xml.etree.ElementTree as xml

class Journal():
  def __init__(self, id): 
    self.id = id
    self.entries = []
    self.locked = True
  
  # Adds an entry to the journal's entries list.
  def add_entry(self, entry_element):
    entry = Journal_entry(entry_element)
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
    
  def unlock(self):
    self.locked = False
    
  def is_locked(self):
    return self.locked