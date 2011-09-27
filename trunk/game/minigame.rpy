init python:
  button = ""
  button_value = ""
  
  def minigame_main_buttons():
    # save
    ui.frame(xpos=42,ypos=594, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_save.png", 
                   "gfx/buttons/minigame_save_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_save"))
    
    # load
    ui.frame(xpos=167,ypos=615, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_load.png", 
                   "gfx/buttons/minigame_load_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_load"))
                   
    # option
    ui.frame(xpos=34,ypos=653, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_option.png", 
                   "gfx/buttons/minigame_option_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_preferences"))
   
    # game menu (minigame menu?)
    ui.frame(xpos=170,ypos=679, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_menu.png", 
                   "gfx/buttons/minigame_menu_hover.png", 
                   clicked=ui.returns("molegame"))
               
    ui.frame(xpos=60,ypos=100, xpadding=0, ypadding=0, background=None)
    ui.text("(Add instructions here)")
    
  def minigame_exit_button():                   
    # exit
    ui.frame(xpos=42,ypos=709, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_exit.png", 
                   "gfx/buttons/minigame_exit_hover.png", 
                   clicked=ui.returns("exit"))


image background_minigame = "gfx/backgrounds/minigame_bg.png"
                   
label minigame:
  hide background_pda
  $config.overlay_functions.remove(pda_buttons)
  with dissolve
  
  show background_minigame 
  $config.overlay_functions.append(minigame_main_buttons)
  $config.overlay_functions.append(minigame_exit_button)
  with dissolve
  
  while (True):
    $button = ui.interact()
    if button == "exit":
      hide background_minigame
      $config.overlay_functions.remove(minigame_main_buttons)
      $config.overlay_functions.remove(minigame_exit_button)
      with dissolve
      
      show background_pda 
      $config.overlay_functions.append(pda_buttons)
      with dissolve
      
      return
      
    elif button == "molegame":
      $config.overlay_functions.remove(minigame_main_buttons)
      call mole_game
      $config.overlay_functions.append(minigame_main_buttons)
      
  