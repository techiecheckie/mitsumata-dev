class Journal_entry():  def __init__(self, id, title, text, rooms):    self.id = id    self.title = title    self.text = text    self.rooms = rooms        self.locked = True      def get_id(self):    return self.id    def get_title(self):    return self.title      def get_text(self):    return self.text      def unlock(self):    self.locked = False      def is_locked(self):    return self.locked      def has_room(self, room):    if "any" in self.rooms:      return True    else:      return room in self.rooms      # debug      def get_name(self):    return self.title