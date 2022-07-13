image bg ch7brunch1 = "ch7brunch1"
image bg ch7brunch2 = "ch7brunch2"
image bg ch7brunch3 = "ch7brunch3"
image bg ch7brunch4 = "ch7brunch4"
image bg ch7brunch5 = "ch7brunch5"
image bg ch7brunch6 = "ch7brunch6"
image bg ch7brunch7 = "ch7brunch7"
image bg ch7brunch8 = "ch7brunch8"
image bg ch7brunch9 = "ch7brunch9"
image bg ch7brunch10 = "ch7brunch10"
image bg ch7brunch11 = "ch7brunch11"
image bg ch7brunch12 = "ch7brunch12"
image bg ch7brunch13 = "ch7brunch13"
image bg ch7brunch14 = "ch7brunch14"
image bg ch7brunch15 = "ch7brunch15"
image bg ch7brunch16 = "ch7brunch16"
image bg ch7brunch17 = "ch7brunch17"
image bg ch7brunch18 = "ch7brunch18"
image bg ch7brunch19 = "ch7brunch19"
image bg ch7brunch20 = "ch7brunch20"
image bg ch7brunch21 = "ch7brunch21"
image bg ch7brunch22 = "ch7brunch22"


label ch7brunch:
    scene black with Dissolve(2)
    show text "{=trans}SHORTLY AFTER, AT THE CAFE{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    play music audio.calm fadein 2.0 fadeout 2.0
    show bg ch7brunch1 with dissolve
    if not persistent.ch7card3:
        $ renpy.notify(['Possible clue', 'alert'])
        show screen hidden_item("ch7card3", "ch7card3", 1294, 671, 110, 96)

    p "{i}This is probably a waste of time. Better be worth dragging me here, Chandra.{/i}"
    p "Alright, Chandra, what is so important that you dragged me over here?"
    $ c_score += 1
    hide screen hidden_item
    show bg ch7brunch2 with dissolve
    if "ch7vicredmoon" in extraevents:
        c "[p], what the fuck happened to you?"
        p "Met an old friend..."
    else:
        c "Holy shit, I wasn't sure you'd actually show!"
        p "I said I would."
    c "Well, park your ass."
    if "ch5visitchandra" not in extraevents:
        c "You remember my friend, Abby?"
        ab "Uhh, hey."
        p "Hey, you look much better than the last time I saw you."
        show bg ch7brunch5 with dissolve
        ab "I imagined him in armor; maybe on a horse."
        p "Uh..."
        show bg ch7brunch6 with dissolve
        c "She's just fucking with you."
        show bg ch7brunch4 with dissolve
        ab "Accurate. Gratitude in either case."
        p "Don't mention it."
    else:
        if ab_score >= 1:
            show bg ch7brunch4 with dissolve
            ab "[p]! You have arrived. Please make this place less boring."
            p "Hey, Abby, holding up just fine I see."
            ab "I survive. Somehow or other."
        else:
            show bg ch7brunch3 with dissolve
            ab "Hey, [p]."
            p "Doing alright?"
            ab "I get by."
    show bg ch7brunch6 with dissolve
    p "What are you even doing in this place? Doesn't seem like you."
    c "What do you mean?"
    p "Thought you hated this bougie stuff."
    show bg ch7brunch5 with dissolve
    ab "She does brunch like every weekend. Her mom used to..."
    c "Fuck that! I just love to people watch!"
    show bg ch7brunch7 with dissolve
    c "Like, over there. Look at those assholes."
    show bg ch7brunch18 with dissolve
    c "All caught up in how special they are, vapid as shit. This is like going to a zoo."
    c "And I think that one caught your scent, [p]!"
    show bg ch7brunch19 with dissolve
    ab "You mean the one that looks dumber than a toaster?"
    c "Yeah, but a toaster you can fuck."
    show bg ch7brunch17 with dissolve
    ab "Oh great, Chandra. She caught you staring."
    c "Wait, she didn't want [p]. Incoming to you, Abby!"
    ab "*sighs*"
    show bg ch7brunch20 with dissolve
    "Girl" "*Looking towards Abby* Hi there. I hope it isn't an imposition, but I wanted to say you are an inspiration."
    ab "Thanks?"
    "Girl" "It's so brave of you to come out of Miltown, but you show these fascists that we won't back down. We're with you sister!"

    show bg ch7brunch10 with dissolve
    ab "My existence is suffering after all."
    ab "Why do you have a camera?"
    show bg ch7brunch21 with dissolve
    "Girl" "We can take a selfie together! I have over 10000 followers and it would be great for your struggle to show that we all believe in equality!"
    "Girl" "Your kind and my kind living as one! Like it should be."
    ab "Of course. It's such an honor for me to be seen with your kind."
    n "*Chandra whispers to you*"
    c "Oh shit, this is going to be good."
    show bg ch7brunch10 with dissolve
    ab "I was just here, having brunch with my friends and I was thinking, you know what I need? A rescue."
    show bg ch7brunch9 with dissolve
    ab "If only some self-absorbed pretentious rich girl would come up and ruin my appetite before my shirred eggs even arrived, then my day would be complete."
    ab "After all, if I didn't help her feel better about her utter banality, whatever would I do?"

    show bg ch7brunch22 with dissolve
    "Girl" "I was just trying to be nice, you little bitch!"
    "Other girl" "Let's just get out of here!"
    "Girl" "Fucking Milchers!"
    show bg ch7brunch8 with dissolve
    c "Ha! That was prime fucking epic! I wish I was recording!"
    ab "And this is why I hate coming here."
    c "Come on! You always handle yourself. And it's uber-entertaining."
    show bg ch7brunch11 with dissolve
    ab "For you. I'm tired of it, Chandy."
    show bg ch7brunch12 with dissolve
    ab "I don't exist to make some stranger feel better about themselves."
    c "Fucking hipsters."
    p "I understand Gloria a lot more now."
    ab "Who?"
    menu:
        "A girl I'm trying to protect":
            p "A girl under my protection. Sadly, I'm not doing a great job."
            show bg ch7brunch16 with dissolve
            ab "How so?"
            p "I lost her."
        "A girl like you":


            $ ab_score += 1
            p "A girl like you. Her condition isn't quite as obvious though."
            show bg ch7brunch16 with dissolve
            ab "Not as apparent you say?!"
            p "Shit, I..."
            ab "Fucking with you. I do that a lot. Get used to it."
            p "Right."
            ab "I'd love to meet her sometime."
            p "Well, I have to find her first. She ran off."



    show bg ch7brunch13 with dissolve
    c "OH OH! That's what Mom was freaking out about this morning, then!"
    p "Wait. What did she say?"
    show bg ch7brunch14 with dissolve
    c "Not so fast! What's in it for your favorite little sex kitten?"
    p "Not now, Chandra! This is serious."
    show bg ch7brunch15 with dissolve
    $ extraevents.append("ch7chandrainfo")
    c "Alright, alright! I heard her screaming on the phone. \"Get my men to Redondo Beach, Victoria. NOW!\""
    p "Good impression."
    c "Damn straight. Sounded important."
    if "ch7victell" in extraevents:
        p "She was telling the truth... Well, fuck, I gotta go. Thanks, Chandra."
    else:
        p "Sam, send that info to Betty."
        s "Done, Sir."
        p "Well, fuck me! Sorry, but I gotta go!"
    c "Already? We haven't even gotten food yet!"
    p "I'll pass."
    show bg ch7brunch4 with dissolve
    ab "Good luck."
    p "Thanks, I'll take all I can get."
    jump ch7sonja
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
