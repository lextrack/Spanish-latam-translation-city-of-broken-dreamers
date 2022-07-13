
image bg ch3montage1 = "ch3montage1"
image bg ch3montage2 = "ch3montage2"
image bg ch3montage3 = "ch3montage3"
image bg ch3montage4 = "ch3montage4"
image bg ch3montage5 = "ch3montage5"
image bg ch3montage6 = "ch3montage6"
image bg ch3montage7 = "ch3montage7"
image bg ch3montage8 = "ch3montage8"
image bg ch3montage9 = "ch3montage9"
image bg ch3montage10 = "ch3montage10"
image bg ch3montage11 = "ch3montage11"
image bg ch3montage12 = "ch3montage12"
image bg ch3montage13 = "ch3montage13"
image bg ch3montage14 = "ch3montage14"
image bg ch3montage15 = "ch3montage15"
image bg ch3montage16 = "ch3montage16"
image bg ch3montage17 = "ch3montage17"
image bg ch3montage18 = "ch3montage18"
image bg ch3montage19 = "ch3montage19"
image bg ch3montage20 = "ch3montage20"
image bg ch3montage21 = "ch3montage21"
image bg ch3montage22 = "ch3montage22"
image bg ch3montage23 = "ch3montage23"
image bg ch3montage24 = "ch3montage24"
image bg ch3montage25 = "ch3montage25"
image bg ch3montage26 = "ch3montage26"
image bg ch3montage27 = "ch3montage27"
image bg ch3montage28 = "ch3montage28"
image bg ch3montage29 = "ch3montage29"
image bg ch3montage30 = "ch3montage30"
image bg ch3montage31 = "ch3montage31"
image bg ch3montage32 = "ch3montage32"
image bg ch3montage33 = "ch3montage33"
image bg ch3montage34 = "ch3montage34"
image bg ch3montage35 = "ch3montage35"
image bg ch3montage36 = "ch3montage36"
image bg ch3montage37 = "ch3montage37"
image bg ch3montage38 = "ch3montage38"
image bg ch3montage39 = "ch3montage39"
image bg ch3montage40 = "ch3montage40"
image bg ch3montage41 = "ch3montage41"
image bg ch3montage42 = "ch3montage42"
image bg ch3montage43 = "ch3montage43"
image bg ch3montage44 = "ch3montage44"
image bg ch3montage45 = "ch3montage45"
image bg ch3montage46 = "ch3montage46"
image bg ch3montage47 = "ch3montage47"
image bg ch3montage48 = "ch3montage48"
image bg ch3montage49 = "ch3montage49"
image bg ch3montage50 = "ch3montage50"
image bg ch3montage51 = "ch3montage51"
image bg ch3montage52 = "ch3montage52"
image bg ch3montage53 = "ch3montage53"
image bg ch3montage54 = "ch3montage54"
image bg ch3montage55 = "ch3montage55"
image bg ch3montage56 = "ch3montage56"
image bg ch3montage57 = "ch3montage57"
image bg ch3montage58 = "ch3montage58"
image bg ch3montage59 = "ch3montage59"
image bg ch3montage60 = "ch3montage60"


image bg ch3vicwatch5 = "ch3vicwatch5"
image bg ch3vicwatch6 = "ch3vicwatch6"


image ch3drive1mov = Movie(play='video/chapter-3-video/ch3drive1.webm', loop=False)
image bg ch3drive1movie movie:
    "ch3drive1mov"
    pause 11.0
    "black"

image ch3drive2mov = Movie(play='video/chapter-3-video/ch3drive2.webm', loop=False)
image bg ch3drive2movie movie:
    "ch3drive2mov"
    pause 12.0
    "black"

image ch3drive3mov = Movie(play='video/chapter-3-video/ch3drive3.webm', loop=False)
image bg ch3drive3movie movie:
    "ch3drive3mov"
    pause 10.0
    "black"





label ch3montage:
    play music audio.burningstars fadein 14.0 fadeout 3.0
    if "ch3findbug" in extraevents:
        menu:
            "Disable Bug":
                $ extraevents.append("ch3disablebug")
                p "(While I'm at it.)"
            "Leave it":
                p "(I'll let you watch for now.)"


    show bg ch3montage1 with dissolve
    $ renpy.pause(1)
    show bg ch3montage2 with dissolve
    $ renpy.pause(1)
    if "ch3disablebug" in extraevents:
        show bg ch3montage3 with dissolve
        p "(Show's over, Victoria.)"
        show bg ch3vicwatch6 with dissolve
        v "Dammit..."
    else:
        show bg ch3vicwatch5 with dissolve
        v "Yes Ma'am, he is getting ready now."
    window hide
    show bg ch3montage4 with dissolve
    $ renpy.pause(1)
    show bg ch3montage5 with dissolve
    $ renpy.pause(1)
    show bg ch3montage6
    $ renpy.pause(1)
    show bg ch3montage7
    $ renpy.pause(1)
    show bg ch3montage8
    $ renpy.pause(1)
    show bg ch3montage9
    $ renpy.pause(1)
    show bg ch3montage10
    $ renpy.pause(1)
    show bg ch3montage11 with dissolve
    window show
    p "(Back in the fray)"
    window hide
    show bg ch3montage12 with Dissolve(2)
    $ renpy.pause(1)
    show bg ch3montage13 with Dissolve(2)
    $ renpy.pause(1)

    scene black with Dissolve(3)
    show bg ch3montage34 with Dissolve(3)
    $ renpy.pause(2)
    show bg ch3montage35 with dissolve
    $ renpy.pause(2)
    if "ch2inviteellen" in extraevents:
        show bg ch3montage36 with dissolve
    else:
        show bg ch3montage37 with dissolve

    $ renpy.pause(1)
    scene black with Dissolve(3)
    show bg ch3montage15 with Dissolve(3)
    $ renpy.pause(1)
    show bg ch3montage16 with dissolve
    $ renpy.pause(2)
    show bg ch3montage17 with dissolve
    $ renpy.pause(2)
    show bg ch3montage18 with dissolve
    $ renpy.pause(1)
    show bg ch3montage19 with dissolve
    $ renpy.pause(1)
    show bg ch3montage20 with dissolve
    $ renpy.pause(1)
    show bg ch3montage21 with dissolve
    $ renpy.pause(1)
    show bg ch3drive1movie movie with dissolve
    scene black with Dissolve(3)
    show bg ch3montage22 with Dissolve(3)
    "Recruiter" "Now, any of you misfits have a clue where this girl is?"
    show bg ch3montage23 with dissolve
    $ renpy.pause(2)
    show bg ch3montage24 with dissolve
    j "Not in the faintest."
    show bg ch3drive2movie movie with Dissolve(2)
    $ renpy.pause(12)

    show bg ch3montage25 with Dissolve(3)
    $ renpy.pause(2)
    if k_score >= 3:
        show bg ch3montage27 with dissolve
        k "This whole thing is insane. This is bigger than he thinks. I just know it."
    else:
        show bg ch3montage26 with dissolve
        k "There is something more to this. I just wish I could explain it."
    show bg ch3montage29 with dissolve
    $ renpy.pause(2)
    show bg ch3montage28 with dissolve
    k "Of course, sticking my nose where it didn't belong is what got me here in the first place."
    k "But, I was always taught to find the truth, so I wouldn't have it any other way."
    if k_score >= 3:
        k "Be safe out there, [pf]..."
    else:
        k "Though, I have a bad feeling about all this."

    show bg ch3drive3movie movie with Dissolve(1)
    $ renpy.pause(10)

    show bg ch3montage31 with Dissolve(3)
    $ renpy.pause(4)
    show bg ch3montage32 with Dissolve(2)
    $ renpy.pause(2)
    if v_score >= 2:
        show bg ch3montage33 with Dissolve(2)
    else:
        show bg ch3montage30 with Dissolve(2)

    $ renpy.pause(2)
    scene black with Dissolve(3)

    show bg ch3montage43 with Dissolve(2)
    $ renpy.pause(2)
    show bg ch3montage44 with Dissolve(1)
    $ renpy.pause(2)
    show bg ch3montage45 with Dissolve(1)
    $ renpy.pause(3)

    $ renpy.music.set_volume(0.2, 3.0, 'music')

    scene black with Dissolve(3)
    show bg ch3montage38 with Dissolve(3)
    h "*Snoring*"
    show bg ch3montage39 with dissolve
    g "Henry? Are you awake?"
    h "*Continues to snore*"
    show bg ch3montage40 with dissolve
    g "Bigs! Wake up!"
    h "*Grumbles*"
    show bg ch3montage41 with dissolve
    h "Gloria, what's the matter? It's early. Another nightmare?"
    g "It's not that."
    show bg ch3montage42 with dissolve
    g "The one I told you about. In my dream...{w} He's here."
    $ renpy.music.set_volume(1, 3.0, 'music')
    jump ch4start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
