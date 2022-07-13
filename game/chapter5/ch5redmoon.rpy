image bg ch5red1 = "ch5red1"
image bg ch5red2 = "ch5red2"
image bg ch5red3 = "ch5red3"
image bg ch5red4 = "ch5red4"
image bg ch5red5 = "ch5red5"
image bg ch5red6 = "ch5red6"
image bg ch5red7 = "ch5red7"
image bg ch5red8 = "ch5red8"
image bg ch5red9 = "ch5red9"
image bg ch5red10 = "ch5red10"
image bg ch5red11 = "ch5red11"
image bg ch5red12 = "ch5red12"
image bg ch5red13 = "ch5red13"
image bg ch5red14 = "ch5red14"
image bg ch5red15 = "ch5red15"
image bg ch5red16 = "ch5red16"
image bg ch5red17 = "ch5red17"
image bg ch5red18 = "ch5red18"
image bg ch5red19 = "ch5red19"
image bg ch5red20 = "ch5red20"
image bg ch5red21 = "ch5red21"
image bg ch5red22 = "ch5red22"
image bg ch5red23 = "ch5red23"
image bg ch5red24 = "ch5red24"
image bg ch5red25 = "ch5red25"
image bg ch5red26 = "ch5red26"
image bg ch5red27 = "ch5red27"
image bg ch5red28 = "ch5red28"
image bg ch5red29 = "ch5red29"
image bg ch5red30 = "ch5red30"
image bg ch5red31 = "ch5red31"
image bg ch5red32 = "ch5red32"
image bg ch5red33 = "ch5red33"
image bg ch5red34 = "ch5red34"
image bg ch5red35 = "ch5red35"
image bg ch5red36 = "ch5red36"
image bg ch5red37 = "ch5red37"
image bg ch5red38 = "ch5red38"
image bg ch5red39 = "ch5red39"
image bg ch5red40 = "ch5red40"
image bg ch5red41 = "ch5red41"
image bg ch5red42 = "ch5red42"
image bg ch5red43 = "ch5red43"
image bg ch5red44 = "ch5red44"
image bg ch5red45 = "ch5red45"
image bg ch5red46 = "ch5red46"
image bg ch5red47 = "ch5red47"
image bg ch5red48 = "ch5red48"
image bg ch5red49 = "ch5red49"
image bg ch5red50 = "ch5red50"
image bg ch5red51 = "ch5red51"
image bg ch5red52 = "ch5red52"
image bg ch5red53 = "ch5red53"
image bg ch5red54 = "ch5red54"
image bg ch5red55 = "ch5red55"
image bg ch5red56 = "ch5red56"
image bg ch5red57 = "ch5red57"
image bg ch5red58 = "ch5red58"
image bg ch5red59 = "ch5red59"
image bg ch5red60 = "ch5red60"
image bg ch5red61 = "ch5red61"
image bg ch5red62 = "ch5red62"
image bg ch5red63 = "ch5red63"
image bg ch5red64 = "ch5red64"
image bg ch5red65 = "ch5red65"
image bg ch5red66 = "ch5red66"
image bg ch5red67 = "ch5red67"
image bg ch5red68 = "ch5red68"
image bg ch5red69 = "ch5red69"
image bg ch5red70 = "ch5red70"
image bg ch5red71 = "ch5red71"


image ch5redmoon = Movie(play='video/chapter-5-video/ch5redmoon.webm', loop=False)
image bg ch5redmoonpmovie movie:
    "ch5redmoon"
    pause 7.0
    "ch5redmoonend"

image ch5shooting = Movie(play='video/chapter-5-video/ch5shooting_1.webm', loop=False)
image bg ch5shootingpmovie movie:
    "ch5shooting"
    pause 10.0
    "ch5shootingend"

image ch5train = Movie(play='video/chapter-5-video/ch5train.webm', loop=False)
image bg ch5trainmovie movie:
    "ch5train"
    pause 10.0
    "ch5trainend"


image bg ch5redmoonflash:
    "ch5red27"
    pause 0.01
    "ch5red28"
    pause 0.01
    "ch5red28"
    pause 0.01
    "ch5red28"
    pause 0.03
    "ch5red28"
    pause 0.01
    "ch5red28"
    pause 0.02
    "ch5red28"
    pause 0.01
    "ch5red28"
    repeat

label ch5redmoon:
    scene black with Dissolve(2)
    show bg ch5red12 with Dissolve(1)
    p "Come on, hurry."
    show bg ch5red9 with dissolve
    e "Damn, all this time and I have never come down here."
    g "Where are we?"
    p "The tram tunnels."
    show bg ch5red8 with dissolve
    g "Are they going to follow us down here?"
    p "Certainly, but we have a bit of a head start on them. Best thing they-"
    show bg ch5red5 with dissolve
    h "SHH! Quiet..."
    g "Bigs whats the matter?"
    show bg ch5red6 with dissolve
    if h_score > 2:
        h "Whatever happens, I need you to keep Gloria safe for me."
        p "What are you talking about? Let's just get out of here."
        h "Keep her safe..."
    else:
        h "I don't trust you, Ghost. But, right now I have no choice. Keep Gloria safe."
        p "What the fuck are you talking about? Get a move on."
        h "I beg you, one soldier to another."
    show bg ch5red7 with dissolve
    g "Henry, you're scaring me."
    h "I know, princess..."
    show bg ch5red9 with dissolve
    e "[p], I don't know what he is on about, but we need to leave. Now!"
    show bg ch5red10 with dissolve
    g "HENRY!"
    show bg ch5red3 with vpunch
    n "The echo of metal on metal reverberates across the pedway as an unknown figure lands onto its cold surface"
    play music audio.redmoon fadein 8.0 fadeout 2.0

    show bg ch5redmoonpmovie movie with dissolve
    h "You need to run!"
    e "What the hell is that?"
    p "A Red Moon!{w} We're fucked..."
    show bg ch5red1 with dissolve
    $ renpy.pause(1)
    show bg ch5red2 with dissolve
    h "Get them out of here, [p]."
    h "It's time to face my past."
    show bg ch5red11 with dissolve
    g "HENRY! NO!"
    n "The behemoth charges down the pedway, leaving you behind"
    show bg ch5red12 with dissolve
    $ renpy.pause(0.5)
    show bg ch5red13 with dissolve
    $ renpy.pause(0.5)
    show bg ch5red14 with dissolve
    $ renpy.pause(0.5)
    play sound audio.metalpunch
    show bg ch5red15 with hpunch
    n "The unknown entity's fist strikes Henry across the face with the force of a sledgehammer"
    show bg ch5red16 with dissolve
    h "*Grunts in pain from the powerful blow*"
    show bg ch5red17 with dissolve
    h "What are you waiting for? Go!"
    h "If you want revenge, you bastard, take it!"
    show bg ch5red18 with dissolve
    p "Henry, get up!"
    show bg ch5shootingpmovie movie with dissolve
    h "COME ON! JUST FINISH IT!"
    p "Why the hell is everything bulletproof?"
    show bg ch5red19 with dissolve
    p "Ah, shit..."
    show bg ch5red20 with dissolve
    $ renpy.pause(1)
    show bg ch5red21 with dissolve
    $ renpy.pause(1)
    play sound audio.metalcrash
    show bg ch5red22 with dissolve
    $ renpy.pause(1)
    show bg ch5red23 with dissolve
    h "Arrogant as always!"
    show bg ch5red25 with dissolve
    h "Some."
    play sound audio.metalpunch
    show bg ch5red24 with vpunch
    h "Things."
    show bg ch5red26 with vpunch
    h "Never."
    play sound audio.metalpunch
    show bg ch5red24 with vpunch
    h "CHANGE!"
    show bg ch5red27 with hpunch
    n "Hurled into the bars, other than the echo of metal on metal, the Red Moon makes no sound"
    show bg ch5red29 with dissolve
    h "Go! Get across. I'll keep this one busy for awhile."
    p "But we-"
    h "Just go! Hurry!"
    show bg ch5red32 with dissolve
    p "Come on, guys, let's go!"
    g "But!"
    p "No time, just go!"
    show bg ch5redmoonflash with dissolve
    h "Remember, keep her safe..."
    p "I will."
    show bg ch5red33 with dissolve
    h "Arggh!"
    h "GO!"
    show bg ch5red31 with dissolve
    g "We can't leave him!"
    p "Ellen, take her and go!"
    show bg ch5red30 with dissolve
    e "*Grimmaces as she tugs on Gloria* Gloria, please! We can't stay here!"
    g "*Chokes up* No, I won't leave him!"
    show bg ch5red35 with dissolve
    $ renpy.pause(0.5)
    show bg ch5red34 with dissolve
    n "Under repeated blows, Henry begins to fall back"
    show bg ch5red36 with dissolve
    h "*Coughs* Gloria..."
    p "Henry, fight back!"
    show bg ch5red38 with dissolve
    "Red Moon" "Join your fallen."
    g "HENRY!"
    play sound audio.metalpunch
    show bg ch5red37 with hpunch
    $ renpy.pause(0.5)
    show bg ch5red39 with dissolve
    n "Henry's body goes limp as the red of his limiter dulls to black"
    p "MOTHER FUCKER!"
    play sound audio.smg
    show bg ch5red40
    $ renpy.pause(0.5)
    show bg ch5red41 with dissolve
    p "Gloria, please... Go with Ellen."
    n "As your bullets bounce off the Red Moon, his focus turns towards you. Behind him, Henry lays still."
    show bg ch5red43 with dissolve
    e "Gloria, look at me. I'm begging you, we have to leave!"
    show bg ch5red44 with dissolve
    g "I can't..."
    e "What on earth?"
    show bg ch5red42 with dissolve
    p "No, Gloria! Not here! Ellen, get away from her!"
    show bg ch5red46 with dissolve
    e "[p]! What's she-"
    play sound audio.emp
    show bg ch5red47 with quickflash
    $ renpy.pause(1)
    show bg ch5red48 with dissolve
    $ renpy.pause(0.5)
    show bg ch5red49 with dissolve
    scene black with Dissolve(3)
    stop music fadeout 3.0

    p "..."
    p "..."
    e "[p]..."
    e "[p]... *struggling* Please get up... *sniffs*"
    e "[p]! Get up!"
    show bg ch5red50 with dissolve
    p "Ellen!"
    p "Fuck, hold on!"
    show bg ch5red51 with dissolve
    e "[p], I-I can't... please."
    n "A sharp pain rips through your back as you try to move towards Ellen"
    show bg ch5red52 with dissolve
    e "Aghh! Don't blame her!"
    show bg ch5red53 with dissolve
    p "ELLEN!"
    p "..."
    p "Ellen..."
    show bg ch5red54 with Dissolve(2)
    play music audio.worried fadein 3.0
    if "ch4vicaccept" in extraevents:
        p "This is your fault..."
        p "(Why didn't I just take you to, Victoria? Fuck!)"
    else:
        p "Gloria... Goddammit, what have you done?"
        p "(Maybe taking you to Baynard... no...)"


    n "Commotion can be heard from the upstairs"
    show bg ch5red55 with dissolve
    p "*Grimaces in pain* Ah, goddammit..."
    p "You're heavier than you look."
    show bg ch5red56 with dissolve
    $ renpy.pause(0.5)
    show bg ch5red57 with Dissolve(3)
    h "*Ugh...*"
    show bg ch5red58 with dissolve
    h "What happened..?"
    p "Gloria happened, is what..."
    show bg ch5red59 with dissolve
    h "Where is... Did Ellen get out?"
    p "..."
    p "Let's just go..."
    h "[p], I'm sor-"
    p "I don't want to hear it... Stay here, and hold them off, or come with me."
    h "..."
    h "Lead on..."
    scene black with Dissolve(2)
    show bg ch5red64 with Dissolve(2)
    h "[p], slow down... *coughs*"
    show bg ch5trainmovie movie with dissolve
    h "We can go back for her."
    p "I saw her fall."
    h "But..."
    p "I said, I saw her fall!"
    show bg ch5red65 with dissolve
    h "[p], she can't know what happened."
    if dep > 2:
        p "Why not!"
    else:
        p "I know..."
    show bg ch5red66 with dissolve
    if dep > 2:
        h "..."
    else:
        h "And Ellen... She could still be alive."
        p "I wish I knew how..."
    show bg ch5red67 with dissolve
    n "The three continue their way down the tunnel in silence"

    jump ch5redmoonout


label ch5redmoonout:
    scene black with Dissolve(3)
    show bg ch5red61 with Dissolve(3)
    $ renpy.pause(1)
    show bg ch5red60 with Dissolve(2)
    $ renpy.pause(1)
    show bg ch5red62 with Dissolve(1)
    $ renpy.pause(1)
    show bg ch5red63 with Dissolve(1)
    $ renpy.pause(1)
    show bg ch5red68 with Dissolve(1)
    $ renpy.pause(1)
    show bg ch5red69 with Dissolve(1)
    $ renpy.pause(1)
    show bg ch5red70 with Dissolve(1)
    v "What happened?!"
    show bg ch5red71 with Dissolve(1)
    v "Ellen..?"
    jump ch6sonja1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
