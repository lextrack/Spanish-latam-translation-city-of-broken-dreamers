
image bg ch6ellen1 = "ch6ellen1"
image bg ch6ellen2 = "ch6ellen2"
image bg ch6ellen3 = "ch6ellen3"
image bg ch6ellen4 = "ch6ellen4"
image bg ch6ellen5 = "ch6ellen5"
image bg ch6ellen6 = "ch6ellen6"
image bg ch6ellen7 = "ch6ellen7"
image bg ch6ellen8 = "ch6ellen8"
image bg ch6ellen9 = "ch6ellen9"
image bg ch6ellen10 = "ch6ellen10"
image bg ch6ellen11 = "ch6ellen11"
image bg ch6ellen12 = "ch6ellen12"
image bg ch6ellen13 = "ch6ellen13"
image bg ch6ellen14 = "ch6ellen14"
image bg ch6ellen15 = "ch6ellen15"
image bg ch6ellen16 = "ch6ellen16"
image bg ch6ellen17 = "ch6ellen17"
image bg ch6ellen18 = "ch6ellen18"
image bg ch6ellen19 = "ch6ellen19"
image bg ch6ellen20 = "ch6ellen20"
image bg ch6ellen21 = "ch6ellen21"
image bg ch6ellen22 = "ch6ellen22"
image bg ch6ellen23 = "ch6ellen23"
image bg ch6ellen24 = "ch6ellen24"
image bg ch6ellen25 = "ch6ellen25"
image bg ch6ellen26 = "ch6ellen26"
image bg ch6ellen27 = "ch6ellen27"
image bg ch6ellen28 = "ch6ellen28"
image bg ch6ellen29 = "ch6ellen29"
image bg ch6ellen30 = "ch6ellen30"
image bg ch6ellen31 = "ch6ellen31"
image bg ch6ellen32 = "ch6ellen32"
image bg ch6ellen33 = "ch6ellen33"
image bg ch6ellen34 = "ch6ellen34"
image bg ch6ellen35 = "ch6ellen35"
image bg ch6ellen36 = "ch6ellen36"
image bg ch6ellen37 = "ch6ellen37"







label ch6ellen:
    play music audio.futurenoir fadein 2.0 fadeout 2.0
    scene black with Dissolve(2)
    show bg ch6ellen1 with Dissolve(2)
    n "Victoria stares out the window into the morning sky. She waits by Ellen's bed, singing to herself."
    show bg ch6ellen2 with dissolve
    v "{i}Yofuke no kohsoku de{/i}"
    show bg ch6ellen3 with dissolve
    v "{i}Nemuri ni tsuku koro{/i}"
    show bg ch6ellen4 with dissolve
    v "{i}Halogen light dake ayashiku kagayaku{/i}"
    show bg ch6ellen5 with dissolve
    v "{i}Kohri no yohni tsumetai onnadato{/i}"
    show bg ch6ellen6 with dissolve
    v "{i}Sasayaku koe ga shitemo don't worry!{/i}"
    show bg ch6ellen7 with dissolve
    $ renpy.pause(1)
    show bg ch6ellen12 with dissolve
    e "*Moans* Wha..?"
    show bg ch6ellen10 with dissolve
    v "Ah, you're awake. Thank..."
    show bg ch6ellen16 with dissolve
    e "Wait! What the hell is going on? Where the prime fuck am I!?"
    show bg ch6ellen9 with dissolve
    v "You're in Baynard General. You had quite a fall. Excuse my appearance, but I needed to change."
    show bg ch6ellen17 with dissolve
    e "Cool as fucking ice, aren't you? Get me the fuck out of here."
    v "Miss Lane, please. I think you should-"
    show bg ch6ellen13 with dissolve
    e "Why the prime hell can't I move? What the fuck did you do to me!"
    v "Ellen, please calm down, you are very lucky."
    e "The fuck you mean I'm lucky? I-I can't feel anything!"
    show bg ch6ellen10 with dissolve
    v "That is by design. You had some spinal damage, but I saw to your treatment. The surgeon said that your nerve transplant went well. You should regain feeling in another day, two at most."
    v "Now, can I get you something? Some water, perhaps?"
    show bg ch6ellen17 with dissolve
    e "Sure, then maybe I can drown you in it."
    show bg ch6ellen11 with dissolve
    v "That was uncalled for, Ellen. Now, I understand this is a difficult situation..."
    show bg ch6ellen16 with dissolve
    e "Oh, just fucking can it and talk like a real person for once in your life."
    v "Excuse me?"
    show bg ch6ellen15 with dissolve
    e "Sure, you can seduce someone. You're fucking tops at that. You wear a slutty dress, say the right words and you got 'em eating right out of your pussy."
    e "But, show some real fucking compassion? You have no fucking clue."
    show bg ch6ellen11 with dissolve
    v "I-"
    show bg ch6ellen17 with dissolve
    e "\"A difficult situation,\" she says. I can't fucking move! Because of you and your goddamn overlords!"
    v "I never wanted that, Ellen, you have to understand this was an unfortunate-"
    show bg ch6ellen14 with dissolve
    e "Shit! You almost make me believe it. How fucked up is that?"
    e "You gonna tell me how much you like my music again, so we can bond while you slip dirty jobs to me?"
    show bg ch6ellen18 with dissolve
    v "I do like your music..."
    show bg ch6ellen16 with dissolve
    e "The fuck you do. Everything you do and say is a lie."
    show bg ch6ellen19 with dissolve
    v "I wasn't lying to you, Ellen."
    e "Bullshit! You knew what Gloria could do! Why didn't that come up?"
    show bg ch6ellen20 with dissolve
    v "I only just found out..."
    e "Point to you, bitch. You played me. I thought I was going to be helping her."
    e "I should have known it was too good to be true. Nothing good happens in Mil-town. Not anymore."
    show bg ch6ellen21 with dissolve
    v "I was doing what I was told to do, Ellen."
    e "You're just a fucking robot, you know that. Lie on command, jump on command. Probably fucked [p] on command too."




    if "ch1vic" in extraevents:
        $ vicsexcount += 1
    if "ch2vicsex" in extraevents:
        $ vicsexcount += 1
    if "ch4vicsex" in extraevents:
        $ vicsexcount += 1
    if "ch4vicdep" in extraevents:
        $ vicsexcount += 1




    if vicsexcount > 0:
        v "I was ordered to, yes..."
        e "Called it. And knowing that horny dumb ass he fell for it, too. Fuck him once and he'll do whatever you want, right?"

        if vicsexcount == 3 and "ch4vicaccept" not in extraevents:
            show bg ch6ellen24 with dissolve
            v "Three times actually."
            e "Whoop de fucking doo! I fucked him more than that. With him, it doesn't mean shit."
            if "ch4vicsex" in extraevents and "ch5ellenvic" in extraevents:
                show bg ch6ellen28 with dissolve
                v "It wasn't what you think. Not anymore. I haven't experienced that before."
                e "So you're gonna tell me he fucked you straight?"
                e "He's good, but not that good."
                show bg ch6ellen27 with dissolve
                v "Believe what you want."

                show bg ch6ellen25 with dissolve
                e "Holy shit. You're not lying, are you?"
                v "I have been honest this entire conversation."
                e "It's you. That dumb shit fell for you even though you're trying to kill him!"
                $ v_score += 1
                show bg ch6ellen26 with dissolve
                v "If you believe nothing else, Ellen, please know I do not wish him dead. Far from it."
                e "Holy fuck."
                show bg ch6ellen28 with dissolve
                v "And what do you mean, he fell for me?"
                show bg ch6ellen30 with dissolve
                e "Oh, piss off. I'm lying here paralyzed in a goddamn hospital rattling bones with the enemy. We aren't doing high school gossip about boys."
                show bg ch6ellen26 with dissolve
                v "Is that what this is? I wouldn't know. I entered the program at 14."
                e "Yeah, I didn't do high school either. I was on tour, finally some common ground."

            if "ch5ellenkiss" in extraevents:
                show bg ch6ellen25 with dissolve
                v "You seem distraught. Did I misunderstand your relationship with him?"
                show bg ch6ellen30 with dissolve
                e "The fuck are you talking about? We're just fuckbuddies. That's... all."
                $ e_score -= 2
                e "(That stupid fucker. Should never have let him kiss me.)"

        elif vicsexcount == 2 and "ch4vicaccept" not in extraevents:
            show bg ch6ellen23 with dissolve
            v "Two times actually."
            e "You fucked him twice! That horny fucking bastard."

            if "ch4vicsex" in extraevents and "ch5ellenvic" in extraevents:
                show bg ch6ellen28 with dissolve
                v "It wasn't what you think. Not anymore. I haven't experienced that before."
                e "So you're gonna tell me he fucked you straight?"
                e "He's good, but not that good."
                show bg ch6ellen27 with dissolve
                v "Believe what you want."

                show bg ch6ellen25 with dissolve
                e "Holy shit. You're not lying, are you?"
                v "I have been honest this entire conversation."
                e "It's you. That dumb shit fell for you even though you're trying to kill him!"
                $ v_score += 1
                show bg ch6ellen26 with dissolve
                v "If you believe nothing else, Ellen, please know I do not wish him dead. Far from it."
                e "Holy fuck."
                show bg ch6ellen28 with dissolve
                v "And what do you mean, he fell for me?"
                show bg ch6ellen30 with dissolve
                e "Oh, piss off. I'm lying here paralyzed in a goddamn hospital rattling bones with the enemy. We aren't doing high school gossip about boys."
                show bg ch6ellen26 with dissolve
                v "Is that what this is? I wouldn't know. I entered the program at 14."
                e "Yeah, I didn't do high school either. I was on tour, finally some common ground."





            if "ch5ellenkiss" in extraevents:
                show bg ch6ellen25 with dissolve
                v "You seem distraught. Did I misunderstand your relationship with him?"
                show bg ch6ellen30 with dissolve
                e "The fuck are you talking about? We're just fuckbuddies. That's... all."
                $ e_score -= 1
                e "(That mother fucker, I even kissed him!)"

        elif vicsexcount == 1 and "ch4vicaccept" not in extraevents:
            show bg ch6ellen22 with dissolve
            v "Yes, just the one time."
            e "Guess he couldn't resist the voodoo. Could have gone a while without that info."
            if "ch5ellenkiss" in extraevents:
                show bg ch6ellen25 with dissolve
                v "You seem distraught. Did I misunderstand your relationship with him?"
                show bg ch6ellen30 with dissolve
                e "The fuck are you talking about? We're just fuckbuddies. That's... all."
            v "You are taking this news differently than I expected."
            e "What, expecting me to get jealous? I'm not like that. Soo sorry."
            show bg ch6ellen26 with dissolve
            v "No, not at all, I just want to be honest with you."
            show bg ch6ellen29 with dissolve
            e "Why start now? I was just getting used to you being a lying whore."

            if "ch4vicsex" in extraevents:
                show bg ch6ellen28 with dissolve
                v "It wasn't what you think. Not anymore. I haven't experienced that before."
                e "So you're gonna tell me he fucked you straight?"
                e "He's good, but not that good."
                show bg ch6ellen27 with dissolve
                v "Believe what you want."
                if "ch5ellenvic" in extraevents:
                    show bg ch6ellen25 with dissolve
                    e "Holy shit. You're not lying, are you?"
                    v "I have been honest this entire conversation."
                    e "It's you. That dumb shit fell for you even though you're trying to kill him!"
                    $ v_score += 1
                    show bg ch6ellen26 with dissolve
                    v "If you believe nothing else, Ellen, please know I do not wish him dead. Far from it."
                    e "Holy fuck."
                    show bg ch6ellen28 with dissolve
                    v "And what do you mean, he fell for me?"
                    show bg ch6ellen30 with dissolve
                    e "Oh, piss off. I'm lying here paralyzed in a goddamn hospital rattling bones with the enemy. We aren't doing high school gossip about boys."
                    show bg ch6ellen26 with dissolve
                    v "Is that what this is? I wouldn't know. I entered the program at 14."
                    e "Yeah, I didn't do high school either. I was on tour, finally some common ground."
                else:
                    e "Holy shit, the ice queen is offended. Maybe he is that good."
                    show bg ch6ellen26 with dissolve
                    v "It was more than that."
                    if "ch5ellenkiss" in extraevents:
                        show bg ch6ellen30 with dissolve
                        e "Did you kiss him?"
                        v "I did."
                        e "Just fucking prime..."

        if "ch4vicaccept" in extraevents:
            show bg ch6ellen26 with dissolve
            v "I was told to do that, yes."
            e "Hopefully, he stood you up."
            show bg ch6ellen28 with dissolve
            v "On the contrary. He was more than willing."
            show bg ch6ellen30 with dissolve
            e "Mother fucker..."
            if "ch5ellenkiss" in extraevents:
                $ e_score -= 1
                e "And to think I kissed him..."
                show bg ch6ellen26 with dissolve
                v "Ellen, I understand you must be feeling quite angry, with me, with him, with this entire situation."
                v "But your feelings are simply irrelevant at this time."
                v "The situation continues to escalate, far past your ability to stop it."
                show bg ch6ellen29 with dissolve
                e "Fuck you! When I get out of here..."
                v "Then this entire situation will be over."
                e "And a girl's life will be too. Or close enough to it."
                show bg ch6ellen27 with dissolve
                v "This world eats up innocent girls every day. You know that as well as I do."
                jump ch6ellencont
    else:



        show bg ch6ellen26 with dissolve
        v "She did..."
        e "Ha, of course, and knowing that horny fucking bastard he jumped right in."
        show bg ch6ellen25 with dissolve
        v "Actually, he refused all my advances."
        e "Oh, shit, what I wouldn't give to have seen the look on your face when that happened."
        e "Not used to rejection, are you?"
        show bg ch6ellen28 with dissolve
        v "Not in quite some time..."
        $ e_score += 1
        v "It was unexpected."
        show bg ch6ellen29 with dissolve
        e "Fucking prime."
        v "Ellen, your friend has complicated matters greatly. The situation is nearly out of my control and I fear that more people will get hurt."
        e "Like you care."
        show bg ch6ellen27 with dissolve
        v "No matter what you think of me, I want this to come to a peaceful resolution. Don't let this situation ruin your life more than it already is."
        jump ch6ellencont
    show bg ch6ellen28 with dissolve
    v "Listen, Ellen, it was not my intention to hurt anyone. Least of all you. I just want this to end peacefully."
    jump ch6ellencont



label ch6ellencont:
    if "ch4vicaccept" in extraevents:
        show bg ch6ellen31 with hpunch
        n "Ellen uses all her force to spit towards Victoria"
        show bg ch6ellen33 with dissolve
        v "Hmmm, I should have expected this."
        show bg ch6ellen32 with dissolve
        e "How'd you expect me to be!?"
        show bg ch6ellen33 with dissolve
        v "Realistic. Though it was always long odds."
        show bg ch6ellen32 with dissolve
        e "Oh, fuck you! You just want someone to tell you that the hideous shit you pull to climb the Baynard ladder is ok. Go fuck yourself gently with a chainsaw!"
        show bg ch6ellen34 with dissolve
        v "I'm sorry you see things that way. In the fullness of time, however, perhaps you will understand."
        e "*sighs*"
        e "Don't count on it."
        show bg ch6ellen35 with dissolve
        v "Now, if you'll excuse me, I have a meeting."
        e "Another trick to turn?"
        v "I will check in on you later. Get well soon."
    else:
        show bg ch6ellen37 with dissolve
        e "Peacefully? That fucking ended when we got attacked by a cyborg nightmare. That bus has left the station."
        v "No one is dead. You nearly were."
        e "I'm tough."
        show bg ch6ellen26 with dissolve
        v "And Ms. Conner?"
        show bg ch6ellen29 with dissolve
        e "She's fucking tougher than I am. Plus she can go all scanners on you."
        v "It's not me she has to worry about. She will be captured eventually. Nothing you or I say can change that."
        e "And when that happens? Then what?"
        show bg ch6ellen34 with dissolve
        v "I can't answer that, however better our hands than Vostok's."
        e "I'd rather [p] and Henry take out everything you send their way."
        v "Just tell me where they have gone."
        show bg ch6ellen32 with dissolve
        e "Fuck. You."
        show bg ch6ellen26 with dissolve
        v "Ellen, look at me. It would be best for everyone if you {i}helped{/i} me."
        show bg ch6ellen30 with dissolve
        e "Ha, I don't know if its the meds or what, but you don't seem so irresistible anymore. More pathetic, really."
        show bg ch6ellen35 with dissolve
        v "*Sighs* Very well, I'll be back to check on you later. I have a meeting."
        e "Another trick your boss wants you to turn, I'm guessing."
        v "It's... a meeting. Get well soon, Miss Lane."
    show bg ch6ellen36 with dissolve
    e "Fucking prime..."
    jump ch6evening
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
