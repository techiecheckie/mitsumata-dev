## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:

    # location of log relative to game/ directory.
    config.log = "%s/log.txt" % renpy.config.gamedir

    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released, so the user can't
    ## cheat using developer tools.

    config.developer = True

    ## These control the width and height of the screen.

    config.screen_width = 1024
    config.screen_height = 768

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Mitsumata: The First Act, Part I"

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "rosegold games"
    config.version = "0.0"

    #########################################
    # Themes
    
    ## We then want to call a theme function. themes.roundrect is
    ## a theme that features the use of rounded rectangles. It's
    ## the only theme we currently support.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.tv(
        # Color scheme: Muted Horror
                                    
        ## The color of an idle widget face.
        widget = "#777777",

        ## The color of a focused widget face.
        widget_hover = "#73735C",

        ## The color of the text in a widget.
        widget_text = "#404033",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#000000",

        ## The color of a disabled widget face. 
        disabled = "#73735C",

        ## The color of disabled widget text.
        disabled_text = "#8C8C70",

        ## The color of informational labels.
        label = "#1A0001",

        ## The color of a frame containing widgets.
        frame = "#555544",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "#1A0001",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "#1A0001",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.            
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    style.window.background = Frame("gfx/transparent.png", 1, 1)
    style.default.color = "#000000"

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    style.window.left_margin = 262
    style.window.right_margin = 262
    style.window.top_margin = -20
    style.window.bottom_margin = 30

    ## Padding is space inside the window, where the background is
    ## drawn.

    #style.window.left_padding = 6
    #style.window.right_padding = 6
    #style.window.top_padding = 6
    #style.window.bottom_padding = 6

    ## This is the minimum height of the window, including the margins
    ## and padding.

    # style.window.yminimum = 250


    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    # style.default.font = "TimesNewRoman.ttf"

    ## The default size of text.

    style.default.size = 19

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to False if the game does not have voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    # config.main_menu_music = "music/main_menu_theme.mp3"

    ## Stick language chooser into main menu.
    
    config.main_menu.insert(3, (u'Language', "language_chooser", "True"))

    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.   
    config.help = "README.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = fade

    ## Used when exiting the game menu to the game.
    config.exit_transition = fade

    ## Used between screens of the game menu.
    config.intra_transition = fade

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = fade

    ## Used when returning to the main menu from the game.
    config.game_main_transition = fade

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = fade

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = fade

    ## Used when a game is loaded.
    config.after_load_transition = fade

    ## Used when the window is shown.
    config.window_show_transition = fade

    ## Used when the window is hidden.
    config.window_hide_transition = fade


    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persisten information can be found by the init code.)
python early:
    config.save_directory = "MitsumataProgram-1313711868"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 20

    #########################################
    ## More customizations can go here.
    
init python hide:
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    
    ###############################################
    ## Language change
init -3 python:
    if persistent.lang is None:
        persistent.lang = "english"

    lang = persistent.lang
    
    ##########################################################
    ## CG Gallery
init:
    # Position the navigation on the right side of the screen.
    $ style.gallery_nav_frame.xpos = 800 - 10
    $ style.gallery_nav_frame.xanchor = 1.0
    $ style.gallery_nav_frame.ypos = 12

    # Add the gallery to the main menu.
    $ config.main_menu.insert(2, ('Gallery', "gallery", "True"))

#######################################    
# The entry is the code for picture galleries.
#######################################
label gallery:
    python hide:

        # Construct a new gallery object.
        g = Gallery()

        # The image used for locked buttons.
        g.locked_button = "gfx/gal/gallery_locked.png"
        
        # The background of a locked image.
        g.locked_background = "gfx/backgrounds/room1.png"

        # Frames added over unlocked buttons, in hover and idle states.
        g.hover_border = "gfx/gal/gallery_hover.png"
        g.idle_border = "gfx/gal/gallery_unlocked.png"

        # An images used as the background of the various gallery pages.
        g.background = "gfx/backgrounds/room1.png"

        # Lay out the gallery images on the screen.
        # These settings lay images out 3 across and 4 down.
        # The upper left corner of the gird is at xpos 10, ypos 20.
        # They expect button images to be 155x112 in size.
        g.grid_layout((3, 4), (10, 12), (160, 124))

        # Show the background page.
        g.page("Backgrounds")

        # Our first button is a picture of the beach.
        g.button("gfx/gal/thumb_room.png")
        #
        # These show images, if they have been unlocked. The image name must
        # have been defined using an image statement.
        g.unlock_image("bg riroom")
        g.unlock_image("bg roroom")
        g.unlock_image("bg soroom")
        g.unlock_image("bg suroom")
        
        #
        # This shows a displayable...
        g.display("beach_sketch.jpg")
        # ... if all prior images have been shown.
        g.allprior()

        # A second set of images.
        #g.button("thumb_hall.jpg")
        #g.unlock_image("bg hall1")
        #g.unlock_image("bg hall2")
        #g.display("lighthouse_sketch.jpg")
        #g.allprior()
        
        #g.button("thumb_for.jpg")
        #g.unlock_image("bg dfor1")
        #g.unlock_image("bg dfor2")
        #g.unlock_image("bg dfor3")
        #g.unlock_image("bg nfor1")
        #g.unlock_image("bg nfor2")
        #g.unlock_image("bg nfor3")
        #g.display("lighthouse_sketch.jpg")
        #g.allprior()
        
        #g.button("thumb_temple.jpg")
        #g.unlock_image("bg lib")
        #g.unlock_image("bg kitchen")
        #g.unlock_image("bg gar1")
        #g.unlock_image("bg gar2")
        #g.display("lighthouse_sketch.jpg")
        #g.allprior()

        #g.button("thumb_street.jpg")
        #g.unlock_image("bg street")
        #g.unlock_image("bg backalley")
        #g.display("lighthouse_sketch.jpg")
        #g.allprior()

        # We can use g.page to introduce a second page.
        #g.page("Characters")

        #g.button("thumb_eileen.jpg")
        #
        # Note that we can give image and unlock image more than one image
        # at a time.
        #g.unlock_image("bg lighthouse day", "eileen day happy")
        #g.unlock_image("bg lighthouse day", "eileen day mad")



        # Another page, this one for concept art.
        #g.page("Concept Art")

        #g.button("thumb_concepts.jpg")
        #
        # We can apply conditions to buttons as well as to images.
        # The "condition" condition checks an arbitrary expression.
        #g.condition("persistent.beat_game")
        #
        #g.display("concept1.jpg")
        #g.display("concept2.jpg")
        #g.display("concept3.jpg")


        # Now, show the gallery.
        g.show()

    return

