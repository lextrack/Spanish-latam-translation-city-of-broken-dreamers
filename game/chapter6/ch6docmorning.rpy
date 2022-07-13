image bg ch6docmorning1 = "ch6docmorning1"
image bg ch6docmorning2 = "ch6docmorning2"
image bg ch6docmorning3 = "ch6docmorning3"
image bg ch6docmorning4 = "ch6docmorning4"
image bg ch6docmorning5 = "ch6docmorning5"
image bg ch6docmorning6 = "ch6docmorning6"
image bg ch6docmorning7 = "ch6docmorning7"
image bg ch6docmorning8 = "ch6docmorning8"
image bg ch6docmorning9 = "ch6docmorning9"
image bg ch6docmorning10 = "ch6docmorning10"


label ch6docmorning:
    show bg ch6docmorning1 with dissolve
    p "Hey, sorry about that, getting ready for a run. Never ends, does it?"
    if k_score >= 3:
        k "No problem."
    else:
        k "It's not a problem and good morning, [p]"
    if k_score >= 3:
        p "Heh, sorry. Morning, Katie."
    p "Sleep well?"
    show bg ch6docmorning2 with dissolve
    k "Yeah, actually. The beds here are better than that motel at least."
    p "Betty knows her shit."
    k "Geez, first you take a girl to a red light motel, then a brothel. She might get the wrong idea."
    p "Or the right one."
    k "Pretty sure it's the wrong one."

    k "Anyway, what's going on?"
    p "Business. Just doing a favor for Betty."
    k "Just you?"
    p "And the big guy. It looks like a two-man job."
    show bg ch6docmorning3 with dissolve
    k "Oh."
    p "Don't worry, it's nothing crazy this time."
    k "I wasn't worried about you."
    p "Gee, thanks."
    show bg ch6docmorning4 with dissolve
    k "No, I meant... Damn it."
    p "What is it?"
    k "(Remains silent, lost in thought)"
    p "Katie..."
    show bg ch6docmorning6 with dissolve
    k "Well, not like I have a real license to lose anyway."
    k "Just go on your own. Henry shouldn't be going on your \"favor\" for Betty."
    p "Not fit for active duty, that what you're saying?"
    show bg ch6docmorning5 with dissolve
    k "Not exactly. More like sick."
    p "How sick are we talking?"
    k "I can't say for sure."
    p "Your best guess?"
    show bg ch6docmorning6 with dissolve
    k "Bad. Very bad. He's got maybe six months and even that's a stretch."
    p "Damn."
    k "Yeah. Damn."
    p "Can anything be done?"
    show bg ch6docmorning5 with dissolve
    k "Betty's set up here is well... scary good, but it's still nothing compared to the facility I would need to fix him up."
    k "And that's not the biggest problem. His limiter, it's dying."
    p "Shit. Must have gotten damaged in the fight with the Red Moon."
    k "That combined with age..."
    k "His body can't take it. The human body isn't meant to deal with what that thing does."
    p "Can't we source a replacement?"
    show bg ch6docmorning4 with dissolve
    k "Where? They don't sell these in the local pharmacy. Even if they did, we're looking at god knows how much for a new one."
    p "Damn that government tech."
    show bg ch6docmorning9 with Dissolve(1)
    p "If he goes out today, is he going to just drop dead?"
    k "No, but every time his adrenaline gets pumping, it's a risk."
    p "I'll talk to him, but I don't see him stopping until Gloria is safe."
    k "Then get her safe, fast."
    show bg ch6docmorning10 with dissolve
    g "No..."
    g "This is all my fault."
    jump ch6mission
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
