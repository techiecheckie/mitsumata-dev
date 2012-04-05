init python:
  # Mob stats, feel free to modify
  MOB_CRIT_CHANCE     = 20 # 5% chance, a random number between 1-MOB_CRIT_CHANCE
  MOB_CRIT_MULTIPLIER = 2
  
  # Default magic cost for all combatants
  MAGIC_COST = 50
  
  # Default damage values for Riku and Roman
  PLAYER_MELEE = 30
  PLAYER_MAGIC = 50
  
  # Name to use: "Mamoru"
  MAMORU_HEALTH = 300
  MAMORU_MANA   = 50
  MAMORU_MELEE  = 20
  MAMORU_MAGIC  = 25
  
  # Name to use: "Naomi"
  NAOMI_HEALTH  = 100
  NAOMI_MANA    = 100
  NAOMI_MELEE   = 5
  NAOMI_MAGIC   = 10
  
  # Name to use: "Demon thug"
  DEMON_THUG_HEALTH = 50
  DEMON_THUG_MANA   = 0
  DEMON_THUG_MELEE  = 20
  DEMON_THUG_MAGIC  = 0
    
  # Name to use: "Demon hunter"
  DEMON_HUNTER_HEALTH = 50
  DEMON_HUNTER_MANA   = 0
  DEMON_HUNTER_MELEE  = 30
  DEMON_HUNTER_MAGIC  = 0
  
  # Name to use: "Carniflora"
  CARNIFLORA_HEALTH = 500
  CARNIFLORA_MANA   = 100
  CARNIFLORA_MELEE  = 10
  CARNIFLORA_MAGIC  = 10
  
  MESSAGE_VICTORY = "You won the fight!"
  MESSAGE_DEFEAT  = "You lost the fight."
  MESSAGE_FLEE    = "You flee from the fight!"
  MESSAGE_TO_BITTER_END = "Don't be so weak-willed, you can't run from this battle!"
  
  # Don't touch any of the values listed below this point!
  
  # Sprite zoom value
  ZOOM = 2.0
  # Default (visual) distance between the attacker and the target in pixels
  ATTACK_DISTANCE = 240
  
  # Extra (visual, stacking) distances between the attacker and the target
  # Stops the attacker from running into the plant
  CARNIFLORA_TARGET_OFFSET = 80
  # Stops Carniflora from running into the target
  CARNIFLORA_MELEE_OFFSET  = 200
  # Magic animation offsets (if larger (wider) sprites than the melee ones)
  CARNIFLORA_MAGIC_OFFSET = 0
  MAMORU_MAGIC_OFFSET     = 0
  NAOMI_MAGIC_OFFSET      = 50
  ROMAN_MAGIC_OFFSET      = 10
  
  # Mob positions on the screen from the top left corner of the screen
  MOB_POSITIONS = [(420,520), (400,550), (450,580)]
  # Player sprite position
  PLAYER_X = 960
  PLAYER_Y = MOB_POSITIONS[1][1]
  
  # Something to hold the messages during the fight
  BATTLE_MESSAGES = []
  
  # Battle states
  BATTLE_STATE_TARGET      = "battle_state_target"
  BATTLE_STATE_ATTACK_TYPE = "battle_state_attack_type"
  BATTLE_STATE_END         = "battle_state_end"
  
  
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
      # TODO: use proper spell cost values
      return self.mana >= MAGIC_COST

    def show_attack(self, target, action, damage, critical, attack_distance):
      BATTLE_MESSAGES.append(self.get_name() + " attacks " + target.get_name() + "\n")
      
      # Carniflora's custom grab-pull-pound-release attack
      if self.id == "Carniflora" and action == "magic":
        renpy.show(self.id + " magic")
        renpy.pause(0.7)
        renpy.show(target.get_id() + " hit", 
                   at_list = [slide(0.2, self.x + 220, self.y - 60)])
        renpy.pause(1.3)
        renpy.show(target.get_id() + " idle", 
                   at_list = [carniflora_drop(PLAYER_X, PLAYER_Y)], 
                   zorder=self.zorder) 
      else:
        # use default animation stuff
        pre_attack_duration    = ANIMATION_DURATION[self.name + " " + action + " delay"]
        attack_duration        = ANIMATION_DURATION[self.name + " " + action]
        post_attack_duration   = attack_duration - pre_attack_duration
        hit_duration           = ANIMATION_DURATION[target.get_name() + " hit"]
        attacker_idle_duration = hit_duration - post_attack_duration

        # slide in
        if self.id == "Mamoru" and action == "melee":
          renpy.show(self.id + " slide", 
                     at_list = [mamoru_slide(target.get_x()-attack_distance, target.get_y())], 
                     zorder=self.zorder)
          renpy.pause(ANIMATION_DURATION["Mamoru slide"])
        else:
          renpy.show(self.id + " idle", 
                     at_list = [slide(ANIMATION_DURATION["slide"],
                                      target.get_x()-attack_distance, 
                                      target.get_y())], 
                     zorder=self.zorder)
          renpy.pause(ANIMATION_DURATION["slide"])
        
        # (1) start attack animation
        renpy.show(self.id + " " + action, zorder=target.get_zorder())
        # wait a bit for the blow to fall
        renpy.pause(pre_attack_duration)
        # (2) start the target hit animation
        renpy.show(target.get_id() + " hit", zorder=target.get_zorder())
        # wait for the attack animation to finish
        renpy.pause(post_attack_duration)
        # (3) start attacker idle animation
        renpy.show(self.id + " idle", zorder=self.get_zorder())
        # wait for the hit animation to end
        renpy.pause(attacker_idle_duration)
        # (4) start the target idle animation
        renpy.show(target.get_id() + " idle", zorder=target.get_zorder())
      
      target.dec_health(damage)
      
      BATTLE_MESSAGES.append(target.get_name() + " is hit for " + str(damage) + " points\n")
      if critical:
        BATTLE_MESSAGES.append("Critical hit!\n")
      
      if target.get_health() <= 0:
        BATTLE_MESSAGES.append(target.get_name() + " is knocked out cold!\n")
        renpy.transition(Dissolve(0.5))
        renpy.hide(target.get_id() + " idle")
        renpy.pause(0.5)
      
      # slide out
      renpy.show(self.id + " idle", 
                 at_list = [slide(ANIMATION_DURATION["slide"], self.x, self.y)], 
                 zorder=self.zorder)
      renpy.pause(ANIMATION_DURATION["slide"])      
       
       
  class Player(Fighter):
    def __init__(self, id, health, mana):
      # TODO: set proper melee and magic damage values
      super(Player, self).__init__(id, id, health, mana, PLAYER_MELEE, PLAYER_MAGIC, PLAYER_X, PLAYER_Y, 1)
        
    def attack(self, target, action):
      attack_offset = 0
      if action == "melee":
        damage = self.damage_melee
        if target.name == "Carniflora":
          attack_offset = CARNIFLORA_TARGET_OFFSET
      elif action == "magic":
        damage = self.damage_magic
        if target.name == "Carniflora":
          attack_offset = CARNIFLORA_TARGET_OFFSET
        elif self.name == "Roman":
          attack_offset = ROMAN_MAGIC_OFFSET
        
        # TODO: add any (magic cost reducing) bonuses that items give
        self.mana -= MAGIC_COST 
        
      # Player's crit chance may vary, using hard-coded values for now, TODO
      if random.randint(1,20) == 20:
        critical = True
        damage *= 2
      else:
        critical = False
          
      Fighter.show_attack(self, target, action, damage, critical, -ATTACK_DISTANCE - attack_offset)
       
       
  class Mob(Fighter):
    def __init__(self, name, id, health, mana, damage_melee, damage_magic, x, y, zorder):
      super(Mob, self).__init__(name, id, health, mana, damage_melee, damage_magic, x, y, zorder)
        
    def attack(self, target):
      attack_offset = 0
      if self.mana > 0:
        # TODO: use proper mana cost values
        self.mana -= MAGIC_COST
        
        # See if the attack should be melee or a magical one
        # "randomize two numbers, then multiply them with each other. If  the 
        # number comes out to be odd, it' a magic attack. Even, it's a regular 
        # attack"
        value1 = random.randint(1,10)
        value2 = random.randint(1,10)
        value3 = value1 * value2

        # decide attack type
        if value3 % 2 == 0:
          action = "magic"
          damage = self.damage_magic
          if self.name == "Naomi":
            attack_offset = NAOMI_MAGIC_OFFSET
          elif self.name == "Carniflora":
            attack_offset = CARNIFLORA_MAGIC_OFFSET
        else:
          action = "melee"
          damage = self.damage_melee
          if self.name == "Carniflora":
            attack_offset = CARNIFLORA_MELEE_OFFSET
      else:
        action = "melee"
        damage = self.damage_melee
        if self.name == "Carniflora":
          attack_offset = CARNIFLORA_MELEE_OFFSET
          
      if random.randint(1,MOB_CRIT_CHANCE) == MOB_CRIT_CHANCE:
        critical = True
        damage *= MOB_CRIT_MULTIPLIER
      else:
        critical = False
          
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
    elif mob_name == "Carniflora":
      health       = CARNIFLORA_HEALTH
      mana         = CARNIFLORA_MANA
      damage_melee = CARNIFLORA_MELEE
      damage_magic = CARNIFLORA_MAGIC
      x            = MOB_POSITIONS[1][0]
      y            = MOB_POSITIONS[1][1]
      zorder       = 0
      mobs.append(Mob(mob_name, "Carniflora", health, mana, damage_melee, damage_magic, x, y, zorder))
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
    ui.text("{size=-3}Select target:\n{/size}", xfill=True)
    for mob in mobs:
      if mob.get_health() > 0:
        ui.textbutton("{size=-3}" + mob.get_name() + ", " + str(mob.get_health()) + " HP{/size}", clicked=ui.returns(mob), xfill=True) 
    ui.close()
     
    return
  
  
  def show_action_list(player, target):
    ui.frame(xpos=65, ypos=100, xmaximum=230, background=None)
    ui.text("{size=-3}" + target.get_name() + ", " + str(target.get_health()) + " HP\n{/size}")
    ui.frame(xpos=65, ypos=140, background=None)
    ui.imagebutton("gfx/buttons/battle_melee.png", "gfx/buttons/battle_melee_hover.png", clicked=ui.returns("melee"))
    ui.frame(xpos=195, ypos=136, background=None)
    if player.can_afford_magic():
      ui.imagebutton("gfx/buttons/battle_magic.png", "gfx/buttons/battle_magic_hover.png", clicked=ui.returns("magic"))
    else:
      ui.image("gfx/buttons/battle_magic_disabled.png")
    ui.frame(xpos=65, ypos=250, xmaximum=230)
    ui.textbutton("{size=-3}Cancel{/size}", clicked=ui.returns("cancel"), xfill=True) 
      
    return
      
      
  def show_battle_messages():
    BATTLE_MESSAGES.append("Click to continue...")

    # full screen click-to-continue    
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    ui.interact()
    
    del BATTLE_MESSAGES[:]
      
    return
    
    
  def battle_message_area():
    ui.frame(xpos=65, ypos=100, xmaximum=240, background=None)
    ui.vbox()
    for message in BATTLE_MESSAGES:
      ui.text("{size=-3}" + message + "{/size}")
    ui.close()
    
    return
    
    
  def battle(player_name, mob_name, mob_count, background, to_bitter_end):
    config.overlay_functions.append(battle_message_area)
    config.rollback_enabled = False
    
    # Create the combatants
    player = Player(player_name, HP + BONUS_HP, MP + BONUS_MP)
    
    mobs = create_mobs(mob_name, mob_count)
    mobs_alive = len(mobs)
    
    # Update the screen elements
    renpy.transition(dissolve)
    hide_main_ui()
    renpy.show(background, at_list = [Position(xpos=MINIGAME_POS_X, ypos=MINIGAME_POS_Y-20), Transform(anchor=(0.0, 0.0))]) 
    show_minigame_ui(None, True)
    config.overlay_functions.remove(minigame_ui_buttons)
    
    # Place player and mob sprites on the screen
    renpy.show(player.get_id() + " idle", 
               at_list = [Position(xpos=player.get_x(), ypos=player.get_y()), Transform(zoom=ZOOM, anchor=(1.0,1.0))], 
               zorder=player.get_zorder())
    
    for i in range(0,len(mobs)):
      renpy.show(mobs[i].get_id() + " idle", 
                 at_list = [Position(xpos=mobs[i].get_x(), ypos=mobs[i].get_y()), Transform(zoom=ZOOM, anchor=(0,1.0))], 
                 zorder=mobs[i].get_zorder())
    
    # Initialize some variables for the battle
    state = BATTLE_STATE_TARGET
    target = None
    action = None
    post_battle_message = None
    
    while state != BATTLE_STATE_END:
      if state == BATTLE_STATE_TARGET:
        show_target_list(mobs)
      elif state == BATTLE_STATE_ATTACK_TYPE:
        show_action_list(player, target)
      
      button = ui.interact()
      
      if button == "exit":
        if to_bitter_end:
          show_message(MESSAGE_TO_BITTER_END, "medium")
        else:
          post_battle_message = MESSAGE_FLEE
          state = BATTLE_STATE_END
      else:
        if state == BATTLE_STATE_TARGET:
          target = button
          state = BATTLE_STATE_ATTACK_TYPE
        else:
          action = button
          state = BATTLE_STATE_TARGET
          
          # Attack stuff begins
          if button != "cancel":
            # Display player attack animation
            player.attack(target, action)
            # Update HP and MP bars
            update_minigame_ui(player.get_health(), player.get_mana())
            # Update battle messages list
            show_battle_messages()
        
            # Loop through the mobs, displaying their attack animations
            mobs_alive = 0
            for i in range(0, len(mobs)):
              mob = mobs[len(mobs)-1-i]
              # Do stuff only if the mob is alive (= not hidden)
              if mob.get_health() > 0:
                mobs_alive += 1
                mob.attack(player)
                if player.get_health() <= 0:
                  post_battle_message = MESSAGE_DEFEAT
                  state = BATTLE_STATE_END
                  break
        
            if mobs_alive > 0:
              update_minigame_ui(player.get_health(), player.get_mana())
              show_battle_messages()
            else:
              post_battle_message = MESSAGE_VICTORY
              state = BATTLE_STATE_END

    # Display post battle messages
    BATTLE_MESSAGES.append(post_battle_message + "\n")
    show_battle_messages()
    
    battle_result = player.get_health() > 0
    
    # When done, hide all the images and clear other resources
    renpy.hide(player.get_id())
    for mob in mobs:
      renpy.hide(mob.get_id())
    
    del mobs[:]
    player = None
  
    update_stats()
  
    renpy.transition(dissolve)
    config.overlay_functions.remove(battle_message_area)
    config.rollback_enabled = True
    hide_minigame_ui(background)
    show_main_ui()
    
    return battle_result
