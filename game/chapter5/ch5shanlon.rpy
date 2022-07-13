
image bg ch5shanloncall1 = "ch5shanloncall1"
image bg ch5shanloncall2 = "ch5shanloncall2"
image bg ch5shanloncall3 = "ch5shanloncall3"
image bg ch5shanloncall4 = "ch5shanloncall4"
image bg ch5shanloncall5 = "ch5shanloncall5"
image bg ch5shanloncall6 = "ch5shanloncall6"
image bg ch5shanloncall7 = "ch5shanloncall7"
image bg ch5shanloncall8 = "ch5shanloncall8"
image bg ch5shanloncall9 = "ch5shanloncall9"
image bg ch5shanloncall10 = "ch5shanloncall10"
image bg ch5shanloncall11 = "ch5shanloncall11"
image bg ch5shanloncall12 = "ch5shanloncall12"
image bg ch5shanloncall13 = "ch5shanloncall13"
image bg ch5shanloncall14 = "ch5shanloncall14"
image bg ch5shanloncall15 = "ch5shanloncall15"
image bg ch5shanloncall16 = "ch5shanloncall16"


label ch5shanlon:
    s "Hold on -- an incoming call from a Shanlon Russell, Sir."
    menu:
        "Ignore it":
            p "Fuck that."
            s "Not sure how to do that, Sir."
            p "Ignore it."
            s "Of course, Sir."
            if "ch2broken" in extraevents:
                s "Sir, she is calling again."
                menu:
                    "Answer":
                        p "For fuck's sake. Answer it, Sam."
                        jump ch5shanlonbreak
                    "Ignore":
                        p "Let her squirm."
                        s "Yes, Sir."
                        p "She hang up?"
                        s "Yes."
                        p "Good."
                        s "However..."
                        p "Seriously, Sam?"
                        s "Afraid so, Sir. Ignore it again? She seems quite insistent."
                        menu:
                            "Answer":
                                $ extraevents.append("ch5shanlonignore")
                                p "Just shut it and answer it, Sam."
                                jump ch5shanlonbreak
                            "Ignore and Block":
                                $ extraevents.append("ch5shanlonblock")
                                p "She wants attention. Sam, block that witch."
                                s "Done, Sir. Blocking Shanlon Russell."
                                return
            else:

                return
        "Answer it":
            p "Answer it, Sam."
            if "ch2broken" in extraevents:
                jump ch5shanlonbreak
            else:
                jump ch5shanlonnormal


label ch5shanlonbreak:

    if shanlonsexname == False:
        $ shanlonsexname = p

    if "ch5shanlonignore" in extraevents:
        show bg ch5shanloncall2 with dissolve
        sh "What the hell took you so long?"
        p "Maybe I don't like dealing with clingy whores. It's a waste of my time."
        $ s_lust += 1
        show bg ch5shanloncall4 with dissolve
        sh "Mmm, [shanlonsexname], I wouldn't waste your time."
    else:
        show bg ch5shanloncall1 with dissolve
        sh "Ah, good. I was afraid you wouldn't pick up."
    p "What do you want? And make it fast."
    show bg ch5shanloncall3 with dissolve
    sh "What do you think I want? A story, with a side of punishment."
    p "I don't run on your schedule. These things take time."
    show bg ch5shanloncall5 with dissolve
    sh "You fucking dog! We had a deal!"
    p "These things take time."
    sh "Fine, fucking [shanlonsexname]."
    p "Better."
    show bg ch5shanloncall6 with dissolve
    sh "I want you over here."
    show bg ch5shanloncall7 with dissolve
    sh "Rip my clothes off..."
    p "When I feel like it."
    sh "But, I need you to hurt me again. Make me your worthless whore."
    menu:
        "Oh yeah?":
            p "Yeah, you need me over there again?"
            show bg ch5shanloncall9 with dissolve
            sh "Yes. I want you to fuck my throat again until I cry all over your cock."
        "You are worthless":
            p "Yeah, you are my worthless cheap whore, aren't you? Can't live without me, after fucking a real man?"
            show bg ch5shanloncall8 with dissolve
            sh "That's right. I want you to fuck my ass with that big cock, then force-feed it down my throat."
            p "Is that it?"
            show bg ch5shanloncall9 with dissolve
            sh "No, I deserve to be choked like a stupid bitch. Then slapped for calling you a dog -- you dog."
            $ s_lust += 1

    p "You'll have to wait. But stay wet for me."
    if s_lust >= 3:
        show bg ch5shanloncall10 with dissolve
        sh "Then I'll have to have fun with myself."
        sh "I'll take this, and--"
        show bg ch5shanloncall11 with dissolve
        n "Shanlon gags down on the dildo"
        p "(What the hell is wrong with her?)"
        show bg ch5shanloncall12 with dissolve
        sh "I want you to fucking wreck me."
        p "Less talking, more gagging you slut."
        show bg ch5shanloncall13 with dissolve
        p "Harder."
        sh "Mmmmphh!!!!"
        show bg ch5shanloncall14 with dissolve
        sh "Do you want me, [shanlonsexname]?"
        p "Nope, you disgust me. But, you do need punishment."
        show bg ch5shanloncall15 with dissolve
        sh "Yes! Fucking slap me while you fuck me!"
        p "Then what?"
        sh "Then bend me over and ram my tight hole!"
        p "You want to get fucked like a dog again?"
        show bg ch5shanloncall16 with dissolve
        sh "YES!! You fucking asshole! YES!!!"
        sh "OH FUCK! YES!"
        p "Too bad. I'm busy."
        sh "Oh god! Fuck my ass!!! Treat me-"
    else:
        show bg ch5shanloncall6 with dissolve
        sh "*Sighs* Don't wait long. I may grow tired of you."
        p "Your loss."
        sh "Bye, [shanlonsexname]."
        return

    p "Sam, end call."
    show bg ch5drive10 with dissolve
    s "Call terminated, Sir."
    p "Thank you."
    return





label ch5shanlonnormal:
    show bg ch5shanloncall2 with dissolve
    sh "I haven't heard from you. Too busy playing in the yard?"
    p "What do you want, Miss Russell?"
    show bg ch5shanloncall3 with dissolve
    sh "We had a deal."
    p "Don't worry; you'll get your story."
    if "ch2shanlon" in extraevents:
        sh "I better. I want something good, not some random rumors!"
    else:
        sh "I better. Something good."
    show bg ch5shanloncall1 with dissolve
    sh "Also, what happened with the girl? I hear you haven't brought her in yet."
    p "We're done here."
    show bg ch5shanloncall5 with dissolve
    sh "Hey, you fucking-"
    p "Hang up, Sam."
    show bg ch5drive10 with dissolve
    s "Of course, Sir."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
