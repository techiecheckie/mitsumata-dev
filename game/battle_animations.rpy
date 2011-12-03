init python:
  # how long the animation lasts (how long the target waits)
  ANIMATION_DELAYS = {}
  # how long until the target should display hit animation
  HIT_DELAYS = {}
  
  # Default slide animation duration
  ANIMATION_DELAYS["slide"] = 0.5

  ANIMATION_DELAYS["Riku melee"] = 0.8
  HIT_DELAYS["Riku melee"]       = 0.4
  
  ANIMATION_DELAYS["Riku magic"] = 1.2
  HIT_DELAYS["Riku magic"]       = 0.4  
  
  ANIMATION_DELAYS["Roman melee"] = 1.6
  HIT_DELAYS["Roman melee"]       = 0.6

  ANIMATION_DELAYS["Roman magic"] = 2.2
  HIT_DELAYS["Roman magic"]       = 1.0
  
  ANIMATION_DELAYS["Demon hunter melee"] = 0.8
  HIT_DELAYS["Demon hunter melee"]       = 0.4  
  
  ANIMATION_DELAYS["Demon thug melee"] = 0.8
  HIT_DELAYS["Demon thug melee"]       = 0.2
  
  ANIMATION_DELAYS["Mamoru melee"] = 1.4
  HIT_DELAYS["Mamoru melee"]       = 0.8
  
  ANIMATION_DELAYS["Mamoru magic"] = 1.6
  HIT_DELAYS["Mamoru magic"]       = 0.2
  
  ANIMATION_DELAYS["Naomi melee"] = 0.8
  HIT_DELAYS["Naomi melee"]       = 0.4
  
  ANIMATION_DELAYS["Naomi magic"] = 2.0
  HIT_DELAYS["Naomi magic"]       = 0.6

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
  pause 0.2
  "gfx/animated/riku/riku_hitl02.png"
  pause 0.4
  
image Riku hit_crit:
  "gfx/animated/riku/riku_hitwussyl01.png"
  pause 0.2
  "gfx/animated/riku/riku_hitwussyl02.png"
  pause 0.4
  
image Riku dead:
  "gfx/animated/riku/riku_hitwussyl01.png"
  pause 0.2
  "gfx/animated/riku/riku_hitwussyl02.png"
  pause 0.4
    
image Riku melee:  
  "gfx/animated/riku/riku_attackl01.png"
  pause 0.2
  "gfx/animated/riku/riku_attackl02.png"
  pause 0.2
  "gfx/animated/riku/riku_attackl03.png"
  pause 0.2
  "gfx/animated/riku/riku_attackl04.png"
  pause 0.2
  
image Riku magic:
  "gfx/animated/riku/riku_firewhitel01.png"
  pause 0.2
  "gfx/animated/riku/riku_firewhitel02.png"
  pause 0.2
  "gfx/animated/riku/riku_firewhitel03.png"
  pause 0.2
  "gfx/animated/riku/riku_firewhitel04.png"
  pause 0.2
  "gfx/animated/riku/riku_firewhitel03.png"
  pause 0.2
  "gfx/animated/riku/riku_firewhitel04.png"
  pause 0.2
 
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
  "gfx/animated/roman/roman_hitwussyl01.png"
  pause 0.2
  "gfx/animated/roman/roman_hitwussyl02.png"
  pause 0.4
    
image Roman hit_crit:
  "gfx/animated/roman/roman_hitwussyl01.png"
  pause 0.2
  "gfx/animated/roman/roman_hitwussyl02.png"
  pause 0.4
  
image Roman dead:
  "gfx/animated/roman/roman_hitwussyl01.png"
  pause 0.2
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
  "gfx/animated/demonic_hunter/demoniccape_idler01.png"
  pause 0.2
  "gfx/animated/demonic_hunter/demoniccape_idler02.png"
  pause 0.2
  "gfx/animated/demonic_hunter/demoniccape_idler03.png"
  pause 0.2
  repeat
  
image DemonHunter hit:
  "gfx/animated/demonic_hunter/demoniccape_hitr01.png"
  pause 0.2
  "gfx/animated/demonic_hunter/demoniccape_hitr02.png"
  pause 0.4

image DemonHunter hit_crit:
  "gfx/animated/demonic_hunter/demoniccape_hitr01.png"
  pause 0.2
  "gfx/animated/demonic_hunter/demoniccape_hitr02.png"
  pause 0.4

image DemonHunter dead:
  "gfx/animated/demonic_hunter/demoniccape_hitr01.png"
  pause 0.2
  "gfx/animated/demonic_hunter/demoniccape_hitr02.png"
  pause 0.4

image DemonHunter melee:
  "gfx/animated/demonic_hunter/demoniccape_swiper01.png"
  pause 0.2
  "gfx/animated/demonic_hunter/demoniccape_swiper02.png"
  pause 0.2
  "gfx/animated/demonic_hunter/demoniccape_swiper03.png"
  pause 0.2
  "gfx/animated/demonic_hunter/demoniccape_swiper04.png"
  pause 0.2
  
################
# Demon thug #
################

image DemonThug idle:
  "gfx/animated/demonic_thug/demonic_idler01.png"
  pause 0.2
  "gfx/animated/demonic_thug/demonic_idler02.png"
  pause 0.2
  "gfx/animated/demonic_thug/demonic_idler03.png"
  pause 0.2
  repeat
    
image DemonThug hit:
  "gfx/animated/demonic_thug/demonic_hitr01.png"
  pause 0.2
  "gfx/animated/demonic_thug/demonic_hitr02.png"
  pause 0.4
 
image DemonThug hit_crit:
  "gfx/animated/demonic_thug/demonic_hitr01.png"
  pause 0.2
  "gfx/animated/demonic_thug/demonic_hitr02.png"
  pause 0.4
  
image DemonThug dead:
  "gfx/animated/demonic_thug/demonic_hitr01.png"
  pause 0.2
  "gfx/animated/demonic_thug/demonic_hitr02.png"
  pause 0.4
  
image DemonThug melee:
  "gfx/animated/demonic_thug/demonic_swiper01.png"
  pause 0.2
  "gfx/animated/demonic_thug/demonic_swiper02.png"
  pause 0.2
  "gfx/animated/demonic_thug/demonic_swiper03.png"
  pause 0.2
  "gfx/animated/demonic_thug/demonic_swiper04.png"
  pause 0.2
    
 
##########
# Mamoru #
##########
  
image Mamoru idle:
  "gfx/animated/mamoru/mamoru_idle2r01.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_idle2r02.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_idle2r03.png"
  repeat
   
image Mamoru hit:
  "gfx/animated/mamoru/mamoru_hitr01.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_hitr02.png"
  pause 0.4
   
image Mamoru hit_crit:
  "gfx/animated/riku/riku_hitwussyr01.png"
  pause 0.2
  "gfx/animated/riku/riku_hitwussyr02.png"
  pause 0.4
  
image Mamoru dead:
  "gfx/animated/mamoru/mamoru_hitr01.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_hitr02.png"
  pause 0.4

# not in use   
#$animation_delays["Mamoru slide"] = 1.0
#image Mamoru slide:
  #  "gfx/animated/mamoru/mamoru_attackr01.png"
  #  pause 0.2
  #  "gfx/animated/mamoru/mamoru_attackr02.png"
  #  pause 0.2
  #  "gfx/animated/mamoru/mamoru_attackr03.png"
  #  pause 0.2
  #  "gfx/animated/mamoru/mamoru_attackr04.png"
  #  pause 0.2
  #  "gfx/animated/mamoru/mamoru_attackr05.png"
  #  pause 0.2
  
image Mamoru melee:
  "gfx/animated/mamoru/mamoru_attackr06.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_attackr07.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_attackr08.png"
  pause 0.4
  "gfx/animated/mamoru/mamoru_attackr09.png"
  pause 0.6
  
image Mamoru magic:
  "gfx/animated/mamoru/mamoru_firewhitehaughtyr01.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_firewhitehaughtyr02.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_firewhitehaughtyr03.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_firewhitehaughtyr04.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_firewhitehaughtyr03.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_firewhitehaughtyr04.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_firewhitehaughtyr03.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_firewhitehaughtyr04.png"
  pause 0.2
    
image Mamoru post_attack:
  "gfx/animated/mamoru/mamoru_hairflickr01.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_hairflickr02.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_hairflickr03.png"
  pause 0.2
  "gfx/animated/mamoru/mamoru_hairflickr04.png"
  pause 0.2
  
#########
# Naomi #
#########
  
image Naomi idle:
  "gfx/animated/naomi/naomi_idler01.png"
  pause 0.2
  "gfx/animated/naomi/naomi_idler02.png"
  pause 0.2
  "gfx/animated/naomi/naomi_idler03.png"
  pause 0.2
  repeat
  
image Naomi hit:
  "gfx/animated/naomi/naomi_hitr01.png"
  pause 0.2
  "gfx/animated/naomi/naomi_hitr02.png"
  pause 0.4
  
image Naomi hit_crit:
  "gfx/animated/naomi/naomi_hitr01.png"
  pause 0.2
  "gfx/animated/naomi/naomi_hitr02.png"
  pause 0.4
  
image Naomi dead:
  "gfx/animated/naomi/naomi_hitr01.png"
  pause 0.2
  "gfx/animated/naomi/naomi_hitr02.png"
  pause 0.4

image Naomi melee:
  "gfx/animated/naomi/naomi_swiper01.png"
  pause 0.2
  "gfx/animated/naomi/naomi_swiper02.png"
  pause 0.2
  "gfx/animated/naomi/naomi_swiper03.png"
  pause 0.2
  "gfx/animated/naomi/naomi_swiper04.png"
  pause 0.2
  
image Naomi magic:
  "gfx/animated/naomi/naomi_magicr01.png"
  pause 0.2
  "gfx/animated/naomi/naomi_magicr02.png"
  pause 0.2
  "gfx/animated/naomi/naomi_magicr03.png"
  pause 0.2
  "gfx/animated/naomi/naomi_magicr04.png"
  pause 0.2
  "gfx/animated/naomi/naomi_magicr05.png"
  pause 0.2
  "gfx/animated/naomi/naomi_magicr06.png"
  pause 0.2
  "gfx/animated/naomi/naomi_magicr07.png"
  pause 0.2
  "gfx/animated/naomi/naomi_magicr08.png"
  pause 0.2
  "gfx/animated/naomi/naomi_magicr09.png"
  pause 0.2
  "gfx/animated/naomi/naomi_magicr10.png"
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
  pause 0.2
  "gfx/animated/riku/riku_hitr02.png"
  pause 0.4
  
image Thug hit_crit:
  "gfx/animated/riku/riku_hitwussyr01.png"
  pause 0.2
  "gfx/animated/riku/riku_hitwussyr02.png"
  pause 0.4
    
image Thug dead:
  "gfx/animated/riku/riku_hitwussyr01.png"
  pause 0.2
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