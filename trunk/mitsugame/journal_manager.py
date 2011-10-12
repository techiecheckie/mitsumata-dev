import xml.etree.ElementTree as xml
import renpy
from journal import Journal
from journal_entry import Journal_entry

class Journal_manager():
  def __init__(self, persistent_manager):
    self.persistent_manager = persistent_manager
    self.journals = []
    self.enabled = False
    self.selected_journal = None
    
    # Debug counter
    unlock_count = 0
    
    print "Initializing journals..."
    
    # Journal creation, simple xml parsing
    journals_xml = xml.parse(renpy.loader.transfn("../journal.xml"))
    journal_elements = journals_xml.findall("journal")
    for journal_element in journal_elements:
      journal_id = journal_element.get("id")
      journal = Journal(journal_id)
      
      # Add all the journal's entries to the actual journal
      entries_element = journal_element.findall("entries")
      entry_elements = entries_element[0].findall("entry") 
      for entry_element in entry_elements:
        entry_id = entry_element.get("id")
        title    = (entry_element.find("title")).text
        text     = (entry_element.find("content")).text
        
        entry = Journal_entry(entry_id, title, text)
      
        journal.add_entry(entry)
        
        # Unlock the journal and the entry if they have been unlock before
        if persistent_manager.has_journal_entry(journal_id, entry_id):
          journal.unlock()
          entry.unlock()
          unlock_count += 1
          print "  Unlocked journal", journal.get_id(), "entry", entry.get_id()
      
      self.journals.append(journal)
      
    print "  Done,", len(self.journals), "journals read into memory (%d entries unlocked)" % unlock_count

  def change_state(self):
    if self.enabled:
      self.disable()
    else:
      self.enabled = True
  
  def is_enabled(self):
    return self.enabled
  
  def disable(self):
    self.enabled = False
    
  def get_journals(self):
    return self.journals
    
  def get_journal(self, id):
    for journal in self.journals:
      if journal.get_id() == id:
        self.selected_journal = journal
        return journal
        
    self.selected_journal = None
    return None
    
  def get_selected_journal(self):
    return self.selected_journal
    
  def unlock_entry(self, journal_id, entry_id):
    for journal in self.journals:
      if journal.get_id() == journal_id:
        for entry in journal.get_entries():
          if entry.get_id() == entry_id:
            entry.unlock()
            journal.unlock()
            self.persistent_manager.add_journal_entry(journal_id, entry_id)
            return
    print "[WARN] Could not unlock entry, no such id found (journal_id: %s, entry_id: %s)" % (journal_id, entry_id)