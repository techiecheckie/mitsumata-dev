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
  
  MAIN_UI     = True
  MINIGAME_UI = False

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
    #ui.frame(xpos=164,ypos=675, xpadding=0, ypadding=0, background=None)
    #ui.imagebutton("gfx/buttons/minigame_menu.png", 
    #               "gfx/buttons/minigame_menu_hover.png", 
    #               clicked=ui.returns(""))
                  
    # exit
    ui.frame(xpos=41,ypos=704, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_exit.png", 
                   "gfx/buttons/minigame_exit_hover.png", 
                   clicked=ui.returns("exit"))
                   
    return
    
  def calculate_new_main_ui_positions():
    # How big a part should the bar cover: (0.01 * hp) * area
    # so with 100 hp coverage is 100% (assuming that the value is between 0-100).
    UI_HP_X = int(UI_HP_INITIAL_X + (0.001 * HP) * UI_HP_AREA)
    UI_MP_X = int(UI_MP_INITIAL_X + (0.001 * MP) * UI_MP_AREA)
    
    return (UI_HP_X, UI_MP_X)
    
  def calculate_new_minigame_ui_positions(hp, mp):
    MINI_HP_X = int(MINI_HP_INITIAL_X + (0.001 * hp) * MINI_HP_AREA)
    MINI_MP_X = int(MINI_MP_INITIAL_X + (0.001 * mp) * MINI_MP_AREA)
    
    return (MINI_HP_X, MINI_MP_X)
  
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
    
  def update_main_ui():
    (UI_HP_X, UI_MP_X) = calculate_new_main_ui_positions()
    
    print HP,MP
    
    renpy.transition(MoveTransition(1.0))
    renpy.show("ui_mp_bar", at_list = [Position(xpos=UI_MP_X, ypos=572), Transform(anchor=(1.0, 0.0))], zorder=8)
    renpy.show("ui_hp_bar", at_list = [Position(xpos=UI_HP_X, ypos=571), Transform(anchor=(1.0, 0.0))], zorder=8)
    
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
    
  def update_minigame_ui(hp, mp):
    (MINI_HP_X, MINI_MP_X) = calculate_new_minigame_ui_positions(hp, mp)
    
    renpy.transition(MoveTransition(1.0))
    renpy.show("minigame_hp_bar", at_list = [Position(xpos=MINI_HP_X, ypos=16)])
    renpy.show("minigame_mp_bar", at_list = [Position(xpos=MINI_MP_X, ypos=18)])
    
    return
    
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
    
  def confirmation_window(action_taken):
    conf_window = ui.frame(xpos=0.4, ypos=0.4)
    
    ui.vbox()
    ui.text("Are you sure you want to " + action_taken + "?")
    ui.textbutton("Yes", clicked=ui.returns("yes"))
    ui.textbutton("No", clicked=ui.returns("no"))
    ui.close()
    
    confirmation = ui.interact(clear=False)
    
    ui.remove(conf_window)
    
    if confirmation == "yes":
        return True
    else:
        return False
        
  def show_message(message, size):
    if size == "large":
      # these should be about half of the image's size
      x_anchor = 265
      y_anchor = 175
      bg = "gfx/textbox.png"
      # how much space the content has (image width - padding (40px atm))
      x_max = 490
    elif size == "medium":
      x_anchor = 304
      y_anchor = 95
      bg = "gfx/textbox_2.png"
      x_max = 560
    elif size == "small":
      x_anchor = 70
      y_anchor = 40
      bg = "gfx/textbox_mini.png"
      x_max = 100
  
    renpy.transition(dissolve)
    frame = ui.frame(xmaximum=x_max, xpadding=40, ypadding=40, xpos=0.5, ypos=0.5, xanchor=x_anchor, yanchor=y_anchor, background=bg)
    ui.text(message)
    
    # Full screen hidden button, "click anywhere to continue" kind
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
    ui.interact(clear=False)
    ui.remove(frame)
    renpy.transition(dissolve)
    
    return
    
  def unlock_item(item_id):
    item = inventory.get_item(item_id)
    
    if item_id not in persistent.unlocked_items:
      persistent.unlocked_items.append(item_id)
    
    # Box 1
    renpy.transition(dissolve)
    frame = ui.frame(xmaximum=560, xpadding=40, ypadding=40, xpos=0.5, ypos=0.5, xanchor=304, yanchor=95, background="gfx/textbox_2.png")
    ui.text(item.get_name() + " recorded")

    # full screen hidden button    
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
    ui.interact(clear=False)
    ui.remove(frame)
    renpy.transition(dissolve)
    
    # Box 2
    renpy.transition(dissolve)
    ui.frame(xmaximum=490, xpadding=40, ypadding=40, xpos=0.5, ypos=0.5, xanchor=265, yanchor=175, background="gfx/textbox.png")    
    ui.hbox(spacing=40)    
    ui.image(im.Scale("gfx/items/" + item.get_id() + ".png", 75, 75))
    ui.text(item.get_description())
    ui.close()
    
    # full screen hidden button
    ui.frame(xpos=0, ypos=0, background=None)
    ui.textbutton("", xfill=True, yfill=True, clicked=ui.returns(0), background=None)
    
    ui.interact()
    renpy.transition(dissolve)
    
    update_stats(MAIN_UI)
    
    return
    
  def unlock_entry(journal_id, entry_id):
    journal = journal_manager.get_journal(journal_id)
    entry   = journal.get_entry(entry_id)
    
    new_id = journal_id + ":" + entry_id
    if new_id not in persistent.unlocked_journals:
      persistent.unlocked_journals.append(new_id)
    
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
    
  def unlock_minigame(minigame):
    if minigame not in persistent.unlocked_minigames:
      persistent.unlocked_minigames.append(minigame)
      
    return
  
  # Not supposed to be in ui.rpy, but it'll do for now.
  def update_stats(ui):
    items = inventory.get_unlocked_items()
    hp = 0
    mp = 0
    clicks = 0
    
    for item in items:
      bonuses = item.get_bonuses()
      if bonuses != None:
        print "Going through item", item.get_name()
        if bonuses.has_key("hp"):
          hp += int(bonuses["hp"])
          print "  Added hp", bonuses["hp"]
        if bonuses.has_key("mp"):
          mp += int(bonuses["mp"])
          print "  Added mp", bonuses["mp"]
        if bonuses.has_key("clicks"):
          clicks += int(bonuses["clicks"])
          print "  Added clicks", bonuses["clicks"]

    # TODO: Go through the minigame bonuses
    
    global HP
    global MP
    global CLICKS
    
    print "Setting HP/MP/CLICKS to", hp, mp, clicks
    HP = hp
    MP = mp
    CLICKS = clicks
    
    if ui == MINIGAME_UI:
      update_minigame_ui(HP, MP)
    elif ui == MAIN_UI:
      update_main_ui()
    
    return
