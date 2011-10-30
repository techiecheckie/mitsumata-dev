#---------------------
# Name Loops!
#---------------------
label sleep:
    $ hp += 20
    $ mp += 20
    $show_message("You have a long, peaceful night's sleep.", "small")
    $update_main_ui()
    return 

label research_loop:
    scene blackscr
    $show_main_ui()
    with slow_fade
    
    "I head for the library to study with Doctor Osamu."
    $renpy.pause(1.0)
    scene bg lib
    $show_main_ui
    with slow_fade
    show k neu with dissolve
    k "Ah, it's you. Come in quickly, then."
    k "Let's see..."
    k "We'll study this tonight."
    return

#----------------------------------------------
# MENU FOR NIGHTLY OPTIONS
#----------------------------------------------

menu:
    "Search.":
        call show_map
    "Sleep.":
        call sleep
    "Store.":
        call shop_loop
    "Research.":
        call research_loop
        $unlock_entry("something", "031")    
