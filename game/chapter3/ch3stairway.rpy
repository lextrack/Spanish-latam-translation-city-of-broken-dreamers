


image bg ch3stairway1 = "ch3stairway1"
image bg ch3stairway2 = "ch3stairway2"
image bg ch3stairway3 = "ch3stairway3"
image bg ch3stairway4 = "ch3stairway4"
image bg ch3stairway5 = "ch3stairway5"
image bg ch3stairway6 = "ch3stairway6"
image bg ch3stairway7 = "ch3stairway7"
image bg ch3stairway8 = "ch3stairway8"
image bg ch3stairway9 = "ch3stairway9"
image bg ch3stairway10 = "ch3stairway10"
image bg ch3stairway11 = "ch3stairway11"
image bg ch3stairway12 = "ch3stairway12"
image bg ch3stairway13 = "ch3stairway13"
image bg ch3stairway14 = "ch3stairway14"
image bg ch3stairway15 = "ch3stairway15"
image bg ch3stairway16 = "ch3stairway16"
image bg ch3stairway17 = "ch3stairway17"
image bg ch3stairway18 = "ch3stairway18"
image bg ch3stairway19 = "ch3stairway19"
image bg ch3stairway20 = "ch3stairway20"
image bg ch3stairway21 = "ch3stairway21"
image bg ch3stairway22 = "ch3stairway22"
image bg ch3stairway23 = "ch3stairway23"
image bg ch3stairway24 = "ch3stairway24"
image bg ch3stairway25 = "ch3stairway25"

image bg ch3stairway26 = "ch3stairway26"
image bg ch3stairway27 = "ch3stairway27"
image bg ch3stairway28 = "ch3stairway28"
image bg ch3stairway29 = "ch3stairway29"
image bg ch3stairway30 = "ch3stairway30"
image bg ch3stairway31 = "ch3stairway31"
image bg ch3stairway32 = "ch3stairway32"
image bg ch3stairway33 = "ch3stairway33"
image bg ch3stairway34 = "ch3stairway34"
image bg ch3stairway35 = "ch3stairway35"
image bg ch3stairway36 = "ch3stairway36"
image bg ch3stairway37 = "ch3stairway37"
image bg ch3stairway38 = "ch3stairway38"
image bg ch3stairway39 = "ch3stairway39"
image bg ch3stairway40 = "ch3stairway40"
image bg ch3stairway41 = "ch3stairway41"
image bg ch3stairway42 = "ch3stairway42"
image bg ch3stairway43 = "ch3stairway43"
image bg ch3stairway44 = "ch3stairway44"
image bg ch3stairway45 = "ch3stairway45"
image bg ch3stairway46 = "ch3stairway46"




label ch3stairway:
    scene black with Dissolve(2)
    show bg ch3stairway1 with dissolve
    j "You know I'm into some weird shit, but this place is still fucking weird."
    show bg ch3stairway2 with dissolve
    p "What, perfectly still sex-bots don't get you wet?"
    show bg ch3stairway3 with dissolve
    j "You saying these dolls give you a hard-on?! Seriously?"
    p "A lot of things give me a hard-on Sonja. You know that."
    j "Even that?!"
    show bg ch3stairway7 with hpunch
    p "Wow, older model!"
    j "I'd say. How-"
    show bg ch3stairway4 with dissolve
    p "That one looks newer."
    j "Yeah, every guy's fantasy... a perfectly cylindrical vagina."
    show bg ch3stairway5 with dissolve
    p "A what?"
    j "Just give me a good old fashioned dildo."
    p "Your dildos were never old fashioned. You know, they probably have some prime dude-bots in the back."
    show bg ch3stairway6 with dissolve
    $ insult = renpy.random.choice(insults)
    j "Wait, you been here before, [insult]?"
    p "(Yeah. More than once.)"
    menu:
        "Never (lie)":
            p "Nope, that shit is disgusting. Who would ever..."
            $ extraevents.append("ch3sonjalie")
            jump ch3stairwaylie
        "Yeah, I have":
            $ extraevents.append("ch3sonjatruth")
            p "Once or twice."
            jump ch3stairwaytruth
        "I love them (lie)":
            p "Yeah, every day and twice on Sunday. Can't get enough."
            $ extraevents.append("ch3sonjajoke")
            jump ch3stairwayjoke

label ch3stairwaylie:
    show bg ch3stairway8 with dissolve
    j "You lying sack of shit! I can see it on your face."
    p "I'm not lying! I told you, this isn't my thing."
    show bg ch3stairway10 with dissolve
    j "Hey, no judgment from me here."
    p "I'm telling you. I..."
    j "You think after Carnavale in 39, I'd give you shit over this?"
    p "Yes."
    j "Well, yes. But judgment-free shit."
    show bg ch3stairway9 with dissolve
    if "ch1ellen" in extraevents:
        j "But now I see why you were so pissed when I scared off your real woman."
    else:
        j "And sometimes, VR just isn't enough."
    jump ch3stairwaywake


label ch3stairwaytruth:
    show bg ch3stairway9 with dissolve
    j "Seriously? You that hard up?"
    p "Yeah, but not for what you think."
    show bg ch3stairway10 with dissolve
    j "No judgment. Well, a little judgment."
    p "I know Betty."
    j "Wait, how the hell do you know Betty?"
    p "She's a contact."
    show bg ch3stairway8 with dissolve
    j "You fuck! I swear to fuck, if you sharked me on this..."
    p "I had no idea! We were in basic together. Ran into her again a few months back."
    jump ch3stairwaywake

label ch3stairwayjoke:
    show bg ch3stairway10 with dissolve
    $ insult = renpy.random.choice(insults)
    j "Fuck off, [insult]."
    p "No, I'm serious. I mean, who wouldn't want a set of triple E's in their face? Look at them!"
    show bg ch3stairway9 with dissolve
    j "I'd say it's nice to have your sense of \"humor\" back. But we don't lie to each other."
    p "What did I say?"
    jump ch3stairwaywake


label ch3stairwaywake:
    show bg ch3stairway13 with dissolve
    "Sex-bot" "Welcome!"
    show bg ch3stairway15 with hpunch
    j "Fuck me! You on ninja protocol or something?"
    show bg ch3stairway12 with dissolve
    "Sex-bot" "My apologies. It was not my intention to frighten."
    show bg ch3stairway11 with dissolve
    "Sex-bot" "I could never commit a cruel act. That is the monopoly of those with a moral sense."
    "Sex-bot" "I do not inflict pain for my own pleasure, only for human desi-"
    show bg ch3stairway16 with dissolve
    j "Whatever you say, Sonny. Spare me the lecture."
    "Sex-bot" "Very well. Right now we are running a special for our female clients."
    show bg ch3stairway14 with dissolve
    "Sex-bot" "My base software is top-rated in both cunnilingus and digital g-spot manipulation. I also have several threesome protocols that you and your partner might find..."
    show bg ch3stairway17 with dissolve
    j "Yeah... no thanks..."
    j "And wipe that shit-eating grin off your face."
    if "vostokdoc" in extraevents:
        p "Same shit happened last night. I think these bots lean towards women."
        j "I'd ask, but I don't care."
    else:
        p "This is just a regular grin. You must admit this is fucking hilarious."
        j "Bullshit, you want that threesome. Well, I'm not plastered and it's not your birthday."
        "Sex-bot" "I am sorry to hear that. If you'd like, we can provide you with alcohol."
    show bg ch3stairway18 with dissolve
    "Unknown Woman" "*From the back of the room* Venus, dear, leave our guests alone."
    ve "Yes, Madame."
    if "ch3sonjatruth" in extraevents:
        "[p] & Sonja in unison" "Betty."
    else:
        j "Betty."

    show bg ch3stairway19 with dissolve
    b "*Leans towards you* You can stay, [p]. {i}That{/i} one needs to go. She damaged my chakra. That, I can't forgive."
    show bg ch3stairway20 with dissolve
    b "You heard me. You can leave now."
    j "Your intel was shit!"
    b "It was fine. Your negative energy tipped off the target."
    show bg ch3stairway21 with dissolve
    j "The fuck it did! [p], make sure whatever you get from this moonbat comes from a vid-feed and not a crystal."
    b "Why are you still here, Ms. Vasquez?"
    "Sonja storms out the door"
    show bg ch3stairway22 with dissolve
    p "What did Sonja mean about crystals?"
    b "Don't let her negative ki affect this interaction. I've been expecting you, Mr. [pl]."
    p "You were?"
    b "Of course, the spirits tell me you are searching for something, someone. And they are nearby."
    menu:
        "Play along":
            p "Wow, yes, you are absolutely right. Amazing as always, Betty."
            b "Venus, my dear. Please join us."
            show bg ch3stairway23 with dissolve
            ve "Of course, Madame."
            b "Our friend here is looking for something."
            p "Someone, yes."
            show bg ch3stairway24 with dissolve
            b "Do you think we can help him?"
            ve "It depends on the length of the encounter. My total remaining battery life is 2 hours 21 minutes, Madame. I was to remind you to ensure \"my flower was plucked\" before my first recharge cycle."
            b "Right, my poor little virgin. I nearly forgot."
            b "Mr. [pl], tell me of the one you seek."
            show bg ch3stairway25 with dissolve
            ve "Yes, do tell."
            p "Well, he is large. Actually, large is an understatement. He's between seven and a half to eight feet tall, bald and extremely well built."
            b "Venus bend over."
            show bg ch3stairway26 with dissolve
            b "Built like this?"
            p "Umm, no. I mean he's strong. Built like a freight drone."
            show bg ch3stairway27 with dissolve
            b "I may have seen someone along those lines nearby."
            p "Where?!"
            b "Patience, Mr. [pl]. Haste disrupts my energy."
            b "You can touch her if you wish. Channel yourself through her."
            menu:
                "Touch Venus":
                    show bg ch3stairway28 with dissolve
                    p "She's very smooth."
                    show bg ch3stairway29 with dissolve
                    b "I made the adjustments, myself. Better than the real thing."
                    b "Venus, sit up, please."
                    show bg ch3stairway31 with dissolve
                    b "The eyes I worked on for quite some time. I like eyes. The doorway to the soul, you know."
                    ve "Do you like my eyes, Sir?"
                    show bg ch3stairway30 with dissolve
                    p "Impressive work."
                    show bg ch3stairway32 with dissolve
                    p "Really, impressive work."
                    b "I'm glad you think so. Your timing is perfect. I need someone to make her first time special."
                    p "(Shit, Betty, it's a fucking robot. Literally.)"
                    show bg ch3stairway31 with dissolve
                    menu:
                        "Love to":
                            p "She hasn't been tested yet?"
                            b "Nope, I figured you could put her through her paces. Make sure she doesn't do anything strange."
                            b "After that, you can head to Maybank Avenue, near the old fire hall. The one you seek, I saw there."
                            p "How do you know this?"
                            b "An outsider wouldn't notice, but, for a local... he stands out. Check near the old fire hall. The last time my cameras picked him up, he was buying women's clothing."
                            p "You've been watching him."
                            b "I watch everyone who might bring trouble. That's why you pay me."
                            b "Now go give this one a test for me."
                            jump ch3venus
                        "Sorry, I can't":
                            $ extraevents.append("ch3bettystop")
                            p "I appreciate the offer, Betty, but I can't."
                            show bg ch3stairway33 with dissolve
                            b "Just the information, then?"
                            p "Much appreciated. Sam, transfer $1000 to the Stairway to Heaven establishment in Lakewood."
                            s "Transferring funds. Have fun, Sir."
                            show bg ch3stairway34 with dissolve
                            b "Now I do know the soul of whom you speak. An outsider wouldn't notice, but, for a local... he stands out. Check near the old fire hall. The last time my cameras picked him up he was buying women's clothing."
                            p "You've been watching him."
                            b "I watch everyone who might bring trouble. That's why you pay me."
                            p "Always a pleasure, Betty. Thanks."
                            b "Of course, now if you don't mind I need to get ready for the mid-day rush."
                            jump ch3tohenry
                "Just tell me":

                    $ extraevents.append("ch3bettystop")
                    p "I'm in a hurry, Betty, just give me the info if you have it."
                    b "*Sighs* Fine, but payment up front. I'm not the trusting innocent I used to be since your \"friend\" broke my heart."
                    jump ch3stairwaycutshit
        "Cut the shit":


            p "Cut the shit, Betty. I'm just looking for information. I will pay you up front."
            b "*Sighs* Venus, darling, come sit with me. I need some of your positive energy. Lakewood really is full of heathens."
            show bg ch3stairway23 with dissolve
            p "I'm looking for a man. Not any regular joe, mind you. Huge, around 7 and a half to 8 feet tall, bald, built like a freight drone."
            b "This is Mil-Town darling, that's not as uncommon as you think. What other visible mutations?"
            p "None. Looks human enough outside of his physique."
            show bg ch3stairway24 with dissolve
            b "Now dear, have we seen anyone like that?"
            ve "I would not know Madame. This is my first activation. I have been running for two hours, twenty-one minutes, thirteen seconds."
            ve "As I am reaching 50%% battery you wished that I remind you to make sure \"my flower was plucked\" before my first recharge cycle."
            b "Right, my poor little virgin, you do need to be made a woman."
            p "Betty, focus, please. Have you seen him or not?"
            show bg ch3stairway25 with dissolve
            b "*Smirks* I know where he might be. Payment first, darling."
            jump ch3stairwaycutshit



label ch3stairwaycutshit:
    $ extraevents.append("ch3bettystop")
    p "Much appreciated. Sam, transfer $1000 to the Stairway to Heaven establishment in Lakewood."
    s "Transferring funds. Have fun, Sir."
    p "... There. Now, where did you see him?"
    show bg ch3stairway34 with dissolve
    b "Now I do know the soul of whom you speak. An outsider wouldn't notice, but, for a local... he stands out. Check near the old fire hall. The last time my cameras picked him up he was buying women's clothing."
    p "You've been watching him."
    b "I watch everyone who might bring trouble. And even if he tries to hide it, that man smells of trouble. Blood and trouble. Just like you, darling."
    p "Thanks, Betty."
    b "Of course, darling. Now if you don't mind I need to get ready for the mid-day rush."
    jump ch3tohenry
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
