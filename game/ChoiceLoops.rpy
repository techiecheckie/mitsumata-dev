#---------------------
# Name Loops!
#---------------------
label sleep:
    $ hp += 1000
    $ mp += 1000
    $show_message("You have a long, peaceful night's sleep.", "medium")
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

 
