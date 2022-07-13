
image bg ch6sonjabath1 = "ch6sonjabath1"
image bg ch6sonjabath2 = "ch6sonjabath2"
image bg ch6sonjabath3 = "ch6sonjabath3"
image bg ch6sonjabath4 = "ch6sonjabath4"
image bg ch6sonjabath5 = "ch6sonjabath5"
image bg ch6sonjabath6 = "ch6sonjabath6"
image bg ch6sonjabath7 = "ch6sonjabath7"
image bg ch6sonjabath8 = "ch6sonjabath8"
image bg ch6sonjabath9 = "ch6sonjabath9"
image bg ch6sonjabath10 = "ch6sonjabath10"
image bg ch6sonjabath11 = "ch6sonjabath11"
image bg ch6sonjabath12 = "ch6sonjabath12"
image bg ch6sonjabath13 = "ch6sonjabath13"


label ch6sonjabath:
    scene black with Dissolve(1)
    show bg ch6sonjabath1 with Dissolve(1)
    j "You stubborn shit."
    show bg ch6sonjabath2 with dissolve
    j "..."
    j "Look at you... what the fuck are you doing?"
    play sound audio.shatter
    show bg ch6sonjabath3 with hpunch
    j "ARRGH!"
    j "Goddammit, [p]!"
    show bg ch6sonjabath5 with dissolve
    j "*Lets out breath slowly*"
    j "(Why did you have to bring up Caracas?)"
    show bg ch6sonjabath6 with dissolve
    j "(That's the last thing I need right now.)"
    j "(I can't do that again. Dammit, [p].)"
    show bg ch6sonjabath12 with dissolve
    n "Kleo's voice comes in through a room speaker"
    klx "Hey, Sonja, you alright?"
    show bg ch6sonjabath6 with dissolve
    j "Not now, Kay. Just leave me alone."
    klx "..."
    j "*sighs* What?"
    klx "Should I order a replacement mirror?"
    j "Are you spying on me?"
    klx "Psh... I spy on everyone."
    j "Then stop."
    klx "If you want to talk about it..."
    show bg ch6sonjabath7 with dissolve
    j "No."
    klx "Sonja..."
    show bg ch6sonjabath8 with dissolve
    j "Piss off, Kay!"
    klx "We don't need this job."
    show bg ch6sonjabath7 with dissolve
    j "Kay, fucking drop it! I said I'm fine. I'm fucking fine!"
    klx "You don't sound fine. But hey, what do I know. I've only been your friend for how long now?"
    show bg ch6sonjabath9 with dissolve
    j "Shit... I'm sorry, Kay... I shouldn't have yelled at you."
    klx "So can we talk, then?"
    j "Not now... Please?"
    klx "In that case, since you don't want to talk, maybe I can come over, get some booze in ya and-"
    show bg ch6sonjabath10 with dissolve
    j "Good try, Kay. You stay on your own team."
    klx "Teams? What an archaic concept. We're living in the sexual renaissance, enjoy yourself."
    show bg ch6sonjabath12 with dissolve
    klx "How about VR? You don't like it, you can just disconnect."
    j "That doesn't even count."
    klx "Sure it does."
    if "ch1futafull" in extraevents:
        klx "Just ask [p]."
        j "If you're trying to make me jealous it won't work. If I got bent out of shape whenever he hit on some hot-ass bitch I'd be even more wound up than I am now."
        klx "Hot-ass bitch? You DO know just what a girl wants to hear."
    show bg ch6sonjabath11 with dissolve
    j "Hasta mañana, Kay. Get some sleep, I'm doing the same. You can give me shit tomorrow."
    klx "Will do, and I can tell I'm wearing you down!"
    j "Sorry, Kay, there's only one girl I love."
    show bg ch6sonjabath13 with dissolve
    j "And we're gonna be spending a lot of time together soon, aren't we, Stella?"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
