
image bg ch3dream1 = "ch3dream1"
image bg ch3dream2 = "ch3dream2"
image bg ch3dream3 = "ch3dream3"
image bg ch3dream4 = "ch3dream4"
image bg ch3dream5 = "ch3dream5"

image ch3dreammovie = Movie(play='video/chapter-3-video/ch3dream.webm', loop=False)
image bg ch3dreammov movie:
    "ch3dreammovie"
    pause 7.0
    "ch3dream"


label ch3sleep:
    scene black with Dissolve(3)
    stop music fadeout 2.0
    show bg ch2dream1 with dissolve
    p "There has to be something. We can do something else... anything."
    show bg ch2dream2 with dissolve
    p "God DAMN you, Meredith!"
    n "Crying can be heard up ahead."
    show bg ch3dream1 with dissolve
    j "My god..."
    n "Both Sonja's and your coms begin to erupt in static-filled chatter."
    m "Agents, the asset is out of control. We have forty seven dead and that's just so far! You know what you have to do."
    show bg ch3dream2 with dissolve
    j "[p], over there."
    show bg ch3dream3 with dissolve
    p "Stick close..."
    show bg ch3dream4 with dissolve
    "Child" "*Whimpering*"
    j "I can't..."
    show bg ch3dreammov movie with dissolve
    p "Why are you-?"
    g "It's you? Who are you!?"
    show bg ch3report28 with dissolve
    p "FUCK ME! What in the!?"
    s "Sir, you need to get up."
    p "I'm up! I'm up! Sam, how long was I out?"
    show bg ch3report30 with dissolve
    s "Forty-two minutes, Sir. I've been trying to wake you for the last fourteen."
    p "Shit, call Sonja. Time to do this."
    show bg ch3report31 with dissolve
    s "Calling Sonja [pl]..."
    p "..."
    p "Come on, Sonja, pick up..."
    p "Where the hell are you? Dammit..."
    p "Sonja, you got the call, didn't you..?"
    p "Sam, looks like we are doing this on our own."
    s "Is that wise, Sir?"
    p "Don't have a choice. Time to get ready."
    jump ch3montage
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
