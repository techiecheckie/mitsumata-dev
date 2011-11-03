######################
# Roman's Birthday Game
######################
label birthdaygame: 
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
   
    if (gift and decor and loca and bircake and surp):
        jump birthdayresults
    else:
        "I need to figure all this stuff out."
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
    if cake:
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
    if count = "5":
        jump perfectparty
    elif count = "4":
        jump decentparty
    elif count = "3":
        jump okparty
    elif count = "2":
        jump fehparty
    elif count = "1":
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
    #$ unlock_item("boob")
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
#label kazuquiz        
