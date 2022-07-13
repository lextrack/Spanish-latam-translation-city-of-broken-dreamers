
image bg ch6stairway0 = "ch6stairway0"
image bg ch6stairway1 = "ch6stairway1"
image bg ch6stairway2 = "ch6stairway2"
image bg ch6stairway3 = "ch6stairway3"
image bg ch6stairway4 = "ch6stairway4"
image bg ch6stairway5 = "ch6stairway5"
image bg ch6stairway6 = "ch6stairway6"
image bg ch6stairway7 = "ch6stairway7"
image bg ch6stairway8 = "ch6stairway8"
image bg ch6stairway9 = "ch6stairway9"
image bg ch6stairway10 = "ch6stairway10"
image bg ch6stairway11 = "ch6stairway11"
image bg ch6stairway12 = "ch6stairway12"
image bg ch6stairway13 = "ch6stairway13"
image bg ch6stairway14 = "ch6stairway14"
image bg ch6stairway15 = "ch6stairway15"
image bg ch6stairway16 = "ch6stairway16"
image bg ch6stairway17 = "ch6stairway17"
image bg ch6stairway18 = "ch6stairway18"
image bg ch6stairway19 = "ch6stairway19"
image bg ch6stairway20 = "ch6stairway20"




label ch6stairway:
    play music audio.creepy fadein 8.0 fadeout 2.0
    scene black with Dissolve(1)
    p "Betty! You here?"
    show bg ch6stairway0 with dissolve
    p "Come on, Betty. Please!"
    show bg ch6stairway9 with dissolve
    p "Easy does it, you just lay there."
    p "Betty!"
    show bg ch6stairway4 with dissolve
    h "This is not what I was expecting."
    p "I wouldn't touch anything. You don't know where it's been or want to."
    show bg ch6stairway1 with dissolve
    ve "Ah, you have returned."
    p "Please, is Betty here?"
    show bg ch6stairway2 with dissolve
    ve "Ma'am, it's [p], from the other day."
    show bg ch6stairway5 with dissolve
    b "Right, here."
    b "And that kind of negative energy just isn't called for when someone enters here unannounced and after hours."
    if "ch3bettystop" in extraevents:
        show bg ch6stairway6 with dissolve
        b "But you're lucky I like you. What's going on, your aura seems tense?"
        p "Betty, can we please pause the hippie bullshit. Just, not now."
        b "You're starting to sound like your musclebound--"
        p "Betty!"
    else:
        show bg ch6stairway20 with dissolve
        b "I do always adore a repeat customer, but I work on appointments only, [p]."
        p "Not here about that."
        b "Clearly, though don't tell Venus, that will break her little heart."
        show bg ch6stairway8 with dissolve
        h "Venus?"
        p "Long story..."

    show bg ch6stairway7 with dissolve
    b "Well, if it isn't the target. I will say this about you, horrible aura or no, you do make for an interesting day."
    b "So what brings you and Mr. Gibson here?"
    show bg ch6stairway8 with dissolve
    h "[p]?"
    p "Thank her for me finding you. She has eyes everywhere."
    h "I don't think a thanks is in order. Gloria and I would probably still be safe there..."
    show bg ch6stairway11 with dissolve
    b "Oh please, darling, someone would have found you eventually. You can't stay off the grid completely, not forever."
    p "Can we focus on what's important?"
    show bg ch6stairway10 with dissolve
    h "I..."
    p "You ok?"
    h "*Grunts in pain* Fine."
    p "No, no you're not."
    show bg ch6stairway12 with dissolve
    b "What's wrong with him?"
    p "He just went toe to toe with a Red Moon."
    b "You're serious? Interesting is an understatement, [p]. What did you get yourself into?"
    p "The shit."
    b "As always. So a Red Moon? A real one?"
    h "*Coughs* Yeah, one at least..."
    show bg ch6stairway13 with dissolve
    b "So you have a killer after you, but unless you want a taste of true love before you move on to a better place, I don't know why you're here."
    p "We need a place to hide, Betty."
    b "Sorry, this is a whorehouse, not a hotel..."
    show bg ch6stairway16 with dissolve
    ve "Ma'am, who is the new girl? Did you bring me a sister?"
    show bg ch6stairway14 with dissolve
    b "A sister? Honey, did your programming get scrambled?"
    b "She's... Christ, I'm sorry, you two."
    b "The answer is no. Now you guys should go."
    show bg ch6stairway17 with dissolve
    if "ch3bettystop "in extraevents:
        ve "Who is your friend? Is he my new Daddy?"
    else:
        ve "Can this one be my Daddy?"


    p "Fuck, Betty, how long have we known each other, don't make me beg."
    show bg ch6stairway15 with dissolve
    b "Do you have any idea how hard it was to get this place up and running? To build an entirely new life? Now you want to hide here? And from whom?"
    p "Baynard, Vostok, the LAPD... Everyone basically."
    show bg ch6stairway16 with dissolve
    ve "Ma'am, this pretty one doesn't look well. Why can't we keep her?"
    show bg ch6stairway14 with dissolve
    b "This is just karma coming back again. Your karma, not mine! You need to leave!"
    show bg ch6stairway15 with dissolve
    b "And Venus, please... No, you can't keep her! It doesn't work like that."
    b "I feel for you, I do, but I can't."
    p "Brothers in arms, brothers for life."
    show bg ch6stairway14 with dissolve
    b "Don't you dare..."
    p "This is important, Betty."
    show bg ch6stairway9 with dissolve
    b "*Sighs* What's wrong with her?"
    p "I'd say you wouldn't believe me. But, this is you."
    show bg ch6stairway11 with dissolve
    b "Don't patronize me, [p]."
    p "Okay, she can blow shit up with her mind, when she does, this happens."
    b "Wait... You're serious?"
    show bg ch6stairway20 with dissolve
    b "Dammit! Venus, help the big lug. [p], take the cutie pewtutee. Let's head out back."
    show bg ch6stairway18 with dissolve
    ve "Thank you for the new Daddy, [p]."
    h "When I can walk right, I'm going to kill you, [p]."
    p "Noted."
    show bg ch6stairway19 with dissolve
    p "Come on, Gloria. Let's get you more comfortable."
    jump ch6stairinside
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
