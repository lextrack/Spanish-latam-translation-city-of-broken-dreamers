
image bg ch4vicfollow1 = "ch4vicfollow1"
image bg ch4vicfollow2 = "ch4vicfollow2"
image bg ch4vicfollow3 = "ch4vicfollow3"
image bg ch4vicfollow4 = "ch4vicfollow4"
image bg ch4vicfollow5 = "ch4vicfollow5"
image bg ch4vicfollow6 = "ch4vicfollow6"
image bg ch4vicfollow7 = "ch4vicfollow7"
image bg ch4vicfollow8 = "ch4vicfollow8"
image bg ch4vicfollow9 = "ch4vicfollow9"
image bg ch4vicfollow10 = "ch4vicfollow10"
image bg ch4vicfollow11 = "ch4vicfollow11"
image bg ch4vicfollow12 = "ch4vicfollow12"
image bg ch4vicfollow13 = "ch4vicfollow13"
image bg ch4vicfollow14 = "ch4vicfollow14"
image bg ch4vicfollow15 = "ch4vicfollow15"
image bg ch4vicfollow16 = "ch4vicfollow16"
image bg ch4vicfollow17 = "ch4vicfollow17"
image bg ch4vicfollow18 = "ch4vicfollow18"
image bg ch4vicfollow19 = "ch4vicfollow19"
image bg ch4vicfollow20 = "ch4vicfollow20"
image bg ch4vicfollow21 = "ch4vicfollow21"
image bg ch4vicfollow22 = "ch4vicfollow22"
image bg ch4vicfollow23 = "ch4vicfollow23"
image bg ch4vicfollow24 = "ch4vicfollow24"
image bg ch4vicfollow25 = "ch4vicfollow25"
image bg ch4vicfollow26 = "ch4vicfollow26"
image bg ch4vicfollow27 = "ch4vicfollow27"
image bg ch4vicfollow28 = "ch4vicfollow28"
image bg ch4vicfollow29 = "ch4vicfollow29"
image bg ch4vicfollow30 = "ch4vicfollow30"


image ch4roadanim2movie = Movie(play='video/chapter-4-video/ch4roadanim2.webm', loop=False)
image bg ch4roadanim2 movie:
    "ch4roadanim2movie"
    pause 10.0
    "ch4roadanim2end"

image ch4tunnelvicmovie = Movie(play='video/chapter-4-video/ch4tunnelvic.webm', loop=False)
image bg ch4tunnelvic movie:
    "ch4tunnelvicmovie"
    pause 12.0

image ch4elevatormovie = Movie(play='video/chapter-4-video/ch4elevator.webm', loop=False)
image bg ch4elevator movie:
    "ch4elevatormovie"
    pause 4.6
    "ch4elevatorend"

image ch4drivemovie = Movie(play='video/chapter-4-video/ch4drive.webm', loop=False)
image bg ch4drive movie:
    "ch4drivemovie"
    pause 10
    "ch4driveend"

image ch4vicpanelemovie = Movie(play='video/chapter-4-video/ch4vicpanele.webm', loop=False)
image bg ch4vicpanele movie:
    "ch4vicpanelemovie"
    pause 10
    "ch4vicpaneleend"

image ch4vicfollowwalkmovie = Movie(play='video/chapter-4-video/ch4vicfollowwalk.webm', loop=False)
image bg ch4vicfollowwalk movie:
    "ch4vicfollowwalkmovie"
    pause 8
    "ch4vicfollowwalkend"




label ch4follow:

    play music audio.delights fadein 10.0 fadeout 3.0
    scene black with Dissolve(3)
    show bg ch4drive movie with Dissolve(3)
    p "(This is a bad idea. But I need to know what they know. Meredith and Victoria both.)"
    show bg ch4vicfollow21 with Dissolve(2)
    p "(They played me. Time to return the favor.)"
    show bg ch4vicfollow20 with Dissolve(2)
    p "(With me and Gloria off the grid, Meredith is going to be pulling in all her assets. Which is just what I want.)"
    scene black with Dissolve(2)
    n "You hear the Baynard corporate tram arrive. Dozens of employees file out of the station. Your target appears soon after, lagging behind the crowd."
    show bg ch4vicfollow23 with Dissolve(2)
    p "(Rough day at the office?)"
    show bg ch4vicfollow22 with Dissolve(1)
    $ renpy.pause(2)
    show bg ch4vicfollow24 with Dissolve(1)
    $ renpy.pause(2)
    show bg ch4vicfollow25 with Dissolve(1)
    n "She steps into a pod and mouths instructions to the navigator"
    p "(Where you taking me tonight, Victoria?)"
    scene black with Dissolve(1)
    show bg ch4vicfollow27 with Dissolve(1)
    p "(The hills? Miss Shields, you do live the high life.)"
    if "ch2choosevic" in extraevents:
        p "(You were honest about that much, at least.)"
    else:
        p "(I guess all the corporate muckity-mucks have to stick together. I wonder if she and Alexis Conner go to the same country club.)"
    show bg ch4vicfollow26 with Dissolve(1)
    $ renpy.pause(1)
    show bg ch4roadanim2 movie with Dissolve(2)
    $ renpy.pause(4)
    show bg ch4tunnelvic movie with Dissolve(2)
    p "(What exactly do you know?)"
    p "(Do you actually believe Meredith when she says Gloria is a cure?)"
    if v_score >= 3:
        p "(I'd like to think you do... but I'm probably lying to myself. You're Meredith's right-hand woman after all.)"
    else:
        p "(Probably not. You're Meredith's right-hand woman after all.)"
    n "You follow Victoria's pod at a safe distance. She sits in silence for the rest of the ride."
    show bg ch4vicfollow28 with Dissolve(1)
    p "(Looks like we're almost home.)"
    show bg ch4vicfollow29 with Dissolve(1)
    if v_score >= 3:
        p "(I'd feel bad about this, but she did break into my home. Fair is fair.)"
    else:
        p "(Break into my house will you? We'll see how you like it. Fair is fair.)"
    if "ch1spellbound" in extraevents:
        p "(Then, when she sees what I can do, she'll want me as much as I want her.)"
        p "(Want her... shit, I have to focus.)"
    show bg ch4vicfollow30 with dissolve
    if v_score >= 3:
        p "(Either way, once this is done, I'll know if you're what you seem to be.)"
        p "(Prove me wrong, Victoria.)"
    else:
        p "(You paid me an unexpected visit.)"
        p "(We'll see how you like it.)"
    show bg ch4vicfollow5 with Dissolve(1)
    p "Sam, talk to me."
    s "Yes, Sir?"
    p "Good to have you back."
    s "I missed you too, Sir."
    p "Just tell me where we are?"
    s "Just off of LaBrea, near Miracle Mile."
    show bg ch4vicfollow6 with dissolve
    p "Top dollar. Surprised she can afford it."
    s "The housing complex is corporate owned."
    p "That explains that."
    show bg ch4vicpanele movie with dissolve
    v "*Lets out a long sigh of relief as she approaches the elevator*"
    p "(Long day, Victoria? Me too.)"
    show bg ch4vicfollow7 with dissolve
    p "(You feel safe; your guard is down. Shame it's not over yet.)"
    show bg ch4vicfollow8 with dissolve
    s "Sir, shall I track what floor she stops on?"
    p "*Whispering* I have a better idea. Remote in. Get the next elevator."
    s "Done, Sir."
    show bg ch4vicfollow9 with dissolve
    p "Sam, quickly. Is it on its way?"
    s "Five seconds, Sir."
    show bg ch4vicfollow10 with dissolve
    p "Then stop me at her same floor."
    s "Yes, Sir."
    show bg ch4vicfollow11 with dissolve
    p "That's a long five seconds."
    s "One elevator, coming up, Sir."
    show bg ch4elevator movie
    p "You watching, Sam?"
    s "Yes, Sir."
    s "Miss Shields has stopped at the thirty-second floor."
    p "Good, stop there."
    window hide
    show bg ch4vicfollowwalk movie with Dissolve(1)
    $ renpy.pause()
    p "Good work, Sam."
    s "Thank you, Sir."
    show bg ch4vicfollow13 with dissolve
    v "*Sighs* I'm home, Hope."
    n "The door unlocks"
    "Hope" "Welcome home."
    show bg ch4vicfollow14 with dissolve
    $ renpy.pause(1)
    show bg ch4vicfollow15 with dissolve
    $ renpy.pause(1)
    show bg ch4vicfollow16 with dissolve
    $ renpy.pause(1)
    show bg ch4vicfollow17 with dissolve
    p "Sam, do you think you can unlock that door?"
    s "Yes, Sir. When Mrs. [pl]'s assistant, Kay, purged any outside influence she also gave me full access to Victoria's privacy protocols."
    p "Sonja. Thank you, you crazy bitch. Wait, assistant? You AI's calling yourselves that now?"
    s "I do assist you, Sir. But, this topic is not relevant to the current situation. Checking alternatives..."
    s "If you prefer, I can also unlock one of her exterior windows."
    p "(Outside is risky, but I could watch her for awhile.)"
    if "ch1spellbound" in extraevents and "ch1vic" in extraevents:
        p "(I think Victoria would prefer it if I just knock. She'll want to see me as much as I want to see her.)"
    $ resetmenu()
    jump ch4followmenu

label ch4followmenu:
    menu:
        "Break In":
            show bg ch4vicfollow18 with dissolve
            $ extraevents.append("ch4breakin")
            p "Work your magic, Sam. Silent opening."
            s "Yes, Sir. This will take a few minutes."
            n "Sam accesses the locking mechanism, slowly but silently opening the door"
            s "Bypassed, Sir."
            jump ch4vicbreak
        "Sneak from outside":
            $ extraevents.append("ch4sneakin")
            jump ch4vicsneak
        "Knock" if "ch1spellbound" in extraevents and "ch1vic" in extraevents and menu1 == True:
            $ menu1 = False
            show bg ch4vicfollow18 with dissolve
            s "Would you like me to bypass the door, Sir?"
            p "No need, Sam."
            s "Sir? I believe this course of action is what you would refer as reckless."
            menu:
                "You're right":
                    p "Shit, you're right."
                    jump ch4followmenu
                "Quiet":
                    p "I know what I'm doing, Sam! Zip it."
            n "You knock on the door. After a moment the door unlocks from behind."
            show bg ch4vicfollow19 with dissolve
            v "Agent? Were you following me?"
            p "Yes... I... I had to see you."
            v "Please, come in."
            $ extraevents.append("ch4knock")
            jump ch4vicknock
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
