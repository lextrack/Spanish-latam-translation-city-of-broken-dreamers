
image bg ch6hosp1 = "ch6hosp1"
image bg ch6hosp2 = "ch6hosp2"
image bg ch6hosp3 = "ch6hosp3"
image bg ch6hosp4 = "ch6hosp4"
image bg ch6hosp5 = "ch6hosp5"
image bg ch6hosp6 = "ch6hosp6"
image bg ch6hosp7 = "ch6hosp7"
image bg ch6hosp8 = "ch6hosp8"
image bg ch6hosp9 = "ch6hosp9"
image bg ch6hosp10 = "ch6hosp10"
image bg ch6hosp11 = "ch6hosp11"
image bg ch6hosp12 = "ch6hosp12"
image bg ch6hosp13 = "ch6hosp13"
image bg ch6hosp14 = "ch6hosp14"
image bg ch6hosp15 = "ch6hosp15"
image bg ch6hosp16 = "ch6hosp16"
image bg ch6hosp17 = "ch6hosp17"
image bg ch6hosp18 = "ch6hosp18"
image bg ch6hosp19 = "ch6hosp19"
image bg ch6hosp20 = "ch6hosp20"
image bg ch6hosp21 = "ch6hosp21"



label ch6vic:



    play music audio.futurenoir fadein 8.0 fadeout 2.0

    scene black with Dissolve(2)
    show bg ch6hosp1 with Dissolve(2)
    "Nurse" "She's stabilized, for now. The surgeon is looking over her scans as we speak."
    v "Any permanent damage?"
    show bg ch6hosp2 with dissolve
    $ renpy.pause(1)
    show bg ch6hosp3 with dissolve
    "Nurse" "I can't say, but she is out of danger for now."
    show bg ch6hosp5 with dissolve
    v "I understand, thank you."
    show bg ch6hosp4 with dissolve
    n "Victoria lets out a sigh of relief as she looks down at Ellen"
    v "Ellen, why were you even there? Why did [p] drag you into this?"
    if "ch4vicsex" in extraevents or "ch4vicgood" in extraevents:
        v "If that idiot wants to get himself killed that's his own business. But..."
        v "Damn him."
    else:
        v "This wasn't part of the plan. What is that fool doing?"
    show bg ch6hosp6 with dissolve
    "Red Moon" "Will she survive?"
    show bg ch6hosp15 with dissolve
    v "Ye-yes."
    v "I have to admit my surprise to your concern."
    show bg ch6hosp7 with dissolve
    "Red Moon" "I could say the same."
    v "And, yet you saved her."
    show bg ch6hosp14 with dissolve
    "Red Moon" "She wasn't a target. Her death would accomplish nothing."
    v "No, that it wouldn't."
    show bg ch6hosp8 with dissolve
    v "I suppose you still have some humanity after all."
    "Red Moon" "There, you are wrong."
    show bg ch6hosp11 with dissolve
    v "And why's that?"
    show bg ch6hosp13 with dissolve
    "Red Moon" "I sacrificed that part for my country and my people. A country that no longer exists and people who are left scarred and scattered."
    show bg ch6hosp12 with dissolve
    "Red Moon" "You, on the other hand, sacrificed the same for nothing of true value."
    show bg ch6hosp9 with dissolve
    v "You know nothing about me."
    show bg ch6hosp12 with dissolve
    "Red Moon" "You're an augment, second generation. Did you think I could not tell? Your predecessors, like this Gibson, they did what they did to combat us."
    "Red Moon" "They became monsters to support their government's cowardice and greed. But, for them, it was a greater cause. You did it for personal profit."
    show bg ch6hosp10 with dissolve
    v "Bit hypocritical, aren't you? You aren't doing this for free."
    show bg ch6hosp13 with dissolve
    "Red Moon" "No, I do this for simple reasons. My wards need food and shelter. In doing this I can hunt down a surviving augment."
    v "So it's revenge; for your burned nation?"
    "Red Moon" "Revenge is nothing but the tantrum of a petulant child. No, this is closure. And for that, I go along with your farce."
    show bg ch6hosp11 with dissolve
    v "Farce?"
    show bg ch6hosp16 with dissolve
    "Red Moon" "No need to continue with the lies. I saw the girl's power myself."
    if "ch4vicsex" in extraevents or "ch4vicgood" in extraevents:
        v "You're the second person to tell me that in the last day. What kind of power?"
    else:
        v "What kind of power?"
    "Red Moon" "She flung me and your friend from the walkway as if we were nothing."
    v "Wait, back up. She threw you off the ledge? That's impossible."
    "Red Moon" "One would think so. Yet it occurred."
    v "Bu-but how?"
    show bg ch6hosp17 with dissolve
    "Red Moon" "Unknown, it happened quite quickly. She screamed and I was gone. I had thought I might get answers from you."
    v "I don't..."

    v "I'm not at liberty to share that information."
    "Red Moon" "I see. You had no idea at all. Interesting."
    "Red Moon" "In either case, I was neither informed nor prepared for her. I shall not make the same mistake twice."
    v "As I said I..."
    show bg ch6hosp18 with dissolve
    "Red Moon" "Don't lie to me again. I realize that it's like breathing to you. Know this, I will not be so forgiving in the future. Are we understood?"
    if v_score >= 4:
        show bg ch6hosp18 with dissolve
        v "Yes..."
    else:
        show bg ch6hosp19 with dissolve
        v "I do."
    "Red Moon" "I don't think so, Miss Shields. I am not your puppet to control. Pass that message on to your superior."
    if v_score >= 4:
        show bg ch6hosp21 with dissolve
        v "*Lets out a sigh of relief*"
        v "This is not going to end well..."
    else:
        show bg ch6hosp20 with dissolve
        v "*Lets out a sigh of relief*"
        v "Meredith, you're playing with fire..."
    jump ch6getdocstairway
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
