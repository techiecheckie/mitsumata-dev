init python:
  # Mob stats, feel free to modify
  MOB_CRIT_CHANCE     = 20 # 5% chance, a random number between 1-MOB_CRIT_CHANCE
  MOB_CRIT_MULTIPLIER = 2
  
  # Default magic cost for all combatants
  MAGIC_COST = 50
  
  # Default damage values for Riku and Roman
  PLAYER_MELEE = 30
  PLAYER_MAGIC = 50
  PLAYER_CRIT_MULTIPLIER = 2
  
  MOB_VARIABLES = {}
  MOB_VARIABLES["Mamoru"]       = { "health":300, "mana":100, "melee":10, "magic":30, "zorder":4, "picture":"Mamoru" }
  MOB_VARIABLES["Naomi"]        = { "health":100, "mana":100, "melee":5,  "magic":10, "zorder":4, "picture":"Naomi" }
  MOB_VARIABLES["Demon thug"]   = { "health":50,  "mana":0,   "melee":20, "magic":0,  "zorder":4, "picture":"DemonThug" }
  MOB_VARIABLES["Demon hunter"] = { "health":50,  "mana":0,   "melee":30, "magic":0,  "zorder":4, "picture":"DemonHunter" }
  MOB_VARIABLES["Carniflora"]   = { "health":500, "mana":100, "melee":10, "magic":10, "zorder":0, "picture":"Carniflora" }
  
  MESSAGE_VICTORY = "You won the fight!"
  MESSAGE_DEFEAT  = "You lost the fight."
  MESSAGE_FLEE    = "You flee!"
  MESSAGE_TO_BITTER_END = "Don't be so weak-willed, you can't run from this battle!"
  
  # Don't touch any of the values listed below this point!
  
  # Sprite zoom value
  ZOOM = 2.0
  # Default (visual) distance between the attacker and the target in pixels
  ATTACK_DISTANCE = 240
  
  # Extra (visual, stacking) distances between the attacker and the target
  ATTACK_OFFSETS = {}
  # Stops the attacker from running into the plant
  ATTACK_OFFSETS["Carniflora target"] = 80
  # Stops Carniflora from running into the target
  ATTACK_OFFSETS["Carniflora melee"] = 200
  # Magic animation offsets (if larger (wider) sprites than the melee ones)
  ATTACK_OFFSETS["Naomi magic"] = 50
  ATTACK_OFFSETS["Roman magic"] = 10
  
  # Mob positions on the screen from the top left corner of the screen
  MOB_POSITIONS = [(420,520), (400,550), (450,580)]
  
  # Player sprite position
  PLAYER_X = 960
  PLAYER_Y = MOB_POSITIONS[1][1]
  PLAYER_ZORDER = 1
  
  # Something to hold the messages during the fight
  BATTLE_MESSAGES = []
  BATTLE_MESSAGE_LIMIT = 18
  
  # Battle states
  BATTLE_STATE_TARGET      = "battle_state_target"
  BATTLE_STATE_ATTACK_TYPE = "battle_state_attack_type"
  BATTLE_STATE_END         = "battle_state_end"
  
  # Base fighter class. 
  class Fighter(object):
    def __init__(self, name, health, mana, damage_melee, damage_magic, pic_name, zorder, x, y):
      self.name = name
      self.health = health
      self.mana = mana
      self.damage_melee = damage_melee
      self.damage_magic = damage_magic
      self.pic_name = pic_name
      self.zorder = zorder
      self.x = x
      self.y = y
        
    def get_name(self):
      return self.name
        
    def get_id(self):
      return self.pic_name
        
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
      return self.mana >= MAGIC_COST
      
    # A big n' messy animation method. Animations have three (3) phases: charge,
    # hit, and retreat. Each phase is timed differently using the values set in
    # battle_animations.rpy, and these values tell things like how long should
    # the target wait for the blow to fall and how long should s/he flinch
    # afterwards, etc. The custom animations added for Mamoru and Carniflora are
    # the only special ones, while the rest of the fighters use the same basic
    # stuff for different actions.
    def show_attack(self, target, action, damage, critical, attack_distance):
      push_message(self.get_name() + " attacks " + target.get_name())
      
      # Carniflora's custom grab-pull-pound-release attack.
      if self.pic_name.startswith("Carniflora") and action == "magic":
        renpy.show(self.pic_name + " " + action)
        renpy.pause(ANIMATION_DURATION[self.name + " " + action + " delay"])
        renpy.show(target.get_id() + " hit", 
                   at_list = [slide(0.2, self.x + 220, self.y - 60)])
        renpy.pause(ANIMATION_DURATION[self.name + " " + action])
        renpy.show(target.get_id() + " idle", 
                   at_list = [carniflora_drop(PLAYER_X, PLAYER_Y)], 
                   zorder=self.zorder) 
      else:
        # Use default animation timing for the attack.
        pre_attack_duration    = ANIMATION_DURATION[self.name + " " + action + " delay"]
        attack_duration        = ANIMATION_DURATION[self.name + " " + action]
        post_attack_duration   = attack_duration - pre_attack_duration
        hit_duration           = ANIMATION_DURATION[target.get_name() + " hit"]
        attacker_idle_duration = hit_duration - post_attack_duration

        # Mamoru has his own custom slide, so display that if needed.
        if self.pic_name.startswith("Mamoru") and action == "melee":
          renpy.show(self.pic_name + " slide", 
                     at_list = [mamoru_slide(target.get_x()-attack_distance, target.get_y())], 
                     zorder=self.zorder)
          renpy.pause(ANIMATION_DURATION[self.name + " slide"])
        else:
          renpy.show(self.pic_name + " idle", 
                     at_list = [slide(ANIMATION_DURATION["slide"],
                                      target.get_x()-attack_distance, 
                                      target.get_y())], 
                     zorder=self.zorder)
          renpy.pause(ANIMATION_DURATION["slide"])
        
        # (1) start attack animation
        renpy.show(self.pic_name + " " + action, zorder=target.get_zorder())
        # wait a bit for the blow to fall
        renpy.pause(pre_attack_duration)
        # (2) start the target hit animation
        renpy.show(target.get_id() + " hit", zorder=target.get_zorder())
        # wait for the attack animation to finish
        renpy.pause(post_attack_duration)
        # (3) start attacker idle animation
        renpy.show(self.pic_name + " idle", zorder=self.get_zorder())
        # wait for the hit animation to end
        renpy.pause(attacker_idle_duration)
        # (4) start the target idle animation
        renpy.show(target.get_id() + " idle", zorder=target.get_zorder())
      
      target.dec_health(damage)

      push_message("  " + target.get_name() + " is hit for " + str(damage) + " points.")
      if critical:
        push_message("  Critical hit!")
        
      if target.get_health() <= 0:
        push_message("  " + target.get_name() + " is knocked out cold!")
        renpy.transition(Dissolve(0.5))
        renpy.hide(target.get_id() + " idle")
        renpy.pause(0.5)
      else:
        push_message("  " + target.get_name() + " has " + str(target.get_health()) + " HP left.")
      push_message("Click to continue...\n")
      
      # slide out
      renpy.show(self.pic_name + " idle", 
                 at_list = [slide(ANIMATION_DURATION["slide"], self.x, self.y)], 
                 zorder=self.zorder)
      renpy.pause(ANIMATION_DURATION["slide"])
       
  # Player class
  class Player(Fighter):
    def __init__(self, name, health, mana):
      super(Player, self).__init__(name, health, mana, PLAYER_MELEE, PLAYER_MAGIC, name, PLAYER_ZORDER, PLAYER_X, PLAYER_Y)
        
    def attack(self, target, action):
      if action == "melee":
        damage = self.damage_melee
      elif action == "magic":
        damage = self.damage_magic
        self.dec_mana(MAGIC_COST)
      
      # See if the player's lucky enough to do a critical hit.
      if random.randint(1,20) == 20:
        critical = True
        damage *= 2
      else:
        critical = False
        
      # Pick an offset from ATTACK_OFFSETS dict, if any. Carniflora has a huge 
      # sprite, so a custom offset must be used for that one.
      if target.name == "Carniflora":
        offset_key = "Carniflora target"
      else:
        offset_key = self.get_name() + " " + action
      
      attack_offset = get_offset(offset_key)
      
      # Finally, start the animation.
      Fighter.show_attack(self, target, action, damage, critical, -ATTACK_DISTANCE - attack_offset)       

  # Mob class
  class Mob(Fighter):
    def __init__(self, name, health, mana, damage_melee, damage_magic, pic_name, zorder, x, y):
      super(Mob, self).__init__(name, health, mana, damage_melee, damage_magic, pic_name, zorder, x, y)
        
    def attack(self, target):
      if self.can_afford_magic():
        self.dec_mana(MAGIC_COST)
        
        # See if the attack should be melee or a magical one:
        # "randomize two numbers, then multiply them with each other. If the 
        # number comes out to be odd, it's a magic attack. Even, it's a regular 
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
      
      # See if it's a critical hit.          
      if random.randint(1,MOB_CRIT_CHANCE) == MOB_CRIT_CHANCE:
        critical = True
        damage *= MOB_CRIT_MULTIPLIER
      else:
        critical = False
      
      # Pick an offset from ATTACK_OFFSETS dict, if any.  
      attack_offset = get_offset(self.get_name() + " " + action)
      
      # Finally, start the animation.
      Fighter.show_attack(self, target, action, damage, critical, ATTACK_DISTANCE + attack_offset)
  
  # Returns offset values defined in dict ATTACK_OFFSETS. Offsets are used to
  # prevent attackers from sliding too far and overlapping their targets when
  # attacking.
  def get_offset(offset_key):
    if offset_key in ATTACK_OFFSETS:
      return ATTACK_OFFSETS[offset_key]
    return 0
  
  # Creates a list of mobs and returns that list after populating it.
  def create_mobs(mob_name, mob_count):
    mob_stats = MOB_VARIABLES[mob_name]
    health       = mob_stats["health"]
    mana         = mob_stats["mana"]
    damage_melee = mob_stats["melee"]
    damage_magic = mob_stats["magic"]
    zorder       = mob_stats["zorder"]
    pic_name     = mob_stats["picture"]
    
    mobs = []
    
    if mob_count > 1:
      create_several_mobs(mob_name, health, mana, damage_melee, damage_magic, pic_name, zorder, mob_count, mobs)
    else:
      x = MOB_POSITIONS[1][0]
      y = MOB_POSITIONS[1][1]
      mobs.append(Mob(mob_name, health, mana, damage_melee, damage_magic, pic_name, zorder, x, y))
      
    return mobs
      
  # Creates mob_count amount of duplicates from the given mob, copying its
  # original pictures (pic_name + action, e.g. "Mamoru melee") as new Renpy 
  # displayables for each copy of the mob to allow separate animations for each
  # one.
  def create_several_mobs(real_name, health, mana, damage_melee, damage_magic, pic_name, zorder, mob_count, mobs):
    for i in range(0, mob_count):
      new_pic_name = pic_name + "_" + str(i)
         
      renpy.copy_images(pic_name + " idle",  new_pic_name + " idle")
      renpy.copy_images(pic_name + " hit",   new_pic_name + " hit")
      renpy.copy_images(pic_name + " melee", new_pic_name + " melee")
      
      if not real_name.startswith("Demon"):
        renpy.copy_images(pic_name + " slide", new_pic_name + " slide")
        renpy.copy_images(pic_name + " magic", new_pic_name + " magic")
          
      x = MOB_POSITIONS[i][0]
      y = MOB_POSITIONS[i][1]
      
      mobs.append(Mob(real_name, health, mana, damage_melee, damage_magic, new_pic_name, zorder, x, y))
          
      zorder += 1
  
  # Creates a list of clickable targets on the parchment area, displaying their 
  # name and their current health. 
  def show_target_list(mobs):
    ui.frame(xpos=65, ypos=100, xmaximum=230, background=None)
    ui.vbox()
    ui.text("{size=-3}Select target:\n{/size}", xfill=True)
    for mob in mobs:
      if mob.get_health() > 0:
        ui.textbutton("{size=-3}" + mob.get_name() + ", " + str(mob.get_health()) + " HP{/size}", clicked=ui.returns(mob), xfill=True) 
    ui.close()
     
    return
  
  # Displays available combat actions on the parchment area. Melee option is
  # always available, magic option also if the player has enough mana for it.
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
  
  # Adds a "message box" to the parchment area. This method is added to Renpy's
  # UI stack in the beginning of the battle() method, so that different messages
  # added to BATTLE_MESSAGES list are displayed automatically after every UI 
  # interaction.
  def battle_message_area():
    ui.frame(xpos=55, ypos=100, xmaximum=260, background=None)
    ui.vbox()
    for message in BATTLE_MESSAGES:
      ui.text("{size=-3}" + message + "{/size}")
    ui.close()
    
    return
  
  # Pushes a message to the battle messages list. The first one is removed if the
  # size of the list exceeds BATTLE_MESSAGE_LIMIT.
  def push_message(message):
    BATTLE_MESSAGES.append(message)
    if len(BATTLE_MESSAGES) >= BATTLE_MESSAGE_LIMIT:
      item = BATTLE_MESSAGES.pop(0)

  # Displays an invisible button the size of the minigame area. Acts as a "click
  # to continue" button to create small pauses between the attacks.
  def click_to_continue():
    ui.frame(xpos=MINIGAME_POS_X,
             ypos=MINIGAME_POS_Y,
             background=None,
             xmaximum=MINIGAME_WIDTH,
             ymaximum=MINIGAME_HEIGHT)
    ui.textbutton("", clicked=ui.returns(0), xfill=True, yfill=True, background=None)
    ui.interact()
    
  # Battle "constructor". Creates the combatants and initializes UI elements
  # before starting the actual battle loop. Boolean to_bitter_end controls
  # whether the player should be able to quit the battle before it ends by using
  # the minigame ui's exit button.
  def battle(player_name, mob_name, mob_count, background, to_bitter_end):
    config.rollback_enabled = False
    
    # Save the currently playing song to a variable and start the battle music.
    currently_playing = renpy.music.get_playing()
    renpy.music.play(BATTLE_MUSIC, fadein=1)
    
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
            config.overlay_functions.append(battle_message_area)
            
            # Display player attack animation
            player.attack(target, action)
            # Update HP and MP bars
            update_minigame_ui(player.get_health(), player.get_mana())

            click_to_continue()
        
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
        
            # Prepare for a new round if any mobs are alive, else quit.
            if mobs_alive > 0:
              update_minigame_ui(player.get_health(), player.get_mana())
              click_to_continue()
              config.overlay_functions.remove(battle_message_area)
            else:
              post_battle_message = MESSAGE_VICTORY
              state = BATTLE_STATE_END

    # Display post battle messages
    push_message(post_battle_message)
    click_to_continue()
    
    # When done, hide all the images and clear other resources
    renpy.hide(player.get_id())
    for mob in mobs:
      renpy.hide(mob.get_id())
    del mobs[:]
    # Though grab the score before clearing the player
    result = player.get_health() > 0
    player = None
    
    update_stats()
    
    # Start the previously played song.
    renpy.music.play(currently_playing, fadein=1)
  
    renpy.transition(dissolve)
    config.overlay_functions.remove(battle_message_area)
    config.rollback_enabled = True
    hide_minigame_ui(background)
    show_main_ui()
    
    return result
