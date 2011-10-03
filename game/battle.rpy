image riroom = "gfx/backgrounds/riroom.jpg"

label battle:
  python:
    def show_battle_overlay():
      ui.frame(xpos=100, ypos=100, xmaximum=200)
      ui.vbox()
      ui.text("attack: melee", xfill=True)
      ui.textbutton("Punch", clicked=ui.returns("punch"), xfill=True)
      ui.textbutton("Swipe", clicked=ui.returns("swipe"), xfill=True)
      ui.textbutton("Kick", clicked=ui.returns("kick"), xfill=True)
      ui.text("attack: magic")
      if mp >= 10:
        ui.textbutton("fireblack", clicked=ui.returns("fireblack"), xfill=True) 
        ui.textbutton("firewhite", clicked=ui.returns("firewhite"), xfill=True)
      if mp >= 20:
        ui.textbutton("icesword", clicked=ui.returns("icesword"), xfill=True)
      ui.text("")
      ui.textbutton("return", clicked=ui.returns("return"), xfill=True)
      ui.close()
      
  show riroom
  
  call show_ui
  $hp = 100
  $mp = 100
  call update_ui
  
  image riku idle:
    "gfx/animated/riku/riku_idler01.png"
    pause 0.2
    "gfx/animated/riku/riku_idler02.png"
    pause 0.2
    "gfx/animated/riku/riku_idler03.png"
    pause 0.2
    repeat
    
  image riku punch:
    "gfx/animated/riku/riku_attackr01.png"
    pause 0.2
    "gfx/animated/riku/riku_attackr02.png"
    pause 0.2
    "gfx/animated/riku/riku_attackr03.png"
    pause 0.2
    "gfx/animated/riku/riku_attackr04.png"
    pause 0.2
    
  image riku swipe:
    "gfx/animated/riku/riku_swiper01.png"
    pause 0.2
    "gfx/animated/riku/riku_swiper02.png"
    pause 0.2
    "gfx/animated/riku/riku_swiper03.png"
    pause 0.2
    "gfx/animated/riku/riku_swiper04.png"
    pause 0.2
    
  image riku kick:
    "gfx/animated/riku/riku_kickr01.png"
    pause 0.2
    "gfx/animated/riku/riku_kickr02.png"
    pause 0.2
    "gfx/animated/riku/riku_kickr03.png"
    pause 0.2
    "gfx/animated/riku/riku_kickr04.png"
    pause 0.2
    "gfx/animated/riku/riku_kickr05.png"
    pause 0.2
    "gfx/animated/riku/riku_kickr06.png"
    pause 0.2
    "gfx/animated/riku/riku_kickr07.png"
    pause 0.2
    "gfx/animated/riku/riku_kickr08.png"
    pause 0.2
    
  image riku fireblack:
    "gfx/animated/riku/riku_fireblackr01.png"
    pause 0.2
    "gfx/animated/riku/riku_fireblackr02.png"
    pause 0.2
    "gfx/animated/riku/riku_fireblackr03.png"
    pause 0.2
    "gfx/animated/riku/riku_fireblackr04.png"
    pause 0.2
  
  image riku firewhite:
    "gfx/animated/riku/riku_firewhiter01.png"
    pause 0.2
    "gfx/animated/riku/riku_firewhiter02.png"
    pause 0.2
    "gfx/animated/riku/riku_firewhiter03.png"
    pause 0.2
    "gfx/animated/riku/riku_firewhiter04.png"
    pause 0.2
    
  image riku icesword:
    "gfx/animated/riku/riku_iceswordr01.png"
    pause 0.2
    "gfx/animated/riku/riku_iceswordr02.png"
    pause 0.2
    "gfx/animated/riku/riku_iceswordr03.png"
    pause 0.2
    "gfx/animated/riku/riku_iceswordr04.png"
    pause 0.2
    "gfx/animated/riku/riku_iceswordr05.png"
    pause 0.2
    "gfx/animated/riku/riku_iceswordr06.png"
    pause 0.2
    "gfx/animated/riku/riku_iceswordr07.png"
    pause 0.2
    "gfx/animated/riku/riku_iceswordr08.png"
    pause 0.2
    "gfx/animated/riku/riku_iceswordr09.png"
    pause 0.2
    "gfx/animated/riku/riku_iceswordr10.png"
    pause 0.2
    "gfx/animated/riku/riku_iceswordr11.png"
    pause 0.2
    
  image riku hit:
    "gfx/animated/riku/riku_hitwussyr01.png"
    pause 0.4
    "gfx/animated/riku/riku_hitwussyr02.png"
    pause 0.4
 
  image mob idle:
    "gfx/animated/riku/riku_idlel03.png"
    pause 0.2
    "gfx/animated/riku/riku_idlel02.png"
    pause 0.2
    "gfx/animated/riku/riku_idlel01.png"
    pause 0.2
    repeat  
    
  image mob attack:
    "gfx/animated/riku/riku_attackl01.png"
    pause 0.2
    "gfx/animated/riku/riku_attackl02.png"
    pause 0.2
    "gfx/animated/riku/riku_attackl03.png"
    pause 0.2
    "gfx/animated/riku/riku_attackl04.png"
    pause 0.2
    
  image mob hit:
    "gfx/animated/riku/riku_hitl01.png"
    pause 0.4
    "gfx/animated/riku/riku_hitl02.png"
    pause 0.4
      
  show riku idle at Position(xpos=0.5, ypos=0.5)
  show mob idle at Position(xpos=0.55, ypos=0.5)
  
  $fighting = True
  while fighting:
    $show_battle_overlay()
    $action = ui.interact()
    
    if action == "return":
      $fighting = False
    else:
      if action == "punch":
        show riku punch
        show mob hit
        $renpy.pause(0.8)
      elif action == "swipe":
        show riku swipe
        show mob hit
        $renpy.pause(0.8)
      elif action == "kick":
        show riku kick
        show mob hit
        $renpy.pause(1.6)
      elif action == "fireblack":
        show riku fireblack
        show mob hit
        $renpy.pause(0.8)
        $mp -= 10
      elif action == "firewhite":
        show riku firewhite
        show mob hit
        $renpy.pause(0.8)
        $mp -= 10
      elif action == "icesword":
        show riku icesword
        $renpy.pause(0.8)
        show mob hit
        $renpy.pause(1.4)
        $mp -= 20
        
        
        
      show riku idle
      show mob idle    
      
      call update_ui
    
      # enemy's turn
      show mob attack
      show riku hit
      $renpy.pause(0.8)
      
      $hp -= 10
      
      show riku idle
      show mob idle
      
      call update_ui
          
  hide riku idle
  hide mob idle
  
  hide riroom
  
  return