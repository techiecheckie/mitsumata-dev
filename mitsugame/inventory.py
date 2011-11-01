from mitsugame.item import Item
import xml.etree.ElementTree as xml
import renpy

class Inventory():
  def __init__(self):
    self.items = []
    self.enabled = False
    
    # Populates the items list, using the items defined in "items.xml"
    items_xml = xml.parse(renpy.loader.transfn("../items.xml"))
    item_elements = items_xml.findall("item")
    for item_element in item_elements:
      id          = item_element.get("id")
      name        = item_element.find("name").text
      description = item_element.find("description").text
      locations = item_element.find("locations")
      
      item_locations = None
      item_bonuses   = None
      
      if locations != None:
        item_locations = []
        
        # Map
        map_locations = locations.findall("map")
        for map_location in map_locations:
         item_location = {}
         item_location["location"] = "map"
         item_location["decision"] = map_location.get("decision")
         item_location["room"]     = map_location.get("room")
         # Not used yet (if ever)
         #item_location["stash"]    = map_location.get("stash")
        
         item_locations.append(item_location)
        
        # Shop; could do better as a separated chunk, but this'll do for now
        shop_locations = locations.findall("shop")
        for shop_location in shop_locations:
          item_location = {}
          item_location["location"] = "shop"
          item_location["decision"] = shop_location.get("decision")
      
          item_locations.append(item_location)
        
      bonuses = item_element.find("bonuses")
      if bonuses != None:
        item_bonuses =  {}
        for bonus in bonuses:
          item_bonuses[bonus.tag] = bonus.text    
              
      item = Item(id, name, description, item_locations, item_bonuses)
        
      self.items.append(item)

  def get_item(self, id):
    for item in self.items:
      if item.get_id() == id:
        return item
    return None
    
  def unlock_item(self, id):
    item = self.get_item(id)
    if item != None:
      item.unlock()
      return
    print "[WARN] Could not unlock item, no such id found (id: %s)" % id
  
  def item_unlocked(self, item_id):
    item = self.get_item(item_id)
    if item == None:
      print "[WARN] No item found with id '%s'" % item_id
      return False
    else:
      return not item.is_locked()
  
  def get_inventory_items(self):
    return self.items
    
  def get_items(self, decision, location):
    items = []
    for item in self.items:
      if item.is_available(decision, location):
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
    