# The game starts here.
label start:
    window hide None

    python:
        driver = MinigameDriver( DuckHunt() )
        ui.add( driver )
        ui.interact( suppress_overlay=True, suppress_underlay=True )

    window show None
