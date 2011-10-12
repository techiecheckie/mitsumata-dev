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
    
    print "Initializing inventory..."
    
    # Populates the items list, using the items defined in "items.xml"
    items_xml = xml.parse(renpy.loader.transfn("../items.xml"))
    item_elements = items_xml.findall("item")
    for item_element in item_elements:
      id          = item_element.get("id")
      name        = item_element.find("name").text
      description = item_element.find("description").text
      locations_list  = item_element.findall("location")
      
      locations = []
      
      for location in locations_list:
        decision = location.get("decision")
        room     = location.get("room")
        stash    = location.get("stash")
        locations.append([decision, room, stash])
        
      item = Item(id, name, description, locations)
      
      if persistent_manager.has_item(id):
        item.unlock()
        unlock_count += 1
        print "  Unlocked item", item.get_id()
        
      self.items.append(item)
      
    print "  Done, ", len(self.items), "items read into memory (%d items unlocked)" % unlock_count
  
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
        print "Inventory: unlocked item", item.get_id()
        return
    print "[WARN] Could not unlock item, no such id found (id: %s)" % id
  
  def get_items(self):
    return self.items
    
  def get_available_items(self, decision):
    items = []
    for item in self.items:
      if item.is_locked() and item.is_available(decision):
        items.append(item)
    return items
  
  def change_state(self):
    self.enabled = not self.enabled
  
  def disable(self):
    self.enabled = False
    
  def enable(self):
    self.enabled = True
  
  def is_enabled(self):
    return self.enabled
    