######################
# Roman's Birthday Game
######################
label birthdaygamemenu: 
    $show_message("You are in charge of throwing Roman a great coming-of-age party.", "medium") 
    $show_message("To throw the best possible party, you will need to get the right gift, fitting decorations, pick the best place in the temple to have the party, a delicious cake, and a special surprise to top it all off.", "large")
    $show_message("Try to do a good job!", "medium")
    
    scene bg riroom with fade
    $show_main_ui()
    r "Where do I start...?"
    $ perparty = False
    $ gift = False
    $ decor = False
    $ loca = False
    $ bircake = False
    $ surp = False
    $ corrgift = False
    $ corrdec = False
    $ corrloc = False
    $ corrcake = False
    $ corrsur = False
    $ count = corrgift + corrdec + corrloc + corrcake + corrsur       
    
label birthdaygame:        
   
    if (gift and decor and loca and bircake and surp):
        jump birthdayresults
    else:
        "I still need to figure stuff out."
menu:
            "Figure out a gift.":
                 jump bgift
            "What kind of decorations...?":
                 jump bdecor
            "Where to put this thing?":
                 jump bloca
            "What kind of cake?":
                 jump bcake
            "A special surprise...?":
                 jump bsurp
    
label bgift:
    if gift:
        jump diditalready
    else:    
        r "Okay. I need some kind of gift. Who should I ask about that?"
menu:
            "Ask Doctor Osamu.":
                jump gosamu
            "Ask Soume.":
                jump gsoume
            "Ask Susa.":
                jump gsusa
            "Ask Liza.":
                jump gliza
            "Do it myself.":
                jump gself
                
label diditalready:
    $show_message("You already have this. Go to the next item on your list.", "medium")
    jump birthdaygame
    
label gosamu:
    show bg lib with dissolve
    r "Hey Doctor Osamu, I need a gift for Roman's birthday."
    k "Mmmm. How about a nice scientific text?"
    r "Hmmmm."
menu: 
        "Accept gift.":
                $ gift = True
                jump birthdaygame
        "Maybe something else...":
                jump bgift
label gsoume:
    show bg soroom with dissolve
    r "Hey Soume, I need a gift for Roman's birthday."
    s "How about this little maneater plant? I think he'd adore it!"
    r "Are they dangerous...?"
    s "...mmm, that is a curious question..."
    s "Define 'danger', exactly..."
menu: 
        "Accept gift.":
                $ gift = True
                jump birthdaygame
        "Maybe something else...":
                jump bgift
label gsusa:
    show bg suroom with dissolve
    r "Miss Susa, what do you think Roman would like as a present?"
    s "Isn't figuring that out YOUR job?"
    r "Yeah, but--"
    s "How about this? It's an old video game I'm not using."
menu: 
        "Accept gift.":
                $ gift = True
                jump birthdaygame
        "Maybe something else...":
                jump bgift
    
label gliza:
    show bg hall1 with dissolve
    #play sound phone ring
    l "Hello?"
    r "Hey um, Liza, this is Riku..."
    l "Oh, hello there, Riku. It's nice to finally get to chat with you."
    l "What did you need?"
    r "Roman's birthday is coming up, and I'm not sure what to get him."
    l "......."
    l "I think a spice rack, with exotic spices already set up."
menu: 
        "Accept gift.":
                $ gift = True
                $ corrgift = True
                jump birthdaygame
        "Maybe something else...":
                jump bgift
label gself:
    r "I can figure this out. What would Roman want for his birthday?"
    r "Maybe some good, powerful sake!"
menu: 
        "Accept gift.":
                $ gift = True
                jump birthdaygame
        "Maybe something else...":
                jump bgift
    
label bdecor:
    if decor:
        jump diditalready
        
    else:    
        r "Okay. I need decorations. Who should I ask about that?"
menu:
            "Ask Doctor Osamu.":
                jump dosamu
            "Ask Soume.":
                jump dsoume
            "Ask Susa.":
                jump dsusa
            "Ask Liza.":
                jump dliza
            "Do it myself.":
                jump dself

label dosamu:
    show bg lib with dissolve
    r "Doc, I need to figure out some decorations for Roman's party. Can you help?"
    k "W-what? I don't have a clue...try a rancid bacterial theme or something!"
    k "And close the door when you leave, I'm busy!"
    #play sound doorslam
    r "Hmph."
menu: 
        "Accept decor.":
                $ decor = True
                jump birthdaygame
        "Maybe something else...":
                jump bdecor
label dsoume:
    show bg soroom with dissolve    
    r "I'm having some trouble figuring out what kind of decorations Roman would like, Soume."
    s "Hmmm. I have an idea..."
    r "Really?"
    s "How about an elaborate floral arrangement?"
menu: 
        "Accept decor.":
                $ decor = True
                $ corrdec = True
                jump birthdaygame
        "Maybe something else...":
                jump bdecor
label dsusa:
    show bg suroom with dissolve
    r "Miss Susa, sorry to bug you, but I just wanted to figure out some decorations for Roman's party..."
    s "Video game themes are always perfect."
menu: 
        "Accept decor.":
                $ decor = True
                jump birthdaygame
        "Maybe something else...":
                jump bdecor
label dliza:
    show bg hall1 with dissolve
    #play sound phone
    l "Hello?"
    r "Hi Liza, it's Riku..."
    l "Ahh, hello there."
    r "I can't figure out what kind of decorations to use for Roman's birthday party. What do you think he'd like?"
    l "Hmmm, how about colorful cloth?"
menu: 
        "Accept decor.":
                $ decor = True
                jump birthdaygame
        "Maybe something else...":
                jump bdecor
label dself:
    r "I'm a smart kid. Decorations should be easy!"
    r "..."
    r "............."
    r "The temple is already pretty decorative by itself."
menu: 
        "Accept decor.":
                $ decor = True
                jump birthdaygame
        "Maybe something else...":
                jump bdecor
    
label bloca:
    if loca:
        jump diditalready
        
    else:    
        r "Okay. I need someplace to put this. Who should I ask about that?"
menu:
            "Ask Doctor Osamu.":
                    jump losamu
            "Ask Soume.":
                    jump lsoume
            "Ask Susa.":
                    jump lsusa
            "Ask Liza.":
                    jump lliza
            "Do it myself.":
                    jump lself

label losamu:
    show bg lib with dissolve
    r "Hey Doc, where do you think I should have Roman's birthday party?"
    k "You can have it in the library if you clean it from top to bottom."
    "This place is pretty filthy..."
menu: 
        "Accept location.":
                $ loca = True
                jump birthdaygame
        "Maybe something else...":
                jump bloca
label lsoume:
    show bg soroom with dissolve    
    r "Soume, you got any ideas for where to hold Roman's birthday party?"
    s "Well, holding it in this room might be fun!"
    s "We can play 'dodge the cake-eating plants' as a game!"
    s "Doesn't that sound like such fun?"
menu: 
        "Accept location.":
                $ loca = True
                jump birthdaygame
        "Maybe something else...":
                jump bloca
label lsusa:
    show bg suroom with dissolve
    r "Miss Susa, I can't think of a good place to hold the party."
    s "Mmm. I guess you can use the main room. It's pretty big and people don't usually go in there."
menu: 
        "Accept location.":
                $ loca = True
                $ corrloc = True
                jump birthdaygame
        "Maybe something else...":
                jump bloca
label lliza:
    show bg hall1 with dissolve
    #play sound phone
    l "Roman?"
    r "Uh, sorry, it's Riku...I wanted to ask about Roman, though?"
    l "Oh, hello, Riku. Ask away."
    r "Where do you think is a good place to have his birthday party?"
    l "Hm. How about the kitchen?"
    l "As long as someone's cleaned it..."
    "I'm not sure if it's clean..."
menu: 
        "Accept location.":
                $ loca = True
                jump birthdaygame
        "Maybe something else...":
                jump bloca
label lself:
    r "Alright, a location, location, location..."
    r "How about right in Roman's room? It's not that big, but that'll be surprising!"
menu: 
        "Accept location.":
                $ loca = True
                jump birthdaygame
        "Maybe something else...":
                jump bloca      
    
label bcake:
    if bircake:
        jump diditalready
        
    else:    
        r "Okay. I need a cake. Who should I ask about that?"
menu:
            "Ask Doctor Osamu.":
                    jump cosamu
            "Ask Soume.":
                    jump csoume
            "Ask Susa.":
                    jump csusa
            "Ask Liza.":
                    jump cliza
            "Do it myself.":
                    jump cself
                
label cosamu:
    show bg lib with dissolve
    r "Sup, Doc! Sorry to bug ya, but I need to know about cakes for Roman's birthday."
    k "Ahh, let me show you my newest invention, then..."
    k "........"
    k "Ta-da!"
    r "...what is it?"
    k "A cake made entirely from fungi!"
menu: 
        "Accept cake.":
                $ bircake = True
                jump birthdaygame
        "Maybe something else...":
                jump bcake
label csoume:
    show bg soroom with dissolve    
    r "Soume, I don't know where I should get a cake for Roman's birthday..."
    s "I'm not really knowledgeable about cakes..."
    s "But how about a cake from the place your mother got the one she sent you?"
menu: 
        "Accept cake.":
                $ bircake = True
                jump birthdaygame
        "Maybe something else...":
                jump bcake
label csusa:
    show bg suroom with dissolve
    r "Miss Susa, can you help me with Roman's birthday cake?"
    s "Ice cream cake."
    "...she's too absorbed in playing video games right now."
menu: 
        "Accept cake.":
                $ bircake = True
                jump birthdaygame
        "Maybe something else...":
                jump bcake
label cliza:
    show bg hall1 with dissolve
    #play sound phone
    l "Hello?"
    r "Hi there, Liza, I just had a quick question. What kind of cake do you think Roman would like at his party?"
    l "Oh my hm...perhaps decorative cupcakes?"
menu: 
        "Accept cake.":
                $ bircake = True
                jump birthdaygame
        "Maybe something else...":
                jump bcake
label cself:
    r "A cake."
    r "There are tons of recipe books in the kitchen."
    r "I bet I can find a vegan or whatever one and just make it."
menu: 
        "Accept cake.":
                $ bircake = True
                $ corrcake = True
                jump birthdaygame
        "Maybe something else...":
                jump bcake
    
label bsurp:
    if surp:
        jump diditalready
        
    else:    
        r "Okay. I need an extra surprise. Who should I ask about that?"
menu:
            "Ask Doctor Osamu.":
                    jump sosamu
            "Ask Soume.":
                    jump ssoume
            "Ask Susa.":
                    jump ssusa
            "Ask Liza.":
                    jump sliza
            "Do it myself.":
                    jump sself

label sosamu:
    show bg lib with dissolve
    r "Doctor Osamu, I need a special surprise for Roman's party. I have no clue what to get."
    k "Hm. I have an idea."
    k "Invite his friend Liza over for the day."
menu: 
        "Accept special surprise.":
                $ surp = True
                $ corrsur = True
                jump birthdaygame
        "Maybe something else...":
                jump bsurp
label ssoume:
    show bg soroom with dissolve    
    r "Hey Soume, I need a special surprise for Roman's birthday..."
    s "...special...surprise...?"
    s "...I could poison everyone..."
    s "That would be very surprising."
    r "...uh..."
menu: 
        "Accept special surprise.":
                $ surp = True
                jump birthdaygame
        "Maybe something else...":
                jump bsurp
label ssusa:
    show bg suroom with dissolve
    r "Miss Suuusaaaaa. I need help with the special surprise for Roman's birthdayyyyy!"
    s "Howsabout a punch to the face and extra chores for a month cause you keep bugging me?"
    menu: 
        "Accept special surprise.":
                $ surp = True
                jump birthdaygame
        "Maybe something else...":
                jump bsurp
label sliza:
    show bg hall1 with dissolve
    #play sound phone
    r "Hey Liza I need a special surprise for Roman's birthday. What do you think?"
    l "I...surprises aren't really my specialty..."
    l "How about a weapon he can train with?"
    menu: 
        "Accept special surprise.":
                $ surp = True
                jump birthdaygame
        "Maybe something else...":
                jump bsurp
label sself:
    r "If I just focus, it will be easy to figure out a special surprise for Roman's birthday."
    r "......."
    r "I COULD SPIKE THE PUNCH BOWL!"
    menu: 
        "Accept special surprise.":
                $ surp = True
                jump birthdaygame
        "Maybe something else...":
                jump bsurp

                
label birthdayresults:    
    r  "There. I think that's everything!"
    if count == "5":
        jump perfectparty
    elif count == "4":
        jump decentparty
    elif count == "3":
        jump okparty
    elif count == "2":
        jump fehparty
    elif count == "1":
        jump failparty
        
label perfectparty:
    su  "Looks like I picked the right person for the job. Everything looks to be in order."
    
    r  "Hey.  Thanks.  Wasn’t really expecting that."
    
    su  "Yeah, well, don’t let it go to your head.  But still, next time I need something, I guess I know who to go to."
    
    "I don’t know what to say.  I have to admit, I like the fact that Susa is trusting me with more stuff."  
    "This is way better than when she used to just beat me with whatever she had in her hand."
    "Not too sure I want more work, though..."
    
    su  "Well here. Have that. For a job well done."
    
    "Susa hands me SOMETHING HERE PLZ."
    
    r  "What's this?"
    
    su  "It's just supposed to help you out in battle. So don't say I never gave you anything."
    
    "Now I really don’t know what to say.  Susa has never given me anything before.  I look up at her, but no words are coming out."
    
    su  "Aw fuck, don’t go getting all emotional on me now.  Just take it and be glad I gave it to ya."
    #$inventory.unlock_item("boob")
    $ perparty = True
    return
label decentparty:
    su "Well, I guess this'll have to do."
    return
label okparty:
     su "Good enough, I guess."
     return
label fehparty:
        su "Could be better..."
        return
label failparty:
        su "Ugh, I don't know why I bothered to trust you with something this easy."
        return

######################
# Kazu's Quiz Game
######################
label kazuquiz:
    $show_message("Doctor Osamu wants to test your skill with a quiz!","medium")
    $show_message("Select the best answer to each question","medium")
    $show_message("Get as many correct as you can, and there may be a reward!","medium")
    
    $q1 = False
    $q2 = False
    $q3 = False
    $q4 = False
    $q5 = False
    $q6 = False
    $q7 = False
    $q8 = False
    $q9 = False
    $q10 = False
    $count2 = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10
    
    if HP >= 200:
        jump quiz1
    elif HP < 200:
        jump quiz2
        
label nextq:
    k "Okay. Next question."
    return
    
label quiz1:    
    $show_message("Question 1", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q1 = True
            call nextq
    $show_message("Question 2", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q2 = True
            call nextq
    $show_message("Question 3", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q3 = True
            call nextq
    $show_message("Question 4", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q4 = True
            call nextq
    $show_message("Question 5", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q5 = True
            call nextq
    $show_message("Question 6", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q6 = True
            call nextq
    $show_message("Question 7", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q7 = True
            call nextq
    $show_message("Question 8", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q8 = True
            call nextq
    $show_message("Question 9", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q9 = True
            call nextq
    $show_message("Question 10", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q10 = True
            call nextq    
            
label quiz1result:
    if count2 == "10":
        jump perquiz
    else:
        jump failquiz
   
label quiz2:    
    $show_message("Question 1", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q1 = True
            call nextq
    $show_message("Question 2", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q2 = True
            call nextq
    $show_message("Question 3", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q3 = True
            call nextq
    $show_message("Question 4", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q4 = True
            call nextq
    $show_message("Question 5", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q5 = True
            call nextq
    $show_message("Question 6", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q6 = True
            call nextq
    $show_message("Question 7", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q7 = True
            call nextq
    $show_message("Question 8", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q8 = True
            call nextq
    $show_message("Question 9", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q9 = True
            call nextq
    $show_message("Question 10", "medium")
    menu:
        "Wrong Answer":
            call nextq
        "Right Answer":
            $q10 = True
            call nextq  
            
label quiz2results:
    if count2 == "10":
        jump perquiz
    else:
        jump failquiz
    
label perquiz:
    k "............."
    k "It seems you've gotten all of them correctly."
    r "HAH! I WAS paying attention!"
    k "Fine. I suppose your intelligence may be...within an acceptable range."
    k "Take this."
    #$inventory.unlock_item("ITEMMMMM")
    return
    
label failquiz:
     k ".........."
     k "As I suspected, below average..."
     r "Hey..."
     k "That is all. You may go."
     r "Awww..."
     return

#########################
# SCAVENGER HUNT
#########################
label scav_hunt:
    $decision = "50"
    r "Alright, alright! I'll do it."
    ro "I do appreciate it, Riku!  These scavenger hunts are always one of my favorite things to do at the rescue."
    
    r  "This kind of thing happen often?"
    
    ro  "Oh, yes.  Not just scavenger hunts, though.  Miss Susa is very good at organizing different things to make everyone feel more at home.  Last year she put together a carnival."
    
    r  "That sounds…terrifying."
        
    ro  "Terrifying?  A carnival?  I’m afraid I don’t understand how you could be afraid of a carnival."
    
    r  "Clowns. I hate clowns."
    r "Freaky, makeup wearing creeps."
    r "I accidentally broke a clown’s nose after he tried to pick me up at the circus. They’re just weird."
       
    ro  "What an odd thing to be afraid of..."
    r "I'm not AFRAID of 'em, I just don't like them."
    ro "Suuuure."
    
    su  "Oi!  OIIIIIIIIIIIIIIII!"
    
    "The crowd had been talking fairly loudly, but as soon as Susa begins to speak, everyone shuts up.  They must all be afraid of her, too."
    
    su  "Looks like everyone is here now, so we will begin.  It is time for our annual scavenger hunt.  There are four items that each team must find."
   
    #Riku whispers.
    
    r "How do we know what we’re looking for?"
    
    su  "OI!  Sprog in the back!  If you would shut your face for two fraking seconds I’d explain it to ya."
    
    r  "Gulp."
    
    su  "Now, if everyone is ready…"
    
    "Susa is glaring at me.  She pulls out a stack of papers from her pocket and starts flipping through them and then looking around at the crowd."
    
    su  "Alright, each team of two is going to get one of these pieces of paper.  They tell you want you’re looking for.  You only get one, so if you lose it tough shit."
    
    "She divides half the stack to Soume, and they both start handing out the list to people in the front."
    
    gir  "Miss Susa, what is the prize this year?"
    
    su  "Woops, thank you.  I almost forgot.  First prize this year is one thousand dollars to spend as you wish."
    
    r  "Whoa!  Good call on waking me up Roman."
    
    #Roman chuckles.
    
    ro  "I told you that it would be enjoyable."
    
    su  "Here ya go, brat.  Try not to lose it."
    
    "I look down the list really quick."
    
    r  "Huh?  All of this is here?  At the rescue?"
    
    ro  "Yes, these items are hidden around here somewhere."
    
    r  "Ugh.  I’ve never seen any of these."
    
    su  "Alright, first to find all of the items on the list wins.  Ready?  Annnnnd….go."
    
    "People take off running in every direction.  Soon, only Roman and I are left."
    
    r  "So…where should we start looking?"
    
    ro  "Hmm…why don’t we start around here?  This seems to be one of the few places we won’t be bumping into other Majin."
    
    r  "‘Kay.  Sounds good to me.  Lemme see here…hrm.  Might as well just start looking around then."
    
    #-Insert minigame here.  This is a hidden objects minigame.  Help Riku and Roman find the objects that Susa has indicated.  There are multiple screens to search, so be sure to check them all.-
    # Use a combination of puzzle logic and the searchable screens for this minigame, no massive new programming.
label succeed:    
    r  "That should be the last of them, I think."
    
    ro  "Let me just double check…hmm…yep!  That’s it.  Lets go tell Miss Susa."
    
    r  "Hey, Susa!  SUUUUUSA!"
    
    su  "WHAT?  Damn, could you not fucking yell.  I’m not deaf."
    
    r  "Er…sorry.  Just wanted to tell you we’re done."
    
    su  "Hmph.  Already?  Lemme check what you have."
    
    su  "Hmm…yup."
    
    su  "Looks good.  Congrats, kids.  Dunno how you did it so quickly, but you won."
    
    ro  "Excellent job, Riku!  I’ve never managed to win one of these before."
    
    su  "Sure it had more to do with you than the brat here.  Here’s the prize.  Wait here for everyone else to finish.  I don’t want you ruining this for the others."
    
    r  "Fine by me.  I’ll just sit here and count my money."       
