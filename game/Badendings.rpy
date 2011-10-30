label badend1:
    "Ahahaha you die cause you suck."
    jump game_over
    
label badend2:
        "You pissed Susa off so bad with your idiot stunting that she kicks you out of the shrine!"
        "What're you going to do for protection now...?"
        jump game_over

label game_over:
        "Here is some game over loop thing that will play."
        "You lose."
        return
