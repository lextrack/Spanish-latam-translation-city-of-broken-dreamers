
image bg ch3sonjamil1 = "ch3sonjamil1"
image bg ch3sonjamil2 = "ch3sonjamil2"
image bg ch3sonjamil3 = "ch3sonjamil3"
image bg ch3sonjamil4 = "ch3sonjamil4"
image bg ch3sonjamil5 = "ch3sonjamil5"
image bg ch3sonjamil6 = "ch3sonjamil6"
image bg ch3sonjamil7 = "ch3sonjamil7"
image bg ch3sonjamil8 = "ch3sonjamil8"
image bg ch3sonjamil9 = "ch3sonjamil9"
image bg ch3sonjamil10 = "ch3sonjamil10"
image bg ch3sonjamil11 = "ch3sonjamil11"
image bg ch3sonjamil12 = "ch3sonjamil12"


label ch3sonjamil:
    scene black with Dissolve(2)
    show bg ch3sonjamil1 with dissolve
    j "Do you ever miss it? Us, on these runs I mean?"
    p "Part of me does. Sure."
    show bg ch3sonjamil2 with dissolve
    $ insult = renpy.random.choice(insults)
    j "Don't bullshit me. I know it's more than a part. We were the best, [pl]. Glad we're together on this, [insult]."
    p "Better than on opposite sides."
    j "I don't know, last time we competed for a target was epic."
    p "So was the aftermath in the Grand Luxe. I think I felt bad for whoever had to clean the room the next morning."
    j "You're still too soft, [pl]. But that's what I... Damn."
    show bg ch3sonjamil3 with dissolve
    j "Look, so we're clear. If I get the call... [p]-"
    p "I know, Sonja. I've got no illusions."
    show bg ch3sonjamil4 with dissolve
    j "I'll send you a gift basket as a consolation prize."
    play music audio.tense fadein 2.0 fadeout 2.0
    n "The wind picks up and the smog in the air descends"
    p "Fuck me. Let's move, Sonja."
    show bg ch3sonjamil5 with dissolve
    j "The hell? *coughs* No warning. What the fuck do those queef collectors at the weather service get paid for?"
    show bg ch3sonjamil6 with dissolve
    n "The smog thickens, moved by the wind. Visibility is reduced to near zero and their lungs burn from the irritation."
    j "COME ON, I KNOW A PLACE UP AHEAD!"
    p "RIGHT BEHIND YOU!"
    show bg ch3sonjamil7 with dissolve
    p "BET YOU'RE GLAD STELLA ISN'T HERE!"
    j "FUCK OFF!"
    scene black with Dissolve(2)
    show bg ch3sonjamil8 with dissolve
    j "*Coughs* Now that was fun."
    p "If you like the taste of pollution and that burning aftereffect in your lungs, absolutely."
    show bg ch3sonjamil9 with dissolve
    j "Quit your bitching. My contact is just down this way."
    p "Is he solid?"
    show bg ch3sonjamil10 with dissolve
    j "Most of the time, but I'm warning you now, she's rather odd and last time her info was out of date."
    p "So you stiffed her?"
    j "You do your job right, you get paid -- otherwise, tough shit."
    show bg ch3sonjamil11 with dissolve
    play music audio.creepy fadein 2.0 fadeout 2.0
    j "Here we are. The Stairway to Heaven."
    p "Wonderful..."
    show bg ch3sonjamil12 with dissolve
    j "Like you're too good for a whorehouse. Come on, it's early. We'll have the place to ourselves."
    jump ch3stairway
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
