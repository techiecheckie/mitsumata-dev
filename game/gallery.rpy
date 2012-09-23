init python:

    # Temp locked button image definition
    #renpy.image("locked_gallery_button", "gfx/gallery/gallery_locked.png")
    #renpy.image("temp1", "gfx/buttons/minigame_force.png")
    #renpy.image("temp2", "gfx/buttons/minigame_mole.png")
    #renpy.image("temp3", "gfx/buttons/minigame_platformer.png")
    #renpy.image("temp4", "gfx/buttons/minigame_power.png")
    #renpy.image("temp5", "gfx/buttons/minigame_squats.png")

    persistent.button1 = True
    persistent.button1_1 = False
    persistent.button1_2 = True
    persistent.button1_3 = True

    # Step 1. Create the gallery object.
    g = Gallery()
    g.locked_button = "locked_gallery_button"

    # Step 2. Add buttons and images to the gallery.
    g.button("dawn")
    g.condition("persistent.button1")
    g.image("temp1")
    g.condition("persistent.button1_1")
    g.image("temp2")
    g.condition("persistent.button1_2")
    g.image("temp3")
    g.condition("persistent.button1_3")

    # The transition used when switching images.
    g.transition = dissolve

# Step 3. The gallery screen we use.
screen gallery:

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add "bg dream"

    # A grid of buttons.
    grid 1 2:

        xfill True
        yfill True

        # Call make_button to show a particular button.
        add g.make_button("dawn", "gfx/gallery/thumb_room_.jpg", xalign=0.5, yalign=0.5)
        #add g.make_button("dark", "gfx/gallery/thumb_room_.jpg", xalign=0.5, yalign=0.5)
        #add g.make_button("end1", "gfx/gallery/thumb_room_.jpg", xalign=0.5, yalign=0.5)

        #add g.make_button("end2", "gfx/gallery/thumb_room_.jpg", xalign=0.5, yalign=0.5)
        #add g.make_button("end3", "gfx/gallery/thumb_room_.jpg", xalign=0.5, yalign=0.5)
        #add g.make_button("end4", "gfx/gallery/thumb_room_.jpg", xalign=0.5, yalign=0.5)

        #add g.make_button("dark mary", "gfx/gallery/thumb_room_.jpg", xalign=0.5, yalign=0.5)
        #add g.make_button("dawn mary", "gfx/gallery/thumb_room_.jpg", xalign=0.5, yalign=0.5)

        # The screen is responsible for returning to the main menu. It could also
        # navigate to other gallery screens.
        textbutton "Return" action Return() xalign 0.5 yalign 0.5
