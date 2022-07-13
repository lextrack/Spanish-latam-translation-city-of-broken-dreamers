
image bg ch7outside1 = "ch7outside1"
image bg ch7outside2 = "ch7outside2"
image bg ch7outside3 = "ch7outside3"
image bg ch7outside4 = "ch7outside4"
image bg ch7outside5 = "ch7outside5"
image bg ch7outside6 = "ch7outside6"
image bg ch7outside7 = "ch7outside7"
image bg ch7outside8 = "ch7outside8"
image bg ch7outside9 = "ch7outside9"
image bg ch7outside10 = "ch7outside10"
image bg ch7outside11 = "ch7outside11"
image bg ch7outside12 = "ch7outside12"
image bg ch7outside13 = "ch7outside13"
image bg ch7outside14 = "ch7outside14"
image bg ch7outside15 = "ch7outside15"




image bg ch7follow1 = "ch7follow1"
image bg ch7follow2 = "ch7follow2"
image bg ch7follow3 = "ch7follow3"
image bg ch7follow4 = "ch7follow4"
image bg ch7follow5 = "ch7follow5"
image bg ch7follow6 = "ch7follow6"
image bg ch7follow7 = "ch7follow7"
image bg ch7follow8 = "ch7follow8"
image bg ch7follow9 = "ch7follow9"
image bg ch7follow10 = "ch7follow10"
image bg ch7follow11 = "ch7follow11"
image bg ch7follow12 = "ch7follow12"
image bg ch7follow13 = "ch7follow13"
image bg ch7follow14 = "ch7follow14"
image bg ch7follow15 = "ch7follow15"
image bg ch7follow16 = "ch7follow16"
image bg ch7follow17 = "ch7follow17"
image bg ch7follow18 = "ch7follow18"
image bg ch7follow19 = "ch7follow19"
image bg ch7follow20 = "ch7follow20"
image bg ch7follow21 = "ch7follow21"
image bg ch7follow22 = "ch7follow22"
image bg ch7follow23 = "ch7follow23"


label ch7apartment:
    scene black with Dissolve(2)
    show text "{=trans}LATER, AT YOUR APARTMENT{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    show bg ch7outside2 with dissolve
    p "Sam, bring up the security logs. I want to know if anyone has been in here since I left."
    s "Checking... Negative, Sir. Everything is in order."
    p "I'm sure that won't last long. How about externals, any stakeouts or tails?"
    s "Yes, Sir. You have someone following you at around 10 meters."
    p "Shit. We'll have to lose them later. Keep eyes on them and let me know if they do anything."
    scene black with Dissolve(1)
    show bg ch7follow1 with dissolve
    sa "So is this the haunted house, Spook?"
    show bg ch7follow2 with dissolve
    s "Your tail is closing in, Sir. It is the Bolter woman from the old precinct."
    p "*Under your breath* Where is she?"
    s "Seven meters behind you now."
    show bg ch7follow3 with dissolve
    s "Shall I activate security measures?"
    p "Let her wait, gives me time to think of something. If she tries to get inside, dissuade her."
    show bg ch7follow4 with dissolve
    sa "Place like this, you spooks really earn those bills, huh?"
    jump ch7apartmentinside


label ch7apartmentignore:
    play music audio.tense fadein 2.0 fadeout 2.0
    $ extraevents.append("ch7sashaignore")
    scene black with Dissolve(1)
    n "You take some time locking your place, ensuring you can be heard"
    show bg ch7follow6 with dissolve
    sa "Shit. Let's see where you go now."
    show bg ch7follow11 with dissolve
    $ renpy.pause(1)
    show bg ch7follow10 with dissolve
    if "ch7vicredmoon" in extraevents:
        p "{i}I can't deal with her, not after that.{/i}"
    p "Reactivate security measures."
    s "I never... Oh, of course, Sir."
    show bg ch7follow23 with dissolve
    $ renpy.pause(1)
    show bg ch7follow22 with dissolve
    p "We're done here."
    jump ch7apartmentoutside


label ch7apartmentrush:
    play music audio.tense fadein 2.0 fadeout 2.0
    $ extraevents.append("ch7sashaconfront")
    scene black with dissolve
    show bg ch7follow5 with dissolve
    if "ch7vicshow" in extraevents:
        sa "Who in the fuck was that woman?"
    else:
        sa "What the hell are you doing in there?"
    show bg ch7follow6 with dissolve
    p "Fucking Bolters."
    sa "Oh shit!"
    show bg ch7follow7 with dissolve
    $ renpy.pause(1)
    show bg ch7follow8 with dissolve
    $ renpy.pause(1)
    show bg ch7follow9 with dissolve
    sa "AGGH!"
    show bg ch7follow10 with dissolve
    if "ch7vicredmoon" in extraevents:
        p "Alright, I am not in the mood for any games. Don't you know it's rude to sneak up on people?"
    else:
        p "Don't you know it's rude to sneak up on people?"
    if "ch6missionshoot" in extraevents:
        show bg ch7follow13 with dissolve
        if "ch7vicredmoon" in extraevents:
            sa "What the fuck happened in there?"
            p "You best mind your own business."
            sa "Fine..."
        else:
            sa "Sorry! Just don't shoot me again!"
            p "Play stupid games, win stupid prizes."
        show bg ch7follow12 with dissolve
        sa "So, what now, you going to kidnap me too?"
        p "What the fuck are you talking about?"
        sa "Like you did Glenn. Don't tell me you forgot already."
    else:
        show bg ch7follow12 with dissolve
        if "ch7vicredmoon" in extraevents:
            sa "What the fuck happened in there?"
            p "You best mind your own business."
            sa "Fine..."
        else:
            sa "*Grimaces* Like you should talk."
            p "I'm a ghost, rude comes with the territory."


    show bg ch7follow14 with dissolve
    sa "Doesn't matter, the word says the whole city's looking for you, Ghost."
    if sa_name == "Sasha":
        p "It's Sasha, right?"
        sa "Yeah..."
    else:
        p "*Exhales* What's your name, so I can stop calling you Bolter."
        $ sa_name = "Sasha"
        sa "Sasha..."
    menu:
        "Help her up":
            $ sa_score += 1
            show bg ch7follow17 with dissolve
            p "Well, Sasha, doesn't matter what you've heard, the stories are false. Now get up."
            sa "Agh... Thanks."
            show bg ch7follow19 with dissolve
            p "Now, you gonna tell me why you're, and I use the term lightly, shadowing me?"
            show bg ch7follow20 with dissolve
            sa "It was Sesh. Boss man wants you dead after what you did before."
            p "Bullshit. He'd be here with his pals. What's your game?"
            show bg ch7follow18 with dissolve
            sa "For fuck's sake..."
            show bg ch7follow20 with dissolve
            sa "The girl... she's worth a lot of cred if we get her to the Pit."
            p "Why the hell does the Pit have a reward for Gloria?"
            show bg ch7follow21 with dissolve
            sa "Ugh... The Pit looks after its own. She's in trouble."
            p "Bullshit."
            sa "Look, I don't know why, but it's a big windfall."
            p "Fuck me. Baynard, Vostok and now the Pit."
            p "Sasha, you honestly don't seem that bad. Hell, for a bolter, you're practically a saint."
            p "I don't want to see you get hurt, so stay away from this."
            show bg ch7follow18 with dissolve
            sa "..."
            p "Now, I'm walking out those doors. You're walking out five minutes later. No sooner. Understand?"
            sa "Yeah..."
            p "Good. You follow, I'll know."
            jump ch7apartmentoutside
        "Leave her on the floor":



            $ dep += 1
            p "Listen, I don't give a shit what you and your friends heard."
            show bg ch7follow15 with dissolve
            sa "What? That you and your giant titan of a buddy are two crazy psychos?"
            p "Henry? Wow. Couldn't be further from the truth."
            if "ch6missionshoot" in extraevents:
                sa "I saw that look in his eye. And you! You fucking shot me."

                p "True... but if I was a psycho killer, you wouldn't be here sitting on your ass right now."
                show bg ch7follow16 with dissolve
                sa "Maybe you had a plan for me?"
                p "For you? Yeah, no."
            else:
                p "You dealt with us once. Did we come off like what you've heard?"
                sa "Well... No. Not so bad, I guess."
                p "Then maybe you don't know the whole story."
            p "Now, you gonna tell me why you're, and I use the term lightly, shadowing me?"
            show bg ch7follow15 with dissolve
            sa "..."
            p "You better speak."
            sa "It was Sesh. Boss man wants you dead after what you did before."
            p "Bullshit. He'd be here with his pals. What's your game?"
            sa "For fuck's sake..."
            show bg ch7follow16 with dissolve
            sa "The girl... she's worth a lot of cred if we get her to the Pit."
            p "Why the hell does the Pit have a reward for Gloria?"
            show bg ch7follow14 with dissolve
            sa "Ugh... The Pit looks after its own. She's in trouble."
            p "Bullshit."
            sa "Look, I don't know why, but it's a big windfall."
            p "Fuck me. Baynard, Vostok and now the Pit."
            p "Sasha, you're in way over your head. You want to stay alive, then get as far away from this as you can. And stay far."
            sa "..."
            p "Now, I'm walking out those doors. You're walking out five minutes later. No sooner. Understand?"
            sa "Yeah..."
            p "Good. You follow, I'll know."
            jump ch7apartmentoutside


label ch7apartmentoutside:
    scene black with dissolve
    if "ch7vicredmoon" in extraevents:
        show bg ch7outside3 with dissolve
        p "Damn, Sam, he did a number on me."
        s "My heart breaks for you, Sir."
        p "... Let's just get out of here."
    else:
        show bg ch7outside1 with dissolve
        if "ch7sashaconfront" in extraevents:
            p "The fucking Pit, just what we needed."
        else:
            p "That girl better not cause us problems..."


    if "ch5visitchandra" in extraevents and (c_score >= 2 or ab_score >= 1) and "ch7chandrahelp" not in extraevents:
        $ extraevents.append("ch7chandrahelp")
    if "ch5visitchandra" in extraevents and "ch5chandrastop" in extraevents and "ch5chandrareallybad" not in extraevents:
        $ extraevents.append("ch7chandrahelpbad")



    s "Sir, you have an incoming call."
    p "Do I want to take it?"
    s "Hard to say, Sir."
    p "Who is it?"
    s "Ms. White, the younger."
    show bg ch7outside4 with dissolve
    if "ch7chandrahelp" in extraevents:
        p "Wouldn't be a day without that brat livening it up. Answer it, Sam."
        show bg ch7outside5 with dissolve
        c "What's up, [p]! Guess who has some prime info for you!"
        p "Gonna go with you."
        c "Fuck to the yes."
        c "If you want it, meet me and Abby for brunch. You remember that cafe on Musk Blvd?"
        menu:
            "On my way":
                $ extraevents.append("ch7chandrameet")
                p "Yeah I know the place; I'm nearby."
                c "Baller Baller, Silver Dollar, see ya soon."
                jump ch7apartmentend
            "No time":
                $ extraevents.append("ch7chandrainfo")
                p "I'd love to, except for being in the middle of the shit right now. Don't have time for games..."
                c "Well fuck... Fine! I'll give you this one. Mom got a call earlier, said they saw someone important at Redondo Beach."
                c "Soon as she heard that she dipped the fuck out."
                p "Well, that is definitely something."
                c "Sweet! Did I help?"
                if "ch7victell" in extraevents:
                    p "You certainly confirmed it."
                else:
                    p "Maybe. Thanks, Chandra."
                c "You owe me."
                p "Sure-sure, sorry, but I gotta go."
                jump ch7apartmentend
    elif "ch7chandrahelpbad" in extraevents:
        $ extraevents.append("ch7chandrajosh")
        $ extraevents.append("ch7chandrainfo")
        p "She better have something useful to say."
        show bg ch7outside6 with dissolve
        c "[p]..."
        p "What is it, Chandra?"
        c "You're going to keep to your promise, right?"
        p "Dealing with that Josh character? Yeah, you have my word."
        c "Good, Mom got a call earlier, said they saw someone important on Redondo Beach. Soon as she heard that, she dipped the fuck out."
        p "Alright, that could actually be useful. Thanks."
        c "Whatever. You better stick to your promise."
        jump ch7apartmentend
    elif "ch3chandranice" in extraevents or "ch3chandramean" in extraevents:
        p "Fuck me, what does she want."

        if "ch3chandranice" in extraevents:
            show bg ch7outside5 with dissolve
            c "[p], I think I owe you for helping my friend the other night."
            p "I appreciate the offer, Chandra, but I don't think there's much you could do for me right now."
            c "Even if I have some info on what mom is doing?"
            c "Meet me and Abby for brunch. You remember that Cafe on Musk Blvd? I'll tell ya there."

            menu:
                "On my way":
                    $ extraevents.append("ch7chandrameet")
                    p "Yeah I know the place; I'm nearby."
                    c "Baller Baller, Silver Dollar, see ya soon."
                    jump ch7apartmentend
                "No time":
                    $ extraevents.append("ch7chandrainfo")
                    p "I'd love to, except for being in the middle of the shit right now. Don't have time for games..."
                    c "Well fuck... Fine! I'll give you this one. Mom got a call earlier, said they saw someone important at Redondo Beach."
                    c "Soon as she heard that she dipped the fuck out."
                    p "Well, that is definitely something."
                    c "Sweet! Did I help?"
                    if "ch7victell" in extraevents:
                        p "You certainly confirmed it."
                    else:
                        p "Maybe. Thanks, Chandra."
                    c "You owe me."
                    p "Sure-sure, sorry, but I gotta go."
                    jump ch7apartmentend
        else:

            $ extraevents.append("ch7chandrainfo")
            p "Whatever, answer it. Let's see what the brat has to say."
            show bg ch7outside6 with dissolve
            c "Yo, [p]. You may be a shitbird, but you did me a solid. So I'm gonna do one for you."
            p "You? Going out of your way to help me?"
            c "I don't like owing people."
            p "You give no shits about owing people."
            c "It fucks over my bitch Mom at the same time, good enough?"
            p "So what's this favor?"
            c "Info. Mom just got a call, said they saw someone important on Redondo Beach. Soon as she heard that, she dipped the fuck out."
            p "That might actually be useful. Thanks."
            c "Yeah, you're welcome. In the future try not to be such a giant swinging cock."
            p "Nah, I'm good where I am."
            c "Prick."
            jump ch7apartmentend
    else:
        $ extraevents.append("ch7chandrainfo")
        $ extraevents.append("ch7chandrajosh")
        p "Whatever, answer it. Let's see what the brat has to say."
        show bg ch7outside6 with dissolve
        c "Hey."
        p "Is there a reason you're calling or are you just here to fucking bother me?"
        c "There's a reason, you cunt discharge."
        c "I want you to kick some dude's ass for me."
        p "Yeah, not happening."
        c "I can fucking pay you!"
        p "Not enough."
        c "I know that Mom's been chasing you down and I got info for you. You want it or not?"
        p "Yes, I want it."
        c "If I do, you'll end this fucker? Promise?"
        p "Fine, just fucking tell me."
        c "Redondo Beach. Someone told that bitch about it and she ran out. I'll call you when I know where Josh is."
        n "Chandra hangs up"
        jump ch7apartmentend

label ch7apartmentend:
    if "ch7sashaignore" in extraevents:
        show bg ch7outside7 with dissolve
        s "She is still following us, Sir."
        if "ch7chandrameet" in extraevents:
            p "Don't worry, we'll lose her on the way to the Cafe."
        else:
            p "Don't worry, we'll lose her on the way back to Betty's."
        show bg ch7outside8 with dissolve
        if "ch7chandrainfo" in extraevents and "ch7victell" not in extraevents:
            p "Sam, send that info about Redondo Beach to Betty. May help them out."
            s "Sent, Sir."
        n "The engine roars as you fire up the ignition"
        show bg ch7outside9 with dissolve
        s "She is trailing behind by a few cars; a black motorcycle."
        p "I see her."
        show bg ch7outside12 with dissolve
        p "Alright, baby, let's show this Bolter what you can do."
        show bg ch7outside10 with dissolve
        p "See ya!"
        show bg ch7outside11 with hpunch
        $ renpy.pause(1)
        show bg ch7outside13 with dissolve
        $ renpy.pause(1)
        show bg ch7outside14 with dissolve
        sa "How the hell?!"
        show bg ch7outside15 with dissolve
        sa "*Sigh* You gotta be fucking kidding me..."
        if "ch7chandrameet" in extraevents:
            jump ch7brunch
        else:
            jump ch7sonja
    else:
        show bg ch7outside8 with dissolve
        if "ch7chandrainfo" in extraevents and "ch7victell" not in extraevents:
            p "Sam, send that info about Redondo beach to Betty. May help them out."
            s "Sent, Sir."
        if "ch7chandrameet" in extraevents:
            p "Alright, Sam, let's go see what Chandra has."
            jump ch7brunch
        else:
            p "Alright, Sam, back to Betty's."
            jump ch7sonja
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
