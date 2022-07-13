
image bg ch6gloria1 = "ch6gloria1"
image bg ch6gloria2 = "ch6gloria2"
image bg ch6gloria3 = "ch6gloria3"
image bg ch6gloria4 = "ch6gloria4"
image bg ch6gloria5 = "ch6gloria5"
image bg ch6gloria6 = "ch6gloria6"
image bg ch6gloria7 = "ch6gloria7"
image bg ch6gloria8 = "ch6gloria8"
image bg ch6gloria9 = "ch6gloria9"
image bg ch6gloria10 = "ch6gloria10"
image bg ch6gloria11 = "ch6gloria11"
image bg ch6gloria12 = "ch6gloria12"
image bg ch6gloria13 = "ch6gloria13"
image bg ch6gloria14 = "ch6gloria14"
image bg ch6gloria15 = "ch6gloria15"
image bg ch6gloria16 = "ch6gloria16"
image bg ch6gloria17 = "ch6gloria17"
image bg ch6gloria18 = "ch6gloria18"
image bg ch6gloria19 = "ch6gloria19"
image bg ch6gloria20 = "ch6gloria20"
image bg ch6gloria21 = "ch6gloria21"
image bg ch6gloria22 = "ch6gloria22"
image bg ch6gloria23 = "ch6gloria23"
image bg ch6gloria24 = "ch6gloria24"
image bg ch6gloria25 = "ch6gloria25"
image bg ch6gloria26 = "ch6gloria26"
image bg ch6gloria27 = "ch6gloria27"
image bg ch6gloria28 = "ch6gloria28"
image bg ch6gloria29 = "ch6gloria29"


image bg ch6gloria30 = "ch6gloria30"
image bg ch6gloria31 = "ch6gloria31"
image bg ch6gloria32 = "ch6gloria32"
image bg ch6gloria33 = "ch6gloria33"
image bg ch6gloria34 = "ch6gloria34"



label ch6stairwaygloria2:
    scene black with Dissolve(1)
    show bg ch6gloria1 with Dissolve(1)
    g "Who are you?! Where the hell am I? Get back!"
    if "ch6venusholdback" in extraevents:
        show bg ch6gloria2 with dissolve
        ve "This is my home, me and Ma'am. You're safe here, Gloria."
        show bg ch6gloria33 with dissolve
        g "How do you know my name? And where is Henry!?"
        ve "He's fine, Gloria. Doctor Katie has been looking after him. You've been unconscious for quite some time. Are you feeling well?"
        show bg ch6gloria31 with dissolve
        g "I'm mainly feeling confused. What is this place?"
        show bg ch6gloria2 with dissolve
        ve "This is the Stairway to Heaven. The premier lounge for the pursuit of erotic delights. Now that you are better I can see to any sexual needs you might..."
        g "Umm..."
        show bg ch6gloria30 with dissolve
        n "You walk up to see Gloria in what looks to be a very uncomfortable conversation"
        g "[p]! I am very confused, a little scared and did I mention scared and confused?"
        g "Or is this another super weird shared dream? It's really feeling like one."
        p "It's a friend's place. We'll be safe here."
        g "You thought that last time."
        p "Well, let's hope I'm right this time. No easy way to link me here."
        p "Venus, can you give us some space?"
        show bg ch6gloria32 with dissolve
        ve "Of course!"
        show bg ch6gloria22 with dissolve
        g "Soo... premier lounge for erotic delights?"
        p "Yeah. Just consider it a safe house. Safer than the last one, hopefully."
        g "Henry must be super uncomfortable here... he's okay, right? The robot wasn't lying?"
        p "No. Katie has been looking after him."
        show bg ch6gloria23 with dissolve
        g "*Sighs in relief*"
        g "Good, I always worry when I pass out like that."
        p "What do you remember anyway?"
        g "I remember we were attacked. Then we ran downstairs but after that, it's a blur."
        g "I guess I went off again?"
        p "Yeah."
        jump ch6stairwaygloriamenu
    else:

        show bg ch6gloria3 with dissolve
        ve "Gloria, you are up! I'm Venus, you can be my new sister! I always wanted a little sister!"
        show bg ch6gloria4 with dissolve
        g "WHAT!? Stay away from me, whatever you are!"
        ve "It's okay, let me hold you as a big sister should."
        g "BACK OFF!!!"
        show bg ch6gloria34 with dissolve
        n "As you walk around the corner you hear a scream from Gloria"
        p "(That's not good.)"
        show bg ch6gloria5 with hpunch
        n "With a crash, Venus is flung across the room"
        show bg ch6gloria7 with dissolve
        p "Shit! Gloria! It's okay, calm down."
        g "What the hell is that? Where the hell am I?"
        if "ch5glorialittlemad" in extraevents or "ch5gloriamad" in extraevents:
            g "And why is everyone so damn handsy?"
        p "That umm... {i}Was{/i} Venus."
        show bg ch6gloria6 with dissolve
        g "I think I killed her... oh God."
        show bg ch6gloria8 with dissolve
        p "Don't worry, she's a bot."
        g "Thank god."
        p "Still, if Betty sees this she's gonna murder me... Ahh, here, one sec."
        show bg ch6gloria9 with dissolve
        g "Betty?"
        p "She owns the joint."
        p "Well, this doesn't look too bad, maybe you just knocked her head out of place. Let's pray it's an easy fix."
        g "Wow, you know how to repair bots?"
        p "Nope, but I better try or a crazy hippie will kill me."
        g "This Betty person that scary?"
        p "Only when you don't want her to be."
        show bg ch6gloria10 with dissolve
        p "I think I saw a toolbox in one of the lockers there. Your far left."
        show bg ch6gloria11 with dissolve
        $ renpy.pause(1)
        show bg ch6gloria12 with dissolve
        g "Umm, [p], where exactly are we?"
        p "Yeah... ugh... Look it's safe for the time being."
        p "Damn, you did a number on her."
        g "Sorry..."
        p "What happened?"
        g "I never had a sister, but I don't think sisters try to hug the way she does."
        show bg ch6gloria13 with dissolve
        p "Well, her head turned back pretty easily."
        g "She feels real... This is really weird."
        p "Heh, yeah..."
        p "Help me get this off. Pretty sure her reset is on her back."
        show bg ch6gloria14 with dissolve
        g "Holy..."
        p "Ha, stop staring."
        g "I would but... like... wow."
        p "Then keep staring, but hand me that Phillips head there."
        show bg ch6gloria15 with dissolve
        g "Pointy one right?"
        p "Aren't they all?"
        show bg ch6gloria16 with dissolve
        g "Umm, right, the one with the cross then. Here you go."
        p "You know your stuff."
        show bg ch6gloria17 with dissolve
        g "Yeah, Henry said I should be good with my hands, taught me some stuff on Papa's cars. It's just a screwdriver, you know?"
        p "Heh, still, did it stick with ya?"
        g "Just the basics..."
        show bg ch6gloria18 with dissolve
        g "OH! Where's Henry!"
        p "He's fine. Doc has been keeping an eye on him."
        show bg ch6gloria19 with dissolve
        g "*Sighs in relief*"
        p "There, that should work."
        p "So, what do you remember, anyway?"
        g "I remember we were attacked. Then we ran downstairs but after that, it's a blur."
        $ extraevents.append("ch6venusbroken")
        jump ch6stairwaygloria2menu


label ch6stairwaygloriamenu:
    menu:
        "Question her powers":
            p "I have a question, though. I've seen you use your powers in a bunch of ways, like your hair. Then the stuff with Ellen's mic."
            g "Yeah..."
            p "Did you ever wonder why it doesn't seem to have side effects from those instances?"
            show bg ch6gloria25 with dissolve
            g "What do you mean? It still does... Sometimes I get light-headed or dizzy. Maybe a nosebleed."
            p "Yeah, but it seems there are times where you have... I don't know, more control, maybe?"
            g "I wish I knew, I really do."
            p "Well, whatever it is, you'll figure it out."
            show bg ch6gloria24 with dissolve
            g "I wish I could agree with you."
            p "Yeah."
            g "So where is Ellen, by the way? Making time with one of the male Venuses? Venusi? What is the plural?"
            jump ch6stairwaygloriaellen
        "Tell her about the Red Moon":

            p "So, you don't remember that guy that Henry squared off against?"
            g "No... I remember a humid, loud and dark place. That's it really."
            p "I don't want to scare you, but whoever it was, he's just as strong as Henry."
            show bg ch6gloria25 with dissolve
            g "Another augment?"
            p "Ask Henry, he'll explain it better."
            g "Alright, fine. Be that way."
            p "Just not my place."
            g "Fine, we'll move on. So where is Ellen, by the way? Making time with one of the male Venuses? Venusi? What is the plural?"
            jump ch6stairwaygloriaellen


label ch6stairwaygloria2menu:
    menu:
        "Question her powers":
            p "Gloria, about what you can do. I've seen you use it, like your hair. Then just now."
            g "Yeah..."
            p "Did you ever wonder why it doesn't seem to have side effects from those instances?"
            show bg ch6gloria18 with dissolve
            g "What do you mean? It still does... Sometimes I get light-headed or dizzy."
            p "Yeah, but it seems there are times where you have... I don't know, more control, maybe?"
            g "Trust me, I didn't want to fling her across the room."
            p "But, you were scared and you didn't blast everything in the room away, just her."
            p "I think whatever it is, you're starting to figure it out."
            show bg ch6gloria19 with dissolve
            g "I wish I could agree with you."
            p "Well, one thing we can both agree on, you messed up Venus here."
            jump ch6stairwaygloria2venuswake
        "Tell her about the Red Moon":

            p "So, you don't remember that guy that Henry squared off against?"
            g "No... I remember a humid, loud and dark place. That's it really."
            p "I don't want to scare you, but whoever it was, he's just as strong as Henry."
            show bg ch6gloria18 with dissolve
            g "Another augment?"
            p "Ask Henry, he'll explain it better."
            g "Alright, fine. Be that way."
            p "Just not my place."
            jump ch6stairwaygloria2venuswake

label ch6stairwaygloria2venuswake:
    p "There! I think that should work."
    show bg ch6gloria20 with dissolve
    ve "Reboot successful."
    g "We have to show Ellen!"
    p "Venus, can you leave us?"
    show bg ch6gloria21 with dissolve
    ve "Of course. Would you like me to fetch you anything?"
    p "No, it's fine."
    show bg ch6gloria22 with dissolve
    g "What's going on, [p]?"
    p "Come sit down on the couch."
    show bg ch6gloria23 with dissolve
    menu:
        "Tell her, but leave out her involvement":
            jump ch6gloriapartial
        "Tell her everything":

            jump ch6gloriafull
        "Lie to her":

            jump ch6glorialie


label ch6stairwaygloriaellen:
    if e_score <=2:
        p "Right, Ellen. Um..."
    else:
        p "..."
        g "What?"
        show bg ch6gloria23 with dissolve
        menu:
            "Tell her, but leave out her involvement":
                jump ch6gloriapartial
            "Tell her everything":

                jump ch6gloriafull
            "Lie to her":

                jump ch6glorialie



label ch6gloriapartial:
    $ extraevents.append("ch6gloriaparttruth")
    p "Gloria..."
    g "What happened?"
    show bg ch6gloria26 with dissolve
    g "Oh no... no... no... [p], just tell me!"
    p "She fell during the fight... I think she may be... Shit, I don't know. We had to get out of there."
    g "Is she hurt? How bad is it?"
    p "I don't know."
    show bg ch6gloria27 with dissolve
    g "That's not good enough! How can you not know?"
    p "She fell, so I lost sight of her. We had to get you to safety."
    g "You left her there?"
    p "We didn't have a choice. Ellen was my friend. If I had a chance, I would have taken it."
    show bg ch6gloria28 with dissolve
    g "You said {i}was{/i}. So she's..."
    p "I hope I'm wrong... but I..."
    g "You don't have to say anything else."
    p "Are you going to be okay?"
    g "No... Are you?"
    p "I don't know..."
    p "Hey, I'll be here. Katie and Henry are here as well, if you need anyone to talk to."
    show bg ch6gloria29 with dissolve
    g "I just want to be alone..."
    p "..."
    p "I understand."
    jump ch6stairwaymenu

label ch6gloriafull:
    $ extraevents.append("ch6gloriatruth")
    show bg ch6gloria25 with dissolve
    p "Gloria..."
    g "What happened?"
    show bg ch6gloria26 with dissolve
    g "Oh no... no... no... [p], just tell me!"
    p "We were underground on a bridge when you lost control. Henry was about to die."
    p "You saved us... But, Ellen... She was right next to you. You pushed her off the landing."
    show bg ch6gloria27 with dissolve
    g "*Gasps*"
    g "I-I... I hurt her?"
    p "It wasn't your fault."
    g "How bad is she?"
    p "I don't know."
    g "That's not good enough! How can you not know?"
    p "She fell, so I lost sight of her. We had to get you to safety."
    g "You left her there?"
    p "We didn't have a choice. Ellen was my friend. If I had a chance, I would have taken it."
    show bg ch6gloria28 with dissolve
    g "You said {i}was{/i}. So she's dead."
    p "I hope I'm wrong... but I..."
    g "You don't have to say anything else."
    p "Are you going to be okay?"
    g "No..."
    p "It wasn't your fault..."
    show bg ch6gloria29 with dissolve
    g "Shut up! Everyone keeps saying that, but it's not true! It {i}was{/i} my fault! All this is my fault!"
    g "Just go away... Please..."
    p "Gloria, you can't take this all on yourself, it will tear you up. Trust me."
    g "*Sniffs* I said go!"
    jump ch6stairwaymenu


label ch6glorialie:
    $ extraevents.append("ch6glorialie")
    show bg ch6gloria24 with dissolve
    g "This doesn't sound good, [p]..."
    p "Oh, nothing. But after all that, I asked Ellen to lay low. This isn't her fight, no matter what she thinks."
    show bg ch6gloria25 with dissolve
    g "Umm, okay?"
    p "Look, you may have been out for a while, me, on the other hand, it's getting late and I need to turn in soon."
    g "You think I'd buy that? You're lying. Why?"
    show bg ch6gloria26 with dissolve
    $ g_score -= 1
    g "[p], just tell me!"
    menu:
        "Tell her the full truth":
            jump ch6glorialiethenfull
        "Leave out her involvement":
            jump ch6glorialiethenpartial





label ch6glorialiethenfull:
    $ extraevents.append("ch6gloriatruth")
    p "You saved us... But, Ellen... She was right next to you. You pushed her off the landing."
    show bg ch6gloria27 with dissolve
    g "*Gasps*"
    g "I-I... I hurt her?"
    p "It wasn't your fault."
    g "How bad is she?"
    p "I don't know."
    g "That's not good enough! How can you not know?"
    p "She fell, so I lost sight of her. We had to get you to safety."
    g "You left her there?"
    p "We didn't have a choice. Ellen was my friend. If I had a chance, I would have taken it."
    show bg ch6gloria28 with dissolve
    g "You said {i}was{/i}. So she's dead."
    p "I hope I'm wrong... but I..."
    g "You don't have to say anything else."
    p "Are you going to be okay?"
    g "No... Are you?"
    p "It wasn't your fault..."
    show bg ch6gloria29 with dissolve
    g "Shut up! Everyone keeps saying that, but it's not true! It {i}was{/i} my fault! All this is my fault!"
    g "Just go away... Please..."
    p "Gloria, you can't take this all on yourself, it will tear you up. Trust me."
    g "*Sniffs* I said go!"
    jump ch6stairwaymenu


label ch6glorialiethenpartial:
    $ extraevents.append("ch6gloriaparttruth")
    p "She fell during the fight... I think she may be... Shit, I don't know. We had to get out of there."
    g "Is she hurt? How bad is it?"
    p "I don't know."
    show bg ch6gloria27 with dissolve
    g "That's not good enough! How can you not know?"
    p "She fell, so I lost sight of her. We had to get you to safety."
    g "You left her there?"
    p "We didn't have a choice. Ellen was my friend. If I had a chance, I would have taken it."
    show bg ch6gloria28 with dissolve
    g "You said {i}was{/i}. So she's dead."
    p "I hope I'm wrong... but I..."
    g "You don't have to say anything else."
    p "Are you going to be okay?"
    g "No... Are you?"
    p "I don't know..."
    p "Hey, I'll be here. Katie and Henry are here as well, if you need anyone to talk to."
    show bg ch6gloria29 with dissolve
    g "I just want to be alone..."
    p "..."
    p "I understand."
    jump ch6stairwaymenu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
