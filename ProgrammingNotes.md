# Programming notes as mentioned in the GDD #



> ##### Status #####
> <ul>
<blockquote><li><font color='red'><b>Not done</b></font>: thing 1</li>
<li><font color='orange'><b>Partly done</b></font>: thing 2</li>
<li><font color='green'><b>Done</b></font>: thing 3</li>
</ul></blockquote>


---


## User Interface ##

The game runs through a basic VN layout that includes a textbox, buttons for saving, loading, options, and your game inventory. In addition, there will be markers letting you know how much HP and MP you have.

### Main UI ###

> Clicking the mouse in a generic area, or pressing enter, will move text along. When you need to make a game decision, the options will pop up in the center of the screen and you may choose one by clicking on it. Upon clicking on a choice, you will hear a sound and the game will move on in the direction you have chosen. If you have made a certain decision already, the color of the text will change to let you know that you have already made that choice.

> The textbox has a few buttons on it, namely, a back and skip button. Back gives you the ability to scroll back through old text. The text will appear in a different color, exactly as it appeared in the box when you it first ran through it. You may only go back as far as your last choice, to make the game difficult. Skip allows you to quickly scroll through text or scenes you have already read.

> The Save button will allow you to save your game by taking you to a saving page. It will inform you of the name of the chapter you were in, and time in the game you have done for that entire save slot. After confirming, it will allow you to either return to the title page, or return to your game.

> The Load button will allow you to immediately load a save slot you've made before, mid-game. However, it will not save a game automatically, so you must remember to save it yourself.

> The Options menu will allow you to change the volume of the music, SFX, voices and change the text between JP and EN.

> ##### Status #####
> <ul>
<blockquote><li><font color='red'><b>Not done</b></font>: next button; Renpy doesn't support this, but it should be possible to make it a roll forward button instead of a dismiss (triggers the next line) button</li>
<li><font color='red'><b>Not done</b></font>: changing text between JP and EN</li>
<li><font color='orange'><b>Partly done</b></font>: back button; will have to modify it to work with the new next button</li>
<li><font color='green'><b>Done</b></font>: saving/loading/options (Renpy defaults)</li>
</ul></blockquote>

### The Palm Pilot ###

> This part of the UI has three major functions; storing your items gained, your journal entries gained, and allowing you to play minigames you have acquired. Clicking on the palm pilot icons will cause the palm pilot screen to come up, which will allow you to do a few things:

  * Check your Inventory.
  * Check your Journal Entries.
  * Play through minigames you have acquired.
  * Return to the game.

> The Inventory button will take you to the inventory, which is largely the same as the original Palm Pilot screen except that a set of icons will appear on it corresponding to the items you have acquired. There should be an arrow allowing you to scroll through all of the items. Clicking on an item will bring up a screen with a large picture of the item, and a detailed description of it. Clicking on that page will cause it to disappear and bring you back to the inventory.

> The Journal button will take you do the stored journal entries, which is the same as above except the icons will correspond to journal entry topics instead, each named briefly. Clicking on a topic will bring you to all the entries you have acquired for that topic. There will be a back button on this screen to return you to the topic screen. Clicking on an entry will bring up a screen so that you may read the journal entry in question. Clicking on that screen again will bring you back to the topic you were on.

> The Minigame button will allow you to play any minigame you have already done. It will bring show you icons for each minigame. Clicking one will take you to that minigame, where you  may play through it. There is a “QUIT” button on every minigame that will allow you to quit at any time and return to the last screen you were on.

> Return to game will return you back to wherever you were in the game.

> ##### Status #####
> <ul>
<blockquote><li><font color='red'><b>Not done</b></font>: button press effects</li>
<li><font color='orange'><b>Partly done</b></font>: inventory screen; the mechanics pretty much work already, so this one is waiting for the proper icons/grid layout/transition effects to make it pretty</li>
<li><font color='orange'><b>Partly done</b></font>: journal screen; same as above</li>
</ul></blockquote>


---


## The Nightly Options ##

Nightly options are a small set of options that pop up during the script. There are four possible options: Search, Rest, Research, Shop.

### Rest ###

> The Rest option merely fades the screen to black and lets you know that Riku slept. Sleeping allows Riku or Roman to rest, and the restful sleep allows them to get a training boost each time they do it. The game will require you to pick, in some cases, between getting a new scene and giving your main character training, so the player needs to play close attention to that.

> ##### Status #####

> <font color='red'><b>Unimplemented</b></font>

### Search ###

> Search brings up searchable screens. They allow people to click around to find items and read funny little ditties about various things in the game. The display will be a background, with the items that correspond to that background for the room chosen. Some backgrounds are reused, and just set up with different items, so that is important to keep in mind when setting them up. To make it easier, each room will have a single screen that is the set of “search spots” associated with it, and then hover versions as necessary.

> Search spots are spots that can be clicked on to get information or find items. They should be very lightly highlighted when scrolled over, and when clicked, a small box explaining what is happening there should pop up, as well as whether or not there is an item in that spot. Search spots are usually light figures, drawers, beds, anything that isn't the wall or the floor can become a search spot.

> Night options are labeled in the programming so that the proper items will go into the correct room on the correct night. Upon clicking Search, a map of the entire shrine will pop up and you may click on the room you wish to search. It will bring you to that room, which may trigger an event. If not, then clicking on search spots will trigger information about what you clicked, or you may receive an item or journal entry, which will go into your palm pilot inventory.

> Not all items can be found during every nightly option, which is why they are labelled and numbered. Some items only appear on certain nights. Some items appear every night, but move positions. If possible, I'd like them to move positions at random.

> ##### Status #####

> <ul>
<blockquote><li><font color='red'><b>Not done</b></font>: event triggering</li>
<li><font color='red'><b>Not done</b></font>: hiding journal entries in stashes</li>
<li><font color='orange'><b>Partly one</b></font>: room selection (missing graphics and final transition effects)</li>
<li><font color='green'><b>Done</b></font>: item filtering based on night</li>
<li><font color='green'><b>Done</b></font>: item filtering based on room</li>
<li><font color='green'><b>Done</b></font>: item location randomization</li>
<li><font color='green'><b>Done</b></font>: items being removed from stashes once found and added to the inventory</li>
</ul></blockquote>

### Research ###

> Research is an option that Riku or Roman can carry out with Kazutaka. Unlike Search and Rest, it does not appear from the beginning of the game, and only appears after the scene where you actually meet Kazutaka. It will appear from then until the end of the game.

> Choosing research will bring up the library image and an image of Kazutaka. It may trigger events, or you may receive a journal entry, which will go into your palm pilot inventory.

> ##### Status #####

> <font color='red'><b>Unimplemented</b></font>

### Shop ###

> Shop is self-explanatory and works much like research. You're taken to the store, where Riku will be allowed to have any one item. You don't need to worry about money...it's assumed that Riku has it. The shop may also trigger extra shop events.

> ##### Status #####

> <font color='red'><b>Unimplemented</b></font>


---


## Battles ##

Battles are simplified. HP and  MP start out very small in game, because your character is weak. Actions taken in game will affect the HP and MP of your character, letting it rise as they get stronger. Minigames also affect the HP and MP of your character, letting it rise as they get stronger. Minigames also control how your attacks work during battle! Having certain items in your inventory will also lift your HP or MP.

In battle, you may choose to attack or use magic.

(Jury is still out on whether or not to allow usage of items.)

Each magic attack takes away a certain amount of MP. Depending on your score in certain minigames, it will allow each magic attack to take away LESS MP so you can do more magic attacks.

Defense is also important. Each monster attack will take away a certain amount of HP, but depending on your score in minigames, each attack will take away less HP.

> ##### Status #####

> <font color='red'><b>Unimplemented</b></font>


---


## Minigames ##

Minigames all have the same basic layout. The game portion takes place within the larger right hand portion of the screen, while a slim portion on the left hand will type the instructions for the game, as well as provide the option to return to your regular game, or start the minigame. Upon selecting start, the minigame will do so and a button allowing you to quit the minigame while playing will become active.

This is preliminary. A Training Grounds background should be used as the BG for all minigames. The only graphics that will differ are the specific ones for each minigame. Minigames affect your HP and MP depending on the score you reach or the level you reach. For example: if you beat level 1, then you get maybe +5 HP and +5 MP. If you beat level 2, you get more. Or, if you have a score of 10,000, you get +10 HP and +10 MP.


> ##### Status #####
> <ul>
<blockquote><li><font color='orange'><b>Partly done</b></font>: minigame layout</li>
</ul></blockquote>


### Strength Game ###

> The player will have to either life a barbell or do squats with a weight. The player will do the work out and depending on how good their technique is decides how much strength they will gain. Technique will be decided by the player hitting the green mark on a meter, that will have a cursor moving up and down it. A perfect example of this can be shown in fable two and how you do jobs.

> #### Game design ####

> The cursor will move up the meter on the lift and down for the drop. Hitting the green bar for both an up and down lift will be one perfect rep, while hitting the orange will be medium technique and red will be bad technique. If the player fails to click it will by bad technique by default, but the game will continue.

> #### Difficulty ####

> The speed that the cursor moves will be increased, as well as the placement of the green area on the meter. We could also do it so they have to do more sets, so that they have to do longer work outs to build more strength.

> #### Potential pieces ####

  * 3 part animation of a guy doing squats.
  * 2 part animation of guy being exhausted.
  * Meter.

### Agility Game ###

> Simple Whack a mole game. The UI would provide 9 slots for moles.

> #### Difficulty ####

> The speed that the moles appear could increase. Having more then one coming up at the same time. You could also have the moles have different speeds, this would mess up the player’s rhythm and making it harder for them to hit the moles as well. Another option would be adding in a mole that they aren't meant to hit. This will also make them have to think more instead of simply hitting. Also you will need to add in a function that will stop players from hitting two keys at the same time, otherwise they would just mash the keypad.

> The keys for this game would be the num pad; 1-9.

> #### Potential Pieces ####

  * 1 smaller background of dirt and whatnot.
  * 1 hole for the moles to come out of (repeated 9 times).
  * 1 mole, perhaps a couple more for variety.
  * 2 part “whack” animation.

### Stamina Game (Also known as Day Challenges) ###

> This mini game will have the player running over changing terrain. There will be a bar on the screen that will have three colours: Red, yellow and green. The player will have to bash a button, or buttons to keep a cursor within the green for the best results. As the terrain changes, the position of the green colour on the bar will also change, so the player will have to change the pace of their button bashing. Keeping the cursor in the green will make the player use the least amount of stamina, while if it is in the red they will lose the most. The mini game will end when the player runs out of stamina.

> #### Game Design ####

> The design will take the player over a few types of terrain. The left/right/up button will make the player start running, and at the same time, they must hit space bar. Hitting it too fast will cause Riku to use too much energy. Hitting it too slow will also cause Riku to use too much energy. Hitting it just right will cause Riku to use the least amount of stamina to get to the end. Different types of terrain will work differently. The game should be timed; with a beginning and ending, and it will have 4 different levels.

> #### Difficulty ####

> The longer the game goes, the faster you must move and switch the amount of spacebar touching. Perhaps some obstacles will be stuck in to stop you?

> #### Potential Pieces ####

  * Sprite with animations.
  * Terrains.
  * Obstacles.


### Magic Control Game ###

> The player will have to hit a target in this mini game. The position and hardness of the target will change as you play. The idea is to use the right amount of ‘Force and ‘Power’ to have enough range to hit the target and smash it. Too much or too little force and the spell will fall short or go over the target, while too little or too much power will cause the target to remain intact or the spell to explode.

> #### Game design ####

> The player will have a view in front of them of a landscape, upon this land scape we can place targets at random. Now the player will choose the amount of ‘Force’ and ‘Power’ they use. Force being the distance the spell travels, while power is the damage the spell will cause upon impact. Now when they select how much of each of these they then choose the option ‘Fire’. This will release the spell and the player will watch it fly out toward the landscape. The place it lands will have a mark. The player can then adjust the force and power accordingly until they hit and destroy the target. The game will be timed, and the player will have 1 minute to destroy as many targets as they can. They will be allowed to try at each target as many times as they need to to break it. The actual control of force and power will be reliant upon touching the space bar and shift keys in conjuction.

> #### Difficulty ####

> Targets will be of varying distances, and different colors will denote targets that take more force to hit. The time will also get shorter and shorter.

> #### Potential Pieces ####

  * Targets of different colors.
  * Destroyed targets of different colors.
  * Minorly burned targets of different colors.
  * Majorly burned targets of different colors.
  * Basic landscape background.
  * Divet in the ground to mark a miss.


### Magic Energy Game ###

> This minigame will represent you trying to maintain magical power within your body. The higher the level the more magical power you will need to try to maintain within your body.

> #### Game design ####

> There will be a hand with “energy tunnels” displayed within. Pressing Shift will start the power flowing. The up button increases the power, the down button lowers the power, the right and left buttons move the cursor between the tunnels. Power must be channeled at a certain level for it to work. Too much and it will explode on your hand. Too little and it will just flop.

> #### Difficulty ####

> The difficulty could be changed by first starting out with just one or two meters, then as the player goes up in the levels they get to a total of five. The unbalance time between meters can also be shortened. Also more than one meter could become unbalanced at the same time.

> #### Potential Pieces ####

  * The hand.
  * The required bars for:
    * The power being channeled into the hand.
    * The power being properly channeled into the finger.
    * The power veering off resulting in fail.
    * The power exploding on your hand.



### Hunt Duck Game ###

> This minigame will basically be Susa's favorite video game.

> #### Game design ####

> There will be ducks. Big ducks, little ducks, ducks of all sizes. Click them with your mouse. Some ducks will take several hits to kill, so be prepared! Score will be determined based on the number of ducks you kill.

> #### Difficulty ####

> The difficulty will be determined by the size of the ducks, and the number of hits it takes to kill the ducks.

> #### Potential Pieces ####

  * Ducks of different sizes and colors.
  * BAM gunshot animation.


### Farmville: Our Version ###

> This will be a planting game. You can plant seeds you find along the game and reap the benefits. The plants here go into your inventory, and just like any other inventory item may affect your HP and MP, or qualify you for new events.

> #### Game design ####

> Roman will, after a certain point in the game, be allowed to keep a little garden. Soume will give you the first seed. The seed will take X amount of time (which you need to spend playing the game) to grow to its four different stages, after which you may collect it. After collecting, it will go into your inventory, where it stays as long as you have the save file. Once the seed or plant goes into inventory, you can use it in any of your save files, but the time calculated for it will only draw from one save file.

> For example, if you plant one seed that takes 1 hour to grow to a full plant, plant it, play for 15 minutes, save and quit, your plant will be saved at 15 minutes or into its second “growth” (using the farmville model). If you open that game, play another 15 minutes, and save it to another file, the first file will have it saved at 15, and the second will be saved at 30, or into its third “growth”. Only when the plant reaches its fourth “growth” will it go into your inventory as a plant. Because seeds and plants go into a game-wide inventory, you can plant as many as you want, however, only the first seed and first plant will affect your stats.

> However, to encourage people to spend time on their farms/gardens, each plant you plant has a 10% chance of becoming a “Monster” plant. If you bloom a monster plant, you get an extra boost in stats, as well as an extra inventory item. (These should not be necessary to get the completed inventory bonus, however.)

> #### Difficulty ####

> N/A. The game stays the same difficulty; it doesn't change. However, if you pass 150% of the time it took to grow the plant, it will wither

> #### Potential Pieces ####

  * Plot of dirt/flowerpot BG
  * 10 plants with 4 growth portions each.
  * 10 withered plants.
  * 10 monster plants.


---


## Extras ##

  * Parallax layering for B.Gs.
  * Blinking and Mouth Movements for Sprites
  * Time tracking
  * Weather Effects
  * Enabling title screen's bonus section after completing an ending