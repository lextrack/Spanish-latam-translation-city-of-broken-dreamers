
image bg ch3wake1 = "ch3wake1"
image bg ch3wake2 = "ch3wake2"
image bg ch3wake3 = "ch3wake3"


image bg chapter3 movie = Movie(play='video/intros/chapter3.webm')



label ch3wake:
    stop music fadeout 2.0
    scene black with Dissolve(2)
    show bg chapter3 movie with dissolve
    $ renpy.pause(2.9)
    show bg ch3wake1 with dissolve
    p "Mother fuck!"
    show bg ch3wake2 with dissolve
    "Robo Cab" "Please watch your language, Sir."
    if dep >= 2:
        p "Oh, fuck off, You're gonna bitch about me swearing in my sleep?"
        "Robo Cab" "There will be an additional 5%% fee assessed for abuse of your virtual driver. If you have any concerns about this fee please send your complaints to..."
        p "I'll pay it... just shut the fuck up."
    else:
        p "Unintentional, I was having a nightmare."
        "Robo Cab" "Understood, Sir. You should try Euphorirem from Baynard Industries. Better dreams are guaranteed."
        p "I'll keep that in mind. Hey, we almost there?"
    show bg ch3wake3 with dissolve
    "Robo Cab" "Yes Sir, approaching the residence of a Sonja [pl]."
    p "Perfect, this time I get to interrupt her."
    jump ch3sonja
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
