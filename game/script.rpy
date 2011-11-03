﻿#****************************************************
#NOTES TO PROGRAMMERS FROM SEIRA
#****************************************************

#Currently at line 2710 out of 6473. Check Bad Endings for necessary animation creations.
#Go to "My species...type?"
#Line 4484 contains a puzzle minigame. 
#Don't forget Roman's "lock" minigame.

#**********************
# SCRIPTING TIPS
#**********************

#{p=timehere} is a function that allows you to pause for the number of second put in the "timehere" slot.
#The bottom two things allow you to change color and size of dialogue within dialogue.
#"{color=#000}This text is colored #000.{/color} This text is not."
#"{size=12}This text is size 12.{/size} This text is not."


#***********************************
# PYTHON CODES GO HERE.
#***********************************

init python:
  print ""
  
  inventory = Inventory()
  journal_manager = Journal_manager()
  pm = Persistent_manager(inventory, journal_manager)
  
  # These are the values that will be used when a new game starts. Everything 
  # defined inside this init block will have its state written somewhere when
  # Renpy creates a new/rewrites an old save game, so it's not actually necessary 
  # to store these in any external file because already Renpy remembers all the 
  # variables' states automatically. Which is nice.
  hp = 0
  mp = 0
  tries = 3
  
  decision = "5"
  event_triggered = False
  pda = False
  minigames = False
  
#---------------------
#KONAMI CODE
#---------------------
# THIS IS A SERIOUSLY FUCKING COOL IDEA AND WE SHOULD ALIGHT A SCENE OR SMTH FOR IT.
# This lets you easily add the Konami code to your Ren'Py game. When
# the Konami code (up up down down left right left right a b) has been
# entered, this calls the konami_code label (in a new context, so that
# the current game state isn't lost.

#init python hide:

#    class KonamiListener(renpy.Displayable):

#        def __init__(self, target):

#            renpy.Displayable.__init__(self)

#            import pygame
            
            # The label we jump to when the code is entered.
#            self.target = target

            # This is the index (in self.code) of the key we're
            # expecting.
#            self.state = 0

            # The code itself.
#            self.code = [
#                pygame.K_UP,
#                pygame.K_UP,
#                pygame.K_DOWN,
#                pygame.K_DOWN,
#                pygame.K_LEFT,
#                pygame.K_RIGHT,
#                pygame.K_LEFT,
#                pygame.K_RIGHT,
#                pygame.K_b,
#                pygame.K_a,
#                ]

        # This function listens for events.
#        def event(self, ev, x, y, st):
#            import pygame

            # We only care about keydown events.
#            if ev.type != pygame.KEYDOWN:
#                return

            # If it's not the key we want, go back to the start of the statem
            # machine.
#            if ev.key != self.code[self.state]:
#                self.state = 0
#                return

            # Otherwise, go to the next state.
#            self.state += 1

            # If we are at the end of the code, then call the target label in
            # the new context. (After we reset the state machine.)
#            if self.state == len(self.code):
#                self.state = 0
#                renpy.call_in_new_context(self.target)

#            return

        # Return a small empty render, so we get events.
#        def render(self, width, height, st, at):
#            return renpy.Render(1, 1)


    # Create a KonamiListener to actually listen for the code.
#    store.konami_listener = KonamiListener('konami_code')

    # This adds konami_listener to each interaction.
#    def konami_overlay():
#        ui.add(store.konami_listener)

#    config.overlay_functions.append(konami_overlay)


# This is called in a new context when the konami code is entered.
#label konami_code:

#    "GJ YOU ACTIVATED SOME SPECIAL SCENE OR SMTH!"

#    return
   

    
#-----------------------------------------
# CREATING AMBIENT MUSIC
#-----------------------------------------
    
# The below code allows us to separate music between silence so that we may make an ambient, cool sounding immersive game. Likely useful.   
# This goes in init block
#    python:
#       def ambient(songlist, interval):
#            playlist = ["sounds/pause_5s.ogg"]
#           for song in songlist:
#                playlist.append(song)
#                j = renpy.random.randint(2, interval)
#                for i in range(0, j):
#                    playlist.append("sounds/pause_5s.ogg")
#            return renpy.music.play(playlist, channel=6)

# This is used a the beginning of label, as the most logical place for ambient noises to begin.. :P
#$ ambient(("sounds/ambient02.ogg","sounds/ambient06.ogg","sounds/ambient09.ogg"), 4)


#--------------------------------------
# SOUNDS DURING TYPING  
#--------------------------------------    

# This stuff here allows you to play a sound while the callback character is talking. 
#init python:
#    def callback(event, **kwargs):
#      if event == "show":
#            renpy.music.play("MUSICFILENAMEHERE", channel="SOUNDHERE")
#       elif event == "slow_done" or event == "end":
#            renpy.music.stop(channel="sound")

# This code here declares who the call back character is. The init and $ signs must be included.
# init:
#    $ r = Character("Riku", callback=callback)



#--------------------------------------------------------------------
# CODE TO MAKE A MUSIC ROOM IN THE MENU
#--------------------------------------------------------------------
#init python:

#    def set_playing_(track):
#        store.playing = track
#        return True

#    set_playing = renpy.curry(set_playing_)

    # Call this with a button name and a track to define a music
    # button.
#    def music_button(name, track):

#        if store.playing == track:
#            role = "selected_"
#        else:
#            role = ""

#        if not renpy.seen_audio(track):
#            name = "u"
#            clicked = None
#        else:
#            clicked = set_playing(track)
        
            
#        ui.textbutton(
#            name,
#            clicked=clicked,
#            role=role,
#            size_group="music")
    
    # Add to the main menu.
#    config.main_menu.insert(3, ("Music Room", "music_room", "True"))

        
#label music_room:

#    scene black

#    python:
#        _game_menu_screen = None

        # The default track of music.
#        playing = "11-Yesterday.ogg"
        
#label music_room_loop:

    # Play the playing music, if it changed.
#    python:
#        renpy.music.play(playing, if_changed=True, fadeout=1)

        # Display the various music buttons.
#        ui.vbox(xalign=0.5, ypos=100)
#        music_button("Yesterday", "11-Yesterday.ogg")
#        music_button("Yellow Submarine", "15-Yellow_Submarine.ogg")
#        music_button("Hey Jude", "21-Hey_Jude.ogg")
#        ui.close()

        # This is how we return to the main menu.
#        ui.textbutton(
#            "Return",
#            clicked=ui.returns(False),
#            xalign=0.5,
#            ypos=450,
#            size_group="music")

#    if ui.interact():
#        jump music_room_loop
#    else:
#        return



#----------------------------------
# DECLARE BG IMAGES
#----------------------------------
# eg. image eileen happy = "eileen_happy.png"

#image bg shrfr = 
image bg hall1 = "gfx/backgrounds/Hallway1.png"
image bg hall2 = "gfx/backgrounds/Hallway2.png"
image bg riroom = "gfx/backgrounds/room1.png"
image bg roroom = "gfx/backgrounds/room2.png"
image bg soroom = "gfx/backgrounds/room3.png"
image bg suroom = "gfx/backgrounds/room4.png"
image bg lib = "gfx/backgrounds/library.png"
#image bg bathroom = 
image bg kitchen = "gfx/backgrounds/kitchen.png"
image bg dfor1 = "gfx/backgrounds/dforest1.png"
image bg dfor2 = "gfx/backgrounds/dforest2.png"
image bg dfor3 = "gfx/backgrounds/dforest3.png"
image bg nfor1 = "gfx/backgrounds/nforest1.png"
image bg nfor2 = "gfx/backgrounds/nforest2.png"
image bg nfor3 = "gfx/backgrounds/nforest3.png"
#image bg shrfr = "shrinefront.png"
image bg kitchen = "gfx/backgrounds/kitchen.jpg"
#image bg traingr = ""
image bg gar1 = "gfx/backgrounds/garden1.png"
image bg gar2 = "gfx/backgrounds/garden2.png"
image bg street = "gfx/backgrounds/streetalley1.png"
image bg store = "gfx/backgrounds/store.png"
image bg backalley = "gfx/backgrounds/streetalley2.png"
#image bg cheapbar = ""

image bg blackscr = "gfx/backgrounds/blackscr.png"
image bg redscr = "gfx/backgrounds/redscr.jpg"
image bg whitescr = "gfx/backgrounds/whitescr.jpg"

image map = "gfx/backgrounds/map.png"
image textbox_l = "gfx/textbox.png"
image textbox_m = "gfx/textbox_2.png"
image textbox_s = "gfx/textbox_mini.png"

#--------------------------------
#DECLARE CG IMAGES
#--------------------------------

image bg dream = "gfx/backgrounds/dream.jpg"


#-----------------------------------------------
#DECLARE RIKU SPRITE IMAGES
#-----------------------------------------------
image r happy = "gfx/sprites/rhappy.png"
#image r sad = ""
#image r scare = ""
#image r grin = ""
#image r fight = ""
#image r blush = ""
#image r upset = ""
#image r neu = ""
#image r mad = ""
#image r confu = ""

#---------------------------------------------------
#DECLARE ROMAN SPRITE IMAGES
#---------------------------------------------------
image ro happy = "gfx/sprites/rohappy.png"
image ro sad = "gfx/sprites/rosad.png"
#image ro scare = ""
#image ro fight = ""
#image ro blush = ""
image ro worry = "gfx/sprites/roworried.png"
image ro neu = "gfx/sprites/roneutral.png"
image ro pout = "gfx/sprites/ropout.png"

#------------------------------------------------
#DECLARE SUSA SPRITE IMAGES
#------------------------------------------------
image su mad = "gfx/sprites/sutch.png"
image su neu = "gfx/sprites/suneu.png"
image su scare = "gfx/sprites/suflip.png"
image su smirk = "gfx/sprites/susmirk.png"
image su grin = "gfx/sprites/suamuse.png"
image su dub = "gfx/sprites/suohrly.png"
image su irk = "gfx/sprites/suannoy.png"

#---------------------------------------------------
#DECLARE SOUME SPRITE IMAGES
#---------------------------------------------------
image s neu = "gfx/sprites/sneu.png"
image s upset = "gfx/sprites/supset.png"
image s smile = "gfx/sprites/sbigsm.png"
image s think = "gfx/sprites/sthought.png"
image s mad = "gfx/sprites/spissed.png"
image s sadsm = "gfx/sprites/ssadsm.png"
image s nerv = "gfx/sprites/snerve.png"
image s ohmy = "gfx/sprites/sohmy.png"
image s distr = "gfx/sprites/sdistractedo.png"
image s blank = "gfx/sprites/sblanko.png"
image s sad = "gfx/sprites/sdepress.png"
image s pens = "gfx/sprites/spensive.png"
image s gigg ="gfx/sprites/stitter.png"
image s shock = "gfx/sprites/sshock.png"
image you grin = "gfx/sprites/youdkgrin.png"
image you piss = "gfx/sprites/youpissed.png"
image you sm = "gfx/sprites/yousm.png"
image you flirt = "gfx/sprites/youflirt.png"
image you misch = "gfx/sprites/youmis.png"
image you neu = "gfx/sprites/youneu.png"
image you bore = "gfx/sprites/youbored.png"

#----------------------------------------------
#DECLARE LIZA SPRITE IMAGES
#----------------------------------------------
#image l neu = ""
#image l upset = ""
#image l frown = ""
#image l smirk = ""
#image l fight = ""

#-----------------------------------------------------
#DECLARE MAMORU SPRITE IMAGES
#-----------------------------------------------------
#image m neu = ""
#image m grin = ""
#image m mad = ""
#image m fight = ""
#image m gentle = ""

#-------------------------------------------------------
#DECLARE KAZUTAKA SPRITE IMAGES
#-------------------------------------------------------
#image k neu = ""
#image k think = ""
#image k freak = ""
#image k frown = ""

#--------------------------------------------------
#DECLARE NORAH SPRITE IMAGES
#--------------------------------------------------
#image n neutral = ""
#image n worry = ""

#----------------------------------------------------------------
#DECLARE DEMON HUNTER SPRITE IMAGES
#----------------------------------------------------------------
#image dg neu = ""
#image dg grin = ""
#image db neu = ""
#image db grin = ""

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
#image rb neu = ""
#image rb scare = ""

#-----------------------------------------------
#DECLARE MISC SPRITE IMAGES
#-----------------------------------------------
#image p = ""
#image u = ""


#-----------------------------------
#DECLARE GAME CHARS
#-----------------------------------
#init python:

    #if lang == "english":
    #    style.default.font = "DejaVuSans.ttf"
        
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
   # elif lang == "japanese":
   #         style.default.font = "enksh.ttf"
   #         style.default.language = "eastasian"
   #         style.default.size = 19
    
   #         config.translations["Language"] = u"言語を選択"

#*****************************************
# DYNAMIC CHARACTER NAMING
#*****************************************
init:
    $ m = DynamicCharacter ("Mamoru")
    $ s = DynamicCharacter ("Soume")
    $ su = DynamicCharacter ("Susa")
    $ ro = DynamicCharacter ("Roman")
    $ n = DynamicCharacter ("Norah")
    $ k = DynamicCharacter ("Kazu")
    $ a = DynamicCharacter ("Audra")
    $ na = DynamicCharacter ("Naomi")


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
     $ renpy.pause(0)
     scene bg whitescr
     show text "rosegold games presents..." with dissolve
     $ renpy.pause(5.0)
     hide text with dissolve
     show text "Mitsumata: The First Act" with dissolve
     $ renpy.pause(5.0)
     hide text with dissolve
     show text "Part I" with dissolve
     $ renpy.pause(1.0)
     hide text with dissolve

     return
    

#*******************************
# EFFECT COMMANDS
#*******************************
init:
   $ slow_dissolve = Dissolve(3.0)
   $ slow_fade = Fade(2, 2, 3)
   $ flash = Fade(0.1, 0.0, 0.5, color="#fff")
   
# The two pan commands do the following.
# Panltr pans the screen from left to right 1600 pixels, taking 10 seconds to do so.
# Panutd pans the screen from up to down 1600 pixels, taking 10 seconds to do so.
# The $renpy.pause() command MUST be used to delay other programming while panning is going on.
# There must always be a full screen's worth of pixels during the pan or it will cause a problem with rendering.
   $ panltr = Pan((0, 0), (1600, 0), 10.0)
   $ panutd = Pan((0,1600), (0, 0), 10.0)

#The below all take with commands.   
#For example, in "wiperight", a wipe from left to right, first the left edge of the image is 
#revealed at the left edge of the screen, then the center of the image, and finally the 
#right side of the image at the right of the screen.   
   $ wiperight = CropMove(1.0, "wiperight")
   $ wipeleft = CropMove(1.0, "wipeleft")
   $ wipeup = CropMove(1.0, "wipeup")
   $ wipedown = CropMove(1.0, "wipedown")

#In a "slideright", the right edge of the image starts at the left edge of the screen, 
#and moves to the right as the transition progresses.   
   $ slideright = CropMove(1.0, "slideright")
   $ slideleft = CropMove(1.0, "slideleft")
   $ slideup = CropMove(1.0, "slideup")
   $ slidedown = CropMove(1.0, "slidedown")

#There are also slideaways, in which the old image moves on top of the new image.   
   $ slideawayright = CropMove(1.0, "slideawayright")
   $ slideawayleft = CropMove(1.0, "slideawayleft")
   $ slideawayup = CropMove(1.0, "slideawayup")
   $ slideawaydown = CropMove(1.0, "slideawaydown")

   $ irisout = CropMove(1.0, "irisout")
   $ irisin = CropMove(1.0, "irisin")

   $ noise_dissolve = ImageDissolve(im.Tile("gfx/effects/noisetile.png"), 2.0, 1)
   
init:
    image snow = Snow("gfx/effects/snowflake.png")

#Shaky uses the at command    
init:
    $ shaky = Shake((0, 0, 0, 0), 2.5, dist=20)

#Shorter dissolve command for teleport
init:
    $ sho_dis = Dissolve(0.2)

#Teleport uses the with command    
init:
    $ teleport = MultipleTransition([False, sho_dis, "#fff", sho_dis, False, 
                                     sho_dis, "#fff", sho_dis,
                                     True, sho_dis, "#fff", sho_dis, True])
   
#***********************
# ITEM LABELS
#***********************
#This unlocks an item.
#inventory.unlock_item("id")
#This locks it again.
#inventory.lock_item("id")
#This checks to see if an item is unlocked.
#inventory.item_unlocked("id")
#This checks to see if an item is locked.
#inventory.item_locked("id")

#For simplistic use during checking for unlocked items
$ pda = inventory.item_unlocked("pda")
$ knife = inventory.item_unlocked("knife")
$ wallet = inventory.item_unlocked("wallet")
$ fullwallet = inventory.item_unlocked("fullwallet")
$ signet = inventory.item_unlocked("signet")
$ redjewel = inventory.item_unlocked("redjewel")
$ map = inventory.item_unlocked("map")
$ salve = inventory.item_unlocked("salve")
$ ice = inventory.item_unlocked("ice")
$ rose = inventory.item_unlocked("rose")
$ cake = inventory.item_unlocked("cake")
$ goodice = inventory.item_unlocked("goodice")
$ trackseed = inventory.item_unlocked("trackseed")
$ memo = inventory.item_unlocked("memo")
$ pic = inventory.item_unlocked("pic")
$ coin = inventory.item_unlocked("coin")
$ seal = inventory.item_unlocked("seal")
$ sake = inventory.item_unlocked("sake")
$ spice = inventory.item_unlocked("spice")
$ meat = inventory.item_unlocked("meat")
$ veg = inventory.item_unlocked("veg")
$ herb = inventory.item_unlocked("herb")
$ pollen = inventory.item_unlocked("pollen")
$ clara = inventory.item_unlocked("clara")
$ terra = inventory.item_unlocked("terra")
$ vita = inventory.item_unlocked("vita")
$ mitsumata = inventory.item_unlocked("mitsumata")
$ uni = inventory.item_unlocked("uni")
$ gun = inventory.item_unlocked("gun")
$ book1 = inventory.item_unlocked("book1")
$ book2 = inventory.item_unlocked("book2")
$ book3 = inventory.item_unlocked("book3")
$ book4 = inventory.item_unlocked("book4")
$ garden = inventory.item_unlocked("garden")
$ phone = inventory.item_unlocked("phone")
$ game = inventory.item_unlocked("game")
$ strpot = inventory.item_unlocked("strpotion")
$ magpot = inventory.item_unlocked("magpotion")

#--------------------------------
# GAME STARTS HURR
#--------------------------------

label start: 
menu:
        "Jump ahead for a test.":
                jump Scene5
        "Start from beginning.":
                jump Scene1
                
label otherstuff:    
    scene bg blackscr
    $show_main_ui()
    
# All of the below commented out effects have proven to work.     
    #show bg riroom at shaky with dissolve 
    #$renpy.pause(3.0)
    
    #show boom
    #$renpy.pause(3.0)
    
    #show snow
    #$renpy.pause(9.0)
    #hide snow
    
    #$ double_vision_on("bg suroom")
    #$renpy.pause(2.5)
    #$ double_vision_off()
    
    #show r happy with noise_dissolve 
    #$renpy.pause(3.0)
    #hide r happy with noise_dissolve
    #$renpy.pause(5.0)
    
    #show ro neu at right with teleport
    #$renpy.pause(2.0)
    
    #show bg soroom with wipedown
    #$renpy.pause(2.0)

    #play music "music/mitsumata1.mp3"
    #show bg rikureading
    "Once upon a time, there was a prince who was not in any way different from other fairy tale princes."
    
    "He was rich, handsome, popular, destined to marry a princess, spoiled---"
    
    "Bored already."
    
    "I’ve barely said a single sentence."

    "And it was the boringest sentence I’ve ever heard in my entire life!"

    "The story might get better if you actually let me tell it."
    
    "Fiiiiiiiiiiine."
    
    "The prince had only ever known the inside of his wonderful kingdom, but there was one other, very special place." 
    "{size=17}You see, he had one thing no other prince had, a large, invisible Tower, filled with Every Good Thing in the entire world. Things from every town, every city, and every country, the best of the best.{/size}" 
    "No one knows how the prince came to have this tower of Stuff, but it's suspected his father collected them from conquered lands."

    "If it’s invisible, how can anyone even find it? And if they do find it, do they just smack their head into it on accident? Like BAM, oh, here’s my invisible tower---"

    "Shhh. Do you want to tell the story, or may I? You’re the one that has to be in bed in 10 minutes."

    "Ooookaaaay. I gueeeeeess you can tell it."

    "{size=17}Thank you. Now, even though the Tower was invisible, the boy had a map to its exact location, as well as the only key in the world that could open its door. Even if other people found it, they wouldn’t be able to have any of the good Stuff inside.{/size}"
    "As the prince got older, the Tower got more and more wonderful things, and soon it was filled to the very tip top of Everything Good in the World."

    "He’s like...the richest kid in the whole universe."

    "Yes, it’s certainly something like that!" 
    "{size=17}Well, one day, as all princes must, he was sent by the king to go out into the land and learn what he could learn. The prince planned for 40 days and 40 nights, and finally, early one morning, he took a step out of the palace he’d lived his entire life in and went out to see the world.{/size}" 
    "He travelled far and wide, and on his return journey, he came upon a little town."

    "I hope he found a hot girl inside."

    "...young man."

    "...sorry."

    "{size=17}There actually wasn’t very much inside. A few broken down, burnt-out huts, a few dried out bits of food in piles for each family, and half-naked children running around and playing in the dirt.{/size}" 
    "They were somewhat surprised to see the prince in all his splendor, but they invited him to sit and play with them. The prince didn’t really want to..."

    "Duh. They’re playing with dirt, and he has a magical tower full of the best toys in the universe."

    "...but he was curious about what they were doing, so he sat down, and he noticed that the children were playing with little pebbles, one pebble for each child."

    "Rocks. They’re playing with rocks."

    "{size=17}Well, when you have no money, anything can become a toy. And these weren’t just rocks; these were some of the most beautiful, shiny pebbles the Prince had ever seen. He wanted them. But, upon asking for them, the children told him that they could not give him the pebbles, for these pebbles were all they had.{/size}"
    "Unsatisfied, the prince thought about it carefully that entire night and went back to the children the next morning."

    "Did he beat them up and just take the pebbles?"

    "Close enough. He asked if they’d share with him." 
    "If they could each take all the pebbles for one night, then they would have to spend some days without any pebbles, but on the night that it was their turn, they’d be able to enjoy all the pebbles." 
    "{size=17}They liked that idea, and since the Prince was the one who came up with it, they offered him the first turn. He took the pebbles, and that night...he left and returned home. The children never even saw it coming.{/size}"

    "So what happened? Did they follow him to the palace and beat him up?"

    "Nope."

    "Well, did a witch put a curse on him to make him a big ugly snarling monster until he got nicer?"

    "Not that, either."

    "...So what happened to him?"

    "Nothing. He just threw the pebbles into his Tower and never looked at them ever again."

    "That’s it? I don’t get it! Nothing bad happened to him?"

    "Nope. Sometimes it just works out that way."

    "That story sucked. I want another one."

    "Language! And it’s your bedtime, and you’ll stay in here and sleep, or you’ll have problems much bigger than a story you don't like."

    "HMPH."

    "Good night, Riku."

    "Night, Mom."
    $ renpy.pause(2.0)    
    
label Scene1:
        scene bg blackscr 
        $hide_main_ui()
        with fade
        
        $ renpy.pause(2.0)
        
        #scene bg mameat1
        scene bg nfor1 
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
        scene bg blackscr 
        with slow_dissolve
# play sound Screaming, crunching, grinding, all sorts of unholy noises.
        $ renpy.pause(3.0)
        #show some kind of splash page here

label Scene2:
        scene bg street
        $show_main_ui()
        with slow_fade
        $ renpy.pause(1.0)

        show st gneu at right with dissolve

        sg "Riku." 
        
        $ renpy.pause(1.0)
        
        sg "...HEY, Riku, wake the hell up!"
        #shake effect here
        
        show r happy at left:
            alpha 0.0
            time 0.75
            linear 1.0 alpha 1.0
        with dissolve
        r "Huh? Oh."
        
        "If you haven't figured it out yet, I'm Riku. Midorikawa Riku, age 17, third year in high school."
        "I don't believe in silly crap like blood-type personalities, and even if I did, I dunno mine. I don't believe in horoscopes, either. Superstition is for kids."

        show r happy at left
        show st bneu at right
        with dissolve
        sb "You've been out of it lately, man...you okay?"
        
        r "Yeah, just thinkin' too hard on school starting again, I guess."

        sb "Pff, yeah. No more free time at all. Even school breaks are gonna get eaten by studying."

        show st gneu at right with dissolve
        sg "Don't remind me of the college exams! I'm so nervous about getting into Toudai. What if I don't get in? How am I going to tell my parents?" 
        show st gwor at right with dissolve
        sg "{size=17}What if I don't make it into Keio either, and I have to go to CRAM SCHOOL for a year before I can reapply? And then what if I fail AGAIN and my parents disown me for being so stupid?! I can't HANDLE THIS---{/size}"

        $renpy.pause(1.0)
        show st gneu at right with dissolve
        "What else do you expect 17 year olds to talk about?"
        "This year in high school is the worst. Once the second half of the year rolls around, no more free time, no more club activities, no more sports---no more fun, period. College exams will own our lives." 
        "Our high school has a pretty good reputation for getting kids into top-level schools, and they're hard-asses about that reputation."
        "Whatever. Bores the shit out of me."

        r "Heh. I heard that this one time, when the school’s practice grades weren't high enough, the principal expelled a bunch of people to raise the marks."

        show st gwor at right with dissolve
        sg "Oh god, you're joking. Tell me you're joking."

        "I am, but she doesn't need to know that."

        show st bmad at right with dissolve
        sb "Riku, don't be a jerk. Not everyone can fly by on sports scholarships like you."

        r "Hey now, don't make it more than it is."

        show st gneu at right with dissolve
        sg "What are you talking about? You’ve got automatic entry no matter how bad you do!"

        r "Yeah, yeah, maybe, but I'm not going to get into any top schools on just sports, and my grades aren't exactly amazing."

        sg "That's because you cut class to go drinking!"

        r "A man's gotta have priorities!"

        "I guess it’s true. I don't have to worry much about grades since I'm kind of a sports legend around here, and even if our school did kick crappy third years out every exam time, I'd get to stay, cause, well..."

        show st bneu at right with dissolve
        sb "Now that I think about it, Riku, you never told us what you got on the first practice exam."

        r "Pfft. Who cares. It was like the bottom quarter."

        "Everyone winces. People with grades that low had better have a hook-up somewhere."
        "Yuck. I don't even want to think about...jobs." 
        "Having to sign my soul away to some company?" 
        "I'd rather stay in high school and deal with shithead teachers for the next 10 years."

        "'Sides, I wasn’t exactly in the bottom quarter anyway." 
        "Not that I studied; I just have a good memory is all. Helps on tests."

        show st gneu at right with dissolve
        sg "Well, serves you right for cutting and refusing to study. That’s okay. When I’m a doctor, you can always be my personal cleaning boy."

        #play sound Laughter.

        #Riku grumbles to himself.
        r "Grr."

        sg "Don't make a sad face, Riku. I could always tutor you, if you're serious...but I'm talking hardcore, three-hour-a-day study sessions, and eight hours on weekends--"

        show st bneu at right with dissolve
        sb "How the hell's he supposed to play if he's studying that much?"

        show st gneu at right with dissolve
        sg "Well, obviously he'll have to sacrifice sports! This is his future!"

        "My watch beeps."
        #play sound beep

        r "...shit."
        
        show st bneu at right with dissolve
        sb "Aw, you gotta head home?"
        
        "I grab my bag and stand, yawning. Just one more day of vacation left, and then it's 48 hours a week of the worst school hell ever."
        "Fuuuuuck.The principal might as well just castrate me now and get it over with."

        "Who in their right mind can even sit for that long, anyway? I got ADD just thinking about it."

        r "Yeah, it's gettin' dark, and I set my watch to tell me when I’m an hour late. Actually, I expect---"
        #play sound Ring ring ring.
        $ renpy.pause(2.0)
        
        r "--my parents to be calling. Yello? Right right, I know; I'm coming. I'm coming!"

        "Those people barking loudly into the phone? My parents. People say I’m lucky, adopted into a rich family of doctors, but they don’t have to live with ‘em."

        show r upset:
            alpha 0.0
            time 2.0
            alpha 1.0
        r "No, I get it---"
        
        r "Awww, not the TV..."

        #play sound Mumbled speaking.

        r "I was already on my way home! Honest! I'm like a minute away!"

        "I wave quickly to my friends, mouthing a good-bye. Ugh. No other seventeen year old in the universe has to be home this early. So fucking unfair."
        
label Scene3:
        #---Flashback---
        scene bg blackscr with fade
        
        #scene bg rikyouth
        $show_main_ui()
        with slow_fade

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
        scene bg blackscr
        
        scene bg street 
        show r happy
        $show_main_ui()
        with fade
        
        "My parents didn't let me have a new door for three whole months cause of that."

        "I do have to be careful, though. Friendly punches can turn into broken arms when I’m the one doing the punching."

        "I make it back to my street pretty fast, running full speed from the beach. My parents won't get on my ass too much for it. They'll actually believe that I was close to home."

        show r happy with dissolve
       
        r "Mm. Kind of cold for spring..."
        #play sound wind

        "Someone's following me. They're being unnaturally discreet about it, too...usually the idiots who want to—well, try to—pick on me don't make much of a show of hiding very well." 
        "Guess they figure it'd be like hiding from the fishbowl when you're trying to catch one of the fish."

        "Heh. My stalkers getting smarter? That'll be the day. Still, if I start a fight at this time of evening on my own street, my parents will flip a nut."

        hide r happy with dissolve
        #play sound Door unlocking.
        #put some kind of door opening effect here to lead into bg rhouse
        show bg riroom with dissolve
        show r happy with dissolve
        
        r "I’m home."

        pa "Riku—in here, please."

        #show r upset with dissolve
        "Aw fuck."

        r "Yeah, Pop?"

        # show pa
        pa "Do you understand why we give you a curfew?"

        r "Yeah, Pop."

        "There's no point arguing about it anymore. They set it when I was like six and have never looked back."

        pa "And why is that?"

        r "Night is when the rapists and murderers come out."

        pa "Riku."

        #Riku makes a nasty, rude, scoffing sound.
        r "...More violent crimes happen at night."

        pa "Exactly. And?"

        r "You want me to be safe."

        pa "And we want you to be able to handle the tiny responsibilities we give you. How can we let you dorm at college if you can't even get home at a reasonable hour?"

        r "Sorry, Pop."

        "It's a damn form letter by this point."

        pa "{size=17}One day, when I get you a job at the company, you're going to see the benefits of going to bed early and waking up early. Life isn't all about friends, Riku. You’ll have a wife and children who rely on you.{/size}"

        r "Sorry again, Pop. Am I free to go?"

        "He sighs, but that means I'm free."

        "I hate his lectures, even when they're short. Nothing outright depresses me more than thinking of having to take up a desk job. My dad doesn't even care about what I wanna do."

        "I don't get no respect around here. No respect at all."
        
        
label flashback:
    scene bg blackscr with fade
    show bg dream with slow_fade
    #put some kind of wispy cloudy effect here
    $show_main_ui()
    with fade
    
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
    
    show bg riroom with slow_dissolve
    
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
    #show bg bar with dissolve
    $ renpy.pause(1.5)
    "I like this place, for a few reasons. One, it’s always got idiots willing to make a bet with me, and two, it’s off the main road, so there aren’t any annoying people nagging at me for underage drinking."
    
    "I wave to my friends. They’re crowded around a table with some large guys, shot glasses already set up."
    
    ob "I thought this guy was supposed to be 17!"
    
    ob1 "Dudn't look older than 12 to me."
    
    ob "Maybe 12 and a half, if he's lucky!"
    
    "This might sound weird coming from a jock, but I fucking hate muscleheads like these guys. They’re always flapping their gums cause I’m a tiny bit smaller than them."
    
    "Whatever. It always ends up the same for them."
    
    "I take a seat and order a burger, rare. The food here's not great, but there's only so many ways you can do a rare burger wrong, mostly by actually trying to cook it."
    
    show r happy with dissolve
    r "Are you here for laughs, or to lose a bet? If you're not a bunch of princesses, why don't we go straight for the good stuff? Onigoroshi sound good?"
    
    "{size=17}Onigoroshi is practically like drinking rubbing alcohol. They don't call it “the demon killer” for nothing; you make it through a few shots and that shit'll put hair on your chest or make your nuts drop, or some other manly shit.{/size}"
    
    "Hasn't worked for me yet."
    
    ob "Why don’t we just get you some milk and call it a day?"
    
    "Ha ha ha. I totally haven’t heard that one before. The big fucking assholes are high-fiving each other like they fucking won a Pulitzer for that cheap line."
    
    "Taking their money will be a pleasure."
    
    $hide_main_ui()
    #scene bg barcg with fade
    $renpy.pause(1.0)
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
    
    show bg riroom with slow_dissolve
    "Annoyed. I’m so annoyed I don’t even realize I’ve headed home early."
    
    pa "Hey, Riku, can you come here for a moment?"
    
    "What do they want now?"
    
    r "Yeah?"
    
    ma "You start school tomorrow, right? Well...your father and I wanted to give you something to inspire you a little this year. Here. A present."
    
    r "Hm---ahh!"
   
    #We need a status message thinger here to declare items.
    $inventory.unlock_item("pda") 
    $ pda = True
    
    $ show_message("You can now access the PDA menu.", "medium")
    
    #Stick an animation here that forces the PDA to blink.
    
    $ show_message("Let's bring it up.", "medium")
    
    call pda_loop
   
    $ show_message("The PDA is how you keep track of your items and what you learn.", "medium")
    $ show_message("It has other uses, but those come up later.", "medium")
    $ show_message("Remember to check your PDA often.", "medium")
    
    $inventory.unlock_item("wallet")
    #This goes back in the regular box.
    r "Whoa, this is the latest tech! It’s awesome! Thanks!"
    
    "I guess it’s not always bad to be the kid of two doctors."


label Scene6:
    scene bg blackscr
    scene bg dream 
    with slow_fade
    #play sound laughter
    #time 4.0
    #stop sound
    show bg blackscr with slow_dissolve
    
    show bg riroom
    $show_main_ui()
    with dissolve
    
    r "Ugh, again with that stupid dream..."
    
    "I don’t really have time to waste, not on a school day. Not like I want to go, but the first few days aren’t usually too bad, at least." 
    "Besides, I gotta earn my braaaaaaaand new palm pilot. I eat breakfast super fast and head out the door."
    
    "I know I can run fast, but I like to walk with friends sometimes. Now I have something to do on the way there~"
    
    show bg street with dissolve
    $renpy.pause(1.5)
    
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
    
    show bg backalley
    "I walk down an alley that’s on the way, instead. I’ll probably be late for school at this rate."
    
    show r happy:
        alpha 0.0
        time 0.75
        linear 0.75
        alpha 1.0
    with dissolve    
    "I turn around and grin."
    
    show dg neu at left
    show db neu at right
    with dissolve
    db "Heh. Just like they said, yeah?"
    
    dg "HQ’s information is top-notch, after all."
    
    "Huh."
    
    r "If you guys have some business with me, let’s get it over with. I have class."
    
    #play sound Knives clicking
    dg "Yeah kid, I'd say we had some business withya."
    
    #show r surp
    r "Whoa, is all that really necessary? I’m just one small kid..."
    
    "Gotta play up your strengths, right?"
    
    dg "Midorikawa Riku, right? It’s easy to get your guard down around a short thing like you. I woulda been fooled if I didn’t already know what we were dealing with."
    
    db "We came extra prepared cause of the special information we got on you, kiddo."
    
    r "Oh, really."
    
    "Who are these people? They’re a little smarter than the usual punk. A new gang, maybe."
    
    db "You should come with us quietly if you want this to go easy."
    
    r "Yeah, or you could just go fuck yourselves."
    
    dg "Nasty mouth, just like they said."
    
    "I really hate them talking like I’m some top-secret science experiment. It’s creepy."
    
    "They’re coming, splitting up to take me from both sides."
    
    scene bg blackscr
    $show_main_ui()
    with fade
    "I close my eyes. I can almost see them just by listening."
    
    scene bg backalley
    $show_main_ui()
    #show r fight
    with dissolve
    #Riku makes martial arts cries while attacking.
    #Screen shaking effect
    r "HIIIIIIIIYAH!"
    
    #play sound people getting hit
    dg "Nngh!"
    db "Augh!"
    
    "I kick the knife away from one and get the other in the gut at the same time. Usually that’s enough to discourage people, but these guys are dedicated."
    
    "I’d appreciate the effort if I had the spare time."
    
    r "HAAAAA!"
    
    "The one who still has a knife goes down hard. He’s not getting up."
    
    dg "Shit! You were still this tough..."
    
    r "You wanna end up like your friend?"
    
    dg "N-no! I’m outta here!"
    
    "Slightly more brains, way less guts."
    
    "One of the dropped knives is by my feet. It’s pretty fancy; looks like there’s actual gold and silver laced into the handle in some sort of emblem shape..."

menu:
    "Pick up Knife.":
        jump getknife
        
    "Leave Knife.":
        jump leaveknife
        
label getknife:
        #Message box should go here, too...
        $show_message("You picked up the knife.", "medium")
        $inventory.unlock_item("knife")
        
        #This goes in the regular textbox.
        "Might as well keep it. If I can’t use it, I can pawn it."
        jump Scene7
   
label leaveknife:
        "You decided to leave the knife."
        jump Scene7
    
    
label Scene7:
    show r mad with dissolve
    r "Assholes. I guess if I run the whole way, I’ll still be on time for class..."
    hide r mad with dissolve
    #play running sound
    
    "I start to run out of the alley when a wave of nausea hits."
    #Some kind of nausea effect here.
    
    r "Oomph."
    
    $ Mamoru = "Dark Man"
    
    #$hide_main_ui()
    #scene bg mamview
    #with fade
    #$renpy.pause(1.0)
    #$show_main_ui()
    m "Ahh, are you all right?"
    
    r "---uh---"
    
    "I look up and see a dark man. He seems perfectly normal, but for the first time I can remember...I’m uneasy. Afraid. I want to run. I back up slowly."
    
    #Mamoru chuckles.
    m "It looks like you have a fair sense about your situation. That’s more than many of your kind, you know."
    
    r "My...kind?"
    
    m "Yes, of course. You didn’t think you were human, did you? Silly child. No, you’re more like...a pig, or a cow. Ahh, but you’re still just an infant, so a piglet or a calf. Cute, really."
    
    r "...what do you mean?"
    
    m "I’m afraid I don’t really have the time to explain. My stomach doesn’t like to be kept waiting."
    
    r "W-what?!"
    
    m "You’re going to run, aren’t you? Feel free; I’ll give you a small head start."
    
    show bg blackscr with dissolve
    #play sound Sound of a backpack dropping
    #stop sound
    #play sound running sounds.
    
    "I gotta get out of here. This guy’s insane, and something’s telling me that I shouldn’t even try to fuck with him."
    
    r "OOMPH!"
    
    show bg backalley with dissolve
    
    "God, I’ve run into one of his friends, haven’t I? I’m gonna die, I’m gonna--"
    
    $ Soume = "Beautiful Person"
    
    show s neu with dissolve
    s "Please stay here. I will handle him."
    
    "When I look up, a man who smells like flowers is hovering over me. Before I know it, I’m being surrounded by sweet-smelling vines that seem to be blocking me off." 
    "He smiles and nods, placing a finger over his lips, before the vines let him out and close."
    hide s neu with dissolve

menu:
    "Trust them.":
        jump trustsoume
        
    "Don't trust them.":
        jump dontrust
        
label trustsoume:
        #Message box should go here, too...
        jump Scene8
   
label dontrust:
        "There's no way in hell I can trust this guy."
        "I should try to find my own way out."
        jump badend1    

label Scene8:
    "I know I probably shouldn’t trust him, but I’m shaking so bad that I’ll take anyone who isn’t eating me. I sit down."
    
    show m grin at left with dissolve
    m "Look what I found~"
    
    #show r scare at right with dissolve
    r "AAANGH!"
    
    m "Well, look at what we have here."
    
    "He’s got me by the neck with a red, inflamed hand, and he yanks me through the vines."
    
    #Put a yank through vines effect.
    #play sound hissing of acid burned skin
    #Mamoru makes a sound of pain.
    show m mad at left with dissolve
    m "Nngh." 
    #stop sound
    m "Oi. Chemical burns? How positively droll."
    
    $ Roman = "Awkward Kid"
    #hide r scare
    #show ro fight at right with dissolve
    ro "Hey---uh---you!"
    
    show m neu at left with dissolve
    m "Really, this meal is becoming a bit too much."
   
    ro "Let him go, or I will...make you regret it!"
    
    "I don’t think this guy knows what he’s doing."
    
    $renpy.pause(1.5)
    "A flash of blue light suddenly appears in his hand, before quickly dissipating."
    #show ro surp at right with dissolve
    m "..."
    r "..."
    ro "..."
    
    "....................."
    
    "Correction: he definitely has no clue what he’s doing. What’s the point of people coming to save me if they can’t even do it RIGHT!"
    
    show m grin at left with dissolve
    m "Let me guess—you’re the new meat? Too bad. I suppose I can fit you both in."
    
    ro "Wai--wait--I’ll get it---"

    $renpy.pause(1.5)
    #play sound false start magic attack
    
    "That’s it. I’m dead." 
    "I didn’t even get laid once."
    
    m "Good show, really, but I’ve had enough dinner interruptions for one day."
    
    "I have to do something, I have to--"
    #stop sound
 
menu:
    "Use Knife":
        jump useknife
        
    "Shoulda picked up that knife!":
        jump noknife
        
label useknife:
    if inventory.item_unlocked("knife"):
        "Thank god I picked up that knife!"
        jump useknife1
    else:
        jump noknife
label noknife:
        "You didn't pick it up!"
        jump badend1
        
label useknife1:
    "I attack using the knife I picked up, sinking it into his wrist."
    show m neu at left with dissolve
    m "Tch." 

    "An odd, hot feeling bubbles up from deep inside. It’s familiar...it sort of reminds me of that dream."

    "I don’t want to die."
    
    "I don’t--"
   
    $renpy.pause(1.5)
    ro "Damn it...damn it, why won’t it work..."
    
    #Mamoru yawns
    m "Still slow, are you? Truly pathetic. Get out of my way...I’m famished."
    
    #play sound The flare of fire.
    #Put some awesome fire effect here.
    hide m neu with dissolve
    
label Scene9:
    scene bg blackscr with fade
    scene bg street
    #show m unhappy
    $show_main_ui()
    with slow_fade
    
    show m mad at right with dissolve
    m "Aahhh! My hand--! You---"
    
    show s smile at left with dissolve
    s "You’re done for today, aren’t you?"
#Mamoru has a knowing, understand, amused voice here.
    m "...ahhh. You. I’ll be back. I suppose you already know that."
#Soume has a calm, amused voice here.    
    s "I wouldn’t expect any less."
#Mamoru sounds amused here, too.
    show m grin at right with dissolve
    m "You live to grow more delicious another day, Riku-chan."

label Scene10:
    scene bg blackscr with fade
    
    scene bg street
    $show_main_ui()
    with slow_fade
    
    show ro worry at left
    show r upset at right
    with dissolve
    
    ro "Hey, are you okay? I’m really sorry about the malfunction back there...I’m still kind of new to this whole rescuing thing..."
    
    r "Uh...I..."
    
    "I’m not sure what they want me to say, so I just stare. One’s a foreigner—he’s got an accent— and the other..."
    
    "The other has me sort of sucking each breath in. Tall (very tall), lean, long hair, shocking eyes, kind smile. The more I look at him, the more I wonder if I’m not dreaming again."
    
    r "...am I dreaming?"
    
    hide ro worry
    show s smile at left
    with dissolve
    
    #Soume chuckles
    s "I’m afraid not, Midorikawa Riku-san."
    
    hide r upset
    hide s smile
    $hide_main_ui()
    with dissolve
    #show bg firstview with dissolve
    #Put wispy wind effect here.
    $show_main_ui()
    
    "He smells powerfully of flowers. It’s making me dizzy."
    
    "And his eyes are so green."
    
    r "R-Riku’s fine."
    
    s "Ara, Riku-san, then?"
    
    ro "Nice to meet you! Are you okay? Come have a seat...you must be famished and in shock and--"
    
    s "\"Roman\"-kun, perhaps we should exercise a bit of restraint..."
    $ Roman = "Roman"
    
    ro "Right, sorry again... Erm... I’m Roman. Roman Kovalyov. This is my partner, \"Soume\". It’s nice to meet you. Try to have a seat."
    $ Soume = "Soume"
    
    r "School. I’m late. They’ll...call my parents...I gotta go."
    
    "I have to get away from these people---I have to find a cop or a doctor or even my mommy..."
    
    s "Please. You must rest. We will deal with your school for you."
    
    show bg street
    #show r happy
    show s smile at right
    with dissolve
    
    "The red-haired guy...Soume, touches my shoulder, and that smell of flowers invades my face. I end up sitting down on the curb."
    
    r "...who was that?"
    
    show ro worried at left
    
    ro "Mamoru. He’s a hunter."
    
    r "A hunter? Like...a guy who kills people?"
    
    ro "Yes. The very same."
    
    #show r scare at right
    
    r "He said...he tried to -eat- me and then...FIRE out of my HANDS."
    
    show s neu at right
    
    s "{size=17}That’s the good side to all of it—you have a few special abilities. You must be terribly stressed, but please listen to me carefully. You are in a lot of danger. Those people will not stop coming after you.{/size}"
    
    r "...oh god, I really fucked up this time..."
    
    ro "No, no, it’s not your fault! But, we want to take you to a safe place. They’ll teach you about yourself and your powers, and you’ll be able to go home when you know enough."
    
    r "The fire thing? And the drinking, and the, uh..."
    
    s "Yes, your biology is different."
    
    #show r confu at right
    r "So, uh...you guys are like me?"
    
    s "Precisely. Allow me to show you."
    
    hide s neu
    hide ro worried
    with dissolve
    #show bg soumeheal
    #with dissolve
    #Put some nice little soft green glowing effect here.
    
    #show bg street 
    #show r excite at left
    #show s smile at right
    #with slow_dissolve
   
    r "Whoa--! You just grew a plant...in your hand!"
    
    #Soume chuckles here.
    s "Indeed."
    
    #play sound Breath of air.
    
    "Soume blows over the tiny bud and a thin powder flies into my face."
    #Some powder flying effect here.
    
    ro "Nn--"
    
    "I feel wonderful. I feel comfortable. I feel relaxed and tired, and like I could sleep."
    
    ro "Is he going to be okay like that?"
    
    s "I don’t want him to get too excited. This is a crowded area and there are a lot of...leavings around. Of a biological nature. There are also other suspicious scents about."
    
    ro "What should I do with him?"
    
    s "I understand that you are new and nervous, Roman-kun, but perhaps try to think about that yourself, hm? I will meet you after I clean up the area."
    
    ro "Okay."

menu:
        "Go home first.":
                jump Scene12
        "Leave without going home.":
                jump Scene13
#* * * * ** * * *

label Scene12:
    scene blackscr with fade
    
    scene bg riroom
    $show_main_ui()
    with slow_fade
    "Like I thought, they were already waiting for me. I've been in some spats before, but how was I gonna explain THIS?"
    
    #show ma
    ma "Riku, it's only the first day and already you're being brought home by truant officers?"
    #show ro
    ro "I'm sorry ma'am. We aren't truant officers. We actually--"
    
    ma "Did you get into a fight with these people? I'm very sorry about my son, gentlemen. And YOU! March straight up to your room---"
    #hide ro
    #show r
    r "Mom, STOP! We could all be in danger."
    
    s "Yes, Riku-kun is right. There isn’t much time, so please simply allow me to explain. Your son was attacked this morning by some very dangerous people." 
    s "I take it by now you've realized your son is...special?"
    
    "There’s a long pause."
    
    pa "Ahem. Maybe.Then again, maybe not. Go on."
    
    ro "With your permission, we'd like to take your son to a safe place where he can discover more about his special gift, and learn to use it for good."
    
    ma "Oh no, absolutely not, not MY boy--"
    
    #Pa shushes his wife.
    pa "Are you two unique like our son?"
    
    ma "NO--"
    
    r "Dad, Mom...they saved my life. You gotta trust ‘em."
    
    s "Again, I fear there isn’t much time, so..."
    
    #show green glow with fade
    #hide green glow with fade
    #show cg soume plant
    
    ma "Oh god..."     
    
    pa "I---see. And Riku, are you okay about going with them? I...your mom and I...I'm sorry we haven't been honest with you. We didn't know much about your past when we adopted you."
    
    r "I...I just have a feeling, but...I think it’ll be okay if I go with them."
    
    "You ever see your own mom ready to cry? It sucks."
    
    ma "Please, I want you two to promise me you'll watch over my son."
    
    s "You have my word."
    
    ro "Definitely. Riku will be safe, and we’ll bring him back as soon as we can."
    
    s "As far as school lessons, we have many on-grounds teachers, and we’ll have him call you the moment he arrives."
    
    pa "It...sounds reasonable."
    
    ma "Riku, listen to me. No matter what happens, we’ll be here. You remember what I told you about staying safe. And take this."
    
    $inventory.unlock_item("redjewel")
    
    r "Yeah. Thanks, Mom."
    
    ro "We should...probably..."
    
    #Riku sounds choked up here, like he's about to cry.
    r "I’m gonna call soon as I can, okay?"
    
    "And just like that, the old Midorikawa Riku was dead." 
    "In an instant, everything had changed, and my new life was finally starting."
    
    "I wonder if the girls are gonna be cute."

#-----------------------------
# CHAPTER CHANGE
#-----------------------------  
    
label Scene13:
    scene blackscr with fade
    
    scene bg dfor3
    $show_main_ui()
    with slow_fade
    r "What a fuuuuucking long ride!"
    
    s "But it was exhilarating, wasn’t it? Seeing the city, seeing the people go by. I do SO love the train system!"
        
    r "Roman, your uh...friend here...is a little...off."
    
    #show ro frown 
    ro "Don’t say that; he’s just not used to going much of anywhere. He’s always like this when we get out. I think it’s sort of endearing."
    
    r "Sure. Endearing. Right."
    
    "I guess, at the very least, there isn’t really anyone around. In fact---"
    
    r "...where the heck are we?"
    
    s "Oh, we have to take the bus from here~ There aren’t really any trains that go where we’re headed!"
    
    "He’s still prancing around like a fucking butterfly."
    
    "A giant pink kimono-wearing butterfly." 
    "Roman’s staring at him like he’s waiting for him to burst into flames, or something, before finally pulling out a map and futzing with it."
    
    ro "Um...the er--I can’t read these kanji---I think---oi."
    
    #Soume is sort of humming to himself, here.
    s "Lalala~"
    
    r "Let ME see it. Where’re we going?"
    
    ro "______ Shrine."
    
    r "Hmmm. Okay, that’s here. Looks like the bus is...what the hell! We’ve got a three-mile walk to the bus station, and then it’s another two hours by bus! Where the heck is this place?"
    
    s "Hidden~"
    
    ro "For protection. Three miles shouldn’t be a big deal."
    
    r "It’s not. It’s just annoying. Plus I’m tired and hungry. Is there even a restaurant around..."
    
    "Soume suddenly tilts his head, his face solemn and focused as if listening to something."
    
    s "We should get moving."
    
    ro "Right."
    
    r "...something happening?"
    
    #Soume giggles here and blows.
    s "Hee hee."
    
    r "Agh---"
    
    s "I’m sorry to delay your feeding schedule, Riku-kun, but we must start walking."
    
    r "Yeah, yeah."
    
    "I could’ve complained more, but he saved my life, I guess."
    
    #show ro frown with fade
    $hide_main_ui()
    scene blackscr
    with fade
    
    #* * * * * * *
    scene nfor3
    $show_main_ui()
    with fade
  
    "It’s nightfall by the time we get there, and I’m exhausted."
    
    show r happy at left with dissolve
    
    r "I’m starvin’. If this place doesn’t have food, I’m going to cook one of you guys."
    
    show s gigg at right with dissolve
    #Soume giggles.
    s "I’m afraid we wouldn’t be to your tastes, Riku-kun~"
    
    hide s gigg
    show ro pout at right with dissolve
    ro "That’s really not a nice thing to say."
    
    r "Stick in the mud."
    
    "Finally, we arrive at a..."
    
    s "Aaaa~ My pretty flowers~ Look at how you’ve drooped while I was gallivanting about in the city. My apologies~"
    
    "Weirdo."
    
    r "So...where’s the shrine?"
    
    "Roman points up. And up. And up. I think I see a dot up there, somewhere, deep in the distance."
    
    scene bg shrfr
    $hide_main_ui()
    with slow_dissolve
    #Make the shrine go up.
    $show_main_ui()
    
    r "...you’re kidding."
    
    show ro pout with dissolve
    ro "Well, what did you expect? It wouldn't be very safe if it were just out in the main road."
    
    r "Nyeeeeh."
    
    #play sound Steps
    
    r "I am not made for all this camping---whoa."
    
    show bg riroom with slow_dissolve
    show bg roroom with slow_dissolve
    show bg soroom with slow_dissolve
    show bg suroom with slow_dissolve
    show bg kitchen with slow_dissolve
    show bg hall1 with slow_dissolve
    show bg library with slow_dissolve
    show bg hall2 with slow_dissolve
    #show bg bath with slow_dissolve
    #show bg traingr1 with slow_dissolve
    #show bg traingr2 with slow_dissolve
    show bg gar1 with slow_dissolve
    show bg gar2 with slow_dissolve
    #show bg shrfr with slow_dissolve
    
    "The shrine is huge, when you get up close to it, and there are koi ponds, gardens, a pool and a training ground."
    
    s "Oh no! My little darlings here are drooping, too..."
    
    #Roman laughs.
    ro "Ahaha."
    
    r "Touched, isn’t he?"
    
    ro "He is a bit eccentric..."
    
    "I watch him. A tiny glow appears between his fingers, and the droopy flowers lift up and bloom."
    
    ro "I think he’s pretty amazing. He's saved my life so many times."
    
    #show ro smile
    r "Yeah. I guess he’s not so bad."
    
    $renpy.pause(2.0)
    show suroom with dissolve
    
    s "Susa-san~ We’ve returned."
    
    su "Bout time ya fuckin’ brats got here. Took you all damn day. You bring the kid? Disinfect him?"
    
    s "Yes ma’am."
    
    "A pretty girl about my height heads down the hall. I straighten up immediately...she’s got a mean look on her face, but she barely looks older than me."
    
    su "Midorikawa Riku, right? Scrawnier and shorter than I thought."
    
    "I am not THAT short."
    
    r "Hey, ya ol’ bitch, don’t call me sho---AAA--HEY--QUI--YOU"
    
    #play sound Smacked Around
    #scene bg suhit with fade
    #$hide_main_ui()
    #shaking screen effect
    #$show_main_ui()
     
    su "You cuss in my shrine again, and next time I’ll break a hole in your skull, got it?"
    
    r "Bitch--you actually bruise---AA--OW-OW-OW-OKAY-QUIT IT!"
    
    su "Get this little shit out of my shrine before I kill ‘im."
    
    r "You f--"
    
    su "What wazzat, brat?"
    
    r "...you...darn...person..."
    
    su "That’s what I thought. Take him to his room, and to the doctor later. You have permission to do whatever you gotta to get him to comply."
    
    show hall1 with slow_dissolve
    
    #Roman makes a sound like he's trying to hold back a laugh.
    ro "Hnnf."
    
    #Soume giggles.
    s "Yes, ma’am!"
    
    r "You think this violence is funny?! Just ‘cause she’s a girl--"
    
    ro "Shh--Susa-san is very nice if you just listen. And don’t insult her. It’s rude for one, and for two, she WILL hurt you."
    
    s "Not seriously. These little bruises are nothing."
    
    "He reaches out and just barely presses a finger to a bruise." 
    #glow effect here
    
    "His fingers are warm when they touch me, and the pain stops."
    
    r "Whoa---you have some kind of healing power or somethin’?"
    
    #Soume giggles.
    s "A bit! I would be glad to explain it to you later, I am simply dying for a glass of water, so Roman-kun will show you around. Please excuse me."
    
    "I look to Roman."
    
    #show ro sweat with dissolve
    #show ro smile with dissolve
    
    ro "Well, first—here."
    
    $inventory.unlock_item("map")
    $inventory.unlock_entry("Humans", "054")
    $journal.unlock_entry("Majin", "043")
    
    ro "It’s a map of the whole place, and some basic information on Majin. You can just put it in your palm pilot if you want to read it later."
        
#    The palm pilot is how Riku keeps track of everything he owns and learns. If you receive items or journal entries, check them by clicking on your palm pilot and clicking on the correct icon.

    r "Majin? What’s that?"
    
    ro "That’s what you are. What we are."
    
    r "There’s a word for it?"
    
    ro "Of course. We aren't human, after all." 
    ro "Read that carefully. It will teach you about the main differences between us and humans, and how to avoid getting caught."
    
    show r neu
    r "Okay. I got it."
    
    ro "This place is a rescue for Majin."
    ro "Soume’s plants keep us completely hidden from the wrong people; it’s why he takes such good care of them." 
    ro "But, Susa doesn’t just let us stay for free, you know? You get up, 4am--"
    
    r "FOUR FUCKING---"
    
    ro "Wai--"
    
    #play sound crashybang
    #shake screen
    su "THE FUCK I TOLD YOU ABOUT FUCKIN’ CUSSIN’ IN MY FUCKIN’ HOUSE, YOU UNGRATEFUL SPROG."
    
    #Riku whispers, here.
    r "...how did she hear me?"
    
    #Roman's also whispering here.
    ro "I'm not joking. Please don’t test her. She finds cursing awfully disrespectful."
    
    r "...got it."
    
    ro "But yes, 4am, sharp, you’re up. We do a warm-up, then we clean the grounds. We eat breakfast at 7am, then it’s training or school. You should probably finish..."
    
    r "Noooooooo thanks. I’d rather learn about my fire powers."
    
    ro "We figured. But I actually very much like the school system here. I never had a real chance to go as a child."
    
    r "You can’t be much older than me, right?"
    
    ro "Eh? Oh...I forget you’ve lived your entire life as a human. Majin live a fair bit longer than humans, actually...you ever wonder why you’re so...well...er..."
    
    r "Yeah yeah, I’m short. I get it."
    
    ro "Yes, but...that’s because as a Majin, you’re still essentially a baby. Approximately 80 or so years from physical maturity."
    
    r "...80 years before I grow up?"
    
    ro "Something like that, yes."
    
    r "Whoa."
    
    show ro neu at right with dissolve
    ro "Explains a lot, doesn’t it?"
    
    r "YEAH! I was wondering, you know, ‘cause most boys my age..." 
    r "Like...their junk descends and stuff, and my parents told me it was totally okay, but I was pretty sure it totally wasn’t, you know?"
    r "I only slept through half the biology classes; I figured I knew what I was talking about."
    
    show ro sweat at right with dissolve
    ro "...that’s...an awful lot of information...all at once...so suddenly."
    
    r "Anyway, g’on and explain more."
    
    ro "Alright. Most Majin are much older than they look." 
    ro "Soume is maybe 1,000. He refuses to tell me." 
    ro "I’m going to be a hundred myself in the coming year."
    
    r "Oh, then the old bi---uhhh---lady is probably about a million."
    
    ro "Actually, she’s younger than me, but she’s not one of us. She’s a human. About 80 or thereabouts."
    
    r "80-year-old humans do NOT look like that."
    
    ro "Some of them do. I’m not sure what they’re called, really, but they all belong to that Church, the Church of the Acts."
    
    $journal.unlock_entry("Church of the Acts", "038")
    $journal.unlock_entry("Humans", "057")
    $journal.unlock_entry("Church of the Acts", "041")
    
    r "That new popular thing that opened up in the country?"
    
    ro "Yes. They’re making moves recently to spread, and it’s getting more dangerous for Majin."
    
    r "So they’re like...special humans, that...eat Majin?"
    
    ro "Yes. Many Majin eat humans as well, but that’s extremely dangerous, and they're likely to be caught by hunters. It's difficult because most of us are carnivorous."
    
    r "Hunters? Lemme guess...like going and shooting a deer?"
    
    ro "Exactly."
    
    r "Whoa. So I really was in trouble, huh?"
    
    ro "Yes, but not anymore. They can’t find us here." 
    ro "The plants sort of guide anyone it doesn't want entering in the wrong direction. Even we have trouble finding the place if we leave without Soume's help."
    ro "Well, he's the only one excited about leaving the grounds anyway."

    ro "You probably won’t be able to visit your parents for a little while, either."
    
    r "Yeah, guess not."
    
    ro "The people here train, learn about the human world and how to survive. So that we can find more of us, and protect them."
    
    r "From being food, right?"
    
    ro "Or worse. They’ll keep you alive and use you as a science experiment, or a slave..."
    
    r "Okay, okay, stop with all that. Let's talk about something nicer." 
    r "Where do we come from?"
    
    ro "We're not sure. There seems to be some sort of mess that brings us from wherever our true home is, our world, to here." 
    ro "There doesn't seem to be a rhyme or reason to it."
    ro "I hear our world is practically sitting on top of this one...but only a few of us can sense it."
    
    r "So we're like aliens. Jeez. Tell me something less depressing about all of this. Like about my---"
    
    ro "Right, right—your powers. Ours are self explanatory. We're elemental users."
    ro "You use fire, I use ice. Soume can control plants."
    
    $journal.unlock_entry("Majin", "044")
    $journal.unlock_entry("Majin", "047")
    r "Is it hard?"
    
    ro "Immensely. I’m still trying to get it right in the heat of battle, myself..."
    
    r "And I’ll learn how to use them whenever I want? Like I could toast a marshmallow on my fingers in the winter?" 
    # For the Japanese version, replace marshmallow with yam.
    
    ro "Not quite sure if it works that way, but possibly."
    
    r "Coooool."
    
    show bg riroom with dissolve
    $renpy.pause(1.0)
    show ro neu at right
    show r happy at left
    with dissolve
    
    ro "Well, this room’s yours. There’s a futon, blankets and pillows in the closet."
    
    r "Kind of...empty, isn’t it?"
    
    ro "You’ll fill it up quickly. You should see Soume’s room—it’s crowded from wall to floor."
    
    r "Hm. Maybe I will..."
    
    $journal.unlock_entry("Humans", "055")

menu:
    "Hang with Soume.":
        jump Scene14A
    
    "Hang with Roman.":
        jump Scene14B
    
label Scene14A:
        scene bg blackscr
        $show_main_ui()
        with slow_fade
        "I decide to hang with Soume, since I already spoke with Roman. I head to his room. Roman wasn't kidding...it's covered in greenery."
        show bg room3 with slow_dissolve
        show s smile at right with dissolve
        s "Ahh, Riku-kun. How are you getting along here?"
        show r upset at left with dissolve
        r "A little smothered by your 'friends'." 
        show s gigg at right with dissolve
        #Soume giggles.
        s "Oh, they mean you no harm. Quite the opposite, in fact; they're our protectors~"
        show r neu at left with dissolve
        r "Roman keeps talking about how hard it is to control these powers, but you make it look easy."
        show s smile at right with dissolve
        s "Every Majin learns at their own pace~ There are many things at work. You seemed to take to your fire abilities quite well—I would hate to get on your bad side after a little proper training!"
        show r grin at left with dissolve
        r "And why is that? Afraid I'll singe the foliage?"
        
        $journal.unlock_entry("Soume", "010")
        "There he goes again, dancing around and being all fucking whimsical."
        show s gigg at right with dissolve
        #Soume giggles.
        s  "Ara, Riku-kun, you do have a way with words. No Majin abilities are perfect; each one has its weaknesses. /nMy own happen to include extreme temperatures...really, I’m a bit useless against you and Roman-kun. I try to fight from behind the scenes."
        show r confu at left with dissolve
        r "But...didn't that guy, uh...Akemiya, I think...use fire? He seemed pretty scared of you."
        show s upset at right with dissolve
        $renpy.pause(1.0)
        show r neu at left with dissolve
        "Whoa, think I struck a chord. This is the first time I've seen this guy's face drop."
        show s pens at right with dissolve
        s "Ah...well. Mamoru-kun merely miscalculated the situation. He’s not one to charge into situations he hasn’t properly prepared for. Next time, I don't think we'll be so lucky."
        
        r "So do you, uh...know him?"
        show s neu at right with dissolve
        s "I’ve fought against him many times. You could say I know him as closely as one should know their worst enemy." 
        $renpy.pause(1.0)
        show s smile at right with dissolve
        s "Yes, I think that’d be the appropriate expression."
        
        r "Hm. I think I get it."
        
        "This guy’s pretty carefree. For someone who’s probably in mortal danger, and all. S’kind of weird."
        
        s "Get some rest. We start training tomorrow." 
        
        show bg blackscr with dissolve
        $hide_main_ui()
        with slow_fade

        jump dec1
        
label Scene14B:
        scene bg blackscr
        $show_main_ui()
        with slow_fade
        "Ten minutes. Ten minutes I've been trying to melt chocolate.  I can’t really remember how I called that fire the first time, but whatever I did, it’s not working."
        show bg room2 with dissolve
        show r upset at left with dissolve
        $renpy.pause(1.0)
        show r mad at left with dissolve
        #shake effect
        r "What’s the point of powers if they’re this stupid to use!"
        
        show ro pout at right with dissolve
        ro "What are you doing with that chocolate...?"
        show r neu at left with dissolve
        r "I'm practicing."
        
        ro "...with...chocolate?"
        
        r "I'm trying to melt it." 
        show ro neu at right with dissolve
        ro "Ah...wouldn't an oven be faster?"
        
        r "I’m trying to do it with my fire powers. I've been trying a long while, but I can’t get it to work. It came to me so easily before."
        show ro smile at right with dissolve
        ro "One thing you’ll find is that duress forces your body to do things it would never normally do. Soume’s going to be your teacher, I think, so he’ll train you to bring that out."
        show r grin at left with dissolve
        r "Ohhh, is that why you were so terrible at it when we were about to get roasted?"
        
        show ro flush at right with dissolve
        ro "Ahem...well, erhm, I already explained it...I’m new to this sort of thing. And I’m of the ice element. He’d’ve murdered me slightly less quickly, I imagine..."
        show r neu at left 
        show ro neu at right
        with dissolve
        r "You mean your power’s stronger than mine? But can’t fire like, melt ice?"
        
        ro "I’m not really sure how it works myself, to be perfectly frank. Though...your powers seem quite similar to his. It’s rather rare from what I hear, actually."
        
        r "Rare?"
        
        ro "Yes. I mean, dark like yours is, anyway. Usually, it’s normal-colored. Fire-colored."
        
        r "Yeah, I’ve never seen fire that was...uh...black."
        show ro smile at right with dissolve
        ro "You can ask Soume about it later. But fire’s a strong element, even against other fire."
        $journal.unlock_entry("Riku","004")
        show r grin at left with dissolve
        r "So next time I run into that guy, he's toast!"  
        show ro sweat at right with dissolve
        ro "I wouldn’t say that...you must be trained, after all..."
        
        r "Yeah, I’m gonna kick him in the -----, right before I shove his ------ down into his ----"
        
        ro "Oh, Riku..."
        show bg blackscr with dissolve
        $hide_main_ui()
        with slow_fade
        
        jump dec1
  
label dec1:
    $show_message("This is your first nightly decision.", "medium")
    $show_message("Nightly decisions are a large part in determining the direction of your game.", "medium")
    $show_message("You should definitely try to save before each one, and make different choices.", "medium")
    
    $ decision = "1"        
menu:   
        "Sleep.":
             call sleep  
             jump Scene16
            
        "Search.":
            $show_message("This is your first search!", "medium")
            $show_message("Each evening, you can search the room for treasure. Sometimes you will unlock extra scenes.", "medium")
            $show_message("Click on items to see if there is anything behind them.", "medium")
            $show_message("However, you can't search all night, so keep an eye on how many clicks you have left.", "medium") 
            call show_map

label Scene16:
    scene bg blackscr
     
    scene bg maminpain
    $show_main_ui()
    with slow_fade
    m "Nngh..."
    
    m "Damned youko."
    $ Norah = "Young Lady"
    n "Brother~ The fox got ya, didn’t he?"
    
    m "Tch. I won’t make the same mistake again."
    
    n "Ouchies! That burn looks like it hurts?"
    
    m "Don’t you have anyone else in agony to mock? Like the children in the dungeons, perhaps?"
    
    n "---I’m sorry. I didn't mean it."
    
    #Mamoru makes a sound of agony.
    m "No, it’s all right, \"Norah\". Would you mind bringing me a glass of water? Aaghh--" 
    $ Norah = "Norah"
    #play sound Sound of sizzling flesh
    
    n "Okay. Hang in there."
    
    m "Nngh. Damn it...DAMN IT." 
    #play sound Sound of punching a wall
    
    n "Niisan, I brought the water...have you checked with the doctors?"
    
    m "No point. This is something of a level far beyond any of our doctors. It's something new he drafted up just for me."
    
    n "Well, I brought some fire salve. I could at least wrap it for you, and bring you a meal?"
    
    $inventory.unlock_item("salve")
    
    m "You’re a good girl, Norah. My favorite sister."
    
    n "Always!"
    n "Wrapping's almost done, promise."
    
    m "Thank you..."

#play sound knocking on door    
    Maid "Mamoru-sama, I heard you called for me."
    
    n "Mhm! Right this way. Niichan needs your help with something. He’s very ill and we need some medicine."
    
    Maid "I...understand. Shall I call upon the doctors?"
    
    n "Oh no. No need."
    show bg blackscr with slow_dissolve
    Maid "Wait--wait!!"
    Maid "Please--please don’t---aaaah!"
    show bg redscr with dissolve
    #play sound horrible ravenous eating sounds
    $renpy.pause(1.0)
    show bg blackscr with slow_dissolve
    
    n "Are you satisfied? You ate so much!"
    
    #Mamoru says this gently, as if he is drifting to sleep.
    m "Thanks for the meal...Norah..."
    
    n "Anything, big brother."
    
    $hide_main_ui()
    with slow_fade
        
label Scene17:
    scene bg blackscr
    $show_main_ui()
    with slow_fade

    "My first morning in this weird place. I roll around and groan. Don’t really want to get up."
    
    show bg riroom with slow_dissolve
    show r neu with dissolve
    r "Yawwwwwwwwwn. Wonder what time it is. No one’s bitc---uh, being loud, so I guess I didn’t have to get up and clean."
    
    r "Mmm. 8 am. That’s not bad, I guess."
    hide r neu with dissolve
    
    "I peer inside the closet. I didn’t get a chance to bring too much from home. I guess it’s all hitting me just now."
    
    "I’m living in a shrine, like a monk worried about cleaning. The clothes in my closet are worse than uniforms."
    
    "It’s enough to make me miss school."
    
    "Thinking about it all is giving me a headache. That was my old life. I can’t go back there anymore."
    
    "And this life has superpowers. How bad could it be?"
    
    #play sound knocking
    show ro neu at left with dissolve
    ro "Riku, you should head down to the training grounds. Soume would like to start with you today."
    
    show r neu at left with dissolve
    #Riku makes a grown, as if tired.
    r "Unngh."
    
    hide ro neu
    hide r neu
    with dissolve
    
    "I get up and put on my new slave wear."
    show bg hall1 with dissolve
    
    show bg gar1 with dissolve
    "Following the map, I head out to the training grounds. Soume’s already there, talking to the flowers as if they could talk back."
    
    show bg souwithplants with dissolve
    "It’s only just then that I realize that the plants actually seem to like it. They’re all sort of shifting toward him."
    
    "Really weird, but...cool."
    hide bg souwithplants
    hide bg gar1
    show bg traingr
    with dissolve
    
    show r neu at left with dissolve
    r "Hey Soume! I’m ready for training!"
    show s smile at right with dissolve
    s "Oh, good morning, Riku-san~ I was just chatting with my little friend. Are you prepared? We’ve got a long day ahead of us."
    
    r "Are you kidding? I’ve been waiting to figure these powers out for ages!"
    
    s "Uhm, well, why don’t we begin with a 10-mile run?"
    
    show r confu at left with dissolve
    r "Awhuh?"
    
    s "A sound body, a sound mind, and a sound spirit. All three are necessary to properly channel your ki without any waste."
    
    r "Ki?"
    
    show s think at right with dissolve
    s "Mmm, how to explain it...your demonic energy." 
    s "When you sleep well, eat well, and feel well, your ki is at its peak. When your mood is low, or you’re hungry or thirsty, or tired, your ki drops."
    s "It’s the product of a set of fine-tuned biological variables."
    
    show r neu at left with dissolve
    r "...oh. I have no idea what you just said."
    
    #Soume gives a gentle laugh.
    show s smile at right with dissolve
    s "No worries, I’ll show you."
   
    #These begin instructions for the next minigame.
    #show bg minigame with dissolve.
    #Soume takes a deep breath.
    $hide_main_ui()
    scene bg soupowers 
    with slow_dissolve
    $renpy.pause(2.0)
    $show_main_ui()
    s "Youki is channelled when you are balanced."
    
    #show Green glow with fade
    
    "As you get more used to the feeling of the channelling, you become better able to utilise it under duress; but to start, you should try to eat healthily, drink a lot of water and sleep 10 hours a night."
    
    "Connect your body to your mind, your mind to your spirit, and release it all at one single point."
    
    "That is the secret of youki."
    
    "A small spindle of a green vine twines itself around Soume’s fingers and forms a bud."
    
    $hide_main_ui()
    scene bg traingr 
    $show_main_ui()
    with slow_dissolve
    
    show r confu at left
    show s smile at right
    with dissolve
    r "Whoa..."
    
    s "Did you understand all that?"
    
    r "I think so... Your, uh...plant power. That’s...pretty cool."
    
    s "Oh, don’t flatter me~! It’s embarrassing!"
    
    r "I mean, uh...how many of us can do that?"
    
    show s think at right with dissolve
    s "Erm, well."
    
    show r neu at left with dissolve
    r "It’s rare?"
    
    s "It’s specific to my kind, but..."
    
    r "...if you don’t want to talk about it---"
    
    show s smile at right with dissolve
    s "It’s fine. I just haven’t seen any others like me in a very long time; that’s all."
    
    r "How old are you, anyway?"
    
    s "Ohhh, a few thousand or so, give or take..."
    
    show r confu at left with dissolve
    r "Whaaa--? No way!"
    
    s "I’m just kidding~ There’s no way I could be that old~"
    
    show r neu at right with dissolve
    r "Aren’t you just a big joker."
    
    s "Sorry, sorry~ Come now. Try to channel your youki. We’ll spend a few days on this."
    
    show r confu at left with dissolve
    r "Whaaa--? A few DAYS? You mean I’m not gonna be able to shoot a fireball by the end of the week?"
    
    show s neu at right with dissolve
    s "I suppose it’s possible, but the expenditure of energy would likely drain your life force and kill you."
    
    show r grin at left with dissolve
    r "...got it. But I warn ya, I’m a major athlete, so I’ll probably get this in minutes."
    
    s  "No need to rush; holding it for a few minutes untrained is a feat by itself."

#call minigame magic control   
    #Put a minigame here:
    
    #This is a balancing game. Channel Riku’s Youki so that it forms a ball at the tip of his finger, just like Soume showed you.
    
    #Instructions: PUT INSTRUCTIONS HERE
    
#label balance failure:
    #r "Awww, this is really tough!"
    
    #s "It takes a bit of practice. Try again, and focus this time."
    #here, the game must replay until you beat at least 1 level.
    
#label balance success:
    r "I did it--whoa."
    
    show r dizzy at left with dissolve
    show s ohmy at right with dissolve
    s "Are you all right, Riku-san?"
    
    r "Yeah, I just...dizzy, all of a sudden."
    
    show s neu at right with dissolve
    s "That’s normal. You’ve never exercised this muscle, after all. Take a few minutes, and get some water and have a rest."
    
    "I settle down for a moment, but I really want to try it again. It takes a little while, but I can soon hold a steady flame."
    
    show r grin at left with dissolve
    r "Hey, I think I’m getting the hang of it!"
    
    show s distr at right with dissolve
    s "Hm, oh, Riku?"
    
    show r neu at left with dissolve
    
    r "Hm?"
    
    "I look up and take a puff of pollen right to the face. My concentration drops."
    
    show r confu at left with dissolve
    r "Aaahh!"
    
    "The flame disappears. Damn it!"
    
    show s neu at right with dissolve
    s "Balance, Riku. You must fight to keep your internal balance in any circumstance, or the enemy could do something as simple as blow at you and leave you in a vulnerable state."
    
    show r upset at left with dissolve
    r "Augh, yuck. What’s in this stuff?"
    
    show s smile at right with dissolve
    s "Oh, just a few things of my own private recipe—doesn’t it smell lovely~?"
    
    r "Yeah, yeah, just like roses."
    
    show s ohmy at right with dissolve
    s "Roses? No, that’s not right...I didn’t use any roses..."
    
    show r neu at left with dissolve
    r "I mean---it smells good; that’s all."
    
    show s think at right with dissolve
    s "But if it smells like roses, then I must’ve mixed the blending up..."
    
    r "Soumeee..."
    
    s "Hm?"
    
    r "Training?"
    
    s "Right, of course. My apologies---where was I...ah! Your enemies will use any number of surprising techniques to break your focus."
    s "{size=17}Fear that you haven’t properly channeled will induce the same effect on your youki, so you must be absolutely cognizant and never expect your enemy to allow you even a second to build an attack.{/size}"
    
    r "Okay. I got it."
    
    "The smell of the pollen is everywhere."
    
    show r confu at left with dissolve
    r "What’s your pollen supposed to do, anyway?"
    
    s "I’m not sure anymore...if it smells like roses, you might turn purple, or your tongue might grow too large for your mouth..."
    
    r "...d-don’t make jokes like that!"
    
    s "Er...yes...jokes..."
    #Soume mumbles this here line
    s "I should probably watch him..."
    
    r "I’m gonna die in here. I just know it."
    
    "I spend most of the day training. After that, I’m totally beat, so I head back to my room."

    show bg blackscr with dissolve
    $hide_main_ui()
    with slow_fade
#* * * * * * * * *

label Scene18:

    "I can still smell Soume’s pollen all over me."
    "I guess I needed a shower anyway, but I’ve sort of gotten used to the scent. It really IS nice, and nothing weird happened, so that’s somethin’ at least." 
    
    ro "Ah, good evening, Riku-kun. How did your training go?"
    
    r "Training was AWESOME. Soume's really great, isn't he?"
    r "Those plant powers of his are ridiculous! He’d better not hold back in training me! I’m gonna take him down one day, with a left jab of fire right in his face--"
    
    ro "Yes. Indeed. He...his plant abilities are something. I’m going to head to bed early. Good night."
    
    "...was it something I said?"
    
    r "You sure you’re okay? I mean, I’m not really good at feelings and all that girl stuff, but I got ears."
    
    ro "You promise you won’t say a word to anyone?"
    
    r "C’mon Roman, I’m not a snitch!"
    
    "Roman doesn’t look like he trusts me that much. Which I guess makes sense."
    
    ro "All right. Soume’s supposed to be my partner, but he makes me awfully nervous."
    "I’ve known him a pretty long while, since the first day I came here, and I don’t feel as if I know any more about him now than I did then."
    
    r "He's a little out there, but he seems like a nice enough guy. He might just be really private, you know?"
    
    ro "I feel as if there’s something I’m missing, that’s all. It’s rather difficult to fight beside him."
    
    r "Difficult? Are you kiddin’? He’s INSANE in battle!"
    
    ro "Believe me, I’m more than well aware of his prowess. He’s...so far above anyone I’ve ever seen. It’s unreal. He hasn’t been flustered in a single fight we’ve entered." 
    ro "I’m stuck in back, unable to call a weapon to save my own skin and he’s casually sauntering along while our enemies are falling around him. It’s fascinating, intensely so, but..."
    
    r "It makes you look pretty bad?"
    
    ro "That as well. I’m in awe of him. He can heal, and he seems to have complete mastery over all plant life. It’s more than amazing...it’s dangerous."
    
    r "But that's a good thing, right? The bad guys will get what’s coming to ‘em."
    
    ro "For...um. Your own training. Did he do the surprise test?"
    
    r "Oh, the pollen thing in your face? Yeah."
    
    ro "That’s not quite how it went for me..."

label Scene19:
    #play sound Sound of weapons clashing.
    #Roman makes martial arts cries.
    ro "HIIIIIIIIIIIYAH!"
    
    s "Very good, Roman-kun. I think you're ready for your first sparring session."
    
    ro "Sparring? I can hardly stand up straight..."
    
    s "Our enemies won't have the courtesy to wait for you."  
    
    ro "Right."
    
    s "Call your best weapon."
    
    #show cg Rikupower with fade
    
    "Soume stands still and watches, fiddling with some seeds in his palm."
    
    s "Very good. Now come at me with the intent to kill, and don’t stop until I am dead."
    
    ro "Wh-what? I can’t do that! You’re my friend! And you’re the best we’ve got..."
    
    s "Which is all well and good, but you will never be able to kill your enemy unless you attack them with the intent to do so."
    
    ro "I don’t think---"
    
    s "Try."
    
    ro "Well...okay...here goes!"
    
    #play sound Sound of footsteps running 
    #play sound Roman’s battle cry. Sound of flesh being punctured.
    
    ro "Oh god! Soume--you didn’t dodge! I thought you would--"
    
    s "Hn."
    
    #play sound Sound of more flesh getting punctured.
    
    ro "Aah--"

#* * * * *

label Scene20:

    r "...ow. He ran your hand through?"
    
    ro "It’s completely healed, not even a scar, but...I didn’t see it coming." 
    ro "I called my attack, and he merely had a flower in his hand and the next thing I knew I was laid flat, about to be run through by a bunch of sharp vines."
    
    r "...cool."
    
    ro "What do you mean, ‘cool’? That’s positively frightening!"
    
    r "I dunno him or you like, at all, but I don’t think he meant to be mean.The guy talks to freakin’ plants. It’s probably one of those adult-lesson things that you don’t get until you have to use it."
    
    ro "I know. He’s never even done it again. He just...at the time...I was really afraid he might kill me."
    
    r "Roman, PLANTS. WHOLE CONVERSATIONS with them."
    
    #Roman gives a resigned laugh.
    ro "I know. I’m being silly."
    
    r "If it bugs you, just talk to him about it. Might help your teamwork."
    
    "Maybe Soume wouldn’t’ve picked on him if he didn’t show enemies his whole fuckin’ deck before a fight. Ain’t nobody pickin’ on ME here."
    
    ro "You’re right; I apologize. I’m just overthinking it. I’ll talk to him."
    
$ decision = "2"
menu:
    "Search.":
        call show_map
    "Sleep.":
        call sleep
    
label Scene22:

    "If there’s one thing I’ve noticed, it’s that I get much better sleep here. I haven’t had that wacky dream in a while."
    
    "I’ve also sort of been forced to quit my vices...there’s nowhere to buy smokes, and I haven’t yet been able to find any liquor, not even for shrine ceremonies!"
    "What kind of old lady doesn’t have alcohol around?"
    
    "Bet she’s hiding it in some secret cupboard or something."
    
    #play sound Sound of birds chirping.
    
    su "GET THE FUCK OUTTA BED YOU LITTLE SHIT!"
    
    r "GAAAAAAAAAH!"
    
    "Something’s trying to crush my skull. This is it--I’m gonna die; it’s---"
    
    "---it’s the tiny foot of a freakishly strong old lady stomping on my head."
    
    su "I SAID GET THE FUCK UP! YOU GOT CLEANING TO DO, YOU UNGRATEFUL FREELOADING LITTLE FUCKER!"
    
    r "I’m up, I’m up!"
    
    "I throw on some clothes and head out to the grounds. Everyone else is already there, scrubbing away. Susa shoves a broom into my hand."
    
    su "Stick your eyes back in your damn skull and get some work done!"
    
    "Is this bit--bat kidding? The sun’s not even up! I’m barely awake enough to keep my eyes open, nevermind clean!"
    
    su "If there’s one goddamn thing I hate, it’s when fuckin’ brats come onto my land, squat in my shrine, eat my food, drink and wash their nasty asses in MY water, and then don’t do a damn thing!"
    
    r "Nnngh. You’re in extra rare form this morning..."
    
    su "Okay everyone, training exercise. Beat up the new kid! First hit in gets no cleaning duty for a week!"
    
    "Everyone suddenly stops brushing and turns to me, at attention."
    
    r "Wai-wai---WHAT?"
    
    r "AAAAAAAAAAAAAAAAAAAAAGHHHHHDLFS--"

label Scene23:
    r "Ow ow ow ow..."
    
    ro "Wasn’t this morning’s training exercise invigorating, Riku?"
    
    r "Yeah, yeah, sure. I can’t believe I’m still alive to DO evening training. The people here are more brutal than I thought."
    
    ro "Yes, but you enjoy this sort, right? The elemental training."
    
    r "It’s the only reason I put up with that ol’ biddy."
    
    #Roman laughs.
    ro "Ahaha."
    
    s "Welcome, you two."
        
    ro "Hey Soume!"
    
    r "I hope you’re teaching us something good tonight!"
    
    s "Ahhh, you wound me. Do you not love my teaching every evening?"
    
    r "You kidding? My fingers are numb after all that!"
    
    s "I’m afraid they’ll only be moreso tonight. This is a sparring lesson."
    
    ro "Eh?"
    
    r "For serious?! FINALLY! I get to throw fireballs---"
    
    s "Riku-san, you haven’t learned that yet. Even just manifesting fire is a difficult task..."
    
    r "Yeah, yeah."
    
    s "Roman-kun, why don’t you show me your own latest manifestation?"
    
    "Roman flushes, and when I think about it, I realize that the entire garden smells especially wonderful tonight. The air is so crisp and clean...I never thought it could be this wonderful just to breathe."
    
    ro "It’s...not much of anything..."
    
    s "Please. Show Riku where he may soon reach in his elemental control."
    
    ro "All right...I guess..."

#label minigame Manifestation
    #  "Lesson 2: manifestation. One must keep a steady stream of ki to manifest properly. The difficulty then comes in holding that 
    # perfect balance and keeping it for an extended period of time at its full power to use as an effective weapon."
    #  [Minigame here? Focus Riku’s ki into a steady manifestation of his fire power and hold it for as long as you can. Instructions------]

#label manifestation fail:    
    #This section if you fail one level in the minigame.
    s "That's alright. Try again. This is very difficult."

#label manifestation success:    
    #This section if you succeed one level in the minigame.
    s "Good, excellent work!"
    
    "For all the sensitive whining Roman does, he’s grinning like a fool at Soume right now."
    
    "We work on it until bedtime."
    if Scene21:
        jump Scene25
    else:
        jump Scene26
label Scene25:    
    s "Roman-kun, would you mind staying a bit late to chat with me?"
    
    ro "Ah...sure, Soume, whatever you’d like."
    
    "Hm. Didn’t invite me. Though that doesn’t necessarily mean anything..."

menu:
        "Eavesdrop.":
                jump eavesdrop
        "Stay out of it.":
                jump stayout
                
label eavesdrop:
    "I stick around to listen in for just a bit. No harm, no foul, right?"
    
    s "You did really wonderfully today, Roman."
    
    #show ro flush with fade
    ro "I--thank you. It means a lot, coming from someone like you..."
    
    s "Please, I’m not worth flattering."
    
    ro "What are you talking about? You’re amazing. I think so, Miss Susa thinks so...even Riku thinks so. He told me himself."
    
    s "Roman...I..."
    
    ro "What is it, Soume?"
    
    s "I wanted to apologize for one of our earlier training sessions. I didn’t realize that I’d scared you. I don’t want to do that; I want us to be friends. I’ve...never had a real friend before."
    
    "This is getting sappy."
    
    #show ro flush with fade
    ro "Ah--it’s okay. I was just overthinking...I’m already over it. It’s nothing."
    
    "Is it just me, or does the air smell really wonderful?"
    
    s "I merely wanted to beg forgiveness. I...the shrine’s been going through some things lately...I lost a lot of very close friends and partners because they weren’t trained well enough. 
    I didn’t want you to be the next one..."
    
    ro "Riku was right. He figured it was just like that. Don’t worry about it. I’m fine, and I appreciate it very much."
    
    s "I’m glad to hear it~ No more secrets from me, little one, all right?"
    
    ro "Eh...no...of course not!"
    
    "Yeah...the air smells really, really beautiful..."
    
label stayout:
    "If I eavesdrop, and that rabid bat catches me, I’m screwed. Better to just move along."

label Scene26:

    su "Oi. You. Doctor’s visit."
    
    r "Uhhh, my parents are my doctors, and I shouldn’t see anyone else..."
    
    su "Idiot. He’s a Majin doctor. Like I’d let you see one of those surgeon hacks they got in hospitals."
    
    r "...right."
    
    su "Anyway, it’ll be your first real check-up, so get your ass downstairs. And you better listen or I’ll have your fuckin’ hands pinned to the wall. With nails."
    
    r "Yeah yeah yeah..."
    
    su "Got somethin’ ta say, punk?"
    
    r "No, ma’am! Just making sure I don’t screw it up, ma’am!"
    
    #play sound Punch
    
    r "Ow..."
    
    su "Don’t take an attitude with me. Get your ass down to the library, before I hurt you even worse!"
    
    "Can’t she take a joke?"
    
    "I head down the stairs. The basement is pretty deep; there’s a locked door and a broad library and lab down here. It’s a giant dusty mess, books and papers and scribbles everywhere."
    
    #play sound Books falling to the ground, dust making loud noises, papers crinkling all over.
    
    r "WHOA!"
    $ Kazutaka = "Uptight Man"
    k "You there, child! Have some more cognizance! You nearly destroyed my research!"
    
    r "Your “research” nearly crushed me!"
    
    k "Is that so? Ah well, no harm done."
    
    "What an as--mean...guy. I hate this no cursing rule."
    
    r "Uh...excuse me?"
    
    k "What IS it? Can’t you see I’m busy? I have a lot of experiments to finish, and there’re the updates to write, and the spores to add to the inoculum..."
    
    r "Miss Susa sent me? For the doctor?"
    
    k "Hm."
    
    r "...so...?"
    
    k "I am \"Dr. Osamu Kazutaka.\" You must be Riku...I should’ve told by your stature, the way your jaw is so positively narrow. Barely above an infant, I’d wager."
    $ Kazutaka = "Doctor Osamu"
    r "You always this great with patients?"
    
    k "Enough speech. Come, sit up here."
    
    r "...on the library desk?"
    
    k "Would you prefer the dissection desk? I haven’t disinfected it yet...there may still be some virulent strains of the ebola virus lingering..."
    
    r "...here’s great."
    
    k "Excellent. Stay still."
    
    "He pulls out a stethoscope and examines me from head to toe, murmuring and taking notes."
    
    r "What’re those notes for?"
    
    k "That’s classified information."
    
    "I really do not like this guy."
    
    k "All right, you are hereby given a clean bill of health. But, to make sure it stays that way, take this literature on Majin, your species type, and our enemies."
    
    $journal.unlock_entry("Majin", "050")
    $journal.unlock_entry("Church of the Three Acts","039")
    $journal.unlock_entry("Church of Three Acts", "040")
    
    r "My...species type?"
    
    "He stares at me blankly."
    
    k "Well obviously we’re not all one singular species. The Majin race is built up of multiple species and subspecies...very fascinating, really. The differences are so vast and yet---"
    
    r "Uh, yeah, sure, whatever."
    
    k "You know nothing about anything, I presume."
    
    r "Hey, I know what’s IMPORTANT, alright pal?"
    
    k "DOCTOR. At ALL times."
    
    r "WHATEVER."
    
    k "I’ll have you know that the things written in that research are potentially vital to your survival as a Majin in the human world."
    k "The Church of the Three Acts may seem kindly on its surface, but the underbelly is worse than a rotted apple with red skin."
    
    "I decide to hold off getting pissed for a minute."
    
    r "They seem pretty cool...always having some kind of fundraiser, or feeding the poor, housing the homeless...stuff like that."
    
    k "Oh, well, it is very easy to gain the money to do great things when you are selling our kind into slavery and onto dinner plates, I suppose."
    
    #Riku chokes.
    r "WHAT?"
    
    k "Nothing about anything, as I feared."
    
    k "Ugh. I do NOT know why Miss Susa insists on bringing little miscreants like you in. You all just cause trouble." 
    k "No better than humans, really. Listen carefully, child. Don’t assume that anyone is on your side." 
    k "The things that humans will do to a Majin could make your blood curdle in your veins and stink of the subsequent fermentation."
    
    r "They...slavery? Wouldn’t we have heard of it?"
    
    k "Would you, prior to us finding you, have believed in the slavery of a mythical being unless you saw it with your own eyes?"
    k "Would your friends? Your family?"
    
    r "I guess not."
    
    k "Those people lure in humans, and not just any ones—humans with special abilities, like Miss Susa. The ability to hunt our kind down."
    
    r "Special humans?"
    
    k "The Church of Three Acts is a front for a small society of humans far beyond the capabilities of the normal...their strength, speed, agility and physical prowess are much more similar to Majin."
    k "That is why they are able to capture us and hold us." 
    k "With that front, they maintain political power as well as their wealth, and with their physical strength and superior numbers, their job is easy." 
    k "On occasion, they’re able to just lure our people in. Many of us have defected to that side...just for the peace of mind."
    
    r "...they’re like...some kind of freako cult. Why doesn’t anyone do anything?"
    
    k "Idiot. You didn’t know Majin existed before you were told. That’s why humans do nothing about the suffering of our people. No one knows about it."
    
    r "Well, we could expose it...we could do something---"
    
    k "And be killed for our trouble? Or risk the humans mass-condoning their behavior because we aren’t them, and they think THEY are the masters of this world?"
    
    r "But...not everyone’s like that..."
    
    k "Well then. Please feel free to forfeit your life for the rest of us. As much as you think you’re human, child, you are not. Human justice only applies to you if they believe you to be human."
    
    r "…"
    
    k "You’ll learn eventually. Now please remove yourself from my library. Your ignorance is starting to leak everywhere."
    
    "Oh, screw that guy. What an as---a grump. Still, what he says sticks with me. Human laws only apply to humans?"
    $ decision = "3"
    
menu:
    "Search.":
        call show_map
    "Sleep.":
        call sleep
    "Research.":
        $show_message("From now on, you will be allowed to research with Kazutaka.", "medium")
        $show_message("You will be able to learn a lot about the world from the information you receive here.", "medium")
        call research_loop
        $journal.unlock_entry("something", "031")    

label Scene27:

    "Mmm, no sign of the witch this morning. Place isn't too dirty, either. No one will miss me if I watch a little TV instead of cleaning up..."
    
    #play sound Sound of someone getting smacked
    
    r "OWWWW!!"
    
    su "You miserable little shit! Did you really fucking think you could get outta cleaning duty?"
    
    r "I’m sorry--agh!"
    
    su "You WILL be sorry, you worthless runty little fuck!"
    
    "Something really hard and painful breaks right over my head."
    
    su "--fuck! Now look what you did! That’s my fucking Hunt Duck gun and your fucking hard head broke it in two!"
    
    r "Remind me again how -I- broke it?"
    
    su "Listen here you piss stain, when I’m not yelling at you shits, I’m playing video games. If I’m not playing video games, I’m yelling at YOU SHITS. Got it?"
    
    "Ouch. Now it's in three pieces.  She's got a good throwing arm."
    
    r "...crystal clear."
    
    su "Good. I’ll be expecting you to buy me a new one. NOW CLEAN ALL THIS SHIT UP!"
    
    "I just wanted to watch some television..."

label Scene28:

    #play sound phone ringing
    
    #Roman sighs here.
    ro  "..."
    
    # play sound phone ringing
    
    ro  "I hope I haven’t missed her again. It is rather late, but--"
    
    l  "Roman?"
    
    ro  "…Liza?  How did…?"
    
    #Liza gives a gentle laugh.
    l "I may be old for the humans, and you, but I am quite proficient with modern technologies."
    l "This Caller Identification thing is very useful. Besides, you’re the only one who ever calls me this late. Most know better."
    
    #show ro flush with fade
    ro "I-I’m terribly sorry. It’s just with training and-"
    
    l "It is nothing, as I’ve mentioned before. I adore hearing from you."  
    
    ro "R-right. Of course. I was just afraid, since you’re used to a strict schedule..."
    
    l "Nonsense! It is barely past nine. Not all of us require as much sleep as you do, Roman."
    
    #hide ro flush with fade
    #show ro smile with fade
    ro "Only to keep my strength up!"  
    
    l "So, how are things at the rescue? How is training and all of that?"
    
    ro "To be perfectly honest, I can’t imagine things going much better! My skills have improved tremendously since I’ve arrived, and things with…uh…well, things are great all around."
    
    l "Excellent! I’m happy to hear that."
    
    ro "That’s actually why I called. I just…well, I wanted to thank you. Again. I mean, for helping me find the rescue." 
    ro "Without you I don’t know what would have happened to me. I’m not sure I can express how--"
    
    #Liza laughs.
    l "You owe me nothing, Roman. I merely led you to someone I knew could help."
    
    ro "But-"
    
    l "But nothing. Everything I’ve done was because I wanted to, not because I was doing you some favor. If you bring it up again, I can’t promise to listen."
    
    ro "But-"
    
    l "I’m not joking about ignoring you, Roman~"
    
    ro "Fine! Have it your way, then. But you can’t stop me from thinking it."
    
    #Liza laughs
    l "Spoken like a true child. How is your life otherwise? How is…Susa doing?"
    
    ro "Oh, she’s the same as always. We recently rescued a boy, Riku. He’s just a baby, really, and there’s quite the wild streak in him. It has taken a lot of the focus off of the rest of us!"
    
    l "Oh?"
    
    ro "Just a little bit ago he tried to sneak out of cleaning duties and decided he was going to watch some television. Right in the middle of the lounge!" 
    ro "Of course, Miss Susa found him, and she was so irate she broke her video game things right over his head." 
    ro "Majin might heal fast, but he had quite the lump on his head."
    
    #Liza gives nostalgic laughter.
    l "I would say that sounds just like her."
    
    ro "I hope I’m not intruding, but you really should stop by."
    
    l "...hm?"
    
    ro "To visit her, I mean. I’m sure she would be quite happy to see you and-"
    
    l "Yes yes, of course. And how is that youko?"
    
    ro "E-excuse me?"
    
    l "The youko, Soume? How have you two been getting along? You’re his partner, aren’t you? Usually our conversations are all about him."
    
    ro "I-I’m not sure I understand what you’re getting at."
    
    #Liza: Very solemn
    l "Ah, mm, well, we should get to dinner some time, one of these days. I might be coming into the area soon."
    
    ro "What a wonderful idea. You must remember that I would need a vegan option at the restaurant, but beyond that-"
    
    l "Vegan? Roman, you can’t mean that silly notion that you mustn’t eat meat--"
    
    ro "I assure you that this isn’t some phase I’m going through. I decided to become a vegan long ago and I can’t imagine ever deviating from my diet."
    
    l "Roman, it’s unnatural for Majin, and likely to be very harmful. Please, I know a very good place; they will cook a lovely veal for you--"
    
    ro "Veal? That’s baby deer, isn’t it? I couldn’t."
    
    l "If you insist..."
    
    ro "I do. I’m not even sure how you could eat a poor young thing..."
    
    l "Mmm...on average, I start with the heart, and then move on to its hopes and dreams for the future."
    
    ro "…that is not funny."
    
    l "Roman, I do believe you’ve taken on my penchant for being too serious..."
    
    ro "Oh goodness. That isn’t a good thing."
    
    #Liza chuckles.
    l "I’m afraid not."
    $ journal.unlock_entry("Liza", "031")

label Scene29:
    #play sound Forest medley
    
    #Girl pants and breathes heavily in terror.
    gir "Run. Must run."
    
    "Lungs feel ready to explode. Don’t know how long I’ve been running. Can’t stop. He’ll--"
    
    gir "Please. Oh god."
    
    "Too afraid to look back. I saw what…what happened to Saadira. What that monster did to her."  
    
    gir "Ugh…nnnngh."
    
    "Only pieces of her left. Blood everywhere. Arm was down to the bone. Not much more of the leg. Could only tell it was her because her head was left largely in tact."
    
    "Not much flesh to get off that, I guess."
    
    gir "Our Father, who art in…Ngh. Shit shit shit shit shit."
    
    "Couldn’t even pretend to be religious. Saadira was the one who went to church, like those fucking human gods were worth anything. Some good it did her."
    
    #Girl starts crying quietly.
    gir "Why? Nnnn….why!?"
    
    "Church of Three Acts. I was supposed to pick her up from it tonight. She never showed. Searched everywhere.  Finally found her. Most of her."
    
    gir "No, please. Please please no."
    
    "He’s back there. I know he’s back there. He saw me. He looked up from Saadira and saw me. And in his eyes…I saw-"
    
    #Girl is trying to catch her breath.
    gir "Huff…nnnnngh."  
    
    "I saw-"
    
    gir "Grgh….errrrgh…"
    #Girl shrieks.
    
    #play sound crashing noises
    
    m "Hello, Audra." #Her name in Japanese A-u-do-ra.
    
    "Hunger."
    
    a "NO! HELP!!! SOMEBODY HELP!!!"
    
    m  "Now that’s just silly. You’re the one who ran us right into the middle of the woods. Who’s going to help you out here? Some benevolent possum? A squirrel in shining armor, perhaps?"
    
    "He smiles. Little dark, curly hairs are stuck between his teeth. Saadira’s."
    
    m "Hm?"
    
    "He catches me staring. Starts picking at his teeth."
    
    m "Hn. How unseemly. I wasn’t even able to clean up properly after my last meal. What’s the phrase...cleanliness is next to godliness?"
    
    a "No...just leave me alone...let me--"
    
    m "But I came all the way out here to see you, Audra. Is that any way to treat a guest?"
    
    a "Please…pl-please. I-I’ll give you anything. I’m special. I-I-I-"
    
    m "You you you."
    m "Contrary to anything you think, my dear, this isn’t about you, nor is it personal." 
    m "And I already know what you are. I’d hardly consider you special. Your sister told us everything..."
    $renpy.pause(2.0)
    m "You're mediocre, at best."
    $renpy.pause(3.0)
    m "Your lives have beeen hard, haven't they?"  
    
    #Audra is whimpring in terror.
    a "No...no..."
    
    m "I’m really only doing you a favor."
    
    a "STOOOOOOOOOOOOOOOOP!!!"
    
    #show screen flash 
    #play sound lightning
    
    m "Oho. That stung a bit."
    
    a "Please…"
    
    m "Hehehe."
    m "It seems I was wrong."
    m "You are more special than I thought."
    
    a  "NOOOOOOOOOOOOOOOOOOOOOOOO!"
    
    #play sound scary noise medley
    
    m "Special indeed."
    
    #show screen flash 
    #play sound lightning
    $ decision = "4"
menu:
    "Search.":
        call show_map
    "Sleep.":
        call sleep
    "Research.":
        call research_loop
        $journal.unlock_entry("something", "031")    

label Scene30a:

    "Time passes, blah blah blah."
     
    "This place has almost started to feel like home. Well, if your home was inhabited by a demon that violently assaulted you every morning."  
    
    "I still talk to my parents a lot. Not that I’m homesick or anything. It…it’s more for their sake than mine."
    
    r "Yeah, I just got the package. That’s why I was calling, actually. I wanted to thank you."
    
    ma "Great! Did you like it?"
    
    r "Uh…well, I haven’t opened it yet. Guess I got too excited."
    
    ma "What? Are you feeling all right?"
    
    r  "Yeah, I feel fine. I mean, I’ve got some bruises, but-"
    
    ma "BRUISES?"
    
    r  "Yeah, but-"
    
    ma "From who? Are you being bullied by one of your classmates?"
    
    r  "Not exactly… Um, you know what? Sure. One of my classmates. That’s it. Everything is fine now though, so don’t worry."
    
    "Better that than telling her the bruises are from the woman running the place."
    
    ma "Oh good. I’m glad you’re making friends. How is everything else? How is, uh, training going?"
    
    r "Awesome! I--am not supposed to really talk about it, but it’s the coolest stuff ever!"
    
    ma "Oh, I see. Well, that’s good. You seem to really like it there."
    
    r "It’s got its problems and stuff, but I do like the place. When they let me go home, I’m gonna show you all the neat tricks I learned."
    
    ma "When...when will they let you?"
    
    r  "Oh--"
    
    "Damn. I don’t have a clue. Could be a long time."
    
    r "It’s...not yet. It’s not safe yet."
    
    ma "Oh. O-of course. But I’m sure it will be soon."
    
    r "Yeah. Soon. I-I have to get going. Training and all that."
    
    ma "Right. Call again as soon as you can, okay? I love you."
    
    r "Love you too, Mom."
    
    "You might think that thing in the corner of my eye is a tear. And you’d be wrong. That’s...man sweat. Manly, he-man sweat, in fact. From…lifting heavy stuff."
    
    "I never did get around to checking the package, though. Inside, there’s an envelope and a box."
    
    "Which should I open first?"
menu:
        "Open Envelope.":
            jump Scene30
        "Open Present.":
            jump Scene30b

label Scene30:
    "Might as well see what’s in here. Probably some sappy card Mom got from the store. Never read these things, but-"
    
    r "Whoa."
    
    "That’s a lot of money. This is way better than a card."
    
    r "Oh, I think it’s time I got some new clothes! Maybe treat myself out to a night at the bar. Or-"
    
    su "That’s my fucking Hunt Duck gun and your fucking hard head broke it in two!"
    
    su "I’ll be expecting you to buy me a new one."
    
    "Ugh. Fuuuuu…fudge. I completely forgot about the old crab’s stupid toy gun. I guess I could use this to get a new one. Or I could just blow it on liquor and other junk I actually want. Hmmm…"

menu:
        "Use money on yourself.":
            jump badend2
        "Agree to purchase Susa a new gun.":
            jump Scene30_1
            
label Scene30_1:
    r  "Ugh. Can’t believe I’m going to do this."
    
    "Just so you know, I'm doing this because I feel like it. Not because I owe her. Not cause I’m afraid of her, either. It’s just…uh, screw it, I AM afraid of her."
    jump Scene32
label Scene30b:
    "I’m opening the box first. Envelopes are for chumps."
    
    "The scent creeping out and working its way through my nose means only one thing: Mom got me a cake."  
    
    "It’s a fucking strawberry shortcake. It’s the biggest fucking strawberry shortcake I’ve ever seen. I might actually manage to leave some until tomorrow!"
    $inventory.unlock_item("cake")
    
menu:
    "Share cake with Soume and Roman.":
        jump Scene31
    
    "Eat by yourself.":
        jump Scene30c

label Scene30c:
    r "What the heck was I thinking? This is the first treat I’ve had since I got here. Let THEIR parents send THEM cake."
    $hp+=20
    $mp+=20
    jump Scene32

label Scene31:

    ro "Mm, is the cake vegan?"
    
    r "Duh, of course."
    
    "Why would my mom put meat in a cake, anyway?"
    
    ro "Oh, that’s so lovely of your mother. And mm--this is positively wonderful! Please tell her I said thank you. It is delicious."
    
    r "Don’t mention it. Figured it was the least I could do, y’know? Considering you two saved my life and all."
    
    "Roman is grinning from ear to ear. He’s taking these small bites and smacking his lips all loud between each one.  I’d say he looks strange, but compared to Soume that would be nearly impossible."  
    
    #Soume is speaking to himself, here.
    s "Hmm…maybe if I just…no no no."
    
    "I gave him the cake like twenty minutes ago. I’ve already finished like six slices, Roman’s had at least four, but Soume’s spent the entire time eyeing it like he’s trying to figure out the best plan of attack."  
    
    r "You gonna eat that, man? S’not poisoned or anything."
    
    #Soume giggles.
    s "Of course it’s not. I distinctly know poisoned food when I see it. It gives off such a...hm. I’m not sure how to describe it, exactly...it’s a very...bemused smell."
    
    r "...huh?"
    
    s "Oh, you know! Bemused-smelling."
    
    ro "Wait--the smell is confused?"
    
    s "Absolutely!"
    
    ro "Er, I don’t think..."
    
    s "I’m not sure how else to describe it really...it’s a bit specific."
    
    #Roman laughs.
    ro "Oh, of course! I imagine it must be!"
    
    "You’re probably confused by now, but long story short: Soume’s a weirdo and Roman’s a suck-up."
    
    r "Well, are you gonna eat the cake or not?"
    
    s "Ah. Yes. Indeed. Mmm."
    
    r "…and? What you think?"
    
    s "Mmm. Mmmmmm. It’s different. I don’t think I’ve tasted anything quite like it."
    
    r "Uh...sure."
    
    s "Mmmm."
    
    r "Are...you okay?"
    
    s "It seems I will be. I’m not sure what I was worried about..."
    
    #play sound  Gurgling
    
    r "What the f--heck was that?"
    
    ro "Maybe Miss Susa is running the sink disposal?"
    
    r "Nah, that isn’t what it sounded like. It was more of a-"
    
    #show so ill with fade
    s "Nnnnnngh."
    
    ro "Soume, are you all right?"
    
    #play sound  Stomach gurgling.
    #show so sweat with fade
    s "Ah. Er. Yes. F-fine. I feel f-fine."
    
    #play sound Stomach gurgling.
    
    s "If you’ll er--e-excuse m-me. I n-need to…um. I’ll be back in a m-moment."
    
    #play sound  Footsteps running off.
    
    r "Think he’ll be okay?"
    
    ro "I certainly hope so...I’ve never seen him do that before..."
    
    r "Well, I’ve never seen him move that fast ever, so I doubt he’s gonna die."
    
    ro "His stomach is quite sensitive. I was rather surprised he took your offer at all."
    
    r "Oh--hm, y’know, I don’t think I’ve ever seen him eat. Like, since I got here."
    
    ro "I have, but it’s never much, and he rarely accepts food from others."
    
    r "Maybe he photosynthesizes his food! Like a plant!"
    #Roman laughs.
    
    ro "I don’t THINK he can do that, but he does drink an awful lot of water."
    
    r "See!"
    
    #Roman chuckles.
    ro "I think it’s more likely that he has a special diet. Some here do. I don’t see Miss Susa eat much with us, either."
    
    r "Oh, well I hope he isn’t sick because of this stuff. It’d suck if he was like, lactose intolerant or allergic to sugar or something."
    
    ro "..."
    
    ro "Excuse me?"
    
    r "I mean, if he was I wouldna offered him these in the first place. I’m not that cruel."  
    
    "Roman starts turning the same green color. What? Majin can’t have freakin’ cake?"
    
    ro "Do these…have milk in them?"
    
    r "Milk? Mmm, I doubt it."
    
    ro "Oh, thank heavens. You had me concerned for a moment."
    
    r "I think Mom said the bakery uses straight cream for these things. Makes them really rich. S’why it’s so good."
    
    ro "CREAM!?"
    
    "I think that’s the first time I’ve heard Roman raise his voice. Well, not counting the time he was screaming like a baby during the fight with Mamoru."
    
    r "Uh…yeah? That’s how you make a cake?"
    
    ro "FROM A COW?"
    
    r "Where the hell else does cream come from!"
    
    ro "RIKU, I’M A VEGAN!"
    
    r "Yeah, you told me. So?"
    
    ro "So? SO? Don’t you-I mean-what is…how can…DO YOU EVEN KNOW WHAT IT MEANS TO BE A VEGAN?"
    
    r "I’m not STUPID, Roman. It means you don’t eat meat or fish or whatever, right?"
    
    ro "What? WHAT?  NO! It means I don’t eat animal products!"
    
    r "...so...?"
    
    ro "Or things produced by animals!"
    
    r "...right..."
    
    ro "CREAM IS PRODUCED BY ANIMALS!"
    
    r "...ohhhhh. I didn’t even think of it like that."
    
    ro "RIKU!!!"
    
    "Roman runs off in the same direction as Soume. I can hear him gagging as he practically gallops to the bathroom."
    
    r "…this is the last time I share my food with ANYONE."
    
label Scene32:
    $ decision = "5"       
    menu:
        "Search.":
            call show_map
        "Sleep.":
            call sleep
        "Research.":
            call research_loop
            $jourhnal.unlock_entry("something", "031")   
label Scene32a:

    "Really, really hate wakin’ up early. If the sun doesn’t fucking have to be up at this time, why do I?"
    
    "Training is the only thing about it I can stand. Still, kind of hard to focus on Soume when my body is pissed at me for forcing it to clean for the past four hours."
    
    "I’m a little late today, but I’m sure Soume will forgive me. I’d rather cross him than Susa, anyway."
    
    s "Why helloooooooo! I almost didn’t see you there!"
    
    r "Hey Soume. Sorry I’m late, I just-"
    
    s "You don’t look like you’ve been getting enough sun. You’re far too teeny~"
    
    r "I ain’t TEENY. I’m at least as big as the other trainees my age!"
    
    s "Let me just move you over here! Mmm, perfect! So much more sun without those other plants hogging it all~! This is just what you need!"
    
    "Oh, he’s talking to those damn plants again. I should’ve figured."
    
    r "Hey! Soume!"
    
    s "Oh, Riku! Sorry, I was tending to my plants. Say hello to Ku-chan!"
    
    "Soume is motioning to the smaller flower he just moved. I stare at him for a minute, but it becomes clear that my training isn’t going to continue until I talk to this damn plant."
    
    r "Uh…hi?"
    
    #Soume giggles
    s "No need to be shy, Riku! Ku-chan won’t bite! At least, I don’t think he will...the plants have been so terribly antsy lately..."
    
    "I really hate when I can’t tell if Soume’s joking or not."
    
    "Especially since Ku-chan has teeth. Sharp teeth. Even though it’s just a small plant, I don’t think I’d want to get my hands anywhere near it."
    
    r "So, training today? What are we doing?"
    
    #show so grin with fade
    s "I think you’ll like this exercise."
    
    r "Really, what am I doing? Shooting fireballs yet?"
    
    #hide so grin with fade
    #show so frown with fade
    s "Ohhhh, did Roman tell you? I told him not to, but-"
    
    r "Wait, really? I am?  I’M GOING TO SHOOT FIREBALLS?"
    
    #hide so frown with fade
    #show so grin with fade
    #Soume giggles.
    s "You’ve been progressing nicely, so I thought it might be a good idea..."
    
    r "Awwwwwwwlright! I thought I was ready, you know? Cause I did pretty good at that other exercise, you know? I think I can do it without, you know, blowing myself up."
    
    s "Oh, it’s very probable!"
    
    r "…huh?"
    
    s "It’s probable. That you won’t cause yourself to combust, I mean. Likely, even!"
    
    r "You’re not helping my confidence here."
    
    s "You’ll be fine! You can channel your Youki even with distractions and hold it for several hours. By all measures I can think of, I could say I’d even be surprised if you failed along that measure."
    
    r "Maybe I should practice channeling more..."
    
    #Soume giggles
    s "No, I think you can handle it. Come now!"

#label minigame3:
    #Lesson 3:  Projection. Now that you can channel your Youki and keep a steady stream of ki, it is time to start utilizing your powers in a tangible way. Focus on your target and project your energy onto it. 
    #Make sure not to lose focus—if you deplete your Youki, you will not be able to do anything!
    
    #[Put in a minigame here?  Maybe some sort of target practice minigame, where you need to hit certain targets while avoiding others?  
    #Some secondary mechanic can be used to replenish Youki levels, possibly something similar to the first minigame.]

#label projectionfail:    
    r "Eh. This is harder than I thought it’d be…"
    
    s "Remember, r focus. In the heat of battle, you need to be able to distinguish between friend and foe."
    
    r "Right, right."
    
    s "I’d rather not be cooked by your flames, if that’s possible...I’m just no good with that much heat..."
    
    r "Okay, okay! I’ll get it this time!"
    
#label projectionsucceed:
    r "YES! WOOOOOO!!!"
    
    #Soume giggles.
    s "Excellent, Riku! I knew you were ready."
    
    r "Did you see that?! Did you see that?!"
    
    s "Yes, I did! My, you’re excitable."
    
    r "FLAMES! FLAMES OUT OF MY HANDS!"
    
    #Soume giggles.
    s "Indeed, it is rather impressive. You must remember, though, Riku..."
    
    "Uh-oh. There’s ALWAYS a catch to the good stuff."
    
    s "Your abilities, my abilities, the abilities of everyone in here—the Youki—that’s what gives us away to our enemies. They will find you by the signature of your fire alone. You must be careful."
    
    r "But you have plants all over! Wouldn’t that give us away?"
    
    s "You will learn how to exert the smallest amount of power for maximum effect, as well as mask your energy signature. But, that takes quite a few years of study."
    
    r "This stuff is harder than I thought it would be. On TV, the main character is already totally cool and powerful!"
    
    "Soume is making a face. He’s about to say something...Soume."
    
    s "That’s quite unrealistic and irresponsible of the television people..."
    
    ro "Sooooumeeeeee..."


label Scene33:
    "Time when you’re demon training goes pretty fast. Soume says I’m a natural, and we’re done with all the boring little stuff...finally."
    
    "Training today is supposed to be extra special, Soume was practically shaking me he was so excited."
    
    "Hurt a bit actually. He’s a lot stronger than he looks, and his fingers are bony besides."
    
    "I head out to the garden."
    
    s "Oh, you have no reason to be nervous! You’ll be fantastic!"  
    
    "He’s talking to one of his plants again. I’ve gotten used to that part by now, but it still freaks me out when the plants actually move like they’re listening to him."
    
    r "Hey, Soume. What’s up?"
    
    s "Ah, Riku! You remember Ku-chan, don’t you?"
    
    "Soume is motioning to the enormous plant he was just talking to."
    
    r  "That thing is Ku-chan? It’s HUGE!"
    
    #Soume giggles.
    s "Yes! He grew quite nicely with a few tiny alterations. Isn’t he just handsome?"
    
    r "...that’s...one way of looking at it."
    
    "Ku-chan is nightmare fuel. Its head is a big, gaping, toothy mouth. Not big enough to swallow me whole, but I could easily lose an arm. Or a head.
    I definitely don’t like the look it’s giving me...and it doesn’t even have eyes!"
    
    s "Well, now that my little Ku-chan is old enough, meet your new sparring partner."
    
    r "Sparring---with THAT?"
    
    #Soume giggles.
    s "No need to hide your excitement!"  
    
    "Who’s hiding? This thing could impale me, tear me apart, and use me to fertilize its children."
    
    r "Um…don’t you have anything smaller I could start out on? Like…a daisy? Or something."
    
    #show so frown with fade
    s "Smaller...?"
    
    r  "Maybe something with less teeth...? Or even no teeth...yeah, I think no teeth, to start out..."
    
    s "No teeth? That doesn’t sound like a proper spar..."
    
    r  "Or, instead of this whole fighting thng...I could just practice channeling my energy. I never really got that, and I’d like to keep my limbs..."
    
    #Soume speaks gently.
    s "Riku."
    
    "Soume touches a hand to my cheek. A smell suddenly permeates the air, a sweet one...my face goes hot. He’s staring at me so intensely."
    
    #Riku whispers.
    r "Y-yes...?"
    
    #Soume speaks gently.
    s "You’ll be fine."
    
    #Riku whispers
    r "Okay."
    
    s "I have complete control over Ku-chan. I’d never let him seriously hurt you."
    
    "I don’t know how Soume does it, but I feel much calmer, now."
    
    r "Okay. Let’s do it."
    
    "He pulls back and slips his hand back into his sleeve."
    
    s "Besides. You’re much too scrawny for him to take an interest in eating you."
    
    r "…thanks, Soume."
    
    s "Oh, no need to thank me, really. Let me go over the basics of a serious battle with you."

label battle1:
#Lesson 4-Battle Tutorial
#Put some stuff about how the combat system works in here.

    s  "Do you understand all of that? Please let me know if I was unclear."
    
    r  "I got it. I know my way around a fight."
    
    s "Then, whenever you’re ready."
    
    #-Battle and all that. If you lose, you play again?-

label battle1vic:    
    r "Victory!"
    
    #Ku-chan whimpers
    #show p with fade
    
    s "Your progress is absolutely incredible. You’ve come so far in such a short time."
    
    r "I always knew I was cool."
    
    #Soume gives a sarcastic laugh
    s "Ah...yes. Still, you may soon surpass Roman."
    
    r "You think so?"  
    
    s "Most Majin must train for years before they are capable of channeling their energy consistently. Roman is competent, but he still has struggles with his manifestation and projection at times."
    
    #Soume mutters as if to himself.
    s "He could be so much better than he is now..."
    
    r "Well, thanks. You’re pretty good at teaching this stuff."
    
    #Soume giggles.
    s "Your flattery embarrasses me."

label Scene34:
    "Today is a day off, FINALLY. Actually, I was supposed to clean this morning,"
    
    "I think I’ve earned a little break. Doubt Susa sees it the same way, but so long as she don’t know, she has no reason to hit me. Not that she needs a reason."
    
    r "So, Roman, where you taking me?"
    
    ro "I’d rather it remain a surprise."
    
    r "Is it a bar?"
    
    #Roman chuckles.
    ro "No. Much better than a bar."
    
    r "Strip club!?"
    
    ro "What? No! Of course not! You’re much too young for that."
    
    r "Dammit, Roman. If this turns out to be a library or a soup kitchen or something, I’m gonna be pissed."
    
    "It’s my first time off the rescue in months, and Roman is making me hike through the woods. First time I’ve been able to fuckin’ swear out loud in months, too."
    
    #Roman chuckles.
    ro "You’ll have to wait until we get there."
    
    "It is nice to be out, though, and Roman is pretty cool to hang with. He’s never knocked my teeth out or had long talks with roses about their views on politics. 
    Actually, now that I think about it, I don’t know a whole lot about him."
    
    r "So...what’s your deal?"
    
    ro "Pardon?"
    
    r  "Like, what’s your story? What’d ya do before the rescue? I guess you’re a foreigner from the accent."
    
    ro "Ah…well…"
    
    "He’s hesitant. Doesn’t seem to like talking about himself, much."
    
    r "...yeah?"
    
    ro "I suppose there isn’t much to tell. I’m not terribly interesting."
    
    r "Are you kiddin’ me? You can make things out of ice. That’s pretty damn interesting!"
    
    ro "Yeah, but-"
    
    r "Anyone who can do that must have at least a couple of interesting stories."
    
    #Roman chuckles.
    ro "Fine. But do not say I didn’t warn you. I was born--ah, I guess it would be more appropriate to say I was raised in Russia."
    
    r "Russia? So you speak Russian?"
    
    ro "That, amongst other things, but Russian is my first language."
    
    r "Cool. So what about your parents? You close with them?"
    
    ro "I never knew my real parents. I was lucky enough to fall in with a few kind people, here and there, but..."
    
    "Roman looks really distant all of a sudden."
    
    r "Well...that’s good, at least...?"
    
    ro "Riku…I’m not sure you understand yet."
    
    r "Whuzzat?"
    
    ro "Do you love your parents?"
    
    "What a weird thing to ask."
    
    r "Uh…sure. They are my parents, after all."
    
    ro "What about your friends?"
    
    r "Huh?"
    
    "I can’t place the emotion on Roman’s face. Fear? Pity?"
    
    ro "It’s so difficult to become attached to humans. Their lives are so short. When everyone you know now is nearing the end of their life, you will barely have hit your adulthood."
    
    r "--a--"
    
    ro "Have you not thought about it yet? I’m very nearly one hundred years old. Soume’s at least a thousand, though he won’t say for sure."
     
    "We walk a bit without talking. I’m going to live for a very long time. And all the humans I know and love will be gone. My parents. My friends. The girl in 3A I’ve been dying to ask out."
    
    ro "…I’m sorry. I don’t know what came over me."
    
    r "Ah, no, it’s fine, I guess."
    
    ro "No--I-I was out of line. Your parents seem like nice people. I’m sure your experiences will be different."
    
    "He sounds like he wants to say something else, but I just don’t feel like it right now. Walking around in the woods doesn’t give me anywhere to go if I want to get out."
    
    r "Don’t worry about it. Really. So you grew up in Russia? How’d you end up here?"
    
    ro "Erm, a friend recommended me."
    
    r "There’s gotta be more detail than that. Who’s your friend? How’d you meet her?"
    
    ro "It’s really such a dull story..."
    
    r "I think you kind of owe me for the ‘your parents are going to die before you are even an adult yet’ thing."
    
    ro "Ah...indeed. I don’t remember much from my early childhood, but I went into servitude fairly young..."
    #show cg lilromancage
    #Riku whispers.
    r "You were captured."
    
    ro "Yes. As a child. We lived in...cages, like animals. And a man would come through every night to check the cages."
    
    #Riku is breathless.
    r "Wow."
    
    #Roman whispers.
    ro "And sometimes, he would take one of us from the cage, and none of us really knew what had gone on...but if that one returned, they would be...damaged, somehow.
    It terrified me, so I used to practice making myself very small so he wouldn’t notice me."
    
    "This story is making me queasy. I think Roman notices."
    
    ro "It wasn’t all bad. I did get sold off...I spent my time working in a small kitchen. I ended up running away when I found out that the meat we cooked was from our own. Majin."
    
    r "So you did the veggie thing."
    
    ro "Yes. No creature has a right to end another creature’s life like that. 
    My own friends...my fellow kitchen mates...anyway, I ran away and was lucky enough to find some wonderful friends, other fellow Majin, in Germany. 
    Someone I met there suggested I come here when I tired of Europe."
     
    r "Susa?"
    
    ro "Close. A lovely woman named Liza."
    
    r "How’s that close?"
    
    ro "Yes, well. -Ahem-. That’s a bit complicated."
    
    "What’s the point of telling a story if you leave out all the good parts? Makes me miss my mom’s bedtime stories."
    
    ro "At any rate, I do apologize. I really didn’t mean to sour the mood. My life is wonderful now, and that is what matters, yes?"
    
    r "Yeah, fuck the past!"
    
    ro "So how about you, Riku? What is your history?"
    
    r "Oh me? Nothing really worth talking about. Typical sort of stuff, I guess. Kinda boring until I came here."
    
    #Roman chuckles.
    ro "I’m sure you are leaving something out! Hobbies? A long-lost love?"
    
    r "My hobbies? Sports and cutting class. Oh, and drinking. Long-lost love? Yeah, right. I’m seventeen. That’s barely enough time for a first love. 
    There is this one girl I want to ask out, but I dunno. I’m not really all that interested yet."
    
    ro "You are still you---"
    
    r "I mean, heck. I’m not fully mature yet, right? You said that. So like, when do our kind like...usually lose our virginities? When’d you lose yours?"
    
    ro "Oh…me?"
    
    r "Yes, you. There isn’t anyone else here."
    
    ro "Uh…well…let’s see…what year is it…?"
    
    r "…"
    
    ro "…hmm… Carry the two…"
    
    r "…Roman?"
    
    ro "Uh…minus x…"
    
    r "…Roman?"
    
    ro "Sorry, I am rather terrible at math."
    
    r "…"
    
    ro "…"
    
    r "...youuuuuu’re still a virgin, arencha?"
    
    ro "…erm, that is also rather complicated..."
    
    r "Awww, DAMN, Roman. You’re like a hundred!"
    
    ro "Uh…ah…wait, I see our destination!"
    
    r "Out of everything you told me today, that has GOT to be the most depressing."
    
    "Roman runs off ahead. He either sees where we’re going, or he’s just trying to get away from me.  Probably both."

label Scene35:
    r "…this is where you wanted to take me?"
    
    ro "Yes!"
    
    r "Some abandoned shack in the middle of nowhere?"
    
    ro "It looks a bit rough at first, but..."
    #Roman chuckles.
    
    r "What?"
    
    ro "You need solve a puzzle before you can enter."
    
    r "...what?"
    
    ro "Well, this store sells Majin specific items. Just leaving it out and obvious would be fairly dangerous, so it’s hidden. Only Majin should be able to solve the little puzzle and enter."
    
    r "All that to go shopping?"
    
    ro "Well, after you have been hunted for food for a century or so, you start getting a bit wary on who you let into your home."
    
    r "Yeah, yeah, I guess."
    
    ro "It’s not too difficult. You just have to crack the lock."
    
    r "The lock?"
    
    "The lock is sort of old, ancient-looking, and very ornate. It has an odd set of symbols on it."
    
    r "Well, tell me the combination and let’s go!"
    
    #Roman chuckles.
    ro "Oh, I can’t! Each combination only allows one person through. Another layer of protection, in case a human were to try to force us to let them in."
    
    #Riku gives an exasperated sigh.
    r "Haaaaaaaaaaah."
    
    ro "This way only Majin can get in, and then only Majin of a certain level of cognizance."
    
    r "Are Majin usually stupid?"
    
    ro "Well...they’re not known on average for particularly high levels of intelligence..."
    
    r "Yeesh. I dodged a bullet. So, once I break the code, I can get in?"
    
    ro "Well, not quite. Almost."
    
    r "Remind me not to go anywhere with you ever again, Roman."
    
    ro "Oh stop! I assure you it’s worth it. You'll likely find something you need! But, once you crack the code, you must locate the key."
    
    r "Who the heck has a code AND a key!?"
    
    ro  "Precautions like this really are vital to our survivial..."
    
    r "Whatever! Just tell me about the key!"
    
    ro "I don’t know. She changes the puzzle regularly as an added security measure. You’ll have to find it out on your own."
    
    r "Fan-fucking-tastic."
    
    ro "I shall go on ahead. Meet me down there once you’ve finished."
    
    r "Roman, wait, I-"
    
    "He was already gone. Walked straight though a damn wall."
    
    r "Roman, you didn’t tell me what I’m looking for! Roman!"
    
    "There’s a little knot of wood explaining the puzzle. It looks complicated and I’m not in the mood to do school shit on my day off. Doesn’t vacation mean anything to ANYONE anymore?"
    
    "Forget this. I’ll just follow him."
    
    r "Roman, here I commmmmmmme-"
    
    #play sound Crashing noises
    
    r "Ouch. Ouch. Ouch."
    
    "Completely solid. Perhaps not my best idea. I think I hear laughter coming from somewhere."
    
    "Looks like I’ll have to play along for now. I’m not sure what’s waiting for me, but it better be good or next time I’ll just hang out with Soume."
    
    #label minigame 4:
    #Solve the lock combination and find the key to enter the shopkeeper’s shop! [Maybe add a bonus item if you figure it out, and have the owner let you in out of pity if you can’t.]
    #label minigame 4 fail:
    "Ugh, I can't figure this stuff out." 
    r "Helloooo!"
    
    #label minigame 4 pass:
    "Something clicks."
    
    r "I got it!"

label Scene36:
    "The store opens up, revealing a big mess of clothes and books and weird little bottles of  liquids."
    ro "About time, Riku! Come on in and take a look around."
    
    r "What…is all of this?"
    
    ro "One of the only Majin stores in existence. I haven’t fully explored it yet, but there are all sorts of things that I suppose have to do with our history and where we’re from..."
    
    "A woman stands behind the counter. She’s scowling at me."
    
    r "Uh…hi. I’m Riku."
    
    #This is a shopkeeper speaking gibberish.
    w "Herghifthetergitish. Huh?"
    
    r "What the hell did you just say?"
    
    w "Ishtheherdinraffgone. Huh?"
    
    r "Uh, I uh...I'm sorry, I don't..."
    
    #Roman chuckles
    ro "Don't worry about it. She only speaks an old Majin language."
    
    w "Furtendeshginethhhhhhhhhp. Heh heh heh."
    
    r  "Do you understand her?"
    
    ro "Eh…not really. Our old Majin language is nearly dead now. Very few can actually speak it. I think Soume might be able to, but I don't know anyone else."
    
    w "Turtenfishginblapthen. Huh?"
    
    r  "Uh, my name is Riku. Riiiiiiiiiku. RIKU."
    
    "Dunno why I think talking louder might help. She’s just laughing at me now."
    
    "Something suddenly crosses my mind, and while it’s unlikely, it can’t hurt to ask."
    
    r "Hey, do you have a Hunt Duck gun?  It…uh…how do I describe…?"
    
    "I look down at the floor for a moment, then back up, but-"
    
    r "Hey, where did she go?"
    
    "I turn to Roman, who is digging around in a pile of books. He's no help."
    
    r "Ho-sh--"
    
    "She's just suddenly standing there, holding a brand new Hunt Duck gun."
    
    r "Yeah, that’s it!"
    
    w "Unghanteelerentflaf. BONK BONK BONK! Heh heh heh."
    
    "Something tells me she knows more than she’s letting on."
    $inventory.unlock_item("gun")
    
    r "Uh, yeah, I’ll take that. Hmm…well, now what?"
    
    ro "Look around! You've passed the lock, so you can come back at any time."
    
    $show_message("'Shop' has now been added to your nightly options." "medium") 
    $show_message("You may shop by selecting that choice.", "medium") 
    $show_message ("Inventory changes frequently, so be sure to check back as often as you can!","medium")
    
    r "Hmm…I do have some cash left. Maybe I will."

label Scene37:
    "Roman and I run back to the rescue. I spent too much time at the shop. Susa won’t be happy."
    
    r "Hey, Roman, thanks for taking me out. That was actually pretty fun. I was starting to forget was going outside was like."
    
    ro "Of course! I’m glad you enjoyed yourself, Riku."
    
    "I think back to what we talked about. Roman’s definitely had it rough. Everyone here’s had it rough."
    
    "Except me, I guess."
    
    r "If you ever need to talk to someone about stuff, just come find me."
    
    ro "…?"
    
    r "Well, you’ve just…y’know…I just dunno how often you talk to people about stuff you’ve been through.  Count on your friends…and all that garbage."
    
    show ro smile with fade
    ro "I appreciate the offer, Riku. It isn’t like I’m completely alone. I have Soume and Miss Susa and Liza-"
    
    r "And now you got me."
    
    ro "Of course. It isn’t that I don’t have people to talk to…there are some things that I’d just rather not talk about."
    
    r "Fine, fine. Just know that-"
    
    "I stop. Sitting right in the middle of the main courtyard is Susa, smoking something."
    
    ro "Oh er, well, good luck Riku!"
    
    "I turn to stop him, but he’s already halfway down the hallway."
    
    r "I THOUGHT WE WERE FRIENDS! TRAITOR!"
    
    "Maybe the Hunt Duck gun will placate her a bit. Or maybe she’ll just break it over my head again."
    
    r "Ahem. Heeeeeeeey."
    
    "Susa is still sitting there. Quietly. Playing with the ends of her hair."
    
    "I’ve never seen her play with anything that she couldn’t use as a bludgeon."
    
    r "So. You’re probably wondering where I was this morning."
    
    su "…"
    
    r "Funny story. Cause well...Roman-you know Roman? Greeeeeeat guy."
    
    su "…"
    
    r "Right, well, anyway, the thing is…uh…"
    
    su "…"
    
    r "Miss Susa?"
    
    "She finally looks up at me, a bit startled."
    
    su "Huh? What do you want?"
    
    r "Oh, I, uh, got you this."
    
    "I hand over the Hunt Duck gun. It might look like my hands are trembling, but only because it’s surprisingly windy down here."
    
    su "What? Oh--this. Mm. You’ve been working hard. Take some time off."
    
    "Time off?"
    
    r "Are you okay?"
    
    su "Yeah. Fine."
    
    "She isn’t even looking at me."
    
    Man "Excuse me, Miss Susa? There is a phone call for you."
    
    "She was up and already past him before he finished the word 'call.'"
    
    r "Um. Later...then?"
    
    "No response. Fine then!"
    $ decision = "6"
menu:
    "Search.":
        call show_map
    "Sleep.":
        call sleep
    "Store.":
        call shop_loop
    "Research.":
        call research_loop
        $journal.unlock_entry("something", "031")

label Scene38:
    #This is Naomi
    #Naomi chuckles.
    $ Naomi = "Cruel-eyed Woman"        
    n  "Look at all these delectable little morsels. Still, are you sure he’s reliable? I don’t fancy getting myself all worked up for a meal that isn’t going to happen."
    
    m  "You can trust him, \"Naomi.\""
    $ Naomi = "Naomi"
    
    #Naomi makes a resigned sigh.
    na  "I want to eat already. Prime meat like this isn't exactly running around freely."
    
    m  "Patience. Your zealousness will find you in trouble some day."
    
    na  "Think about that before you put filet mignon in front of me after I haven't eaten in a while."
    
    #Mamoru chuckles
    m  "Have you ever heard the parable about the wise cat and his milk?"
    
    na  "No, but I'm sure you will tell me."
    
    m  "Once, in a barnyard, there were two cats. Each day their master would bring them out a saucer of milk. Alas, the master was poor, so that was all they'd receive. "
    m "The foolish cat, he would gulp down his milk, and spend the rest of his day hungry."
    
    m "The wise cat would only drink some of his milk. Each day, he would leave his saucer half full, bring it to the back of the barn, and then return after a nap."
        
    m  "The foolish cat follow his brother to the barn and he saw many mice sharing in the milk." 
    m "'Brother!' he yelled out, 'Why would you share your food with lesser creatures?'"
    
    m "'Food?' the wise cat laughed. 'My dear brother, what separates us is imagination. What you see only as food, I see as bait.'"
    
    na "Bait, hm?"
    
    m "Precisely."
    
    na "So, we’re not going to eat those there?"
    
    m "We will, I'm loathe to let food to waste. Merely...do not become so focused on the crumbs that you lose sight of the feast."

    na "Hm. I got it."
    
    m "It's been confirmed. Go. Alert the other hunters. Prepare them to head out within the week."
    
    na "Understood."

label Scene39:

    n  "Where are you taking me? It’s cold down here!"
    
    m "I have a present for you, Norah. For being such a good sister."
    
    n "A gift? I love gifts."
    
    m "I do have a knack for knowing what you like."
    
    n "What are we doing down in the dungeon, though? Unless it's--"
    
    #show m smile with fade
    m "You have always been too clever for me. I cannot hide anything from you!"
    
    n "You brought dinner!"
    
    m "It's the least I can do. You took such good care of me while I was will."
    
    n "Tell me! What is it! Ooooh, I can’t wait!"
    
    m "Norah, you will find out shortly! At least let there be a little surprise. You cannot-"
    
    a "P-please…k-kill me..."
    
    n "Oh...it's a girl. I love girls."
    
    m "What? Those scraps? Norah, my dear sister, certainly you know I think more of you than that!"
    
    n "She looks tasty to me, and so precious!"
    
    m "No no. I would never feed my little sister anything but the best. That one had quite the poor diet and I'd hate to have her bad habits passed to you."
    
    #Mamoru laughs.
    m "Sometimes I wonder how I put up with you, Norah."
    
    n "Because I’m your favorite little sister~"
    
    m "You’re my only sister."
    
    n "What about---"
    
    #Boy groans in pain.
    Boy "Help…please…girl…get help…"
    
    n "Mmm, you went out of your way to please me, brother."
    
    Boy "What do you want? Please, my parents are rich…"
    
    n "‘What do I want?’ How about your eyes, just to start?"
    
    m "Norah, come now...you are too old to still be playing with your food."
    
    n "But you always play with YOUR food."
    
    #play sound  Crashing noise
    
    n "AH. He tried to take a swing at me just now, did you see?"
    
    Boy "Ngh. Can’t…breathe…"
    
    m "What uncivilised filth."
    
    #Boy sobs.
    Boy "I don’t understand! WHY IS THIS HAPPENING? I WANT TO GO HOME!"
    
    m "Why---"
    
    n "Brother, may I?"
    
    m "You absolutely may."
    
    Boy "Please…I DON’T WANT TO DIE!"
    
    #(CG: Norah gently touching the boy’s face.)
    
    n "Shhhh. You’re making a lot of noise for food, and unlike my brother, I’m not very fond of that. This is just how it is. Food is food."
    
    n "The cry hasn’t  been invented yet that can be heard by an empty stomach."
    
    Boy "…grgh…"
    
    m "Swine. Worse, really. At least swine can die with some dignity."
    
    #play sound Eating sounds.
    
    n "I’m finished~"
    
    m "And a mess, as usual. Come, into the bath; you need to be cleaned up."
    
    n "I’m sorry. I tried, I did!"
    
    m "You’re forgiven, but into the bath before it starts to smell!"
    $ decision = "7"
menu:
    "Search.":
        call show_map
    "Sleep.":
        call sleep
    "Store.":
        call shop_loop
    "Research.":
        call research_loop
        $journal.unlock_entry("something", "031")
        
label Scene40:
#Soume whispers. His voice sounds a bit harsh.

    s "Tch. They're more intelligent than I thought."
    
    "..."
    
    ro "…?"
    
    #Soume whispers angrily.
    s "This wasn’t supposed to happen."
    
    ro "(Who is Soume talking to?)"
    
    #Soume sounds muffled.
    s "…unacceptable…won’t…"
    
    ro "Hey…Soume?"
    
    s  "--hm?"
    
    ro "I’m sorry...was I interrupting?"
    
    s  "Ahhh, Roman. No need to apologize, I was just…"
    
    ro "Soume?"
    
    s  "Nevermind that. It isn’t important."
    
    ro "Who was that you were talking to?"
    
    s  "Ah, you heard me..."
    
    ro "Was...I not supposed to?"
    
    s "It isn’t---This is what I was talking to."
    
    ro "AH! Is that…is that one of your plants?"
    
    s  "Was. It was one of my plants. Her name was Icho."
    
    ro "What happened to it?"
    
    s  "A real shame. She was getting up there in age, but she was still remarkably strong. Full of life, and-"
    
    ro "Soume, who did this? How could this happen?"
    
    s  "…I--I’m not sure."
    
    ro "You don’t know?"
    
    s  "I wish I did. When I got here, she was already like this. I must’ve gotten a formula wrong..."
    
    ro "I’m sorry, Soume, is...there anything I can do?"
    
    s "Death is a natural part of life, and one’s spirit will always come back anew in some way. Here. This is for you."
    
    ro "Ah---one of Icho’s seeds?"
    
    s "Yes. Icho was a bit special. I was developing her to tolerate more extreme climates; she was made to withstand and even thrive in very brutal winters. I think one of her children would be perfect for you."
    
    ro "Oh...this is...I’m not much for gardening, and I wouldn’t want to do any damage to it..."
    
    s "Well, of course I will teach you to take care of it."
    
    ro "You don’t mind? I mean, if it isn’t too much trouble…"
    
    s "It’s not. Now, watch carefully: I’ll show you how to set the pot up..."
    $inventory.unlock_item("ios")
    #Farming minigame.
    
    #Roman chuckles.
    ro "Wow, that was easier than I thought!"
    
    s "I told you~! You have a natural talent there, Roman."
    
    ro "Well, it was all thanks to you."
    
    s "Oh, nonsense Roman. All I did was give a couple of tips."
    
    ro "You really do not give yourself enough credit, Soume. You’re amazing at this. You just make things seem so…so…easy."
    
    s "Thank you. But it really is simple, depending on the student."
    
    ro "But see how Riku has progressed! So quickly. And me, too. I don’t know what the shrine would do without you."
    
    s "You’re far too kind, Roman…"
    
    ro "I just wanted to say that I…uh…well…"
    
    s "Yes?"
    
    ro "…t-thanks. Ahem. Yes, thank you. For everything."
    
    s "You are absolutely welcome."
    
    ro "…yeah."
    
    s "So what will you name this little one?"
    
    ro "Oh, hmmm. What do you think sounds nice?"
    
    s "Mmm. I think that you should be the one to give it a name. Then the plant will have a special connection only to you."
    
    ro "Oh. Well...if it’s that important...I think Svetlana is a lovely name."
    
    s "Svetlana?"
    
    ro "Yes, I’ve always felt a certain attachment to it..."
    
    s "Svetlana it is! A bit odd for a boy plant, though."
    
    #play sound footsteps
    
    ro "B-boy plant? Hey Soume, come back! How could you tell it was a boy plant?"

#[Scene 40]
label Scene40a:

    boy  "OOF!"

    r  "AHA! And another one! Man, I haven’t lost a sparing match in weeks!"

    s  "Excellent job, Riku. You’ve acclimated to your abilities very quickly."
    
    r  "So what do you think, Soume? I gotta be about ready to start accompanying you guys out on your missions."

    s  "Ah, you have been progressing remarkably, don’t get me wrong, it’s just that--"
    
    s "Mmnrh."

    r  "What?"

    s  "It's merely that Miss Susa is in charge of assignments like that."

    r  "...her?"

    s  "And you would need to get clearance from Doctor Osamu first, as well."

    r  "...him?"

    "Great. Miss Susa and Doctor Osamu. The tag-team from hell." 
    "It's like they want me to clean toilets forever."

    #Soume giggles.
    s  "I think you might be ready though! You certainly are the most capable of all the trainees."

    r "Think?"
    
    s "Well...there are always...doubts..."
    
    "Miss Susa walking over toward us." 
    "This is probably the best time to talk to her."

    su  "Soume, I was wondering if-"

    r  "Soume says you should start letting me go out on missions with them!"

    su  "..."

    r  "Right, Soume? Didn’t you say Miss Susa should let me come?"

    su  "Y’know, I’m not sure if I should knock some respect into you, or pity you, since you've clearly suffered some sort of fuckin’ head trauma."

    r  "--huh?"

    su  "You heard me talking to Soume, and you just fucking barge in like some delirious bull?"

    r "N-no, I didn't mean to---"

    su  "If you're too dumb not to interrupt, how am I just s'posed to let you go the fuck out on missions?" 
    su "This isn’t a goddamn game, kid, and you’re nowhere near ready."

    r  "I am though! Just ask Soume!"

    su  "I don’t give a shit how many yams you’ve fried with your little fire power." 
    su "You start acting like a fucking adult, and maybe I’ll consider it."

    r  "But I’m ready now!"
    su "....."
    "She looks pretty mad...but I gotta push it."
    $renpy.pause(1.0)
    
    r  "I am! Look, maybe I’m not as powerful as Soume or as smart as Roman, but I want to help!"

    "Susa slowly lets her gaze drift over toward Soume. He gives her a little nod, which I think is his way of vouching for me."
    "Wish he'd put the same passion into this as he does for his plants."

    r  "Please. Miss Susa, Lady Susa, Queen Susa...whatever!" 
    r "There are a lot of Majin out there that I know need help, and all I’m asking is for a chance."

    su  "..."

    r  "One slip up, and I’ll voluntarily clean the bathrooms for a month."

    su  "One slip up, and I’ll be using your face to clean the bathrooms for a month."

    "Is that an okay?"

    r  "Deal; that’s totally fine. I’ll do whatever, I’m just so-"

    su  "But first, a test."

    r  "Test?"

    su  "Of course. We don't just let any baby out on rescue missions." 
    su "You'll probaby fail, but in the .1% chance that you don't, you'll have my clearance. It's a 7 day challenge."

    r  "7 Day Challenge, eh? I’ll complete it in two!"
    $renpy.pause(1.0)
    su ".........."

    su  "Soume, how do you put up with this idiot?"
    
    r "---what did I do NOW?"

    #Soume giggles.
    s  "Oh, he isn’t so bad, Miss Susa!"

    su  "Whatever."
    su "Look dumbass, if the challenge could be completed in two days, I wouldn't waste my time calling it a 7 day challenge, got it?"
    r "...got it."
    $renpy.pause(1.0)
    su "We usually give out this test after the trainees have been here a full year." 
    su "You pass it now, I’ll let you go out on a mission. You fail, and I don’t have to hear shit about this again until you turn 20."

    r  "Hrm...well, how about-"

    su  "This isn't a negotiation. Take it or leave it, punk."

    r  "Ah. Fine. Fine, I’m ready."

    su  "I’ll give you a bit of time to go get ready, if you want. Some last minute training. Don’t say I never did anything for you, brat."

    "Hmm...it might be a good idea to go train a little bit. Dunno what the hell she has in store for me, but a little extra preparation couldn’t hurt."
menu:
    "I need a bit more training.":
        call pda_loop
    "I'm ready right now!":
        jump daychal2
label daychal2:
    r  "All right, I think I’m ready."

    su  "You sure there, twerp? You don’t get another shot at this."

    r  "I won’t need it."

    su  "Cocky. As always. That’s fine with me; it’ll just be more enjoyable when you fail."

    #Put the Day challenge minigame here.

    #Fail
    #su "Prepare to clean like you have never cleaned before...
    
    #OPTION:
    #Wait, one more chance...
    
    #su "Fine, you're lucky I'm in a good mood. Ready...GO!"
    
    #Awwww man...
    
    #r "Just great..."

label daychal2suc:

    r  "YES! Wooo! A bit trickier than I guessed, but at least I passed, right?"

    su "Feh. I guess you did. Barely."

    r  "I guess that means I’m ready for missions now, huh Susa?"

    su  "..."

    "Susa is clenching her hands and glaring at me. Very strange way to congratulate someone, but it is Susa, so as long as she’s not hitting me, I’d consider it a win."

    r  "Uh...Miss Susa, I meant."

    su  "..."

    r  "Ahem. Soooooooo...my mission. When should we-"
    
    su "Hn. I'll think about it."

    r "H-hey! That's not fair! Awwwww..."

label Scene41:

    k  "Honestly, I don’t know how I can make this any clearer."
    k "HOLD STILL, or I will not be able to collect the blood sample I need."

    "I try to stop my face from twisting into a scowl, but I can’t help it." 
    "This asshole has been stabbing the same needle into my arm for about five goddamn minutes now and can’t seem to hit the fucking vein."

    r  "I don’t know how this is my fault, Mr. Osamu. Just hurry up so I can get out of here."

    k  "Doctor. DOCTOR. Refer to me as doctor, you disrespectful peon! ...There!"

    "He finally hits the vein. He seems pleased with himself, nodding his head and smiling. I try not to actually watch my blood being drawn. That shit always makes me woozy."

    r  "Right, right, doc---whooa..."

    "How the heck did this guy even become a doctor? Maybe a witch doctor!"

    r  "What is with this whole “doctor” thing, anyway?"

    k  "Hrm?"

    "He doesn’t look up from what he’s doing.  He’s putting my blood into some sort of machine and messing around with a bunch of dials and shit."

    r "It was just a mistake...you don't have to get so mad about something like that."

    "He lets out this drawn out sigh and actually stops messing with the machine for a second." 
    "He rubs his eyes, and the way he talks to me I get the fucking impression that this is the way he’d explain something to a brain-damaged brick."

    k  "Because I’ve earned it, you understand?"

    r  "Earned it?"

    k  "The average IQ for Majin is 87 on the human scale. Eighty-seven, Riku. Did you know that?"

    r  "No. Issat bad?"
    $journal.unlock_entry("Majin", "054")

    k "............"
    #Doctor Osamu sighs.
    $renpy.pause(2.0)
    "He’s back to messing with the machine again, but I get the feeling he just doesn’t want to look at me."

    k  "Of course you didn’t know that." 
    k "It's in the information I gave you the first day, but you didn’t read it, did you?" 
    k "Nobody ever does. No one wants to better themselves." 
    k "No one wants to learn WHY our side keeps losing, why we have to hide out and be forced to do things...terrible things..."

    "I don't say anything. I have a feeling I'll know what going on soon enough."

    k  "Most Majin are just fine to go through life, completely ignorant of the world around them." 
    k "They fight, they eat, and they fornicate. And that’s it. That is all they do."

    "He laughs. Sneers back at me."

    k  "That’s why they see us as food, you know." 
    k "As slaves. As whores. Why they think we’re animals. We act like animals." 
    k "If we quack and walk and swim like ducks, why should they treat us any differently from a duck?"

    "If I punched him through the skull, would anyone blame me?"

    k  "I'm not like you, though."
    k "I’ve gone through my studies, worked at trying to survive in this world, and I became the first recognized Majin doctor." 
    k "The ONLY accepted Majin doctor." 
    k "None of you little pigs, while you were rabidly feasting and fucking in the streets, thought that there may be merit to even learning your own biology."

    r  "Congrats, Doctor."
    "I can't help but be sarcastic. What the hell is his problem?"
    
    k  "Right. Doctor. You see? You see what we can do?" 
    k "What we're capable of?"
    k "We’re not just food, or lab rats to be tested on and discarded." 
    k "Doctors, scientists, philosophers; there are so many thing we could do if we just tried. We aren’t food or slaves or breeding toys."
    "I'm getting tired of all this crap, but what should I say?"
    
menu:
    "What's wrong with Majin and humans just being different?":
        jump majhumdiff
    "I guess you're right...":
        jump urite   
        
label majhumdiff:    
    r "Learning is great and all, but maybe we're just supposed to be what we are." 
    r "Why do we have to do what humans do to live when we aren't made for it?"
    
    k "...excuse me?"
    $renpy.pause(1.0)
    r "Seems to me like..." 
    r "You should stop hating yourself and your own kind and trying to do what humans do..."
    r "And just accept yourself for what you are."
    
    k "........."
    
    "Huh. I think I made him speechless."
    
    k "Kch! You don't understand anything, you churlish little paramecium!"
    
    $renpy.pause(3.0)
    "...can't say I didn't try."
    
label urite:
    r  "Fine, whatever."
    r "I’d like to go out and help Susa rescue some other Majin, but I can’t until you give her the okay. Can I go or what?"

    k  "Let me see, I’ll just need to-"

    #play sound Explosion, electronic noise

    k  "Ngh. Stupid machine. This worthless thing is always breaking on me."

    r  "Didn’t you build it?"

    k  "Of course I built it, but it can't possibly break with my calculations. A flaw of the machinery, I assure you. My design is perfect."

    r  "Riiiiiight, doctor. So can I go, or what?"

    k  "You may, but I can't parse the results until this machine is fixed, I'm afraid."

    r  "Oh c’mon, man! Look at me, I’m fine!"

    k  "I'm sorry, but this is simply how things must be done. You could have a bruised valve somewhere and I need my machine to catch it."
    k "Unless you prefer to die..."

    "He smiles at me. Bastard enjoys watching me suffer. I bet that's why he and Susa get along so well."

    r  "Well, how long is this going to take?"

    k  "Oh...I don't know...perhaps an hour, maybe a week. I need to assemble the replacement parts..."

    "He looks around his lab for a bit, gathering what looks like several bits of scrap metal."

    k  "Here, take these!"

    r  "What the heck am I supposed to do with this?"

    k  "I always keep the spare parts around just in case of emergencies like this, but they make the room so very cluttered if I just leave them..."

    r  "...lemme guess, you expect me to put them back together."
    
    k "Ehehehe."
    k "We'll see if your mind is ready for a mission, and then we'll test your physical condition."

    "He goes back to fiddling with his instruments and messing around with the big screen in front of him."

menu:
    "Do what he says.":
        jump dowhatkazsays
    "Resist.":        
        jump notgonnahappen
   
label notgonnahappen:        
    r  "No. No way. I'm not gonna let you push ME around."
    k ".................."
    k "Ah."
    k  "It's just as well. I’m not in any rush to have you sent out on your first mission." 
    k "In fact, I'm relieved that you aren't either. Dangerous things lurk out there, you know? Better to be here, where Miss Susa can have you clean and help me around the lab."

label dowhatkazsays:    
    #Riku frowns.
    r  "FINE."

    k  "Oh, what an excellent attitude! I knew I could count on you." 
    k "The quicker you fix everything, the faster I can clear you and the sooner you can go out and get yourself killed."

#gear minigame here

#label gearfail:
    #r "............I can't do this stupid thing."
    #k "Well, if that's the case, I can't give you your 'stupid' clearance."
    #r "FINE I'll try again!"
    #minigame here
label gearsuc:
    r  "There. The stupid thing is working again. Thanks to me."

    "I glare over at Doctor Osamu. He didn’t bother to help me at all, and now he’s just sitting at his console, grinning at the screen."

    k  "Ah! Yes! Excellent, this is truly excellent."

    "A 'thank you' would have been nice. Or a 'good job'. Hell, I would have even taken a fucking grunt in my direction from this guy."
    "Still, if I get to go on missions, it's worth it."
    "Sorta."

    r  "So...what’s it say? Am I good to go, or what?"

    k  "Hrm?" 
    k "Oh yes, I almost forgot about you."

    r  "Yeah, me. The guy who just fixed your dumb machine. So, does it clear me, or what?"

    k  "Oh, this machine doesn't do that."

    r  "........"
    r "WHAT?"

    k  "No, no, no. You must have misinterpreted the situation." 
    k "This is for something else entirely. Call it professional curiosity. I had heard about your power..."

    r  "W-what do you mean this isn’t going to clear me? Why the hell did I hafta fix it for?"

    "Doctor Osamu continues like he didn’t even hear my question." 
    "I can barely understand the jumble of words coming out of his mouth."

    k  "You are quite unique, even amongst Majin."
    k "Dark flames and all that, strong enough to ward off one of the most...troublesome...of our enemies."
    k "Remarkable, really. I've never seen that sort of manifestation in any Majin. I haven't even heard of it."

    r "I'm not your guinea pig! What the hell're you talkin' about?"

    k  "Imagine that!"
    k "Me, not having heard of something before!" 
    k "Ooooh, to feel ignorant about something, I mean truly ignorant; it's delightful!"
    k "The learning opportunity---"

    r  "Yeah, that’s great Doc, but what I’m interested in-"

    k  "I had almost forgotten what that feels like." 
    k "The thrill of the unknown, the tension one feels during the chase of the answer, the satisfying climax of discovering something new, I--"

    "...does he get off on science, or what?"
    $journal.unlock_entry("Doctor Osamu", "028")
    r  "Hey, Doc! Yo, I’m still here. You need to clear me."

    k  "Ah yes, quite. My mistake."

    "He looks me up and down quickly."

    k  "You’re in fine shape. Tell Miss Susa I say you’re cleared to go."
    r "..................."
    r  "Wait, are you freakin’ kidding me? That’s it?"

    k  "I can make it more invasive, if you’d prefer. I haven’t performed a rectal cavity search in years, but I'm sure for you..."

    r  "N-NO! No. That’s fine! I’m good."
    r "Was just expecting something, uh, more I guess. Not complaining!"

    k  "Well, get out of my lab then. Your ignorance is fogging up my machinery."

    r "I'm goin' already!"
    # if, some scene where Soume is acting weird, then you get Scene42
    # else: jump Scene43
label Scene42:    
    r  "I have to go talk to Soume anyway so-"

    "Doctor Osamu has finally turned around from his data, and for the first time since I’ve been down here he seems like he’s actually paying attention to me."

    k  "You haven’t noticed anything peculiar about Soume recently, have you?"

    "He’s staring at me from behind his glasses now. He’s doesn’t break eye contact once, and he sits unmoving, waiting for my response."
    "It’s really unnerving."

    r "Uh, well...he talks to plants. That’s pretty weird."

    "He waves his hand at me."

    k  "No, he always does that. I mean unusual for him.Think, difficult as that may be."

    "I make the face I always used to make in class, when I wanted to pretend I was paying attention."

    r  "Um. No, not really. Seems normal to me."

    k  "There’s something going on with him—I know it."

    "He grabs me firmly by the shoulder and shakes me slightly. I don’t know how to tell someone they’re crazy without pissing them off, but here it goes."

    r  "I dunno, Doc. Soume seems pretty, uh, fine to me. Maybe you’re just imagining things."

    k  "No."

    k  "I’m sure he’s up to something. He doesn't let me examine him."

    "If that's the only requirement for being 'up to something', then lock me up now. Who would WANT to get examined by him?"

    k  "Something needs to be done about him. I told Miss Susa---Talk to him if you can. See if you can’t figure something out."

    r  "S-sure thing. Look, I got to get going. Thanks for all your, uh, help."

    k  "Riku, listen to me. I am a sensory Majin, and I'm sure--Soume is trouble; he’s dangerous. He is a threat to everything I’ve worked for and--"
 
    "He pauses. I think he notices I’m uncomfortable, because his demeanor suddenly changes."

    k  "Ahem. You’re right...I’m overreacting. You’re free to go."

    "He wheels back to his desk and goes back to his work. There’s definitely something strange about this situation, but I’m not sure it’s Soume."
    
    r  "Thanks again, Doctor Osamu."

    "I walk out of the lab and head back upstairs. I don't really wanna mess with that guy."
    $ Scene42 = True
    
label Scene43:
    ro  "So, Riku, what was Doctor Osamu’s verdict? Have you passed?"

    r  "With flying colors!"

    #Roman chuckles.
    ro "Excellent! And even more so because..."

    r  "What?"
    
    ro "Miss Susa has just issued a mission and if you'd passed, you'd be allowed to go!"
    
    r "Awwwwwwwlright!"
    r "So what is it? Fighting that Mamoru guy head on, or taking on a giant horde of hunters..."
    
    ro "...nothing like that..."
    
    r "Oh, so we're gonna bust into the enemy base, ambush them and save someone?"
    
    ro "...no."
    r "......."
    ro "It's a very good one for your first mission, don't give me that look..."
    ro "We're picking up a Majin in the forest and bringing her here."
    r "............"
    ro "You know, for a better life!"
    r "................"
    ro "Well, what DID you expect?"
    r "Fiiiiiiine. I guess it's okay."
    ro "You'll enjoy it, I promise."
    r "Get some rest tonight, we leave tomorrow morning, early!"
    
    if Scene42:
        jump Scene43b
    else:
        jump Scene43c
        
label Scene43b:    
    "I just sort of nod in Roman’s direction. He’s smiling, but for some reason I can’t get excited. All that stuff the doctor was talking about is still bugging me."

    ro  "Great timing, too. Soume just mentioned to me that Susa recently received word of another Majin in need of rescue."

    "I feel like I should be asking him more about the mission, but I can’t get my mind off of what the doctor said. He seemed paranoid for sure, but it would still be nice to learn a bit more about Soume."

    r  "Roman, you’re close to Soume, right?"

    #Roman sounds very nervous, because he has a crush on Soume and doesn't want Riku to know.
    ro  "E-excuse me? I’m afraid I don’t quite know what you’re getting at."

    r  "Well, like he talks to you, right?"

    #Roman gives a sigh of relief.
    ro "Oh, that’s what you mean!"

    r  "Uh, yeah. What else would I be talking about?"

    ro  "Nothing! Ahem. No, nothing. Soume and I talk a fair bit, that is true. He talks to you too, though. I’ve seen him frequently!"

    r  "Well...yeah, that’s true. Sort of, I guess."

    ro  "What do you mean, Riku? How do you “sort of” talk to someone?"

    r  "Well, I dunno. Kinda hard to explain. But, I mean, he talks to me, all right. But it’s always about training, or plants, or something small. I don’t really know anything about him."

    ro  "Oh, I see."

    "It looks like Roman finally got what I was trying to say. He furrows his brow a bit, and is silent for a little while."

    ro  "Well, it is true that Soume is a bit introverted. He doesn’t talk about his past or himself all that often."

    r  "Do you know why?"

    ro  "I can only guess. I mean, not many of us like to talk about our past, Riku. Not all of us were lucky enough to grow up with a nice family like you."

    r  "Yeah. True."

    "I thought back to what Roman told me about himself. If Soume’s past was half as bad as his, I suppose I could understand him keeping quiet about it."

    r  "Do you know anything about his past?"

    ro  "Well, he has told me a bit. I’m not sure if it’s my place to speak about it though."

    "Roman breaks eye contact with me and bites his lip. He seems suddenly uncomfortable, but finally looks back toward me."

    ro  "All I really know is that he was a slave for some human family for quite some time until Susa saved him."

    r  "Susa saved him? Herself?"

    ro  "Yes. She used to go out on missions quite frequently, apparently. What is this all about, anyway?"

    r  "Huh?"

    ro  "Why are you so curious about Soume all of a sudden?"

    "I’m not sure if I should tell him. But Roman has always been honest with me, and I feel like I can trust him."

    r  "Uh...well, it’s nothing really. Doctor Osamu just...well, he seems like he doesn’t trust Soume for some reason."

    ro  "Doctor Osamu? I see."

    "He gets quiet suddenly and starts walking faster."

    r  "Whoa whoa, Roman. Where are you running off to? Something about the doctor I should know?"

    ro  "Again, Riku, I’m not sure I should be talking about any of this. It really amounts to just a bunch of gossip. All I can say is I know the feeling of mistrust is mutual."

    r  "Mutual? Why? What happened between them?"

    ro  "I only know second-hand information. If you’re that curious I’d suggest talking to Soume."

    "Damn. Roman always gets quiet once he gets to the good stuff. I’ll make sure I talk to Soume when I get the chance."

    r  "It’s just that, well, he said that Soume won’t let him test on him."

    ro  "Well, I can’t say I’d blame him for that. The Doctor really is a genius, but I myself worry about his...enthusiasm at times."

    "That was a fair point, I guess. I wasn’t in any hurry to get back to the lab anytime soon."

    ro  "He actually tried to get me to give him some blood during one of my routine visits. I don’t know how silly he thinks I am to go along with that."

    "I could feel my face getting hot and red. I tried to act casual."

    r  "Is there any reason not to give him your blood? He is a doctor, right?"

    "I should have asked for some damn credentials when I went in there."

    ro  "Well, he is a doctor—that part is true. But he is a sensory demon as well, so I’m just a bit wary, you know?"

    r  "Oh...yeah. --wait, no. What do you mean?"

    "Roman looks around, making sure that no one else is within earshot."

    ro  "Again, this might just be more superstition than anything else. So don’t go repeating this to everyone."

    r  "Fine, fine. Just get on with it already."

    ro  "Well, as I said, he’s a sensory demon. So he can sense things like paths to take or imminent danger. He is quite good at it too; I don’t think we’ve ever been ambushed when he accompanies us."

    $journal.unlock_entry("Majin","053")
    r  "So?"

    ro  "Well, he really only gets flashes of what’s going on. He knows if danger is incoming, but not exactly who or what it is. He can tell what paths to take, but doesn’t know what’s on the other paths."

    r  "...uh, I still don’t get it."

    ro  "Well, this is where I rely more on rumors than anything else. But I’ve heard that his powers are enhanced if he, uh, well..."

    r  "If he what, Roman?"

    ro  "Well, if he samples your blood."

    "Roman’s face flushes suddenly. Sort of looks like one of my mom’s tomatoes now."

    ro  "That’s just something I heard though. I’ve never really asked him if it were true or not."

    r  "Right. But what exactly do you mean by 'samples'?"

    ro  "Well, I mean he...ahem..."

    "He looks around quickly again. The next part he whispers so quietly I can barely hear him."

    ro  "...drinks it."

    r  "He drank my blood!?"

    ro  "SSSSHHHHHH!"
    $journal.unlock_entry("Doctor Osamu", "030")

    "Roman clasps his hand over my mouth while looking around again."

    ro  "Remember, I don’t know that for sure. That’s just something I heard."

    "He finally releases my mouth. I feel like yelling again, but I think better of it."

    r  "Why the hell would he do that? Does it make him stronger?"

    ro  "No. Well, yes. But not really."

    r  "...what?"

    ro  "Well, it allows him to...sense better. Or so I hear."

    r  "Right. So what does that mean?"

    ro  "I said before he only gets flashes of things. Well, apparently, if he samples a bit of someone’s blood, he can determine where they are at all times." 
    ro "He can sense them coming and going, where they are and what they’re doing."

    r  "How does he do that?"

    ro  "I’m not a sensory demon, how should I know?"

    r  "...oh."

    "That was the most I could muster. Rumor or not, I wish Roman would have told me this earlier. I also wish I could go and get my blood back."

    ro  "Anyway though, I think I’ve spread enough rumors for one day. You should get some rest! We might be departing on our first mission tomorrow!"

    r  "Sure. Uh, thanks, Roman."

    "Roman heads down the hall. I gotta learn to stop asking questions I really don’t want the answer to."

label Scene43c:    
    $ decision = "8"
    
menu:
    "Search.":
        call show_map
    "Sleep.":
        call sleep
    "Store.":
        call shop_loop
    "Research.":
        call research_loop
        $journal.unlock_entry("something", "031")
        
label Scene44:
    
    su  "Now the recon point is...Oi! You listening, sprog?"

    "Susa keeps on interrupting herself to make sure I'm paying attention." 
    "I dunno why—I haven’t nodded off once during her whole lecture, which is kind of a miracle for me."
    "I'm not very good at paying attention."
    $journal.unlock_entry("Riku","064")

    r  "Yeah, yeah. I’m listening."

    su  "Soume, if he slows you down or forgets the plan, you have my permission to kill him."

    #Soume giggles
    s  "I hardly believe that will be necessary."

    r  "I told you, I’ve been paying attention. I’m not gonna screw this up."

    su  "I still don’t think ya ready yet, kid. I mean, he’s just a pup!"

    ro  "Oh Miss Susa, he’ll be fine. Trust me, if not him. He’s ready."

    "Susa starts grumbling something under her breath. I can’t hear her, but I doubt I’d want to even if I could."

    su  "Well, let’s get on with this then. Now, here is where you’ll be waiting for the target."

    r  "What’s her name?"

    su  "See, that’s just what I mean. I already told you this! Her name is Akiko! You can’t just show up and be like 'hey you, come with me.' She’ll run off, won’t she!"

    r  "Right, sorry. Akiko. Akiko  Akiko."

    "I keep on repeating the name to myself in my head. Can’t forget this again, or Susa isn’t going to let me go along."

    su  "After meeting her, escort her back here, to the safe zone."

    k  "Which is where I’ll be waiting."

    "Doctor Osamu coming along on a mission is supposedly rare, since he can't fight."
    "I'm not particularly happy about it, but by his expression, neither is he."

    su  "Yes. While I’m not expecting any resistance, you never really know. This area is far enough away that you'll be safe even if there is a skirmish."

    k  "Excellent. I like the sound of that."

    su  "And, you’ll be on scene to heal any injuries if need be." 
    su "Now, first escort Kazutaka to the safe zone, then head over to where you will be waiting for the target. He can use his abilities to make sure there aren't any problems."

    "Soume and Roman both nod. Doctor Osamu frowns, and looks off. Susa turns to me."

    su  "Simple enough for ya?"

    r  "I got it."

    su  "Listen to what Soume tells you. He’ll be in charge once you leave the grounds. If I hear anything bad from him-"

    r  "You won’t! I swear."

    su  "Well, if I do, you’ll be in training for at least a decade before I let you back out."

    "Susa turns to leave, and Doctor Osamu and Soume follow her out."

    ro  "Ready, Riku?"

    r  "I think so. Don’t tell Miss Susa, but I am a little nervous, you know?"

#Roman giggles
    ro  "Completely natural. There is nothing to worry about. It's rare that our missions involve real fighting. Both Soume and I will be there in case things become complicated."

    r  "Yeah, I know, I’m just...I dunno. I don’t want to screw this up when someone else is depending on me."

    "I don't want to remind Roman of just how ineffective he was the LAST time I saw him fight."

    ro  "I can’t think of anyone else I’d rather have out there with us. You’ll be excellent!"

    "That cheers me up a bit, at least. Still feel like I might be sick, though."

    ro  "Oh! I almost forgot."

    "Roman grabs a small potted plant that he brought in with him."

    ro  "Here!"

    "I take the plant from Roman, but I’m not quite sure what he wants me to do with it."

    r  "Uh...thanks. Did Soume ask you to give this to me?"

#Roman chuckles
    ro "No, I grew this little guy myself."

    r  "Really?"

    "It is a bit scrawny compared to Soume’s usual offerings, but it was pretty impressive for the guy’s first try.  And it wasn’t covered in fangs or claws, so I sort of prefer it."

    r  "You want me to have this?"

    ro  "Yes. Consider it a gift in celebration of your first successful mission!"
    $inventory.unlock_item("rose")

    r  "Thanks, Roman."
    
    ro "You're welcome. His name is Svetlana."

    r  "...Svetlana?"

    ro  "...ahem. Well, put him somewhere safe and then come join us at the entrance."

    #-play sound footsteps-

    r  "Svetlana, huh?"

#[Scene 45]
label Scene45:
    r  "We there yet?"

    k  "Patience, child."

    "I know I had promised to behave, but this was starting to get boring." 
    "We've been on foot for the last 30 minutes or so, and we're not even to the site yet."
    
    r "Are we theeeeeeeeeere yet?"

    k  "HUSH! I am TRYING to concentrate!" 
    k "..."
    k "Mm-- right, it seems safe. We can proceed."

    s  "We are getting close to the safe zone, Riku. Prepare yourself."

    r  "‘Bout time. I was beginning to think the Doc here was getting us lost."

    "Doctor Osamu scowls back at me. He is mumbling to himself as we walk, and it sounds like he’s describing some part of the forest. Not the stuff around here, though; his descriptions don’t match up."

    k  "...small clearing...large tree stump...bed of flowers..."

    "He turns slightly to his right, and we all follow. Soume is bringing up the rear, and he is surprisingly solemn. I’ve never seen him so serious. He catches me looking at him."

    s  "Riku, it is important to stay alert. Don’t let your focus wander."

    r  "Right, sorry."

    "I turn back around, and I find us approaching the area Doctor Osamu was just describing. He walks over to the stump and sits on top of it." 
    "Soume walks into the clearing as well, in a slow circle, dropping seeds. They sprout up as full grown plants."

    s  "For protection."

    "He doesn’t stop until there is a complete circle of flowers around us. They’re giving off this pollen that’s making my nose itch."

    k  "Don’t you have something a bit less...pungent?"

    #Soume giggles.
    s "Less pungent than this and you won’t be shielded, Doctor! Are we safe to continue?"

    "Doctor Osamu wipes his nose and bows his head slightly."

    k  "Hmm...I can’t..."

    "He looks like he's gotta go to the bathroom."

    r  "Doc?"

    k  "Ah. No, I was mistaken. Everything looks clear ahead."

    s  "Excellent. Be sure to warn us if the situation changes."

    #Doctor Osamu sounds a bit rude, here.
    k  "Well, of course I know that."

    "Doctor Osamu shakes his head like this was a silly thing to have said. Soume turns to Roman and myself."

    s  "All right. We’re less than a mile away now. Riku, stay close behind Roman and myself."

    #Kazu yawns
    k  "Trust me, there is no danger. Let the child lead the way if he wants."

    s  "I don’t think that would be wise."

    r  "Uh, yeah. Me neither. I’ll just stick behind you, if that’s all right. I’m kinda fond of all my limbs."

    #Roman chuckles.
    ro "Riku, I doubt it’ll be that serious."

    s  "Follow me. And please be quiet from this point forward."

    k  "Hmph. Stick to your plants, Soume, and leave the sensory work to the master."
    
    s "...."

    "We leave the safe zone and head deeper into the forest." 
    "According to Susa's instructions, there is a small shack thing where our rescue is living." 
    "We just need to find her and get back to the safe zone. Job done. Easy, I think, for my first mission."

    "Roman and I follow Soume as he leads us past a river. I feel like we should be getting close when Soume motions for us to stop, before slowly peering around the edge of a rock wall."

    "Soume turns back quickly, his face paled."

    #Soume whispers.
    s  "Hunters. A swarm of them."

    r  "What?"

    ro  "Are you sure, Soume?"

    "Roman peers around the corner as well. He looks back and doesn’t say anything, but he looks like he's going to throw up."
    "I think I am going to throw up."

    r  "I thought this area was safe?"

    s  "These are somewhat minor hunters. Perhaps Doctor Osamu couldn’t detect them."

    ro  "Are they Mamoru’s minions?"

    s  "I can’t tell for sure, but Mamoru-kun is the highest level demon hunter. I doubt he would have such...easy targets with him."

    "Soume closes his eyes, and pulls something from his hair, which he drops to the floor. No clue what that's about."

    r  "What are we going to do?"

    s  "Riku, I want you to wait here. Let Roman and I clear out the area quickly, then we can head out together."

    "I pause for a second. I know I should probably listen to Soume, but I think about Doctor Osamu. He really seemed to think there wasn’t any danger this way."

    r  "...what about Doctor Osamu?"

    s  "What about him?"

    r  "What if the hunters show up back at the safe zone? Will he be safe?"

    s  "Well..."
    s "...probably."
    s "It is sort of hard to tell in these situations. I’m sure he’s at least alert. As long as he didn’t fall asleep..."

    r "..........."
    
    ro  "He did look like he was ready to doze off."

    s  "Hrm. Riku, I leave it up to your judgement. Either wait here or go warn Doctor Osamu. I leave the decision to you."

menu:
        "Stay with Soume and Roman.":
            jump Scene46a
        "Head back to Doctor Osamu.":
            r "I should go warn the Doc...we probably don't want him to get eaten."
            s "Fair enough. Move as quickly and silently as you can."
            jump Scene46b
                
label Scene46a:    
    "I settle down and wait for them to come back." 
    #play sounds battle
    "I can hear the fight starting..."
    "I'm kind of jealous." 
    "The whole reason I wanted to go on missions in the first place was so I could fight." 
    "Lucky bastards."

    #This is a hunter.
    u  "-gurugle-"

    "I turn around. While I was admiring Soume and Roman, a couple of demons managed to sneak up behind me. They really don’t look so tough."

    r  "Uhhh...Soume? Roman?"

    "I call out, but they're too far away."

    r  "Aw shit. I’m going to have to fight you, aren’t I?"

    u "-gurgle-"

    #-Battle here. Riku versus a couple of minor demons. Game over if lose-

    r  "Hmph. Didn’t even break a sweat."

    "Even though I won, I'm still nervous. These things are trying to kill me. Even if they're easy to fight...they're trying to KILL me."
    "I'm trembling."

    ro  "Riku!"

    "Roman comes running in my direction. I don't see Soume anywhere."

    r  "Roman, I just got ambushed. A couple of those little things snuck up on me."

    ro  "Soume wants you to fall back. There are too many of these things out here right now. Head back to the safe zone with the Doctor. Wait for us to return."

    r  "But-"

    ro  "Riku, this isn’t up for debate! Return immediately; this area is no longer safe!"

    "Roman takes off running in the direction he came from. Well shit."
    "Maybe though, if I try, I could take em..."
    "Or maybe I'd just get killed..."
menu:
        "Ignore the warning and try to help.":
                jump badend3
        "Head back to the safe spot.":
                jump Scene46b

label Scene46b:
    "I’m practically in a full sprint as I head back to the safe spot."

    "Doctor Osamu is lounging on the tree stump, reading some paper he brought with him.  He glances up over the top of the paper briefly when he sees me coming."

    k  "Oh, what happened?  Did they kick you out already?  Were they tired of babysitting?"

    r "............."
    "He laughs to himself and goes back to reading."
    "He doesn't seem to have the slightest clue what's going on."
    $renpy.pause(1.0)
    "For a sensory demon, he sucks."

    r  "Uh Doc, don't you sense anything?"

    k "....?"
    k  "Is that why they sent you back here?"  
    k "Everything is clear. There is no danger around for miles."  
    k "Now, scoot on back to the others and let me get back to my work, please."

    r  "Well, your sensing pretty fucking screwed up, or you have a weird idea of what danger is.  We were just attacked by demons."

    k "........."
    k "...what?"

    r  "You didn't know?"
    r "Roman and Soume are still out there fighting them!"

    "Now he looks like he's going to have a heart attack."

    k  "No, no. That is impossible. I’d be able to tell. You must be mistaken."

    r  "Look, I know what I saw.  Maybe you just weren’t paying attention or somethin’." 
    r "There were hunters.  Dozens of them."
    k "............."
    k  "No, no.  That can’t be!  It can’t!  I’d be able to tell. I’d-"
    k ".............."
    
    "He looks like he's going to blow the little vein on his forehead."

    k  "Ngh." 
    k "I don't sense a thing. Not a single thing. This is IMPOSSIBLE."

    r  "I don't know! Maybe your sensors are on the fritz!"
    r "Cause I KNOW what I saw."

    k  "It's NOT POSSIBLE, DAMN YOU!"
    k "I must have been drugged!" 
    k "........"
    k "Yes...drugged...that must be it..."

    "I roll my eyes.  This guy just can’t admit when he made a mistake."

    r  "Whatever it is, I’m back now.  I’m supposed to keep you safe."

    k  "You?  That is rich.  You’re still a child, barely out of your mother’s womb." 
    k "Oh lords of science..."
    k "I'll be MURDERED without a fight."


    "Couldn’t Soume have sent me off to guard something a little more charming?"  
    "Like some maggots or a slug or a garbage bin full of horse shit."

    k  "It is rather odd that Soume sent you off like that though, don’t you think."

    r  "Uh...not really."

    "It was basically my idea.  I brought it up first after all; I thought this guy might need some help."

    k  "Definitely odd. Everything that man does is suspicious. Certainly, he does not act like a rational creature."

    "Doctor Osamu has taken up pacing back and forth again, mumbling something to himself."

    "I take the place on the stump he vacated.  If I have to listen to him, I might as well make myself comfortable."


label Scene47:
    s  "Roman, are you alright?"

    ro  "Yes. Those hunters were rather weak, weren't they?"

    #Soume giggles.
    s  "I do feel a bit silly for sending Riku away now.  Even Doctor Osamu could have handled this bunch."

    m  "Is that so?" 
    m "Well...I hope I might provide a more suitable challenge."

    ro  "---ah--"
    
    #Soume should sound a little condescending when he talks to Mamoru, as if Mamoru is a 3 year old child that is disobedient.
    s  "Ahhh. The air did smell a bit foul, Mamoru."

    m  "I really do apologize for my opening act.  I was hoping it might provide you with a rigorous warm up, but it appears they were unworthy of you."
    m "As usual, Soume."
    $renpy.pause(1.0)
    m "I'm quite embarrased. But I assure you, I’ll be sure to make note of this during their performance reviews!"
    "His laugh is so chilly."

    s  "So to what do we owe the pleasure of your company?"

    "Mamoru is frightening. I never understand how Soume can stay so calm and casual around him...even going as far as to refer to him casually."
    "And meanwhile, I'm positively shivering."
    
    m  "I came to see you, of course..."

    ro  "No---are we too late?"

    m  "Oh, nothing like that. I've only just arrived. I was so delighted to see you, Soume."

    ro  "No---"

    s  "Roman, hush!  Say no more."
    #Translate this next line, but it will only go into the JP script. It's in Roman's voice.
    #"I don't think he's ever called me just Roman before."

    m  "Oh.  Oh!  I see now.  You are referring to little rabbit who lived here just a while ago!" 
    m "Alas, I am afraid that in that case you are a tad late." 
    m "I would share leftovers, but I know that isn't to your taste, right, Soume?"

    ro  "You, you...monster!"

    #Mamoru laughs gleefully.
    m  "Ahaha..."
    m "A monster? Oh Roman, you wound me."

    r "Y-you’ve been warned, Mamoru! You can't defeat both of us!"

    #For this, I think use "Roman-chan" for extra effect.
    m  "Come now, Roman, don’t flatter yourself. Any difficulty I had here would not have anything to do with you."

    s  "Mamoru."
    
    "Mamoru's face suddenly changes." 
    "He really is afraid of Soume."

    m  "How trite." 
    m "But it's fine. I wasn’t looking for you two, anyway."  
    m "I had heard that an old friend had come to visit me. Riku, I believe you know him. I don’t suppose there’s any chance you two might point me in the right direction?"

    s  "Not tonight, I'm afraid."

    #Mamoru's tone is solemn and nasty.
    m  "You're being exceptionally difficult today, Soume."

    #Soume calls Mamoru "Mamoru-kun", and he also sounds a bit more severe than usual.
    s  "How ironic, coming from you, Mamoru."
    
    m "Is it?"

    ro "..."

    na "Well well, what have you got here, Chief?"
    
    m "Ah, so your group has finally decided to show, have they?"

    ro  "Demon hunters--b-but how?"

    s "....."
    s  "It seems we’re surrounded. You've gotten a litle smarter, Mamoru."

    m  "...tch! I'll leave them to you, Naomi."

    na "Sure thing, Chief. Pretty sure I could handle these two by myself if need by, from the look of them."

    m  "Don't be foolish."

    ro  "What’s the matter?  Too f-frightened to fight us by yourself?"

    #Mamoru calls him "Roman-chan" here too.
    m  "You're still as cute as ever, Roman."
    
    m  "Sorry to have to run and all that, but there is an old friend that I simply must go and say hi to."

    ro  "No!  Come back!  COWARD!"

    s  "Roman!  Calm yourself."
    # Translate this next line, but it will only go into the JP script. It's in Roman's voice.
    #"There it is again. He called me just Roman."

    ro  "But he’s going after Riku and-"

    s  "They’ll be fine.  We won’t be able to do them any good if we wind up dead."

    na "We~ll. Who wants to die first?"

    s  "Roman, I will try to distract the leader and lead a good portion of them off this way.  Try to handle the lighter ones until I return."

    ro  "Soume...be careful."

    s "...and you stay alive."

    db "Captain! That one is attempting to run."

    na "Oh for fuck's sake.  Do I have to do everything? Chase after him, you twits.  Fuck."

    ro  "HAH!"

    #Animation of ice sword.

    dg "Get ‘im!"

    #play sound Swords clashing

#Battle goes here; Roman against demon hunters.

    db "Hurk!"

    m  "Ahhh, so easily dispatched. Perhaps I will make a more worthy opponent?"

    ro  "M-M-M-Mamoru!"

    m  "M-m-m-m-me!  You really should get that stutter checked."

    ro  "No, but--"

    m  "I wouldn’t look around for your precious Soume right now.  Last I saw he had his hands quite full with Naomi."

    ro  "H-he's not---Soume and I---"

    #Mamoru should sound very mean here, very different from him usually sounding very good-natured.
    m "Shut up." 
    
    ro "........"
    
    "This is bad. I've never seen him get seriously angry before."
    
    m "I know everything that youko thinks, and I can see it in your eyes."
    
    ro  "..."

    #Riku should be referred to as "Riku-chan".
    m  "Oh, and I might have lied just a bit.  You see, the target today wasn’t actually Riku."

    ro "........"
    ro  "What...?"

    #He should be called Roman-chan again.
    m  "Oh yes. Lucky you, Roman."
    m "You're not really to my personal tastes. Ugly. Scrawny. Whiny. Pale."
    m "........."
    m "But, you're edging in on my territory. I really don't like that."

    #Roman is being strangled.
    ro  "Ngh--"

    #Roman-chan again.
    m  "Make a wish, Roman.  I’d recommend it being a good one."

    ro  "AHHHHH!"

    #-SFX crashing noises-

    ro  "--ahn--no..."

    m  "Yes...scream...it'll make this sweeter for me."

    #Mamoru-kun.
    s  "Mamoru."
    m "........"

    m  "Ah, Soume, back so soon? Those idiots couldn't even keep you for ten minutes. I should have known."

    s  "I'd advise you let him go."

    ro  "...Soume...run..."

    s  "Roman, please keep quiet."
    
    m ".........."

    m  "Why do you favor this trash?"
    
    s "I have no idea what you might be referring to."
    m "......"
    m "How touching."
    m "........"
    m "How about a trade?" 
    m "I'll leave your little Riku, in exchange for this one."
    m "You must know the importance."

    s "......."
    s  "I'm afraid my answer is no."
    
    m "How about if I throw in the doctor, for good measure?"
    s "...."
    s "The answer is still no."
    
    "What is going on? Is Mamoru trying to BARGAIN my life?"

    #Mamoru sounds a bit whiny here, as if Soume were being a mean parent and he were a petulant child.
    m  "Ehhhh? Really?" 
    m "Soume, you aren’t being very rational here." 
    m "Two go free and all I want is this useless powerless denier."  
    #-SFX sizzling noises-
    
    #Soume sounds nearly amused, but perfectly calm.
    s  "This is your last warning."
    s "I am starting to get angry."

    ro  "Soume...just leave me...save the others..."

    m  "'Save the others, Soume'. Listen to this guy. He knows what he's talking about."

    s  "Time's up."

    #play sound plants blooming and attacking.

    m  "---AUUUUUUUUUUUUUUUGH!"

    #-SFX cracking noises-

    na "Chief!  You alright there?  This guy is a quick little fucker, I'd JUST turned my---"

    m  "Shut up. Before I kill you."

    na "--y-yes, Chief."

    m  "And as for you, Soume...you are extremely lucky."

    s  "I did warn you, if you can recall."

    m "Ehehehehe..."
    m  "Indeed. Next time I'll be much more prepared."
    
    s "Until then."
    
    m "........."
    m "Call a retreat."
    na "Chief, what about the doctor guy---are we just gonna let everyone go?"
    na "This wasn't the pl---"
    m "If you want to live another night, you'll call the retreat."
    na "........."
    
    "........................"
    
    ro "...Soume..."

    s "Shhhhh. You should rest. Your arm is pretty badly broken."
    
    "....................."
    
#[Scene 48]
label Scene48:
    r  "Did you hear that?"

    "I sit up and peer off into the forest. I can’t see much beyond the trees right in front of us."

    k  "Hear what?"

    r  "I heard...I dunno...it sounded like a scream.  Or something."

    k  "A scream?  How absurd.  I would be able to tell if there was trouble, remember?"  
    k "Sometimes I wonder if you just say things for the attention of it all."

    r  "No, I’m positive I heard something."

    "Doctor Osamu shakes his head at me and lets out a long exasperated sigh."

    k  "If you don’t mind, I'm actually trying to be useful."

    r "Whatever."
    
    "I should be out there with Roman and Soume right now. Instead I'm here. Babysitting the punk."

    "Another noise."

    r  "Did you hear it that time!  It sounded like a voice."

    "Kazutaka sits up and looks around.  It seems he heard it this time too.  Something faint a little ways away."

    r  "Hello?  Soume?  Roman?"

    "Just then Soume busts through the treeline carrying Roman.  Roman’s arm is bent in a way it shouldn’t be and he looks like he’s barely conscious."

    r  "Holy fucking shit---"

    s  "Be quiet. Back up a bit. Give me some space."
    
    "I back away, covering my mouth. I feel sick."

    k  "No..."
    k "This can't..."

    r  "What the hell HAPPENED out there?"

    s  "Mamoru."

    "Soume doesn’t look up from Roman.  He’s doing something to his arm, and Roman doesn’t particularly seem to be liking it.  His face is twisted in pain."

    ro  "Nnngh..."

    k  "This can’t be happening."

    "Doctor Osamu is pacing back and forth, running his hands through his hair and mumbling things to himself.  He looks wild, and a little fucking frightening."

    r  "...this...this isn't the time to freak out..."
    
    "His freaking out is making ME want to freak out."

    k  "No.  NO!  I WILL NOT RELAX! Why couldn’t I sense the danger?"

    s "I TOLD YOU to be quiet." 
    
    "Now I'm really scared."
    "I've never heard Soume raise his voice."
    "Ever."
    
    "Doctor Osamu is wringing his hands together and closes his eyes, tightly.  It seems like he’s really fucking concentrated on something.  Or that he’s constipated."

    k  "This isn't possible, it's just not--"
    k  "How can this be happening..."

    "I turn, because I want to yell something something horrible at him, but there's something darting out of the forest."

    r  "LOOK OUT!"

    "Doctor Osamu turns, but Akiko is already on top of him." 
    "I feel something start to burn within me." 
    "What should I do? He's going to die!"

menu:
        "Use your skills.":
                jump badend4
        "Use your instincts.":
                jump Scene49

label Scene49:

    "I run over in front of Doctor Osamu.  I have no idea what I’m doing.  It’s like my body is moving on its own."

    s  "Riku!"

    gir "HAAAAAAAAAAA!"

    r  "Stop!"

    "I can feel my body glowing.  An intense power, one I’ve never felt before is pulsating inside of me."
    
    "My vision goes white."

    "Somewhere, far away, I think hear someone scream."  
    "It’s hurting my ears. I just wish it would stop."

    "The flames finally stop coming, and I collapse on the floor, exhausted."  
    "My vision slowly returns, and I look up." 
    "Now I know where the screams were coming from."

    r  "Ah--"
    
    "Where Akiko was standing is now just a charred corpse."
    
    r "No---no, I didn't mean to---"

    "I just killed a man."

    k  "HURK!"

    "Doctor Osamu is vomiting behind me.  He looks shaken, the first time I’ve ever seen him drop his confident demeanor.  It could be the smell.  Like fucking burnt hair and rotten meat."

    ro  "Riku, are you okay?"

    "Roman places his hand...his good hand...on my shoulder."
    "Soume seems to have at least gotten his arm fixed somewhat, and in a sling."

    r  "I-I didn’t mean to!  I don’t know what happened!  I just--"

    s  "Calm yourself, Riku."

    r  "I-I-I....I fucking killed her, Soume!"
    r "We were supposed to save her, now she’s dead!"

    s "Shhh..."

    "Roman is staring at what used to be Akiko. He looks green."

    "Soume crushes something in his hand and blows it in my face, in Roman's face and around the clearing."

    s  "You can’t blame yourself for this.  You saved Doctor Osamu’s life. He would have died."

    "I know that. I know she was going to kill Doctor Osamu. I know what I did was in self-defense. I---"

    "I'm calm...the pollen is doing its work."

    k  "Ngh."

    "The pollen seems to be working on him, as well."
    
    k  "They found me--they knew I was here...they’re coming for me."

    s  "Doctor, please."

    "Doctor Osamu drops his volume, sitting down in a pile of upset."

    k  "I knew we shouldn’t have split up."
    k  "I'm a dead man..."

    ro  "Doctor Osamu, Mamoru himself said he had come here for me.  Soume isn’t--"

    k  "Why would he come here for you? You’re worthless! There are dozens of yous out there. You’re nothing!  It is me they want. How can you not see that, you simpleton?"

    "Roman looks hurt.  Worse than what Mamoru did to him.  He just stands there, trying to stammer something out."

    "I stand up quickly, to defend him, but suddenly everything is spinning. I used too much energy."

    "I fall back."
    "I'm going to pass out."

    ro "Riku!"

    s  "He’s fine."

    ro  "What's going on...?"
    ro "Why would Akiko attack us...?"
    
    s "I'm...not sure."

    k "Thank god Riku DID something!"
    k  "I would’ve been dead, if it was up to you two incompetent apes."

    s  "Doctor, please, calm yourself.  I need you and Roman to escort Riku back to the rescue.  Make sure he gets back to Miss Susa and let her know what has happened."

    k  "And what about you?  Why don’t you do that yourself?"

    s  "There are numerous dead bodies here. Someone has to clean up or there will be issues."

    k  "I'm sure. Not setting another trap, are you?"
    s "..........."
    k "Speechless, are you?"
    
    ro "DOCTOR!"
    
    s "It is fine, Roman."
    s  "If I was planning another trap, I trust you would actually warn for it, this time."

    k  "I--that isn’t..."

    s  "I need to take care of all of the bodies.  We cannot allow them to be discovered. Please return home. I will join with you shortly."

    k  "................"

    s  "Are we clear?"

    k  "...fine.  But only because I want to get out of this area as quickly as I can."

    ro  "Be careful, Soume."

    s  "You be careful. I'll come back to you soon."

    k  "Let’s go.  I’m in no mood to stick around."

label Scene50:
    #The narrator here is Roman, now.
    "I’m having that dream again.  The one I always have when I’m nervous or exhausted.  I’m back in Russia.  Enslaved and scared."

    "There's a boy in the cage next to me." 
    "He's trying to talk to me. He's trying desperately to connect with me, to make a friend."
    "I don't answer him."
    "I know better."
    
    "And then the man comes."

    "I move all the way to the back of the cage, where the candle light doesn't touch."
    "Don't pick me."
    "Pick him."
    "Don't pick me."

    "He picks the boy next to me."
    "The boy calls for me, calls out to me for help."
    "I don't reply."
    "I can't risk them taking me, instead."

    ro  "AHHHHHHHHHHHH!"

    "I wake up with a start and look around my room.  To my surprise, Soume is in there with me."

    ro  "Soume?"

    #Soume sounds solemn.
    s  "How are you feeling?"

    ro  "I'm alright...you’re back already?"

    s  "Oh yes, I’ve been back for quite some time now."  
    s "I came in to check on you. Maybe make your room a little more cheery! It could use some more flora."

    "He smiles and backs away from my dresser to show me several plants he just finished potting."

    "My face is hot. It's always like this when Soume is around."
    ro  "I---you didn't have to..."

    "My room smells wonderful. Soume knows his way around plants...I feel like I'm floating, and Soume looks so--"

    s  "Shhhhh. Someone needs to worry about your health when you won't. I'll be your nurse."
    
    "He smiles at me."
    "I can feel my body melting."

    ro  "Right.  Ah, well...ahem.  Yes, thank you. I-I...appreciate your company."

    s  "It's no trouble at all."

    "He’s back to working with his plants." 
    "I want to say something else, but I end up holding it in." 
    "I don’t know why...the time just doesn’t feel right."
    "I'll tell him eventually."
    "One day."
    "I'll tell him how I feel."

    ro  "How is Riku doing?  He was just coming to last time I saw him."

    s  "Ah, physically, he is fully recovered. He is remarkably strong for his age...overusing energy is one of the highest natural death causes for Majin."

    ro  "Yeah, he is rather unique. My ability doesn't just manifest like that." 
    ro "And he's so much younger than me..."

    "Soume flinches, as if he knew what I was about to ask."

    s  "I was actually on my way to visit him just now.  With a power like his, I’m afraid we might need to have a couple more training sessions..."

    ro  "I’ll come with.  Let me just grab my-"

    s  "No, no, you stay here."

    "He puts his hand on my shoulder, and my body suddenly feels like it's on fire."

    s  "Get a little more rest. Please."

    ro "I...alright. I will, if you think I need it."
    
    s "I absolutely do."
    
    "I try to take in a breath." 
    "It's hard to...while his hand is still touching me."
    
    "He suddenly pulls back. He must've notice me blushing."
    "How embarrassing."
    
    ro "N--what is it?"

    s "You...should get that rest. I'll pay Riku a visit and come back in a little while to check on you."
    
    ro "Oh...yes. I will. Thank you."
    #play sound  Door closing

label Scene51:
    k  "Ah.  Soume.  So nice to run into you."

    s  "Doctor Osamu.  Did you just finish checking up on Riku?  I was just heading in myself."

    k  "Yes.  I was monitoring his progress.  I would prefer it if you did not interfere by trying any of your little parlor tricks."

    s   "Doctor, you always manage to make me laugh with your teasing."

    k  "I can assure you, Soume, I am completely serious with my warning."

    s  "If you please, we both have Riku’s best interest at heart."

    k  "Do we?"

    s "............"
    s  "I'm not sure of your implications."

    k  "No need to play stupid, Soume.  You might be oblivious, but you’re smarter than I'd prefer to give you credit for."
    
    s  "Excuse me?"

    k "Hn."
    k "It's no matter."
    k  "Just keep your plants and silly shamanism away from him."  
    k "Only one of us is an actual doctor, and I can assure you that I don’t need your help."

    s  "With all due respect, Doctor--"

    k  "With all due respect, Soume, I honestly don’t care for your opinion." 
    k "I am a medical professional, and I know exactly what I am doing."

    s  "Doctor, I only want--"

    k  "What you want is irrelevant. Miss Susa has put me in charge of Riku’s wellbeing and I don’t want you interfering with my medicine."

    s "..........."
    s  "I understand."

    k  "Good."
    k "And when the time is right, Soume...I'll reveal you for what you really are."
    k "Now, if you excuse me-"

    s  "May I ask, Doctor Osamu, what your problem is with me?"

    k  "Oh, you've noticed, have you? Well you are the perceptive one! Your sensory abilities clearly rival even my own!"

    s  "..."

    k  "Listen carefully. The others here might be stupid enough to buy into your whole act, but I can assure you I am not that dense."

    s  "You've always been unnaturally paranoid, however this is too m---"

    k  "I know you’re up to something, you pathetic little cretin.  And I--"

    s  "I can assure you that you don’t know what you’re talking about. Even considering our past...incident."

    k "....................."
    k  "Kch. I should've known you'd never let me live that down."

    s  "All things considered, Doctor, how could I possibly?"
    
    k "...rgh..."
    k  "I will expose you.  It is only a matter of time.  You will find that engaging me in a battle of wits will leave someone of your capacity sorely outmatched."

    s "............."
    s  "You may be right. Do have a lovely day, Doctor."

label Scene52:

    "I finish taking whatever gross thing Doctor Osamu just gave me."

    #Riku is gargling something here.
    r  "Ugh, that’s gross."

    "It tastes like raw eggs and old fish." 
    "He tried to explain to me what it was...something about replacing something and increasing my something with something something."

    #play sound knocking

    r  "Aw man."

    "I consider pretending to be asleep, but knowing Doctor Osamu he’d just barge in anyway and inject me with something he was testing."

    r  "Come in. I guess."

    s  "Is this a bad time?"

    r  "Oh, Soume, it's you. No, come in. I just thought you were Doctor Osamu again, is all."

    #Soume giggles.
    s  "Ah! Then I guess I can’t blame you."

    r  "Yeaaaaaah. So what'd you bring?"

    "Soume is carrying a plate with something on it.  He put it behind his back quickly."

    s  "Uh...well, I don’t know if you’d want it...I probably shouldn’t even have brought it here now that I think about it..."

    r  "Show me! Show me!"

    "It smells like food, and I'm starved!"
    
    s  "It’s just a...uh...burger."

    r  "A burger!"

    "I grab it from the plate before Soume can push me away and I finish half of the think my first bite."

    r  "MMM!!!  This is delicious!  Mmm...kinna different though. What kind of meat?"

    s  "No, that’s what I wanted to talk to you about before you started.  It is a...different meat."

    r  "Hm...I’ve had bison before, so I know it isn’t that...hmm....I give up.  What’s this?"
    
    s "..........."
    s  "It is...lamb."

    r  "Lamb burger, huh?"
    
    "Lamb is awesome."
    
    r "You're a great chef."
    
    #Soume says thank you nervously.
    s  "Yes...thank you...at any rate, Riku, I really wanted to talk to you more about your training."

    r  "Awww....I thought I was finished with that."

    #Soume chuckles.
    s  "Training never ends, Riku. There is always something to learn."

    r  "Yeah...I don’t know how I did it, and I felt like I wasn’t even in control of it.  It just...happened."

    s  "It isn’t anything to be ashamed of.  You’re quite unique, even amongst us Majin.  We just need to help you control them."

    r  "Yeah."

    s  "Today, you should rest. We'll resume training again next week."

    "I guess I won't mind training more. I’d rather not explode and take out a city block."

    r "Well, thanks for the burger. I feel much better."
    s "........."
    s "I'm glad."
    s  "Now that you're full, lie back down. I’m sure Doctor Osamu will be back to check in on you shortly."

    r  "Ugh, I should hide from him, instead."

    # Soume giggles.
    s  "Try to take it easy, Riku. You’re more important to this rescue that you realize."
    r "What do you mean?"
    s "Well...we'll see."
    
    "No less cryptic, that guy."

label Scene53:
    ro  "Hey Riku!  Hold on!"

    "I am on my way over to the phone."
    "I’m not supposed to leave my room, but I want to talk to my parents." 
    "I just need to hear their voices even for a minute."

    r  "Hey Roman."

    ro  "I just wanted to make sure you were alright."

    r  "Yup.  How about yourself?"

    ro  "Don’t worry about me.  I’m afraid Soume made a bigger deal over my arm than he should have."

    ro  "Anyway...I just though I'd ask because you seemed a bit shaken."

    r  "Nah. I’m fine.  Just got a little dizzy, was all."

    "I smile, but only to get Roman to drop it. I don't want to think about it."
    "The fact that I killed someone."

    ro  "Of course. Just let us know if you need more time to recover. We want you to be fully healed before you start exerting yourself again."

    r  "Sure thing.  Thanks."

    "I duck quickly into the phone room and  call up my parents."

    ma  "Hello?"

    r  "Hey Mom, it’s me."

    ma  "Riku! Oh, I’m so glad to hear from you!"

    r  "Yeah, I figured it had been a little while since I called last, so I just wanted to call and say hi."

    ma  "Tell me everything. How is training going?"

    r  "Great. Training is great. I finished up most of my introductory level stuff last week."

    ma  "Really!  Already? You've always been a good student..."

    r  "Yeah, they were sort of surprised here too.  Supposed to take like two years or something normally."

    ma  "Honey, that’s amazing!  I’m so proud of your...gifts."

    r  "I was actually sent out on my first mission the other day."

    ma  "Mission? That sounds dangerous, I'm not sure I like that---"

    r  "Mom, I was fine.  Actually, I-"

    "I swallow hard.  I want to tell her what happened.  I don’t want to hide anything from her."

    ma  "Yes?"

    "But I don’t want her to look at me differently. I killed someone. With my powers. I can’t tell her that."

    r  "I wasn’t in danger at all.  We didn’t run into any trouble."

    ma  "That’s good, then.  Still, I think this is too early for you to be going out and doing things so dangerous..."

    r  "I’ll tell Miss Susa."

    ma  "So, when are you coming to visit?"

    "She sounds hopeful.  Like me getting my first mission means I’m good enough to go back into the world."

    r  "I don’t...well, soon hopefully.  Yeah, I should be able to come visit you guys soon. Just...not yet. I'll ask, though."

    ma  "Oh...I see. Tell me the moment you can, I'll make all your favorite foods."
    
    "I  can't do this anymore. My chest feels tight."
    
    r "Hey Mom, I...I gotta go. New training session is coming up in a few minutes."

    ma  "Oh, of course...it was great hearing from you. Make sure you call me again soon."

    r  "Sure thing."

    ma  "And brush your teeth."

    r  "I will."

    ma  "And don’t give them too much trouble."

    r  "I--I won't..."

    ma  "And...be safe."

    r  "...I love you, Mom."

    ma "............."
    ma  "I love you too, Riku. See you soon."

    "I hang up the phone. I don't think it helped, much."

label Scene54:
    su  "So, how is the little sprog, Doctor?"

    r  "I keep telling you, I’m-AH-fine."

    k " Hmm...yes, his color is finally starting to return."

    su  "I told ya to be careful out there!  And look what you’ve gone and done. Taken yourself out of three days worth of cleaning."
    su "I bet you did it on purpose."

    r  "Aw come on, this wan’t my fault.  I didn’t know it was gonna happen like that."

    su  "You’ll be pulling double shifts next week just to make up for it!"

    "Miss Susa never changes."
    "It's kind of comforting."

    k  "Well, I believe he is back at nearly full health.  I’ll be taking him off of bed rest starting tomorrow."

    su  "About fucking time."

    "Susa frowns and stares at me.  She's almost being nice to me, today."

    su  "You sure you’re all right? I don’t want you passing out and getting blood on the linoleum, cause someone's gonna hafta clean that."

    r  "Yeah, yeah.  I’m fine.  Don’t worry.  Your floors will be sparkling."

    su  "Good.  Good.  Just worried about the floors, you see."

    r  "I get it."
        
    k "Ahem...Riku?"
    
    r "Yeah?"

    k  "Ah, thank you.  For...saving my life."

    r  "Yeah.  Don’t mention it."

    k "........"
    su ".........."
    su "Riku..."
    su  "You know you didn’t do anything wrong?"

    r  "..........."

    su  "So don't look like that. There will be others, and they will need you at your best, and sometimes...there will be sacrifices."

    r  "Heh.  Thanks, Miss Susa."

    "Nice to know she believes in me. Makes me question myself a bit less."

    su  "Well. Yeah. Get ready to get back to fucking work, you hear me? No more freeloading if you want to eat. Now get some rest. I’ll be around if you need to talk."

    "Susa heads off. Doctor Osamu is still hanging around, his head down."

    k  "Thanks again.  Sorry for things I might have said or thought earlier about you."

    r  "Huh?"

    "Did Doctor Osamu just tell me he was sorry?  Doctor Osamu?  That was one word I thought was missing from his vocabulary."

    k  "Ahem. Yes, well, I’ll be around in my lab. If you’d like to help me. I could use an assistant, and you do seem less moronic than most of the people I run into."

    r  "Uh...thanks."

    "He nods his head at me at gives a really weak looking smile that looks like is causing him physical pain."

    r  "So...I can go?  I’m not required to sit around in my room any longer?"

    k  "Yes, I have now officially cleared you. Too late to start training or whatever else silly thing Soume would have you doing, but you can at least leave your room for the evening."

    r  "Finally. Getting cabin fever just sitting here like this."

    k  "Right. Well..." 
    k "I’ll be back down in my lab if you need me. Feel free to stop by later if you need anything."

    "Doctor Osamu leaves my room and heads off. I finally have some FREE TIME!"

    "I could head to the lab and work with the Doctor..."
    "Or I could go check in on Roman.  Make sure he’s doing all right and everything.  I haven’t talked to him much recently, and he’s always happy to see me."
    "I could also talk to Miss Susa about everything."

    r  "Hmmm..."
    
    $ susa_arc = False
    $ kazu_arc = False
    $ main_arc = False
menu:
    "Visit Susa.":
        $ susa_arc = True
        jump endarc
    "Visit Doctor Osamu.":
        $ kazu_arc = True
        jump endarc
    "Visit Roman.":
       $ main_arc = True
       jump endarc

label endarc:
    $show_message("You have completed the first half of the game.", "medium")
    $show_message("From here, the game will follow the story of the character you've most clicked with.", "medium")
    $show_message("Saving is heavily advised.", "medium")

menu:
    "Continue.":
        if susa_arc:
            jump su1
        elif kazu_arc:
            jump kaz1
        elif main_arc:
            jump main1



