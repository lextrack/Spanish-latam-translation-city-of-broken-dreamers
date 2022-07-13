
image bg ch7wakeup1 = "ch7wakeup1"
image bg ch7wakeup2 = "ch7wakeup2"
image bg ch7wakeup3 = "ch7wakeup3"
image bg ch7wakeup4 = "ch7wakeup4"
image bg ch7wakeup5 = "ch7wakeup5"
image bg ch7wakeup6 = "ch7wakeup6"
image bg ch7wakeup7 = "ch7wakeup7"
image bg ch7wakeup8 = "ch7wakeup8"
image bg ch7wakeup9 = "ch7wakeup9"
image bg ch7wakeup10 = "ch7wakeup10"
image bg ch7wakeup11 = "ch7wakeup11"
image bg ch7wakeup12 = "ch7wakeup12"
image bg ch7wakeup13 = "ch7wakeup13"

image bg ch7gloria1 = "ch7gloria1"
image bg ch7gloria2 = "ch7gloria2"
image bg ch7gloria21 = "ch7gloria21"


image ch7gloriasubway = Movie(play='video/chapter-7-video/ch7gloriasubway.webm', loop=False)
image bg ch7gloriasubwaymovie movie:
    "ch7gloriasubway"
    pause 10.0
    "ch7gloriasubwayend"



label ch7stairwaymorning:
    scene black with Dissolve(1)



    scene black with Dissolve(1)
    show text "{=trans}EARLY THE NEXT MORNING{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)

    show bg ch7wakeup1 with Dissolve(1)
    p "Ugh... Morning Venus..."
    ve "..."
    p "Nevermind."
    show bg ch7wakeup2 with dissolve
    p "Huh?"
    p "Venus, where's Gloria?"
    show bg ch7wakeup3 with dissolve
    p "Venus, wake up."
    show bg ch7wakeup4 with dissolve
    $ renpy.pause(1)
    show bg ch7wakeup5 with dissolve
    n "After a moment Venus's still body begins to move as she opens her eyes"
    show bg ch7wakeup6 with dissolve
    if "ch6venusbroken" in extraevents:
        ve "Good Morning [p], would you like to fuck my ass?"
        p "I'm starting to think I didn't quite fix you right."
        p "Venus, where's Gloria?"
    else:
        ve "Yes, [p], do you require my services."
        p "Ahh, maybe later. Where's Gloria?"
    ve "Not here."
    p "I can see that, where is she?"
    ve "She left last night."
    play music audio.worried fadein 2.0 fadeout 2.0
    p "WHAT?! What do you mean she left?! Why didn't you stop her?"
    show bg ch7wakeup7 with dissolve
    ve "I am not allowed to restrain anyone without a safe-"
    p "Of fucking course. Fine. Why didn't you tell us?"
    ve "She told me not to say anything until the morning."
    p "Fuck me... not a request, just a statement."
    p "Did she say where she was going?"
    show bg ch7wakeup8 with dissolve
    ve "Still exiting hibernation. A moment, please."
    jump ch7stairwaymorningcont


label ch7stairwaymorningcont:
    show bg ch7wakeup10 with dissolve
    h "Isn't it a little too early to start screaming?"
    p "Gloria snuck off last night."
    show bg ch7wakeup11 with dissolve
    h "SHE WHAT!?"
    p "I know! Hold on."
    show bg ch7wakeup8 with dissolve
    h "Hold on?! We have to find her!"
    p "Yeah, well, right now we have no idea where she went or how long ago she left. But Venus here may know something."
    show bg ch7wakeup9 with dissolve
    h "Venus, tell us what happened!"
    ve "There we are. Gloria left after she saw a report about the singer Ellen Lane's hospitalization on the midnight news."

    p "Ellen! She's alive!"
    ve "According to the report, yes. After seeing that, Gloria became agitated and began to pack up what she could."
    h "Did she say where she was headed?"
    show bg ch7wakeup7 with dissolve
    ve "No, but she did leave a message for you."

    scene black with Dissolve(2)
    show bg ch7gloria1 with Dissolve(2)
    g "Hey Bigs, I'm sorry. Not a great way to wake up, I'm sure. When I saw Ellen was alive, I realized just how lucky I was that no one had died... Yet."
    g "You raised me well and I'll be careful, but seeing you risking yourself for me... I can't bear it."
    g "Who knows what happened to Ellen, and you... well, we talked about it. I can't be the reason you die. And I know you'll say it's not gonna happen, but I know better."
    g "You taught me well, Henry, I'll be ok. I promise."

    show bg ch7gloria2 with dissolve
    g "Live your life, Henry. You're gracious and kind. Don't waste the time you've got left on a lost cause."
    if g_score >= 3:
        g "Tell [p] and Katie I am sorry as well. I know they risked a lot to help me."
        g "Though, knowing [p], he's probably next to you listening to this anyway."
    else:

        g "Tell Katie I am sorry as well. I know she risked a lot to help me."
        g "I know [p] is gonna want to find me. But don't let him look either."

    show bg ch7gloriasubwaymovie movie with dissolve
    g "I put too many people in danger."
    g "I'm sorry, but I need to stop here. If I keep talking, I might not leave."
    show bg ch7gloria21 with dissolve
    g "I love you, Henry. I'll do right by you and Ellen. I promise."

    show bg ch7wakeup12 with dissolve
    h "Dammit, she is going to the hospital!"
    p "We don't know that!"
    h "Where else does she have to go? I have to catch her before she does something that gets her killed!"
    p "Wait! Even if that's true, we can't just storm into a Baynard hospital."

    h "Watch me."
    show bg ch7wakeup13 with dissolve
    p "Shit..."
    jump ch7ellenvic
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
