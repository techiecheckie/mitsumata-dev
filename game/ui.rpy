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
image minigame_bg     = Solid( "#000" )

init python:
  # the distance the health bar can move
  UI_HP_AREA = 300
  # where it starts from
  UI_HP_INITIAL_X = 176
  # and how far it should be from the initial position (100% health = 300 px)
  UI_HP_X = 0

  # the above applies to all three below
  UI_MP_AREA = 283
  UI_MP_INITIAL_X = 603
  UI_MP_X = 0
  
  MINI_HP_AREA = 395
  MINI_HP_INITIAL_X = 113
  MINI_HP_X = 0
  
  MINI_MP_AREA = 388
  MINI_MP_INITIAL_X = 585
  MINI_MP_X = 0
  
  MESSAGE_BOX_PADDING_X = 40
  MESSAGE_BOX_PADDING_Y = 40

  # Adds main ui buttons (the stuff on the bottom of the screen) to the ui layer
  # stack. Used as a config.overlay_functions.append() parameter
  def main_ui_buttons():
    ui.frame(xpos=98,ypos=630, xpadding=0, ypadding=0, background=None)
    ui.imagebutton(im.Scale("gfx/transparent.png", 83, 44),
                   "gfx/buttons/button_save_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_save"))

    ui.frame(xpos=35,ypos=672, xpadding=0, ypadding=0, background=None)
    ui.imagebutton(im.Scale("gfx/transparent.png", 83, 44), 
                   "gfx/buttons/button_load_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_load"))

    ui.frame(xpos=98,ypos=717, xpadding=0, ypadding=0, background=None)
    ui.imagebutton(im.Scale("gfx/transparent.png", 84, 45),
                   "gfx/buttons/button_options_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_preferences"))

    ui.frame(xpos=842,ypos=651, xpadding=0, ypadding=0, background=None)    
    if pda:
      ui.imagebutton(im.Scale("gfx/transparent.png", 145, 111), 
                     "gfx/buttons/button_palm_pilot_hover.png",
                     clicked=renpy.curried_call_in_new_context("pda_loop"))
    else:
      ui.image("gfx/buttons/button_palm_pilot_disabled.png")
                    
    return
  
  # Adds minigame ui buttons to the ui layer stack. Like the function above,
  # this is also usually passed as a parameter to config.overlay_functions.append()
  # function.
  def minigame_ui_buttons():
    ui.frame(xpos=40,ypos=589, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_save.png", 
                   "gfx/buttons/minigame_save_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_save"))

    ui.frame(xpos=165,ypos=611, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_load.png", 
                   "gfx/buttons/minigame_load_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_load"))
                   

    ui.frame(xpos=38,ypos=649, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_option.png", 
                   "gfx/buttons/minigame_option_hover.png", 
                   clicked=renpy.curried_call_in_new_context("_game_menu_preferences"))
   
    # game menu (minigame menu?)
    #ui.frame(xpos=164,ypos=675, xpadding=0, ypadding=0, background=None)
    #ui.imagebutton("gfx/buttons/minigame_menu.png", 
    #               "gfx/buttons/minigame_menu_hover.png", 
    #               clicked=ui.returns(""))
                  

    ui.frame(xpos=41,ypos=704, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_exit.png", 
                   "gfx/buttons/minigame_exit_hover.png", 
                   clicked=ui.returns("exit"))
                   
    return
  
  # Calculates the positions of hp and mp bars on the main ui.
  #
  # How big a part should the bar cover: (0.001 * hp) * area
  # With 1000 hp/mp, the coverage is 100%
  def calculate_new_main_ui_positions():
    UI_HP_X = int(UI_HP_INITIAL_X + (0.001 * HP) * UI_HP_AREA)
    UI_MP_X = int(UI_MP_INITIAL_X + (0.001 * MP) * UI_MP_AREA)
    
    return (UI_HP_X, UI_MP_X)
  
  # Calculates the positions of hp and mp bars on the minigame ui
  def calculate_new_minigame_ui_positions(hp, mp):
    MINI_HP_X = int(MINI_HP_INITIAL_X + (0.001 * hp) * MINI_HP_AREA)
    MINI_MP_X = int(MINI_MP_INITIAL_X + (0.001 * mp) * MINI_MP_AREA)
    
    return (MINI_HP_X, MINI_MP_X)
  
  # Displays all the elements that are part of the main ui (hp/mp bars and the
  # actual ui on top of those). The hp/mp bar positions are recalculated each
  # time this function is called.
  def show_main_ui():
    (UI_HP_X, UI_MP_X) = calculate_new_main_ui_positions()
  
    renpy.transition(dissolve)   
    renpy.show("ui_mp_bg",  at_list = [Position(xpos=596,     ypos=573), Transform(anchor=(0.0, 0.0))], zorder=8)
    renpy.show("ui_mp_bar", at_list = [Position(xpos=UI_MP_X, ypos=572), Transform(anchor=(1.0, 0.0))], zorder=8)
    renpy.show("ui_hp_bg",  at_list = [Position(xpos=171,     ypos=572), Transform(anchor=(0.0, 0.0))], zorder=8)
    renpy.show("ui_hp_bar", at_list = [Position(xpos=UI_HP_X, ypos=571), Transform(anchor=(1.0, 0.0))], zorder=8)
    renpy.show("ui", zorder=8)
    
    if main_ui_buttons not in config.overlay_functions:
      config.overlay_functions.append(main_ui_buttons)

    return
  
  # Moves the hp and mp bar in the main ui to their new positions using a
  # MoveTransition
  def update_main_ui():
    (UI_HP_X, UI_MP_X) = calculate_new_main_ui_positions()
    
    renpy.transition(MoveTransition(1.0))
    renpy.show("ui_mp_bar", at_list = [Position(xpos=UI_MP_X, ypos=572), Transform(anchor=(1.0, 0.0))], zorder=8)
    renpy.show("ui_hp_bar", at_list = [Position(xpos=UI_HP_X, ypos=571), Transform(anchor=(1.0, 0.0))], zorder=8)
    
    renpy.pause(1.0)
    
    return
  
  # Hides all the elements of the main ui
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
  
  # Displays all the elements that are part of the base minigame ui. A background
  # can be given as a parameter to be displayed behind the minigame ui.
  def show_minigame_ui(background):
    (MINI_HP_X, MINI_MP_X) = calculate_new_minigame_ui_positions(HP, MP)
    
    renpy.transition(dissolve)
    if background:
      renpy.show(background, zorder=-2)
    renpy.show("minigame_mp_bg",  at_list = [Position(xpos=579,       ypos=16), Transform(anchor=(0.0, 0.0))])
    renpy.show("minigame_mp_bar", at_list = [Position(xpos=MINI_MP_X, ypos=18), Transform(anchor=(1.0, 0.0))])
    renpy.show("minigame_hp_bg",  at_list = [Position(xpos=105,       ypos=16), Transform(anchor=(0.0, 0.0))])
    renpy.show("minigame_hp_bar", at_list = [Position(xpos=MINI_HP_X, ypos=16), Transform(anchor=(1.0, 0.0))])
    renpy.show("minigame_ui")
    
    config.overlay_functions.append(minigame_ui_buttons)

    return
  
  # Moves the hp and mp bar in the minigame ui to their new positions using a
  # MoveTransition.
  def update_minigame_ui(hp, mp):
    (MINI_HP_X, MINI_MP_X) = calculate_new_minigame_ui_positions(hp, mp)
    
    renpy.transition(MoveTransition(1.0))
    renpy.show("minigame_hp_bar", at_list = [Position(xpos=MINI_HP_X, ypos=16)])
    renpy.show("minigame_mp_bar", at_list = [Position(xpos=MINI_MP_X, ypos=18)])
    
    return
  
  # Hides all the elements of the base minigame ui
  def hide_minigame_ui(background):
    renpy.transition(dissolve)
    if background:
      renpy.hide(background)
    renpy.hide("minigame_mp_bar")
    renpy.hide("minigame_mp_bg")
    renpy.hide("minigame_hp_bar")
    renpy.hide("minigame_hp_bg")
    renpy.hide("minigame_ui")
    
    config.overlay_functions.remove(minigame_ui_buttons)
    
    return
  
  # Displays a message in the middle of the screen in a box of the size specified 
  # in the parameters. The anchor values specified for each size should be about
  # half of the background image's size to have it properly displayed in the
  # middle of the screen.
  def show_message(message, size):
    if size == "large":
      bg = "gfx/textbox.png"
      x_anchor = 265
      y_anchor = 175
      x_max    = 490
    elif size == "medium":
      bg = "gfx/textbox_2.png"
      x_anchor = 304
      y_anchor = 95
      x_max    = 560
    elif size == "small":
      bg = "gfx/textbox_mini.png"
      x_anchor = 70
      y_anchor = 40
      x_max    = 100
  
    renpy.transition(dissolve)
    frame = ui.frame(xmaximum=x_max, xpadding=40, ypadding=40, 
                     xpos=0.5, ypos=0.5, 
                     xanchor=x_anchor, yanchor=y_anchor, 
                     background=bg)
    ui.text(message)
    
    # Full screen hidden button, "click anywhere to continue" kind
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
    ui.interact(clear=False)
    ui.remove(frame)
    renpy.transition(dissolve)
    
    return
    
  # Displays two windows containing information about the item that was unlocked:
  # the first one is a plain "(item name) recorded" message in a smaller window,
  # and the second one displays the item's name, description and image in a large
  # window using a hbox.
  def show_item_unlock(item):    
    # Box 1: "Knife recorded"
    renpy.transition(dissolve)
    frame = ui.frame(xmaximum=560, xpadding=40, ypadding=40, xpos=0.5, ypos=0.5, xanchor=304, yanchor=95, background="gfx/textbox_2.png")
    ui.text(item.get_name() + " recorded")

    # full screen hidden button    
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
    ui.interact(clear=False)
    ui.remove(frame)
    renpy.transition(dissolve)
    
    # Box 2: displays item info + image
    renpy.transition(dissolve)
    ui.frame(xmaximum=490, xpadding=40, ypadding=40, xpos=0.5, ypos=0.5, xanchor=265, yanchor=175, background="gfx/textbox.png")    
    ui.hbox(spacing=40)    
    ui.image(im.Scale("gfx/items/" + item.get_id() + ".png", 75, 75))
    ui.text(item.get_name() + "\n\n" + item.get_description())
    ui.close()
    
    # full screen hidden button
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
    ui.interact()
    renpy.transition(dissolve)
    renpy.pause(1.0)
    
    update_stats()
    update_main_ui()
    
    return
  
  # Displays two windows containing information about the journal entry that was
  # unlocked. This function works like the unlock_item function does: two windows,
  # the first one being "Entry (entry_id) recorded", and the second displays
  # the entry's image and title.
  def show_entry_unlock(entry):
    # Box 1
    renpy.transition(dissolve)
    frame = ui.frame(xmaximum=560, xpadding=40, ypadding=40, xpos=0.5, ypos=0.5, xanchor=304, yanchor=95, background="gfx/textbox_2.png")
    ui.text("Entry " + entry_id + " recorded")

    # full screen hidden button    
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
    ui.interact(clear=False)
    ui.remove(frame)
    renpy.transition(dissolve)
    
    # Box 2
    renpy.transition(dissolve)
    ui.frame(xmaximum=560, xpadding=40, ypadding=40, xpos=0.5, ypos=0.5, xanchor=304, yanchor=95, background="gfx/textbox_2.png")    
    ui.hbox(spacing=40)    
    ui.image(im.Scale("gfx/journals/" + journal_id + ".png", 75, 75))
    ui.text(entry.get_title())
    ui.close()
    
    # full screen hidden button
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
    ui.interact()
    renpy.transition(dissolve)
    
    return
