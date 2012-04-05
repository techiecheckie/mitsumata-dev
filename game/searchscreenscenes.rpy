label Scene15:
    scene bg blackscr
    $show_main_ui()
    with slow_fade
    
    "Bored and hungry. Time for a little late-night snack."
    
    show bg kitchen
    show fx darkness
    with dissolve
    "You know what’s hard? Holding a candle to a map because a certain old bat won’t letcha turn on the lights. I’d use a flashlight, but apparently she’s got something against--"
    
    #shaking effect
    show r upset
    r "UNF---"
    hide r upset
    
    "Effin’ chair. I kick it and it smashes something. Serves the bitc---bat right." 
    "No, I don’t dare to curse, not even in my own head."
    
    #show fx light
    "There’s a light coming from down the hall. What’s he doing up?"
    
    show r neu with dissolve
    r "Hey Roman, it’s--"
    
    hide r neu
    show ro surp 
    with dissolve
    
    #shake screen
    ro "AAAH!"
    
    #play sound SMASH CRASHY BANG
    
    "Well, whatever that was, we’re probably not going to want to eat it anymore. It’s bleeding all over the floor."
    
    show ro upset at right with dissolve
    show r upset at left with dissolve
    $renpy.pause(1.0)
    hide fx darkness with slow_dissolve
    ro "Oh MY. Miss Susa will be upset about this plate..."
    
    r  "You let that bi--old bat punch you around, too?"
    
    "I've never seen someone clean with such a purpose."
    
    show ro neu at right with dissolve
    ro "She hasn’t ever hit me, actually, but she’s rather like that to everyone. You get used to it. It even gets rather charming, after a while!" 
    
    show r neu at left with dissolve
    r "Words I’d probably never use... So what're you doing up? You wanted a midnight snack, too?"
    
    show ro smile at right with dissolve
    ro "This? Oh goodness no, I'd never eat this. I'm just checking the meat. My apologies; I'm always a little jumpy when I handle meat."
    
    show r grin at left with dissolve
    r "Scared one of the dead things’ animal friends will take revenge on you?"
    
    show ro pout at right with dissolve
    ro "Uhm. Well, actually, I used to be a cook back when I was a servant. I mostly prepared...us. Majin. It’s not fun to find out that your friend is your next meal."
    $renpy.pause(1.0)
    
    show r neu at left with dissolve
    r  "...ooh."
    
    show ro smile at right with dissolve
    ro "It’s...all right. You had no way of knowing any of---it’s fine. It was a long, long time ago."
    
    r "So you swore off meat?"
    
    show ro neu at right with dissolve
    ro "That’s correct. I'm a vegan."
    $unlock_entry("Roman","006", True)
 
    ro "Their animal friends may not exact revenge, but I just can't stand to think of eating a creature that can cry out in pain." 
    ro "To humans, we're every bit an animal as any cow, chicken or lamb."

    show r upset at left with dissolve   
    r "Not...-all- humans."
    
    show ro worry at right with dissolve
    ro "Oh, forgive me. I didn’t mean---"
    ro "I agree with you. Many are very kind people, and I also don’t support Majin eating humans either, and some do."
    
    $unlock_entry("Majin","045", True)

    show ro neu at right with dissolve
    ro "I just like to check. For my own sake. Were...you hungry?"
    
    show r neu at left with dissolve
    r "Uh...no...not much, anymore."
    
    ro "Good night, then?"
    
    r "G’night."
    $ Scene15 = True
    show bg blackscr with dissolve
    $hide_main_ui()
    with slow_fade
    return
    

label Scene21:
    scene bg hall1
    $show_main_ui()
    with dissolve
    "I don’t even know why I bothered to go looking around in the hallway. It’s a hallway. The heck was I expecting?"
    
    s "Nngh--"
    
    #play sound Sound of slumping to the floor.
    
    r "Hm?"
    
    s "…"
    
    r "Someone there?"
    
    s "It’s ah---me. I’m a bit peckish...I--I just wanted to get some water, but I suddenly found myself here."
    
    r "Soume? Are you all right? Stay there...I can get you the water."
    
    s "You’re too kind."
    
    "I rush to the kitchen to get the water for him, and bring it to his lips. He sips it hungrily, and I notice, just then, how bony his wrist is."
    
    r "Soume...your ha--"
    
    s "So why are you awake at this hour, Riku?"
    
    "I guess he doesn’t want to talk about it."
    
    r "Just couldn’t sleep. You know how it is, being in a new place..."
    
    s "Yes. It’s so very difficult. Roman was similar when he first arrived. You get used to the atmosphere quickly, though, I find."
    
    r "Actually, uh...while we’re talking about Roman...he said that he’s kind of scared of you. And that he doesn’t really like when you just use your plants on him." 
    r "I think you should talk with him a little...he seems like a nice guy."
    
    #show s smile with fade
    s "Thank you, Riku, for telling me. I will patch things up with him as quickly as possible."
    
    r "Cool. You need help getting back to your room?"
    
    s "Ah, no. I shall be all right."
    
    r "You sure? It sounded like you landed pretty hard..."
    
    s "The water was all I needed—thank you again. Good night, Riku."
    
    r "G’night, Soume."
    
    "If he has a last name, he’s keeping that as secret as the rest of him. I wonder if I’ll ever understand him, really."
    $ unlock_entry("Soume","009", True)
    $ Scene21 = True
    return
    
    
label Scene37a:
    "Miss Susa is in her room...looks like she's having some kind of heated conversation..."
    
    su "What the hell is going on?"
    
    "I creep up as close as I can to the door. She’s kind of muffled, but I can still hear her."
    
    su "Yes, I gathered that from your message, and I-"
    
    su "No, Liza, I-"
    
    "Liza? The woman Roman was telling me about?"
    
    su "Yeah, I get that, but-"
    
    su "LIZA. Spare me the fucking pleasantries for once and fucking TELL me if the intel was confirmed or not."
    
    "Her voice sounds strange. Less…harsh?"
    
    "She’s quiet for a really long time."
    
    su "Oh god. No, no, the where doesn’t matter right now, Liza."
    
    "Her voice is almost completely different now."
    
    su "If he’s there, I will find him without a doubt."
    
    "Find who? Who is she talking about?"
    
    "Shit. She moved or something. I can’t quite make out what she’s saying. Maybe if I just move a little-"
    
    #This is Kazu.
    k "AHEM."
    
    "I jump back into the wall and trip over myself. Great. I’m dead. I look up and see-"
    
    r "Mister Osamu---"
    
    k "YOU WILL REFER TO ME AS DOCTOR OSAMU. Always. Never by my first name."
    
    r "Man, what the hell are you doing creeping around out here?"
    
    k "I could ask you the same."
    
    "I don’t like the way he’s smiling at me. I start to say something, but some heavy breathing is coming from behind me and my brain loses its ability to communicate with my mouth."
    
    su "Just what the hell are you doing out here, you clumsy little buffoon. I’m on the GODDAMN PHONE!"
    
    k "Oh, we were just leaving. Riku had volunteered to help me with some…experiments."
    
    r "I did--"
    
    "Doctor Osamu is smiling at me. He looks like he just got a new toy."
    
    k "Or, was something else happening out here, Riku?"
    
    r "No, I…uh, I mean, Mist-"
    
    k "Doctor."
    
    r  "…"
    
    k "What’s that?"
    
    r "Nngh."
    
    k "Ah, Miss Susa, funny story--"
    
    su "If you jackasses are interrupting my phone conversation, this better be the best story I've ever heard in my life."
    
    k "It IS, actually---"
    
    r "--I agreed to help Doctor Osamu! Yes, he’s doing some experiments on-"
    
    k  "Limb regeneration."
    
    r "LIMB REGENERATION?!"
    
    k "And Riku here was so kind as to volunteer."
    
    su "About time he made himself useful. Don’t forget to clean the doctor’s lab for him when you’re all done."
    
    k "Of course he will. He actually said he’d be on cleaning duty for the next month."
    
    su "Hn. Finally some initiative."
    
    k "If you'll excuse us, Miss Susa. Come along, assistant."
    
    r "Heeeeelp."
    $ Scene37a = True
    return
    
    
label su17:
    r "And from his car door was dangling an iron hook!"
    s "Oh no!  Did it scratch the paint!"
    r "...what?  What do you mean?  Why would that matter?"
    s "Oh...I dunno.  Probably would hurt the resale value some."
    r "That...that isn't the point of the story, Soume!  It is supposed to be scary.  It is about an escaped convict!"
    s "Well, property damage can be scary, can't it~!  I would hate it if anything happened to any of my beautiful little plants~!"
    "Soume has turned around and is trying to reach out to his nearest plant.  It is completely dark out now, so I can't tell if it responds, but Soume coos softly before turning around."
    ro "...I'm sorry, I guess I don't understand how that is supposed to be scary.  It doesn't make any sense."
    r "Oh for the love of....not you too, Roman!"
    ro "How is it supposed to be scary?  He's already gotten away from the escaped convict without even knowing it."
    r "Well...yeah, but-"
    ro "And if he did escape from prison, why does he still have his hook hand?  That is something you would think the prison might have confiscated before his arrest."
    r "Er..."
    ro "Honestly!  What kind of prison guard just lets a prisoner walk around with a sharp metal object coming out of his arm?  No wonder he escaped.  Probably murdered all the prison guards."
    r "Ugh...I don't know why I even tried."
    
    "I am terrible at telling stories.  I'll fucking admit it."  
    "Still though, at least Roman or Soume could pretend to act scared.  Roman is too busy disecting the logic of it all and Soume wouldn't be frightened unless my story involved a weed whacker."
    
    su "What're you all doing out so late.  Should be getting to bed.  Especially you, sprog."
    r "Right, I was just-"
    ro "Riku was just telling us about the appauling state of our prison system."
    r "No!  It was just supposed to be a scary story, is all!"
    su "Aw, really?  I love a good scary story.  Which one was it?"
    r "The one with the escaped convict with a hook for a hand."
    su "That shitty old story? Fuck, no wonder they look bored, kid.  You gotta do a better job than that."
    r "But that's the only one I know.  And I thought it was pretty good..."
    su "Nah.  But, here, I'll tell you a good one.  A true one, actually.  One involving this very rescue."
    r "Oh yeah?  Does it end with you jumping at me and yelling 'IT IS RIGHT BEHIND YOU!'"
    su "What, no.  No one would be stupid enough to fall for-RIKU WATCH OUT!"
    r "AH!"
    "I turn around to where she is pointing, only to see Soume sitting there twirling his fingers around in the cool grass.  He looks up at me and waves enthusiastically."
    s "Hi Riku!"
    r "Uh...yeah.  Hi."
    su "Ha ha ha!  I can't believe that actually worked.  Anyway, as I was saying, I don't think I ever told you this before sprog, but someone died here."
    r "Here?  Like where I'm sitting?"
    su "No, dunce.  I mean here, like here at the rescue."
    r "Really?  Someone died?"
    
    "I'm not sure if I should take here seriously or not."  
    "Roman and Soume are talking to each other about something, so apparently they've already heard this or know Susa is just messing with me.  I can't tell which yet."
    
    su "Yup.  Before I got here though.  Long time ago.  The last person that ran this place didn't really take a hands on approach.  Just sort of let you guys take care of yourselves."
    r "Sounds better than-"
    su "You sayin' something, kid?"
    r "Ah...no.  Just commenting that, uh...nothing.  I'll ask later."
    su "Hmph.  So, some of the Majin would end up training themselves.  Others just spend the entire day playing around and relaxing around the rescue."
    r "Any chance we could start that up again?"
    su "No.  And stop fuckin' interrupting.  Now one day a group of young Majin were playing upstairs."  
    su "They were playing hide-and-seek.  One of the children decided to hide inside an old antique trunk, but when he climbed inside, the trunk closed on him."
    s "Oh no!"
    
    "Soume is finally paying attention again.  Sort of.  Right after he yelled that, he starts looking around at his plants again."
    
    su "The other children searched for hours, but couldn't find him.  It wasn't until days later that they found him in the trunk, but by then it was too late.  There was nothing they could do."
    su "Well, that was the end of things, at least for a while."  
    su "But later, people started noticing some weird things.  Items went missing."  
    su "People would feel chills when passing by the room he trapped himself in.  And then...people started seeing him again.  Glimpses, but people kept on seeing him."
    
    r "Sure.  And why don't people still see him then?  Hmph.  Nice try."
    
    su "Heh.  Who says they don't?  Come with me kiddo."
    
    "She stands up and walks towards a particularly dense portion of trees by Soume's garden."  
    "I look over at Roman and Soume.  Roman is smiling at me and motions for me to follow her.  I get closer to the trees and look around."
    
    r "What am I supposed to be looking for?"
    su "Just peak back through here, sprog."
    
    "I look around pass the trees she's pointing at.  Nothing.  Can't believe I almost believed her."
    r "Hmph.  Nice try, but-OH WHAT THE HELL?"
    
    "I see it.  There is just a flicker, but a shadow of a girl flickers in front of my eyes.  She looks happy, but a little confused.  She reaches towards me, but fades out before she can finish the motion."
    
    r "Ghosts!  There are ghosts here?  THIS PLACE IS HAUNTED?"
    
    "I begin thinking of the quickest ways to pack up all my stuff, but Susa starts laughing."
    
    r "What?  What're you laughing at."
    su "Sorry, sorry.  Didn't mean to frighten you.  That much at least.  Those weren't ghosts."
    r "Huh?  Then what were they?  I...I definitely saw her.  She was just in front of me."
    su "Yeah, those aren't ghosts though.  They pop up here every once in a while, but all of that is just brief glimpses of Majin on the other side of the barrier."
    r "Oh...that...is strange.  How do they get here?"
    su "Fuck, I dunno.  They seem to show up in places wherever there are a lot of Majin, but beyond that I don't know.  Glad they do show up though; makes it easier to scare all the new students."
    r "I-I wasn't scared."
    su "Mm hmm...why don't you head back with Roman and Soume.  I have some stuff I need to finish up anyway."
    "She turns and heads back towards her office.  She is smiling a bit, which is a nice change of pace, but I think it might have something to do with how loud I yelled when she showed me the 'ghost'."
    $ su17 = True
    return

label rikucrib:
        scene bg blackscr
        $show_main_ui()
        with dissolve
        ma "Graduation was lovely, wasn't it?"
        pa "It was. You looked beautiful."
        ma "Well, you looked very handsome."
        pa "And now that is over...perhaps we should talk about how to tell your parents we eloped."
        ma "Hahaha. I'm sure they'll be alright with it. They've always liked you."
        r "Laaahaaaaaaaaah."
        ma "...what was that?"
        r "Laaaaaaaaaaaaaaaahlaaaaaaaaaaaaaaah."
        pa "...it sounds like..."
        ma "...a baby..."
        r "Laaahloolaaahluuuu~"
        pa "How did an infant get here?"
        ma "Oh, he's not wearing any clothes..."
        ma "We can't just leave him."
        pa "...."
        pa "Okay, pick him up. We can keep him just for the night and figure out what to do about it in the morning..."
        
        r "Laaaaaaaaaaaaaah looooo laaaaaaaaaaaah loooooo."
        pa "...he's up early..."
        ma "I'll get him..."
        "..........."
        ma "Aaagh!"
        pa "What is it---wha--how...?"
        r "Heeeee heeeee~"
        ma "When we examined him, he couldn't have possibly been older than a few months..."
        ma "There's no way he could possibly stand on his own..."
        pa "...maybe we examined him incorrectly. We did just graduate medical school..."
        ma "I have a bit more faith in our abilities than that, dear."
        pa "Alright. Let's examine him once more..."
        return

label kazmischief:
    scene bg blackscr
    $show_main_ui()
    with dissolve
    r "Hey Roman...you wanna get in trouble?"
    ro "...not particularly..."
    r "Come on. Let's go do something fuuuuun."
    ro "Fun for you is dangerous for the rest of us..."
    r "I promise it won't be. And whatever we mess with, we'll put back exactly as we found it. No one will even know."
    ro "...fine. Okay. What did you want to do?"
    r "...let's look around in the doc's lab!"
    ro "Hmmm. I am a bit curious about the things in there..."
    r "See? Perfect!"
    
    "................."
    
    ro "Riku, I am pretty sure it's not a good idea to mix chemicals---"
    r "No way, he's training me to use this stuff. I know exactly what I'm doing."
    ro ".........."
    ro "What ARE you doing?"
    r "I'm making an invisibility potion!"
    ro "That doesn't look like it'll do anything but kill you."
    r "No way, it will work. I've seen the doc use it on stuff. It's fine."
    "........."
    r "There, it's done."
    ro ".....mmmm."
    ro "I'm not testing it."
    r "Spoilsport."
    r "........"
    r "I know. Let's sneak it in the doctor's coffee."
    ro "Riku---"
    "Too late. He's gone and dumped it in the coffee already."
    
    "Luckily, the doctor JUST walks in."
    
    k "...what are you two doing down here?"
    ro "We--uh---"
    r "Learning!"
    k "...oh really?"
    r "Absolutely! I was just looking at your very, very interesting studies!"
    k "Hmmm."
    
    "He takes a drink from his coffee."
    k "Mmm. This tastes odd..."
    
    r "..........."
    ro "..........."
    
    k "...what are you two staring at?"
    
    r "Hmph."
    ro "...thank god."
    
    k "WHY are you two acting so suspicious?!"
    
    "!!!!!!!!!!!!!"
    k "What is with those looks!"
    
    ro "Doctor---you---"
    r "YOUR FACE IS POLKA-DOTTED!"
    r "AHAHAHAHAHAHAHAHAA!"
    
    k "WHAT?"
    
    ro "...IT WAS RIKU'S IDEA!"
    r "HEY! Are you sellin' me out? You agreed to come with!"
    
    k "OUT OUT OUT OUT OUT!"
    
    r "AHAHAHAHAHAHAHA!"
    ro "........."
    r "The look on his face...that was GREAT!"
    ro "........"
    ro "...ehehe."
    ro "I guess it was a little funny..."

    return
    
label sualcohol:
    scene bg blackscr
    $show_main_ui
    with dissolve
    r "Hey Roman...you wanna get in trouble?"
    ro "...not particularly..."
    r "Come on. Let's go do something fuuuuun."
    ro "Fun for you is dangerous for the rest of us..."
    r "I promise it won't be. And whatever we mess with, we'll put back exactly as we found it. No one will even know."
    ro "...fine. Okay. What did you want to do?"
    r "...let's look around for something to drink!"
    ro "I'm not really fond of alcohol..."
    r "C'mon! I haven't had a drink in ages. I need to keep up on my vices!"
    ro "I don't even think there's alcohol in the house, Riku."
    r "There is. I found this back room...looks like there's a cellar. Pretty sure the ole bat is keeping all the booze in there."
    ro "......fine."
    r "Alright, let's see..."
    r "HA! Jackpot!"
    ro "...there's really sake down here?"
    r "A TON of it---hmm, what's thi---"
    ro "Don't touch that!"
    r "---what is it?"
    ro "It's an alarm system...you almost got us caught, idiot."
    r "...whoops! Well, thanks. How do we get past it?"
    ro "You---shouldn't this be a clue that Miss Susa doesn't want us here?"
    r "Yep."
    r "So how do we get past it?"
    ro "................"
    ro "It--seems there's an inscription here. We can only take one of the bottles...the puzzle will probably reset."
    r "Just ONE, damn!"
    ro "One is PLENTY, and you aren't even of legal age, yet!"
    r "Fine fine. Which one should we take?"
    #stick the alcohol minigame here
    #$minigame("bottles", 0, 0, None, True) # just defining the game name is enough here
    return
    
label sorodirty1:
        scene bg blackscr
        $show_main_ui()
        "They're taking a bath and Soume's washin' Roman's hair, how sweeeeeeeeeeet! No smut tho."
        return

label sorodirty2:
        scene bg blackscr
        $show_main_ui()
        "Now they are having hot smeeeeeeeexooooooooooors, nomnomnom."
        return
