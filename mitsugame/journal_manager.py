import renpygame as pygame

import xml.etree.ElementTree as xml
import renpy
from journal import Journal
from journal_entry import Journal_entry

class Journal_manager():
  def __init__(self):
    self.enabled = False
    self.selected_journal = None

    # Journal creation, simple xml parsing
    self.journals = []
    journals_xml = xml.parse(renpy.loader.transfn("../journal.xml"))
    
    journal_elements = journals_xml.findall("journal")
    for journal_element in journal_elements:
      id = journal_element.get("id")
      journal = Journal(id)
      
      # Add all the journal's entries to the actual journal
      entries_element = journal_element.findall("entries")
      entry_elements = entries_element[0].findall("entry") 
      for entry_element in entry_elements:
        journal.add_entry(entry_element)
      
      self.journals.append(journal)
      
    print "Journal initialized,", len(self.journals), "journals read into memory"

  def change_state(self):
    if self.enabled:
      self.disable()
    else:
      self.enabled = True
  
  # Returns the journal page's status  
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