# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say

screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.        
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:            
                window:
                    style "say_who_window"

                    text who:
                        id "who"
                        
            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.5
        
        vbox:
            style "menu"
            spacing 2
            
            for caption, action, chosen in items:
                
                if action:  
                    
                    button:
                        action action
                        style "menu_choice_button"                        

                        text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)
    style.menu_choice_button.yminimum = 79
    style.menu_choice_button.background = Frame("gfx/Choicebox.png", 609, 79)
    style.menu_choice_button.hover_background = Frame("gfx/Choicebox_hover.png", 609, 79)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        has vbox

        text prompt
        input id "input"

        
##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
        
# Make sure the bonus menu stuff actually exists before trying to do anything
# with them (line 201 below and all the way to the bottom, too). 
init -2 python:
  if persistent.bonus == None:
    persistent.bonus = {}
    persistent.bonus["unlocked"]      = False
    persistent.bonus["cg_gallery"]    = [False]
    persistent.bonus["music_gallery"] = [False]
    persistent.bonus["trophy_room"]   = [False]

##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
    
    imagemap:
        ground "gfx/menus/main.jpg"
        hover  "gfx/menus/main_hover.jpg"
       
        hotspot (185, 450, 105, 220) action Start()
        hotspot (365, 450, 105, 220) action ShowMenu("load")
        hotspot (555, 450, 105, 220) action ShowMenu("preferences")
        hotspot (740, 450, 105, 220) action Quit(confirm=False)
    
    if (persistent.bonus["unlocked"] == True):
      frame:
        textbutton _("Bonus") action ShowMenu("bonus")

init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98
        
        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"
    

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker:
    frame:
        xpos 310
        ypos 228
        xmaximum 365
        ymaximum 390
        
        ymargin 0
        ypadding 0
        background None
    
        $ columns = 1
        $ rows = 4
                
        # Display a grid of file slots.
        grid columns rows:
            xfill True
            yfill True
            style_group "file_picker"
            
            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):
                
                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True
                    #ymargin 10
                    #background None

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)
                    
                    # Format the description, and add it as text.
                    $ description = "% 2s. %s\n%s" % (
                        FileSlotName(i, columns * rows),
                        FileTime(i, empty=_("Empty Slot.")),
                        FileSaveName(i))

                    text description

                    key "save_delete" action FileDelete(i)



screen save:
    # This ensures that any other menu screen is replaced.
    tag menu
    
    imagemap:
        ground         "gfx/menus/save.jpg"
        idle           "gfx/menus/save.jpg"
        hover          "gfx/menus/save_hover.jpg"
        selected_idle  "gfx/menus/save_hover.jpg"
        selected_hover "gfx/menus/save_hover.jpg"
       
        hotspot (830,  70, 55, 55) action Return()          
        hotspot (771, 157, 52, 68) action FilePagePrevious()
        hotspot (771, 561, 52, 68) action FilePageNext()
        hotspot (767, 264, 60, 256) action MainMenu(confirm=True)
        
    use file_picker

screen load:
    # This ensures that any other menu screen is replaced.
    tag menu
    
    imagemap:
        ground         "gfx/menus/load.jpg"
        idle           "gfx/menus/load.jpg"
        hover          "gfx/menus/load_hover.jpg"
        selected_idle  "gfx/menus/load_hover.jpg"
        selected_hover "gfx/menus/load_hover.jpg"
       
        hotspot (830,  70, 55,  55) action Return()       
        hotspot (771, 157, 52,  68) action FilePagePrevious()
        hotspot (771, 561, 52,  68) action FilePageNext()
        hotspot (767, 264, 60, 256) action MainMenu(confirm=True)

    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)

    

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
    
screen preferences:
    tag menu

    imagemap:
        ground         "gfx/menus/options_selected_idle.jpg"
        idle           "gfx/menus/options_selected_idle.jpg"
        hover          "gfx/menus/options_selected_hover.jpg"
        selected_idle  "gfx/menus/options.jpg"
        selected_hover "gfx/menus/options_hover.jpg"
       
        hotspot (830,  70,  55, 55) action Return()   
        hotspot (274, 250, 355, 60) action Preference("music mute", "toggle")
        hotspot (694, 250,  60, 60) action Preference("music mute", "toggle")
        hotspot (274, 480, 355, 60) action Preference("sound mute", "toggle")
        hotspot (694, 480,  60, 60) action Preference("sound mute", "toggle")
        
    frame:
        background None
        
        bar:
            value Preference("music volume")
            xpos 285
            ypos 341
            xmaximum 440
            ymaximum 60
            thumb Image("gfx/menus/slider_thumb.png")
            thumb_offset 31
            left_bar None
            right_bar None
            
        bar:
            value Preference("sound volume")
            xpos 285
            ypos 568
            xmaximum 440
            ymaximum 60
            thumb Image("gfx/menus/slider_thumb.png")
            thumb_offset 31
            left_bar None
            right_bar None


init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

    add "gfx/menus/quit.jpg"
    
    modal True

    frame:
        style_group "yesno"

        xfill True
        xpos 0.3
        xmaximum 380
        ypos .25
        yanchor 0
        ypadding .05
        background None

        vbox:
            xalign 0.5
            xfill True
            
            # TODO: change font sizes in a way that actually makes some sense
            label _("{size=-4}" + message + "{/size}"):
                bottom_padding 50
            
            textbutton _("Yes"):
                action yes_action
                xfill True
            textbutton _("No"):
                action no_action
                xfill True


init -2 python:    
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5

#This code is the language chooser.
#label language_chooser:
#    scene black
    
#    menu:
#        "{font=DejaVuSans.ttf}English{/font}":
#            $ persistent.lang = "english"
#       "{font=enksh.ttf}日本語{/font}":
#            $ persistent.lang = "japanese"

#    $ renpy.utter_restart()
    
#This code changes the menu after reaching an ending.    
#screen main_menu:
#    tag menu
#Must change these labels for Endings, here.
#    if persistent.ending == "Ending 1":
#        use main_menu_1
#    else:
#        use main_menu_default

        
        
#------------------------------------------------------------------------------
#Use the below code to declare the different kinds of menu
#------------------------------------------------------------------------------

#screen main_menu_default:
#    tag menu

#    imagemap:
#        ground 'menu.png'
#        hover 'menuhover.png'
       
#        hotspot (522, 251, 722, 300) action Start()
#        hotspot (522, 315, 722, 363) action ShowMenu('load')
#        hotspot (522, 378, 722, 426) action ShowMenu('preferences')
#        hotspot (522, 443, 722, 492) action Help()
#        hotspot (522, 506, 722, 554) action Quit(confirm=False)   
        
#screen main_menu_1:
#    tag menu

#    imagemap:
#        ground 'menugood.png'
#        hover 'menugoodhover.png'
       
#        hotspot (522, 251, 722, 300) action Start()
#        hotspot (522, 315, 722, 363) action ShowMenu('load')
#        hotspot (522, 378, 722, 426) action ShowMenu('preferences')
#        hotspot (522, 443, 722, 492) action Help()
#        hotspot (522, 506, 722, 554) action Quit(confirm=False)   

# A very simple placeholder for the bonus menu.
#screen bonus:
#    # This ensures that any other menu screen is replaced.
#    tag menu
#    
#    add "gfx/menus/quit.jpg"
#    
#    frame:
#        has vbox
#        
#        if persistent.bonus["cg_gallery"][0] == True:
#          textbutton _("CG Gallery") action ShowMenu("bonus")
#        if persistent.bonus["music_gallery"][0] == True:
#          textbutton _("Music Gallery") action ShowMenu("bonus")
#        if persistent.bonus["trophy_room"][0] == True:
#          textbutton _("Trophy Room") action ShowMenu("bonus")
#        textbutton _("Return") action Return()
