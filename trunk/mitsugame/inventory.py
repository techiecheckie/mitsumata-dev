#import sys
#import pygame
#from pygame.locals import *
import renpygame as pygame

from item import Item
import xml.etree.ElementTree as xml
import renpy

class Inventory():
  def __init__(self):
    self.items = []
    self.enabled = False
    
    # populates the items list, using the items defined in "items.xml"
    items_xml = xml.parse(renpy.loader.transfn("../items.xml"))
    item_elements = items_xml.findall("item")
    for item_element in item_elements:
      id          = item_element.get("id")
      name        = item_element.find("name")
      description = item_element.find("description")
      
      item = Item(id, name.text, description.text)
      self.items.append(item)
      
    print "  Inventory initialized,", len(self.items), "items read into memory"
  
  # Checks whether the inventory contains an item with the given name.
  def has_item(self, item_name):
    for item in self.items:
      if item.get_name() == item_name:
        return True
    return False

  # Returns the item that matches the given name.
  def get_item(self, item_name):
    for item in self.items:
      if item.get_name() == item_name:
        return item
    return None
    
  def get_size(self):
    return len(self.items)
  
  def get_items(self):
    return self.items
  
  # Changes the inventory's state, setting it visible if it has previously been
  # hidden, and vice versa. The enabled variable tells whether the inventory
  # screen should be drawn or not.
  def change_state(self):
    self.enabled = not self.enabled
  
  # Disable (hide) the inventory
  def disable(self):
    self.enabled = False
  
  # Returns the status of inventory's visibility
  def is_enabled(self):
    return self.enabled