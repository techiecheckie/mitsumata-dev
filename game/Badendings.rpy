label badend1:
    "Ahahaha you die cause you suck."
    jump game_over
    
label badend2:
        "You pissed Susa off so bad with your idiot stunting that she kicks you out of the shrine!"
        "What're you going to do for protection now...?"
        jump game_over

label badend3:
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
        ".............."
        show bg blackscr
        $renpy.pause(3.0)
        
        "You really need to learn how to listen to your superiors."
        jump game_over  
        
label badend4:
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
    $renpy.pause(3.0)
    
    "Unfortunately for you, your skills just weren't where you thought they were."
    "Next time, try to think before you act."
    jump game_over
    
label badend5:
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
    show bg dream
    "..........................."
    show bg blackscr
    
    "Life is about lessons." 
    "You haven't learned everything you need to know to continue with that life."
    "Go back, and consider some of your actions more carefully."
    jump game_over
    
label game_over:
        "Here is some game over loop thing that will play."
        "You lose."
        return
