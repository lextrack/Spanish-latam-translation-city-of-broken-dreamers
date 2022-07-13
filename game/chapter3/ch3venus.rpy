


label ch3venus:
    show bg ch3stairway35 with Dissolve(1)
    play music audio.black fadein 2.0 fadeout 2.0
    ve "So are you going to be my first client?"
    p "Looks that way."
    ve "I hope I perform adequately."
    p "I'm sure you'll be fine."
    ve "Thank you, Sir."
    ve "I must also state that the management is not responsible for any injuries that are a result of unapproved insertions from either party."
    show bg ch3stairway36 with dissolve
    ve "Now if you follow me. I will lead you to an appropriate room."
    show bg ch3stairway37 with dissolve
    if not persistent.ch3card1:
        $ renpy.notify(['Possible clue', 'alert'])
        show screen hidden_item("ch3card1", "ch3card1", 972, 515, 207, 113)
    p "What exactly can you do, anyway?"
    ve "I have been equipped with two main settings."
    p "Like?"
    hide screen hidden_item
    show bg ch3stairway38 with dissolve
    ve "Allow me to explain. As of software update 0.1.5 I have two primary modes."
    ve "Mode one, or princess mode. A sweet and innocent girl with just the right touch of naivete. She is daddy's little girl and you can be her daddy. All the jail bait, with none of the jail."
    ve "Mode two, or depraved slut mode. Your very own depraved whore. A virtual slave that you can treat however you wish."
    ve "She has been a bad girl and needs to be punished. Enjoy acting out your most repressed desires in a safe and legally responsible environment."
    ve "The second setting, due to higher maintenance costs, is $1000 per session. The other you have been approved for."
    show bg ch3stairway39 with dissolve
    ve "More settings will be added in our next update."
    ve "Which setting do you prefer?"
    menu:
        "Princess":
            p "I think the princess setting will work."
            show bg ch3stairway40 with dissolve
            ve "Of course, Daddy. I will be your little princess."
            p "I'd like that."
            show bg ch3stairway42 with dissolve
            ve "Good, now if you will follow me to the left."
            jump ch3venusprincess
        "Slut":

            p "I think I need a girl to punish. Besides, Betty does want me to break you in, correct?"
            show bg ch3stairway42 with dissolve
            ve "Yes, we can do this. Switching modes."
            p "..."
            show bg ch3stairway41 with dissolve
            ve "Mmm, join me to the right, master. I will be in shortly. I've been a bad girl... and I deserve punishment."
            jump ch3venusslut
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
