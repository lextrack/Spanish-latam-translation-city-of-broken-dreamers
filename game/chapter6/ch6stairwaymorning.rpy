
image bg ch6morning1 = "ch6morning1"
image bg ch6morning2 = "ch6morning2"
image bg ch6morning3 = "ch6morning3"
image bg ch6morning4 = "ch6morning4"
image bg ch6morning5 = "ch6morning5"
image bg ch6morning6 = "ch6morning6"
image bg ch6morning7 = "ch6morning7"
image bg ch6morning8 = "ch6morning8"
image bg ch6morning9 = "ch6morning9"
image bg ch6morning10 = "ch6morning10"
image bg ch6morning11 = "ch6morning11"
image bg ch6morning12 = "ch6morning12"
image bg ch6morning13 = "ch6morning13"
image bg ch6morning14 = "ch6morning14"
image bg ch6morning15 = "ch6morning15"
image bg ch6morning16 = "ch6morning16"
image bg ch6morning17 = "ch6morning17"
image bg ch6morning18 = "ch6morning18"
image bg ch6morning19 = "ch6morning19"
image bg ch6morning20 = "ch6morning20"
image bg ch6morning21 = "ch6morning21"
image bg ch6morning22 = "ch6morning22"
image bg ch6morning23 = "ch6morning23"
image bg ch6morning24 = "ch6morning24"
image bg ch6morning25 = "ch6morning25"
image bg ch6morning26 = "ch6morning26"
image bg ch6morning27 = "ch6morning27"
image bg ch6morning28 = "ch6morning28"
image bg ch6morning29 = "ch6morning29"
image bg ch6morning30 = "ch6morning30"
image bg ch6morning31 = "ch6morning31"
image bg ch6morning32 = "ch6morning32"
image bg ch6morning33 = "ch6morning33"
image bg ch6morning34 = "ch6morning34"





label ch6morning:

    scene black with Dissolve(1)
    show bg ch6morning32 with Dissolve(1)
    p "(I don't think this day could have gone any worse...)"
    p "Lights..."
    show bg ch6morning33 with Dissolve(1)
    scene black with Dissolve(3)
    play music audio.darkcalm fadein 2.0 fadeout 2.0
    call ch6sonjabath from _call_ch6sonjabath
    scene black with Dissolve(2)
    play music audio.calm fadein 2.0 fadeout 2.0
    p "..."
    p "..."
    "Up!"
    p "(what the hell?)"
    ve " Wake up!"
    show bg ch6morning28
    p "GAH!"
    if "ch6venusbroken" in extraevents:
        p "Christ, it's shit like this that gets you flung across a room!"
    else:
        p "Christ, you need to try and be less creepy."
    show bg ch6morning30 with dissolve
    ve "Good Morning! Betty wanted to talk to you!"
    p "Yeah, I remember."
    show bg ch6morning29 with dissolve
    ve "Mr. Gibson is on his way."
    p "Him too? Alright. I'll be right down."
    if "ch6venusbroken" in extraevents:
        show bg ch6morning31 with dissolve
        ve "Thank you! I hope you have a good m--- fuck me against the wall and break my slutty ass!"
        ve "--orning."
        show bg ch6morning29 with dissolve
        p "Ooookay."
        p "(Betty is certainly going to notice that.)"
        $ achievement.grant("GLITCHED")
        init:
            $ achievement.register("GLITCHED")
        $ achievement.Sync()
    else:

        ve "Thank you! I hope you have a good morning!"
    show bg ch6morning1 with dissolve
    p "(Let's see what Betty needs, I hope it isn't something too weird.)"
    show bg ch6morning2 with dissolve
    p "Henry!"
    show bg ch6morning3 with dissolve
    h "Morning."
    p "You're not going to puke on me, are you?"
    h "Probably not. I haven't eaten yet."
    p "That's good."
    show bg ch6morning4 with dissolve
    p "Because you look like shit."
    h "You don't look so hot yourself."
    p "Doubt I have a shiner like that though. Jesus."
    h "Looks worse than it is."
    p "How is it that you're bulletproof and you can still swell up like that?"
    show bg ch6morning5 with dissolve
    h "That Red Moon hit pretty hard."
    p "Yeah, no shit."
    p "Hell, I'm still feeling that this morning."
    h "You and me both."
    p "Wish Betty would have given me some more time to sleep though."
    show bg ch6morning6 with dissolve
    h "I was already up."
    p "Did you sleep at all?"
    h "Enough."
    p "So that's a no."
    show bg ch6morning7 with dissolve
    h "It's enough. I only need about half the rest you do. Besides, how can you sleep in a place like this?"
    p "If you say so."
    show bg ch6morning8 with Dissolve(1)
    b "Good morning, [p]... Sexy."
    h "Uh, morning."
    p "Morning, Betty."
    show bg ch6morning9 with dissolve
    b "Take a seat both of you."
    p "Uh, Betty?"
    b "What?"
    show bg ch6morning18 with dissolve
    p "There's only one seat."
    show bg ch6morning17 with dissolve
    b "It's a love seat, it fits two."
    h "I..."
    show bg ch6morning10 with dissolve
    b "Don't worry sweetheart, if [p] puts the moves on you, I'll protect you."
    show bg ch6morning19 with dissolve
    h "Thanks?"
    b "Go ahead make yourselves comfortable."
    show bg ch6morning25 with dissolve
    b "See? There we go!"
    show bg ch6morning20 with dissolve
    h "Uh..."
    p "What?"
    h "Why {i}are{/i} you wearing that mask?"
    show bg ch6morning26 with dissolve
    if "ch6katietease" in extraevents:
        p "Henry, we've fought, crawled through a sewer, you've puked on Katie-"
    else:
        p "Henry, we've fought, crawled through a sewer, you've puked on me-"
    h "And I haven't showered..."
    p "And you haven't showered."
    b "Are you boys done?"
    show bg ch6morning27 with dissolve
    "You and Henry" "Yeah."
    b "Good."
    show bg ch6morning11 with dissolve
    b "Now, I brought you two here so we can discuss payment."
    h "However much you need..."
    b "Not money, dear. Well, not now."
    b "I have a small mission for you."
    show bg ch6morning12 with dissolve
    $ renpy.pause(1)
    show bg ch6morning13 with dissolve
    b "This man here is Glenn Dewars. A regular of mine."
    b "Now, what I need the two of you to do..."
    show bg ch6morning21 with dissolve
    h "If you need us to strong-arm a payment, just let me cover his debts. I'm not a thug."
    show bg ch6morning15 with dissolve
    b "Oh, sweetheart, that's adorable. No, he doesn't owe me anything, but I do need his assistance with Venus."
    p "So where do we come in, why not just call him up?"
    show bg ch6morning16 with dissolve
    b "If you two will let me finish. Glenn spends most of his time off the grid."
    p "Betty, no offense, but if you don't know where this guy is, no way in hell can we find him before you."
    b "Oh no, I know exactly where he is."
    h "Then what do you need?"
    b "I need you to kidnap him for me."
    show bg ch6morning22 with dissolve
    h "..."
    h "*Sighs*"
    show bg ch6morning23 with dissolve
    h "Yeah, okay. At this point, why does this not surprise me?"
    show bg ch6morning14 with dissolve
    if not persistent.glos_sculptor:
        $ persistent.glos_sculptor = True
        $ renpy.notify(['Glossary Updated', 'glossary'])
    b "He can help Venus, but he can also help Gloria. He's one of the best {color=#359eff}sculptors{/color} out there."
    show bg ch6morning24 with dissolve

    h "*Under his breath* Psst, [p], what's a sculptor?"
    p "They rig up DNA profiles and do identity swaps and shit."
    h "That could be useful."
    show bg ch6morning14 with dissolve
    b "Well, right now a couple of Bolters grabbed him. Probably trying to get a new profile for one of their own."
    b "I got camera feeds all the way to the spot they are holding him."
    show bg ch6morning27 with dissolve
    h "Bolters..."
    p "Always fucking Bolters."
    p "Are they far? No vehicle makes things tough."
    show bg ch6morning16 with dissolve
    b "Oh, honey. That's already taken care of."
    p "Betty, you are in the wrong line of work. Thank you!"
    p "Now, fill Henry in on the location. I'll go let Katie know what's happening."
    jump ch6gloriamorning
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
