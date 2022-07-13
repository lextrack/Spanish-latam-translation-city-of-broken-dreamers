
image bg ch7latenight1 = "ch7latenight1"
image bg ch7latenight2 = "ch7latenight2"
image bg ch7latenight3 = "ch7latenight3"
image bg ch7latenight4 = "ch7latenight4"


image bg ch7kitchen1 = "ch7kitchen1"
image bg ch7kitchen2 = "ch7kitchen2"
image bg ch7kitchen3 = "ch7kitchen3"
image bg ch7kitchen4 = "ch7kitchen4"
image bg ch7kitchen5 = "ch7kitchen5"
image bg ch7kitchen6 = "ch7kitchen6"
image bg ch7kitchen7 = "ch7kitchen7"
image bg ch7kitchen8 = "ch7kitchen8"
image bg ch7kitchen9 = "ch7kitchen9"


label ch7stairwaynightbefore:
    s "Sir?"
    p "Yeah, Sam?"
    s "You still seem to have an issue sleeping. Can I get you something to help?"
    p "Ugh... Nah, that's okay. I'll just take a stroll."
    if "ch4vicaccept" in extraevents:
        menu:
            "Enact Victoria's plan":
                p "I have a better idea."
                s "Sir?"
                jump ch7vicsplan
            "Just take a small walk":
                p "Good idea."
                jump ch7stairwaynight
    else:
        jump ch7stairwaynight

label ch7stairwaynight:
    scene black with Dissolve(1)
    show bg ch7latenight1 with dissolve
    b "Shouldn't you be sleeping?"
    if "ch7katiesex" in extraevents:
        p "Fuck, you scared me. How long have you been out here?"
        b "Just long enough. She's a nice girl, [p]. Don't be your usual self and screw it up."
        p "..."
    else:
        p "Fuck, you scared the shit out of me. I just had a bad dream."
    show bg ch7latenight2 with dissolve
    b "I can tell, your aura's all over the place. Come on, darling, follow me."
    p "Where to?"
    show bg ch7latenight4 with dissolve
    b "You need to get over your desire to know everything at all times. It would help cleanse you of your negative energy."
    p "..."
    scene black with Dissolve(1)
    show bg ch7kitchen1 with Dissolve(1)
    b "Just keep it down. Little guy must have passed out."
    p "I don't want to sound rude, but what's his deal?"
    show bg ch7kitchen2 with dissolve
    b "Glenn? Poor thing is a bit on the spectrum for sure, but he's also a bit of a savant."
    b "Normally this world would step on someone like him, but he was able to find that useful niche that people need."
    b "Reminds me of us, in a way. We're not meant for a normal life, neither is he."
    p "Well, if you think he can help, I believe it."

    show bg ch7kitchen3 with dissolve
    b "He'll do his best. It's you I am worried about. Most would call what you're doing suicide."
    p "I know."
    if "ch6bettyweapons" in extraevents:
        p "If you're that worried, I could always use some of your stash."
        show bg ch7kitchen4 with dissolve
        b "Now, don't you even think about it. Those are in case of an emergency."
        p "Come on, do you really need that much firepower?"
        b "LA's like a big bubble that just keeps getting fatter. When it pops, which it will, those are gonna keep this place safe."
    show bg ch7kitchen5 with dissolve
    b "But that's tomorrow's talk, you need something to help you sleep. "
    p "Betty, I'll be fine. I don't need anything."
    show bg ch7kitchen6 with dissolve
    b "Nonsense. Just park your behind there."
    show bg ch7kitchen7 with dissolve
    p "Umm, what is it?"
    b "It's warm milk, you idiot. What were you expecting?"
    show bg ch7kitchen8 with dissolve
    p "Not that, but hell, it sounds great right about now. No psychedelics in here, right?"
    b "The best kind. Nutmeg."
    show bg ch7kitchen9 with dissolve
    b "Just drink it and try to get some rest."
    p "Heh, thank you, Betty."
    b "Don't mention it. I need you in prime condition so you can hurry up and get out of my hair."
    scene black with Dissolve(1)
    if "ch6katiesex" in extraevents:
        show bg ch7morning1 with dissolve
        p "{i}Let's try this now.{/i}"
    else:
        show bg ch7morning2 with dissolve
        p "{i}Let's try this now.{/i}"
    jump ch7stairwaymorning
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
