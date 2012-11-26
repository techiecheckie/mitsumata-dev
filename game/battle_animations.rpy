init python:
  # animation durations counted from sprite animation phases
  ANIMATION_DURATION = {}
  
  # Default slide animation duration
  ANIMATION_DURATION["slide"]        = 0.5
  # Mamoru's special slide (jump)
  ANIMATION_DURATION["Mamoru slide"] = 1.2
  
  # attack animation duration
  ANIMATION_DURATION["Riku melee"]       = 0.7
  # how long until the blow falls
  ANIMATION_DURATION["Riku melee delay"] = 0.3
  # attack duration (total)
  ANIMATION_DURATION["Riku magic"]       = 1.2
  # how long until the blow falls
  ANIMATION_DURATION["Riku magic delay"] = 0.4
  # hit animation duration
  ANIMATION_DURATION["Riku hit"]         = 0.6
  
  ANIMATION_DURATION["Roman melee"]       = 1.3
  ANIMATION_DURATION["Roman melee delay"] = 0.4
  ANIMATION_DURATION["Roman magic"]       = 1.9
  ANIMATION_DURATION["Roman magic delay"] = 1.0
  ANIMATION_DURATION["Roman hit"]         = 0.6
  
  ANIMATION_DURATION["Demon hunter melee"]       = 0.9
  ANIMATION_DURATION["Demon hunter melee delay"] = 0.4
  ANIMATION_DURATION["Demon hunter hit"]         = 0.6
  
  ANIMATION_DURATION["Demon thug melee"]       = 0.9
  ANIMATION_DURATION["Demon thug melee delay"] = 0.4
  ANIMATION_DURATION["Demon thug hit"]         = 0.6
  
  ANIMATION_DURATION["Mamoru melee"]       = 1.4
  ANIMATION_DURATION["Mamoru melee delay"] = 0.8
  ANIMATION_DURATION["Mamoru magic"]       = 1.6
  ANIMATION_DURATION["Mamoru magic delay"] = 0.2
  ANIMATION_DURATION["Mamoru hit"]         = 0.6
  
  ANIMATION_DURATION["Naomi melee"]       = 0.8
  ANIMATION_DURATION["Naomi melee delay"] = 0.4
  ANIMATION_DURATION["Naomi magic"]       = 2.0
  ANIMATION_DURATION["Naomi magic delay"] = 0.6
  ANIMATION_DURATION["Naomi hit"]         = 0.6
  
  ANIMATION_DURATION["Carniflora melee"]       = 0.8
  ANIMATION_DURATION["Carniflora melee delay"] = 0.4
  ANIMATION_DURATION["Carniflora magic"]       = 1.3
  ANIMATION_DURATION["Carniflora magic delay"] = 0.7
  ANIMATION_DURATION["Carniflora hit"]         = 0.6

########
# Riku #
########
  
image Riku idle:
  "gfx/battle/riku/riku_idlel01.png"
  pause 0.2
  "gfx/battle/riku/riku_idlel02.png"
  pause 0.2
  "gfx/battle/riku/riku_idlel03.png"
  pause 0.2
  repeat
  
image Riku hit:
  "gfx/battle/riku/riku_hitl01.png"
  pause 0.2
  "gfx/battle/riku/riku_hitl02.png"
  pause 0.4

image Riku melee:  
  "gfx/battle/riku/riku_attackl01.png"
  pause 0.2
  "gfx/battle/riku/riku_attackl02.png"
  pause 0.1
  "gfx/battle/riku/riku_attackl03.png"
  pause 0.2
  "gfx/battle/riku/riku_attackl04.png"
  pause 0.2
  
image Riku magic:
  "gfx/battle/riku/riku_firewhitel01.png"
  pause 0.2
  "gfx/battle/riku/riku_firewhitel02.png"
  pause 0.2
  "gfx/battle/riku/riku_firewhitel03.png"
  pause 0.2
  "gfx/battle/riku/riku_firewhitel04.png"
  pause 0.2
  "gfx/battle/riku/riku_firewhitel03.png"
  pause 0.2
  "gfx/battle/riku/riku_firewhitel04.png"
  pause 0.2
 
#########
# Roman #
#########
    
image Roman idle:
  "gfx/battle/roman/roman_idlel01.png"
  pause 0.2
  "gfx/battle/roman/roman_idlel02.png"
  pause 0.2
  "gfx/battle/roman/roman_idlel03.png"
  pause 0.2
  repeat
  
image Roman hit:
  "gfx/battle/roman/roman_hitwussyl01.png"
  pause 0.2
  "gfx/battle/roman/roman_hitwussyl02.png"
  pause 0.4

image Roman melee:
  "gfx/battle/roman/roman_kickl01.png"
  pause 0.2
  "gfx/battle/roman/roman_kickl02.png"
  pause 0.1
  "gfx/battle/roman/roman_kickl03.png"
  pause 0.1
  "gfx/battle/roman/roman_kickl04.png"
  pause 0.1
  "gfx/battle/roman/roman_kickl05.png"
  pause 0.2
  "gfx/battle/roman/roman_kickl06.png"
  pause 0.2
  "gfx/battle/roman/roman_kickl07.png"
  pause 0.2
  "gfx/battle/roman/roman_kickl08.png"
  pause 0.2
  
image Roman magic:
  "gfx/battle/roman/roman_iceswordl01.png"
  pause 0.2
  "gfx/battle/roman/roman_iceswordl02.png"
  pause 0.2
  "gfx/battle/roman/roman_iceswordl03.png"
  pause 0.2
  "gfx/battle/roman/roman_iceswordl04.png"
  pause 0.2
  "gfx/battle/roman/roman_iceswordl05.png"
  pause 0.2
  "gfx/battle/roman/roman_iceswordl06.png"
  pause 0.1
  "gfx/battle/roman/roman_iceswordl07.png"
  pause 0.2
  "gfx/battle/roman/roman_iceswordl08.png"
  pause 0.2
  "gfx/battle/roman/roman_iceswordl09.png"
  pause 0.1
  "gfx/battle/roman/roman_iceswordl10.png"
  pause 0.1
  "gfx/battle/roman/roman_iceswordl11.png"
  pause 0.2
    
################
# Demon hunter #
################
  
image DemonHunter idle:
  "gfx/battle/demonic_hunter/demoniccape_idler01.png"
  pause 0.2
  "gfx/battle/demonic_hunter/demoniccape_idler02.png"
  pause 0.2
  "gfx/battle/demonic_hunter/demoniccape_idler03.png"
  pause 0.2
  repeat
  
image DemonHunter hit:
  "gfx/battle/demonic_hunter/demoniccape_hitr01.png"
  pause 0.2
  "gfx/battle/demonic_hunter/demoniccape_hitr02.png"
  pause 0.4

image DemonHunter melee:
  "gfx/battle/demonic_hunter/demoniccape_swiper01.png"
  pause 0.2
  "gfx/battle/demonic_hunter/demoniccape_swiper02.png"
  pause 0.2
  "gfx/battle/demonic_hunter/demoniccape_swiper03.png"
  pause 0.2
  "gfx/battle/demonic_hunter/demoniccape_swiper04.png"
  pause 0.3
  
################
# Demon thug   #
################

image DemonThug idle:
  "gfx/battle/demonic_thug/demonic_idler01.png"
  pause 0.2
  "gfx/battle/demonic_thug/demonic_idler02.png"
  pause 0.2
  "gfx/battle/demonic_thug/demonic_idler03.png"
  pause 0.2
  repeat
    
image DemonThug hit:
  "gfx/battle/demonic_thug/demonic_hitr01.png"
  pause 0.2
  "gfx/battle/demonic_thug/demonic_hitr02.png"
  pause 0.4
  
image DemonThug melee:
  "gfx/battle/demonic_thug/demonic_swiper01.png"
  pause 0.2
  "gfx/battle/demonic_thug/demonic_swiper02.png"
  pause 0.2
  "gfx/battle/demonic_thug/demonic_swiper03.png"
  pause 0.2
  "gfx/battle/demonic_thug/demonic_swiper04.png"
  pause 0.3
    
 
##########
# Mamoru #
##########
  
image Mamoru idle:
  "gfx/battle/mamoru/mamoru_idle2r01.png"
  pause 0.2
  "gfx/battle/mamoru/mamoru_idle2r02.png"
  pause 0.2
  "gfx/battle/mamoru/mamoru_idle2r03.png"
  pause 0.2
  repeat
   
image Mamoru hit:
  "gfx/battle/mamoru/mamoru_hitr01.png"
  pause 0.2
  "gfx/battle/mamoru/mamoru_hitr02.png"
  pause 0.4
  
image Mamoru melee:
  "gfx/battle/mamoru/mamoru_attackr06.png"
  pause 0.2
  "gfx/battle/mamoru/mamoru_attackr07.png"
  pause 0.2
  "gfx/battle/mamoru/mamoru_attackr08.png"
  pause 0.4
  "gfx/battle/mamoru/mamoru_attackr09.png"
  pause 0.6
  
image Mamoru magic:
  "gfx/battle/mamoru/mamoru_firewhitehaughtyr01.png"
  pause 0.2
  "gfx/battle/mamoru/mamoru_firewhitehaughtyr02.png"
  pause 0.2
  "gfx/battle/mamoru/mamoru_firewhitehaughtyr03.png"
  pause 0.2
  "gfx/battle/mamoru/mamoru_firewhitehaughtyr04.png"
  pause 0.2
  "gfx/battle/mamoru/mamoru_firewhitehaughtyr03.png"
  pause 0.2
  "gfx/battle/mamoru/mamoru_firewhitehaughtyr04.png"
  pause 0.2
  "gfx/battle/mamoru/mamoru_firewhitehaughtyr03.png"
  pause 0.2
  "gfx/battle/mamoru/mamoru_firewhitehaughtyr04.png"
  pause 0.2
  
image Mamoru slide:
  "gfx/battle/mamoru/mamoru_attackr01.png"
  pause 0.2
  "gfx/battle/mamoru/mamoru_attackr02.png"
  pause 0.3
  "gfx/battle/mamoru/mamoru_attackr03.png"
  pause 0.3
  "gfx/battle/mamoru/mamoru_attackr04.png"
  pause 0.2
  "gfx/battle/mamoru/mamoru_attackr05.png"
  pause 0.2
    
#image Mamoru post_attack:
#  "gfx/battle/mamoru/mamoru_hairflickr01.png"
#  pause 0.2
#  "gfx/battle/mamoru/mamoru_hairflickr02.png"
#  pause 0.2
#  "gfx/battle/mamoru/mamoru_hairflickr03.png"
#  pause 0.2
#  "gfx/battle/mamoru/mamoru_hairflickr04.png"
#  pause 0.2
  
#########
# Naomi #
#########
  
image Naomi idle:
  "gfx/battle/naomi/naomi_idler01.png"
  pause 0.2
  "gfx/battle/naomi/naomi_idler02.png"
  pause 0.2
  "gfx/battle/naomi/naomi_idler03.png"
  pause 0.2
  repeat
  
image Naomi hit:
  "gfx/battle/naomi/naomi_hitr01.png"
  pause 0.2
  "gfx/battle/naomi/naomi_hitr02.png"
  pause 0.4

image Naomi melee:
  "gfx/battle/naomi/naomi_swiper01.png"
  pause 0.2

  "gfx/battle/naomi/naomi_swiper02.png"
  pause 0.2
  "gfx/battle/naomi/naomi_swiper03.png"
  pause 0.2
  "gfx/battle/naomi/naomi_swiper04.png"
  pause 0.2
  
image Naomi magic:
  "gfx/battle/naomi/naomi_magicr01.png"
  pause 0.2
  "gfx/battle/naomi/naomi_magicr02.png"
  pause 0.2
  "gfx/battle/naomi/naomi_magicr03.png"
  pause 0.2
  "gfx/battle/naomi/naomi_magicr04.png"
  pause 0.2
  "gfx/battle/naomi/naomi_magicr05.png"
  pause 0.2
  "gfx/battle/naomi/naomi_magicr06.png"
  pause 0.2
  "gfx/battle/naomi/naomi_magicr07.png"
  pause 0.2
  "gfx/battle/naomi/naomi_magicr08.png"
  pause 0.2
  "gfx/battle/naomi/naomi_magicr09.png"
  pause 0.2
  "gfx/battle/naomi/naomi_magicr10.png"
  pause 0.2


    
##############
# Carniflora #
##############
 
image Carniflora idle:
  "gfx/battle/carniflora/carniflora_idler01.png"
  pause 0.2
  "gfx/battle/carniflora/carniflora_idler02.png"
  pause 0.2
  "gfx/battle/carniflora/carniflora_idler03.png"
  pause 0.2
  "gfx/battle/carniflora/carniflora_idler04.png"
  pause 0.2
  "gfx/battle/carniflora/carniflora_idler05.png"
  pause 0.2
  "gfx/battle/carniflora/carniflora_idler06.png"
  pause 0.2
  "gfx/battle/carniflora/carniflora_idler07.png"
  pause 0.2
  "gfx/battle/carniflora/carniflora_idler08.png"
  pause 0.2
  repeat  
    
image Carniflora hit:
  "gfx/battle/carniflora/carniflora_hitr01.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_hitr02.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_hitr03.png"
  pause 0.2
  "gfx/battle/carniflora/carniflora_hitr04.png"
  pause 0.2
   
image Carniflora melee: 
  "gfx/battle/carniflora/carniflora_attack1r01.png"
  pause 0.2
  "gfx/battle/carniflora/carniflora_attack1r02.png"
  pause 0.2
  "gfx/battle/carniflora/carniflora_attack1r03.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack1r04.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack1r05.png"
  pause 0.2
  
image Carniflora magic:
  "gfx/battle/carniflora/carniflora_attack2r01.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack2r02.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack2r03.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack2r04.png"
  pause 0.2
  "gfx/battle/carniflora/carniflora_attack2r05.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack2r06.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack2r07.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack2r08.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack2r09.png"
  pause 0.2
  "gfx/battle/carniflora/carniflora_attack2r10.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack2r11.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack2r12.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack2r13.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack2r14.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack2r15.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack2r16.png"
  pause 0.2
  "gfx/battle/carniflora/carniflora_attack2r17.png"
  pause 0.1
  "gfx/battle/carniflora/carniflora_attack2r18.png"
  pause 0.1
