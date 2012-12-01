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
    
    # Should autosave be enabled?
    config.has_autosave = False

    ## These control the width and height of the screen.

    config.screen_width = 1024
    config.screen_height = 768
    
    config.thumbnail_width = 105
    config.thumbnail_height = 75

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
    #style.default.color = "#604200"

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
    # style.default.font = "TimesNewRoman.ttf"
    style.default.size = 19
    style.default.color = "#622a00"
    
    # Font settings for the PDA: item/journal information and journal entry buttons
    style.pda = Style(style.default)
    style.pda.color = "#000605"
    style.pda.size = 36
    
    # Font settings for the minigame screen description.
    style.minigame_description = Style(style.default)
    style.minigame_description.color = "#000000"
    style.minigame_description.size = 18
    
    # Font settings for the UI message box.
    style.message = Style(style.default)
    style.message.color = "#622a00"
    style.message.size = 21
    
    # Font settings for the choice box.
    style.menu_choice.color = "#622a00"
    style.menu_choice.size = 24

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
    #config.help = "README.html"


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

init python:
    MINIGAME_MUSIC = "sfx/mitsumata_festival.ogg"
    BATTLE_MUSIC = "sfx/shop_theme.mp3"

    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persisten information can be found by the init code.)
python early:
    #config.save_directory = "MitsumataProgram-1313711868"
    config.save_directory = "saves/Mitsumata"

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

                         
## This section contains information about how to build your project into 
## distribution files.
#init python:
    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
#        build.directory_name = "mitsumata-dev-0.1"
    
    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
#        build.executable_name = "mitsumata-dev"
    
    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
#        build.include_update = False
    
    ## File patterns:
    ## 
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##    
    ##
    ## In a pattern:
    ##
    ## / 
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    #    build.classify('**~', None)
    #    build.classify('**.bak', None)
    #    build.classify('**/.**', None)
    #    build.classify('**/#**', None)
    #    build.classify('**/thumbs.db', None)
    #    build.classify('**.rpy', None)
    #    build.classify('**.txt', None)
    #    build.classify('**.psd', None)
    #    build.classify('**.xcf', None)
    #    build.classify('game/cache/', None)
    #    build.classify('game/gallery/', None)
    #    build.classify('game/gallery.*', None)
    
#        build.archive("gfx", "all")
#        build.archive("sfx", "all")
    
    # Demo specific ignores
    
    # Ignore everything but Riku & Mamoru battle sprites, and cells, squats, and
    # duck hunt minigames.
#        build.classify('game/gfx/battle/carniflora/', None)
#        build.classify('game/gfx/battle/demonic_hunter/', None)
#        build.classify('game/gfx/battle/demonic_thug/', None)
#        build.classify('game/gfx/battle/naomi/', None)
#        build.classify('game/gfx/battle/roman/', None)
#        build.classify('game/gfx/bottles/', None)
#        build.classify('game/gfx/buttons/minigame_bottles*', None)
#        build.classify('game/gfx/buttons/minigame_force*', None)
#        build.classify('game/gfx/buttons/minigame_garden*', None)
#        build.classify('game/gfx/buttons/minigame_gears*', None)
#        build.classify('game/gfx/buttons/minigame_lock*', None)
#        build.classify('game/gfx/buttons/minigame_platformer*', None)
#        build.classify('game/gfx/buttons/minigame_power*', None)
#       build.classify('game/gfx/garden/', None)
#        build.classify('game/gfx/gears/', None)
#        build.classify('game/gfx/lock/', None)
#        build.classify('game/gfx/magic_force/', None)
#        build.classify('game/gfx/magic_power/', None)
#        build.classify('game/gfx/map/', None)
#        build.classify('game/gfx/platformer/', None)
#       build.classify('game/gfx/whack_a_mole/', None)
#        build.classify('game/minigame_bottle*', None)
#       build.classify('game/minigame_force*', None)
#        build.classify('game/minigame_garden*', None)
#        build.classify('game/minigame_gears*', None)
#        build.classify('game/minigame_lock*', None)
#        build.classify('game/minigame_mole*', None)
#        build.classify('game/minigame_platformer*', None)
#        build.classify('game/minigame_power*', None)
#        build.classify('game/shop*', None)
    
    # Ignore everything but the knife, pda, and wallet
#        build.classify('game/gfx/items/a*', None)
#        build.classify('game/gfx/items/b*', None)
#        build.classify('game/gfx/items/c*', None)
#        build.classify('game/gfx/items/d*', None)
#        build.classify('game/gfx/items/e*', None)
#        build.classify('game/gfx/items/f*', None)
#        build.classify('game/gfx/items/g*', None)
#        build.classify('game/gfx/items/h*', None)
#        build.classify('game/gfx/items/i*', None)
#        build.classify('game/gfx/items/j*', None)
#        build.classify('game/gfx/items/key*', None)
#        build.classify('game/gfx/items/kimono*', None)
#        build.classify('game/gfx/items/l*', None)
#        build.classify('game/gfx/items/m*', None)
#        build.classify('game/gfx/items/parts*', None)
#        build.classify('game/gfx/items/phone*', None)
#        build.classify('game/gfx/items/pic*', None)
#        build.classify('game/gfx/items/pol*', None)
#        build.classify('game/gfx/items/r*', None)
#        build.classify('game/gfx/items/s*', None)
#        build.classify('game/gfx/items/t*', None)
#        build.classify('game/gfx/items/u*', None)
#        build.classify('game/gfx/items/v*', None)
    
    # Ignore everything but the few backgrounds used in the script.

#        build.classify('game/gfx/backgrounds/bath.png', None)
#        build.classify('game/gfx/backgrounds/DForest1.png', None)
#        build.classify('game/gfx/backgrounds/DForest2.png', None)
#        build.classify('game/gfx/backgrounds/DForest3.png', None)
#        build.classify('game/gfx/backgrounds/firstview.png', None)
#        build.classify('game/gfx/backgrounds/Garden1.png', None)
#        build.classify('game/gfx/backgrounds/Garden2.png', None)
#        build.classify('game/gfx/backgrounds/Hallway1.jpg', None)
#        build.classify('game/gfx/backgrounds/Hallway2.jpg', None)
#        build.classify('game/gfx/backgrounds/kazulie.png', None)
#        build.classify('game/gfx/backgrounds/Kitchen.jpg', None)
#        build.classify('game/gfx/backgrounds/ldead.png', None)
#        build.classify('game/gfx/backgrounds/Library.jpg', None)
#        build.classify('game/gfx/backgrounds/lizadead.png', None)
#        build.classify('game/gfx/backgrounds/lscamp.png', None)
#        build.classify('game/gfx/backgrounds/mall.png', None)
#        build.classify('game/gfx/backgrounds/manaroof.png', None)
#        build.classify('game/gfx/backgrounds/map.png', None)
#        build.classify('game/gfx/backgrounds/Nforest2.png', None)
#        build.classify('game/gfx/backgrounds/NForest1.png', None)
#        build.classify('game/gfx/backgrounds/NForest3.png', None)
#        build.classify('game/gfx/backgrounds/nightgrass.jpg', None)
#        build.classify('game/gfx/backgrounds/nightsky.jpg', None)
#        build.classify('game/gfx/backgrounds/noreat.png', None)
#        build.classify('game/gfx/backgrounds/rcrib.png', None)
#        build.classify('game/gfx/backgrounds/rikumom.png', None)
#        build.classify('game/gfx/backgrounds/Room1.png', None)
#        build.classify('game/gfx/backgrounds/Room2.png', None)
#        build.classify('game/gfx/backgrounds/Room3.png', None)
#        build.classify('game/gfx/backgrounds/Room4.png', None)
#        build.classify('game/gfx/backgrounds/rrplot.png', None)
#        build.classify('game/gfx/backgrounds/rsgarden.png', None)
#        build.classify('game/gfx/backgrounds/rvfood.png', None)
#        build.classify('game/gfx/backgrounds/scaryouko.png', None)
#        build.classify('game/gfx/backgrounds/shop.png', None)
#        build.classify('game/gfx/backgrounds/slkid.png', None)
#        build.classify('game/gfx/backgrounds/soumeheal.png', None)
#        build.classify('game/gfx/backgrounds/souplant.png', None)
#        build.classify('game/gfx/backgrounds/susahit.jpg', None)
#        build.classify('game/gfx/backgrounds/templebottom.png', None)
#       build.classify('game/gfx/backgrounds/templetop.png', None)
#        build.classify('game/gfx/backgrounds/templewhole.png', None)
#        build.classify('game/gfx/backgrounds/train1.png', None)
#        build.classify('game/gfx/backgrounds/train2.png', None)
#        build.classify('game/gfx/backgrounds/trainwhole.png', None)

    # Ignore everything but the few sprites used in the script.
#        build.classify('game/gfx/Sprites/ka*', None)
#        build.classify('game/gfx/Sprites/l*', None)
#        build.classify('game/gfx/Sprites/n*', None)
#        build.classify('game/gfx/Sprites/ro*', None)
#        build.classify('game/gfx/Sprites/s*', None)
#        build.classify('game/gfx/Sprites/you*', None)

    # Ignore everything but the few sound files used in the script.
#        build.classify('game/sfx/Battle*', None)
#        build.classify('game/sfx/Game*', None)
#        build.classify('game/sfx/Happy*', None)
#        build.classify('game/sfx/mitsumata_bgm05*', None)
#        build.classify('game/sfx/mitsumata_bgm06*', None)
#        build.classify('game/sfx/MITSUMATA_ED*', None)
#        build.classify('game/sfx/mitsumata_festival*', None)
#        build.classify('game/sfx/mitsumata_mamorus*', None)
#        build.classify('game/sfx/mitsumata_OPb*', None)
#        build.classify('game/sfx/mitsumata_piano*', None)
#        build.classify('game/sfx/mitsumata_romans*', None)
#        build.classify('game/sfx/mitsumata_soumes*', None)
#        build.classify('game/sfx/mitsumata_susas*', None)

    ## To archive files, classify them as 'archive'.
    
    #build.classify('**.png', 'gfx')
    #build.classify('**.jpg', 'gfx')
    #build.classify('**.mp3', 'sfx')
    #build.classify('**.ogg', 'sfx')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

#        build.documentation('*.html')
#        build.documentation('*.txt')
    
