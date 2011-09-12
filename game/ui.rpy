init python:
  def button_save():
    ui.frame(xpos=98,ypos=630, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/button_save.png", 
                   "gfx/buttons/button_save_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_save"))
                   
  def button_load():
    ui.frame(xpos=35,ypos=672, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/button_load.png", 
                   "gfx/buttons/button_load_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_load"))
                   
  def button_options():
    ui.frame(xpos=98,ypos=717, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/button_options.png", 
                   "gfx/buttons/button_options_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_preferences"))
    
  def button_palm_pilot():
    ui.frame(xpos=842,ypos=651, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/button_palm_pilot.png", 
                   "gfx/buttons/button_palm_pilot_hover.png", 
                   # TODO: change the "clicked" event. Now it works only once
                   clicked=renpy.curried_call_in_new_context("pda_loop"))
    
  config.window_overlay_functions.append(button_save)
  config.window_overlay_functions.append(button_load)
  config.window_overlay_functions.append(button_options)
  config.window_overlay_functions.append(button_palm_pilot)

image ui = "gfx/ui.png"
image hp_bar = "gfx/hp-bar.png"
image hp_background = "gfx/hp-background.png"
image mp_bar = "gfx/mp-bar.png"
image mp_background = "gfx/mp-background.png"
  
label show_ui:    
    show mp_background at Position(xpos=741, ypos=580)
    show mp_bar at Position(xpos=mp_x, ypos=580)

    show hp_background at Position(xpos=324, ypos=579)
    show hp_bar at Position(xpos=hp_x, ypos=581)
    
    show ui
    
    with dissolve

    return
    
label update_ui:
    $hp_x = hp_initial_x + ppp * hp
    $mp_x = mp_initial_x + ppp * mp
    show hp_bar at Position(xpos=hp_x, ypos=581)
    show mp_bar at Position(xpos=mp_x, ypos=580)
    with MoveTransition(1.0)
    
    return
