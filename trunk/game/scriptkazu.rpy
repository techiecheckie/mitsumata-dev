#*************************
# Kazutaka's Branch
#*************************
#Currently at 2256 out of 3506
# was editing at Kaz28.
# Nearly done with this arc.
#At label Kaz20 and ND=16

#Scene w/Riku asking Kaz about his past.

label kaz1:
    "I could go check on the doctor. He was the most shaken up."  
    "Seeing him freak out...well, it's good to know I wasn't the only one."
    
    #play sound knocking
    
    k  "Yes?  Who is it?"
    
    r  "Uh...it’s me.  Riku."
    
    k  "Riku?"
    ".........................."    
    k  "Ah, yes.  Hold on."
    
    #play sound  Unlocking noise.
    
    k  "Come in.  You will excuse me for the current state of my lab.  I wasn’t expecting company.  A little bit of warning would be appreciated in the future."
    
    "Current state of his lab? It’s dirty as usual!"
    
    r "Uh...it’s no problem."
    
    k "Good timing at any rate. I have been working on this new strain of bacteria and I thought you might be interested..."
    
    r "...no thanks. Can you work with...bacteria and talk at the same time?"
    
    k "Child, I am a scientist. I’m quite the expert at multitasking.  In the past, I have performed surgery on two separate individuals at once because neither could wait."
    
    r "Oh.  …cool, I guess."
    
    k  "Hn. I suppose I can’t expect you to describe such a novel achievement without resorting to frivilous adolescent language such as that."  
    k "This bacteria is rather vicious, you see.  I mean, I can handle it, of course, but you being a novice and rather inexperienced in matters such as this…I would worry about you."
    
    r  "Greeeeeeat. So, what makes it so bad?  Gives you the flu, or something?"
    
    k "Hm…I guess you could put it that way.  The only major difference is…well, you know how the flu dehydrates your body and makes your head rather congested?"
    
    r  "Yeah."
    
    k "Well, this little critter takes your insides and your outsides, and reverses their relative position."
    
    r  "…how is that remotely the same?  And why are you studying it?"
    
    k "It is absolutely fascinating, I know, I completely agree with you.  I only just discovered it last year after it infected one of my patients."  
    
    "He walks over and points to a Petri dish behind a glass enclosure."
    
    k "Here is the culture, if you’re curious. Just look at the size of the colonies!  Have you seen anything like this before?"
        
    #Riku mutters to himself.
    r "Like I'd wanna see something like that--"
    
    k  "Kazutaka coli."
    
    r "Excuse me?"
    
    k "The name of it. It is undiscovered you see, so I get to name it!  So far it seems unique to Majin, so humans haven’t had a chance to classify it."
    k "Of course...I'd love to test it on a human..."
    
    r "Creeeeepy. So, anyway-"
    
    k "It'll be a whole new genus, you see!  Nothing like this has been seen before.  So, naturally, I named the genus after myself."  
    
    r "You discovered a bug that is capable of killing Majin, and you decided to name it after yourself?"
    
    k "Of course!  Perhaps a little vain, now that I think about it, but I think I deserve a little bit of self indulgence!" 
    k "And, of course, you realize species name 'coli' already, coming from Latin and meaning 'of the colon.'"
    
    r  "Yeah…of course.  We covered that in my 'Latin you’ll never need to use' course."
    
    k  "So, what do you say, Riku?  Care to help me grow it?"
    
    r  "‘Scuse me?"
    
    k  "Miss Susa, you see, she’s been on me to start training an apprentice.  What with me being the only Majin doctor, she believes I need to start passing on some of my knowledge."
    
    r "I don't think I'm a good choice..."
    r "Not really in the mood to be playing with something that would like to rearrange my insides."
    
    k "Oh, Riku, please.  This is rather simple.   So simple even a child like yourself should have no problems."
    
    r "But I like my body parts where they are."
    
    k  "It is perfectly safe! The bacteria will be behind this glass hood at all times! All you need to do is replate it."  
    k "I fear they are rather delicate outside of their natural habitat, so this is a more arduous process than it typically is."
    
    "How do I get roped into these things?"
    
    r "I guess I can do it."
    
    k "Excellent!  I knew you were the man for the job, Riku.  I could see it in you; you’ve always taken a special interest in my work!"
        
    r "Yeah.  You know me.  Woo science, and all that."
    
    k "I’ll be over at my desk.  Just inform me when you are finished or if you manage to contaminate yourself so I can alert the morgue."  
    
    r "WAIT!  Hold on, you need to show me what I’m doing here.  I don’t know what to do with this."
    
    k "Oh, I had assumed that would be obvious Riku.  Don’t you see the tools in front of you?"
    
    r  "Uh…yeah.  So?"
    
    k "Ah, well, I guess I better explain it to you."

label cells2:  
    $result = minigame("cell", 2, 1000)
    if result == True: 
            jump cellsucceed2
    else: 
            jump cellfailure2
    
label cellfailure2:
    k  "No no no no no!  My bacteria!  You’re killing them Riku."
    
    r "This is harder than I thought it would be."
    
    k "Hmph.  You are quite lucky I have more stock we can use.  Be careful this time!"
    
    r "Sure thing.  Sorry Doc, I know I can do it this time."
    jump cells2

label cellsucceed2:
    k "Brilliant, simply brilliant, Riku!" 
    k "Of course, I could have done the same task in a fraction of the time.  And these colonies are much smaller than the ones I am capable of growing.  They don’t seem as viable, either..."
    
    r "Look fine to me."
    
    k "To the untrained eye, perhaps.  Trust me though, these colonies are quite substandard when compared to my typical work."
    
    "Even his damn compliments sound like insults.  Have to admit, helping him wasn’t as bad as I thought it would be.  And at least he doesn’t always roll his eyes when he talks to me anymore."
    
    r "I should get back up.  Thanks though."
    
    k "I am always happy to help those who are in the pursuit of knowledge, Riku.  You are welcome back at any time."
    
    r "Great.  Oh, uh, you know, I think we’re heading out to the city tomorrow."
    
    "Doctor Osamu stops smiling and his old frown returns to his face."
    
    k  "'We'?  Who is 'we'?"
    
    r "Uh, well, me, of course.  And then Roman.  And maybe Soume."
    
    "Doctor Osamu clicks his tongue loudly and waves his hand, as if to dismiss me."
    
    k "I certainly cannot stop you from associating with trash and traitors, but I would rather spend the day alone in my lab, thank you."
    
    r "You sure? Soume isn’t so bad, once you get to know him."
    
    k "I know him quite well. Better than you, I would expect.  And I know he’s up to something.  Do not trust him, Riku."
    
    "There is an urgency to his voice. I don’t know what happened between him and Soume, but whatever it was is enough to make him fucking paranoid.  He almost jumps whenever I say his name."
    
    r "You keep on telling me that, but he seems like an ok guy to me, you know?"
    
    k "You are still young.  You're at least a hundred years too early to have developed a keen sense of character, and the ability to see that in others.  It will come in time."
    
    r "Riiiiight."  
    
    k "It is his fault, you know?"
    
    r "What exactly is that?"
    
    k "Those plants he uses...they blocked my sensory capacities. That's how we were ambushed."
    
    r "…you don’t think Mamoru is a more likely candidate?  The evil guy trying to eat all of us.  Soume included."
    
    k "HA, as if that Mamoru actually considers Soume to be on his menu."  
    
    r "Well, do you have evidence that it was Soume?"
    
    k "I…well, that is…nothing tangible, mind you.  But I know it’s him!"
    
    r "Look, just cheer up some.  It wasn’t your fault that we got ambushed.  You don’t need to look for someone to blame."
    
    k "I’m not-"
    
    r "Here."
    
    "I take out the plant Roman gave me earlier.  I put it on his desk, and he eyes it.  He prods it with the end of his pencil and looks back up at me."
    
    k "What’s this?"
    
    r "What’s that?  Are you sure you’re a scientist?  That there is a plant.  And a gift."
    
    "He looks back down at it.  He looks confused, like he’s never received either of those things before in his life."
    
    r "Keep it, water it, do all that sort of stuff."  
    r "Just...remember that you aren’t alone here. We all have your back.  Even Soume.  Whether you want to recognize it or not."

    k "..."   
    r "I'll talk to you later, okay?"
    k "...idiot."
    "....."
    "I think I might actually understand him a little better..."
	
    $ decison ="9"
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


label kaz2:
    #Roman tries to convince Kazu to lighten up on Soume.
    ro "Doctor Osamu!"
        
    k "What?  Oh…you?"
    
    ro "Doctor Osamu.  Hey.  Sorry for the intrusion, but I just wanted to make sure you were alright.  I haven’t had a chance to check up on you since the unfortunate circumstances of last-"
    
    k "I can assure you, I am perfectly alright.  And if I wasn’t, I would be in a rather sore state indeed if you were the one checking up on me."
    
    ro "Ah, well, I'm not a doctor by any means...you certainly are far more capable there..."
    
    k "You will have no argument from me on that.  Now, if you don’t mind."
    
    "The doctor moves to return to his lab.  It seems he had just stopped up for something to eat, judging by the sandwich."
    
    ro "Wait, please.  I am walking in that direction anyway."
    
    #Sarcastically.
    k "Lovely."
    
    "I should just turn around and leave.  The doctor has made his feelings on Soume perfectly clear."
    "He even started disliking me once he found out that Soume and I were close."
    "I should give up, like Soume said."
    "Still, we are all fighting for the same goal."  
    "We have the same enemy." 
    "It would be best if I could somehow mend the damage to their relationship."
    
    ro "What I was suggesting though, is that if you are in trouble there are those here that can help."
    
    k "Hrm.  We’ve already ruled out you, and Miss Susa herself has admitted she knows nothing about Majin biology."
    
    ro "But what about Soume? He knows so much about healing already..."
    
    k "Soume?  Ha!  Do you let the wolves tend to the sheep as well?  I am quite adept at taking care of myself.  Let us just leave it at that."
    
    ro "But Soume is wonderful!  He has abilities that-"
    
    k  "Hush, child!  I have asked nicely for you to drop the subject.  I have no time to hear about you and your little schoolboy crushes."
    
    ro "E-excuse me?  I-I don’t know what you’re talking about---I'm not---"
    
    k "PLEASE. Spare me the dramatics. If this is something you’ve been trying to hide, you’re doing it with all the tact of a drunken boar."
    
    ro "...is it that obvious?"
    
    k "We laugh about it when you aren't looking."
    
    ro "Oh...but--but that's BESIDES the point, and it's that Soume is an amazing healer--"
    
    k "Hmph.  Mere parlor tricks.  I have no time for his shamanism or his alternative medicine.  I am a doctor; I have no need for voodoo."
    
    ro "Doctor, I fear you've misunderstood me. He uses his own ene--"
    
    k "And I’M afraid you missed the part where I repeatedly told you I have no interest in going to that youko for anything."
    
    "Now we’re walking in silence.  I am taken a little aback by his demeanor. I didn't expect it to be this bad."
    "They rarely even talk to each other, but before Doctor Osamu at least maintained an air of civility."
    
    k "Since you are so close to Soume, perhaps you can do something about the smell coming from the kitchen."
    
    ro "The smell?"
    
    k "Oh, don’t tell me you haven’t noticed. It has gotten so strong that even you must have a hard time ignoring its call now."
    
    ro "I'm really not sure what you're referring to..."
    
    #Kazutaka chuckles, darkly.
    k "Oho...come now, Roman. You don't know what that particular smell comes from? Truly?"
    
    ro "With all due respect, Doctor Osamu, I try my best to avoid meat.  I hold my breath when I pass the kitchen."
    
    k "Oh, that’s right. I forgot you were a vegan. I can’t even imagine how your mind rationalizes Soume’s eating habits."
    
    ro "Well, lots of people eat meat, Doctor Osamu. I suspect that is a ham sandwich you’re carrying right now."
    
    "Whatever he's getting at, I know I won't like it."
    
    k "Yes, this is ham, but the pigs can't--wait.  Wait just a moment, Roman."
    
    "Doctor Osamu is now smiling broadly at me.  I find something about it completely unnerving."
    
    k "You don’t know, do you?"
    
    ro "Know what, Doctor?"
    
    #Kazu laughs
    k "You don’t.  Oh, this is simply perfect!  He has no idea!  I can’t believe the richness of the situation.  This is too good.  He doesn’t know."
    
    "The Doctor has started talking like I’m not here.  I’ve noticed he has a tendency to do that, especially when he gets excited or stressed."
    
    ro "I’m afraid I don’t understand."
    
    k "Well, Roman, perhaps you should talk to your beloved...'friend' about it. And tell him to hurry and finish it as well, or I might sample his supply."
    
    "Doctor Osamu walks off laughing and talking to himself."

    ################
    call su1 #Susa has a phone convo with Liza about their son.
    #################

label kaz3:
    #Roman and Soume talk about the convo with Kazu and his not easing up on Soume.
    #Roman explains his veganism, moralizes at Soume, and angers Soume.
    $unlock_entry("Soume","082")
    $unlock_entry("Majin","049")
    ro "It does smell wonderful here, you know."
    
    s "Why, certainly.  You can thank my precious children for that."
    
    "I’m relaxing with Soume in the garden. I always feel relaxed when I come here...the flowers are so soothing."  
    "After my talk with Doctor Osamu, I need some relaxation."
    
    #Soume giggles
    s "Is something bothering you, Roman? You have been awfully quiet today!"
    
    ro "Ah.  It…it is nothing."
    
    "Soume frowns at me.  He knows I’m lying. He always knows."
    #Roman sighs.
    ro "..."
    
    "How can I compare with him?"
    
    s "I have the sneaking suspicion you aren't being entirely honest."
    
    ro "Heh. Sorry, it is just a trifling matter.  I really didn’t want to concern you with anything, especially something so insignificant."
    
    "What the Doctor said is truly alarming. I don't know that much about Soume. He never talks about himself, even though I'm his partner."
    "Is it possible that Doctor Osamu knows something that important about Soume?"
    
    s "..."
    
    s "Is your arm healing properly?  Did I not treat it well enough?"  
    s "I could have sworn I did it properly..."
    s "Have you noticed any strange side effects?  Swollen tongue?  Loss of toes or fingers?  That sort of thing?"
    
    #Roman laughs a bit nervously.
    ro "I know you, Soume, you must stop teasing me like this..."
    
    "Soume is carefully looking at my hands and feet now, counting my fingers and toes to make sure they’re all there."
    
    s "Hm?  Oh…right. Teasing..."
    
    ro "Ehhh…no, I'm fine, you did a wonderful job.  I can move it around pretty well and everything."
    
    s  "Oh excellent~! You had me worried for a moment..."
    
    ro "No…it’s just that…ah, well, you see…I was talking to Doctor Osamu."
    
    s "Ahh, no wonder you look so gloomy."
    
    "Soume is back to tending with his plants. He glides to each one, giving each some encouraging words and a pat."
    
    ro "Yes, he has been...slightly more grating than usual. I imagine he blames himself for the ambush."
    
    s "Oh, is that so? It doesn’t sound like the Doctor to blame himself for anything."
    
    ro "Well, outwardly, no.  But you can tell it is eating at him.  He seems to be going off at the slightest provocation.  You know what he complained about today?"
    
    s "Roman, I think it would be quicker if I just guessed what he didn’t complain about today."
    
    ro "True!  Today he complained about the smell of the meat!"
    
    s  "…the meat?"
    s "..."
    
    ro "Yes! I couldn’t believe it. He went on about how terrible the scent has grown!  He singled out you specifically.  He informed me that he wanted me to talk to you about it!"
    
    s "Ah. He said that?"
    
    ro "Don’t worry, Soume, I’m not going to lecture you about it.  I think the good Doctor is just looking for something to vent about these days.  Take his complaints with a grain of salt."
    
    s  "Yes. Of course. Did…did he say anything else to you?"
    
    ro "Nothing much of importance."
    
    "Soume seems genuinely hurt by Doctor Osamu’s comments.  Now I sort of wish I hadn’t even told him.  I never considered he would take this so seriously."  
    
    ro "Soume, honestly don’t trouble yourself over it.  I haven’t noticed any difference in the odor, and you know how detestable I find meat."
    
    s "Right.  You have mentioned that before."
    
    ro "I'm sure I'd be the first to know."
    
    s "Well..."
    
    ro "I’m sure you would be a vegan too if you witnessed what I did."
     
    "I used to be a kitchen slave for a wealthy family in Russia. What happened to me...it's not something I talk about."
    "But I want to tell Soume. I want Soume to understand me, and maybe...let me in a little bit."
    "And he was in captivity himself...we have so much in common!"
    "Am I just being hopeful?"
    
    s  "Oh?"
    
    ro "I...used to be a servant. For humans."
    
    "Soume is quiet.  He turns to me and looks on silently.  I think he’s waiting for me to continue."
    
    ro "That's where I learned to cook. Me and the guys in the kitchen...we thought we had the best job."
    
    "Soume listens attentively.  I don’t think he’s going to interrupt until I finish now."
    
    ro "All of us were Majin, but unlike the others, we got to stay in warm kitchen to sleep. I didn't need it much, since my specialty is the cold, but..."

    ro "We all thought we were so blessed."
    
    "I clear my throat.  All those terrible memories are starting to come back."
    
    ro "As long as we cooked the meals on time, no one bothered us."
    
    s "...go on."
    
    ro "Then one guy I didn't know very well disappeared. Then another."
    ro "Then another."
    
    ro "And all the while...I didn't even think about all the meat that was coming into the kitchen."
    
    ro "The first thing I cooked in that kitchen was the boy I was replacing."
    ro "But I couldn't tell...he just looked like...like red meat."
    
    ro "I must've cooked my cell mates. My friends. The missing kitchen staff..."
    
    "I was almost shaking now.  I couldn’t stop though.  If Soume was ever going to know me, he had to know this."
    
    ro "Until finally, one day, I caught them. My last close friend in the kitchen. They killed him. All that meat I'd been eating...it was...all of it was..."
    
    ro "It was then I promised myself, if I got out of here, I would never eat meat again."  
    ro "Not after I had eaten my friends.  Cooked them.  Let them die."
    
    "Soume looks like he wants to say something, but he stops himself and lets me continue."
    
    s "It wasn't your fault..."
    
    ro "It WAS. How could I have been so stupid...I was EATING my own--"
    
    ro "But I was terrified. We all were.  I didn’t want to die.  Does that make me a terrible person?  I cooked everything they wanted without thinking." 
    ro "Children. Friends. Pregnant mothers."
    
    ro "When I was the only one left...I ran before they could get me, in the dead of winter. It's so thankful that I have an immunity to the cold and humans don't, or they might have come after me."
    ro "But can I ever redeem myself for those people that I...prepared for humans to eat?"
    
    s "..."
    s "...oh Roman."    
    s "You did what you had to survive. No one else would blame you, and least of all myself."
    
    ro  "Is that right, though? Shouldn't I be held culpable for my crimes?"
    
    s  "…well, maybe you will, someday."
    s "But right now...you're here, with me, and safe."
    
    "Soume slips an arm around me. My face is going so red that I might pass out from the effort."
    
    ro  "A-ah--thank you for listening. To my story. To---um--"
    
    "Soume nods. He is looking at me with an expression I can’t quite place."  
    
    s "And because of those things...that is why you no longer eat meat."
    
    "I’m taken a little aback. I have to admit, of all the things he was going to say, that was one I didn't expect."
    
    ro "Ah. Yes. That is when I stopped eating meat. No one should be someone else’s food. Living creatures are destined for so much more than that."  
    "Majin, cow, pig, human, everyone.  There is no reason why we must dine on other living things."
    "It's worse when that thing can beg for mercy."
    
    s "And yet...you dine on plants, do you not?  Vegetables?"
    
    ro "Yes…but that is different."
    
    s "Different how?  Are plants not alive?  They can certainly feel pain, I can assure you of that."
    
    ro "…"
    
    s  "And the pigs and the cows that you refuse to touch, each day they ravage the land, eating their weight in flowers and grass and plants of all kinds."
    
    ro "Soume..."
    
    "I don’t know what to say. Soume...seems upset." 
    "I never really thought about this before, but he is remarkably close to plants.  He always talks to them. Do my eating habits hurt him?"
    
    ro "But one must eat…something."
    
    s "That is true enough."
    
    "He stares at me a little while longer.  He looks as if he’s thinking about something, but not quite comfortable vocalizing it."
    
    s "You do know, Roman, that Majin are largely meat-eaters. Some can only stomach the primest of meat. Human or other Majin."
    
    ro "Yes, I've...heard of them."
    
    s "And what is your opinion of them?"
    
    ro "No one should be anyone else's food. I can't change my opinion on that."
    
    "The look Soume is giving me now...he's never given me it before. I think I've really messed up."
    "His voice is steady, but brimming with terseness."
    
    s "Even if they have no other choices?"
    
    ro "If it was me, I would rather die than eat a human.  I could never do such a thing.  Even if some have treated us badly, there is no reason--"
    
    s  "What do you know of hunger, little one?"
    
    "Soume is forcing me down into the tatami, his face ferocious."
    "The hairs on the back of my neck stand. That feeling of imminent death..."
    "It's the first time it really hits me..."
    "Soume is far above my station in every way."
    
    s "Your body can tolerate the garbage you eat. Barely, but you're still breathing. Yet you look down at those who cannot do otherwise, to appease your human moralizing. What do YOU know?"
    
    "He is leaning towards me now, his breath in my face. It's an awful smell...I wonder why I never noticed it before."
    "Like acid...like rotting."
    "I turn, but I catch his robe falling open. I can see his chest...what remains of it."
    
    ro "Soume---"
    
    "It's all bones. His pale skin pulled tightly over them. There is barely any muscle to him, any meat at all."  
    "It looks as if someone has stretched the scarcest amount of flesh over a skeleton."
    
    "He catches me staring, and closes his robes quickly."
    
    ro "Soume--I--I didn't--"
    
    "He's starving. I'm talking about my gripes and he's been starving, and from the look, on the verge of death."
    
    s "..."
    
    "He isn't letting me go. I'm worried now...he's just staring at me. Staring at me like--"
    
    #Soume's voice is very quiet.
    s "Do you know I'm so hungry right now I could swallow you whole and go into the hallway for more?"
    
    "Oh god."
    "I start to struggle in his grasp, but his bony fingers have me tight."
    
    ro "Soume...Soume please...don't--"
    
    s "You're so lucky, to be able to eat dead things. Even that meat in the kitchen is hardly satisfying...it's been dead too long. My stomach only takes one kind of meat well..."
    s "...fresh...live...meat..."
    
    ro "No--no--"
    
    "He's baring his teeth. After all that...this is..."
    
    s  "…"
    
    "He lets me go. I shuffle backward."
    
    s  "I’ve tried to stop. I've tried a myriad of other food. My body can’t digest it. It makes me ill. So on occasion...I clean up after battles."
    
    ro "You don’t eat...live then?"
    
    s "Not for some time. I barely get any energy, any strength from corpses.  Fresh meat is the only thing that really satiates my hunger."
    
    ro "Soume...I...I was so insensitive, I didn't think that you...you never ate anything...god, I'm so STUPID, how could I just---"
    
    s "As for the Doctor, he's worried that I'll give him a bit of payback for his actions against me, but tell him not to worry, I've no interest in his stringy tough flesh."
    
    ro "Payback?"
    
    s "Yes...but that isn't appropriate to discuss in good company. As for my secret...I'd appreciate it if you kept it to yourself."
    
    "He puts his hand on top of mine. I should run off screaming. Animal meat I can tolerate, but human? Other Majin?"
    "But he smells so powerful, and this is Soume we're talking about..."
    "What should I do?"
    $bc1 = False

menu:
    "Pull away.": 
    #This will divert to the Soume/Roman scenes at the end of the game (instead of Kazutaka's ending, and go to a bad ending where Soume will kill Roman, as well.
        jump pullaway
    "And with that, I leave the garden. Eating people, even if there is nothing else...I can't abide by it."
    "Stay close.":
        jump kaz3b

label pullaway:
    ro "I'm sorry Soume...I can't...I can't---"
    ro "I can't surround myself with that. I've suffered enough already."
    s "............."
    s "I see."
    $ bc1 = True
    jump goshop

label kaz3b:
    "I stay within his grasp, and allow him to hold me."
    "This is the right decision. There are times where one must throw away their ideas to accommodate the fact that others, different from us, must co-exist with us."
    "I want Soume to live."
    
    "And now, I know his deepest secret.  And he knows mine."
    "It isn't his fault. He's only dealing with the hand that life has dealt."
    
    "We sit in silence for a long while."
    
    ro "The air really does smell lovely today."
    
    s "Thank you. I tried to make the flowers to your tastes."
    
    ro "...really?"
    
    s "Of course. You're...special to me."
    
    "For the first time, I feel like I have a chance to touch this...otherwordly being that Soume is."
    
    ro "You're special to me too."

    $ decision = "10"
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

label goshop:
    
    su "You. Roman. A new mission."
    
    ro "Already? But I've just barely healed from the prior mission!"
    
    su "This one should be just fine."
    
    $show_message("Mission: Take Soume to the mall and buy him some new clothing. He's been wearing his for twenty years already.","medium")

    ro "...b-but...this...is a mission?"
    
    su "Do you have a problem?"
    
    ro "No...I'll...get right on it."
    
    "..."
    
    s " I…I really don’t know about this Roman."
    
    ro "Oh come on!  Miss Susa gave us some money and we might as well use it."
    
    s "Yes, but..."
    
    ro "Well, you need some new clothes! All of yours are so similar..."
    
    s "What’s wrong with them?"
    $bc2 = False
    
menu:
    "They're too girly...":
         jump toogirly
    
    "You need more color variety.": 
         jump colorvar
label toogirly:
    ro "They're too...you know...they make you look like a girl."
    
    #Soume sounds hurt.
    s "T-they do...?"
    
    "Ouch. The look on his face is really sore."
    ro "We'll get you some pants, that's all, for variety!"
    $ bc2 = True
    jump kaz4b
    
label colorvar:    
    
    ro "You just need more color." 
    ro "Pink and green is great, but blues and purples would really offset your hair and eyes."
    s "Blues and purples...?"
    jump kaz4b

label kaz4b:       
    s "Hmm...I don’t know about this."
    
    ro "Come on, it will be fun! And you haven't been off the shrine grounds in a while, right?"
    
    s "Mmn..."
    #Soume sighs.
    s "Alright. Please allow me some time to get dressed."
    
    r "Aren't you already---"
    
    "He's already locked himself up in his room."
    
    "*Two Hours Later*"
    
    ro "Soumeeeeeee. Aren't you ready to go yet?"
    
    "He finally leaves his room, in a flourish of amazing, flowery smells."
    
    ro "...wow."
    
    "He's dressed especially fancy, his hair tied up with ribbons, nails perfectly painted---is that rouge on his cheeks?"
    
    s "How do I look?"
    
    ro "...I uh--you look stunning."
    
    "Soume giggles and does a twirl."
    
    s "Shall we?"
    
    "It's a bit of a ride to the only mall in the area, and with Soume delaying us two hours, there's less time overall."
    "But I think it will be fun, to get to do something besides training with Soume."
        
    s "Hello!  Hello!  Hello!  And hellllllllllllo~!"
    
    ro "Soume...people are staring..."
    
    "Soume has taken the time to great every single potted plant we’ve come across.  I’d think it was cute if people hadn’t started gathering and staring."
    
    s "Of course they are, Roman. They always do. And I don’t want to be rude."
    
    "I would have thought that seeing a tall, beautiful slender man wearing a woman's clothing, hairstyle and makeup would make people whisper amongst themselves."
    "Instead, everyone in the area is just looking at Soume, as if enamored. It could be the smell in the air."
    "Soume always has a powerfully alluring smell around him."
    
    ro "..."
    
    "It's making me nervous, even though it isn't me they're focused on."
    
    "We finally make it to the mall, gratefully, and the shyness that Soume had shown at going out seems to have dissipated completely."
    
    s "Oooooh!  I could wear that! What a lovely fabric~"
    
    ro "Er...that is a curtain store..."
    
    s "Can we look in there?"
    
    ro "Later, Soume, I promise.  Let’s go in here first.  It looks like they have a good selection of kimonos."  
    
    s  "A kimono! That would be perfect! Some of mine are a little run down. Roman, you should get one!"
    
    ro "I don't...I would look awful in a kimono...just awful...let's try here..."
        
    s "Roman, I couldn't wear these sorts of clothing...these are for...well...business transactions in offices and the like."
    s "My old business, well, what I have now would be perfect."
    
    "I'm afraid, and worried, to ask what sort of business he was in."
    
    ro "Maybe try it on. I think it would look great on you."
    
    s  "Well, I suppose it wouldn’t hurt to...the color is wonderful."
    
    ro "Hold on, let me find someone.  Miss?  Excuse me, miss?"
    
    cl "Yes.  Can I…uh…help you two?  Find anything you like?"
    
    "Soume is--STRIPPING--oh god--calm down--okay, just to an undershirt of sorts, it seems. He pulls the jacket over it." 
    "I don't think he's ever worn a suit in his life."
    "The clerk is rushing over to him, and she looks terrified Soume is going to start tearing things apart."
    
    ro "Yes, there are a couple things he’d like to try on.  Is there a dressing room available?"
    
    cl  "Yes, he can-sir!  SIR!  Please do not step into the pants already.  He can use dressing room number-SIR!  Please stop tugging, you’re going to rip the collar!"
    
    "She’s ushering Soume across the store, and is dragging him by the sleeve while he reaches out and grabs whatever article of clothing catches his eye."
    
    s "Oooh~!  This one is nice, don’t you think Roman?"
    
    cl "You can use dressing room five.  Please be careful with the clothing, if you don’t mind."
    
    s  "Of course~!"
    
    "Soume shuts the door behind him.  I can hear movement behind it, and from the shadows it looks like he has started changing."
    
    cl "Are you two looking for anything in particular?"
    
    ro "Uh…not really.  He just needs some new clothing.  Something that will fit him.  He has a rather slender frame so I don’t know if-"
    
    s "Noooo.  No, I’m not wearing this."
    
    ro "You alright Soume?  Do you not like the suit?"
    
    s "It doesn’t fit.  I look silly."
    
    ro "Come on out and show us.  I’m sure you look fine, Soume."
    
    s "No, the whole outfit is just too baggy.  I look so awful."
    
    cl "Let us see so we can get an idea of your size, please, sir.  It will be easier for me to go find a suitable replacement."
    
    s "Eh…"
    
    "I hear the door unlock and Soume steps through.  The size itself looks close, at least in terms of height and length."  
    "But Soume was right; he looks absurd in the suit. There's something about the way he's...standing, perhaps, that makes me realize just how well his normal clothes suit him."
    
    cl "Oh dear.  No, this is not even close.  Your legs are much too long for these pants!"
    
    ro "Could you maybe go look for another size?"
    
    cl "I'll see what I can do..."
    
    s "I told you this was horrible…"
    
    ro "It isn’t terrible!  It looks fantastic!  You look quite dignified, Soume."
    
    "Soume blushes slightly and smiles at me."  
    
    s "Do you really think so? It's tugging awfully on my--"
    
    ro "W-Why don’t you try something else on? Here. Try these!"
    
    "...."
    
    ro "Any luck?"
    
    cl "I'm afraid not. He's just a bit too tall for our tallest size...perhaps try the store a little farther down..."
    $bc3 = False
menu:
    "Try the kimono store, like Soume wanted.":
        jump kaz5
    "Try to convince Soume to try another suit store.":
        jump kaz5a
        
label kaz5a:
    
    ro "Soume...let's try the other suit store..."
    
    s "I'd rather not. Can we just go home?"
    
    ro "...oh...of course..."
    $bc3 = True
    jump kaz6
    
label kaz5:
    ro "I'm sorry, Soume. I didn't know it would be so difficult. How about if we try the kimono store?"
    
    "Soume purses his lips and thinks very carefully."
    
    s "I'll tell you what. I will try on another suit, if you will try on suits with me."
    
    ro "No, you don't have to---"
    
    s "I wouldn't suggest it if I didn't want to!"
    
    ro "Okay! That sounds fair. But I don't look very good in suits..."
    
    s "No one looks good in a suit, Roman, look at the dreadful things.."
    
    "Soume disappears back into the dressing room with the clothes I picked out, and I go into another dressing room with suits he picked out for me."

    "I walk out, feeling completely ridiculous and fiddling with the tie."
    "Soume walks out shortly after, looking...stunning."  
    
    #Roman flushes.
    ro "I...uh...well, it..."
    
    s  "...?"
    
    s "Oh, are you having trouble with the tie? Allow me. I'm good at this."
    
    "He fixes my tie in moments."
    
    s "...and then you have to loop it through here like this..."
       
    ro "..."
    ro "Where did you learn how to do a tie?"
    
    s "Hm?"
    
    s "Oh..."
    
    s "Well, my masters wore a lot of ties. It's easier to get it perfect if someone helps."
    
    ro "...oh."
    
    l "Roman?"
    
    "I lose my train of thought as I hear the familiar voice.  Liza is walking quickly towards me.  She has a bag in her hand, and once she becomes sure it is me a smile spreads across her face."
    
    l "I thought it was you.  I would recognize your rigid posture anywhere.  You always do look like you’re about ready to salute someone."
    
    ro "Liza, so good to see you!  What are you doing all the way out here?"
    
    l "Shopping, of course.  What else would I do at a mall?  I am afraid my bedsheets have seen better days, so I was just purchasing some new ones."
    
    s "Miss Liza.  Greetings!  I certainly haven’t seen you in a while! It is great to see you in a friendly setting."
    
    "A friendly setting?"
    
    l "Ah. Soume. Hello."
    l "You certainly look better."
    
    "...do they know each other?"
    
    s "Roman has just taken me out shopping.  Would you like to take a look at what I’ve purchased?"
    
    l "Hm.  Perhaps some other time."
    
    ro "Just a quick look, it took us nearly all day to find something in his size."
    
    l "No, not today. I apologize, I am a little bit busy."
    
    s "Oh, of course.  No problem."
    
    "There's something happening here, and I'm not sure what it is."
    
    l "Hm. Anyway, how are you Roman? I heard you were in a bit of a scuffle the other day. Is your arm properly healed?"
    
    ro "Oh, it was nothing major. Soume healed it in minutes!"
    
    l "Ahh, yes, of course."
    
    ro "How did you know about the ambush? Have you been talking to Miss Susa again? I am so glad that you two--"
    
    l "What? Roman, I appreciate your interest in me, but I would prefer if we left my personal life where it is, hm?"  
    
    ro "My apologies.  I didn’t mean to overstep my-"
    
    "Liza waves her hand at me, and from the smile on her face I can tell she isn’t mad.  She does take a glance at her watch before she resumes speaking."
    
    l "Don't worry about it. I’m just afraid you never can take a hint unless I am especially emphatic about it, is all."
    
    ro "Yes, you have told me that several times."
    
    l "You are alright though? No lingering effects from the battle. Soreness?  Headaches?  Anything?"
    
    ro "No, no, and no.  Please don’t worry too much over me Liza. Soume is a wonderful healer. I didn't need a splint after the first day."
    
    s "Please stop flattering me like this, Roman. I easily blush~!"
    
    ro "Nonsense!  It isn’t flattery if it is true. He really is quite possibly the best healer I’ve ever met."
    
    l "Hm.  Yes, fascinating.  And how is life at the temple?"
    
    ro "Fantastic!  Pretty much the same as the last time we talked, but I honestly have never been happier."
    
    "Is it just me, or does Liza's smile look a little different than usual?"
    
    l "Well, I should be going, the days are getting shorter, after all. I will talk to you later, Roman."
    l "Soume."
    
    ro "Of course!"
    s "Have a lovely evening."
    
    "Liza turns and I can see her heading towards the stairs. She does at least have the appearance of one in a hurry, as she darts in and out of the slower people walking either up or down the staircase."
    
    ro "Well, that was a pleasant surprise! I can’t remember the last time I saw Liza in person. What are the odds we’d run into each other here?"
    
    s "I wonder."
    s "I must say that was the best mood I think I’ve ever seen her in.  She’s usually so…formal."
    
    ro "I've heard similar about her, but she's always been friendly with me!"
    
    s "That's good. You should have more friends like her. She's incredibly capable."
        
    ro "Isn't she? I wasn’t aware you knew her though. She’s never mentioned that to me…"
    
    s  "Ah, well it was a long time ago. We've worked together on a few things, nothing complicated."
    
    "I know if I press him, he won't answer."
    "I don't bother."
    
    ro "We used to work together too! But I know her best because...she was one of the regular visitors of the rescue I stayed at in Russia."
    ro "She helped me figure out who I really am."
    
    s "Is that so..."
    s "I will have to thank her, sometime."
    
    "Soume's being so cryptic today."
    "He gets like this sometimes."
    "I'm used to it by now, I think."
    
    ro  "I can't thank her enough." 
    ro "She’s the one that brought me to the rescue. To Miss Susa. It was on our travels together that we became close."  
    
    s  "And now you call and bother her at night?"
    
    ro "I don’t bother her!  She enjoys our calls!"
    
    s "Suuuuuuuuure~!  Whatever you say, Roman."
    
    "Soume winks at me and, with renewed energy, runs back up the stairs to explore the other side of the mall."
    "This might be the happiest I’ve ever been in my life."

    $inventory.unlock_item("kimono")

label kaz6:
    m  "Damn. Hmph."
    
    m  "That youko is making a fool out of me."
    
    m  "What does he think he's doing?"
    
    #play sound knocking
    
    na "You all right?  Took a hell of a beating the other day.  That tree trunk came outta nowhere, huh?  WHAM!"
    
    m  "Don't patronize me."
    
    na "I'm just saying. I think we should have just killed that plant asshole." 
    na "I'll off him myself."
    
    m "..."
    m "Naomi, you somehow manage to cheer me up..."

    m "I’m often surprised when a simpleton manages to live as long as you have. In one piece."
    
    na "......."
    na  "I'm just looking out for you."
    
    m "It's unnecessary. And you'll do well to remember your orders, and not your feelings."
    
    na "..."
    
    m "If you had distracted him a moment longer..."

    na "Boss, if I may...this is unlike you." 

    m "You'd do well to stop now."

    na "Look--I've worked with you for five years now! I can tell!"
    na "You're distracted by that youko."

    m "Naomi--"
    na "The plan was to grab the doctor, but you went and played with the little runty whateverhisname."
    
    m "..."
    
    na "A guy of his calibre isn't even worth being your food."
    na "Why did you abort the mission?"
    
    m "......."
    m "Your life is treading on thin ice."
    
    na "We've had this plan in the works for months. That doctor almost never leaves the temple and getting another chance that good will never happen again!"
    na "You BLEW the whole thing up to get your hands on that kid."
    
    m "..."
    m  "I have my reasons."
    m "Our future plans will be easier if he is eliminated, regardless of what the Church thinks."
    
    na "Our plans, boss? Or your plans?"
    
    m "..."
    
    m "Well that depends. Where do your allegiances lie?"
    na "..."
    na "With you."
    
    m "Very well then. Here is the new plan..."

    $ decision ="11"
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

label kaz7a:
    s "Good morning, Riku. Are you ready to move on to the next level of your training?"
    r "The next level, huh?"
    r "Alright. Lay it on me!"

label power2:     
    $result = minigame("power", 2, 2000, "bg dsky")
    if result == True: 
            jump powerfail2
    else: 
            jump powersucceed2

label powerfail2:
    r "Ugh...harder than I thought. Let's do it!"
    s "Oh my..."
    s "That's...would you like to try again?"

menu:
    "Of course! No way I'll quit!":
	jump power2
    "Nah, this is too much."
        jump endpower2

label endpower2:
    s "Alright. You can try to practice this anytime you want, okay?"
    r "Thanks, Soume."
    jump kaz7b

label powersucceed2:
    $hp += 50
    $mp += 10
    s "Excellent work, Riku. I think we're done for today, since you got the hang of it so quickly."
    r "Whew! I didn't think I could take anymore!"
    s "You did well. Have a good night's sleep, alright?"
    r "Definitely."

label kaz7b:
    r "Actually Soume, before I go..."
    r "How come our training has changed all of a sudden?"
    r "We didn't used to do this kind of intense stuff before."
    s "Well, your powers still get out of hand here and there."
    s "Training your body, your spirit and your mind will help you to put some of that wayward energy toward a very powerful focus."
    r "I thought I was getting the hang of this stuff..."
    s "You are, Riku, make no mistake."
    s "There is just always room for improvement."
    r "Mmmmrgh. Can we go a little while longer, tonight, then?"
    s "Anything you wish."
    "......"
    "We end up training so late I collapse right into bed..."
    call sleep
        
label kaz7c:
    "Sunday. My favorite day. I just get to lie around doing nothing."
    r "Teeeeeeveeeeeeee, teeeeeeeveeeeeeee..."
    "I head for the main room, the only room with a decent television in this whole place."
    r "....aw."
    "Miss Susa's already on it."
    "Doesn't she have a TV in her room? Why does she gotta get on THIS one out HERE?"
    su "DIE! DIE DIE DIE!"
    su "HA! EAT THAT! TAKE IT AND SHOVE IT RIGHT UP YOUR---"
    "...interesting."
    #play sound footsteps
    r "Oh cool! You've got one of those game things!"
    "It looks like some kind of shooting game...like the one I had to replace the gun for."
    "She's pretty good at it."
    su "BLAM BLAM BLAM BLAM BLAM! YEAH SUCK ON THAT!"
    "It's kind of funny to watch her."
    #play sound negative game over
    su "AWWWWWWW FUCK! What the HELL! I HIT THAT!"
    su "Did you SEE THAT? I FUCKING HIT IT! FFFF---"
    #play sound cracking
    ".............."
    r "....guh...."
    "I better run. She just stepped on the video game box and I know it's gonna be my faul---"
    su "Kid, get over here."
    "..........damnit."
    r "...I-I-I---"
    su "Cool your damn jets. I do this all the time."
    su "C'mere. You got little tiny hands, it'll be easier for you to figure it out."
    r "...oh--I see. The pieces just popped out."
    su "You mind?"
    r "....mmrph. My hands aren't that small."
    su "Sure kid. Whatever makes you feel good."

label gear2:    
    $result = minigame("gear", 2, 1000)
    if result == True: 
            jump gearfail1
    else: 
            jump gearsuc1

label gearfail2:
    su "Oh GIVE ME THAT! You're terrible!"
    r "I told you my hands weren't that small! Sheesh!"
    "I don't think I'll ever please this lady!"
    jump kaz7

label gearsuc2:
    su "Hey, I guess you aren't completely worthless at this."
    r "......"
    su "Well, thanks. Come sometime and play."
    r "...sure." 	

label kaz7:
    k  "No.  No, that can’t be right…"
    k  "I’m sure I checked all the variables."
    k  "Was this calibrated…?  Ah.  Yes, here is the problem.  Of course."
    k "How did I miss that?  How could I miss that?"
    k  "What is wrong with me?  These errors are the mistakes of a novice, of a child without any experience."
    k "I don't MAKE these mistakes."
    $renpy.pause(1.5)
    #play sound hand slamming on desk
    
    k "........."
    k  "...why couldn’t I sense the danger in that forest?"
    
    k "........."
    
    k "I need to focus. I will be able to figure this out." 
    k "There has to be something here…something that I overlooked…"
    
    k  "How could I be lured into so rudimentary a trap? An ambush?" 
    k ".........."
    k "It isn't possible that I would be unable to detect such imminent danger…"
    
    k "I’ve spent so long honing my sensory skills to such precise calculations; I once detected an angry hornet a quarter mile away."
    
    k  "Could I have missed a sign?"
    k "..........."
    k "No!  Impossible!"  
    k "I don't let my mind wander easily to frivolities, and even if I were fatigued the danger signature should have been nigh electric."
    
    k  "Is it possible that Mamoru drafted a way to overstep my abilities?"
    k "---no, I avoided giving them any of the key information."
    
    k "And if they had that information and could reach me at any time, why would they go after me with a full platoon for protection?"
    k "No, there is something different about these circumstances..."
    k "Something specific that I am missing."
    k "..........."
    k  "I must be. I cannot be wrong."
    
    k  "…it must be Soume."    
    k "To muddle my senses without my knowledge...for a youko, that is a trivial power display."
    k "By that alone, it must be him."
    k "......."
    k  "...oh. I’ve confused my variables here. No wonder my equations were off."
    
    k  "But they’ve found me."
    k "They want to take me back there."
    k "I can't let them. I can't do those things again."
    
    k "No. Calm yourself. They may not have been after you."
    k "...."
    k  "Of course they were after me! I am the most useful to their goals..."
    k "...."    
    k  "I have to...ARGH!"
    
    #play sound  Footsteps and door opening
    show bg hallway
    #screen shake
    s "Ah, Doctor Osamu. I'm sorry, I didn't realize you were out here."
    
    k "Watch where you’re going, you oaf!  You nearly walked straight into me.  I could’ve fallen, but I expect that is exactly what you were hoping for, isn’t it?  Hmm?"
    
    s  "Of course not. Please forgive me."
    
    k  "Hn." 
    k "My, my. Look at how much you’re glowing tonight. Fresh off a meal, are you?"
    
    s  "..."
    s "I’m sure I don’t have the moral high ground that you do, Doctor. Tell me again about those experiments you used to do?"  
    
    k  "......."
    k "...you know I was under orders. I had no choice."
    s  "Then you understand that concept well."
    k "Tch..."
    
    k  "That cheerful attitude of yours will surely sour after I’ve had my talk with Miss Susa."
    k "Don’t think you will forever be able to skulk around here, poisoning everything with your presence."
    
    s  "We shall see, won't we?"
    
    k  "You---"
    k "How can you be so casual?"
    k "I'm telling you I know!"
    
    s  "It's as I said. We shall see. Good afternoon, Doctor."
    
    #play footsteps
    
    k  "Hmph. Keep that smile on your face while you still have the opportunity, Soume."

    $ decision ="12"
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
        
label kaz8a:
    s "Good morning, Riku. Are you ready to move on to the next level of your training?"
    r "The next level, huh?"
    r "Alright. Lay it on me!"

label mole1:
    $result = minigame("mole", 1, 3000)
    if result == True: 
            jump molesuc1
    else: 
            jump molefail1

label molefail1:
    r "Errrr...that wasn't good, was it."
    s "Well, at the very least I don't have to explain it..."
    s "Perhaps another attempt..."
menu:
    "Try again?":
       jump mole1
    "Some other time.":
       jump endmole1	

label endmole1:
    s "...if you wish. You can try again whenever you feel like."
    r "Thanks, Soume. See you tomorrow?"
    s "Same time."
    jump kaz8

label molesuc1:
    s "Very good!"
    r "Those damn things are fast, but I'm WAY faster!"
    s "Alright, I think we're done for today."
    r "Whew! Free afternoon!"
    
label kaz8:
    #play sound  Knocking
    
    su  "Whaddya want?"  
    
    k  "Ah.  Miss Susa, I really hope I’m not interrupting anything.  I really need to talk to you though, if you have the time."
    
    #play sound door opening
    
    su  "I’m kind of in the middle of the something here...once I finish looking at these documents, I can get back to you..."
    
    k  "Well…ah.  You see, this is rather important...can we possibly discuss it now? I am afraid time may not be a luxury we have."
    
    su "Doctor, if this-"
    
    k  "In fact, perhaps I can help you with whatever it is you are working on.  Another set of eyes, you know.  Let me just take a look at-"
    
    su  "No!"
    k "....."
    su "...I don’t want to trouble you with this. It's...trifling business, really. I’ll just put this aside for now."
    
    k "What was that a map of, if you don’t mind? I am ashamed to admit the area outlined on it did not look familiar to me."
    
    su "I just received news of another Majin. Further north than we usually go, so I might take on this job personally."
    
    k "Personally, Miss Susa? Is that wise? The temple will be largely unguarded without your power..."
    
    su "I used to do missions all the time. And I could use a little vacation from this place."
    su "Besides, Soume is perfectly capable of guarding this place as well as I."
    
    k "That's actually what I wanted to discuss with you..."
    k  "I know we've discussed this before, but there was something quite odd with that last mission." 
    k "I’ve always been able to trust my sensory abilities before. They have never failed me. I’ve honed them to perfection."
    
    su "Are you still thinking about that? People make mistakes. You aren't infallible." 
    
    k  "Of course, infallibility is...perhaps out of my reach, but I know my skills, Miss Susa." 
    k "I must have been sabotaged. There is no other logical answer."
    
    su "Our enemies are powerful. If Mamoru was there, well, you know his capabilities can seem nearly limitless."
    
    k  "I’ve dealt with him before. I know what he can do, and I was prepared for that." 
    k "I’ve been able to sense him in the past without issues.This had to have been the interference of someone else."
    
    su  "Mamoru's ability to adapt is unprecendented. Your calculations may have simply been wrong."
    
    k  "No! I can’t have made such an egregious error! There has to be a spy!"
    
    su  "I will say it once more, Kazutaka, you are completely wrong on this one." 
    su "You have made this accusation several times and not once have you brought concrete proof."
    
    k  "Miss Susa, please! I’m begging you to listen to me. I am in serious danger! They are after me, and it is all his fault!"
    
    su  "CALM yourself. You're acting completely irrational!"
    k "........"
    k  "Y-you're correct. I...apologize."  
    k "But please, you must understand the severity of this situation."
    
    su "And you need to understand you’re not in any danger."  
    
    k  "I’m not!  Miss Susa, we need to at the very least search his things, quarantine those plants, something---"
    
    su "Absolutely not. Stop with these baseless accusations." 
    su "That is not a suggestion."  
    su "Soume is not a spy. Trust my judgment, or bring me concrete proof."
    k "..........."
    k  "...I understand. Forgive my brashness, Miss Susa."
    
    su  "It's fine, but I’m pulling you off missions temporarily."
    
    k  "I wasn't planning to leave here anyway."
    
    su "Just until Mamoru directs his interests elsewhere."
    
    k  "...yes, of course."
    
    su  "And Kazutaka?"  
    su "This isn’t a punishment. I don’t have to remind you how important you are to the rescue."
    
    k "Understood."
    su "...."
    su "Ah, that reminds me."
    su "How about taking on an apprentice?"
       
    k  "An apprentice?"
    k "I suppose...it might be a good idea..."
    
    su "Take the Riku kid."    
    su "He seems to improve your mood, and it'd keep you occupied from your little delu--well, you'd be occupied."
    
    k  "Hmph. I suppose he does have...potential, but I don't think he has the ability to last long-term."
    
    su  "He doesn't. Not yet at least. Give him a couple hundred years."     
    k  "...if I have that long."
    su "...excuse me?"
    k "It's nothing. What if he doesn't show promise?"
    
    su  "Tell him I’ll put him back on toilet duty. With a toothbrush. And he won't be able to use his hands."
    
    k  "...that may work."
    su "....."
    su "Are you feeling a little better now?"  
    
    k  "Yes. I do apologize for my outburst. My rational sense left me for a while."
    
    su "Good. Sorry to rush you out, but I need to finish this analysis. You can see yourself to the door."
    
    k  "Yes, of course."
    k "Have a good evening."
    
    #play sound  Door closing
    
    k  "Hmph."
    k  "Unbelievable."
    k  "Simply unbelievable."
    k  "I believed Miss Susa to be a woman of intelligence and sound judgment."
    k  "I've given her too much credit."
    k "It was ridiculous of me to trust humans."
    k  "What a simpleton.  What a plebian.  How dare she question my assessment."    
    k  "Who does she think she is?  Questioning my mental state like I am some sort of school boy, wasting my time with trivial concerns and gossip."
    
    k  "..."
    k "But I cannot face any of them alone. Proof. I need proof."
    k  "And I need someone to help me."
    k "Hmmm."
   
label kaz9:
    #Roman vegetarian food scene!
    r " Ehh...what did you say this, er, thing is?  Somethin’ about this don’t look right to me…"
    
    #Roman chuckles.
    ro  "Riku, I believe you are being rather overdramatic.  It is called a Falafel Seitan Bratwurst.  Something I picked up from my time in Germany."   
    r " ...yeeeeah.  This doesn’t look like any Bratwurst I know."  
    
    "I turn over...whatever this thing is...with my fingers."  
    "It's nice and all for him to cook for me, but I'm just not interested in this vegan stuff."
 
    ro  "Riku, please just try it. You wouldn’t even know it was vegan if I hadn’t told you."
    r  "Yeah.  I’m...uh...getting around to it. It’s just a little hot, is all.  Yup."
    ro  "..."
    ro "You owe me for the cake, before."
    
    r  "...do I gotta?"
    
    ro  "Just try it."
    r "...."
    r  "So, uh, Soume’s garden smells pretty good."
    
    "That last part isn’t a lie." 
    "The flower smell has been getting stronger lately...I’m kind of getting a little light-headed from being downwind, but I can’t complain. It makes me feel calm."
    
    ro  "Stop stalling.  I’m just asking you to try it; if you don’t like it I’ll finish it."  
    ro "I spent all afternoon cooking that for you, and you still owe me for that cake, so please, just take a bite."
    
    r  "Okay okay, fine. If this makes me sick though, I might never talk to you again."
    
    ro  "I appreciate your faith in my cooking prowess!"
    
    r  "Hmph.  You’re just lucky I like you.  Now…let’s see here…"
    
    "Okay.  C’mon Riku.  Do it for Roman."
    
    "Roman is looking at me with a big grin on his face."
    "Why would anyone want to make fake meat? It's fake. Fake is like a secret code for 'shittier than the original'."
    "Plus, the color in this thing is all off.  Smell too."
menu:
        "Riku, you can do this.":
            jump eatthefood
        "AGH just NO WAY!":
            jump canteatit
       
label eatthefood:            
    r  "Alright.  Ah, well…here I go."
    
    "I close my eyes and prepare for what I can only assume will be the worst thing I’ve ever tasted."
    "I take my first bite."
    r "....."
    ro "......"
    r "....."
    ro "...well?"
    r  "Huh. This isn’t terrible."
    
    ro  "See?"
    
    r  "Okay, okay. You were right. It's not half bad."
    r "I could actually eat this."  
    
    ro  "I’m glad you like it! I can make you some more, if you’d like."
    
    r  "Sure. Can’t believe I’m eating things made from dirt and sticks, but I guess a decent chef can make anything taste decent."
    
    ro  "Uh…it isn’t made from dirt or sticks."
    
    r  "Oh, so this isn’t vegan?"
    
    ro  "No, it is. It’s just that--"
    ro "......"
    
    r  "Relax, Roman! I’m just teasing ya."
    ro "Oh, yes. Of course. I knew that."
    "Poor naive bastard. I don't know how he lives with Soume's brand of teasing."
    $hp+=50
    $mp+=30
    $inventory.unlock_item("book5")
    jump kaz10a
    
label canteatit:
    "I stare at the guck in front of me. It stares back."
    "Mocking me."
    "Haunting me with its puce green gloppy glare."
    "I gag."
    
    r "Sorry, Roman, I can't. There are just some things I can't do and THIS IS IT."
    ro "You haven't even tried it!"
    r "It SMELLS. I can't, Roman. I promise I will make the cake thing up to you, but I CAN'T--"
    
    "I am really going to puuuuuuuuuuuuuke---"
    jump kaz10a
    
label kaz10a:    
    $ decision ="13"
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
        
label kaz10b:
    k "Oh Riku~ I need a little bit of your assistance, if you don't miiiiiind~"
    "Uh oh."
    k "Nothing you haven't done before, but I have this other little tiny mechanism that needs a little fixer-upper~"
    r "Alright, lemme see it."

label gear3:    
    $result = minigame("gear", 3, 1000)
    if result == True: 
            jump gearfail3
    else: 
            jump gearsuc3

label gearfail3:
    k "You've just messed it up further! Arghhh!"
    r "Well maybe you should fix your own stuff!"
    "SHEESH!"
    jump kaz10

label gearsuc3:
    k "An admirable display. I thank you."
    r "You're we--"
    "He's already slunk back into his lair."
    "Huh."
    
label kaz10:    
    su  "Oi!  Hey brat, get over here."
    
    "Damnit."
    "That’s what I get for being too happy. I’m almost convinced she can sense when I’m happy, and that sets off some sort of alarm in her office that she needs to go and make me miserable."
    
    r  "Look, I already cleaned all the light fixtures--"
    
    su  "What?"
    
    r "...nothing."
    
    su "Anyway. Gotta mission for you."
    r "I--I don't think that's---"
    su "Don't shit your pants just yet. You can handle this one."
    r "...what is it?"
    su "Roman’s birthday is coming up. His hundredth."
    
    r  "Oh yeah...he mentioned that. It's that soon already?"
    su "No, I'm just talking for my health."
     
    r  "......."
        
    su "A hundred years is the big one, so I want to throw him a party or something."
    r "Oh cool! I haven't been to a party in forever!"
    
    #play sound  -smacking noises-
    
    r  "OW OW OW!"
    
    su  "It's supposed to be a surprise, so quit fucking screaming about it!"
    
    r  "Surprise?"
    su "I'm sending you to the doctor to get your hearing checked. Yes. A surprise. As in, don't fucking go blabbing to him about it."    
    r  "So what do you want me?"
    
    su  "I'd plan it myself, but I’m busy."
    
    r "Busy doing what? All you do is play video games!"
    su "..."
    "I probably shouldn't've pushed my luck that far."
    su "...I can rip off your head, if you want."
    r "No thanks, ma'am."
    
    su  "Your mission is to prepare, set up, and throw Roman a successful birthday party"
    
    r  "B--why me? I've never thrown a party in my life!"
    
    su "Well I guess you'll learn, won't you?"
    su "Besides, you know Roman pretty well. You can figure out what kind of things he likes."
    su "Ask around."
    call birthdaygame

    
label kaz10c:
    
    su  "Hurry up and get off to bed. Wake your ass up early tomorrow and make sure Roman stays in his room until at least nine."
    
    r  "Got it."

label kaz11:
    "I set my alarm extra early today for Roman's party."
    "Roman's a super morning person, and if I don't beat him, I'll be pissed at myself."
    "I don't even bother to shower, just throw some clothes on and head for his room."
    
    "I turn the corner just in time to catch him."
    r "Yo, Roman!"
    
    ro  "Ahh, good morning, Riku!  Excuse me for asking, but today is Sunday. Why are you running?"
    
    r  "Oh…huff huff…just, y’know…huff…exercising.  Gotta…huff…stay in shape!"
    
    ro  "Ah.  Well, you must have been running rather fast if you are winded."
    
    r  "Yeah, well, extreme training and all that. Miss Susa’s orders.  For…mission…uh-preparation."  
    
    ro  "Hm. Strange. Oh well. If you’re done training, you are more than welcome to come with me to breakfast, I was just heading-"
    
    r  "NO!"
    
    ro  "...excuse me?"
    
    r  "No---breakfast yet. I…uh…really need to talk to you. I need a tour of your bedroom!"
    
    ro  "Perhaps this could wait...I'm awfully hungry."
    
    r  "Awww c'mon, we'll eat in a little bit, lemme see your room!"
    
    ro  "Well…I suppose. This is all rather sudden though, isn't it?"  
    
    r  "I’m just curious. We been friends for a while now and I've never REALLY seen inside."
    
    ro  "I see... Come in then."
    
    "Roman opens the door back up and ushers me inside.  I step in, and I immediately feel a change of temperature of like twenty degrees."
    
    r  "Whoa! Why is it so cold in here?"
        
    ro  "Oh, I forgot...I prefer it to be a bit colder than most, perhaps."
    
    "There are ice sculptures of different kinds everywhere."
    "Books, and some other things from Europe or Russia or something, probably."
    "In one corner are a few straggling plants, growing."
    $renpy.pause(1.5)
    "Poorly."
    
    r  "Uh…those plants over there alright?"
    
    ro  "I'm afraid not...I just don't have a green thumb like Soume does."
    
    r  "Might have something to do with the sub-zero temperature in here..."
       
    ro  "But Soume said that these were resistant to the cold, I must be doing something else wrong."
    
    "Roman gives me the tour of his room, which I draw out as long as possible by asking questions about everything."  
    "This is harder than you might imagine."
    
    r  "Man, it is really cold in here."
    "Probably about the fortieth time I've repeated that."
        
    ro  "Yes, you mention---hey...are you alright?"
    
    r  "Hm?  Yeah, I just…"
    
    "I think the temperature in Roman’s room is starting to get to me, but it's odd."
    
    r  "I dunno.  My head just feels kinda weird."
    
    ro  "Weird? In what way?"
    ro "It's because you're a flame user, isn't it? The cold is too much."
    
    r  "No, it's not that..."
    r "I don't really know how to describe it...it's like I just woke up."
    r "I don't feel sick, I feel better, if that makes sense. Like I was walking through fog and just got into the open."
    
    ro  "Perhaps we should see the doctor..."
    
    r  "NO. No way. I'm fine now. Great, actually!"
    
    "I do feel pretty good physically, but something in my gut tells me that whatever just happened wasn't right."
    "I feel like the happy's been sucked out of me. Like I'm depressed all of a sudden."
    
    r  "...do you feel...sad all of a sudden?"
    
    ro  "Sad?"
    ro "No. Why?"
    
    r  "N-nothing. I'm just being weird."
        
    ro  "Well, I still think you're having a reaction to the cold, so let's head to the kitchen. I'm really hungry now."
    
    "I look down at my watch. Just about 9. Good, I can’t take being in this room much longer."
    
    r  "Sure! C'mon, follow me."
    
    "I quickly head out of Roman’s room, and make a mental note to avoid it in the future."

label kaz12:
    ro  "Riku, I think you must be lost.  This isn’t the way to the dining area."

    r  "Uh…yeah, I forgot something.  Just come with me for a sec.  We’ll head over to the dining area together after the…after I find the thing."

    "Riku is acting awfully strange this morning."

    ro  "Can’t you just find it and meet up with me later?"

    r  "C'mon, we're almost there! Race ya to the end of the hall!"
    
    "He takes off running, and my head droops."
    "I just want to get some breakfast!"

    r  "Here we are..."
    
    "We're in front of one of the rooms in the temple."
    "No one really goes in here, so I don't have a clue why Riku's would have lost something in this room."
    "Something is really fishy..."
    
    r "Go on in!"

    ro  "Huh? You're the one who's lost something! Go and get it so I can eat!"
    
    r "Okay okay, fiiiiiiiine."
    
    "Come to think of it..."
    "The temple is awfully quiet today, as well..."
    
    ro "Aaah!"
    
    "Riku shoves me inside the room. It's dark."

    ro  "Riku, what the heck is going---"

    #play sound light switch click

    "SURPRIIIIIIIIIIIIIIIIISE!"

    ro  "Ah!"

    su  "Happy birthday, Roman!"

    ro  "Miss Susa?  Riku, is this…?"

    r  "Yeah, yeah.  Happy birthday, pal.  Sorry to lead you around everywhere like that, but Miss Susa made me."

    su  "Oi.  Sprog, get inside and get to the table.  I’ve prepared a breakfast feast for you, Roman.  All vegan, of course."

    ro  "You shouldn’t have…this is amazing."

    su  "Yeah yeah, hurry up and take a seat."

    "All of the students are here."
    "Even Doctor Kazutaka looks in my direction and grunts something that sounds remarkably similar to happy birthday."
    "And of course..."

    s  "Happy birthday, Roman!"
    
    "I blush. I can't help myself."
    ro  "S-Soume...you were in on it too..."

    s  "Naturally. Do you like the decorations?"
    
    ro "I love them."
    "I love everything he does for me."
    
    su  "Well, you look surprised enough. I'M surprised that brat didn't blow everything."
    
    ro  "No, no!  Riku played his part excellently!"  

    r  "Hmph.  Hear that, Susa?  Excellently!  You can thank me later."

    su  "Yeah, that’ll be the fucking day.  C’mon, Roman, dig in.  Don’t tell me you’re not hungry."

    "She doesn’t have to tell me twice!"
    $renpy.pause(2.0)
    
    "It's evening now. We've been partying most of the day."
    ro  "Miss Susa, I really must thank you.  I can’t remember having a better time."

    su  "Hrm?  Oh, well, I suppose that has more to do with the company you’re keeping these days, huh?"

    "She looks down and checks her watch."  
    "She’s been checking her watch all day, and taking time out to go and adjust her hair in the mirror every couple of minutes."  
    "I wonder..."

    su  "There's one more surprise for you. I'll go get it."

    $renpy.pause(2.0)
    r  "Where she off to in such a hurry?"
    
    ro "I’m not sure.  She says it is a surprise, so I would gather you might know more about it than me."

    r  "Pfft. I never know with that lady."
    
    ro  "But you know, Riku, she must like you to be giving you all this attention."  
    ro "You’ve been able to accomplish much in a very short time."

    r  "I think it was better when she wasn't impressed..."

    ro  "She isn't hitting you nearly as much now, though."

    r  "That IS true..."
    $renpy.pause(2.0)
    r "Hahahaha, look at Soume dancing!"
    
    "Soume is dancing awkwardly with one of the younger students."  
    "He's awfully good at it."
    "I don't have any rhythm at all."
    $renpy.pause(1.0)
    "Maybe he'll teach me."
    "Maybe I should ask him."
    "Heh, I couldn't possibly!"
    "............" 
  
label kaz13:
    l  "Oh, leaving already?  This is hardly a way to great an old friend, I would think."
    
    ro "Liza!"
    
    "I throw my arms around her and hold her tightly."
    
    l  "Happy birthday, Roman."
    ro "Thank you, Liza. I know it is difficult for you to take time out..."
    l "Nonsense. You're a dear friend. I had to make an appearance."
    l "Why don't you show me around a little?"


    l  "Hmm…so this is your room?"
    
    ro  "Yes. I put all the ice sculptures I've made here, so I can test my growth."

    l  "I see."
    l "You have certainly improved your craft."
    ro "I practice very hard."
    
    "Liza wanders over to my paltry looking plants."
    l "And taking up gardening, I see."
    
    ro  "A little...I'm not very good at it."
    l "Well, we can't all have every talent."
    ro "That's true. Come on, I want to show you outside."
    ro  "Is this your first time actually visiting the rescue?"

    l  "Not quite. I used to visit it rather frequently, many years ago." 
    l "It has changed quite a lot since then."
    
        
    ro  "Oh, how so? ---this here is Soume's garden. Isn't it lovely?"
    
    l  "This garden is certainly new. A rather impressive array of plants, to say the very least."  
    l "I should think all that security Susa has installed would be rather moot with Soume’s army of plants down there."
    
    ro  "Well, the plants are more of a backup plan. Sort of in case of emergency; if we are somehow found we at least should have a chance to fight back."
    
    l  "Indeed."
    
    "We walk for a little while longer." 
    "It is really quite relaxing, being able to talk to Liza like this."
    
    ro  "So, how did Miss Susa manage to talk you into coming out here?  I didn’t really think the two of you were on…ahem…speaking terms."
    
    l  "Ah. Well, we had some business to discuss anyway."

    ro "Ahh, you don't have to tell me if it's private."
    l "It is in fact private, and I had no intention of telling you."
    ro "Oh..."    
    l "Don't feel bad. It's not as if I'm leaving only you out of the loop."
    $renpy.pause(3.0)
    ro  "And this is the library. It doubles as Doctor Osamu's laboratory.  His office is just down the hallway."  
    ro "I’d take you inside, but he'd likely get angry..."
    
    l  "Oh, don’t worry about it.  I’m fairly familiar with his work, and I’m sure he’d show it to me if I asked him to."  
        
    ro "I think you overestimate his good nature..."  
    
    l  "You might be surprised."
    
    ro  "Why's that?"
    
    l  "Ah--nothing, really.  Look, Roman, I wanted to ask you something.  Well, offer you something, actually."
    
    ro  "Such as?"
    
    l  "I was just wondering...well, would you like to move in with me?"
    
    ro  "…move in with you?"
    l "Yes. I have a very large place, and I would personally oversee your continued training."
    
    ro "Why...would you ask that now?"
    l "Well, we don't get to see each other very much anymore...it would just be easier if we lived together."
    
    "Why would Liza ask me that question?"
   
menu:
    "I...can't, Liza. There's...someone...":
        jump kaz13a
    "Move?":
        jump kaz13b
    
label kaz13a:
    l "...someone?"
    ro "...it's hard to explain."
    l "Ah. I see. Little Roman has found love."
    ro "No...it's nothing like that...he doesn't even--"
    l "It's okay, I understand. I won't ask again."
    ro "I'm sorry, Liza. I'd move in with you in a moment otherwise..."
    l "Just be careful, Roman. Be careful."
    ro "I will. I promise."
    jump kaz13c

label kaz13b:    
    jump neuend00
    
label kaz13c:    
    l "I'll need to go have my conference with Susa, but I did want to give you this."
    
    $inventory.unlock_item("gift")
    
    ro "Oh Liza, you didn't have to."
    l "But I wanted to, so take it and keep it."
   
    "With that, we head back inside, and Susa and Liza rush off to talk."

    if perparty:
        jump kaz13d
    else: 
        jump kaz13e
 
label kaz13d:
    "Evening fell so quickly, there's not much time left to enjoy my birthday."
    "What should I spend the last few hours doing?"
menu:
        "Talking to Soume.":
            jump sobirtalk
        "Talking to Riku.":
            jump ribirtalk
   
label sobirtalk:
    
    ro "Soume?"
    s "Ahh, Roman, come in."
    ro "Sorry to bother you...I just uh--"
    s "Hm?"
    "He still makes me so tongue tied.
    s "It's alright. Come sit down."
    ro "Thanks..."
    "It looks like he's been staring at a full moon."
    ro "Do you like the moon, Soume?"
    s "...hm?"
    s "Oh, ah...a little. It's so big and round tonight."
    s "I suppose it has an effect on me..."
    ro "Really? What sort?"
    s "...mm. Who knows."
    "Something brushes by my hand."
    "It disappears underneath Soume's robe!"
    ro "Soume...there...your robe...something just..."
    s "Oh, did I catch you? I'm sorry."
    "He starts to pull his robe OPEN--"
    ro "WAIT WAIT! I don't need to see--"
    "Tails! Two tails, twisting and turning."
    s "I have to let them out sometimes...it's much more comfortable like this."
    ro "...w-wow..."
    "I settle back down, but I know my face is pretty flushed."
    ro "...ahem."
    ro "Hey Soume...can you maybe...tell me about youko, a little more?"
    ro "I mean, since we're partners..."
    s "Hmm. You are right. It would be better for us both if you understood my biology, I suppose."
    s "How should I start..."
    ro "...how about with the tails?"
    s "Haha, alright."
    s "Well, youko start out with no tails at all. After they reach the first thousand years of life, they gain the first one, and one every thousand years afterward.
    ro "...you're TWO THOUSAND years old?!"
    s "Give or take a few decades..."
    ro "Wow..."
    s "At any rate, my weakest form is that of a basic fox. My human form is of course, a disguise, but my most powerful form is the youko form itself, which is a...hm. A blend of human and fox, so to speak. It gives me the greatest control over my abilities."
    ro "The youko form? Have I seen you use that...?"
    s "I try to refrain. It can be a bit overwhelming at times."
    ro "I see...but still, Soume. Two thousand years old. You must've seen all of history?"
    "Soume's mood suddenly sours. He turns away from me."
    "Was it something I said?"
    s "No. Not particularly."
    ro "But you must have! All the events in the bible...all sorts of wars...perhaps you even know the writers of the Bible! Jesus Christ! Was he real, like they describe?"
    s "......"
    "But Soume's staring at me blankly."
    ro "...what is it?"
    s "Nothing. I'm just not...sure what you're talking about."
    ro "Not sure? The Bible? Jesus Christ?"
    s "Never heard of them~"
    ro "...oh..."
    s "Well, I am awfully tired now, Roman. You should get some sleep too~"
    ro "Huh--oh. Yes. Good night, Soume."
    s "Good night~"
    $unlock_entry("Majin","046")
    jump kaz13e
    
label ribirtalk:
    "I'm. Really. Drunk."
    "I don't know how I continue to let Riku convince me to do these things..."
    r "Heeeeeeey...you ever realize how when you get reaaaaaaaaaaaally close to Soume...he smells really good."
    ro "Oh my yes...he smells like heaven..."
    r "Right? I thought it was just me..."
    ro "No...not just you..."
    r "...how does he do that? You think it’s a special soap or something?"
    ro "I don’t THINK so...sometimes it seems to just come out of nowhere..."
    r "You noticed that too, huh...?"
    ro "Oh, and! Have you noticed how startlingly attractive he is? I mean, just awfully attractive, for a man."
    r "...sort of. I guess, yeah. For a man."
    ro "I mean, it’s amazing, isn’t it? He’s probably the most perfect sort of person I’ve ever seen. Sometimes I can’t stop staring."
    r "...uh..."
    ro "Ahem. I mean, you know. For a man."
    r "...I dunno. What you said just now sounded...you know. Like you’re interested."
    ro "No way. I’m not. I’m NOT. He’s--just...special."
    r "I mean, I get what you’re saying. He’s pretty hot. If he---if he was a girl, I’d be ALL OVER THAT, you know?"
    ro "Yeaaaaaaah, all over. Wait---how can YOU be all over something? You’ve not even hit puberty yet."
    r "Right right okay, but. I’m just sayin’. If I HAD. And Soume was a chick? All mine."
    ro "It doesn’t even matter to me...he’s just...the most wondrous...fantastic...amazing person I’ve ever met."
    r "...are youuuuuuuu gay?"
    ro "What?! No...no way, whe--no!"
    r "Just sayin’ man, I know we’re drunk right now and stuff, but that sounded pretty gay from over here."
    ro "I’m just talking. Drunk talking. That’s all. I mean...erm..."
    r "Man whatever, I gotta pee and I’m goin’ to bed. Think I might get a hangover this time, heh."
    ro "Okay. Yes. You should...yes, the bathroom."
    r "Night, Romannnnnn."
    ro "Night, Riku."
    jump kaz13e
    
label kaz13e:
     "It's really late now."
     "I could just pass out..."

label kaz14:
    k  "I want to thank you for coming here to meet with me."
    
    l  "I already told you, Doctor, I came here for Roman. Having the extra time to meet with you was only a fortunate coincidence."
    
    k  "Well, regardless, you understand the situation at hand."
    
    l  "Perhaps, but I have to admit, I am a little confused as to why you don’t just bring this matter up to Susa. She is quite apt to handle it."
    
    k  "Hmph. I tried!  She’s too close to the situation.  She doesn’t believe me.  She won’t even listen to what I have to say."  
    
    l  "Well, even you must admit, this is a severe accusation. And you have no concrete proof to support your theory."  
    
    k  "I need for you to trust my talent. I know, perhaps, you are wary of me because of what you have heard in the past..."
    k "But there is no doubt in my mind. Soume is working as a double agent."
    l "Mm."
    $renpy.pause(1.0)
    l  "I cannot move on a hunch, Doctor. I cannot take action without evidence."
    
    k  "So, even you-"
    
    l  "I’m not saying I will not help you."  
    l "But there are too many things at stake to risk being incorrect."
    
    k  "My sensory powers are being toyed with. I have been having trouble lately, even in the sanctity of my lab."
    k "Is that not proof enough of something going on on temple grounds?"
    
    l  "But it is not proof that it is Soume."  
    
    k  "It MUST be him! There is no one else with that level of capability!"
    
    l "And I am afraid that once more, I must ask for proof of this claim."
    
    k "The circumstantial evidence is enough for a further look!"
    
    l "Then you must make that evidence concrete."
    l "I am dealing with another issue that is extremely important..."
    l "I cannot spare the time to examine this in your stead."
       
    k  "Damnit, what the hell do you expect me to do?"
    k "I can't get near him."
    
    l "Of course you cannot."
    l "He is not stupid either."
    
    $renpy.pause(2.0)
    l "Look."
    l "I think that what you claim is not impossible."
    l "But two people I hold in very high regard trust Soume with their lives."
    l "If you can pin even one thing on Soume, I will personally face him."
    l "Find out what is interfering with your sensory powers, and we may be able to use that to make a case."
    l "If there is one."
    
    k "I have been able to find nothing out of the ordinary."
    
    l "Well, I would recommend you think of something, quickly, if the problem is as urgent as you believe it to be."  
    l "I’ll do what I can from my end, but until we have an actual link to a suspect, I won’t be able to do anything substantial."
    
    k "And what about Miss Susa?  She told me to stop investigating matters, and that I should trust her judgement."
    
    l "Well then, it would be to your benefit to not get caught."
    l "I shall keep quiet about our dealings.  If the time comes that something needs to be done, I will speak to her directly."
    
    k "May I ask you something?"
    
    l "You may ask. I don't guarantee an answer."
    
    k "Why are you so open to this idea?"
    
    l  "Why indeed."
    
    k "Miss Susa dismissed me outright."
    k "Many have said I am being unfair."
    k "But you are at least listening to me."
    
    k "Why?"
    
    l "Don't mistake my intentions, Doctor."
    l "I am not 'on your side' or anything of that sort."
    l "I am merely entertaining the possibility that you are correct."
    l "And, I worry about Roman's safety."
    
    k "Of course.  You will forgive me, I suspect, if I misspoke."
    
    l "It is nothing."
    l "Take this. It is my direct line."  
    l "You may call this number immediately if you find anything out. I will call you if I manage to discover anything on my end."
    
    k "Do you believe you will?"
    
    l "I cannot say anything for certain."
    
    k "Right, well, keep in touch, if you don’t mind."
    
    l "I’ll call when I feel like I have some information you need to know, and not before that."
    
    k "Understood."
    
    l "Then, Doctor, I bid you good evening."

    $ decision = "14"
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
        
label kaz14:
    "This morning is an unlucky morning, I think."
    "I'm hungover..."
    "I stepped on something hiding under a pile of laundry."
    "And now this..."
   
    k  "Riku, would you please come see me in my lab at some point this evening?  I have something I would like to talk to you about."
    r  "...something like...?"    
    k  "Stop talking back and just BE here tonight."
    
    "He probably just wants me so he can test his new strain of bacteria out."
    
    r "Can't you just gimme a hint? A little one?"
    
    "...guess not, with the way he's looking at me."
    
    r "Fine, fine. I'll be there."
    
    k "Much obliged."
    
    "Grrrr..."
    
label scavenge:

    "I might be young, but I have no idea how I get dragged into these things..."
    ro  "Oh, please, come on?  I promise you that you will enjoy it!"
    
    r  "Ugh. Aren't you too old for this?"
    
    ro  "Come on. It's a scavenger hunt. The bonus is supposed to be very good."
    
    r  "I told ya.  I wasn’t gonna do it.  I just wanted to catch a quick nap.  Why didn’t you just partner with Soume?"
    
    ro  "Ah.  Well, Soume helped Miss Susa set it up.  He very well can’t participate in the scavenger hunt if he knows where some of the items are at."
    
    r  "Bah!"
    
    ro  "C'mon. Partner up with me!"
    
    r  "..........."
    r "Alright already! SHEEESH!"
    call scav_hunt    
    
label kaz16:
    #play sound Knocking at door-
    r "Thank god that's over..."
    r "But it's nice to relax every now and then."
    r  "Hey, Doc? You in?"
    
    
    "I’m not even sure why I'm here. I know he asked to meet with me, but..."  
    "I can think of like fifty different things Doctor Osamu might try to surprise me with, and nearly all of them involves significant blood loss."  
    "Still, he looked excited yesterday, and I’d feel like a bit of an ass if I didn’t even show up."
    
    r  "Hey, Dooooc, you there?"
    
    #play sound Knocking-
    #play sound door opening
    
    k  "Hrm...yes, that might be a possibility...no, no, what am I saying?  I would have had other symptoms.  But then what?"
    
    r  "Doctor Osamu? ...you said you wanted to see me?"
    
    k  "Hrm? Oh...Riku. Yes, please do come in. Take a seat over there, and be careful not to touch anything."
    
    "He clears off a spot for me on one of his chairs, which had previously been covered with a couple of old journals and loose papers, and returns to his chair."  
    "He goes to move his books to the side to clear off a little space on his desk, but before he finishes I manage to take a look at one of the titles."
    
    r  "'Common Majin Ailments of the Late 15th Century:  A Historical Perspective.'”  Just in for a bit of light reading there?"
    
    k  "Please. I wish this was just light reading. Unfortunately, while others in the shrine really aren’t in any hurry to find the traitor, I need to discover what has been dampening my powers as of late."
    
    r  "You think you'll find it in there?"
    
    k  "It appears rather doubtful, at the moment. The person who wrote this book was less of a true doctor, and more of a nurse."  
    k "Symptoms are poorly described, and treatments are often glossed over entirely in favor of drawings."
    
    k  "Most of the research available belongs to me."  
    k "I believe whatever is blocking me is directly affecting my brain chemistry."  
    k "No, that much is certain, my physical health hasn't changed."
    
    r  "Huh. I’m sure you’ll figure it out eventually."
    "Might put him in a better mood."        
    k  "Well, of course I will.  I am not going to be outsmarted by some silly little man and whatever stupid tricks he is using."
    
    "He goes back to reading, mumbling something to himself and furiously flipping through the pages.  Looks like he already forgot I was here."
    
    r  "What did you want to talk to me about?"
    
    k  "Ahh, yes."
    k "Miss Susa has been asking me to pass on my medical knowledge to someone worthy and capable of learning it well."
    k "Your memory for detail is quite amazing...and I'd like you to be my apprentice. In case anything should happen."
    k "So, congratulations. You can start tomorrow."
        
    r  "M-me?"
    k "...yes, you. Is that a problem?"
    r "I'm just not good with any of this learning stuff! You'd be wasting your time on me."
    k "I don't know. It seems your mock exam grades came up rather toward the high end..."
    r "T-that---how did you even get that?"
    
    k "I have my ways."
    k "You won't stop training with Soume. You'll just also come here for lessons. You have a concentration problem, correct?"
    
    r "........"
    r "Sort of. I can't sit still for that long unless I'm in the mood."
    k "Well, we can work on that too. This is supposed to be training to help you live in the human world, right?"
    r ".......can you really help?"
    k "I'll try."
    
    r "......."
    "I guess he's not as horrible as I thought."
    
    k  "You will start off assisting in my research.  I need to teach you proper technique, along with the essentials of scientific inquiry."  
    k "We’ll start slow though, so I’ll show you some of the more common methods I utilize, I think."
    
    r "I don't know..."
    k "Riku. You're very smart, considering the average IQ of most Majin."  
    k "You also handle directions fairly well, and your desire to prove yourself can be useful if you actually try to apply yourself."
    "........."
    "Was that a compliment?"    
    k  "You also did a fairly decent job plating those colonies I asked you to last time.  I figure it couldn’t hurt to make you my assistant in an official capacity."
    
    k  "Besides, Miss Susa has been so eager for me to find an assistant for so long."  
    k "What do you say?"
    
menu: 
        "Take the job.":
                jump kaz16b
        "Refuse.":
                jump somemainscene

label kaz16b:        
    r  "Okay, I'll do it.  When do you want me to be here tomorrow?"
    
    k  "Hrm, that is a good question."
    k "Considering your training, plan to come to my lab after your lunch time.  We can go over some of my research then."  
    
    r  "Sounds good.  One last question though; why is Miss Susa so desperate to find you an assistant?"
    
    k  "Ah.  Well, I would rather not go over that at the moment.  I’m quite busy, you see.  We can talk tomorrow."  
    k "Now, if you would please excuse me.  I’m having a hard time concentrating with you badgering me every couple of seconds."
    #play sound shut
    #play sound locked
    
    r "......"
    r "I do not get this guy..."
    
label kaz16c:
    m "Mmmm. I'm bored...and I haven't been in the city for some time."
    db "Sir, please remember you have an appointment with the head in three hours."
    m "Well that leaves plenty of time for fun, doesn't it?"    
    db "Yes, but sir..."
    m "Oh, come off it. I'll only be gone a little bit."
    db "Sir please--"
    db "...."
    db "He's already gone...I'm in so much trouble if he doesn't get back on time..."
    
    m "Alright...for the best time...who should I play with..."
	
menu:
    "A woman.":
        jump chickflirt
    "A man.":
        jump dudeflirt
label chickflirt:
    m "Definitely a girl."
    m "And there's one now..."
    m "Hiya~"
    sg "Oh--oh. Hello there. Um. Wow."
    m "I'm a little bit new to the area and I haven't eaten in hours...would you mind showing me a good place?"
    sg "...I was supposed to meet someone..."
    m "It will only take a few moments, you look like you know this area so very well..."
    sg "Heheh, I guess. Since you specifically asked me, I could take you to a nice little shop..."

    m "Ahh, this place looks wonderful~"

    "Two hours later..."
    sg "Oh Mamoru, you're so funny! I don't think I've ever met a man quite as alluring as you..."
    m "Well, I try to keep up..."
    sg "So you're in Japan to for work...what kind do you do?"
    m "Ohhh, this and that, management. Talking about work on the first date isn't any fun, is it?
    sg "You're right...how rude of me."
    m "Not at all. I see you have a keen eye for good taste...perhaps you would like to accompany me to a show tonight."
    sg "A show? What kind?"
    m "A musical affair. I've got tickets, but I was dumped..."
    sg "That's so terrible! Whoever did that must not have known what they had..."

    #play sound RING RING RING
    sg "Oh, that's me...ahaha, it's just the friend from earlier. I'll text her back later."
    sg "Shall we?"
    m "...let's."

    sg "This doesn't look like the right place."
    m "It doesn't, does it?"
    sg "W-why are we back here?
    m "Well, I couldn't very well let the whole world see."
    sg "...s-see? Don't touch me, if you do, I'll scream."
    m "That would be unfortunate, when you could just fight me."
    sg "...how did you know about me?"
    m "That's easy. My food always has a certain smell..."
    #play sounds medley of dark crunchy munchy sounding shit and a scream.

    jump doneeating

label dudeflirt:
      "Mamoru flirts with the dude and then eats him yay!"
      jump doneeating

label doneeating:
    db "Where have you been! You're nearly late, I almost had a heart att--!!!"
    m "I really hate when people lecture me like they're my parent. Shut up."
    db "U--urrrggh."
    "...."
    Voice "The smell of Majin blood. You've arrived finally, Mamoru."
    Voice "Clean yourself and come in. And call a maid for that mess outside."
    m "Hn."
    m "You're the same as always...Father." 
    
label dec15:      
    $ decision = "15"
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
    
label kaz17:      
    "The next morning, I'm in the lab, smelling like decaying...something."
        
    k  "Riku, please, focus.  I cannot trust you to handle my projects if you can’t even pay attention for a couple of minutes."
    
    r  "I’m paying attention."
    "I'm trying to, anyway."
    r "Aaaaaaaaaaaaaachooo!"
    k "What are you doing?! You're getting mucus into my bacteria!"
    r "I am not!"
    k "My precious bacteria..."
    
    k "Just pay attention!"
    r "What's the point of this today, anyway?"
    k "We're trying to find a mix of bacteria that results in a certain biological outcome."
    r "...what?"
    k "If I sneeze, you'll know you have it right! Just do it!"
    
label cell3:    
    $result = minigame("cell", 3, 1000)
    if result == True: 
            jump cellfail3
    else: 
            jump cellsuc3

label cellfail3:
    k "Murderer, murderer, murderer!!!"
    r "They're just CELLS!"
    k "Do it over!"
    jump cell3	

label cellsuc3:
    k "Achoo!"
    k "ACHOO! ACHOO! ACHOO!"
    r "Looks like sneezing to me!"    
    k  "ACHOO--ngh. Hmm...not exactly right but very close."
    
    r  "No way, I did pretty well on it!"
    
    k  "I said you were close, child, are you paying attention?"
    r "..........."    
    k  "Anyway, this shall be enough for one day.  Which compounds did you use for the last mixture?"
    
    r  "Uh...these three, I think."
    
    k  "You think?!"  
    k "Riku, where are your notes on the experiment?  How can you expect to be a real scientist if you aren’t documenting each of your steps?  How can I possibly reproduce your results?"
    
    r  "Err...sorry.  I didn’t know I needed to do that."
    
    k  "I thought you would have had enough sense to deduce that on your own!  My, you certainly have a lot to learn."
    r "I toldja, I'm not GOOD at this--"        
    k  "Hmph.  Excuses.  Nevermind, you are dismissed. I have a lot of work to do."
    
    r  "........."
    r "Fine. Same time tomorrow?"
    k  "Yes, certainly.  Oh, and Riku?"
    
    r  "Huh?"
    
    k  "You performed quite adequately today.  However, try to do better than adequate next time."
    
    r  "......."
    r "Will do."
    #play sound door open and close.
    
    #play sound phone ringing-
    
    k  "Riku, please get that.  The noise is annoying me."
    
    #play sound phone ringing-
    k "Right. I dismissed him. Argh."

    #play sound phone ringing
    
    k  "This is nothing but a distraction."
    
    k  "Hello.  This is Doctor Osamu speaking.  Who is calling?"
    
    l  "Doctor?"
    
    k  "Ah! Liza, one moment..."
    
    l "This will only take a moment, Doctor..."    
    l  "I’m afraid I won't be able to help you for the forseeable future..."
    
    k "W-what? But why?"
    k  "I simply must impress upon you how urgent the matter is."
    
    l "I understand that, and I am treating this with the appropriate amount of urgency."
    l "However, something more pressing has arriven that must be dealt with."
    
    k  "More important than the safety of the shrine?!"
    
    l "Doctor, like I made clear last time, there is only so much I can do until you provide me with more legitimate evidence."  
    l "Until then I will work to find out what I can.  I promise you that if I hear something, you will be the first to know."
    
    k  "F---fine. Please hurry and finish with your business."
    
    l  "I will do my best. I do apologize for the inconvenience."
    k "Hmph. Good day."
    
    #play sound Dial-tone, slamming noise-
    
    k  "DAMNIT!"
    
label kaz19:
    k "Fine. FINE. I don't need anyone. If she won't help me, I'll do it myself."
    k "I don't need them. I don't need anyone..."
    cl "Frreeejndndgth."
    k "Yes yes. Hello. I don't have time for idle chat today...do you have this book on hand?"
    cl "Shhdleme in the back."
    k "Much obliged."
    k "I can research this alone. I am the greatest, the ONLY Majin doctor with my knowledge, my credentials. This is simple!"
    db "Hello doctor. It's been a while."
    k "AAAAAGH! No...no I can't...I should've sensed you--"
    db "Shhh. No need to worry. I'm only here to talk."
    k "T-there's nothing to discuss."
    db "Let's not play games."
    db "This will be our last offer to you. Rejoin us."
    db "If you do our work, we will allow you unlimited funding for your own."
    db "All the equipment you could possibly desire...and of course, a state of the art laboratory."
    k "...state of the art...?"
    db "Nothing less."
    db "The request comes straight down from our leader."
    k "....."
    db "Your answer?"
    k "I...refuse. I will never, ever join you again. Not after--"
    db "Mm. My master said you may need more persuading than that. I will report this to him...we'll be seeing you soon, Doctor Osamu."
    k "......"
    k "He's gone..."
    k "Oh god..."
    k "Why didn't he kill me...? I-I HAVE to figure out what's wrong."
    $inventory.unlock_item("book6")
    
label kaz20:
    su  "Yes."
    su "No, I agree, Liza. I have a couple of things left I need to do, but I am almost ready. I will contact you when I am leaving."
    su  "Sounds good. Yes. Bye."
    
    #play sound knocking-
    
    su  "Eh? Whoever is there needs to learn how to make a fucking appointment."
    
    k  "Forgive my intrusion, Miss Susa, but we must talk."
    
    su  "Oh, Doctor Osamu.  You know I didn’t really invite you in, right?"
    
    k  "Yes, and I do apologize for the intrusion, but I--I was just--"
    
    k  "Ahem.  Miss Susa?  Perhaps you could stop rummaging around your file cabinet and listen to what I am about to say?"
    
    su  "Just a sec. I need to find something... I tell you, once of these days I’m actually going to fucking organize this thing.  Never can find what I am looking for when I need it."
    
    k  "Perhaps you can look for whatever you need in a couple of moments?"  
    
    su  "No need. I can guess what you’re going to say anyway."
    
    k  "Oh really?  And what would that be?"
    
    su  "Soume blah blah blah ambush his fault blah blah your sensory abilities blah.  Something along those lines?"
    
    k  "Miss Susa, I...I was attacked in the bookstore! 
    "She stares me up and down."
    su "Well, you look very good for someone who's been attacked."
    k "Well, it wasn't an attack, exactly...I was approached by the Church. They want me to return to work for them."
    
    k  "I believe the safety of this entire shrine is at risk."
    
    su  "Fuck, Osamu. I don't have time for this. Did you bring it up with Soume?"

    k "Miss Susa! I believe that Soume is the one leading everyone here!"
    
    k  "I beg of you, do not take my warnings lightly!  I am sure it is him!  I am positive he is behind all of this!  I am in very grave danger!"
    
    su  "OSAMU!  Relax.  Now.  Calm yourself and sit down."
    
    k  "But--"
    
    su  "No.  Sit your ass down now."  
    
    k  "...yes, Miss Susa."
    
    su  "You have been becoming increasingly paranoid these past couple of years. It isn’t healthy. For you, for Soume, fuck for me because I have to listen to this shit every other month."
    
    k  "This isn’t paranoia!  This-"
    
    su  "Osamu, since Soume arrived, you've beelined on him as a spy."
    
    k  "Er...well...yes, but now I am absolutely sure..."
    
    su  "Shut it! You are by far the most brilliant mind here, but you convince yourself of these crazy conspiracy theories!"  
    
    k  "C-crazy?"
    
    su "PSYCHO."
    su "Look."
    su "I already know what you did to Soume, under the Church's order."
    su "I understand you aren't comfortable with his presence here, but he deserves a chance just as well as you do."
    
    k  "What I did? This has n-nothing to do with--I-I haven’t even thought about that in years."
    
    su "Sell that line to someone who'll buy it."
    su  "You don't like him. You've never liked him because you were afraid."
    su "You've accused him several times already. But not once have you been able to prove a thing."
    
    k "Well maybe you protect him because you feel bad for what you and yours did to him!"
    su "............."
    k  "Don’t think I forgot what you used to be, before you opened up this rescue out of the goodness of your heart!"
    
    su  "............."
    
    k  "Perhaps...perhaps your failing to believe me is a case of overcompensation, yes?"
    k "Indeed! Maybe it is your own bias!"
    
    su "........."
    su "This conversation is over."
    su "Get the fuck out of my room."
    k "Wait...I didn't mean--"
    su "GET THE FUCK OUT!"
    k "................."

    "............"
    "Roman, Soume and I are playing cards in the main room."
    "Free evenings are pretty nice, we can just relax and chat."
    "~*~ GET THE FUCK OUT ~*~"
    r "Whoa."
    ro "...I wonder what's gotten Miss Susa so mad..."
    s "She's been a bit on edge lately..."
    ro "Do you know why?"
    s "Oh, no. I don't know things like that."
    r "Maybe someone didn't iron the linens right. Hehehe."
    ro "No...that's...more than usual."
    s "Much more."
    r "......"
    r "Come to think of it, she's been pretty nice to me, lately."
    ro "Oh?"
    r "Even let me check out her video game."
    r "It's pretty nice. I'll probably check it out again if she lets me."
    ro "That is...exceptionally nice of her."
    s "Well, I'm sure it will work out."
    r "Yeah, I think so too!"
    "............"

    $kbc = False
    $ decision = "16"
menu:
    "Search.":
        call show_map
    "Sleep.":
        call sleep
    "Store.":
        call shop_loop
    "Research.":
        call label kaz22
        $kbc = True
        $journal.unlock_entry("something", "031")

#############################################################
Kaz22 need massive fixing.
#############################################################    
label kaz22:
    k  "No!  Ngh...another dead end!"
    
    k  "Unless...perhaps I misread the results.  That has to be it."  
    
    k  "Let me see…if I just recalibrate the instruments…hmm…and then…"
    
    k  "Ngh!  Again!  NO!  How can this be just bamboo charcoal?"
    
    k  "What of the other substances Riku added?  Surely…I must be running this wrong?"
    
    k  "Bamboo charcoal?  This can’t interfere with my sensory abilities.  I use all the time…I purify my water supply with it."
    
    k  "It was there as a control!  Something I knew wouldn’t impede my abilities!"
    
    k  "AUGH!  He must have screwed something up at some point!  This is the only explanation!"
    
    k  "I knew it!  I knew he would just interfere with my experiments!  I should have just told Susa as much.  This child with his plebian mind probably wasn’t even paying attention to what he was doing."
    
    k  "How could I have let this happen!  This has set me back weeks!"  
    
    k  "No…no, it isn’t my fault.  This is his fault.  Soume’s.  He’s behind this somehow.  He must have put Riku up to it!"
    
    k  "But…but something did impede my abilities.  I could barely tell the ball was coming at me when Riku threw it.  Something here must have done it."
    
    k  "But what?  I’ve tried mixing these compounds together again.  Whatever it is can’t be synthetic!  I would have found it!"
    
    k  "Riku  managed to find it though.  But…how?  How could he find it yet I fail to?  He can barely rub two sticks together, the clod."
    
    k  "Think…think…I can figure this out.  There has to be an explanation for this.  Just stay calm.  Concentrate."
    
    k  "Ngh."
    
    k  "No…concentrate.  What is causing this?  I must find out.  And soon.  I don’t have time to begin again.  I have enough data already in front of me.  I just know it…"
    
    k  "Ngh.  Eh."
    
    k  "Heh heh."
    
    k  "HAHAHAHAHAHAHAHAHAHAHAHAHA!"
    
    k  "FUCK!  FUCK FUCK FUUUUUUUUUUUUUCK!"
    
    #play sound  Glass breaking-
    
    k  "WHY CAN’T I FIGURE THIS OUT!"
    
    #play sound Thuds, crashes, general mayhem-
    
    k  "I AM NOT GOING TO BE OUTSMARTED BY SOME"
    
    #play sound Shattering-
    
    k "STUPID"
    
    #play sound Loud fall-
    
    k  "GUTLESS"
    
    #play sound Metal bending-
    
    k  "MAJIN!"
    
    #play sound Crunching or splatting-
    
    k  "Ngh."
    
    k  "Riku’s plant."
    
    k  "The gift he gave me…"
    
    k  "No.  No, it will be alright."
    
    k  "Come on plant…stand up straight…"
    
    k  "Dead.  Dead like me.  Dead like I will be."
    
    k  "I can’t even save a plant.  What chance do I have."
    
    #play sound Thud-
    
    k  "Ouch.  Stupid book."
    
    k  "Eh…let me just sit down.  Sit for just a second.  I’ll figure it out."
    
    k  "I’ll…figure…"
    
    #Dr. Osamu sobs.
    
    k "I…guess I am…just another…stupid animal."
    
    r  "Uh…you in there Doc?"  
    
    "There're no sounds."
    
    #play sound Knocking
    
    r  "Doc?  C’mon, say something if you’re in there."
    
    k  "…Riku?"
    
    r  "Yeah, it’s me.  Mind if I come in."
    
    k  "I…ahem…perhaps another time.  I am…busy at the moment."
    
    r  "Nah, I’m gonna come in.  I heard some weird noises and…"
    
    "I look around the lab once I open the door, and then entire room looks like a bull just ran through the place."  
    "There is broken equipment everywhere and I need to watch where I’m walking because there are shards of glass everywhere."
    
    "The weirdest sight, however, is the doctor himself.  He is in the corner of the room, curled on the floor with his arms around his legs.  His eyes are all swollen and it looks like he’s been crying."
    
    r  "Holy hell…you alright Doc?"
    
    "He looks up and smiles at me feebly."
    
    k  "I broke your plant."
    
    r  "Huh?"
    
    k  "The plant you gave me. I destroyed it. This is an APOLOGY!"
    
    r  "Oh…uh, no worries, Doc.  I’ll get you a new one."
    
    k  "…you can call me Kazutaka.  Or Kazu, if you wish."
    
    r  "Huh?  What the hell is going on in here?"
    
    k  "I can’t figure it out.  I don’t know what is happening to me.  I-I can’t explain it.  I’m an idiot."
    
    r  "Look, I know you’re stressing out about this, but you’re not an idiot.  You’re the smartest guy here!  Aren't you like the only Majin doctor?"
    
    k  "That’s just a title Susa gave me.  It means nothing.  There isn’t a formal university or anything like that for me to attend.  There aren’t any other because no one else want to be one."
    
    r  "Er…that’s not it.  There are no others because none of us are capable of doing it.  I still don’t know how you do."
    
    k  "Hmph.  Well, I can’t.  This is the most urgent problem I’ve ever addressed, and I still don’t have any leads."
    
    r  "What about that, uh, thing we found the other day?  That I mixed.  That was something…wasn’t it?"
    
    k  "False positive.  It was just some bamboo charcoal.  We’re at a dead end.  I’m at a dead end.  They’ll find me.  And I’ll just be another body."
    
    r  "Is that what this is all about?  Jeez, Doc, you’re gonna be fine."  
    
    k  "Well, you’re just like the others.  You don’t believe me."
    
    r  "No, I...I believe you."
    
    "I don’t really.  But I have to tell him something.  He looks too sad for me to throw salt on the wound."
    
    k  "You do?"
    
    r  "Yeah...and even if they do get you, you won’t just be another body.  All the work you’ve done will live on.  It isn’t like that’s just gonna disappear, y’know?"
    
    k  "...that is true.  My journals will outlive me.  My work..."
    
    "He suddenly looks at me urgently.  His eyes widen."
    
    k  "Promise me...promise me, you’ll continue it."
    
    r  "Huh?  What do you mean?"
    
    k  "If I die...if they get me...promise me you’ll continue what I’ve started.  I cannot be the last Majin doctor.  There must be others, or our kind is doomed."  
    
    r  "Sure, whatever you want. Yeah.  I will."
    
    "Kazu rest his head against the wall and smiles.  He looks relieved."
    
    r  "But we don’t have to worry about that.  Cuz you and I are gonna figure this out."
    
    k  "So...you’ll help me?  Help me show the others it is Soume?  You’ll help me with the investigation?"
    
    r  "Ah...yeeeah.  Yes.  Course I will, Doc."
    
    "I know it isn’t Soume.  It probably is Mamoru, if I had to guess.  But if I can help him figure out how, then I’m guessing we’ll be able to find out who, and eliminate Soume from his list of suspects."
    
    k  "Ahem.  Yes.  Thank you…thank you so much, Riku.  I knew I could trust you."
    
    r  "So, are we gonna start or-"
    
    k  "Oh, certainly not.  Do you see the state that my lab is in?  I got a bit emotional.  You’ll forgive me for my outburst, I hope."
    
    r  "Yeah.  Of course.  No problem."
    
    k  "And I would prefer it if you don’t mention this to others.  I have a reputation to uphold, you see.  I can’t let it get out that I was in hysterics."  
    
    r  "Nah, I don’t know what you’re talking about.  I didn’t even come to your lab today, so I wouldn’t know what condition it was in if I was asked."
    
    k  "...thank you, Riku.  I’ll have this cleaned up by tomorrow.  We can start our research again then.  Please arrive here by noon.  I will not tolerate lateness, as I’m afraid we have limited time."
    
    r  "Sure thing, Doc."
####################################################################################    
    
label kaz24:
    s  "Riku, please, focus.  I understand that channeling this much youki at once must be difficult, especially for one as young as you.  You can do it though~!  Just concentrate."
    
    r  "Ngh…ah!"
    
    #play sound flashing
    
    r  "Hmm…that was close.  Almost was able to get it that time."
    
    #Soume giggles.
    
    s  "That was indeed closer.  But we need to train you to the point that you can release your power when you want to, and not as a reaction.  It can be dangerous otherwise."
    
    "Soume has had me attempting to repeat what I did a couple weeks ago now since I healed up from the ambush.  I still dunno how I was able to do it, because I haven’t been able to do it again."
    
    "He seems confident that with enough training, I’ll be able to burst like that whenever I want.  That I’ll be able to control it.  I’m not so sure."
    
    s  "Here, we will try again.  This time, make sure-"
######################################################################

    "The next morning is weird, even for this place."
    "Susa woke everyone up at 3am...for some conference, or something."
    
    su "For the next few days, I'll be out on a private mission."
    sg "A private mission..."
    sb "That's really weird..."
    sg "Has she done this before?"
    sb "Not that I remember..."

    su "Quiet!"
    su "Nothing changes while I'm away."
    su "If I see this place dirty when I get back, each and every one of you is going to regret it!"
    su "Keep to your training!"
    su "Soume will make sure things run smoothly until I return!"
    "Soume's flushing, I can tell."
    su "I have to leave now, but Soume will spend the next hour explaining all the details, got it?"
    ev "Understood!"
    
    ".................."

    na "Sir, we can be ready to leave at any time."
    m "Then make sure your team is prepared."
    na "If you please, sir...I...wanted to apologize."
    na "For my behavior before. It was presumptuous of me."
    m "....."
    m "I believe I gave you a direct order."
    na "........"
    na "Yes sir. Forgive my intrusion."

    "..............."

    su  "Here is the key to my office, and the main key. And keep an eye on Kazutaka, will you?"
    
    s  "Miss Susa?"
    
    su  "Supposedly he was ambushed at the bookstore...send the sprogs to figure out what happened and make sure the clerk is okay."
    
    "Soume plays with the key nervously in his hands."
    
    s  "Are you sure you have to leave now? Perhaps you can do this at another time."
    
    su  "You'll be fine. You've been here the longest, you know all the ins and outs." 
    su "I need to take care of this. I trust you to handle everything over here when I’m gone. The brats shouldn’t give you too much trouble."
    
    s  "Is it...about your son?"
    
    su "........"
    su "Forgot that amazing memory of yours."
    s "Forgive me, if that was rude to ask..."
    su "Take care of business for me, and we'll call it even, okay?"
    s "I...I hope you find him, Miss Susa."
    su "........"
    su "Me too."
    "..................."
       
label kaz25:
    r "Well at least this is just an escort...checking mission or something."
    ro "A mission with just us two? It seems like Miss Susa isn't thinking clearly..."
    k  "Ahem."
    ro "Er I mean--it's just...Soume usually..."
    
    k "It's fine."
    r "What happened last time?"
    k "It...was a demon hunter. He approached me. Asked me to switch sides."
    ro "To switch sides...?"
    k "Ahm. What I do is very important to them. Let's leave it there."
    r "And then he just let you go?"
    ro "...seems like they're waiting to try to get you some other time..."
    k "...yes. I...imagine so."
    r "Are you okay to be...out...now?"
    k "There is something else I need to pick up at the store."
    
    "Susa has already been gone three days.  With Soume working to keep the shrine running, Roman, me, and a couple of other better trainees have had our hands full conducting all of the training."  
    
    "It would be kinda fun at times, if I didn’t only have to deal with the youngest kids."
    
    "...I probably need to remember to thank Soume again for dealing with me next time I see him."

    "Hard to believe I've been here nearly a year already. It's just flown by..."

#################################################################################
#This part beneath here needs to be rewritten/redrafted.

#Start from Kazu Arc 40 on the Susa.Kazu page.
#################################################################################    
    
    "I have to admit, when he’s at full strength like that, he’s pretty damn impressive."
    
    k  "Thank you.  I will just wait outside then when you complete your transaction."
    
    r  "That’s probably for the best.  I doubt you could even talk to the old woman behind the counter anyway."
    
    k  "Eh?  And why would you say that?"
    
    r  "She speaks entirely in the old language.  Can’t understand a fuckin’ word she says.  It is nothing but gibberish."
    
    #Roman chuckles.
    
    ro "Ah yes, I completely forgot about that."
    
    r  "Huh?  Whuzzat?"
    
    k  "Entirely in the old language?  That doesn’t make any sense, Riku.  No one only speaks in the old language any more."
    
    r  "But…but she did!"
    
    k  "Highly unlikely.  Our kind has been here for upwards of two thousand years.  There aren’t any Majin settlements or anything like that."  
    k "We all have learned other languages in order to assimilate.  How else could she complete her order forms if she only spoke in ancient Majin."
    
    r  "But…but…"
    
    #Roman chuckles.
    
    ro  "I am really sorry Riku!  It was her idea!  She does it to all of the new customers!"
    
    k  "Apparently, only on the ones gullible enough to fall for it."
    
    ro  "I thought you would have figured it out once she got your Duck Hunt gun for you!  How else would she know what it was?"
    
    r  "Aw, you gotta be kiddin’ me!  You were in on this Roman?"
    
    ro  "Like I said, not really!  I just…let you believe what you wanted to believe."
    
    r  "I’m pretty sure you told me she didn’t speak English!"
    
    ro  "Did I?  Well…perhaps I enhanced the truth, slightly.  Can you forgive me this one time?"
    
    r  "Hmph.  Fine.  I’ll give her a piece of my fucking mind though, I’ll tell ya-"
    
    k  "WAIT!"
    
    r  "Eh?"
    
    ro  "What is the matter?"
    
    k  "Something…something isn’t right up ahead.  In that old house."
    
    ro  "That’s where the store is.  It is just the work of the old shopkeeper though, so there isn’t anything-"
    
    k  "No, not that isn’t it.  There is something dangerous up ahead.  I…I think something might have happened in there."
    
    ro  "What?  Doctor, are you sure?"
    
    k  "Yes…yes, I can feel it.  There is something wrong about that place…we should turn back now.  We need to run."
    
    ro  "No.  No, we need to see what is wrong.  Doctor, you hide here.  Riku, come with me."
    
    r  "Gotcha."
    
    k  "I’m telling you, we need to retreat.  There is something powerful around here….something dangerous."
    
    ro  "We will be quick.  If there is something ahead, we need to find it.  We can’t let something dangerous near the rescue."  
    ro "We are less than half a mile away from this point…someone might stumble upon the entrance.  Especially if they were wise enough to see through the shopkeepers illusion."
    
    k  "Ngh…be careful.  And return quickly."
    
label kaz26:
    ro  "Riku, be careful."
    
    "I nod at him.  The entrance room to the shop looks old, and destroyed.  Pieces of debris laying everywhere.  Everything is covered in dust, and it looks like no one has lived here for twenty years."
    
    "So, completely normal, I guess.  At least, it looks like it did the last time I was here."
    
    #Roman whispers.
    
    ro  "Riku!"
    
    "I look over, and I see to Roman pointing towards something on the floor.  At first, I don’t notice anything peculiar, but after my eyes adjust a bit more to the dim light, I figure out what he’s trying to show me."
    
    "Footprints.  A couple of pairs of them.  They lead down towards the entrance of the shop."
    
    #Riku whispers.
    
    r  "Fuck."
    
    #Roman whispers.
    
    ro  "Quietly now.  Head down to the shop."
    
    "Again, I nod.  I lead the way down the hallway towards the entryway of the shop, and it is here that I can definitely tell something is wrong."  
    "There are usually items adorning the walls.  Old masks and other antiques of the Majin culture.  Some really cool things that I always liked to look at."
    
    "But there is nothing left on the way.  Most of the items are thrown on the floor, and broken into several pieces."  
    "The ones that aren’t have blood smeared across them.  Further into the shop, it is even worse."
    
    "Entire aisles are knocked over and large pools of blood are spread out on the floor.  And something smells…rotten.  I don’t know what it is, but it is making my stomach turn."
    
    ro  "Hello?"
    
    "He must have noticed what I did.  The room looks empty.  I don’t see anyone in it.  Nobody dangerous, but the shopkeeper doesn’t appear to be around either."
    
    "I go to check one of the few aisles still standing, when I hear Roman scream."
    
    ro  "OH MY-Who would do this!?"
    
    "He is peering behind the counter.  I run over to go see what he is talking about."
    
    ro  "No, Riku!  Stay back!"
    
    "But it is too late.  I see her.  What is left of her, anyway.  The old shopkeeper is in a  heap behind the register."  
    "Her head rests firmly against the wall, but only because her neck and face were one of the few areas that remained untouched."  
    "Entire chunks of flesh have been torn out of her midsection.  There look to be bite marks on her shoulders, and both of her arms have been torn out of the sockets and are no where to be seen."
    
    "I turn around quickly and vomit everything I ate this morning onto the floor.  Roman doesn’t look much better, but at least he is keeping everything down."
    
    r  "What…ngh…what did this to her?"
    
    ro  "I…I can’t say for sure."
    
    r  "But you have a guess?"
    
    "I look back at the shopkeeper.  I don’t want to, but I can’t help myself. I can tell from the look on her face that they started doing this to her when she was still alive."  
    "The look of pain on her face is the strongest I’ve ever seen."
    
    dg  "Oi, look wot we got here.  A couple o’ stragglers."
    
    "I turn around, and two demon hunters are now blocking the door to the exit.  They each have broad grins on their faces, and the one that just spoke is licking his lips."
    
    db "My, my, my.  Boss will certainly be happy about this."
    
    ro  "I-I warn you…stay back.  Do not come any closer."
    
    dg "Who says boss got to know about these little buggers.  They’re both so small.  Jus’ table scraps, really."
    
    db "Ahhhhh…I like where your head is at today.  Yes, he has already gone on ahead.  I think we can indulge…just this once."
    
    "Sure fucking wish Soume was with us right now.  Roman is shaking, and I don’t feel much better.  Especially if these are the two that did whatever they did to the shopkeeper."
    
    r  "Look, just move the fuck out the way, and we won’t be forced to hurt you."
    
    "It is the bravest threat I could muster.  I want to just run, but I don’t have anywhere to go.  The only way out is through these two."
    
    dg "Haw haw haw!  Ya hear dat one?  I call dibs on ‘im.  I like ‘em feisty."
    
    db"I won’t fight you for him.  More meat on the other one anyway."
    
    ro  "Riku!  Prepare yourself!"
    
    #Insert battle here.  Riku and Roman fight two Demon Hunters-
    
    ro  "Ngh….Riku, are you alright."
    
    r  "Yeah…yeah, I’m fine."
    
    "All that training with Soume sure as hell paid off.  Don’t think I would have been able to take both of them without Roman though."
    
    r  "Glad you came with me.  Fuck."
    
    ro  "Yeah, I would hate to-"
    
    ro  "Riku!  Doctor Kazutaka!"
    
    r  "Oh, fuck.  Hurry!"
    
    "We both run off through the doors and head back to where we left Kazu.  Hopefully, he’s still there."
    
label kaz27:
    k  "Hmph.  What is taking them so long?"  
    
    k  "They better be alright.  I told them there was danger ahead."
    
    k  "Ngh.  No.  No!  Not here!  Not now!"
    
    na  "Why hello there, Doctor.  Fancy meeting you in this part of the woods."
    
    k  "You!  What are you doing here?"
    
    na  "Is that any way to treat a lady?  Fuck, I just came out here to talk to you.  I’m not gonna hurt you.  Yet, at least."
    
    k  "Stay…stay back!   I’ve got friends with me."
    
    na  "Nyeh heh heh!  You’ve got friends.  Holy shit, you have gone fucking mad.  No offense, but you kina suck to be around."
    
    k  "Help!  Help!  Riku!  Roman!"
    
    na  "Yeah…they’re probably already dead.  A couple of my men were hanging around the outside hoping someone would stumble in.  Just you and me, darlin’."
    
    k  "Ngh.  Don’t…don’t kill me."
    
    na  "Kill you?  Nyeh heh heh!  Silly man.  You are much more use to us alive."
    
    k  "I don’t…I’m afraid I don’t understand."  
    
    na  "We want you back.  We’re even willing to look past all of your past little mistakes.  A clean slate!  We’ll even forgive your betrayal, and the fact you ran away like a fucking coward."
    
    k  "No…no…"
    
    na  "C’mon.  You can’t ask for much more!  The boss man even said I can’t hurt ya, as long as you come with us."
    
    k  "No!  I won’t go back!  I refuse!  YOU CAN’T MAKE ME DO IT AGAIN!"
    
    na  "Oh, please, stop being so fucking overdramatic.  We never did anything to ya."
    
    k  "But…but what you made me do…to others…"
    
    na  "Well, yeah, but fuck that sort of comes with the job, doesn’t it?  Listen, just come with me and nobody is going to get hurt.  Well, besides the one’s we’ll have you hurtin’, that is."
    
    k  "N-No…"
    
    na  "Last chance, Doctor K.  Boss said if I couldn’t get you to come with me, to make sure you were disposed of."  
    na "Honestly, I’d prefer it better if I could just rip the meat from your bones, but I gotta at least tell the boss I tried."
    
    k  "I…but…please…"
    
    na  "Not making much fucking sense here.  Shit, I didn’t think it would take this long.  Look, either start making sense or stick your fucking neck out.  It’ll be easier for me that way."
    
    k  "…just kill me.  I won’t go back."
    
    na  "Well, at least you can die with your convictions.  That means you stand for somethin’, right."
    
    na  "I mean, it also makes you a giant fucking idiot, but at least you’re an idiot that stands for something."
    
    k  "Ngh…"
    
label kaz27a:    
    
    ro  "Stop right there!"
    
    na  "Ah fuck. The damn cavalry showed up."  
    
    r  "You alright, Doctor Osamu?"
    
    k  "Barely!"
    k "Next time if you could come a little bit quicker, my heart would certainly appreciate it."
    
    r  "Just for that, I'm gonna make sure you lose at least one body part before we come save you next time."
    
    na  "Oh, is it just the two of you? I was all worried for nothing."
    
    na  "Look, here’s what I’m gonna do, Osamu."  
    na "I’m going to kill these two."
    na "And then I am going to use their intestines to decorate the tree behind us."  
    na "If you change your mind, excellent. And if you don’t, well, I'll decorate two trees"
    
    ro  "Doctor, stand behind us.  We can take it from here."
    
    na  "Bold words, kid.  How about we see how well you can talk after I rip the tongue from your mouth."
    
    na  "HAAAAAAAAAAAA!"
    
#Battle scene here.  Riku and Roman (and Kazutaka?) must defeat Naomi in battle.  Failure to do so will result in a bad ending.  Success will continue the scene.-
    
    na  "Eh…urk.  This…this can’t--"
    
    #Riku huffs. Not as kinky as you'd think.
    
    r  "Not as tough as you look, huh?"  
        
    k  "What are you waiting for?  Finish her off now!  Before she pulls out some trickery!"
    
    r  "…"
    
    ro  "…"
    
    k  "HELLO! Kill her already!"
    
    ro  "...I--I can't make decisions like this..."
    ro "You do it, Riku."
    
    r "...WHAT?"
    
    "Naomi stares up at me.  She moves for her dagger, but she’s too weak to pick it up.  She tries to pull herself up against a rock, but fails at that as well."  
    
    r  "I…I can’t."
    
    k  "She would show you now mercy if the situation was reversed! Hurry! Kill her now!"
    
    na  "Ngh."
    
    r  "No.  No, I can’t.  You’re probably right."  
    r "She would kill me in an instant.  But I--I can’t just kill someone."  
    r "We…we will take her back with us.  Maybe we can get some information outta her."
    
    ro  "Good idea."
    
    k  "Are you two mad?  Here, give me your weapon; I shall finish the job myself."
    
    ro  "Doctor!  Please calm yourself.  We will discuss the matter with Soume and Miss Susa first.  After they decide what to do with her, we will carry out the orders.  But not before."
    
    na  "Heh."
    
    "I was caught up in what Roman was saying, but during that time Naomi has managed to prop herself up against that rock she was trying to use earlier.  And she is smiling at us.  It makes me uneasy."
    
    na  "Nyeh heh heh heh!"
    na  "You idiots. I'll never tell you anything."
    na "Not even the little piece of information you've been dyyyyyyyying to know."
    
    k "............"
    
    r  "Ignore her; she’s fucking nuts.  Someone restrain her and we can get her to talk back at the rescue."
    
    na  "Nyeh heh heh!"
    na "In your dreams, you bed-wetting infant."
    
    r "Ohhhh that's IT!"
    
    k  "You two, hold her down. I might have be able to make her talk."
    
    ro  "How?"
    
    k  "A truth serum. Highly experimental, but--"
    
    m  "Oh, Doctor Osamu, I thought you had given experimentation up?"
    
    "The air goes cold."
    "Why is he here?"
    "Of all people, when Soume isn't around, why is he HERE?"
    
    k  "............."
    
    m  "Testing possibly poisonous substances on poor helpless Majin…"
    m "How unethical."  
    m "And the reason we desired your special brand of expertise in the first place."
    
    ro  "Mamoru!"
    
    m  "Yes, yes, I am terribly sorry to break up this little party."
    m "I will be taking the good doctor with me, though.  Duty calls."
    
    k  "No!  Roman, Riku, follow me!"
    
    m  "Will you run?"
    m "I love it when they run."
    
    ro  "No! We can't just run--he's---"
    
    m  "You really have such an irritating mouth, Roman."
    m "The doctor and I have something of a business arrangement, one that he didn’t exactly fulfill his end of the bargain on."  
    m "I’m only seeking restitution for the service he denied me. Surely you won’t stop me from that?"
    
    k  "No…that was slavery!  I’m not going back!"
    
    m  "Your choice here isn’t to go or not go. It is to go in a single, living piece, or in several dead ones."
    m "It's simply how I've learned to operate with those who don't pay their due."
    
    na  "Ehehehehehe, I told you---HHHHHRK!"
    
    "Mamoru grabs Naomi by the neck with one single hand."
    
    m  "And you…you chattering little idiot."
    m "I gave you one task. One!  Get the doctor to come with you." 
    m "And could you do it?"
    
    #Naomi is choking.
    
    na  "I…was…"
    
    m  "No. You didn't, did you?" 
    m "I mean, the doctor is still over there."
    m "That much should be obvious even to your limited mental capacity."
    
    "Naomi’s face is starting to turn purple.  Her feet kick uselessly at the ground, but can’t quite make contact with it."
    
    m  "Instead, what ends up happening?"
    m "You came this close to revealing our master plan."
    m "I can't really just allow things like that to go on."
    m "You know?"
    
    na  "Ngh----one---more chance--"
    
    m  "Oh, Naomi. I would love to give you another chance."
    m "But we have a problem."
    m "Now, you are not only useless…you’ve become a liability."  
    m "And you know what happens to liabilities, don't you?"
    
    #Naomi is still choking.
    
    na  "--please---no---"
    m "That's right."
    
    "Electricity starts to crackle out of the ends of Mamoru’s fingers.  I begin to smell the scent of something burning, and before long, I notice that scent is coming from Naomi."  
    "She is trying to scream, but nothing is coming out.  Her face contorts in agony and her hands claw desperately and Mamoru’s fist."
    
    "And then...her head just melts away."
        
    k  "Ngh…"
    ro "........"
    r "........."
    
    m  "Right, now where were we?"
    
    ro  "I-I…"
    
    "The three of us just stare at Mamoru for a while.  He is smiling at us, like he just told us the punchline of a joke and was waiting for a response."
    
    m  "Oh, come now.  No need to be so tense."  
    m "I apologize for all that unpleasantness, it was just business."
    m  " I hope you three don’t let a little thing like a failed deal sour our good mood."
    
    "My mind is blank. We're all going to die."
    
    m  "Now where were we? Ah yes." 
    m "Doctor, I will need you to come with me."
    
    "He smiles at us.  Opens his mouth wide, and I can see what looks like dried blood on this teeth."
    
    ro  "N-No.  We won’t let you take him."
    
    m  "Hmmmmm? I'm sorry, I believe I am going a bit deaf in the one ear." 
    m "Could you repeat that one more time?"
    
    "Roman is shaking.  He doesn’t even look like he’s believing what he’s saying.  He eventually steadies himself again, and manages to make eye contact with Mamoru.  He draws up an ice sword."
    
    ro "You two, hurry up and get out of here."
    
    k "......."
    
    "Doctor Osamu runs. Coward."
    "But I don't want to die either."
    
    ro "Riku, GO!"
    
    "I start to run."
    "And for the first time in my life, I start to pray."
    
label kaz28b:    
    m "You realize that you're just delaying the inevitable."
    ro  "No, you can’t-----I won't let you---"
    
    "Before I can even draw up his sword, Mamoru closes in and breaks it with his bare hands, lifting me by his neck, just like he did Naomi."
    
    m "Yes, good."
    m  "I had secretly hoped you would put up some resistance."
    m "I wanted so badly to have an excuse to devour you whole."
    
    "This is it."
    "I'm done for."

    ro "...do...whatever you want."
    m "Oh, I don't need your permission for that."
    m "Won't you squirm? Won't you scream?"
    
    ro  "Go to hell."
    
    m "I've been. It was dull."
    
    ro "Nngh--"
    
    m "Any last words?"
    
    ro "................gck."
    
    "I somehow manage to call up an ice sword, but before I can hit him, he breaks my arm."
    
    ro "AGGHHHHHHHHHHHHHH."
    
    m "Ahhh, there we are, a good old fashioned scream of terror never hurt anyone, did it?"
    
    ro "..........."
    
    "He's broken my arm so badly that it hangs limply from my shoulder."
    
    m  "I'll say it again."
    m "Any last words?"
    
    ro "...tell...Soume...sorry..."
    
    m "............."
    m "Heh. I will relay that message with glee."
    
    "I'm already fading in an out." 
    "It won't be too much longer, now."
    
    "A sharp pressure at the base of my neck, and then blood all over my front."
    "He's going to devour me."
    
    "My life ends as food."
    
    "Out of nowhere, Soume dashes into the clearing."
    "I hardly recognize him...he's in the youko form."
    
    "Before I know it, I'm looking directly into his eyes."
    
    m  "You."
    s "I warned you."
    
    "A giant tree branch sprouts from the ground and impales Mamoru on the end of it."
    
    m "HRRKKKK---"
    
    "He goes flying through the air before connecting with a loud thud against a tree.  He scrambles to his feet."
    
    "Soume is still sprinting at him. The youko form moves so calmly, but even like this I can tell that Soume is extremely angry."

    "Is he angry because Mamoru hurt me?"
    "Isn't it too dangerous for me to think like this?"
    
    "For the first time, I see true panic flash across Mamoru's face."
    
    m "Can't we...discuss this?"
    s "Fight or die."
    m "...well then. I can't argue with that, can I, Soume?"
    
label kaz28d:    
    
    s   "Roman~!  Oh, please Roman be alright!"
    
    r  "Soume, he’s hurt badly.  I don’t…I don’t know if he’s going to make it."
    
    ro  "Urgh…glrgh…ffbt…"
    
    "He’s trying to tell us something, but all that comes out from his mouth are guttural sounds and bubbles of blood."  
    "I get a look at his face, and it looks as if he is missing at least half of his teeth.  I see some of them scattered across the grass."
    
    k  "Soume…how did you find us?"
    
    s  "I was on my way to the store…saw a group of demon hunters.  I-I got here as quick as I could.  Oh, Roman…please pull through."
    
    "Soume is spreading something over Roman.  Some sort of pollen.  The bleeding appears to stop, but the wounds themselves do not heal."
    
    s  "We have to get him back, now."
    
    r  "Here, let me help you."
    
    s  "No!  Riku, I am sorry, but you will only slow us down.  Doctor Kazutaka and yourself, get back to the shrine immediately."  
    s "Follow me as quickly as you can.  I don’t know if there are any more around us."
    
    "Soume picks up Roman and takes us.  I run after him, but he is going faster than I can match even carrying the extra person."  
    "I turn to say something to Kazu, but he isn’t with me.  He’s looking at something in the grass."
    
    r  "Kazu, come on, we don’t have time for you to be classifying new species!"
    
    k  "Hmm…"
    
    "He picks up some sort of electronic piece of equipment and turns it over in his hands.  He stuffs it into his pockets and runs to catch up with me."
    
    r  "What did you pick up there?"
    
    k  "I’m not sure yet.  Riku, after you check on Roman, meet me back in my lab.  It is urgent."
    
    "We both run back towards the rescue.  It would be easy enough to find even if we didn’t know where it was at.  The blood trail from Roman’s body would lead us to it."


label kaz28:
    "I’m sitting in Kazu’s lab, shaking.  I just got back from seeing Roman.  He isn’t conscious yet.  Soume told me he should be fine, but the look in his eyes seemed to indicate he wasn’t so sure."
    
    r  "I…I can’t believe this."
    
    k  "Hm?  Oh yes, I hope Roman does pull through.  Once Soume is finished, I shall go take a look myself.  I’m sure once he receives some proper medical attention, he’ll be fine."
    
    "I look down at the floor.  I am trying to hold back from crying, but I don’t know if I’ll be able to do it."
    
    r  "What…what did Mamoru mean…that you used to work for him?"
    
    k  "Ah…well, I was a prisoner of his for some time.  He captured me from my previous master, after he discover my talents."
    
    r  "Oh…and he made you…uh…"
    
    k  "He forced me to do experiments on other Majin.  Just like my master before him, and my master before him.  Being the only Majin doctor makes me a rather sought after commodity."
    
    r  "That…that sounds terrible."
    
    k  "It was.  I did…unspeakable things to other Majin.  At their orders.  I…I did some terrible things to a lot of people.  To…Soume."
    
    r  "Huh?  Soume?"
    
    k  "Yes. I didn't want---I was forced to experiment on him. They threatened my life!"
    r "...what did you do?"
    
    k "They...wanted to test regrowth of limbs and organs."
    k "I tried to convince them to do otherwise, but they wouldn't---"
    r "What did you do to him?"
    k "I removed his genitals. And the other part."
    
    r  "..........."
    k "He never forgave me. I know he didn't."
    
    k  "They grew back, but he just never..." 
    k "I…I know so much about so many various Majin bodies...because of those experiments."
    
    "A look of extreme sadness flashes over his face, and for a second he freezes.  He shakes his head, mumbles something to himself, and then immediately gets back to what he was working on."
    
    k  "That was a long time ago. Miss Susa released Soume from capture twenty years ago."  
    k "And she rescued me."
    
    r  "…............"
    
    k ".........."
    k  "Well, there, now you know everything you could ever need to know about me."
    k "You’re the first person I’ve ever told that story to willingly. You should feel honored."
    
    "Even when the Doc is revealing intimate details about his life, he still manages to do it in a way that makes him seem a little pompous."  
    "That takes real talent."
    
    r  ""
    
    k  "I assure you I don’t need to be coddled.  I do appreciate your show of friendship though.  I will think about it the next time I find myself saddened by something."
    
    r  "Uh…cool?"
    
    k  "Heh.  You are rather fond of that meaningless word.  Perhaps when we are done here I will take some time to expand your vocabulary!"
    
    "Kazu is working quickly setting up some of his remaining glassware, but he takes this time to smile at me."  
    "I don’t have the strength to smile back.  Roman is nearly dead, and the attack happened somewhere we are supposed to feel safe."
    
    r  "They were…just a half mile away from the rescue.  They have to be closing in on us.  Even if Roman does live…"
    
    k  "All the more reason why we most complete this research at once.  Hm…yes, this might work nicely.  And perhaps some of this…"
    
    "He is running around his lab, pouring some of any chemical he can find into several bowls.  He has set up the same thing we used last time when we were testing his reflexes."
    
    r  "Kazu, don’t take this the wrong way, but I’m not sure if now is the best time for all this.  Like, I just need some time to-"
    
    k  "No!  Riku, there is no other time.  You said it yourself.  They are closing in.  But we can still figure this all out."  
    k "But I need your help!  Please, I can’t do this on my own.  Let Soume worry about Roman for now.  I need you here."
    
    "He looks at me.  His desperation has left.  I don’t know what it is, but the confidence that he lost last week seems to have fully returned to him."
    
    r  "…fine.  Yeah, I can help."
    
    k  "Good, now, this is the same as-excuse me, what are you holding in your hands?"
    
    r  "Hm?  Oh…this is just another plant Roman gave me.  The last one he gave me.  I…I dunno.  I just wanted it near me."
    
    k  "Hrm.  Well, if you could please put it down for now."
    
    "I walk over to the table with it and set it down.  I adjust it a bit so it catches the light from the window."
    
    r  "Heh.  Who knows.  Maybe it will bring us some luck."
    
    k  "Hmph.  Luck is for those who lack skill.  There is no luck in this work; it is merely a silly concept created by the weak to scapegoat their own faults.  No, we-"
    
    "He finally looks over at me.  I’m not sure why but he stops.  His face softens.  Maybe it was how desperate I look, I dunno."
    
    k  "Ah, yes.  Luck.  Sure.  That…that is certainly possible."
    
    r  "…thanks, Kazu."
    
    k  "Yes, well.  Ahem.  Look, you were able to dull my sense last time."  
    k "I haven’t been able to duplicate your success recently, so I am relying on you to do what ever you did last time again.  I’ve brought more chemical."
    
    r  "‘Kay.  Yeah, I can try."
    
    k  "Excellent.  Same procedure as last time.  And Riku, time is of the essence, so please work diligently."
    
    r  "Sure thing."
    
    #Time passes
    
    k  "Ouch!"  
    
    r  "Gotcha again.  I’m getting pretty good at this science stuff."
    
    k  "That was excellent.  I…I couldn’t tell it was coming at all.  Tell me now, what compound was it?  Did you use any of the diluted neurotoxins?"
    
    r  "No, not really.  It-"
    
    k  "How about any of these common inhibitors over here?"
    
    r  "No.  I…I, uh, just put in one of these leaves."
    
    k  "What?  The leaves?   From this plant?"
    
    r  "Yeah.  I dunno, I was just trying anything.  Didn’t really think that would work but, hey."
    
    k  "No, Riku.  Think, what else did you add?  It couldn’t be the plant that did this, because-"
    
    "Kazutaka freezes.  His eyes dart back and forth in his head and he’s mumbling to himself."
    
    k  "Wait.  Then this means…"
    
    r  "Huh?"
    
    k  "Oh, you brilliant, brilliant boy!  Miss Susa was right about you!  How could I not see this before?  Oh, and it was so obvious!"
    
    r  "What are you talking about, Kazu?  What is so obvious?"
    
    k  "The embarrassing thing is I should have seen it sooner!  How could I miss the signs!  Oh and the charcoal!  The charcoal must have been picking it up from the air!  Ha ha ha!"
    
    r  "Huh?  What are you talking about."
    
    "Kazutaka hugs me and lifts me around in the air.  I would be a little weirded out if I wasn’t so fucking confused."
    
    k  "You beautiful, brilliant, child!  There is hope for our kind after all!  What outside the box thinking you exhibit!  Why didn’t you just tell me your suspicions?"
    
    r  "What suspicions?  I don’t know what you’re talking about…."
    
    k  "HA!  And so modest!  Riku, here, this is Liza’s emergency contact.  I managed to get someone to tell it to me.  Please, run upstairs and contact her immediately."  
    k "Tell her…tell her she must return to the shrine at once."
    
    r  "What?  Why?"
    
    k  "We can explain it to her later.  Just tell her everyone here is in grave danger!  Oh, this is just wonderful!"
    
    "He is pushing me out of the lab now.  Never knew someone to break out into song like this after the announcement of grave danger, but Kazu is a unique guy."
    
    k  "Thank you again, Riku!  You are perhaps the best assistant I have ever had!"
    
    "He leans down and hugs me, still laughing and making an assortment of excited noises.  With one last push, he shoves me out of the door and slams it behind him."
    
    r  "Uh…thanks?"
    
    "Guess I’ll go give Liza a call.  Not fucking sure what I’ll say to her, but I guess I can figure that out if she actually picks up the phone."
    
label kaz29:
    s  "Roman…"
    s "Roman, can you hear me?"
    
    ro  "Nngh…"
    
    s  "Roman…open your eyes."
    "It takes me a little while...everything is blurry, but there are warm hands grasping me."
    
    s  "Roman! You--you worried me."
    s "I was afraid...I was going to lose you."
    
    "I’m frightened.  I…I only sort of remember what happened to me.  I have vague memories of Mamoru grabbing my neck.  Did I die?"
    
    ro "...So...me...what's...happened?"
    s  "You were...attacked."  
    s "I've already done all the emergency surgery, and now that you're awake, I can fix the rest."  
    
    ro  "Oh...I--I'm alive."
    
    s  "Yes. Try not to talk too much right now."
    
    ro  "--t-thank you."
    
    "My face and head feel so stiff. I don’t even know if Soume can understand me."
    
    s "It was nothing. Truly."
    s  "I don’t know what I would have done..."
    
    "I know this isn’t a good time for me to say something like this."  
    "But I don't know, with everything that's happened, if I will be able to do this later."
    
    ro  "S-soume..."
    s "Shhhhh. You need to rest."
    ro "...I--love you. I've loved you for--so long now."
    
    s  "..........."
    
    "It's quiet."
    "I've ruined everything, haven't I? Everything!"
    if socompletion:
        jump loveconfession
    else: 
        jump sorrybutno
        
label loveconfession:    
    "Then there is a warm breath at my ear."
    
    s  "I love you too." 
    
    "...did that just happen?"
    
    s "I am so grateful that you came into my life."
    s "You're so unlike anyone I've known." 
    
    ro  "--a--"
    
    s  "Please don’t try to talk anymore. There will be time for all of this later."
    s "I'll finish healing you within the day."
    
    "I'm not sure what's happening, but it seems like Soume is searching for something."
    
    ro "...Soume...?"
    
    s "Mm, so he's found it."
    
    ro "...mm...?"
    "Soume leans down and presses a kiss to my forehead."
    
    s  "Rest, my little Roman."
    s "I must run a little errand. I will return to you soon."
    
    "I hear the door close, and as I think about what Soume and I just talked about, I fall peacefully into sleep."
    
label kaz30:
    k  "I've got it. I've got you now, youko scum."  
    
    #play sound  Static-
    
    k  "This plant collects energy and transmits it through pollen...a biological walkie-talkie!"
    
    k  "He's likely been sneaking the enemy in here, gallivanting about however he pleases, setting traps..."
    k "I must get contact to MIss Susa, immediately..."
    
    #play sound Door opening-
    
    k  "Ah, Riku, about time that you--"
    
    s  "I'm sorry, Doctor Kazutaka. It is only me."
    
    k  "Ah. Ahahaha!  Look who walks in here with his tail in between his legs!  I told you it was only a matter of time!"
    k "You're finished! I have all the evidence I will ever need."
    
    s  "I know…you've caught me."
    
    k "........."
    
    s "Though...I had hoped it wouldn’t come to this."
    
    k "........"
    k  "W-well, you unfortunately took part in a battle of wits against a man that has you quite outmatched."  
    k "I just ran a quick analysis on this little plants of yours. The pollen I figured out before."
    
    s  ".............."
    s "I see..."
    
    k  "Using this to block my sensory abilities?  Quite brilliant on your part."  
    k "They are all over the shrine, and Riku even managed to sneak one into my lab!  Not his fault mind you, as he was fooled like the rest of them into thinking you were harmless."
    
    s  "Yes, you are correct."
    
    k  "But the pheromones! No, I didn't see those coming."
    k "The way you always smell so sickeningly powerful."
    k "No wonder everyone has such an intense affinity for you! You’ve stacked the deck in your favor!"
    
    s  "Not exactly. I can't quite help those as much as I'd like."
    
    k  "Oh, I'm sure!"
    k "No wonder Roman is falling over himself for you."
    k "I'll make sure he knows first."
    
    s  ".........."
    s "I really am very sorry..."
    
    k  "Sorry?  You are sorry?  Hahaha!  I somehow doubt that will make everyone feel better.  Especially when I show them this!"
    
    s  "My transmitter."
    
    k  "Left it behind in your hurry to get back here, didn’t you? Well, I don’t know for sure who you are contacting with this, but if it is who I think it is, your game is over!"
    
    s  "…yes.  That would be problematic."
    
    k  "You could indeed say that!  You---"
    
    k "............"
    
    s  "I really would prefer not to have to kill you."
    s "You forced my hand a little sooner than I was planning. And what a waste of talent and surgical skill, beisdes."
    
    k "...stay away...don't get any closer!"
    
    s "You are without a doubt the smartest Majin I have ever encountered. Truly."
    
    k  "Ngh…no…Soume--"
    
    s  "Again, Doctor, I am deeply apologetic about this." 
    s "My plants will clean up the area."
    s "Out of respect, they are releasing a drug that should make it swift and painless."
    
    k  "But…how did…how could I miss…the…danger signs--ah." 
    k "The jamming pollen. I forgot to stop the release of the jamming pollen."
    
    s "That turned out lucky for me."
    s "Your clairvoyance is rather annoying. It is exceptionally difficult to catch you off guard." 
    s "I had to work very hard to perfect the pollen."
    
    k "..............."
    
    s "...well."
    s "I really must get back to Roman, he needs medical attention."  
    s "Please, do not take this personally."
    
    k  "HURK!"
    
    s "Well...perhaps a little personally."
    s "I did never forgive you for that little experiment on my genitals."
    
    k "---acchh---"
    
    s  "Goodbye, Doctor Osamu Kazutaka."
    
    #play sound  Door closing
    
    k  "Ngh…huff…huff…so…this is death…"
    
    k  "…ngh…"
    
    k " …how…fascinating…"
    
    #play sound  Crunching noises, splattering gooey noises, etc-

