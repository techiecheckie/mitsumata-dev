init python:
  # Sprite zoom value
  ZOOM = 2.0
  ATTACK_DISTANCE = 80 # the distance between the attacker and the target (visual effect only)
    
  MOB_CRIT_CHANCE     = 20 # 5% chance, 1-20
  MOB_CRIT_MULTIPLIER = 2
    
  MAMORU_HEALTH = 100
  MAMORU_MANA   = 100
  MAMORU_MELEE  = 20
  MAMORU_MAGIC  = 25
  MAMORU_MAGIC_OFFSET = 0
  
  NAOMI_HEALTH  = 100
  NAOMI_MANA    = 100
  NAOMI_MELEE   = 20
  NAOMI_MAGIC   = 20
  NAOMI_MAGIC_OFFSET = 100
    
  DEMON_THUG_HEALTH = 25
  DEMON_THUG_MANA   = 0
  DEMON_THUG_MELEE  = 10
  DEMON_THUG_MAGIC  = 0
    
  DEMON_HUNTER_HEALTH = 50
  DEMON_HUNTER_MANA   = 0
  DEMON_HUNTER_MELEE  = 10
  DEMON_HUNTER_MAGIC  = 0
  
  ROMAN_MAGIC_OFFSET = 50
  
  MOB_POSITIONS = [(420,420), (400,450), (450,480)]
  
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
      # TODO: use proper spell costs
      some_test_value = 20
      return self.mana >= some_test_value

    def show_attack(self, target, action, damage, critical, attack_distance):
      # slide animation
      renpy.show(self.id + " idle", at_list = [slide(ANIMATION_DELAYS["slide"], 
                                              target.get_x()-attack_distance, 
                                              target.get_y())], 
                                              zorder=self.zorder)
      renpy.pause(ANIMATION_DELAYS["slide"])
        
      # attack animation
      renpy.show(self.id + " " + action, zorder=target.get_zorder())

      # target waits a bit for the blow to fall, then plays the animation
      renpy.pause(HIT_DELAYS[self.name + " " + action])
      if target.get_health() > 0:
        if critical:
          renpy.show(target.get_id() + " hit_crit", zorder=target.get_zorder())
        else:
          renpy.show(target.get_id() + " hit", zorder=target.get_zorder())
        renpy.pause(ANIMATION_DELAYS[self.name + " " + action] - HIT_DELAYS[self.name + " " + action])
        renpy.show(target.get_id() + " idle", zorder=target.get_zorder())
      else:
        renpy.show(target.get_id() + " dead", zorder=target.get_zorder())
        renpy.pause(ANIMATION_DELAYS[self.name + " " + action] - HIT_DELAYS[self.name + " " + action])
      
      # slide back
      renpy.show(self.id + " idle", at_list = [slide(ANIMATION_DELAYS["slide"], 
                                               self.x, 
                                               self.y)], 
                                               zorder=self.zorder)
      renpy.pause(ANIMATION_DELAYS["slide"])      
       
  class Player(Fighter):
    def __init__(self, id, health, mana):
      # TODO: set proper melee and magic damage values
      super(Player, self).__init__(id, id, health, mana, 10, 50, 800, 480, 1)
        
    def attack(self, target, action, messages):
      attack_offset = 0
      if action == "melee":
        damage = self.damage_melee
      elif action == "magic":
        damage = self.damage_magic
        if self.name == "Roman":
          attack_offset = ROMAN_MAGIC_OFFSET
         
        # TODO: add any bonuses that items give
        self.mana -= 10 
        
      # Player's crit chance may vary, using hard-coded values for now, TODO
      if random.randint(1,20) == 20:
        critical = True
        damage *= 2
        messages.append("Critical hit!")
      else:
        critical = False
          
      target.dec_health(damage)
      messages.append(target.get_name() + " is hit for " + str(damage) + " points.")
      if target.get_health() <= 0:
        messages.append(target.get_name() + " dies.")
          
      Fighter.show_attack(self, target, action, damage, critical, -ATTACK_DISTANCE - attack_offset)
       
       
  class Mob(Fighter):
    def __init__(self, name, id, health, mana, damage_melee, damage_magic, x, y, zorder):
      super(Mob, self).__init__(name, id, health, mana, damage_melee, damage_magic, x, y, zorder)
        
    def attack(self, target, messages):
      attack_offset = 0
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
          if self.name == "Naomi":
            attack_offset = NAOMI_MAGIC_OFFSET
        else:
          action = "melee"
          damage = self.damage_melee
      else:
        action = "melee"
        damage = self.damage_melee
          
      # Mobs have a 5% critical hit chance 
      if random.randint(1,MOB_CRIT_CHANCE) == MOB_CRIT_CHANCE:
        critical = True
        damage *= MOB_CRIT_MULTIPLIER
        messages.append("Critical hit!")
      else:
        critical = False
          
      target.dec_health(damage)
      messages.append(target.get_name() + " is hit for " + str(damage) + " points.")
      if target.get_health() <= 0:
        messages.append(target.get_name() + " dies.")
          
      Fighter.show_attack(self, target, action, damage, critical, ATTACK_DISTANCE + attack_offset)
       
        
  def create_mobs(mob_name, mob_count):
    mobs = []
    zorder = 4
    if mob_name == "Demon hunter":
      create_normal_mobs(mob_name, "DemonHunter",
                         DEMON_HUNTER_HEALTH, DEMON_HUNTER_MANA,
                         DEMON_HUNTER_MELEE, DEMON_HUNTER_MAGIC,
                         mobs, mob_count, zorder)
    elif mob_name == "Demon thug":
      create_normal_mobs(mob_name, "DemonThug", 
                         DEMON_THUG_HEALTH, DEMON_THUG_MANA,
                         DEMON_THUG_MELEE, DEMON_THUG_MAGIC,
                         mobs, mob_count, zorder)
    elif mob_name == "Mamoru":
      health       = MAMORU_HEALTH
      mana         = MAMORU_MANA
      damage_melee = MAMORU_MELEE
      damage_magic = MAMORU_MAGIC
      x = MOB_POSITIONS[1][0]
      y = MOB_POSITIONS[1][1]
      mobs.append(Mob(mob_name, "Mamoru", health, mana, damage_melee, damage_magic, x, y, zorder))
    elif mob_name == "Naomi":
      health       = NAOMI_HEALTH
      mana         = NAOMI_MANA
      damage_melee = NAOMI_MELEE
      damage_magic = NAOMI_MAGIC
      x = MOB_POSITIONS[1][0]
      y = MOB_POSITIONS[1][1]
      mobs.append(Mob(mob_name, "Naomi", health, mana, damage_melee, damage_magic, x, y, zorder))

    return mobs
      
      
  def create_normal_mobs(real_name, pic_name, health, mana, damage_melee, damage_magic, mobs, mob_count, zorder):
    for i in range(0, mob_count):
      id = pic_name + "_" + str(i)
         
      renpy.copy_images(pic_name + " idle",     id + " idle")
      renpy.copy_images(pic_name + " hit",      id + " hit")
      renpy.copy_images(pic_name + " hit_crit", id + " hit_crit")
      renpy.copy_images(pic_name + " dead",     id + " dead")
      renpy.copy_images(pic_name + " melee",    id + " melee")
          
      x = MOB_POSITIONS[i][0]
      y = MOB_POSITIONS[i][1]
      mobs.append(Mob(real_name, id, health, mana, damage_melee, damage_magic, x, y, zorder))
          
      zorder += 1
  
  
  def show_target_list(mobs):
    ui.frame(xpos=65, ypos=100, xmaximum=230, background=None)
    ui.vbox()
    ui.text("Select target:", xfill=True)
    for mob in mobs:
      if mob.get_health() > 0:
        ui.textbutton(mob.get_name() + ", " + str(mob.get_health()) + " HP", clicked=ui.returns(mob), xfill=True) 
    ui.close()
     
    return
  
  
  def show_action_list(player, target):
    ui.frame(xpos=65, ypos=100, xmaximum=230, background=None)
    ui.text(target.get_name() + ", " + str(target.get_health()) + " HP")
    ui.frame(xpos=65, ypos=140, background=None)
    ui.imagebutton("gfx/buttons/battle_melee.png", "gfx/buttons/battle_melee_hover.png", clicked=ui.returns("melee"))
    ui.frame(xpos=195, ypos=136, background=None)
    if player.can_afford_magic():
      ui.imagebutton("gfx/buttons/battle_magic.png", "gfx/buttons/battle_magic_hover.png", clicked=ui.returns("magic"))
    else:
      ui.image("gfx/buttons/battle_magic_disabled.png")
    ui.frame(xpos=65, ypos=250, xmaximum=230)
    ui.textbutton("Cancel", clicked=ui.returns("cancel"), xfill=True) 
      
    return
      
      
  def show_battle_messages(messages):
    messages.append("")
    messages.append("Click to continue...")
      
    ui.frame(xpos=65, ypos=100, xmaximum=230, background=None)
    ui.vbox()
    for message in messages:
      ui.text(message)
    ui.close()
      
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    ui.interact()
      
    del messages[:]
      
    return
      
  def battle(player_name, mob_name, mob_count, background):
    messages = []
      
    # Create the combatants
    player = Player(player_name, HP, MP)
      
    mobs = create_mobs(mob_name, mob_count)
    mobs_alive = len(mobs)
    
    # Update the screen elements
    hide_main_ui()
    show_minigame_ui(background)
    
    renpy.show(player.get_id() + " idle", at_list = [Position(xpos=player.get_x(), ypos=player.get_y()), Transform(zoom=ZOOM)], zorder=player.get_zorder())
    
    for i in range(0,len(mobs)):
      renpy.show(mobs[i].get_id() + " idle", at_list = [Position(xpos=mobs[i].get_x(), ypos=mobs[i].get_y()), Transform(zoom=ZOOM)], zorder=mobs[i].get_zorder())
  
    # And start the actual battle loop
    while player.get_health() > 0 and mobs_alive > 0:
      show_target_list(mobs)
      target = ui.interact()
      show_action_list(player, target)
      action = ui.interact()
      
      if action != "cancel":
        player.attack(target, action, messages)
        
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

    messages.append("(Post-battle message)")
    show_battle_messages(messages)
    
    battle_result = player.get_health() > 0
    
    # When done, hide all the images and clear other resources
    renpy.hide(player.get_id())
    for mob in mobs:
      renpy.hide(mob.get_id())
    
    del mobs[:]
    player = None
  
    update_stats(MINIGAME_UI)
  
    renpy.transition(dissolve)
    hide_minigame_ui(background)
    show_main_ui()
    
  
    return battle_result
  
label test_battle:
  #$hp = 100
  #$mp = 30
  #call battle("Riku", "Demon hunter", 2, "bg riroom")
  $print battle("Riku", "Naomi", 1, "bg riroom")
  
  return
