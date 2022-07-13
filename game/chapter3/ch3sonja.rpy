
image bg ch3sonja1 = "ch3sonja1"
image bg ch3sonja2 = "ch3sonja2"
image bg ch3sonja3 = "ch3sonja3"
image bg ch3sonja4 = "ch3sonja4"
image bg ch3sonja5 = "ch3sonja5"
image bg ch3sonja6 = "ch3sonja6"
image bg ch3sonja7 = "ch3sonja7"
image bg ch3sonja8 = "ch3sonja8"
image bg ch3sonja9 = "ch3sonja9"
image bg ch3sonja10 = "ch3sonja10"
image bg ch3sonja11 = "ch3sonja11"
image bg ch3sonja12 = "ch3sonja12"
image bg ch3sonja13 = "ch3sonja13"
image bg ch3sonja14 = "ch3sonja14"
image bg ch3sonja15 = "ch3sonja15"
image bg ch3sonja16 = "ch3sonja16"
image bg ch3sonja17 = "ch3sonja17"
image bg ch3sonja18 = "ch3sonja18"
image bg ch3sonja19 = "ch3sonja19"
image bg ch3sonja20 = "ch3sonja20"
image bg ch3sonja21 = "ch3sonja21"
image bg ch3sonja22 = "ch3sonja22"
image bg ch3sonja23 = "ch3sonja23"
image bg ch3sonja24 = "ch3sonja24"
image bg ch3sonja25 = "ch3sonja25"



image ch3sonja = Movie(play='video/chapter-3-video/ch3sonja.webm', loop=False)
image bg ch3sonja movie:
    "ch3sonja"
    pause 6.6
    "ch3sonja26"


label ch3sonja:
    play music audio.calm fadein 2.0 fadeout 2.0
    scene black with Dissolve(2)
    p "Hey, Sonja, it's me."
    show bg ch3sonja1 with dissolve
    j "How long did the lock take you?"
    p "Forty-two seconds."
    show bg ch3sonja3 with dissolve
    j "Getting slow."
    p "Wasn't trying that hard."
    j "What brings you to my humble abode?"
    p "Just looking for a bit of help."
    show bg ch3sonja2 with dissolve
    j "Well, you came to the right place."
    j "Sorry, was just getting dressed."
    p "Nothing I haven't seen before."
    if e_score >= 2 and "ch1ellen" in extraevents:
        menu:
            "Confront her about Ellen":
                $ extraevents.append("ch3sonjasorry")
                p "Before we get started though, we need to clear the air about you being a total bitch the other night..."
                show bg ch3sonja5 with dissolve
                j "Well, fuck you too!"
                p "Seriously. Ellen didn't deserve to be treated like that. She's a decent person and you treated her like shit."
                show bg ch3sonja6 with dissolve
                j "Shit, did I?"
                p "Yes..."
                j "I just figured she was some random stand... wait, she's not something serious is she?"
                p "It doesn't matter if she is or not."
                j "..."
                j "No. I'd never try to make things uncomfortable with your girlfriend. I'm sorry."
                p "Don't tell me. Tell it to Ellen if you ever see her again."
                j "I will..."
                p "You have to remember that not everyone is like you, Sonja."
                j "Okay, now I feel like shit. Let's move on, [p]."
                p "Anyway, now that we've gone there, did you get a chance to try Stella out?"
            "Let it slide":
                p "Did you get a chance to try Stella again? Everything in working order?"
    else:
        p "Did you get a chance to try Stella again? Everything in working order?"
    show bg ch3sonja4 with dissolve
    j "No thanks to you, [p]! Poor thing was all dirty. But she's back, baby!"
    show bg ch3sonja7 with dissolve
    j "I took her to the range. It was like she never left."
    p "Shit, Sonja, you look like a kid on Christmas morning."
    show bg ch3sonja8 with dissolve
    j "Perfect precision. Cleared the advanced course in record time with her. *Begins to make gun sound effects.*"
    p "Ha, I'm glad I could keep her safe for you."
    show bg ch3sonja9 with dissolve
    j "Just thinking about it makes my nipples hard enough to cut glass."
    p "Too much info, Sonja."
    show bg ch3sonja10 with dissolve
    j "Oh, fuck off, cum dunt. Pass me my shirt."
    show bg ch3sonja11 with dissolve
    p "Damn, Sonja, when's the last time you washed this?"
    j "I was busy. It was movie night."
    p "And you tell me I need to take care of myself."
    show bg ch3sonja12 with dissolve
    j "Hey, you kept Sam. Manual laundry sucks."
    show bg ch3sonja13 with dissolve
    j "Okay, before you ask, no, I haven't been called in on this job for that girl."
    p "That's good."
    j "As of yet..."
    p "Of course."
    j "So, what do you need?"
    p "Okay, two things. First, I need you to check my place. I think it's bugged."
    show bg ch3sonja14 with dissolve
    j "Got a reason to think that or is this just your usual paranoia?"
    p "I had an unexpected visitor yesterday. Don't know her full intentions but far from trustworthy."
    j "You really need to change your locks."
    p "No shit, best security around, my ass. Can you run a remote scan?"
    show bg ch3sonja15 with dissolve
    j "Probably. Let me see what we can do."
    j "Hey, Kay, you there?"
    n "After a few seconds, some type comes across the screen"
    show bg ch3sonja18 with dissolve
    j "You mind routing into my husband's AI? I'll log you in from here."
    menu:
        "Hold up!":
            p "Wait, I don't know if I'm comfortable with some stranger getting into Sam."
            show bg ch3sonja16 with dissolve
            j "That's adorable. You want my help or not?"
            menu:
                "Fine, carry on.":
                    p "Fuck it, give it a sweep."
                    j "Alright, let's do this."
                    jump ch3sonjabug
                "No, stay out of there.":
                    $ extraevents.append("ch3preventbug")
                    p "I'll assume it is."
                    show bg ch3sonja17 with dissolve
                    $ insult = renpy.random.choice(insults)
                    j "Whatever you say, [insult]."
                    p "Yeah, well, I'd rather people stay away from him."
                    j "No, it's fine. I understand. Not like I gave Sam to you or anything."
                    jump ch3sonjatwo
        "Let her continue":


            jump ch3sonjabug

label ch3sonjabug:
    $ extraevents.append("ch3findbug")
    show bg ch3sonja18 with dissolve
    j "Sweep it, Kay. Standard bug protocol. It'll probably be trying to piggyback on..."
    n "More typing comes onto the screen"
    show bg ch3sonja19 with dissolve
    j "Sorry, Kay... Do your thing."
    n "Sonja continues to watch the screen. New visuals pass by as multiple scans are listed on the monitor."
    show bg ch3sonja20 with dissolve
    j "There you are, ya bastard. It's decently hidden, almost didn't find it. Someone is watching you for sure."
    j "The thing is, there's not much range on it, so they'll have to be close or bounce it off something else."
    p "Can you pinpoint it or shut it off?"
    j "Not from here."
    show bg ch3sonja18 with dissolve
    j "Kay triangulated its position though. It'll be near your weapons locker. Just keep your eyes open for an XF-27 or 28."
    show bg ch3sonja16 with dissolve
    j "Those aren't cheap. Just who exactly is spying on you?"
    p "Who do you think?"
    j "Yeah, forget I asked."
    jump ch3sonjatwo


label ch3sonjatwo:
    j "So what's the next favor?"
    p "You up for a little recon? Locate the target?"
    show bg ch3sonja21 with dissolve
    j "Oh, fuck yes! Let me get my baby!"
    p "Locate, Sonja! Not collect! I need to track her down first. Then we set up a plan."
    j "*Sighs* Fine, ruin my fun. Give me a minute and meet me out front."
    scene black with Dissolve(2)
    show bg ch3sonja23 with dissolve
    p "(It's still early, but the clock is ticking.)"
    show bg ch3sonja22 with dissolve
    p "Your minute's pretty fucking long!"
    $ insult = renpy.random.choice(insults)
    j "Shut it! I'm doing you a favor here, [insult]."
    show bg ch3sonja movie with dissolve
    j "Besides, If I can't take Stella, I'm taking Judy, smaller, but she knows how to get down and dirty."
    p "You named my sidearm Judy?"
    j "Hey, she's mine now."
    p "*Sighs* Fine, but you really need to stop naming your guns."
    show bg ch3sonja24 with dissolve
    $ insult = renpy.random.choice(insults)
    j "Fuck off, [insult]. So, where to?"
    p "Southwestern Mil-town. I have some contacts I need to hit up."
    j "Ahh, we're not even going into Bolter territory. You owe me. I got a few contacts there as well, if we need 'em."
    show bg ch3sonja25 with dissolve
    j "Let's go find your little blonde."
    jump ch3sonjamil
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
