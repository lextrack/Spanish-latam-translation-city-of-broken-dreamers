
image bg ch6stairwaybetty1 = "ch6stairwaybetty1"
image bg ch6stairwaybetty2 = "ch6stairwaybetty2"
image bg ch6stairwaybetty3 = "ch6stairwaybetty3"
image bg ch6stairwaybetty4 = "ch6stairwaybetty4"
image bg ch6stairwaybetty5 = "ch6stairwaybetty5"



label ch6stairwaybetty:
    $ extraevents.append("ch6stairwaygetroom")
    show bg ch6stairwaybetty2 with dissolve
    p "Hey, Betty, sorry about dropping this on you..."
    b "Well, at times the spirits work in strange ways."
    p "Heh... Still, I know this is the last thing you asked for."
    show bg ch6stairwaybetty1 with dissolve

    b "[p], I may have some years on you, but even so, you never counted me out back in basic, even if everyone said I was too old to start."
    p "Pretty sure us staying here outweighs that by miles."
    show bg ch6stairwaybetty4 with dissolve

    b "Doesn't matter. You helped me back then. Even if it was just encouragement, that's what I needed."
    b "And right now, what you need is a place to hide. I call that even, almost. Besides, I think if I kicked that girl out Venus may have literally blown a fuse."
    p "So, you do realize she's just a bot?"
    show bg ch6stairwaybetty3 with dissolve
    b "I'm not insane, [p]."
    p "..."
    b "I won't have that negativity around me, you hear me?"
    p "Noted. Your house, your rules."
    show bg ch6stairwaybetty5 with dissolve
    b "Good, now, here is a keycard to room 108. It's nothing great, but it's clean."
    p "Thanks. Tell me it has a bed?"
    show bg ch6stairwaybetty4 with dissolve
    b "Yeah, of course. Look around, what kinda place do you think I run here."
    p "Fantastic, sleeping in chairs and couches was starting to take its toll."
    show bg ch6stairwaybetty2 with dissolve
    b "Well, thank me when you get up. I have something I need you to do for me."
    p "Without my ride, it may prove tough."
    b "Let me handle that. Just take it easy tonight, I'll explain in the morning."
    p "No problem. Thanks again, Betty."
    jump ch6stairwaymenu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
