from mitsugame.item import Item
import xml.etree.ElementTree as xml
import renpy

class Inventory():
  def __init__(self, persistent_manager):
    self.persistent_manager = persistent_manager
    self.items = []
    self.enabled = False
    
    # Debug counter
    unlock_count = 0
    
    # Populates the items list, using the items defined in "items.xml"
    items_xml = xml.parse(renpy.loader.transfn("../items.xml"))
    item_elements = items_xml.findall("item")
    for item_element in item_elements:
      id          = item_element.get("id")
      name        = item_element.find("name")
      description = item_element.find("description")
      
      item = Item(id, name.text, description.text)
      
      if persistent_manager.has_item(id):
        item.unlock()
        unlock_count += 1
        
      self.items.append(item)
      
    print "Inventory initialized,", len(self.items), "items read into memory (%d items unlocked)" % unlock_count
  
  def has_item(self, id):
    for item in self.items:
      if item.get_id() == item_id:
        return True
    return False

  def get_item(self, id):
    for item in self.items:
      if item.get_id() == id:
        return item
    return None
    
  def unlock_item(self, id):
    for item in self.items:
      if item.get_id() == id:
        item.unlock()
        self.persistent_manager.add_item(id)
        return
    print "[WARN] Could not unlock item, no such id found (id: %s)" % id
  
  def get_items(self):
    return self.items
  
  def change_state(self):
    self.enabled = not self.enabled
  
  def disable(self):
    self.enabled = False
  
  def is_enabled(self):
    return self.enabled
    