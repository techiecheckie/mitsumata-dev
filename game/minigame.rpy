init python:
  button = ""
  button_value = ""
  
  def enable_minigame_main_buttons():
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
                   clicked=ui.returns(("testgame", "")))
                   
    # exit
    ui.frame(xpos=42,ypos=709, xpadding=0, ypadding=0, background=None)
    ui.imagebutton("gfx/buttons/minigame_exit.png", 
                   "gfx/buttons/minigame_exit_hover.png", 
                   clicked=ui.returns(("exit", "")))

image background_minigame = "gfx/backgrounds/minigame_bg.png"
                   
label minigame:
  # Should probably use a black screen mask for the transitions so that the new
  # buttons don't pop in so suddenly. That, or replace the currently used normal
  # (idle) images with fully transparent ones.
  hide background_pda with dissolve
  show background_minigame with dissolve
  
  $button = ""
  $button_value = ""
  
  $ui.frame(xpos=60,ypos=100, xpadding=0, ypadding=0, background=None)
  $ui.text("Nothing here yet")
  
  while (True):
    if button == "exit":
      # Proper exit behaviour someday?
      hide background_minigame with dissolve
      show background_pda with dissolve
      return
    elif button == "testgame":
      # The button to launch the testgame is called "game menu" until there's
      # some other way (like the minigame menu Seira mentioned earlier) to launch
      # these
      call testgame
      
      # Would probably be a good idea to disable the menu buttons on the left 
      # before entering the minigame. --> TODO
    
    
    # Renpy disables pretty much everything after an interaction, so these need
    # to be re-enabled every time we click something
    $enable_minigame_main_buttons()
    
    #$print "waiting for input..."
    $button, button_value = ui.interact()
    #$print "", button, ":", button_value