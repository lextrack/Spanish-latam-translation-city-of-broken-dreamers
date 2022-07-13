label ch7backagaininside:
    scene black with Dissolve(2)
    show text "{=trans}BACK AT THE STAIRWAY TO HEAVEN{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    show bg ch7return11 with dissolve
    play music audio.space fadein 2.0 fadeout 2.0
    p "Hey Venus."
    p "Venus?"
    show bg ch7return12 with dissolve
    s "I believe she is recharging, Sir."
    p "Thank you for that astute observation, Sam. Well, better see how they are making out."
    jump ch7backagain

label ch7backagain:
    scene black with Dissolve(1)
    show bg ch7returnoutside8 with Dissolve(1)
    sa "So? He come back?"
    "Bolter" "Why ask? Thought you were following the ghost man?"
    show bg ch7returnoutside9 with dissolve
    sa "Hey, fuck off. I get enough shit from the rest of them, I don't need it from you as well."
    "Bolter" "Cool your tits, girl. Just yawning from the waiting. Saw the ghost man. No girl, though."
    show bg ch7returnoutside8 with dissolve
    sa "Well, go. I'll keep a lookout. I see the girl, I'll let you know."
    "Bolter" "Fine, just don't fuck anything up, yeah?"
    "Bolter" "And girl, you gonna freeze your ass off when it pours tonight. All over the nets, storm's comin'."
    sa "I'll be fine."
    show bg ch7returnoutside10 with dissolve
    sa "So long as I don't get shot."
    jump ch7scan
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
