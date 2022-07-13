

image bg ch4docmorning1 = "ch4docmorning1"
image bg ch4docmorning2 = "ch4docmorning2"
image bg ch4docmorning3 = "ch4docmorning3"
image bg ch4docmorning4 = "ch4docmorning4"
image bg ch4docmorning5 = "ch4docmorning5"
image bg ch4docmorning6 = "ch4docmorning6"
image bg ch4docmorning7 = "ch4docmorning7"
image bg ch4docmorning8 = "ch4docmorning8"
image bg ch4docmorning9 = "ch4docmorning9"
image bg ch4docmorning10 = "ch4docmorning10"
image bg ch4docmorning11 = "ch4docmorning11"
image bg ch4docmorning12 = "ch4docmorning12"
image bg ch4docmorning13 = "ch4docmorning13"
image bg ch4docmorning14 = "ch4docmorning14"
image bg ch4docmorning15 = "ch4docmorning15"
image bg ch4docmorning16 = "ch4docmorning16"
image bg ch4docmorning17 = "ch4docmorning17"

image ch4docmorningpanmovie = Movie(play='video/chapter-4-video/ch4docmorningpan.webm', loop=False)
image bg ch4docmorningpan movie:
    "ch4docmorningpanmovie"
    pause 10.0
    "ch4docpanupend"

label ch4katiemorning:
    play music audio.calmmorning fadein 2.0 fadeout 2.0
    scene black with Dissolve(3)
    if "ch4katie" in extraevents:
        jump ch4katiemorning1
    else:
        jump ch4katiemorning2


label ch4katiemorning1:
    show bg ch4docmorning1 with Dissolve(3)
    $ renpy.pause(1)
    show bg ch4docmorning2 with Dissolve(3)
    p "Psst, Katie. It's getting late we should get up."
    k "[p]..?"
    show bg ch4docmorning3 with dissolve
    k "*Let's out a deep yawn followed by a small burp*"
    p "Is it too late to take back me calling you \"perfect\"?"
    show bg ch4docmorning4 with dissolve
    k "Nope, sorry, it's in the public record. What time is it?"
    p "Close to ten. Doesn't your AI have an alarm?"
    k "..."
    p "Forget I said anything. Anyway, we should go and check on..."
    show bg ch4docmorning5 with dissolve
    k "In a minute. [p]..."
    p "Yeah?"
    k "Before anything else. We need to talk about last night."
    show bg ch4docmorning6 with dissolve
    k "You really surprised me. Not the waking me up in the middle of the night part, I should be used to that by now..."
    k "I mean, you were sweet and patient and..."
    p "Katie, all things considered, I think it was a great night."
    k "Just... Thanks. I don't know how, but you really are a sweetheart."
    show bg ch4docmorning7 with dissolve
    k "I should get some clothes on."
    p "Should you? I could do with less."
    show bg ch4docmorning8 with dissolve
    k "Is it too late to take back me calling you sweet?"
    p "Nope, sorry, it's part of the public record, Doc."
    k "*Giggles* Screw off!"
    show bg ch4docmorning10 with dissolve
    p "What are you doing?"
    window hide
    show bg ch4docmorningpan movie with dissolve
    $ renpy.pause()

    k "Just need to make sure that Gus didn't trip the AC breaker again."
    k "He *grunt* tends to do that."
    k "I'll see you downstairs."
    jump ch4morning


label ch4katiemorning2:
    if k_score >= 3:
        k "Hey!"
        p "..."
        show bg ch4docmorning15 with dissolve
        p "*Yawns* What time is it?"
        show bg ch4docmorning16 with dissolve
        k "It's like ten or something. Gus didn't set off the alarm. Again."
        k "You sleep okay?"
        p "Yeah, better than I thought."
        p "They didn't try anything last night, did they?"
        show bg ch4docmorning17 with dissolve
        k "Not that I can see. We're still alive and the door hasn't been opened."
        p "We should see how the girl's doing. After that, I don't know."
    else:
        k "Hey, [p]. Wake up."
        p "..."
        show bg ch4docmorning11 with dissolve
        k "Time to get up. You still have some guests downstairs. In my office... where you dropped them... unannounced."
        p "Right, sorry."
        show bg ch4docmorning12 with dissolve
        k "I'm just somewhat cranky this morning. Don't apologize. I'm glad you brought her here."
        p "Don't be too glad. Who knows what kind of trouble I dropped on you."
        show bg ch4docmorning13 with dissolve
        k "Trouble or not. Better me than some corp getting their hands on her."
        p "Well, I know of two that want her, bad."
        show bg ch4docmorning14 with dissolve
        k "Either way, you shouldn't leave them alone down there. So, go, see if the tranq has worn off on the girl."
        k "And let me get dressed in peace."
        p "Okay, I'll meet you down there."
    jump ch4morning
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
