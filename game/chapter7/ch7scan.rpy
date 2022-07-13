
image bg ch7scanning1 = "ch7scanning1"
image bg ch7scanning2 = "ch7scanning2"
image bg ch7scanning3 = "ch7scanning3"
image bg ch7scanning4 = "ch7scanning4"
image bg ch7scanning5 = "ch7scanning5"
image bg ch7scanning6 = "ch7scanning6"
image bg ch7scanning7 = "ch7scanning7"
image bg ch7scanning8 = "ch7scanning8"
image bg ch7scanning9 = "ch7scanning9"
image bg ch7scanning10 = "ch7scanning10"
image bg ch7scanning11 = "ch7scanning11"
image bg ch7scanning12 = "ch7scanning12"
image bg ch7scanning13 = "ch7scanning13"
image bg ch7scanning14 = "ch7scanning14"
image bg ch7scanning15 = "ch7scanning15"
image bg ch7scanning16 = "ch7scanning16"
image bg ch7scanning17 = "ch7scanning17"
image bg ch7scanning18 = "ch7scanning18"
image bg ch7scanning19 = "ch7scanning19"
image bg ch7scanning20 = "ch7scanning20"
image bg ch7scanning21 = "ch7scanning21"



label ch7scan:
    scene black with Dissolve(1)
    show bg ch7scanning17 with Dissolve(1)
    b "So, he returns. Get what you needed?"
    if "ch7ammo" in extraevents:
        p "Yeah, tell me that lead gave you something?"
    else:
        p "Only that bit of information. Useful?"

    show bg ch7scanning1 with dissolve
    b "Ask him."
    p "Well?"
    show bg ch7scanning3 with dissolve
    gl "Umm, yep. Helped me narrow down a region to scan. Still looking to find her track through the city."
    p "How long do you need?"
    gl "A few hours."
    show bg ch7scanning6 with dissolve
    h "Hours! I thought you said it would be quick?!"
    show bg ch7scanning2 with dissolve
    gl "This is quick! LA has thousands of cameras and I'm not a hacker. A client gave me access to the tracking system, but I have to run it off-cycle."
    gl "It will take time, but I'll find her. Without what [p] gave us, it might have been days instead."
    h "God DAMN IT! Work faster!"
    p "Ease up, Henry."
    if h_score >= 3:
        show bg ch7scanning5 with dissolve
        h "Sorry. I know. I just feel so helpless. She's out there all alone."
        p "You know as well as I do that she can take care of herself. She'll be just fine when we find her."
    else:
        show bg ch7scanning4 with dissolve
        h "Don't you tell me what to do! Gloria's missing and it's like I'm the only one who cares!"
        p "We'll find her. Just let him work."

    show bg ch7scanning18 with dissolve
    k "[p], we put Ellen where Gloria was staying. She doesn't seem too happy."
    p "Well, that's Ellen. She's never happy."
    k "Still, you may want to check on her."
    menu:
        "Check on Ellen":
            p "You're probably right, I'll go see how she is holding up."
            jump ch7stairwayellen
        "Wait":
            p "Sometimes it's best to just let Ellen cool off."
            show bg ch7scanning20 with dissolve
            k "Not what I'd recommend. Don't blame me if she gives you a swift kick in the butt when she wakes up."
            k "She seems like she holds a grudge."
            p "You have no idea."

            show bg ch7scanning19 with dissolve
            k "Ugh... I hope he finds her soon. This waiting is killing me."
            p "When he does, we'll be ready to go. Right now, we just have to wait."
            scene black with Dissolve(2)
            show text "{=trans}ONE HOUR LATER{/=trans}" with Dissolve(1)
            $ renpy.pause(2)
            hide text with Dissolve(1)



label ch7scanfind:
    gl "FOUND HER!"
    show bg ch7scanning21 with dissolve
    b "*Slurring her words* Dat's my boy. Knew ya had it in ya."
    k "Where is she?!"
    show bg ch7scanning7 with dissolve
    h "Quickly, show me!"
    show bg ch7scanning8 with dissolve
    gl "That's her, right?"
    show bg ch7scanning9 with dissolve
    h "I think so, but we need to be sure."
    show bg ch7scanning10 with dissolve
    h "Can you enhance that or whatever it is you guys do?"
    gl "Umm, I can't enhance it, but I can just zoom in."
    show bg ch7scanning11 with dissolve
    h "Gloria..."
    gl "Is it her?"
    show bg ch7scanning12 with dissolve
    $ renpy.pause(1)
    show bg ch7scanning13 with dissolve
    h "It's her. Gloria, what on earth are you doing?"
    show bg ch7scanning14 with dissolve
    h "Can you give me a projected route?"
    gl "One sec."
    show bg ch7scanning15 with dissolve
    h "... oh no."
    p "Henry, what is it?"
    show bg ch7scanning16 with dissolve
    h "Get your things, I know exactly where she's headed."
    p "Where?"
    h "Home."

    jump ch7end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
