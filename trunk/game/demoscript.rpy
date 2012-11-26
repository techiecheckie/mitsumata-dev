init: 
  #*******************************
  # EFFECT COMMANDS
  #*******************************
  $ slow_dissolve = Dissolve(3.0)
  $ slow_fade = Fade(2, 2, 3)
  $ flash = Fade(0.1, 0.0, 0.5, color="#fff")
   
  # The two pan commands do the following.
  # Panltr pans the screen from left to right 1600 pixels, taking 10 seconds to do so.
  # Panutd pans the screen from up to down 1600 pixels, taking 10 seconds to do so.
  # The $renpy.pause() command MUST be used to delay other programming while panning is going on.
  # There must always be a full screen's worth of pixels during the pan or it will cause a problem
  #  with rendering.
  $ panltr = Pan((0, 0), (1600, 0), 10.0)
  $ panutd = Pan((0,1600), (0, 0), 10.0)

  # The below all take with commands.   
  # For example, in "wiperight", a wipe from left to right, first the left edge of the image is 
  # revealed at the left edge of the screen, then the center of the image, and finally the 
  # right side of the image at the right of the screen.   
  $ wiperight = CropMove(1.0, "wiperight")
  $ wipeleft = CropMove(1.0, "wipeleft")
  $ wipeup = CropMove(1.0, "wipeup")
  $ wipedown = CropMove(1.0, "wipedown")

  # In a "slideright", the right edge of the image starts at the left edge of the screen, 
  # and moves to the right as the transition progresses.   
  $ slideright = CropMove(1.0, "slideright")
  $ slideleft = CropMove(1.0, "slideleft")
  $ slideup = CropMove(1.0, "slideup")
  $ slidedown = CropMove(1.0, "slidedown")

  # There are also slideaways, in which the old image moves on top of the new image.   
  $ slideawayright = CropMove(1.0, "slideawayright")
  $ slideawayleft = CropMove(1.0, "slideawayleft")
  $ slideawayup = CropMove(1.0, "slideawayup")
  $ slideawaydown = CropMove(1.0, "slideawaydown")

  $ irisout = CropMove(1.0, "irisout")
  $ irisin = CropMove(1.0, "irisin")

  $ noise_dissolve = ImageDissolve(im.Tile("gfx/effects/noisetile.png"), 2.0, 1)

  #Shaky uses the at command    
  $ shaky = Shake((0, 0, 0, 0), 2.5, dist=20)

  #Shorter dissolve command for teleport
  $ sho_dis = Dissolve(0.2)
  
  #Teleport uses the with command    
  #$ teleport = MultipleTransition([False, sho_dis, "#fff", sho_dis, False, sho_dis, "#fff", sho_dis,
  #                                     True, sho_dis, "#fff", sho_dis, True])
  
  image snow = Snow("gfx/effects/snowflake.png")

  
#label music_room:
#    scene black
#    python:
#        _game_menu_screen = None
#        # The default track of music.
#        playing = "11-Yesterday.ogg"
        
#label music_room_loop:
#    # Play the playing music, if it changed.
#    python:
#        renpy.music.play(playing, if_changed=True, fadeout=1)
#
#        # Display the various music buttons.
#        ui.vbox(xalign=0.5, ypos=100)
#        music_button("Yesterday", "11-Yesterday.ogg")
#        music_button("Yellow Submarine", "15-Yellow_Submarine.ogg")
#        music_button("Hey Jude", "21-Hey_Jude.ogg")
#        ui.close()
#
#        # This is how we return to the main menu.
#        ui.textbutton(
#            "Return",
#            clicked=ui.returns(False),
#            xalign=0.5,
#            ypos=450,
#            size_group="music")
#
#    if ui.interact():
#        jump music_room_loop
#    else:
#        return



#----------------------------------
# DECLARE BG IMAGES
#----------------------------------
# eg. image eileen happy = "eileen_happy.png"
#image bg bar = ""
#image bg barcg = ""
#image bg bath = ""
#image bg firstview = ""
#image bg mameat1 = ""
#image bg mameat2 = ""
#image bg maminpain = ""
#image bg mamview = ""
#image bg rikureading = ""
#image bg rikuyouth = ""
#image bg shrfr = ""
#image bg soumeheal = ""
#image bg soupowers = ""
#image bg souwithplants = ""
#image bg suhit = ""
#image bg traingr1 = ""
#image bg traingr2 = ""
#image bg train1 = ""
#image bg train2 = ""

image bg backalley = "gfx/backgrounds/streetalley2.png"
#image bg hall1 = "gfx/backgrounds/Hallway1.jpg"
#image bg hall2 = "gfx/backgrounds/Hallway2.jpg"
#image bg riroom = "gfx/backgrounds/room1.png"
#image bg roroom = "gfx/backgrounds/room2.png"
#image bg soroom = "gfx/backgrounds/room3.png"
#image bg suroom = "gfx/backgrounds/room4.png"
#image bg library = "gfx/backgrounds/library.jpg"
#image bg dfor1 = "gfx/backgrounds/dforest1.png"
#image bg dfor2 = "gfx/backgrounds/dforest2.png"
#image bg dfor3 = "gfx/backgrounds/dforest3.png"
#image bg nfor1 = "gfx/backgrounds/nforest1.png"
#image bg nfor2 = "gfx/backgrounds/nforest2.png"
#image bg nfor3 = "gfx/backgrounds/nforest3.png"
#image bg kitchen = "gfx/backgrounds/kitchen.jpg"
#image bg gar1 = "gfx/backgrounds/garden1.png"
#image bg gar2 = "gfx/backgrounds/garden2.png"
image bg street = "gfx/backgrounds/streetalley1.png"
#image bg store = "gfx/backgrounds/store.png"
#image bg ngro = "gfx/backgrounds/nightgrass.jpg"
#image bg nsky = "gfx/backgrounds/nightsky.jpg"
#image bg dgro = "gfx/backgrounds/daygrass.jpg"
#image bg dsky = "gfx/backgrounds/daysky.jpg"
#image bg shrfr = "gfx/backgrounds/templetop.png"
#image bg shrbot = "gfx/backgrounds/templebottom.png"
#image bg train1 = "gfx/backgrounds/train1.png"
#image bg train2 = "gfx/backgrounds/train2.png"
#image bg trainwhole = "gfx/backgrounds/trainwhole.png"

image bg blackscr = "gfx/backgrounds/blackscr.png"
image bg redscr = "gfx/backgrounds/redscr.jpg"
image bg whitescr = "gfx/backgrounds/whitescr.jpg"

#image map = "gfx/backgrounds/map.png"
image textbox_l = "gfx/textbox.png"
image textbox_m = "gfx/textbox_2.png"
image textbox_s = "gfx/textbox_mini.png"
image pda_button = "gfx/buttons/button_palm_pilot_hover.png"

#--------------------------------
#DECLARE CG IMAGES
#--------------------------------
image bg dream = "gfx/backgrounds/dream.jpg"
image bg dungeon = "gfx/backgrounds/dungeon.png"
#image bg bath = "gfx/backgrounds/bath.png"
#image bg firstview = "gfx/backgrounds/firstview.png"
#image bg kazulie = "gfx/backgrounds/kazulie.png"
#image bg ldead = "gfx/backgrounds/ldead.png"
#image bg lscamp = "gfx/backgrounds/lscamp.png"
#image bg mall = "gfx/backgrounds/mall.png"
image bg mameat = "gfx/backgrounds/mamdeadbody.png"
#image bg mnroof = "gfx/backgrounds/manaroof.png"
#image bg noreat = "gfx/backgrounds/noreat.png"
#image bg rcrib = "gfx/backgrounds/rcrib.png"
image bg rikubar = "gfx/backgrounds/rikubar.png"
#image bg rikumom = "gfx/backgrounds/rikumom.png"
#image bg rrplot = "gfx/backgrounds/rrplot.png"
#image bg rsgarden = "gfx/backgrounds/rsgarden.png"
#image bg run = "gfx/backgrounds/run.png"
#image bg rvfood = "gfx/backgrounds/rvfood.png"
#image bg scaryou = "gfx/backgrounds/scaryouko.png"
#image bg slkid = "gfx/backgrounds/slkid.png"
#image bg souheal = "gfx/backgrounds/soumeheal.png"
#image bg souplant = "gfx/backgrounds/souplant.png"
#image bg suhit = "gfx/backgrounds/susahit.png"


#-----------------------------------------------
#DECLARE RIKU SPRITE IMAGES
#-----------------------------------------------
image r flush = "gfx/sprites/rflush.png"
image r smirk = "gfx/sprites/rsmirk.png"
image r think = "gfx/sprites/rthink.png"
#image r fight = ""
image r grin = "gfx/sprites/rdkgrin.png"
image r happy = "gfx/sprites/rhappy.png"
image r mad = "gfx/sprites/rmad.png"
image r neu = "gfx/sprites/rneu.png"
image r sad = "gfx/sprites/rhurt.png"
image r scare = "gfx/sprites/rscared.png"
image r nerve = "gfx/sprites/rnerve.png"
image r no = "gfx/sprites/rno.png"

#---------------------------------------------------
#DECLARE ROMAN SPRITE IMAGES
#---------------------------------------------------
#image ro happy = "gfx/sprites/rohappy.png"
#image ro sad = "gfx/sprites/rosad.png"
#image ro scare = ""
#image ro fight = ""
#image ro blush = ""
#image ro worry = "gfx/sprites/roworried.png"
#image ro neu = "gfx/sprites/roneutral.png"
#image ro pout = "gfx/sprites/ropout.png"
#image ro surp = ""
#image ro frown = ""
#image ro smile = ""
#image ro sweat = ""
#image ro flush = ""

#------------------------------------------------
#DECLARE SUSA SPRITE IMAGES
#------------------------------------------------
#image su mad = "gfx/sprites/sutch.png"
#image su neu = "gfx/sprites/suneu.png"
#image su scare = "gfx/sprites/suflip.png"
#image su smirk = "gfx/sprites/susmirk.png"
#image su grin = "gfx/sprites/suamuse.png"
#image su dub = "gfx/sprites/suohrly.png"
#image su irk = "gfx/sprites/suannoy.png"

#---------------------------------------------------
#DECLARE SOUME SPRITE IMAGES
#---------------------------------------------------
#image s neu = "gfx/sprites/sneu.png"
#image s upset = "gfx/sprites/supset.png"
#image s smile = "gfx/sprites/sbigsm.png"
#image s think = "gfx/sprites/sthought.png"
#image s mad = "gfx/sprites/spissed.png"
#image s sadsm = "gfx/sprites/ssadsm.png"
#image s nerv = "gfx/sprites/snerve.png"
#image s ohmy = "gfx/sprites/sohmy.png"
#image s distr = "gfx/sprites/sdistractedo.png"
#image s blank = "gfx/sprites/sblanko.png"
#image s sad = "gfx/sprites/sdepress.png"
#image s pens = "gfx/sprites/spensive.png"
#image s gigg ="gfx/sprites/stitter.png"
#image s shock = "gfx/sprites/sshock.png"
#image you grin = "gfx/sprites/youdkgrin.png"
#image you piss = "gfx/sprites/youpissed.png"
#image you sm = "gfx/sprites/yousm.png"
#image you flirt = "gfx/sprites/youflirt.png"
#image you misch = "gfx/sprites/youmis.png"
#image you neu = "gfx/sprites/youneu.png"
#image you bore = "gfx/sprites/youbored.png"
#image so grin = ""
#image so frown = ""

#----------------------------------------------
#DECLARE LIZA SPRITE IMAGES
#----------------------------------------------
#image l neu = "gfx/sprites/lneu.png"
#image l upset = "gfx/sprites/lpissy.png"
#image l frown = "gfx/sprites/lsmirk.png"
#image l smirk = ""
#image l shock = "gfx/sprites/lshock.png"

#-----------------------------------------------------
#DECLARE MAMORU SPRITE IMAGES
#-----------------------------------------------------
#image m neu = ""
image m grin = "gfx/sprites/magrin.png"
#image m mad = ""
#image m fight = ""
#image m gentle = ""
image m unhappy = "gfx/sprites/mathink.png"

#-------------------------------------------------------
#DECLARE KAZUTAKA SPRITE IMAGES
#-------------------------------------------------------
#image k neu = "gfx/sprites/kazno.png"
#image k think = "gfx/sprites/kazthink.png"
#image k freak = "gfx/sprites/kazscare.png"
#image k frown = "gfx/sprites/kazuh.png"
#image k smirk = "gfx/sprites/kazsmirk.png"
#image k grin = "gfx/sprites/kazdkgrin.png"

#--------------------------------------------------
#DECLARE NORAH SPRITE IMAGES
#--------------------------------------------------
#image n neutral = "gfx/sprites/nneu.png"
#image n grin = "gfx/sprites/nsmirk.png"

#----------------------------------------------------------------
#DECLARE DEMON HUNTER SPRITE IMAGES
#----------------------------------------------------------------
image dg neu = "gfx/sprites/dgneu.png"
image dg grin = "gfx/sprites/dgsmirk.png"
image db neu = "gfx/sprites/dbneu.png"
#image db grin = "gfx/sprites/hunterboy_smile.png"

#-----------------------------------------------------
#DECLARE STUDENT SPRITE IMAGES
#-----------------------------------------------------
image st gneu = "gfx/sprites/girstuneu.png"
image st gwor = "gfx/sprites/girstuwor.png"
image st bneu = "gfx/sprites/boystuneu.png"
image st bmad = "gfx/sprites/boystumad.png"

#------------------------------------------------
#DECLARE MAJIN SPRITE IMAGES
#------------------------------------------------
#image rg neu = ""
#image rg scare = ""
#image rb neu = "gfx/sprites/sgneu.png"
#image rb scare = "gfx/sprites/sgsmile.png"

#-----------------------------------------------
#DECLARE MISC SPRITE IMAGES
#-----------------------------------------------
#image p = ""
#image u = ""
#image pa = ""
#image ma = ""


#-----------------------------------
#DECLARE GAME CHARS
#-----------------------------------
        
define su = Character('Susa', show_two_window=False)
define r = Character('Riku', show_two_window=False)
define ro = Character('Roman', show_two_window=False )
define s = Character('Soume', show_two_window=False )
define l = Character('Liza', show_two_window=False)
define m = Character('Mamoru', show_two_window=False)
define k = Character('Doctor Osamu', show_two_window=False)
define n = Character('Norah', show_two_window=False)
define u =Character('Unknown',  show_two_window=False)
define dg = Character('Demon Hunter 1', show_two_window=False)
define db = Character('Demon Hunter 2', show_two_window=False)
define sg = Character('Student 1', show_two_window=False)
define sb = Character('Student 2', show_two_window=False)
define rg = Character('Majin 1', show_two_window=False)
define rb = Character('Majin 2', show_two_window=False)
define p = Character('Plant', show_two_window=False)
define pr = Character('Prisoner 1', show_two_window=False)
define pri = Character('Prisoner 2', show_two_window=False)
define ma = Character('Man', show_two_window=False)
define wo = Character('Woman',  show_two_window=False)
define boy = Character('Boy', show_two_window=False)
define gir = Character('Girl', show_two_window=False)
define se = Character('Servant', show_two_window=False)
define ma = Character('Mom',  show_two_window=False)
define pa = Character('Dad', show_two_window=False)
define ob = Character('Older Boy 1', show_two_window=False )
define ob1 = Character('Older Boy 2', show_two_window=False)
define a = Character('Audra', show_two_window=False )
define na = Character('Naomi', show_two_window=False )
define ak = Character('Akiko', show_two_window=False)
define cl = Character ('Clerk', show_two_window=False)
define ev = Character ('Everyone', show_two_window=False)

#*****************************************
# DYNAMIC CHARACTER NAMING
#*****************************************
#init:
#    $ m = DynamicCharacter ("Mamoru")
#    $ s = DynamicCharacter ("Soume")
#    $ ro = DynamicCharacter ("Roman")
#    $ n = DynamicCharacter ("Norah")
#    $ k = DynamicCharacter ("Kazu")
#    $ a = DynamicCharacter ("Audra")
#    $ na = DynamicCharacter ("Naomi")


    # Set "maid_name" to mean something early on in the game.
    # You don't have to use it right away.
    # $ maid_name = "Maid"
    # ''now'' the variable "maid_name" exists - it's only created when you set it.

    # millie "I hope you'll be comfortable here."
    # millie "We always do our best to make our guests comfortable."
    # millie "If you need anything, just ask for \"Millie\" - that's me."
    # $ maid_name = "Millie"
    # millie "The bell boy's just bringing your suitcases now."


#***********************
# SPLASH SCREEN
#***********************
# The splashscreen is called, if it exists, before the main menu is
# shown the first time. It is not called if the game has restarted.
# We'll comment it out for now.
#
#label splashscreen1:
#    if not persistent.chose_lang:
#        $ persistent.chose_lang = True
#        jump language_chooser
#    return

label splashscreen:
    #$ renpy.pause(0)
    #scene bg whitescr
    #show text "rosegold games presents..." with dissolve
    #$ renpy.pause(5.0)
    #hide text with dissolve
    #show text "Mitsumata: The First Act" with dissolve
    #$ renpy.pause(5.0)
    #hide text with dissolve
    #show text "Part I" with dissolve
    #$ renpy.pause(1.0)
    #hide text with dissolve

    return

#***********************
# ITEM LABELS
#***********************
# This unlocks an item.
#   $unlock_item("id", True|False), True to display a message, False to not.
#
# This locks it again.
#   $lock_item("id", True|False), the boolean has no effect here yet, because the
#   message part hasn't been implemented yet (if ever). It can be done if necessary.
#
# This checks to see if an item is unlocked.
#   inventory.item_unlocked("id"), returns True is unlocked, else False.
#
#   A shorter version of this has been added to init.rpy:
#   item_unlocked("id")

#--------------------------------
# GAME STARTS HURR
#--------------------------------
label start:
    $hide_main_ui()

    menu:
        "Jump to Scene 1 to test the characters":
                jump Scene1
        "Test PDA functions.":
                jump pdatest
    
label Scene1:  
        play music "sfx/mitsumata_bgm01.ogg" 
        #scene bg mameat1
        scene bg dungeon 
        $show_main_ui()
        with slow_dissolve
        
        $ renpy.pause(3.0)
        
        "It's so dark in here. No windows, no sunlight. Smells musty and wet. Wherever this is, it's probably far underground."

        "That’s smart. Wouldn’t expect any less from these kidnappers."

        "I can't see too far out of my own cell; it’s nearly pitch black in here. I can see pretty well in low lights, but I can only catch a glint of the glassy eyes of the guy in the other cell."

        "Reminds me of donuts, the glazed kind. I don’t know much about this world and I haven’t been here that long, but discovering donuts was worth the confusion."

        pr "Ohhh, I wish I had a glazed donut."

        pri "You’re a long way from that stuff, brother."

        #play laughter sound
        "The babbling amongst the other cells breaks for some cracked, hoarse laughter."

        "Always keep them laughing, eh?"

        #play footsteps
        "I hear footsteps, coming closer. The room becomes dead silent."

        "That can't be good."

        se "It’s all right, young master. Step carefully."

        wo "And hurry along now."

        boy "Papa said this was okay?"

        gir "Less talking, more walking, please! I have training to get to."

        boy "Shut up. If I did everything just cause you said, I'd be in trouble all the time like you."

        gir "You wanna get strangled, brat?"

        wo "Now now. Be kind to your little brother."

        # Girl growls, angry.
        gir "Grr."

        # play sound Footsteps.

        boy "Are you sure this is okay?"

        se "Of course. Your father gave us special permission, and we acquired him just for you."

        "'Acquired him'? I don’t know what that means, but there’s a suddenly sickening smell in the air. The sound stops in front of my cell, and very vivid green eyes peer in."

        "Is that...?"

        #show bg mameat2
        #eye-light flicker animation?
        "The thick metal door opens, and a little boy walks in, looking at me with large, shiny light brown eyes."
 
        #play sound doorcreak
        boy "Hi."

        "I give him a look. I really hate the weird lingo here, but these people don't understand any logical language." 
        "Every other person is speaking some new gibberish, instead of the normal set of three"
        "What's the point of having like 100 different languages? Nobody can't understand nobody else!"
        "Doesn’t make any damn sense, but these meatsacks got tiny brains and won’t have any clue what you’re sayin’ otherwise."

        pr "...uh, hey."

        "He gets closer, kneels at my feet and touches my ankle. I kick his hand off. Weird little fuck. Real warm hands. It actually makes all the hair on the back of my neck stand."

        boy "If you stay still, it'll hurt a lot less."

        pr "Oh, really. You're going to hurt me."

        "Kids. No respect these days, not even back home."

        gir "Smells like piss in here."

        #boy scoffs.

        se "Please don't rush your brother's dinner, little mistress."

        gir "Some of us have lives and don't want to spend all evening watching someone ELSE eat."

        "It’s like a scene out of a fucked-up play. One I probably woulda gone to see if I weren’t the main fucking attraction."

        "I lift a fist to teach the kid a lesson. He’s slow; you could see it in his muscles."

        $ hide_main_ui()
        show bg redscr 
        with dissolve
        $ renpy.pause(2.0)
        $ show_main_ui()
        pr "Aack! My arm---"
        
        "The vivid eyes I’d been looking at hover above me, and suddenly my arm is on fire! Broken! Nearly torn out of the socket and bleeding all over."

        pr "Aghh--why...are you...with--"

        se "Please do attempt to refrain from attacking the little master."

        pr "No...spare me...I don’t want to---"

        boy "Think of this as fate. That sounds kind of nice, doesn’t it?"
        $hide_main_ui()
        show bg mameat
        play music "sfx/sad_theme.mp3" fadeout 2.0
        $ renpy.pause (5.0)
        scene bg blackscr 
        with slow_dissolve
        # play sound Screaming, crunching, grinding, all sorts of unholy noises.
        $ renpy.pause(3.0)
        #show some kind of splash page here
        stop music
        
label Scene2:
        scene bg street
        $show_main_ui()
        with slow_fade
        $ renpy.pause(1.0)

        show st gneu at right with dissolve

        sg "Riku." 
        
        $ renpy.pause(1.0)
        
        show bg street at shaky with dissolve
        sg "...HEY, Riku, wake the hell up!"
        #shake effect here
        play music "sfx/mitsumata_rikus_theme.mp3" fadeout 1.0
        
        show r think at left:
            alpha 0.0
            time 0.75
            linear 1.0 alpha 1.0
        with dissolve
        r "Huh? Oh."
        show r neu at left
        with dissolve
        "If you haven't figured it out yet, I'm Riku. Midorikawa Riku, age 17, third year in high school."
        "I don't believe in silly crap like blood-type personalities, and even if I did, I dunno mine. I don't believe in horoscopes, either. Superstition is for kids."

        show st bneu at right
        with dissolve
        sb "You've been out of it lately, man...you okay?"
        show r think at left
        with dissolve
        r "Yeah, just thinkin' too hard on school starting again, I guess."

        sb "Pff, yeah. No more free time at all. Even school breaks are gonna get eaten by studying."

        show st gneu at right with dissolve
        sg "Don't remind me of the college exams! I'm so nervous about getting into Toudai. What if I don't get in? How am I going to tell my parents?" 
        show st gwor at right with dissolve
        sg "{size=17}What if I don't make it into Keio either, and I have to go to CRAM SCHOOL for a year before I can reapply? And then what if I fail AGAIN and my parents disown me for being so stupid?! I can't HANDLE THIS---{/size}"

        $renpy.pause(1.0)
        show st gneu at right 
        show r no at left
        with dissolve
        "What else do you expect 17 year olds to talk about?"
        "This year in high school is the worst. Once the second half of the year rolls around, no more free time, no more club activities, no more sports---no more fun, period. College exams will own our lives." 
        "Our high school has a pretty good reputation for getting kids into top-level schools, and they're hard-asses about that reputation."
        "Whatever. Bores the shit out of me."
        show r grin at left with dissolve
        r "Heh. I heard that this one time, when the school’s practice grades weren't high enough, the principal expelled a bunch of people to raise the marks."

        show st gwor at right with dissolve
        sg "Oh god, you're joking. Tell me you're joking."

        "I am, but she doesn't need to know that."

        show st bmad at right with dissolve
        sb "Riku, don't be a jerk. Not everyone can fly by on sports scholarships like you."
        show r nerve at left with dissolve
        r "Hey now, don't make it more than it is."

        show st gneu at right with dissolve
        sg "What are you talking about? You’ve got automatic entry no matter how bad you do!"

        r "Yeah, yeah, maybe, but I'm not going to get into any top schools on just sports, and my grades aren't exactly amazing."

        sg "That's because you cut class to go drinking!"
        show r grin at left with dissolve
        r "A man's gotta have priorities!"

        "{size=17}I guess it’s true. I don't have to worry much about grades since I'm kind of a sports legend around here, and even if our school did kick crappy third years out every exam time, I'd get to stay, cause, well...{/size}"

        show st bneu at right with dissolve
        sb "Now that I think about it, Riku, you never told us what you got on the first practice exam."
        show r nerve at left with dissolve
        r "Pfft. Who cares. It was like the bottom quarter."
        show st gwor at right with dissolve
        "Everyone winces. People with grades that low had better have a hook-up somewhere."
        "Yuck. I don't even want to think about...jobs." 
        "Having to sign my soul away to some company?" 
        "I'd rather stay in high school and deal with shithead teachers for the next 10 years."

        "'Sides, I wasn’t exactly in the bottom quarter anyway." 
        "Not that I studied; I just have a good memory is all. Helps on tests."

        show st gneu at right with dissolve
        sg "Well, serves you right for cutting and refusing to study. That’s okay. When I’m a doctor, you can always be my personal cleaning boy."

        #play sound Laughter.
        show r no at left with dissolve
        #Riku grumbles to himself.
        r "Grr."

        sg "Don't make a sad face, Riku. I could always tutor you, if you're serious...but I'm talking hardcore, three-hour-a-day study sessions, and eight hours on weekends--"

        show st bneu at right with dissolve
        sb "How the hell's he supposed to play if he's studying that much?"

        show st gneu at right with dissolve
        sg "Well, obviously he'll have to sacrifice sports! This is his future!"

        "My watch beeps."
        #play sound beep
        show r flush at left with dissolve
        r "...shit."
        
        show st bneu at right with dissolve
        sb "Aw, you gotta head home?"
        show r neu at left with dissolve
        "I grab my bag and stand, yawning. Just one more day of vacation left, and then it's 48 hours a week of the worst school hell ever."
        "Fuuuuuck. The principal might as well just castrate me now and get it over with."

        "Who in their right mind can even sit for that long, anyway? I got ADD just thinking about it."

        r "Yeah, it's gettin' dark, and I set my watch to tell me when I’m an hour late. Actually, I expect---"
        #play sound Ring ring ring.
        $ renpy.pause(2.0)
        
        r "--my parents to be calling. Yello? Right right, I know; I'm coming. I'm coming!"

        "Those people barking loudly into the phone? My parents. People say I’m lucky, adopted into a rich family of doctors, but they don’t have to live with ‘em."

        show r no at left with dissolve
        r "No, I get it---"
        
        r "Awww, not the TV..."

        #play sound Mumbled speaking.

        r "I was already on my way home! Honest! I'm like a minute away!"
        show r neu at left with dissolve

        "I wave quickly to my friends, mouthing a good-bye. Ugh. No other seventeen year old in the universe has to be home this early. So fucking unfair."
        
label Scene3:
        #---Flashback---
        play music "sfx/comical.mp3" fadeout 1.0
        scene bg blackscr with fade
        
        #scene bg rikuyouth
        $show_main_ui()
        with slow_dissolve

        $ renpy.pause(2.0)
        r "How come I can't do sports this year? I'm good at them, the teacher SAYS!"

        pa "You're not ready to handle the responsibilities that come with being on a sports team."

        ma "Your grades aren't that great, you get into a lot of fights—we need to think about your safety."

        r "The fights aren't even my fault! Everyone picks on me cause I'm small! I'm not going to just LET them beat me up!"

        ma "Riku. We understand that this is upsetting, but you need to understand our point of view." 
        ma "You're a very strong boy, and sometimes you get out of hand, especially when you’re fired up."

        r "That was an ACCIDENT! I had no IDEA spleens could just 'SPLODE like that if you hit 'em too hard!"

        pa "Which is why you will wait until you are older and more aware of that fact."

        r "But---"

        pa "The answer is no, Riku. That’s it. Don’t bring it up again."

        ma "You can play whatever you'd like in your second year of junior high."

        #Riku: Makes a loud noise of child-like rage.
        r "ARAAAAAAAAAAAGHAFLDSK!"
        #Shaking screen effect goes here.
        # play sound Sound of shit breaking all over the house.

        #Mom sighs.
        ma "…Oh, Riku."

        pa "This time he’s paying for that out of his allowance."
       
# --------

label Scene4:
        play music "sfx/shop_theme.mp3" fadeout 1.0
        scene bg blackscr
        
        scene bg street 
        show r think with dissolve
        $show_main_ui()
        with dissolve
        
        "My parents didn't let me have a new door for three whole months cause of that."

        "I do have to be careful, though. Friendly punches can turn into broken arms when I’m the one doing the punching."

        "I make it back to my street pretty fast, running full speed from the beach. My parents won't get on my ass too much for it. They'll actually believe that I was close to home."

        play music "sfx/mitsumata_bgm04.ogg" fadeout 1.5
        r "Mm. Kind of cold for spring..."
        #play sound wind
        show r no with dissolve
        "Someone's following me. They're being unnaturally discreet about it, too...usually the idiots who want to—well, try to—pick on me don't make much of a show of hiding very well." 
        "Guess they figure it'd be like hiding from the fishbowl when you're trying to catch one of the fish."

        "Heh. My stalkers getting smarter? That'll be the day. Still, if I start a fight at this time of evening on my own street, my parents will flip a nut."
        
        #play sound Door unlocking.
        #put some kind of door opening effect here to lead into bg rhouse
        show bg blackscr with dissolve
        play music "sfx/Library.mp3" fadeout 2.0
        show r neu with dissolve
        r "I’m home."

        pa "Riku—in here, please."
        show r upset with dissolve
        #show r upset with dissolve
        "Aw fuck."

        r "Yeah, Pop?"

        # show pa
        pa "Do you understand why we give you a curfew?"
        show r no with dissolve
        r "Yeah, Pop."

        "There's no point arguing about it anymore. They set it when I was like six and have never looked back."

        pa "And why is that?"

        r "Night is when the rapists and murderers come out."

        pa "Riku."
        show r nerve with dissolve
        #Riku makes a nasty, rude, scoffing sound.
        r "...More violent crimes happen at night."

        pa "Exactly. And?"

        r "You want me to be safe."

        pa "And we want you to be able to handle the tiny responsibilities we give you. How can we let you dorm at college if you can't even get home at a reasonable hour?"

        r "Sorry, Pop."

        "It's a damn form letter by this point."

        pa "{size=17}One day, when I get you a job at the company, you're going to see the benefits of going to bed early and waking up early. Life isn't all about friends, Riku. You’ll have a wife and children who rely on you.{/size}"
        show r no with dissolve
        r "Sorry again, Pop. Am I free to go?"

        "He sighs, but that means I'm free."

        "I hate his lectures, even when they're short. Nothing outright depresses me more than thinking of having to take up a desk job. My dad doesn't even care about what I wanna do."

        "I don't get no respect around here. No respect at all."
        
        
label flashback:
    play music "sfx/mitsumata_musicbox.ogg" fadeout 2.0
    scene bg blackscr with fade
    show bg dream with slow_dissolve
    #put some kind of wispy cloudy effect here
    $show_main_ui()
    with dissolve
    
    "She's there, again, in my dreams."
    #play sound wind
    "Who are you?"
    "Why can't I stop seeing you?"
    "And why the fuck won't you let me get a good night's rest?"
    "Can dream ghosts even hear?"
    "If I squint, I can almost see her face properly."
    "Come closer."
    "My hand looks weird."
    "She's right there. I can almost..."
    $ renpy.pause(2.0)
    #stronger wispy cloud/blur effect?
    #Riku screams.
    "No-- where--"
   
label Scene5: 
    scene bg blackscr with fade
    #play sound Clock alarm
    #time 3.0
    #stop sound
    
    $show_main_ui()
    with slow_dissolve
    
    #Shaking screen effect here
    r "AAAAAAAAAAAAAAAAAAAAAGH!"
    
    "My hand goes out and smashes the alarm clock to bits. Literal bits—it’s scrap metal now. Serves the fucking thing right for scaring the shit out of me."
    
    "I check my watch. Eleven in the AM. Barely slept and woke up late at the same time. Fuckin' great day this is gonna be."
    
    #play sound Ring ring ring
    
    r "Yello?"
    
    boy "Riku, hurry up and get down to you-know-where. We just bet some guys 10,000 yen that you can outdrink them."
    
    r "And I get mosta of that for my trouble, yeah? Plus, you pay for the drinks."
    
    boy "C'mon, s'not like you need it..."
    
    r "I like to think of it as a part-time job."
    
    boy "Fine, fine! Hurry up!"
    
    "Can't say anything bad about a day that’s got free money waiting for me. I throw on some clothes and take off."
    
    "Alcohol’s just what I need."
    
    show bg street with dissolve
    play music "sfx/shop_theme.mp3"
    $ renpy.pause (1.5)
    
    "I like this place, for a few reasons. One, it’s always got idiots willing to make a bet with me, and two, it’s off the main road, so there aren’t any annoying people nagging at me for underage drinking."
    
    "I wave to my friends. They’re crowded around a table with some large guys, shot glasses already set up."
    
    ob "I thought this guy was supposed to be 17!"
    
    ob1 "Dudn't look older than 12 to me."
    
    ob "Maybe 12 and a half, if he's lucky!"
    
    "This might sound weird coming from a jock, but I fucking hate muscleheads like these guys. They’re always flapping their gums cause I’m a tiny bit smaller than them."
    
    "Whatever. It always ends up the same for them."
    
    "I take a seat and order a burger, rare. The food here's not great, but there's only so many ways you can do a rare burger wrong, mostly by actually trying to cook it."
    
    show r grin with dissolve
    r "Are you here for laughs, or to lose a bet? If you're not a bunch of princesses, why don't we go straight for the good stuff? Onigoroshi sound good?"
    
    "{size=17}Onigoroshi is practically like drinking rubbing alcohol. They don't call it “the demon killer” for nothing; you make it through a few shots and that shit'll put hair on your chest or make your nuts drop, or some other manly shit.{/size}"
    
    "Hasn't worked for me yet."
    
    ob "Why don’t we just get you some milk and call it a day?"
    
    "Ha ha ha. I totally haven’t heard that one before. The big fucking assholes are high-fiving each other like they fucking won a Pulitzer for that cheap line."
    
    "Taking their money will be a pleasure."
    hide r grin with dissolve
    $hide_main_ui()
    show bg rikubar with dissolve
    $ renpy.pause(1.5)
    $show_main_ui()
    with dissolve
    
    "My sake comes and I pour myself three glasses, setting the bottle down next to my dumbfuck opponent."
    
    r "How about we raise the stakes? Fifty-thousand yen."
    
    ob1 "Do you even have that kind of money, kiddo?"
    
    "I pluck five crisp 10,000 yen bills from my pocket and set ‘em down. I’m not worried. I’ve got a good eye on where my money is."
    
    "They rummage around and manage to match the money.  Again, not worried. I’ve got a good eye on where their money is, too."
    
    "I take the first three shots, easy. All three of them have got really dumb looks on their faces now."
    
    ob "Not bad, I guess."
    
    "He matches the shots. I can’t help but grin when he starts choking on them."
    
    r "Maybe you should just hand over your money, get some milk, and call it a day."
    
    "No more mocking looks from them now."
    
    "I pour the next three and take them. He matches, but he’s starting to look a little woozy."
    
    "I feel it myself, the sweet fuzz of powerful sake taking over my senses. I enjoy it as best I can...it won’t last long. I pour three more glasses slowly." 
    "I want to savor this and hold the contest up to make sure he’s really drunk."
    
    r "You’re probably feeling fucking stupid right now. Too bad."
    
    "I down all three shots and look at him."
    
    r "Besides losing your money, you’re probably gonna need a hospital."
    
    ob "Nnngh..."
    
    "Someone has to pour his glass for him. Everyone in the bar’s staring at me. They don’t get how I can still be so clear-headed. What can I say...I’m a great drunk."
    
    "When his head hits the table, I immediately snatch up all the money and head off to the bathroom. The poor dumbass." 
    "He never had a chance. His friends are fawning all over him to make sure he’s not going to croak on ‘em."
    
    show bg blackscr with dissolve
    $renpy.pause(1.0)
    "This is the worst part about it, for me. Staring at the nasty bathroom ceiling, I do my business, and by the time I leave the bathroom, it’s like I haven’t had a drop. That’s it. Good-bye, sweet buzz."
    
    "I give my friend his share of the money and stuff the rest in my pocket. Didn’t even get a hangover after nine shots."
    
    show bg blackscr with slow_dissolve
    "Annoyed. I’m so annoyed I don’t even realize I’ve headed home early."
    
    pa "Hey, Riku, can you come here for a moment?"
    
    "What do they want now?"
    
    r "Yeah?"
    
label pdatest:
    ma "You start school tomorrow, right? Well...your father and I wanted to give you something to inspire you a little this year. Here. A present."
    
    r "Hm---ahh!"

    # Display PDA icon blink animation
    $renpy.show("pda_button", at_list=[blink(2.0, 0.0), Position(xpos=842, ypos=651), Transform(anchor=(0.0,0.0))], zorder=8)

    $unlock_item("pda", True) # False = don't show "item unlocked" messages
    
    $ show_message("You can now access the PDA menu.", "medium")

    $pda = True
    
    # Stop the blinking animation
    $renpy.hide("pda_button")
    
    $ show_message("Let's bring it up.", "medium")
    
    call pda_loop
    # or maybe call pda_introduction? Or perhaps fake the first PDA session using images only?
   
    $ show_message("The PDA is how you keep track of your items and what you learn.", "medium")
    $ show_message("It has other uses, but those come up later.", "medium")
    $ show_message("Remember to check your PDA often.", "medium")
    
    $unlock_item("wallet", True)
    
    #This goes back in the regular box.
    r "Whoa, this is the latest tech! It’s awesome! Thanks!"
    
    "I guess it’s not always bad to be the kid of two doctors."
    stop music
    $hide_main_ui()
    
label Scene6:
    scene bg blackscr
    with slow_fade
    show bg dream
    with slow_fade
    $ renpy.pause (1.0)
    #play sound laughter
    #time 4.0
    #stop sound
    show bg blackscr with slow_dissolve
    
    $HP += 100
    $MP += 50
    
    $show_main_ui()
    with dissolve
    
    r "Ugh, again with that stupid dream..."
    
    "I don’t really have time to waste, not on a school day. Not like I want to go, but the first few days aren’t usually too bad, at least." 
    "Besides, I gotta earn my braaaaaaaand new palm pilot. I eat breakfast super fast and head out the door."
    
    "I know I can run fast, but I like to walk with friends sometimes. Now I have something to do on the way there~"
    
    show bg street with dissolve
    $renpy.pause(2.0)
    
    show dg neu at left
    show db neu at right
    with dissolve
    dg "That’s the kid, isn’t it?"
    
    db "You sure?"
    
    dg "Pretty sure. Let’s go."
    hide dg neu
    hide db neu
    with dissolve
    
    "Isn’t this my lucky day? I know I look small, but SHIT--"
    
    "They’re following me. I don’t want them to know where my friend lives."
    
    show bg backalley with dissolve
    "I walk down an alley that’s on the way, instead. I’ll probably be late for school at this rate."
    
    show r grin:
        alpha 0.0
        time 0.75
        linear 0.75
        alpha 1.0
    with dissolve    
    "I turn around and grin."
    hide r grin with dissolve
    
    show dg neu at left
    show db neu at right
    with dissolve
    
    db "Heh. Just like they said, yeah?"
    
    dg "HQ’s information is top-notch, after all."
    
    "Huh."
    hide db neu with dissolve
    show r no at right with dissolve
    r "If you guys have some business with me, let’s get it over with. I have class."
    
    #play sound Knives clicking
    dg "Yeah kid, I'd say we had some business withya."
    show r flush at right with dissolve
    #show r surp
    r "Whoa, is all that really necessary? I’m just one small kid..."
    
    "Gotta play up your strengths, right?"
    
    dg "Midorikawa Riku, right? It’s easy to get your guard down around a short thing like you. I woulda been fooled if I didn’t already know what we were dealing with."
    hide dg neu with dissolve
    show db neu with dissolve
    db "We came extra prepared cause of the special information we got on you, kiddo."
    show r grin with dissolve
    r "Oh, really."
    
    "Who are these people? They’re a little smarter than the usual punk. A new gang, maybe."
    
    db "You should come with us quietly if you want this to go easy."
    
    r "Yeah, or you could just go fuck yourselves."
    hide db neu with dissolve
    show dg grin with dissolve
    dg "Nasty mouth, just like they said."
    show r no with dissolve
    "I really hate them talking like I’m some top-secret science experiment. It’s creepy."
    
    "They’re coming, splitting up to take me from both sides."
    
    scene bg blackscr
    $show_main_ui()
    with fade
    "I close my eyes. I can almost see them just by listening."
    
    scene bg backalley at shaky with dissolve
    $show_main_ui()
    with dissolve
    #show r fight
    #with dissolve
    #Riku makes martial arts cries while attacking.
    #Screen shaking effect
    r "HIIIIIIIIYAH!"
    
    #play sound people getting hit
    dg "Nngh!"
    db "Augh!"
    
    "I kick the knife away from one and get the other in the gut at the same time. Usually that’s enough to discourage people, but these guys are dedicated."
    
    "I’d appreciate the effort if I had the spare time."
    show r mad with dissolve
    r "HAAAAA!"
    
    "The one who still has a knife goes down hard. He’s not getting up."
    
    dg "Shit! You were still this tough..."
    show r grin with dissolve
    r "You wanna end up like your friend?"
    
    dg "N-no! I’m outta here!"
    
    "Slightly more brains, way less guts."
    show r think with dissolve
    "One of the dropped knives is by my feet. It’s pretty fancy; looks like there’s actual gold and silver laced into the handle in some sort of emblem shape..."

    menu:
        "Pick up Knife.":
            jump getknife
        
        "Leave Knife.":
            jump leaveknife
        
label getknife:
        #Message box should go here, too...
        $show_message("You picked up the knife.", "medium")
        #$renpy.show("pda_button", at_list=[blink(2.0, 0.0), Position(xpos=842, ypos=651), Transform(anchor=(0.0,0.0))], zorder=8)
        $unlock_item("knife", True)
        
        #This goes in the regular textbox.
        show r neu with dissolve
        "Might as well keep it. If I can’t use it, I can pawn it."
        jump Scene7
   
label leaveknife:
        show r smile with dissolve
        "You decided to leave the knife."
        jump Scene7
      
label Scene7:
    show r mad with dissolve
    r "Assholes. I guess if I run the whole way, I’ll still be on time for class..."
    hide r mad with dissolve
    #play running sound
    
    "I start to run out of the alley when a wave of nausea hits."
    $ double_vision_on("bg backalley")
    $renpy.pause(2.5)
    $double_vision_off()
    
    show bg backalley at shaky with dissolve
    r "Oomph."
    
    $ Mamoru = "Dark Man"
    
    #$hide_main_ui()
    #scene bg mamview
    #with fade
    #$renpy.pause(1.0)
    #$show_main_ui()
    show m grin with dissolve
    m "Ahh, are you all right?"
   
    r "---uh---"
    
    "I look up and see a strange...oddly compelling man."
    "He seems perfectly normal, but for the first time I can remember...I’m uneasy. Afraid. I want to run. I back up slowly."
    
    #Mamoru chuckles.
    m "You look a bit pale, do you need a doctor? Some water? I don't live in the area, but I have friends--"
    
    r "I---no. I don't need any help."
    
    "Why am I so afraid? Why is everything telling me to run?"
    
    "I start to fidget around."
    
    m "...are you sure? You look so very nervous."
    
    "Damn it. I feel like my skin is crawling, which just makes me fidget worse."
    
    r "No, I just need to get back to school--"
    m "Do...I make you nervous?"
    
    "........"
    
    m "It looks like you have a fair sense about your situation. That’s more than many of your kind, you know."
    
    r "My...kind?"
    
    m "Yes, of course. You didn’t think you were human, did you? Silly child. No, you’re more like...a pig, or a cow. Ahh, but you’re still just an infant, so a piglet or a calf. Cute, really."
    
    r "...what do you mean?"
    
    m "I’m afraid I don’t really have the time to explain. My stomach doesn’t like to be kept waiting."
    
    r "W-what?!"
    
    m "You’re going to run, aren’t you? Feel free; I’ll give you a small head start..."
    
    r "I'm dead. I'm dead!"
    hide m
    
    $battle("Riku", "Mamoru", 1, "bg backalley", False)
    $hide_main_ui()
    with dissolve
    
label SceneDemoEnding:    
    scene bg blackscr with dissolve
    
    $ show_message("This is the end of the Mitsumata demo!", "medium")
    $ show_message("You can now test the minigames!", "medium")
        
    call pda_loop
    
    $ show_message("Thanks so much for playing this demo and please wait for the final release!", "medium")
