define d = Character( "Dude" )

init python:

    game_width  = 635
    game_height = 590

    games = [
        ("minigame_mole", "Whack-A-Mole"),
        ("minigame_duck", "Hunt Duck")
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
            return

        call expression _return

label minigame_mole:
    window hide None
    python:
        run_minigame( WhackAMole,
                      0, 0,
                      game_width, game_height )
    window show None
    return

label minigame_duck:
    window hide None
    python:
        run_minigame( DuckHunt,
                      0, 0,
                      game_width, game_height )
    window show None
    return
