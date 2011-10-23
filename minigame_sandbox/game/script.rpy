define d = Character( "Dude" )

init python:

    games = [
        ("minigame_mole", "Whack-A-Mole")
        ]

screen games:

    side "c r":
        area (120, 40, 400, 300)

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                for label, name in games:
                    button:
                        action Return( label )
                        left_padding 20
                        xfill True

                        hbox:
                            text name style "button_text" min_width 400

                null height 20

                textbutton "Quit":
                    xfill True
                    action Return( False )

        bar adjustment adj style "vscrollbar"


# The game starts here.
label start:
    $ games_adjustment = ui.adjustment()

    while True:
        $ d( "Pick a game.", interact=False )

        call screen games( adj=games_adjustment )

        if _return is False:
            jump end

        call expression _return

#    window hide None
#
#    python:
#        run_minigame( WhackAMole )
#
#    window show None

label end:
    d "Leaving minigames."
    return

label minigame_mole:
    window hide None
    python:
        run_minigame( WhackAMole )
    window show None
    return
