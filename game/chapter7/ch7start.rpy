image bg ch7dream1 = "ch7dream1"
image bg ch7dream2 = "ch7dream2"
image bg ch7dream3 = "ch7dream3"
image bg ch7dream4 = "ch7dream4"
image bg ch7dream5 = "ch7dream5"
image bg ch7dream6 = "ch7dream6"
image bg ch7dream7 = "ch7dream7"
image bg ch7dream8 = "ch7dream8"
image bg ch7dream9 = "ch7dream9"
image bg ch7dream10 = "ch7dream10"

label ch7start:
    stop music fadeout 2.0
    scene black with Dissolve(2)

    show bg ch7dream1 with Dissolve(2)
    m "Not much further. The target is just ahead."
    show bg ch7dream2 with dissolve
    p "What the fuck?"
    show bg ch7dream3 with dissolve
    j "[p], how are we suppose to stop this? Look at them all..."
    m "Quickly. Each blast is on a greater and greater radius. It is now or never."
    show bg ch7dream4 with dissolve
    p "Sonja, let's get this over with."
    j "I'm right beside you, the whole way."
    show bg ch7dream5 with dissolve
    p "Shh. You hear that? Behind the canisters."
    show bg ch7dream6 with dissolve
    j "*Gulps* Yeah... Quietly, and no quick movement."
    p "I know."
    j "We just can't startle..."
    show bg ch7dream7 with dissolve
    j "Her..."
    m "Do it, [p]! Before she recovers and then does to you what she did to the others!"
    p "I... Fuck!"
    show bg ch7dream10 with dissolve
    j "Christ, she's so young."
    m "And dangerous. Execute your orders, agents!"
    p "She's just a little girl."
    m "Right now she is your death if you don't act. Yours and everyone else in a one-block radius."
    show bg ch7dream8 with dissolve
    "Child" "*In a fearful stutter* ¿M-mami? Dijeron que podía hablar con mi mami. ¿Donde esta?"
    m "Do it, Agent!"
    p "That's easy for you to say, Meredith!"
    show bg ch7dream9 with dissolve
    j "[p], you can't do this."
    scene black with Dissolve(1)
    play sound audio.guneffect
    jump ch7wake
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
