####################
# NEUTRAL ENDINGS
####################

label neuend00:
    scene bg blackscr
    $show_main_ui()
    with dissolve    
    r "You really want me to move in with you?"
    l "Absolutely. I am a woman of my word."
    r "I guess...it mght be nice to..."
    r "Okay! Lemme just say g'bye and get my stuff together! Come get me in a week?"
    l "That sounds perfect."
    
    "Roman decides to live with Liza at her place, something he's always wanted."
    "But as his car takes off, and the temple fades away into the distance, Roman can't help but wonder if he's forgotten something important..."

    $hide_main_ui()
    show bg blackscr
    with slow_dissolve
    
    $show_message("You got a neutral ending.", "medium")
    $show_message("Not bad, but you might've left things before they were settled.", "medium")
    jump neu_over
    
label neuend0:
    scene bg blackscr
    $show_main_ui()
    with dissolve
    s "No. This is my home. I don't want to leave it."
    l "I understand your feelings, Susa."
    l "...I'll miss you."
    s "...Liza..."
    "Susa's life went well, but she never saw Liza again."
    "She'd always wonder what could have been..."
    $hide_main_ui()
    show bg blackscr
    with slow_dissolve
    
    $show_message("You got a neutral ending.", "medium")
    $show_message("Not bad, but you might've left things before they were settled.", "medium")
    jump neu_over    

label neu_over:
    $hide_main_ui()
    with slow_dissolve
    $show_message("A decent first try, though.", "medium")
    $show_message("Play again, but this time remember what's important...", "medium")
    return


####################
# BAD ENDINGS
####################

label badend1:
    scene bg blackscr
    $show_main_ui()
    with dissolve
    r "I run away from this tall freak. I run and run and run and----"
    r "HRRRRRRRK!"
    m "Hm. Dinner to go."
    r "No--NOOOOOOOOOO!"
    $hide_main_ui()
    with slow_dissolve
    
    $show_message("Your instincts were just off this time around...","medium")
    $show_message("Sometimes you have to think ahead to get ahead.","medium")
    jump game_over
    
label badend2:
        scene bg blackscr
        $show_main_ui()
        with dissolve
        r "No way. I'm not buying that bitch a new gun!"
        r "SHE broke it!"
        su "............."
        #play sound fighting
        r "Aaaaaaaagh!"
        su "WHAT THE HELL---DID I TELL YA----BOUT CUSSIN----IN MY DAMN HOUSE---!"
        $hide_main_ui()
        with slow_dissolve
        
        $show_message("You pissed Susa off so bad with your idiot stunting that she kicked you out of the shrine.","medium")
        $show_message("Try being more appreciative of what others sacrifice so you can have a pleasant and easy life, you big jerk!","medium")
        jump game_over

label badend3:
        scene bg blackscr
        $show_main_ui()
        with dissolve
        "If I run away now, what was the point of my training?"
        "I'm gonna stay and help."
        "I rush out into the fray, my hand aflame, ready to rock!"
        #play sounds fighting
        "I hit the first guy. He goes down."
        r "YEAAAAAAAAAAAAAAH!"
        ro "Riku, behind you!"
        #play sound, squelch
        show bg redscr
        r "...agh--"
        "Someone...behind me...they..."
        "...it's going dark..."
        show bg dream
        with dissolve
        ".............."
        show bg blackscr
        $hide_main_ui()
        with slow_dissolve
        $renpy.pause(2.0)
        
        $show_message("You really need to learn how to listen to people with more experience than you...","medium")
        $show_message("Thinking you're a hotshot doesn't make you one.","medium")
        jump game_over  
        
label badend4:
    scene bg blackscr
    $show_main_ui()
    with dissolve
    "I've trained for this. I can do this."
    "I light the dark fire in my hand and lunge at her to get her away from Doctor Osamu."
    "She---"
    "She dodges and kicks me in the back of the knee!"
    "Oh god, my leg, she's broken my leg---"
    #play sound squelch
    r "...aaagh."
    "Hot. There's pain in my chest. So hot. I'm burning up. I'm..."
    "...cold."
    show bg dream
    "................."
    show bg blackscr
    $hide_main_ui()
    with slow_dissolve
    $renpy.pause(2.0)
    
    $show_message("Unfortunately for you, your skills just weren't where you thought they were.","medium")
    $show_message("Be more careful with that arrogance next time.","medium")
    jump game_over
    
label badend5:
    scene bg blackscr
    $show_main_ui()
    with dissolve
    "As quickly as I can, I manage to summon a fireball and send it in the hunter’s direction. She sees me and avoids it."

    "In one swift motion, she runs Doctor Osamu through with his sword."
    "He crumples to the ground, mouthing something at me as blood spills over his lips."
    "I freeze up---I can't---no---"

    "I feel something in my back.  Something cold and sharp."

    "I look down.  The end of that sword is sticking out through my shirt."

    "I look up at Soume."
    "He isn't even paying attention."
    "He's still...healing...Roman..."
    
    "I try to call out, to say anything, but the blade is twisting its way deeper into me." 
    "I can’t feel anything anymore."

    "I close my eyes."
    "...it's...dark..."
    show bg dream with dissolve
    "..........................."
    show bg blackscr
    $hide_main_ui()
    with slow_dissolve
    
    $show_message("To live life is to learn lessons.","medium") 
    $show_message("You haven't learned everything you need to know to continue with this life.","medium")
    $show_message("Go back and consider some of your actions more carefully.","medium")
    $show_message("You'll find it makes all the difference.","medium")
    jump game_over
    
label badend6:
        scene bg blackscr
        $show_main_ui()
        with dissolve
        "Roman and I are just watching TV, enjoying ourselves."
        #play sound loud knocking
        r "C'mon in!"
        "Soume all of a sudden bursts into the room, looking very upset."
        ro "...Soume, is everything okay?"
        s "............"
        s "Hn."
        s "It will be now."
        "He's growing a plant like I've never seen before!"
        "It's so bright and vivid, though kinna scary."
        "It's opening its mouth and----"
        #play sound whumpfwhumpfwhumpf
        "...I--so...dizzy...all of a---"
        $hide_main_ui()
        with slow_dissolve
        
        $show_message("Soume got rid of you because you just weren't very kind to him.","medium") 
        $show_message("Next time, try not to be a callous jerk!","medium")
        $show_message("What YOU think is funny just might not be funny to everyone else, and maybe you wouldn't be in this mess if you'd paid more attention to that.","medium")
        jump game_over
        
label badend7:
    scene bg blackscr
    $show_main_ui()
    with dissolve
    "How can I deny my own people?"
    "I grin at Liza, and start to laugh."
    l "...Susa..."
    su "Hey, it's pretty damn funny!"
    l "........"
    $hide_main_ui()
    with dissolve
    $show_message("Later that night, while you're sleeping...","medium")
    $renpy.pause(1.0)
    
    $show_message("Liza makes a masterful break out, finally freeing herself from the clutches of your nasty family.","medium")
    $show_message("Oh, and she made sure to cut off your treacherous head while she was at it.","medium")
    $show_message("You really need to pay more attention to how you treat your own friends.","medium")
    $show_message("Not all of them are going to tolerate cruelty...","medium")
    jump game_over
    
label badend8:
    scene bg blackscr
    $show_main_ui()
    with dissolve
    "I can't take this stuff."
    "Sometimes I just need to relax in front of the tube."
    "The ground suddenly shakes and everything falls down."
    "The shrine's collapsing!"
    "I start to run, but something hits me in the hea---"
    "Darkness."
    "Just darkness."
    show bg dream with dissolve
    show bg blackscr
    $hide_main_ui()
    with slow_dissolve
    
    $show_message("It pays to care a little more about others and be a little more cognizant of your surroundings.","medium")
    $show_message("Sometimes you have to give up what you want to do for someone else's sake.","medium")
    jump game_over
    
label badend9:
        scene bg blackscr
        $show_main_ui()
        with dissolve
        k "What are you DOING?"
        r "I can't just KILL her---"
        ro "Riku---watc---"
        "There's suddenly an intense pain in my chest."
        "While I was arguing, Naomi stabbed me."
        "I fall back, my vision darkening."
        "Soon I can't hear anyone calling my name anymore."
        show bg dream with dissolve
        "And then it's...just dark."
        $hide_main_ui()
        show bg blackscr
        with slow_dissolve
        
        $show_message("It was really kind of you to spare her life.","medium") 
        $show_message("But kindness isn't always the answer.","medium")
        $show_message("Naomi kills unscrupulously, and no amount of kindness from you would have fazed that goal.","medium")
        $show_message("Sometimes, you just have to save yourself. You're important too!","medium")
        jump game_over
        
    
label game_over:
        scene bg blackscr
        $show_message("Your story doesn't have to end here.", "medium")
        $renpy.pause(1.0)
        $show_message("Have you learned your lesson...?","medium")
        $renpy.pause(1.0)
        $show_message("Then try again.","medium")
        return
