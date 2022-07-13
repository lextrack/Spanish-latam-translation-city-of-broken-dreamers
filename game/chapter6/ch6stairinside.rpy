
image bg ch6stairinside0 = "ch6stairinside0"
image bg ch6stairinside1 = "ch6stairinside1"
image bg ch6stairinside2 = "ch6stairinside2"
image bg ch6stairinside3 = "ch6stairinside3"
image bg ch6stairinside4 = "ch6stairinside4"
image bg ch6stairinside5 = "ch6stairinside5"
image bg ch6stairinside6 = "ch6stairinside6"
image bg ch6stairinside7 = "ch6stairinside7"
image bg ch6stairinside8 = "ch6stairinside8"
image bg ch6stairinside9 = "ch6stairinside9"
image bg ch6stairinside10 = "ch6stairinside10"
image bg ch6stairinside11 = "ch6stairinside11"
image bg ch6stairinside12 = "ch6stairinside12"
image bg ch6stairinside13 = "ch6stairinside13"
image bg ch6stairinside14 = "ch6stairinside14"
image bg ch6stairinside15 = "ch6stairinside15"
image bg ch6stairinside16 = "ch6stairinside16"
image bg ch6stairinside17 = "ch6stairinside17"
image bg ch6stairinside18 = "ch6stairinside18"
image bg ch6stairinside19 = "ch6stairinside19"
image bg ch6stairinside20 = "ch6stairinside20"
image bg ch6stairinside21 = "ch6stairinside21"
image bg ch6stairinside22 = "ch6stairinside22"
image bg ch6stairinside23 = "ch6stairinside23"
image bg ch6stairinside24 = "ch6stairinside24"
image bg ch6stairinside25 = "ch6stairinside25"
image bg ch6stairinside26 = "ch6stairinside26"
image bg ch6stairinside27 = "ch6stairinside27"
image bg ch6stairinside28 = "ch6stairinside28"
image bg ch6stairinside29 = "ch6stairinside29"
image bg ch6stairinside30 = "ch6stairinside30"
image bg ch6stairinside31 = "ch6stairinside31"

image bg ch6stairinside32 = "ch6stairinside32"
image bg ch6stairinside33 = "ch6stairinside33"
image bg ch6stairinside34 = "ch6stairinside34"
image bg ch6stairinside35 = "ch6stairinside35"
image bg ch6stairinside36 = "ch6stairinside36"
image bg ch6stairinside37 = "ch6stairinside37"
image bg ch6stairinside38 = "ch6stairinside38"
image bg ch6stairinside39 = "ch6stairinside39"





label ch6stairinside:
    show bg ch6stairinside1 with dissolve
    b "And you said I was insane. Where did she come from, corporate black site?"
    p "Nah, the rich part of town."
    show bg ch6stairinside2 with dissolve
    b "Well, bring her in. The couch is fine."
    p "Thank you, Betty."
    show bg ch6stairinside3 with dissolve
    p "There ya go."
    show bg ch6stairinside4 with dissolve
    h "[p]..."
    ve "Excuse me, Ma'am. The large one appears to be in some distress."
    show bg ch6stairinside5 with dissolve
    h "Ahh..."
    if h_score >= 3:
        p "Henry?"
    else:
        p "Gibson?"

    p "What is it?"
    show bg ch6stairinside6 with dissolve
    h "I..."
    show bg ch6stairinside7 with vpunch
    n "Henry passes out, crashing onto the floor"
    p "Shit!"
    p "Henry, wake up!"
    show bg ch6stairinside8 with dissolve
    b "What's wrong with him?"
    p "How the fuck should I know?"
    show bg ch6stairinside11 with dissolve
    p "Christ, he isn't breathing."
    show bg ch6stairinside9 with dissolve
    b "In the locker, there are medical supplies, grab them!"
    p "On it!"
    show bg ch6stairinside12 with dissolve
    n "Betty begins to perform CPR on Henry"
    b "Quickly!"
    show bg ch6stairinside10 with dissolve

    jump ch6stairwaylocker


label ch6stairwaylocker:
    menu:
        "Left":
            show bg ch6stairinside17 with dissolve
            p "What the fuck?"
            show bg ch6stairinside13 with dissolve
            b "Not that one!"
            jump ch6stairwaylocker
        "Center":
            show bg ch6stairinside16 with dissolve
            $ extraevents.append("ch6bettyweapons")
            p "Holy..."
            b "Wrong locker, Darling!"
            p "We need to talk about this after."
            show bg ch6stairinside13 with dissolve
            b "The right locker!"
            jump ch6stairwaylocker
        "Right":

            show bg ch6stairinside15 with dissolve
            p "Perfect, got it!"
            b "Quick, get the epi hypo, it should give him a nice jolt to the system."
            show bg ch6stairinside14 with dissolve
            b "Venus, honey, watch the girl, will ya?"
            ve "Yes, Ma'am."
            jump ch6stairwayhenryfix

label ch6stairwayhenryfix:
    show bg ch6stairinside18 with dissolve
    p "Fuck, I hope this works, his skin is practically bulletproof."
    b "I deal with Milchers in here sweets, that sucker is tungsten, good luck breaking it. Now, try his neck."
    p "I hope I'm strong enough to push it in."
    b "Phrasing dear."
    show bg ch6stairinside19 with dissolve
    p "Fuck me, it's no use!"
    show bg ch6stairinside32 with dissolve
    b "Venus, dear!"
    show bg ch6stairinside33 with dissolve
    ve "Yes?"
    b "Run emergency protocol \"code blue\"."
    show bg ch6stairinside34 with dissolve
    ve "Of course."
    show bg ch6stairinside35 with dissolve
    ve "Loading protocol."
    show bg ch6stairinside36 with dissolve
    ve "Syringe."
    show bg ch6stairinside37 with dissolve
    $ renpy.pause(1)
    show bg ch6stairinside38 with vpunch
    n "With a sharp downward jab, Venus plunges the needle straight into Henry's chest"
    p "Holy shit!"
    show bg ch6stairinside39 with dissolve
    ve "Anything else?"
    b "Ahh, no, dear, thank you."


    show bg ch6stairinside20 with dissolve
    p "Dammit, Henry, wake up! Why isn't it working?"
    b "Give it a second!"
    n "Henry's body jerks as he sucks in a gasp of breath."
    ve "He appears to be alive, Ma'am."
    b "Yes. Good job, Venus, dear. Glad I created that little protocol for you."
    show bg ch6stairinside21 with dissolve
    b "*Sighs in relief* [p], what's happening to him?"
    p "I'm not sure... It has to be because of this."
    show bg ch6stairinside25 with dissolve
    b "A gen one? Shit. Thought they were extinct. Should have figured it out just from the size of him."
    show bg ch6stairinside22 with dissolve
    b "You have strange friends and stranger enemies."
    if h_score >= 3:
        p "Friend?"
        p "It didn't start that way, but yeah, I guess so. We tried to kill each other the first time we met."
        p "But, he's more honest a man than anyone I've met."
        p "And he has a simple mission in life. The same one I do."
    else:
        p "I wouldn't say we are friends."
        p "Under normal circumstances, I'm pretty sure he would love to crush my skull."
        p "But, right now, we have the same goal."


    b "Which is?"
    show bg ch6stairinside23 with dissolve
    $ renpy.pause(1)
    show bg ch6stairinside24 with dissolve
    if "ch4vicaccept" in extraevents:
        p "Whatever ends up being best for her. For everyone."
    else:
        p "Keeping her safe."
    show bg ch6stairinside26 with dissolve
    ve "What's the pretty one's name?"
    p "That's Gloria. Sweet kid, unless she is blowing you across the room by accident."
    show bg ch6stairinside27 with dissolve
    ve "How does one perform fellatio by accident?"
    show bg ch6stairinside28 with dissolve
    b "Sorry, she still needs work, she's stuck in princess mode right now. What about tall dark and handsome here?"
    p "Handsome? No love for me?"
    show bg ch6stairinside30 with dissolve
    b "Pfft, you're a decade too young and besides, you're not my type. Plus LOOK at him."
    p "Heh, I'm sure he'd be flattered."
    show bg ch6stairinside29 with dissolve
    b "He may be out of the woods for now, but he still needs a doctor."
    p "I know one, but it's too hot right now to go and get her."
    show bg ch6stairinside31 with dissolve
    b "Let me handle that, Darling."
    jump ch6getdoc
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
