image ui        = "gfx/ui.png"
image ui_hp_bar = "gfx/hp-bar.png"
image ui_hp_bg  = "gfx/hp-background.png"
image ui_mp_bar = "gfx/mp-bar.png"
image ui_mp_bg  = "gfx/mp-background.png"

init python:
  def button_save():
    ui.frame(xpos=98,ypos=630, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/ui_generic_button_hitbox.png", 
                   "gfx/buttons/button_save_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_save"))
                   
  def button_load():
    ui.frame(xpos=35,ypos=672, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/ui_generic_button_hitbox.png", 
                   "gfx/buttons/button_load_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_load"))
                   
  def button_options():
    ui.frame(xpos=98,ypos=717, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/ui_generic_button_hitbox.png", 
                   "gfx/buttons/button_options_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_preferences"))
    
  def button_palm_pilot():
    ui.frame(xpos=842,ypos=651, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/button_palm_pilot.png", 
                   "gfx/buttons/button_palm_pilot_hover.png",
                   clicked=renpy.curried_call_in_new_context("pda_loop"))
  
  # HP bar can move a distance of 300 pixels
  ui_hp_area = 300
  ui_hp_initial_x = 176
  ui_hp_x = int(ui_hp_initial_x + (0.01 * hp) * ui_hp_area)
  # How big a part should the bar cover: (0.01 * hp) * area
  # so with 100 hp coverage is 100% (assuming that the value is between 0-100).
      
  ui_mp_area = 283
  ui_mp_initial_x = 603
  ui_mp_x = int(ui_mp_initial_x + (0.01 * mp) * ui_mp_area)
  
label show_ui:    
  python:
    renpy.transition(dissolve)
    renpy.show("ui_mp_bg",  at_list = [Position(xpos=596,     ypos=573), Transform(anchor=(0.0, 0.0))])
    renpy.show("ui_mp_bar", at_list = [Position(xpos=ui_mp_x, ypos=572), Transform(anchor=(1.0, 0.0))])
    renpy.show("ui_hp_bg",  at_list = [Position(xpos=171,     ypos=572), Transform(anchor=(0.0, 0.0))])
    renpy.show("ui_hp_bar", at_list = [Position(xpos=ui_hp_x, ypos=571), Transform(anchor=(1.0, 0.0))])
    renpy.show("ui")
    
    config.overlay_functions.append(button_save)
    config.overlay_functions.append(button_load)
    config.overlay_functions.append(button_options)
    config.overlay_functions.append(button_palm_pilot)

  return
    
label update_ui:
  python:
    ui_hp_x = int(ui_hp_initial_x + (0.01 * hp) * ui_hp_area)
    ui_mp_x = int(ui_mp_initial_x + (0.01 * mp) * ui_mp_area)
    
    renpy.transition(MoveTransition(1.0))
    renpy.show("ui_mp_bar", at_list = [Position(xpos=ui_mp_x, ypos=572), Transform(anchor=(1.0, 0.0))])
    renpy.show("ui_hp_bar", at_list = [Position(xpos=ui_hp_x, ypos=571), Transform(anchor=(1.0, 0.0))])
    
  return
    
label hide_ui:
  python:
    renpy.transition(dissolve)
    renpy.hide("ui_mp_bar")
    renpy.hide("ui_mp_bg")
    renpy.hide("ui_hp_bar")
    renpy.hide("ui_hp_bg")
    renpy.hide("ui")
    
    config.overlay_functions.remove(button_save)
    config.overlay_functions.remove(button_load)
    config.overlay_functions.remove(button_options)
    config.overlay_functions.remove(button_palm_pilot)
    
  return