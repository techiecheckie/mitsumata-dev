label prepare_battle_animations:
  $animation_delays = {}
  
  transform slide(delay, x, y):
    linear delay xpos x ypos y

  ########
  # Riku #
  ########
  
  image Riku idle:
    "gfx/animated/riku/riku_idlel01.png"
    pause 0.2
    "gfx/animated/riku/riku_idlel02.png"
    pause 0.2
    "gfx/animated/riku/riku_idlel03.png"
    pause 0.2
    repeat
  
  image Riku hit:
    "gfx/animated/riku/riku_hitl01.png"
    pause 0.4
    "gfx/animated/riku/riku_hitl02.png"
    pause 0.4
    
  image Riku hit_crit:
    "gfx/animated/riku/riku_hitwussyl01.png"
    pause 0.4
    "gfx/animated/riku/riku_hitwussyl02.png"
    pause 0.4
    
  image Riku dead:
    "gfx/animated/riku/riku_hitwussyl01.png"
    pause 0.4
    "gfx/animated/riku/riku_hitwussyl02.png"
    pause 0.4
    
  #$animation_delays["Riku melee"] = 0.8
  image Riku melee:  
    "gfx/animated/riku/riku_attackl01.png"
    pause 0.2
    "gfx/animated/riku/riku_attackl02.png"
    pause 0.2
    "gfx/animated/riku/riku_attackl03.png"
    pause 0.2
    "gfx/animated/riku/riku_attackl04.png"
    pause 0.2
    
  #$animation_delays["Riku magic"] = 0.8
  image Riku magic:
    "gfx/animated/missing.png"
    
  #########
  # Roman #
  #########
    
  image Roman idle:
    "gfx/animated/roman/roman_idlel01.png"
    pause 0.2
    "gfx/animated/roman/roman_idlel02.png"
    pause 0.2
    "gfx/animated/roman/roman_idlel03.png"
    pause 0.2
    repeat
  
  image Roman hit:
    "gfx/animated/riku/riku_hitl01.png"
    pause 0.4
    "gfx/animated/riku/riku_hitl02.png"
    pause 0.4
    
  image Roman hit_crit:
    "gfx/animated/roman/roman_hitwussyl01.png"
    pause 0.4
    "gfx/animated/roman/roman_hitwussyl02.png"
    pause 0.4
    
  image Roman dead:
    "gfx/animated/roman/roman_hitwussyl01.png"
    pause 0.4
    "gfx/animated/roman/roman_hitwussyl02.png"
    pause 0.4
    
  image Roman melee:
    "gfx/animated/roman/roman_kickl01.png"
    pause 0.2
    "gfx/animated/roman/roman_kickl02.png"
    pause 0.2
    "gfx/animated/roman/roman_kickl03.png"
    pause 0.2
    "gfx/animated/roman/roman_kickl04.png"
    pause 0.2
    "gfx/animated/roman/roman_kickl05.png"
    pause 0.2
    "gfx/animated/roman/roman_kickl06.png"
    pause 0.2
    "gfx/animated/roman/roman_kickl07.png"
    pause 0.2
    "gfx/animated/roman/roman_kickl08.png"
    pause 0.2
    
  image Roman magic:
    "gfx/animated/roman/roman_iceswordl01.png"
    pause 0.2
    "gfx/animated/roman/roman_iceswordl02.png"
    pause 0.2
    "gfx/animated/roman/roman_iceswordl03.png"
    pause 0.2
    "gfx/animated/roman/roman_iceswordl04.png"
    pause 0.2
    "gfx/animated/roman/roman_iceswordl05.png"
    pause 0.2
    "gfx/animated/roman/roman_iceswordl06.png"
    pause 0.2
    "gfx/animated/roman/roman_iceswordl07.png"
    pause 0.2
    "gfx/animated/roman/roman_iceswordl08.png"
    pause 0.2
    "gfx/animated/roman/roman_iceswordl09.png"
    pause 0.2
    "gfx/animated/roman/roman_iceswordl10.png"
    pause 0.2
    "gfx/animated/roman/roman_iceswordl11.png"
    pause 0.2
    
  ################
  # Demon hunter #
  ################
  
  image DemonHunter idle:
    "gfx/animated/riku/riku_idler02.png"
    pause 0.2
    "gfx/animated/riku/riku_idler03.png"
    pause 0.2
    "gfx/animated/riku/riku_idler01.png"
    pause 0.2
    repeat
    
  image DemonHunter hit:
    "gfx/animated/riku/riku_hitr01.png"
    pause 0.4
    "gfx/animated/riku/riku_hitr02.png"
    pause 0.4
    
  image DemonHunter hit_crit:
    "gfx/animated/riku/riku_hitwussyr01.png"
    pause 0.4
    "gfx/animated/riku/riku_hitwussyr02.png"
    pause 0.4
    
  image DemonHunter dead:
    "gfx/animated/riku/riku_hitwussyr01.png"
    pause 0.4
    "gfx/animated/riku/riku_hitwussyr02.png"
    pause 0.4
  
  #$animation_delays["Demon hunter melee"] = 0.8
  image DemonHunter melee:
    "gfx/animated/riku/riku_swiper01.png"
    pause 0.2
    "gfx/animated/riku/riku_swiper02.png"
    pause 0.2
    "gfx/animated/riku/riku_swiper03.png"
    pause 0.2
    "gfx/animated/riku/riku_swiper04.png"
    pause 0.2
    
  ##############
  # Unassigned #
  ##############
  
  image Riku fireblack:
    "gfx/animated/riku/riku_fireblackr01.png"
    pause 0.2
    "gfx/animated/riku/riku_fireblackr02.png"
    pause 0.2
    "gfx/animated/riku/riku_fireblackr03.png"
    pause 0.2
    "gfx/animated/riku/riku_fireblackr04.png"
    pause 0.2
    
  ##########
  # Mamoru #
  ##########
  
  image Mamoru idle:
    "gfx/animated/mamoru/mamoru_idle2l01.png"
    pause 0.2
    "gfx/animated/mamoru/mamoru_idle2l02.png"
    pause 0.2
    "gfx/animated/mamoru/mamoru_idle2l03.png"
    repeat
    
  image Mamoru hit:
    "gfx/animated/mamoru/mamoru_hitl01.png"
    pause 0.4
    "gfx/animated/mamoru/mamoru_hitl02.png"
    pause 0.4
    
  image Mamoru hit_crit:
    "gfx/animated/riku/riku_hitwussyr01.png"
    pause 0.4
    "gfx/animated/riku/riku_hitwussyr02.png"
    pause 0.4
    
  image Mamoru dead:
    "gfx/animated/mamoru/mamoru_hitl01.png"
    pause 0.4
    "gfx/animated/mamoru/mamoru_hitl02.png"
    pause 0.4
  
  image Mamoru melee:
    "gfx/animated/mamoru/mamoru_attackl01.png"
    pause 0.2
    "gfx/animated/mamoru/mamoru_attackl02.png"
    pause 0.2
    "gfx/animated/mamoru/mamoru_attackl03.png"
    pause 0.2
    "gfx/animated/mamoru/mamoru_attackl04.png"
    pause 0.2
    "gfx/animated/mamoru/mamoru_attackl05.png"
    pause 0.2
    "gfx/animated/mamoru/mamoru_attackl06.png"
    pause 0.2
    "gfx/animated/mamoru/mamoru_attackl07.png"
    pause 0.2
    "gfx/animated/mamoru/mamoru_attackl08.png"
    pause 0.2
    "gfx/animated/mamoru/mamoru_attackl09.png"
    pause 0.
  
  image Mamoru magic:
    "gfx/animated/riku/riku_firewhiter01.png"
    pause 0.2
    "gfx/animated/riku/riku_firewhiter02.png"
    pause 0.2
    "gfx/animated/riku/riku_firewhiter03.png"
    pause 0.2
    "gfx/animated/riku/riku_firewhiter04.png"
    pause 0.2
    
  image Mamoru post_attack:
    "gfx/animated/riku/riku_hairflickr01.png"
    pause 0.2
    "gfx/animated/riku/riku_hairflickr02.png"
    pause 0.2
    "gfx/animated/riku/riku_hairflickr03.png"
    pause 0.2
    "gfx/animated/riku/riku_hairflickr04.png"
    pause 0.2
    
  ########
  # Thug #
  ########
 
  image Thug idle:
    "gfx/animated/riku/riku_idler03.png"
    pause 0.2
    "gfx/animated/riku/riku_idler02.png"
    pause 0.2
    "gfx/animated/riku/riku_idler01.png"
    pause 0.2
    repeat  
    
  image Thug hit:
    "gfx/animated/riku/riku_hitr01.png"
    pause 0.4
    "gfx/animated/riku/riku_hitr02.png"
    pause 0.4
    
  image Thug hit_crit:
    "gfx/animated/riku/riku_hitwussyr01.png"
    pause 0.4
    "gfx/animated/riku/riku_hitwussyr02.png"
    pause 0.4
    
  image Thug dead:
    "gfx/animated/riku/riku_hitwussyr01.png"
    pause 0.4
    "gfx/animated/riku/riku_hitwussyr02.png"
    pause 0.4
   
  image Thug melee: 
    "gfx/animated/riku/riku_attackr01.png"
    pause 0.2
    "gfx/animated/riku/riku_attackr02.png"
    pause 0.2
    "gfx/animated/riku/riku_attackr03.png"
    pause 0.2
    "gfx/animated/riku/riku_attackr04.png"
    pause 0.2
    
  return
