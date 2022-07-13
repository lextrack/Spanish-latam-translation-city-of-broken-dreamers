
image bg ch7shanlon1 = "ch7shanlon1"
image bg ch7shanlon2 = "ch7shanlon2"
image bg ch7shanlon3 = "ch7shanlon3"
image bg ch7shanlon4 = "ch7shanlon4"
image bg ch7shanlon5 = "ch7shanlon5"
image bg ch7shanlon6 = "ch7shanlon6"
image bg ch7shanlon7 = "ch7shanlon7"
image bg ch7shanlon8 = "ch7shanlon8"
image bg ch7shanlon9 = "ch7shanlon9"
image bg ch7shanlon10 = "ch7shanlon10"
image bg ch7shanlon11 = "ch7shanlon11"
image bg ch7shanlon12 = "ch7shanlon12"
image bg ch7shanlon13 = "ch7shanlon13"
image bg ch7shanlon14 = "ch7shanlon14"
image bg ch7shanlon15 = "ch7shanlon15"
image bg ch7shanlon16 = "ch7shanlon16"
image bg ch7shanlon17 = "ch7shanlon17"
image bg ch7shanlon18 = "ch7shanlon18"
image bg ch7shanlon19 = "ch7shanlon19"
image bg ch7shanlon20 = "ch7shanlon20"
image bg ch7shanlon21 = "ch7shanlon21"
image bg ch7shanlon22 = "ch7shanlon22"
image bg ch7shanlon23 = "ch7shanlon23"
image bg ch7shanlon24 = "ch7shanlon24"
image bg ch7shanlon25 = "ch7shanlon25"
image bg ch7shanlon26 = "ch7shanlon26"
image bg ch7shanlon27 = "ch7shanlon27"
image bg ch7shanlon28 = "ch7shanlon28"
image bg ch7shanlon29 = "ch7shanlon29"
image bg ch7shanlon30 = "ch7shanlon30"
image bg ch7shanlon31 = "ch7shanlon31"
image bg ch7shanlon32 = "ch7shanlon32"
image bg ch7shanlon33 = "ch7shanlon33"
image bg ch7shanlon34 = "ch7shanlon34"
image bg ch7shanlon35 = "ch7shanlon35"
image bg ch7shanlon36 = "ch7shanlon36"
image bg ch7shanlon37 = "ch7shanlon37"
image bg ch7shanlon38 = "ch7shanlon38"

image bg ch7gloria3 = "ch7gloria3"
image bg ch7gloria4 = "ch7gloria4"
image bg ch7gloria5 = "ch7gloria5"
image bg ch7gloria6 = "ch7gloria6"
image bg ch7gloria7 = "ch7gloria7"
image bg ch7gloria8 = "ch7gloria8"
image bg ch7gloria9 = "ch7gloria9"
image bg ch7gloria10 = "ch7gloria10"
image bg ch7gloria11 = "ch7gloria11"
image bg ch7gloria12 = "ch7gloria12"
image bg ch7gloria13 = "ch7gloria13"
image bg ch7gloria14 = "ch7gloria14"
image bg ch7gloria15 = "ch7gloria15"
image bg ch7gloria16 = "ch7gloria16"
image bg ch7gloria17 = "ch7gloria17"
image bg ch7gloria18 = "ch7gloria18"
image bg ch7gloria19 = "ch7gloria19"


image bg ch7bike1 movie = Movie(play='video/chapter-7-video/ch7bike1.webm', loop=False)
image bg ch7bike2 movie = Movie(play='video/chapter-7-video/ch7bike2.webm', loop=False)
image bg ch7car1 movie = Movie(play='video/chapter-7-video/ch7car1.webm', loop=False)
image bg ch7car2 movie = Movie(play='video/chapter-7-video/ch7car2.webm', loop=False)
image bg ch7car3 movie = Movie(play='video/chapter-7-video/ch7car3.webm', loop=False)
image bg ch7plane1 movie = Movie(play='video/chapter-7-video/ch7plane1.webm', loop=False)
image bg ch7plane2 movie = Movie(play='video/chapter-7-video/ch7plane2.webm', loop=False)
image bg ch7plane3 movie = Movie(play='video/chapter-7-video/ch7plane3.webm', loop=False)
image bg ch7tank1 movie = Movie(play='video/chapter-7-video/ch7tank1.webm', loop=False)
image bg ch7tank2 movie = Movie(play='video/chapter-7-video/ch7tank2.webm', loop=False)
image bg ch7redmoon movie = Movie(play='video/chapter-7-video/ch7redmoon.webm', loop=False)
image bg ch7gloriaexplode movie = Movie(play='video/chapter-7-video/ch7gloriaexplode.webm', loop=False)




image ch7redmoon = Movie(play='video/chapter-7-video/ch7redmoon.webm', loop=False)
image bg ch7redmoon movie:
    "ch7redmoon"
    pause 10.0
    "ch7redmoon-end"

label ch7end:
    play music audio.verycalm fadein 2.0 fadeout 2.0
    scene black with Dissolve(2)
    show bg ch7shanlon38 with dissolve
    sh "Well, well, well."
    show bg ch7shanlon37 with dissolve
    g "Shanlon..."
    sh "Gloria..."
    g "You going to let me in?"
    show bg ch7shanlon1 with dissolve
    sh "This is a surprise. I thought you'd be in custody by now, honestly."
    if "ch2shanlon" in extraevents:
        show bg ch7shanlon3 with dissolve
        $ renpy.pause(1)
        show bg ch7shanlon2 with dissolve
        sh "But where are my manners? Don't stand out there like a wet puppy. Get inside, out of the rain."
        show bg ch7shanlon5 with dissolve
        sh "Shame on you for getting my hopes up, I thought you might be someone else."
        g "Where's Papa?"
        show bg ch7shanlon4 with dissolve
        sh "God, you haven't changed a bit. Take a seat."
        show bg ch7shanlon35 with dissolve
        g "No thanks..."
        show bg ch7shanlon6 with dissolve
        sh "Antoine, turn on privacy mode... Sit down, girl."
    else:

        sh "But where are my manners? Don't stand out there like a wet puppy. Get inside, out of the rain."
        show bg ch7shanlon7 with dissolve
        sh "Shame on you for getting my hopes up, I thought you might be someone else."
        g "Where's Papa?"
        show bg ch7shanlon8 with dissolve
        sh "God, you haven't changed a bit. Take a seat."
        show bg ch7shanlon35 with dissolve
        g "No thanks..."
        sh "Sit down, girl."

    show bg ch7shanlon7 with dissolve
    sh "So... I take it you saw the interview then?"
    g "I did. So, where is he?!"
    show bg ch7shanlon8 with dissolve
    sh "I can't believe you actually bought it. I thought you were smarter than that."
    sh "If you're here for a chat and not revenge, I'd turn around right now. It won't go as you expect."
    show bg ch7shanlon14 with dissolve
    g "You might have turned him against me but..."
    show bg ch7shanlon8 with dissolve
    sh "Dear God, was I ever this young and stupid?"
    show bg ch7shanlon9 with dissolve
    sh "I know you hate me, if I were you I would too. With a dead mother and the daddy issues you had, it's no surprise."
    g "You hated me too, I could tell."
    sh "Darling, when it came to you, I never cared one way or the other."
    show bg ch7shanlon10 with dissolve
    sh "What, you think I whispered in his ear at night to throw you out, especially after what happened to that Timmy, or whatever his name was?"
    show bg ch7shanlon11 with dissolve
    $ renpy.pause(1)
    show bg ch7shanlon12 with dissolve
    g "You hate people like me! You call us Milchers."
    sh "I don't hate Milchers, far from it. Without you lot and the controversy you generate, I'd be half as popular as I am."
    sh "You'd be amazed at how much of my audience tunes in just to get angry."
    show bg ch7shanlon15 with dissolve
    g "You're full of it."
    show bg ch7shanlon16 with dissolve
    sh "If anyone hates Milchers in this house, it's your precious Papa."
    g "..."
    sh "Believe me or don't. Makes no difference."
    show bg ch7shanlon17 with dissolve
    sh "He's upstairs, ask him yourself."
    show bg ch7shanlon18 with dissolve
    g "Fine, goodbye..."
    play music audio.darkcalm fadein 2.0 fadeout 2.0
    scene black with Dissolve(2)
    show bg ch7gloria3 with Dissolve(2)
    g "It really is like I never left."
    show bg ch7gloria4 with dissolve
    g "*Sniffs* Hey buddy, it's been a long time."
    show bg ch7gloria5 with dissolve
    g "Did you miss me?"
    show bg ch7gloria6 with dissolve
    g "I missed you too."
    show bg ch7gloria7 with dissolve
    g "*Sniffs* Donut, I'm scared..."
    show bg ch7gloria8 with dissolve
    g "But this is the only way to help them."
    a "Help who?"
    show bg ch7gloria9 with dissolve
    g "Papa?"
    play music audio.epic fadein 14.0 fadeout 2.0
    show bg ch7gloria10 with dissolve
    a "What are you doing here?"
    show bg ch7gloria15 with dissolve
    g "We need to talk..."
    scene black with Dissolve(1)













    show bg ch7car1 movie with dissolve
    $ renpy.pause(9)

    show bg ch7gloria10 with dissolve
    a "You will turn yourself in, I will get you counsel, you will plead guilty..."
    a "Then we're done."

    show bg ch7car3 movie with dissolve
    $ renpy.pause(2)


    show bg ch7gloria16 with dissolve
    g "Papa? Why won't you even look at me?"
    show bg ch7gloria12 with dissolve
    a "In return, I will clear Ellen's debts. And I will never see you again, is that understood?"
    g "But, Papa..."

    show bg ch7gloria11 with dissolve
    a "Don't call me that!"
    a "Don't act like you're really her! My Gloria died two years ago!"

    show bg ch7bike2 movie with dissolve
    $ renpy.pause(8)


    show bg ch7gloria17 with dissolve
    g "*Begins to well up* Don't say that... I'm right here!"
    show bg ch7bike1 movie with dissolve
    $ renpy.pause(6)
    show bg ch7gloria18 with dissolve
    g "Just look at me... Please!"

    show bg ch7plane1 movie with dissolve
    $ renpy.pause(9)
    show bg ch7tank1 movie with dissolve
    $ renpy.pause(6)

    show bg ch7gloria13 with dissolve
    a "The police will be here soon."
    g "What about Henry!?"
    a "..."
    g "Papa!"
    a "STOP CALLING ME THAT YOU MONSTER!"
    show bg ch7plane2 movie with dissolve
    $ renpy.pause(9)
    show bg ch7tank2 movie with dissolve
    $ renpy.pause(4)

    show bg ch7gloria18 with dissolve
    g "I'm the monster?"

    show bg ch7plane3 movie with dissolve
    $ renpy.pause(5.5)
    show bg ch7car2 movie with dissolve
    $ renpy.pause(12)




    show bg ch7gloria18 with dissolve
    g "Everyone was right about you. I should have known."
    show bg ch7redmoon movie with dissolve
    $ renpy.pause(9)
    show bg ch7gloria18 with dissolve
    g "I was just a kid when you threw me out! But I'm the monster?"

    a "Gloria? What are you-"
    g "Well, if that's what I am, I might as well show it!"
    show bg ch7gloriaexplode movie with dissolve
    $ renpy.pause(5.7)


    play sound audio.empblast
    show bg ch7gloria19 with hpunch
    $ renpy.pause(3)

    stop music fadeout 3.0
    scene black with Dissolve(3)
    $ renpy.pause(3)

    $ cobd.pl = pl
    $ cobd.dep = dep


    $ cobd.e_met = e_met
    $ cobd.e_score = e_score
    $ cobd.e_lust = e_lust

    $ cobd.g_met = g_met
    $ cobd.g_score = g_score
    $ cobd.g_lust = g_lust

    $ cobd.v_met = v_met
    $ cobd.v_score = v_score
    $ cobd.v_lust = v_lust

    $ cobd.k_met = k_met
    $ cobd.k_score = k_score
    $ cobd.k_lust = k_lust
    $ cobd.k_dirty = k_dirty

    $ cobd.s_met = s_met
    $ cobd.s_score = s_score
    $ cobd.s_lust = s_lust
    $ cobd.s_break = s_break

    $ cobd.j_score = j_score


    $ cobd.sa_name = sa_name
    $ cobd.sa_met = sa_met
    $ cobd.sa_score = sa_score
    $ cobd.sa_lust = sa_lust
    $ cobd.sa_int = sa_int

    $ cobd.c_met = c_met
    $ cobd.c_score = c_score
    $ cobd.c_lust = c_lust

    $ cobd.h_score = h_score

    $ cobd.ab_score = ab_score
    $ cobd.ab_lust = ab_lust



    $ cobd.vicsexname = vicsexname
    $ cobd.ellensexname = ellensexname
    $ cobd.katiesexname = katiesexname
    $ cobd.gloriasexname = gloriasexname
    $ cobd.chandrasexname = chandrasexname


    $ cobd.pcap = pcap
    $ cobd.pdastart = pdastart

    $ cobd.extraevents = extraevents
    $ cobd.ch4battlescore = ch4battlescore
    $ cobd.vicsexcount = vicsexcount

    $ cobd.save()

    jump versionend
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
