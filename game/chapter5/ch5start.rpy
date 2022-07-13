

image bg ch5drive1 = "ch5drive1"
image bg ch5drive2 = "ch5drive2"
image bg ch5drive3 = "ch5drive3"
image bg ch5drive4 = "ch5drive4"
image bg ch5drive5 = "ch5drive5"
image bg ch5drive6 = "ch5drive6"
image bg ch5drive7 = "ch5drive7"
image bg ch5drive8 = "ch5drive8"
image bg ch5drive9 = "ch5drive9"
image bg ch5drive10 = "ch5drive10"
image bg ch5drive11 = "ch5drive11"
image bg ch5drive12 = "ch5drive12"


image ch5driving = Movie(play='video/chapter-5-video/ch5driving.webm', loop=False)
image bg ch5drivingmovie movie:
    "ch5driving"
    pause 10.0
    "ch5drivingend"



image bg ch5intro:
    "ch5intro"
    yalign 0.5
    zoom 1
    alpha 1.0
    pause 1.0
    easeout 3.0 zoom 1.5 alpha 0.0


image bg chapter5 movie = Movie(play='video/intros/chapter5.webm')



label ch5start:
    stop music fadeout 2.0
    scene black with Dissolve(2)
    show bg chapter5 movie with dissolve
    $ renpy.pause(2.9)

    play music audio.space fadein 2.0

    scene black with Dissolve(2)
    show bg ch5drive12 with dissolve
    p "Well, that was... Well, something. Sam, time to go home."
    s "Home, Sir? Do you think that wise?"
    p "Shit, sorry. Ellen's loft or whatever it is. Home's off-limits for now. How did this get so fucked up?"
    s "Would you like an unabridged retelling or the simple one?"
    show bg ch5drive10 with dissolve
    p "Shut it, Sam."
    show bg ch5drivingmovie movie with dissolve
    s "You have a message, Sir."
    p "I told you to cut me off the comms grid."
    s "I did. And yet, the call still arrived."
    show bg ch5drive11 with dissolve
    $ extraevents.append("ch5answer")
    p "Play the message, Sam."
    s "Yes, sir."
    n "The voice that plays back is distorted"
    "???" "Agent, [pl]. You don't know me, but we have a friend in common. One who is a little confused by what you are up to."
    "Kay" "My name's Kay. You might've heard of me."
    p "(Sonja's AI?)"
    "Kay" "A mutual friend wanted us to talk about... Stuff."
    "Kay" "And uh, that's about it. I don't want to talk more on open comms. Well, encrypted comms, but just show up, okay?"
    "Kay" "The meet is where you \"broke into hives.\" Hope that means something to you."
    "Kay" "I understand if you don't show up, but I'll be here until oh-two-hundred."
    n "The message ends"
    p "Sam, what the fuck? Kay is real, why didn't you tell me?"
    s "You never asked."
    p "Maybe be a little more forthcoming in the future."
    s "Of course. Also, Hives, sir?"
    p "I trusted some oysters I shouldn't have. Let's leave it at that."

    p "Any other messages?"
    s "You have seventeen from Baynard Industries."
    p "Trash 'em."
    s "Done, Sir. Off to Ms. Lane's hideout then?"
    if "ch5answer" in extraevents:
        p "Actually... Meredith's place is close by, same with the meetup with Kay."
    else:
        p "Actually... Meredith's place is close by."
    jump ch5locationmenu



label ch5locationmenu:
    menu:
        "Visit Meredith's home" if "ch5visitchandra" not in extraevents:
            $ extraevents.append("ch5visitchandra")
            p "You know, the queen bitch lives right around here."
            s "Ms. White's, then?"
            p "Yeah."
            scene black with Dissolve(2)
            show bg ch5drive1 with Dissolve(2)
            p "Place hasn't changed a bit. Now to find a way in."

            if "ch3chandrapissed" not in extraevents:
                jump ch5meredithsgood
            else:
                jump ch5meredithsbad
        "Meet Kay" if "ch5answer" in extraevents and "ch5visitkay" not in extraevents:
            $ extraevents.append("ch5visitkay")
            p "Might as well see what this Kay wants."
            p "Let's head to the Happy Clam."
            jump ch5kay

        "Check on Doc" if "ch5visitdoc" not in extraevents:
            $ extraevents.append("ch5visitdoc")
            p "Katie is probably pissed... Maybe I could make some peace with her."
            jump ch5doc
        "Back to Ellen's":

            p "Let's just get back. I don't want to piss Henry off."
            jump ch5ellen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
