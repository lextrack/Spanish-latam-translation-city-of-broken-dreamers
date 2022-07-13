


image bg ch3chandra115 = "ch3chandra115"
image bg ch3chandra116 = "ch3chandra116"
image bg ch3chandra117 = "ch3chandra117"
image bg ch3chandra118 = "ch3chandra118"
image bg ch3chandra119 = "ch3chandra119"

image bg ch3report1 = "ch3report1"
image bg ch3report2 = "ch3report2"
image bg ch3report3 = "ch3report3"
image bg ch3report4 = "ch3report4"
image bg ch3report5 = "ch3report5"
image bg ch3report6 = "ch3report6"
image bg ch3report7 = "ch3report7"
image bg ch3report8 = "ch3report8"
image bg ch3report9 = "ch3report9"
image bg ch3report10 = "ch3report10"
image bg ch3report11 = "ch3report11"
image bg ch3report12 = "ch3report12"
image bg ch3report13 = "ch3report13"
image bg ch3report14 = "ch3report14"
image bg ch3report15 = "ch3report15"
image bg ch3report16 = "ch3report16"
image bg ch3report17 = "ch3report17"
image bg ch3report18 = "ch3report18"
image bg ch3report19 = "ch3report19"
image bg ch3report20 = "ch3report20"
image bg ch3report21 = "ch3report21"

image bg ch3report22 = "ch3report22"
image bg ch3report23 = "ch3report23"
image bg ch3report24 = "ch3report24"
image bg ch3report25 = "ch3report25"
image bg ch3report26 = "ch3report26"
image bg ch3report27 = "ch3report27"
image bg ch3report28 = "ch3report28"
image bg ch3report29 = "ch3report29"
image bg ch3report30 = "ch3report30"
image bg ch3report31 = "ch3report31"



label ch3report:
    scene black with Dissolve(1)
    play music audio.calm fadein 4.0 fadeout 4.0
    show bg ch3chandra115 with dissolve
    c "Mind if I kick it here for a bit? Just need a breather."
    p "I have things I need to prep for..."
    show bg ch3chandra116 with dissolve
    c "Damn, you always this busy?"
    p "No, but right now, I am."
    c "Can I help?"
    menu:
        "Only for a minute":
            $ c_score += 1
            p "Not sure with what, but okay."
            c "Cool, I can be your rubber ducky."
            show bg ch3report14 with dissolve
            p "My what?"
            c "Your rubber ducky. I don't need to know shit. You just talk to me like I do."
            show bg ch3report16 with dissolve
            p "And that helps me, how?"
            c "Just try it. You'll see."
            p "..."
            p "Chandra?"
            c "Yeah?"
            p "Why is it called a rubber ducky?"
            show bg ch3report15 with dissolve
            c "Fuck if I know."
            $ achievement.grant("RUBBERDUCKY")
            init:
                $ achievement.register("RUBBERDUCKY")
            $ achievement.Sync()
            p "Well, rubber ducky. Let's start. I don't have much time."
            jump ch3reportwith
        "You gotta go":



            p "I really need to get to this. Wasted far to much time already."
            show bg ch3chandra118 with dissolve
            c "Wasted?! That was a blast!"
            p "Poor choice of words, sorry."
            show bg ch3chandra117 with dissolve
            c "Shitty. I get it, [p]. Be interesting to see what you dudes do."
            p "Not all dudes, you know that."
            c "Pfft, whatever, you knew what I meant. Don't get all PC on me."
            p "..."
            c "Heh, well... I'll get out of your hair. See you around, [chandrasexname]."
            show bg ch3chandra119 with dissolve
            p "(Fuck, I don't have much time. I need to go over this stuff fast.)"
            jump ch3reportaloneafter


label ch3reportwith:
    $ extraevents.append("ch3reportwith")
    p "Sam, load up the material you got from Baynard."
    s "The files are ready to be viewed, Sir."
    s "What would you like to start with?"
    p "Options?"

    s "A limiter, Sergeant Major Henry Gibson, Gen One Augments and the Akatsuki Corporation."
    p "I only have time for a few of these. Thanks to a certain someone."
    show bg ch3report17 with dissolve
    c "Sorry... Nah, I'm not sorry."
    p "Atatuski? And what the hell is this limiter? Doesn't matter, I need to know more on this guy. They say he is an Augment..."


    c "See? Working already!"
    p "Uh huh... Sam, bring up -"
    $ count = 0;
    $ resetmenu()
    jump ch3reportmenu

label ch3reportalone:
    scene black with Dissolve(2)
    play music audio.calm fadein 4.0 fadeout 4.0
    show text "{=trans}A WHILE LATER, BACK AT THE APARTMENT{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    show bg ch3report13 with dissolve
    p "(Fucking, Chandra...)"
    jump ch3reportaloneafter

label ch3reportaloneafter:
    p "Sam, are the docs from Baynard ready to go?"
    show bg ch3report12 with dissolve
    s "The files are ready to be viewed, Sir."
    s "What would you like to start with?"
    p "Options?"
    show bg ch3report11 with dissolve
    s "A limiter, Sergeant Major Henry Gibson, Gen One Augments and the Akatsuki Corporation."
    p "Okay, let's start with..."
    $ count = 0
    $ resetmenu()
    jump ch3reportmenu

label ch3reportmenu:
    if "ch3chandra" in extraevents and count >= 2:
        jump ch3reportnotime
    elif count >= 3:
        jump ch3reportnotime
    menu:
        "Limiter" if menu1:
            $ menu1 = False
            $ count += 1
            jump ch3reportlimiter
        "Henry Gibson" if menu2:
            $ menu2 = False
            $ count += 1
            jump ch3reporthenry
        "Augments" if menu3:
            $ menu3 = False
            $ count += 1
            jump ch3reportaugments
        "Akatsuki" if menu4:
            $ menu4 = False
            $ count += 1
            jump ch3reportredmoon

label ch3reportlimiter:
    $ extraevents.append("ch3reportlimter")
    p "Sam, tell me about the limiter."
    show bg ch3report1 with dissolve
    s "Due to the experimental nature of the generation one augment program, early candidates' bodies would often collapse from the strain of their increased strength and cardiovascular capabilities."
    s "A device known as a limiter was introduced to regulate proper body activity in the generation one augment program."
    s "Typically the limiter was located at the base of the neck."
    s "During normal use displayed with a green light, the limiter would keep proper respiratory and musculoskeletal functions."
    show bg ch3report2 with dissolve
    s "During combat or high stress as detected by heightened adrenaline, the limiter would switch to combat readiness as evidenced when it turns red."
    s "In this mode, the limiter would adjust the nano and chemical augmentations in the subject to increase speed, strength, and awareness."
    s "The limiter was phased out in the generation two augments due to complications."
    p "What kind of complications, Sam?"
    s "None specified, Sir."
    if "ch3reportredmoon" in extraevents and "ch3reportwith" in extraevents:
        show bg ch3report18 with dissolve
        c "Well, that's helpful. If you get into a scrap with an old war relic, you can jab him in the neck with a live power cable!"
        p "I'll keep that in mind."

    if "ch3reportaugments" in extraevents and "ch3reportwith" in extraevents:
        show bg ch3report18 with dissolve
        c "Well, that's helpful. If you get into a scrap with an old war relic, you can jab him in the neck with a live power cable!"
        p "I'll keep that in mind."


    p "Okay, what next?"
    jump ch3reportmenu

label ch3reporthenry:
    $ extraevents.append("ch3reporthenry")
    p "Sam, bring up what they have on this fella."
    show bg ch3report4 with dissolve
    s "Sergeant Major Henry Gibson"
    show bg ch3report5 with dissolve
    s "Born in International Falls, Minnesota he climbed to the rank of Sergeant Major in the Marines before being honorably discharged."
    show bg ch3report10 with dissolve
    s "Gibson spent most of his career in the Pacific theater. He is fluent in Japanese, Korean, and Mandarin."
    s "During the Japanese liberation of Taiwan, Gibson was wounded, causing paralysis from the waist down."
    s "Baynard Industries had suggested it would be very likely that the Augment Program could restore his ability to walk."
    s "Baynard was true to their word. In fact, he was one of the first that succeeded in the initial trials, where many would follow. He was walking within months."
    s "During the war, Gibson's unit was renowned for their effectiveness but also their ruthlessness. He was rewarded two bronze stars, a Medal of Valor and finally a purple heart."
    n "Sam continues to read out more information on his biography, mostly relating to his career in the Marines."
    if "ch3reportwith" in extraevents:
        show bg ch3report20 with dissolve
        c "I thought you were going after some little blonde chick. This dude looks like he will kick your ass."
        p "So I've been told."
    p "Okay, what next?"
    jump ch3reportmenu



label ch3reportaugments:
    p "Sam, bring up the information on the First Gen Augments. Let's see if they have anything I don't already know."
    s "Yes, sir."
    if v_score >=3:
        $ extraevents.append("ch3reportaugments")

        s "Bringing up the unredacted version. Someone likes you, Sir."
        p "Perfect, let's see it."
        show bg ch3report8 with dissolve
        s "The Augment program was created in joint by the United States Military and the Baynard Corporation."
        s "A counter was needed for the Akatuski Red Moon program. This was the United States answer."
        s "Biological, chemical and nanotech were used in the subject to increase speed, strength, and awareness."
        s "A device known as a limiter was used to manage the subjects' abilities. This, in turn, kept them operational throughout the war."
        s "Though effective in battle, the Red Moon quickly discovered that a highly charged EMP directed at the base of the neck would render the subject immobile."
        s "For this and other reliability reasons, the first generation augments stopped production immediately after the Treaty of Hiroshima was signed. Problems with the augments..."
        s "...included failing limiters, chronic pain and almost universal cases of severe PTSD. The first generation augments were soon replaced with less ambitious second and third generation models."

        n "Sam continues to read out reports and technical schematics on the program."
        if "ch3reportwith" in extraevents:
            show bg ch3report18 with dissolve
            c "Well, that's helpful. If you get into a scrap with an old war relic, you can jab him in the neck with a live power cable!"
            p "I'll keep that in mind."
        p "Okay, what next?"
    else:


        $ extraevents.append("ch3reportaugmentsred")

        s "Bringing up a redacted version, Sir."
        p "Redacted... Of course."
        show bg ch3report9 with dissolve
        s "The Augment program was created in joint by the United States Military and the Baynard Corporation."
        s "A counter was needed for the Akatuski Red Moon program. This was the United States answer."
        s "Biological, chemical and nanotech were used in the subject to increase speed, strength and awareness."
        s "A device known as a limiter was used to manage the subjects' abilities. This, in turn, kept them operational throughout the war."
        s "Though effective in battle, the Red Moon quickly discovered... *Silence*."
        s "Sorry, Sir. That section has been removed from the data stores."
        p "It's not your fault, Sam."
        if "ch3reportwith" in extraevents:
            show bg ch3report19 with dissolve
            c "Yeah, I have a pretty good idea whose fault it is, though."
            p "You and me, both."
        p "Okay, what next?"
    jump ch3reportmenu


label ch3reportredmoon:
    $ extraevents.append("ch3reportredmoon")
    p "Bring up the info on Red Moon, Sam."
    show bg ch3report6 with dissolve
    s "Created by the Akatsuki Zaibatsu for the Japanese Defense Force they were ostensibly designated as anti-terrorist agents."
    if "ch3reportwith" in extraevents:
        show bg ch3report21 with dissolve
        c "Now that's BADASS!"
        p "Yeah, they were."
    show bg ch3report7 with dissolve
    s "Akatsuki was years ahead in the research and development of Cybertechnology, giving Japan the largest edge ever on a worldwide scale."
    s "Their effectiveness was so dominant a single Red Moon squad could eliminate a company of seasoned veteran soldiers in a matter of minutes."
    n "Sam continues to go on about the Red Moon troops."
    p "Nothing I haven't heard before."
    s "The US government contracted Baynard's biotech division to come up with a countermeasure. The result was the Augment program."
    s "Despite early promising results, the Augments proved an imperfect match. The Red Moon quickly learned that a focused EMP burst to the back of an Augment's neck would render the subject immobile until their limiter rebooted."
    if "ch3reportaugments" not in extraevents:
        p "Wait! What was that?"
        s "Would you like me to repeat that, Sir?"
        p "No, it's fine. A little something I think Victoria and Meredith missed."
    if not persistent.glos_redmoon:
        $ persistent.glos_redmoon = True
        $ renpy.notify(['Glossary Updated', 'glossary'])
    p "Okay, what's next?"
    jump ch3reportmenu

label ch3reportnotime:
    s "Sir, I should remind you that you are due to leave shortly."
    p "Right."
    if "ch3reportwith" in extraevents:
        p "Now, you need to go."
        show bg ch3report22 with dissolve
        c "Cool that you let me stay."
        show bg ch3report24 with dissolve
        c "*Grumbles* Damn, these fucking pants."
        c "Was kinda fun, I guess. Not really my thing. Reading, pfft! Overrated!"
        p "Prep is the boring part. The exciting stuff happens later."
        show bg ch3report25 with dissolve
        c "Yeah, enjoy your shooting, old man."
        p "That's what I do..."
        show bg ch3report26 with dissolve
        c "I'm, ugh. Sure it is."
        show bg ch3report27 with dissolve
        c "There, done. Take care! Mauh!"
        p "Stay outta trouble..."
    show bg ch3chandra119 with dissolve
    p "Damn, Sam. That was a long day."
    show bg ch3report29 with dissolve
    p "I may have to... *Yawn*"
    jump ch3sleep
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
