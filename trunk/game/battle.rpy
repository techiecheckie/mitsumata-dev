label battle(player_name, mob_name, mob_count, background):
  call prepare_battle_animations

  python:
    # Sprite zoom value
    zoom = 2.0
  
    messages = []
  
    class Fighter(object):
      def __init__(self, name, id, health, mana, damage_melee, damage_magic, x, y, zorder):
        self.name = name
        self.id = id
        self.health = health
        self.mana = mana
        self.damage_melee = damage_melee
        self.damage_magic = damage_magic
        self.x = x
        self.y = y
        self.zorder = zorder
        
      def get_name(self):
        return self.name
        
      def get_id(self):
        return self.id
        
      def get_x(self):
        return self.x
        
      def get_y(self):
        return self.y
        
      def get_zorder(self):
        return self.zorder
       
      def get_health(self):
        return self.health
        
      def dec_health(self, amount):
        self.health -= amount
        
      def get_mana(self):
        return self.mana
        
      def dec_mana(self, amount):
        self.mana -= amount
        
      def can_afford_magic(self):
        some_test_value = 20
        return self.mana >= some_test_value
        
      def attack(self, target, action, damage, critical, attack_distance, messages):
        if critical:
          damage *= 2
          
        target.dec_health(damage)
      
        # The rest of this is drawing shite (slide into position, attack, slide back)
        renpy.show(self.id + " idle", at_list = [slide(0.5, target.get_x()-attack_distance, target.get_y())], zorder=self.zorder)
        renpy.pause(0.5)
      
        messages.append(target.get_name() + " is hit for " + str(damage) + " points.")
        if critical:
            messages.append("Critical hit!")
        
        renpy.show(self.id + " " + action, zorder=target.get_zorder())
        if target.get_health() > 0:
          if critical:
            renpy.show(target.get_id() + " hit_crit", zorder=target.get_zorder())
          else:
            renpy.show(target.get_id() + " hit", zorder=target.get_zorder())
          renpy.pause(animation_delays[self.name + " " + action])
          renpy.show(target.get_id() + " idle", zorder=target.get_zorder())
        else:
          messages.append(target.get_name() + " dies.")      
          renpy.show(target.get_id() + " dead", zorder=target.get_zorder())
          renpy.pause(animation_delays[self.name + " " + action])
       
        renpy.show(self.id + " idle", at_list = [slide(0.5, self.x, self.y)], zorder=self.zorder)
        renpy.pause(0.5)
       
       
    class Player(Fighter):
      def __init__(self, id, health, mana):
        super(Player, self).__init__(id, id, health, mana, 25, 50, 800, 480, 1)
        
      def attack(self, target, messages):
        if action == "melee":
          damage = self.damage_melee
        elif action == "magic":
          damage = self.damage_magic
          self.mana -= 20
        
        # Player's crit chance may vary, using hard-coded values for now
        if random.randint(1,20) == 20:
          critical = True
        else:
          critical = False
          
        Fighter.attack(self, target, action, damage, critical, -60, messages)
       
       
    class Mob(Fighter):
      def __init__(self, name, id, health, mana, damage_melee, damage_magic, x, y, zorder):
        super(Mob, self).__init__(name, id, health, mana, damage_melee, damage_magic, x, y, zorder)
        
      def attack(self, target, messages):
        # Refactor this shite
        if self.mana > 0:
          # See if the attack should be melee or a magical one
          # "randomize two numbers, then multiply them with each other. If  the 
          # number comes out to be odd, it' a magic attack. Even, it's a regular 
          # attack"
          value1 = random.randint(1,10)
          value2 = random.randint(1,10)
          value3 = value1 * value2
          if value3 % 2 == 0:
            action = "magic"
            damage = self.damage_magic
          else:
            action = "melee"
            damage = self.damage_melee
        else:
          action = "melee"
          damage = self.damage_melee
          
        # Mobs have a 5% critical hit chance 
        if random.randint(1,20) == 20:
          critical = True
        else:
          critical = False
          
        Fighter.attack(self, target, action, damage, critical, 60, messages)
        
        
    def create_mobs(mob_name, mob_count, mob_positions):
      mobs = []
      zorder = 4
      if mob_name == "Demon hunter":
        for i in range(0, mob_count):
          id = "DemonHunter_" + str(i)
          health = 50
          mana = 0
          damage_melee = 10
          damage_magic = 0
          # Copy the default images mentioned in battle_animations.rpy to named ones
          renpy.copy_images("DemonHunter idle",   id + " idle")
          renpy.copy_images("DemonHunter hit",    id + " hit")
          renpy.copy_images("DemonHunter dead",   id + " dead")
          renpy.copy_images("DemonHunter melee",  id + " melee")
          
          x = mob_positions[i][0]
          y = mob_positions[i][1]
          mobs.append(Mob(mob_name, id, health, mana, damage_melee, damage_magic, x, y, zorder))
          
          zorder += 1
        
      elif mob_name == "Mamoru":
        health = 100
        mana = 100
        damage_melee = 20
        damage_magic = 25
        x = mob_positions[1][0]
        y = mob_positions[1][1]
        mobs.append(Mob(mob_name, "Mamoru", health, mana, damage_melee, damage_magic, x, y, zorder))

      return mobs
  
  
    def show_target_list(mobs):
      ui.frame(xpos=50, ypos=100, xmaximum=230, background=None)
      ui.vbox()
      ui.text("Select target:", xfill=True)
      for mob in mobs:
        if mob.get_health() > 0:
          ui.textbutton(mob.get_name() + ", " + str(mob.get_health()) + " HP", clicked=ui.returns(mob), xfill=True) 
      ui.close()
      
      return
  
  
    def show_action_list(player, target):
      ui.frame(xpos=50, ypos=100, xmaximum=230, background=None)
      ui.vbox()
      ui.text(mob_name + ", " + str(target.get_health()) + " HP")
      ui.textbutton("Attack: melee", clicked=ui.returns("melee"), xfill=True)
      if player.can_afford_magic():
        ui.textbutton("Attack: magic", clicked=ui.returns("magic"), xfill=True)
      else:
        ui.text("Attack: magic (not enough mana)")
      ui.textbutton("Cancel", clicked=ui.returns("cancel"), xfill=True) 
      ui.close()
      
      return
      
      
    def show_battle_messages(messages):
      messages.append("")
      messages.append("Click to continue...")
      
      ui.frame(xpos=50, ypos=100, xmaximum=300, background=None)
      ui.vbox()
      for message in messages:
        ui.text(message)
      ui.close()
      
      ui.frame(xpos=0, ypos=0, background=None)
      ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
      ui.interact()
      
      del messages[:]
      
      return

     
    # Create the combatants
    player = Player(player_name, hp, mp)
    
    mob_positions = [(420,420), (400,450), (450,480)]
    mobs = create_mobs(mob_name, mob_count, mob_positions)
    mobs_alive = len(mobs)
    
    # Update the screen elements
    hide_main_ui()
    show_minigame_ui(background, player.get_health(), player.get_mana(), True)
    
    renpy.show(player.get_id() + " idle", at_list = [Position(xpos=player.get_x(), ypos=player.get_y()), Transform(zoom=zoom)], zorder=player.get_zorder())
    
    for i in range(0,len(mobs)):
      renpy.show(mobs[i].get_id() + " idle", at_list = [Position(xpos=mobs[i].get_x(), ypos=mobs[i].get_y()), Transform(zoom=zoom)], zorder=mobs[i].get_zorder())
  
    # And start the actual battle loop
    while player.get_health() > 0 and mobs_alive > 0:
      show_target_list(mobs)
      target = ui.interact()
      show_action_list(player, target)
      action = ui.interact()
      
      if action != "cancel":
        player.attack(target, messages)
        
        update_minigame_ui(player.get_health(), player.get_mana())
        show_battle_messages(messages)
        
        mobs_alive = 0
        for i in range(0, len(mobs)):
          mob = mobs[len(mobs)-1-i]
          if mob.get_health() > 0:
            mobs_alive += 1
            mob.attack(player, messages)
            if player.get_health() <= 0:
              break
        
        if mobs_alive > 0:
          update_minigame_ui(player.get_health(), player.get_mana())
          show_battle_messages(messages)

    messages.append("Some post-battle message")
    show_battle_messages(messages)
          
    # When done, hide all the images and clear other resources
    renpy.hide(player.get_id())
    for mob in mobs:
      renpy.hide(mob.get_id())
    
    del mobs[:]
 
    # Update main HP and MP so that the changes are visible outside the battle, too
    hp = player.get_health()
    mp = player.get_mana()
    
    player = None
  
    hide_minigame_ui(background, True)
    show_main_ui(hp, mp)
  
  return
  