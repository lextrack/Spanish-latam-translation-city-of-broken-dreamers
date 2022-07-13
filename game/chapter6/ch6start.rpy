



image bg ch6start1 = "ch6start1"
image bg ch6start2 = "ch6start2"
image bg ch6start3 = "ch6start3"
image bg ch6start4 = "ch6start4"
image bg ch6start5 = "ch6start5"
image bg ch6start6 = "ch6start6"
image bg ch6start7 = "ch6start7"
image bg ch6start8 = "ch6start8"
image bg ch6start9 = "ch6start9"
image bg ch6start10 = "ch6start10"
image bg ch6start11 = "ch6start11"
image bg ch6start12 = "ch6start12"
image bg ch6start13 = "ch6start13"

image bg ch6intro:
    "ch6intro"
    yalign 0.5
    zoom 1
    alpha 1.0
    pause 1.0
    easeout 3.0 zoom 1.5 alpha 0.0




image bg chapter6 movie = Movie(play='video/intros/chapter6.webm')


label ch6start:

    stop music fadeout 2.0
    scene black with Dissolve(2)
    show bg chapter6 movie with dissolve
    $ renpy.pause(2.9)
    show bg ch6start1 with dissolve
    play music audio.stress fadein 8.0 fadeout 2.0
    h "[p], why are we back in Lakewood?"
    p "I'll tell you, but you won't like it."
    h "Why?"
    show bg ch6start2 with dissolve
    p "Two reasons, one it's not exactly a high-class place."
    h "You saw my old apartment right?"
    p "I said two reasons. Second one is the owner, she's not..."
    show bg ch6start3 with dissolve
    h "Not what?"
    p "Completely sane."
    show bg ch6start4 with dissolve
    h "Sounds like we'll fit right in."
    menu:
        "No jokes. Not now.":
            $ extraevents.append("ch6henryjoke")
            show bg ch6start5 with dissolve
            p "Can we not joke, not now. Not after..."
            h "Sorry."
            p "Yeah."
            show bg ch6start6 with dissolve
            h "Look, I know it's hard, but you have to find a way to move forward."
            if "ch5ellenkiss" in extraevents:
                p "She's dead. Maybe it should get to me."
                h "I've lost friends too. I understand. But you-."
                show bg ch6start5 with dissolve
                p "You think I don't fucking know that? Just can it!"
                h "Alright, sorry."
                p "Thank you."
            else:
                show bg ch6start5 with dissolve
                p "I know, but it still isn't something I can get used to."
                h "We aren't meant to get used to it. We're meant to wear its burden on our shoulders."
                p "I thought I left this shit behind. But seems like karma won't let me."
                h "Don't I know it."
        "Probably":
            show bg ch6start5 with dissolve
            p "We're a ragtag group of fuck ups. So you're probably right."
            show bg ch6start7 with dissolve
            h "She won't mind us dropping in?"
            p "Oh, she'll mind. A lot. But she'll help."
            h "Sounds like, El-"
            p "... yeah."

    if "chellendrink" in extraevents:
        show bg ch6start8 with dissolve
        p "Let's get a move on. I could use a drink."
        h "Me too."
    else:
        show bg ch6start8 with dissolve
        p "Let's get a move on."
        h "Alright, we could use a break."

    show bg ch6start11 with dissolve
    n "The sounds of commotion can be heard coming from down the street"
    show bg ch6start10 with dissolve
    h "Riots are still on."
    show bg ch6start9 with dissolve
    p "Best news we could hope for. If the cops have to deal with them, less resources they have to find us."
    h "And we'll be harder to track."
    scene black with Dissolve(2)
    p "Okay, just down here."
    show bg ch6start12 with Dissolve(2)
    h "What is this place?"
    show bg ch6start13 with dissolve
    h "The Stairway to Heaven? You're kidding, right?"
    p "Nope."
    jump ch6stairway
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
