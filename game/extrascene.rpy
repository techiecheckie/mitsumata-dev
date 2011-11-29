################################
#Extra Scenes for after game is beat
################################

#Scene w/Mamoru offering Soume food

label XS:
    ".........."
    "....................."
    u "It seems as if the receiver is no longer working."
    u "I knew it was becoming obsolete. Raphael never wants to listen."
    u "Well, there's no point in trying to watch anymore while it is like this. What should we do?"
    u "I could not begin to tell you. Sarakiel will have issues communicating with them..."
    u "Mmmm. That will be troublesome for us."
    u "Then we have no choice. We must dip into the reserves until communication has beeen restored."
    u "And they are already so low."
    u "What can we do? Humans simply aren't like they used to be."
    u "We should have removed a bit more of their free will like I suggested."
    u "Come now. You know that was not prudent in the midst of a war."
    u "It isn't prudent now, either. We're losing energy to every sector. If this doesn't work, it will mean our end."
    u "It will work. Come, enjoy from the reserves."
    u "Ahhh. Refreshing."
    u "There is one thing I wonder, however."
    u "Oh?"
    u "Why that pureblood denies his instincts so readily."
    u "Yes. That is odd, isn't it? So error-filled, the poor creatures."
    u "Indeed. Nigh pathetic."
    return
    
label XS2:
    db "We've confirmed it, sir, she's a lightning user. One of the many elemental types."
    m "You haven't hurt her too badly, I hope?"
    db "Of course not, sir. She's as you've ordered."
    m "Good."
    "....."
    #play sound knock
    #play sound door open
    a "----!"
    m "Hello, Audra. How are you feeling? Have you eaten your fill?"
    a "......."
    a "What do you want?"
    m "To talk. To give you an option."
    a ".........."
    m "We would like you to join our ranks. You would live comfortably and never run out of food."
    a "...in exchange for killing my own kind."
    m "Well, it's a minor side effect."
    a "........."
    a "Never."
    m "Your other choice is to die here."
    a ".........."
    a "I'D RATHER DIE THAN BE A TRAITOR!"
    #play sound fighting
    "..............."
    m "Well."
    "..............."
    m "It's better for me, this way."
    
    # play sounds eating
   
    "..........................."
    na "...so can I see you do it?"
    m "Naomi, I'm tired. I've just had dinner."
    na "But I want to see you do it. Just a little bit!"
    m "One time, and then you are off to bed."
    na "Okay okay okay!"
    #play lightning effect
    na "...coooool."
    m "I'm still learning to control it, but it gets easier each time."
    na "That's amazing. I wish I could do that..."
    m "Now now. No need to be jealous. I will use these new abilities to protect you."
    na "I know, but..."
    m "Remember your promise? Into the bath, and then bed."
    na "Ooookayyy. I'm going. Good night, Brother."
    m "Good night, Naomi."
    return
    
label XS3:
        "blah blah blah." 
        return
   
label XS4:
    "blah blah blah."
    return
    
label extsc2:    
    su "...fuck.  This isn't your fault you know.  You didn't do anything wrong."
    
    "I still don't look up, but I can hear her rumaging for something under her desk.  Something is clanking."
    
    su "Hmmm...now, where did I, ah!  Yup, this should do the trick."
    
    "She slams some sort of bottle on her desk.  I finally look up, and I can see a clear, syrupy licking slowly sloshing around in an bottle that is just labeled 'XXX'."
    
    su "Here, take a swig of this."
    
    "Susa pours out two drinks.  I move the drink closer to me, and I can smell it way before I move it up to my nose."
    
    r "What is this?"
    su "Don't worry about that.  Just drink it.  It'll make you feel better."
    
    "I eye the glass suspiciously, but I've never been one to turn down free drinks.  I empty the glass in one gulp.  Susa does the same."
    "I feel the warmth coat the inside of my throat and work its way down to my stomach.  My hands and toes tingle and I feel my head get a bit foggy."
    "Is...am I getting drunk?  I cough."
    
    r "Fuck.  What is this stuff."
    
    "I realize what I said after the words have left my mouth."
    
    r "Sorry!  I didn't...that was..."
    
    "I prepare for a swift hit to the face, but Susa is just laughing."
    
    su "Nah, I don't blame ya for that one.  This shit is strong.  Strong enough so even you Majin can feel it."
    
    "I laugh sheepishly.  It isn't like Susa to miss a chance to discipline someone for disrespecting the rules.  I just count myself lucky and try to move on."
    
    r "Heh.  Right.  So, what is this?"
    su "Somethin' of my own creation."
    
    "She pours another two glasses and downs her's before I even have a chance to take my glass.  Gotta give her some credit.  For an old lady, she can really handle her liquor."
    "She wipes her mouth with her hand and examines the bottom of her glass."  
    "Looks like she's making sure no drops have managed to get away undrunk."
    su "Kazu always says something.  Majin metabolism is...well, there are these dehydrogenasomethings."
    su "Majin have a lot of them, apparently.  And see, Kazu has found something that makes them do their job not as well.  Or something."
    
    "She stares at me for a second, like she's trying to decide if she should tell me something or not.  She just shrugs."
    
    su "Y'know, honestly I have no idea what the fuck he's talking about half the time."  
    "All I could really understand is he's found something that stops Majin from processing alcohol so quickly.  I add that to these drinks when I serve 'em."
    
    "I laugh.  Not a fake laugh, like before."  
    "It is nice to know that even Susa can't follow what Kazu is trying to talk about most of the time."  
    "Makes me feel less dumb.  Still, I'll have to thank the guy next time I see him if he's made something that finally allows me to get drunk."
    
    su "So, what's on your mind, brat?  You came in here for a reason, and I figure it wasn't to drain me off all my alcohol stock."
    r "Ah...yeah."
    "I finish off my drink, but before I even have the glass all the way down on the table, she's pouring me another one."
    r "I just...I can't get the image out of my head.  I mean, I-whoa, whoa, that's enough."
    "She swats my hand away and keeps on pouring into my glass before I finally manage to pull it away from her hand."
    su "Yeah.  No, I understand what you're going through."
    "I raise my eyebrow at her.  She barely leaves the shrine.  I can't imagine her getting her hands dirty."
    su "Don't give me that look, kiddo.  There is a lot you don't know about me.  I've...I've had to do what needed to be done before."
    "She finishes off her glass, exhales deeply, and looks at me."
    su "And that is all you did.  You did what you had to do.  You can't feel guilty about it, you just can't."
    "I nod my head.  I don't do it with much enthusiasm, but I at least understand what she's trying to say."
    su "It sucks.  I know, trust me.  And the worst of it is, this is probably gonna happen again.  This is what your life is going to be like."  
    "There are people out there that want to hurt you, Roman, Soume, and any other Majin they can get their hands on."
    r "Yeah..."
    su "But, look here, you didn't start this.  You aren't out their killing people.  You can't think of it like that, kid, you just can't.  It will eat you up inside."
    "I say nothing, but I am listening intently now."
    su "You are defending yourself, and people you care about.  That's all you're doing.  It isn't like you're going out their looking to attack someone.  Right?  Right?"
    r "True."
    "Susa sighs again.  Deeply this time.  She smiles at me a little, something which I don't remember her ever doing before.  She pours herself another glass."
    su "It was you or him.  And you made the right choice."
    "I don't know why, but I feel much better.  Better even than after talking to my parents or Roman.  I smile my first real smile in days."
    su "Oi.  You aren't gonna let me drink here alone, are ya?  Didn't know you were such a lightweight, sprog, or I'd have just poured you some milk instead."
    r "Huh?  This stuff is so weak I thought it was milk.  Course, if you think you can handle it, we can move on to something a bit stronger."
    su "Know you're talking kid."
    
label exsc2:
    l "...thanks.  But I can handle myself."
    su "Oh, that wasn't for your safety.  It was for theirs.  Don't let them bother you, Liza.  Keep focused on the mission."
    l "...what if that is what is bothering me?"
    su "Eh?  What are you going on about?"
    l "I escaped from the Nazi party, and head out here looking for...I don't know.  Something different.  But I'm doing the same thing here, aren't I?"
    su "..."
    l "I mean, why are we doing this, Susa?  Why are we hunting down Majin?  Why am I hunting down individuals just like me and sending them to be slaughtered?"
    su "..."
    l "Is this all there is in the world?  The strong taking advantage of the weak?  Is there no decency?"
    l "I mean, I just...sigh.  I'm sorry.  I know I shouldn't be telling you this, of all people."
    su "Heh.  You're just tired.  Get some sleep.  We have a mission in the morning."
    db "Miss Susanoo!"
    su "Oi!  Don't be fuckin' sneaking up on me like that, ya twit."
    db "My...apologies Miss Susanoo.  It is just that we have just received an urgent message for you."
    su "Eh?  Urgent?  From who?"
    db "I apologize again.  I did not read your message so I cannot tell you."
    su "Hrm.  Let me see...AH!"
    l "Susa, are you alright?  You look pale."
    su "Huh?  Er...yeah, I just gotta go somewhere.  You're in charge until I get back, Liza."
    l "Susa, wait where are you-"
    "play sound door slamming"
    l "...or don't tell me.  It isn't as if I was in the process of asking you anything important."
    db "..."
    l "...can I help you with anything?"
    db "I...I was waiting for you to dismiss me.  You're in charge now."
    l "Right.  Hrm.  Actually, I would appreciate it if you stayed momentarily.  I would like your input regarding tomorrow's mission.  If you don't mind, of course."
    
    
