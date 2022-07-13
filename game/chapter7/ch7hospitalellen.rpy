

image bg ch7findellen1 = "ch7findellen1"
image bg ch7findellen2 = "ch7findellen2"
image bg ch7findellen3 = "ch7findellen3"
image bg ch7findellen4 = "ch7findellen4"
image bg ch7findellen5 = "ch7findellen5"
image bg ch7findellen6 = "ch7findellen6"
image bg ch7findellen7 = "ch7findellen7"
image bg ch7findellen8 = "ch7findellen8"
image bg ch7findellen9 = "ch7findellen9"
image bg ch7findellen10 = "ch7findellen10"
image bg ch7findellen11 = "ch7findellen11"
image bg ch7findellen12 = "ch7findellen12"
image bg ch7findellen13 = "ch7findellen13"
image bg ch7findellen14 = "ch7findellen14"
image bg ch7findellen15 = "ch7findellen15"
image bg ch7findellen16 = "ch7findellen16"
image bg ch7findellen17 = "ch7findellen17"
image bg ch7findellen18 = "ch7findellen18"
image bg ch7findellen19 = "ch7findellen19"
image bg ch7findellen20 = "ch7findellen20"
image bg ch7findellen21 = "ch7findellen21"
image bg ch7findellen22 = "ch7findellen22"
image bg ch7findellen23 = "ch7findellen23"
image bg ch7findellen24 = "ch7findellen24"
image bg ch7findellen25 = "ch7findellen25"
image bg ch7findellen26 = "ch7findellen26"
image bg ch7findellen27 = "ch7findellen27"
image bg ch7findellen28 = "ch7findellen28"
image bg ch7findellen29 = "ch7findellen29"


image ch7henrydress = Movie(play='video/chapter-7-video/ch7henrydress.webm', loop=False)
image bg ch7henrydressmovie movie:
    "ch7henrydress"
    pause 7.0
    "ch7henrydressend"


label ch7hospitalellen:

    scene black with Dissolve(1)
    show bg ch7findellen1 with dissolve
    play music audio.calm fadein 2.0 fadeout 2.0
    e "What is going on out there?"
    n "Ellen hears a muffled groan and a sharp bang outside"
    show bg ch7findellen2 with dissolve
    e "Keep it down, you sons of-"
    if k_score >= 5:
        show bg ch7findellen7 with dissolve
    else:
        show bg ch7findellen8 with dissolve
    p "Ellen! There you are!"
    k "Ah, hey..."
    h "Ellen."
    show bg ch7findellen3 with dissolve
    e "[p]! Henry! Random girl I don't know! HEY!"
    show bg ch7findellen10 with dissolve
    k "Umm, hey, I'm Katie."
    e "Ahh, well, umm... Nice to meet you."
    show bg ch7findellen5 with dissolve
    e "Now that we're done with the small talk, can you get me the fuck out of here?"
    if k_score >= 5:
        show bg ch7findellen7 with dissolve
    else:
        show bg ch7findellen8 with dissolve
    p "Ellen, have you seen Gloria?"
    show bg ch7findellen4 with dissolve
    e "What do you mean? I've been in this fucking bed since I saw you last."
    h "Shit..."
    show bg ch7findellen5 with dissolve
    e "Wait, you lost her? How the fuck did you lose her?!"
    p "Ellen, please..."
    show bg ch7findellen9 with dissolve
    h "[p], what do we do now?"
    p "We get Ellen out of here, after that..."
    show bg ch7findellen11 with dissolve
    k "[p], let me make sure we can actually move her without making things worse."
    p "Quickly."
    show bg ch7findellen12 with dissolve
    k "Wow. You're lucky to be alive."
    e "I heard that already."
    k "No, seriously. With back damage this severe... it would have cost a fortune to..."

    show bg ch7findellen13
    e "I get it! I'm fucked up! Lucky, whatever! Can you stop fucking gawking like an idiot and get me out of this bed?"
    e "Now would be nice!"
    show bg ch7findellen12 with dissolve
    k "Sure thing. But one question, do you want to drink your meals through a straw the rest of your life?"
    e "No..."
    k "Then let me do my job."
    show bg ch7findellen14 with dissolve
    e "Well, shit."
    p "Let her finish, Ellen. We'll have you out of here soon."
    show bg ch7findellen15 with dissolve
    e "God, I can be such a bitch..."
    show bg ch7findellen16 with dissolve
    e "Sorry... You didn't deserve that."
    k "Comes with the job. You get used to it."
    e "Still... now I feel like shit, snapping at you."
    k "I'll survive."
    show bg ch7findellen17 with dissolve
    k "They really did good work. Maybe the best I have ever seen..."
    p "So we can move her?"
    k "Ah, yeah, just try not to drop her down a flight of stairs or anything."
    show bg ch7findellen18 with dissolve
    e "Henry, there are clothes in there."

    show bg ch7henrydressmovie movie
    h "Ummm... This doesn't seem like you."
    e "Don't even ask, big guy."
    h "Trust me, I won't. Let's just go."
    show bg ch7findellen19 with dissolve
    h "Please."
    p "Sure thing, big guy. Katie, help her get dressed."
    show bg ch7findellen20 with dissolve
    p "We'll take her back to Betty's. I just hope her little spy network found something."
    h "It's our only shot. She could be anywhere."
    show bg ch7findellen21 with dissolve
    k "Okay, one disgruntled patient in a dress coming up."
    e "Ugh..."
    menu:
        "Good enough":
            p "Well, good enough. Henry, let's get her out of here."
        "Damn, that's hot":
            $ k_score -= 1
            p "Damn, Ellen. That looks good."
            k "Huh?"
            show bg ch7findellen22 with dissolve
            e "Wrong place, wrong time, [p]..."
        "You should dress that way more often":

            $ e_score += 1
            $ extraevents.append("ch7ellenstylechange")
            p "I know you hate dresses Ellen, but it really suits you. I think you should drop the punk look and go for \"lounge singer.\""
            show bg ch7findellen22 with dissolve
            e "Don't think I can't kick your ass laying down, Spook."
            p "Heh, Henry, let's get her out of here."

    scene black with dissolve
    show bg ch7findellen23 with dissolve
    e "I think I can get used to this."
    h "..."
    p "Let me check the hallway. We can get to the elevator and right out the front door during this whole mess."
    h "Do it."
    scene black with dissolve
    show bg ch7findellen25 with dissolve
    p "Hold up..."
    show bg ch7findellen24 with dissolve
    p "Okay, quickly to the elevator."
    show bg ch7findellen26 with dissolve
    h "We're coming. Not too fast. Last thing I want to do is hurt her even more."
    e "I feel so useless right now..."
    show bg ch7findellen27 with dissolve
    h "Don't say that..."
    e "Not being able to fucking walk? When you are in this position, you let me know."
    h "I've been where you are. Paralyzed from the waist down, as well. So, yeah, I get it."
    show bg ch7findellen28 with dissolve
    e "Damn, Henry... You really have been through the shit, haven't you?"
    h "Yeah, and umm... Could you fix your top?"
    show bg ch7findellen29 with dissolve
    e "Ha, yeah sure."
    k "Guys, we need to move before they notice she's missing..."
    e "Giddy up, bronco!"
    h "*Sighs* Coming..."
    jump ch7return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
