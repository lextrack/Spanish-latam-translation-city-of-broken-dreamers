label ch4docupstairsapproach:
    show bg ch4docupstairs76 with dissolve
    if k_score >= 3:
        p "(Damn, you are even cuter when you sleep. Cute... What's wrong with me.)"
    else:
        p "(Just taking a look around, Katie. Never mind me.)"
    show bg ch4docupstairs77 with dissolve
    p "(Huh? Photo and an old datapad.)"
    jump ch4docsleepmenu

label ch4docsleepmenu:
    menu:
        "Look at photo":
            show bg ch4docupstairs78 with dissolve
            p "*Chuckles* (Must be your Mom. You don't look so impressed.)"
            p "(You can tell she loves you, though. It's probably why you kept it.)"
            jump ch4docsleepmenu
        "Check the datapad":
            p "(Now, why are you saving some old datapad like this?)"
            show bg ch4docupstairs79 with dissolve
            n "Upon turning it on it loads where it was last turned off"
            p "(Two archived messages. This is private...)"
            menu:
                "Check the messages":
                    $ extraevents.append("ch4katiespast")
                    p "(Let's play the first message.)"
                    show bg ch4docupstairs80 with dissolve
                    n "After a second, a male voice begins to speak"
                    "Unknown Male" "Hey, kiddo, sorry we couldn't get down to see you."
                    "Unknown Male" "You have no idea how proud I am of you. Soon, I can say my daughter is a doctor!"
                    "Katie's Mother In the Background" "Katie, believe me, he won't stop."
                    "Katie's Father" "Yeah, yeah, your Mom is proud too, don't worry!"
                    "Katie's Mother In the Background" "Oh, stop it! Your Dad is just being his usual self. I miss you so much!"
                    "Katie's Father" "We will get down next month, I promise. Keep studying hard, baby. Love you!"
                    "Katie's Mother In the Background" "Love you!"
                    p "(They sound nice, Katie. I envy you.)"
                    p "(Now for the second message.)"
                    show bg ch4docupstairs81 with dissolve
                    n "After a second, Katie's father begins to speak"
                    "Katie's Father" "Hey, kiddo, I heard what happened at the hospital."
                    "Katie's Father" "You know, screw them, what you did was right. Insurance or not, they needed help."
                    "Katie's Father" "I'm proud of you, I truly am. You have a heart of gold, just like your mother. I wanted to let you know that."
                    "Katie's Father" "If you want to come home-"
                    show bg ch4docupstairs82 with dissolve
                    n "The recording abruptly ends, followed by static."
                    p "Katie..?"
                    show bg ch4docupstairs83 with dissolve
                    p "(Katie, who are you?)"
                    p "(I shouldn't have gone through your things... I'm sorry.)"
                    jump ch4docupstairschoices
                "Sit back down.":
                    $ dep -= 1
                    p "(I better not.)"
                    jump ch4docupstairschoices
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
