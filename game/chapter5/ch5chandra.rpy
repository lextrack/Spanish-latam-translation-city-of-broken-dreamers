
image ch5chandrapanup = Movie(play='video/chapter-5-video/ch5chandrapanup.webm', loop=False)
image bg ch5chandrapanupmovie movie:
    "ch5chandrapanup"
    pause 10.0
    "ch5chandrapanupend"

image bg ch5chandradoggy movie = Movie(play="video/chapter-5-video/ch5chandradoggy.webm")

image bg ch5chandradrill1 movie = Movie(play="video/chapter-5-video/ch5chandradrill1.webm")
image bg ch5chandradrill2 movie = Movie(play="video/chapter-5-video/ch5chandradrill2.webm")
image bg ch5chandrablow movie = Movie(play="video/chapter-5-video/ch5chandrablow.webm")



label ch5chandra:

    play music audio.party fadein 2.0 fadeout 2.0
    if _in_replay:
        $ setReplay()
    show bg ch5chandra25 with dissolve
    p "You really know how to push my buttons, don't you?"
    c "Just the right ones."
    show bg ch5chandra27 with dissolve
    c "Don't waste too much time, spooky."
    p "I wasn't planning on it."
    show bg ch5chandra26 with dissolve
    c "Mmm..."
    p "Can't tell if you are wet from the pool or-"
    c "Oh, I don't swim."
    show bg ch5chandra28 with dissolve
    p "How did you become such a naughty thing?"
    c "That's a dumb question. I've always been. Now make me taste it again."
    show bg ch5chandra29 with dissolve
    p "Good?"
    c "It's prime!"
    p "Kids and your slang. Whatever happened to just \"good.\""
    c "Because, boring!"
    p "Fuck, you drive me nuts."
    c "I know. I piss you off and make you horny. It's a pretty sweet combo if I say so myself."

    if chandrasexname == False:
        menu:
            "Say nothing":
                $ chandrasexname = p
            "First things first, call me...":
                python:
                    chandrasexname = renpy.input("What do you want her to call you?")
                    chandrasexname = chandrasexname.strip()
                    persistent.chandrasexname = chandrasexname
    show bg ch5chandrapanupmovie movie

    c "So, [chandrasexname] are you going to see if I have been practicing?"
    p "Well, you're not drunk or high. It's going to be a challenge for you."
    c "Challenge fucking accepted. Now get up here."
    show bg ch5chandra30 with dissolve
    p "You asked for it."
    c "I did, now put it in my mouth."
    show bg ch5chandra31 with dissolve
    $ renpy.pause(1)
    show bg ch5chandra32 with dissolve
    p "If Abby came down now..."
    c "Mmmph, Keep dreaming."
    show bg ch5chandra33 with dissolve
    p "There we go. Phew...."
    c "*With her mouth full* Dreeper!"
    show bg ch5chandrablow movie with dissolve
    p "Holy shit! You are a fast learner!"
    c "Mmm-hmm!"
    p "That's right, all the way down."
    show bg ch5chandra34 with dissolve
    p "Perfect view. Just hold it there for a sec."
    c "Mmmm!"
    show bg ch5chandra35 with dissolve
    c "What did I tell ya!?"
    p "I'm impressed. But now I want to see that nice ass of yours."
    show bg ch5chandra36 with dissolve
    c "Yes, [chandrasexname]."
    show bg ch5chandra37 with dissolve
    p "Oh, just get these off."
    show bg ch5chandra38 with dissolve
    p "Perfect."
    c "Are you going to fuck me now?"
    p "What else?"
    $ resetmenu()
    jump ch5chandramenu

label ch5chandramenu:
    if menu1 == True:
        $ menu1 = False
        jump ch5chandradoggy
    menu:
        "Fuck from behind":
            $ menu1 = False
            jump ch5chandradoggy
        "On her back" if menu1 == False:
            jump ch5chandraback
        "Cum in her mouth" if menu1 == False:
            jump ch5chandracummouth
        "Cum in her pussy" if menu1 == False:
            jump ch5chandracumpussy


label ch5chandradoggy:
    if menu2 == True:
        $ menu2 = False

        p "I think some doggy is in order."
        show bg ch5chandra39 with dissolve
        c "Should I bark?"
        p "..."
        p "Ahh, no."
        show bg ch5chandra40 with dissolve
        "*You push deep inside her*"
        c "Good because that would be fucking weird!"
        p "You mentioned it!"
        show bg ch5chandra42 with dissolve
        p "Now, lose the top."
        c "What, you don't like it? Bah, fine, [chandrasexname]."
        show bg ch5chandra43 with dissolve
        p "Nothing wrong with it. Just, it's in the way."
        c "Better not be lying."
        p "Me? Lie to you?"
        c "Ahh, yeah. A lot."
        show bg ch5chandra44 with dissolve
        p "Being a sarcastic little brat, I'd think you'd understand that."
        c "Just shut up and fuck me!"
    else:

        p "Time for some doggy again."
        show bg ch5chandra43 with dissolve
        c "Woof woof!"
        p "Stop!"
        c "Why? Am I making you uncomfortable?"
        if "ch2shanlon" in extraevents:
            p "It just reminds me of someone."
            c "Now that is someone I want to meet."
            p "No... No, you don't."
        else:
            p "Yes!"
            c "Ha, awesome!"

    show bg ch5chandradoggy movie with dissolve
    c "Getting better. First, ugh! Fuck at your place, now my place!"
    p "What are you getting at?"
    c "Mom's office next?!"
    if dep >= 2:
        p "Sounds like a plan."
        show bg ch5chandra41 with dissolve
        c "Fucking aces!"
    else:
        p "Fuck, you are persistent."
        show bg ch5chandra41 with dissolve
        c "Fucking right!"

    c "Fuck me, keep going!"
    p "Damn, I can't wait to explode."
    c "Soon, [chandrasexname]!"
    show bg ch5chandra45 with dissolve
    c "Fuck! You made me cum!"
    p "I have my ways."
    c "Hell yeah, you do."
    jump ch5chandramenu


label ch5chandraback:
    p "Flip over. I know what you like."
    c "Fuck, yes, [chandrasexname]!"
    show bg ch5chandra46 with dissolve
    c "Now I want you to make me cum good."
    show bg ch5chandra47 with dissolve
    c "Teach this little thing something."
    p "That's the goal, isn't it?"
    p "Now get closer."
    show bg ch5chandra48 with dissolve
    c "Of course."
    p "I swear this is the only time you listen to me."
    c "Yep!"
    show bg ch5chandra49 with dissolve
    p "Shit, I still can't get over how tight you are."
    c "Well, because I'm not ancient like your other escapades."
    show bg ch5chandra51 with dissolve
    p "You really want to get fucked, don't you?"
    c "Ahh, yeah. Now come on, [chandrasexname], give it to me!"
    show bg ch5chandradrill2 movie with dissolve
    c "Ah, shit! Nice and deep, [chandrasexname]! Please!"
    p "Just enjoy it."
    show bg ch5chandradrill1 movie with dissolve
    c "*Murmurs in pleasure as you push inside her*"
    p "Nice, I just realized something else."
    c "Uhh, what's that?"
    p "Now I know of two ways to make you quiet."
    c "Oh, fuck off and let me-"
    show bg ch5chandra50 with dissolve
    c "Cuuuuum.... *pants vigorously*"
    p "Wow..."
    show bg ch5chandra52 with dissolve
    c "Just remember, when you cum, we probably don't have time to clean up."
    jump ch5chandramenu

label ch5chandracummouth:
    c "Shit! The shower stopped. She'll be down here soon."
    p "Quick, open your mouth!"
    show bg ch5chandra56 with dissolve
    c "Ha, okay!"
    show bg ch5chandra57 with dissolve
    p "Shit, here it comes!"
    "You blast deep into Chandra's mouth. When you think it's over, you explode again."
    show bg ch5chandra58 with dissolve
    c "AWWHHH!"
    p "Don't play with it! Swallow it!"
    show bg ch5chandra59 with dissolve
    c "*Gulps down*"
    show bg ch5chandra60 with dissolve
    p "Ha, fucking aces!"
    c "Hey, that's my line! Whatever..."
    jump ch5chandrabeforeabby

label ch5chandracumpussy:
    p "I guess we should fill you up then."
    show bg ch5chandra53 with dissolve
    c "As long as it doesn't leak out when Abby gets down here."
    c "Shit, quick, the shower just stopped."
    p "Fuck!"
    c "SHH!!! She'll hear you!"
    show bg ch5chandra54 with dissolve
    p "Phew... Damn, damn, damn."
    show bg ch5chandra55 with dissolve


label ch5chandrabeforeabby:
    c "Now quick, get your clothes on!"
    show bg ch5chandra61 with dissolve
    p "Good thing you weren't wearing those pants from the other night."
    c "Heh, tell me about it."
    show bg ch5chandra62 with dissolve
    c "Ta-da! Finished!"
    $ extraevents.append("ch5chandrasex")
    $ renpy.end_replay()
    if not persistent.ch5chandrasex:
        $ renpy.notify(['Scene Unlocked', 'unlock'])
        $ persistent.ch5chandrasex = True
    play music audio.sol fadein 2.0 fadeout 2.0
    jump ch5chandraabby
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
