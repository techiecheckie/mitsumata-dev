image ui        = "gfx/ui.png"
image ui_hp_bar = "gfx/hp-bar.png"
image ui_hp_bg  = "gfx/hp-background.png"
image ui_mp_bar = "gfx/mp-bar.png"
image ui_mp_bg  = "gfx/mp-background.png"
image minigame_ui     = "gfx/backgrounds/minigame_bg.png"
image minigame_hp_bar = "gfx/minigame_hp_bar.png"
image minigame_hp_bg  = "gfx/minigame_hp_bg.png"
image minigame_mp_bar = "gfx/minigame_mp_bar.png"
image minigame_mp_bg  = "gfx/minigame_mp_bg.png"

init python:
  ui_hp_area = 300
  ui_hp_initial_x = 176
  ui_hp_x = 0
      
  ui_mp_area = 283
  ui_mp_initial_x = 603
  ui_mp_x = 0
  
  mini_hp_area = 395
  mini_hp_initial_x = 113
  mini_hp_x = 0
  
  mini_mp_area = 388
  mini_mp_initial_x = 585
  mini_mp_x = 0

  def main_ui_buttons():
    ui.frame(xpos=98,ypos=630, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/ui_generic_button_hitbox.png", 
                   "gfx/buttons/button_save_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_save"))

    ui.frame(xpos=35,ypos=672, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/ui_generic_button_hitbox.png", 
                   "gfx/buttons/button_load_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_load"))

    ui.frame(xpos=98,ypos=717, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/ui_generic_button_hitbox.png", 
                   "gfx/buttons/button_options_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_preferences"))

    ui.frame(xpos=842,ypos=651, xpadding=0, ypadding=0, background=None)    
    if pda:
      ui.imagebutton("gfx/buttons/button_palm_pilot.png", 
                     "gfx/buttons/button_palm_pilot_hover.png",
                     clicked=renpy.curried_call_in_new_context("pda_loop"))
    else:
      ui.image("gfx/buttons/button_palm_pilot_disabled.png")
                    
    return
    
  def minigame_ui_buttons():
    # save
    ui.frame(xpos=40,ypos=589, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_save.png", 
                   "gfx/buttons/minigame_save_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_save"))
    # load
    ui.frame(xpos=165,ypos=611, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_load.png", 
                   "gfx/buttons/minigame_load_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_load"))
                   
    # option
    ui.frame(xpos=38,ypos=649, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_option.png", 
                   "gfx/buttons/minigame_option_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_preferences"))
   
    # game menu (minigame menu?)
    ui.frame(xpos=164,ypos=675, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_menu.png", 
                   "gfx/buttons/minigame_menu_hover.png", 
                   clicked=ui.returns(""))
                  
    # exit
    ui.frame(xpos=41,ypos=704, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_exit.png", 
                   "gfx/buttons/minigame_exit_hover.png", 
                   clicked=ui.returns("exit"))
                   
    return
    
  def calculate_new_main_ui_positions(hp, mp):
    # How big a part should the bar cover: (0.01 * hp) * area
    # so with 100 hp coverage is 100% (assuming that the value is between 0-100).
    ui_hp_x = int(ui_hp_initial_x + (0.001 * hp) * ui_hp_area)
    ui_mp_x = int(ui_mp_initial_x + (0.001 * mp) * ui_mp_area)
    
    return (ui_hp_x, ui_mp_x)
    
  def calculate_new_minigame_ui_positions(hp, mp):
    mini_hp_x = int(mini_hp_initial_x + (0.001 * hp) * mini_hp_area)
    mini_mp_x = int(mini_mp_initial_x + (0.001 * mp) * mini_mp_area)
    
    return (mini_hp_x, mini_mp_x)
  
  def show_main_ui():
    (ui_hp_x, ui_mp_x) = calculate_new_main_ui_positions(hp, mp)
  
    renpy.transition(dissolve)   
    renpy.show("ui_mp_bg",  at_list = [Position(xpos=596,     ypos=573), Transform(anchor=(0.0, 0.0))], zorder=8)
    renpy.show("ui_mp_bar", at_list = [Position(xpos=ui_mp_x, ypos=572), Transform(anchor=(1.0, 0.0))], zorder=8)
    renpy.show("ui_hp_bg",  at_list = [Position(xpos=171,     ypos=572), Transform(anchor=(0.0, 0.0))], zorder=8)
    renpy.show("ui_hp_bar", at_list = [Position(xpos=ui_hp_x, ypos=571), Transform(anchor=(1.0, 0.0))], zorder=8)
    renpy.show("ui", zorder=8)
    
    if main_ui_buttons not in config.overlay_functions:
      config.overlay_functions.append(main_ui_buttons)

    return
    
  def update_main_ui():
    (ui_hp_x, ui_mp_x) = calculate_new_main_ui_positions(hp, mp)
    
    renpy.transition(MoveTransition(1.0))
    renpy.show("ui_mp_bar", at_list = [Position(xpos=ui_mp_x, ypos=572), Transform(anchor=(1.0, 0.0))])
    renpy.show("ui_hp_bar", at_list = [Position(xpos=ui_hp_x, ypos=571), Transform(anchor=(1.0, 0.0))])
    
    renpy.pause(1.0)
    
    return
    
  def hide_main_ui():
    renpy.transition(dissolve)
    renpy.hide("ui_mp_bar")
    renpy.hide("ui_mp_bg")
    renpy.hide("ui_hp_bar")
    renpy.hide("ui_hp_bg")
    renpy.hide("ui")

    if main_ui_buttons in config.overlay_functions:
      config.overlay_functions.remove(main_ui_buttons)
    
    return
  
  def show_minigame_ui(background, battle):
    (mini_hp_x, mini_mp_x) = calculate_new_minigame_ui_positions(hp, mp)
    
    renpy.transition(dissolve)
    renpy.show(background)
    renpy.show("minigame_mp_bg",  at_list = [Position(xpos=579,       ypos=16), Transform(anchor=(0.0, 0.0))])
    renpy.show("minigame_mp_bar", at_list = [Position(xpos=mini_mp_x, ypos=18), Transform(anchor=(1.0, 0.0))])
    renpy.show("minigame_hp_bg",  at_list = [Position(xpos=105,       ypos=16), Transform(anchor=(0.0, 0.0))])
    renpy.show("minigame_hp_bar", at_list = [Position(xpos=mini_hp_x, ypos=16), Transform(anchor=(1.0, 0.0))])
    renpy.show("minigame_ui")
    
    # temp
    if not battle:
      config.overlay_functions.append(minigame_ui_buttons)

    return
    
  def update_minigame_ui(hp, mp):
    (mini_hp_x, mini_mp_x) = calculate_new_minigame_ui_positions(hp, mp)
    
    renpy.transition(MoveTransition(1.0))
    renpy.show("minigame_hp_bar", at_list = [Position(xpos=mini_hp_x, ypos=16)])
    renpy.show("minigame_mp_bar", at_list = [Position(xpos=mini_mp_x, ypos=18)])
    
    return
    
  def hide_minigame_ui(background, battle):
    renpy.transition(dissolve)
    renpy.hide(background)
    renpy.hide("minigame_mp_bar")
    renpy.hide("minigame_mp_bg")
    renpy.hide("minigame_hp_bar")
    renpy.hide("minigame_hp_bg")
    renpy.hide("minigame_ui")
    
    if not battle:
      config.overlay_functions.remove(minigame_ui_buttons)
    
    return
    
  def confirmation_window(action_taken):
    ui.frame(xpos=0.4, ypos=0.4)
    
    ui.vbox()
    
    ui.text("Are you sure you want to " + action_taken + "?")
    ui.textbutton("Yes", clicked=ui.returns("yes"))
    ui.textbutton("No", clicked=ui.returns("no"))
    
    ui.close()
    
    confirmation = ""
    confirmation = ui.interact()
    
    if confirmation == "yes":
        return True
    else:
        return False
        
  def show_message(message, size):
    if size == "large":
      box = "textbox_l"
      x_pos = 0.3 # or use a pixel value, x_pos = 500
      y_pos = 0.35
      x_max = 500
    elif size == "medium":
      box = "textbox_m"
      x_pos = 0.25
      y_pos = 0.45
      x_max = 580
    elif size == "small":
      box = "textbox_s"
      x_pos = 0.45
      y_pos = 0.47
      x_max = 130
  
    renpy.transition(dissolve)
    renpy.show(box, at_list=[Position(xpos=0.5, ypos=0.5), Transform(anchor=(0.5,0.5))], zorder=9)
    
    ui.frame(xpos=x_pos, ypos=y_pos, xmaximum=x_max, background=None)
    ui.text(message)
    
    # Full screen hidden button, "click anywhere to continue" kind
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
    ui.interact(suppress_overlay=True)
    
    renpy.transition(dissolve)
    renpy.hide(box)
    
    return

    
  def unlock_item(item_id):
    item = inventory.get_item(item_id)
    item.unlock()
    
    # Box 1
    renpy.transition(dissolve)
    renpy.show("textbox_m", at_list=[Position(xpos=0.5, ypos=0.5), Transform(anchor=(0.5,0.5))], zorder=9)
        
    ui.frame(xpos=0.25, ypos=0.45, background=None)
    ui.text(item.get_name() + " recorded")
    
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
    ui.interact(suppress_overlay=True)
    
    renpy.transition(dissolve)
    renpy.hide("textbox_m")
    
    # Box 2
    renpy.transition(dissolve)
    renpy.show("textbox_l", at_list=[Position(xpos=0.5, ypos=0.5), Transform(anchor=(0.5,0.5))], zorder=9)
    
    ui.frame(xpos=0.3, ypos=0.35, background=None)
    ui.image("gfx/items/generic_item.png")
    
    ui.frame(xpos=0.4, ypos=0.35, xmaximum=300, background=None)
    ui.text(item.get_description())
    
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
    ui.interact(suppress_overlay=True)
    
    renpy.transition(dissolve)
    renpy.hide("textbox_l")
    
    return
    
  def unlock_entry(journal_id, entry_id):
    journal_manager.unlock_entry(journal_id, entry_id)
    
    renpy.transition(dissolve)
    renpy.show("textbox_m", at_list=[Position(xpos=0.5, ypos=0.5), Transform(anchor=(0.5,0.5))], zorder=9)
        
    ui.frame(xpos=0.25, ypos=0.45, xmaximum=550, background=None)
    ui.text("Entry " + entry_id + " recorded")
    
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
    ui.interact(suppress_overlay=True)
    
    renpy.transition(dissolve)
    renpy.hide("textbox_m")
    
    return
