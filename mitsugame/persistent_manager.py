import renpyclass Persistent_manager():  def __init__(self, inventory, journal_manager):     self.inventory = inventory    self.journal_manager = journal_manager      file = open(renpy.loader.transfn("../persistent.txt"), "r")    items_line = (file.readline()).strip("\n\r").strip(" ")    entries_line = (file.readline()).strip("\n\r").strip(" ")    file.close()        # Goes through the ids mentioned in the file and calls for inventory/journal    # manager to unlock them.    item_ids = items_line.split("=")[1].split(" ")    for item_id in item_ids:      if len(item_id) > 0:        inventory.unlock_item(item_id)        entry_ids = entries_line.split("=")[1].split(" ")    for entry_id in entry_ids:      if len(entry_id) > 0:        ids = entry_id.split(":")        journal_manager.unlock_entry(ids[0], ids[1])      def save(self):    items = self.inventory.get_items()    items_string = ""    for item in items:      if not item.is_locked():        items_string += item.get_id() + " "            journals = self.journal_manager.get_journals()    journals_string = ""    for journal in journals:      if not journal.is_locked():        entries = journal.get_entries()        for entry in entries:          if not entry.is_locked():            journals_string += journal.get_id() + ":" + entry.get_id() + " "                file = open(renpy.loader.transfn("../persistent.txt"), "w")    file.write("items=" + items_string.strip(" ") + "\n")    file.write("entries=" + journals_string.strip(" ") + "\n")    file.close()    