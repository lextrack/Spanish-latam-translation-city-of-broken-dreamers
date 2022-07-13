



label ch7katie:
    k "What's wrong?"
    show bg ch7morning8 with dissolve
    p "Sorry, I didn't mean to wake you."
    k "It's okay, [p]. Did something happen? You seem rattled."
    p "Just a bad dream."
    show bg ch7morning9 with dissolve
    k "Hey, come here. Lay back down."
    p "Katie, it's fine..."
    k "Just get over here, silly."
    show bg ch7morning10 with dissolve
    k "Did you want to talk about it?"
    menu:
        "Tell her":
            p "I was back on an old job. A bad one..."
            k "What happened?"
            p "People died. A lot of people. And I was working for the people who caused it. Baynard, and specifically, Meredith White."
            k "I met her once as a student when she recruited some of us into their R&D track. I never liked her."
            p "You're a good judge of character."
            show bg ch7morning12 with dissolve
            k "Well, [p], she always rubbed me the wrong way."
            show bg ch7morning10 with dissolve
            if "ch1katieknowsvic" in extraevents:
                k "I wonder if I hadn't been kicked out, would I be a corp slave like that redhead you know?"
                if "ch1tellkatie" in extraevents:
                    k "And if you decide you never want to tell me what happened that night with her, I'm for it."
                    p "What night?"
                    k "You told me you were seeing her for drinks."
                    if "ch1vic" not in extraevents:
                        $ k_lust += 1
                        p "Strictly business."
                        k "Still, she's trouble."
                    else:
                        menu:
                            "Partial Truth":
                                $ k_lust += 1
                                p "Yeah, she tried to seduce me. Probably thought it would give her a leg up in negotiations."
                                k "Wow... how can she live like that, using sex as a tool. She's trouble."
                            "Lie":
                                p "Strictly business. We were just discussing payment."
                                k "Still, she's trouble."

                    if "ch4vicgoodbye" in extraevents:
                        p "Maybe. But she's more than that, too. I don't think she's too happy with Meredith right now either."
                        k "What makes you say that?"
                        p "Just a feeling."
                    else:
                        p "Yeah, I agree."


                    if "ch5ellendoc" in extraevents or k_lust >= 6:

                        jump ch7katiestart
                    else:
                        k "Well, you should just relax and try to get some sleep."
                        show bg ch7morning11 with dissolve
                        p "I will-"
                        k "*Begins to snore lightly*"
                        p "Seriously, how does she do that?"
                        jump ch7stairwaynightbefore
            else:

                k "And that assistant of hers..."
                p "Victoria?"
                k "You know her? She's the real creepy one. Trouble with a capital \"T\"."
                if "ch4vicgoodbye" in extraevents:
                    p "Maybe."
                    show bg ch7morning12 with dissolve
                    k "Heh, she's a drone. It's her job to follow the queen's orders."
                    p "Like I said, maybe. But she's more than that, too. I don't think she's too happy with Meredith right now either."
                    if "ch5ellendoc" in extraevents or k_lust >= 6:

                        jump ch7katiestart

                    jump ch7katiesleep
                else:
                    p "You're not wrong."
                    if "ch5ellendoc" in extraevents or k_lust >= 6:

                        jump ch7katiestart

                    jump ch7katiesleep
        "Hold off":



            p "I will... But, not tonight, I... I'm just not up for it right now."
            k "Whenever you're ready. I'll be here to listen, no matter how bad it is. No judgments."
            menu:
                "Tell her about Sonja":
                    $ k_lust += 1
                    p "Well, it involves my wife... Or ex-wife. Or is it estranged? Whatever."
                    show bg ch7morning12 with dissolve
                    k "Sonja, right?"
                    p "You know her?"
                    k "I know most of you guys. Though, I never knew her well. Just patched her up a few years back. I heard she left town."
                    p "Well, she's back now. She's one of the people hunting us."
                    show bg ch7morning10 with dissolve
                    k "Oh... And I thought she was one of the nice ones..."
                    p "\"Nice\" is not a compliment she usually receives."
                    k "Well, she was with me. I don't get it, why's she after you?"
                    p "I'm between her and her target. That's how it works."
                    show bg ch7morning12 with dissolve
                    k "You guys are weird..."
                    p "Heh, yeah I guess we can be."
                    if "ch5ellendoc" in extraevents or k_lust >= 3:

                        jump ch7katiestart
                    else:
                        k "Now, just relax and try to get some sleep."
                        show bg ch7morning11 with dissolve
                        p "I will-"
                        k "*Begins to snore lightly*"
                        p "Damn, you can fall asleep like clockwork."
                        jump ch7stairwaynightbefore
                "In time":

                    p "I will, later, once this is all done."
                    k "Promise?"
                    p "Promise."
                    k "Ok then. Now, just relax and try to get some sleep."
                    show bg ch7morning11 with dissolve
                    p "I will-"
                    k "*Begins to snore lightly*"
                    p "Seriously, how does she do that?"
                    jump ch7stairwaynightbefore
        "It's nothing":

            p "It's nothing, just a nightmare."
            k "It's more than that, but I won't pry. If you ever want to talk..."
            p "Don't think I will."
            k "Ok then. Now, just relax and try to get some sleep."
            show bg ch7morning11 with dissolve
            p "I will-"
            k "*Begins to snore lightly*"
            p "Seriously, how does she do that?"
            jump ch7stairwaynightbefore


label ch7katiesleep:
    k "Well, I shouldn't keep you up any longer. Just relax and try to get some sleep."
    show bg ch7morning11 with dissolve
    p "I will-"
    k "*Begins to snore lightly*"
    p "Seriously, how does she do that?"
    jump ch7stairwaynightbefore
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
