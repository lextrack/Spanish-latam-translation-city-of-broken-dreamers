
image bg ch7henry1 = "ch7henry1"
image bg ch7henry2 = "ch7henry2"
image bg ch7henry3 = "ch7henry3"
image bg ch7henry4 = "ch7henry4"
image bg ch7henry5 = "ch7henry5"
image bg ch7henry6 = "ch7henry6"
image bg ch7henry7 = "ch7henry7"
image bg ch7henry8 = "ch7henry8"
image bg ch7henry9 = "ch7henry9"
image bg ch7henry10 = "ch7henry10"
image bg ch7henry11 = "ch7henry11"
image bg ch7henry12 = "ch7henry12"
image bg ch7henry13 = "ch7henry13"
image bg ch7henry14 = "ch7henry14"
image bg ch7henry15 = "ch7henry15"
image bg ch7henry16 = "ch7henry16"
image bg ch7henry17 = "ch7henry17"
image bg ch7henry18 = "ch7henry18"
image bg ch7henry19 = "ch7henry19"
image bg ch7henry20 = "ch7henry20"
image bg ch7henry21 = "ch7henry21"
image bg ch7henry22 = "ch7henry22"
image bg ch7henry23 = "ch7henry23"
image bg ch7henry24 = "ch7henry24"
image bg ch7henry25 = "ch7henry25"
image bg ch7henry26 = "ch7henry26"
image bg ch7henry27 = "ch7henry27"
image bg ch7henry28 = "ch7henry28"
image bg ch7henry29 = "ch7henry29"
image bg ch7henry30 = "ch7henry30"
image bg ch7henry31 = "ch7henry31"
image bg ch7henry32 = "ch7henry32"
image bg ch7henry33 = "ch7henry33"
image bg ch7henry34 = "ch7henry34"




label ch7stairwayprep:
    play music audio.space fadein 2.0 fadeout 2.0
    scene black with Dissolve(1)
    show bg ch7henry1 with Dissolve(1)
    p "Listen to me! What is the plan, just bust through the front doors?"
    if h_score > 4:
        show bg ch7henry3 with dissolve
        h "If I have to, [p]. I can't stay here and sit on my ass while she is out there, alone."
        p "Ok, let's just calm down and figure this out, ok?"
        show bg ch7henry6 with dissolve
        h "Sorry..."
        show bg ch7henry7 with dissolve
        p "We'll get her back. Ellen, too."
        show bg ch7henry8 with dissolve
        h "Ellen... I'm glad she's alright. She's one of the good ones."
        p "Don't know about alright, but alive is better than the alternative. Maybe Katie can..."
        k "*Yawns* Can what?"

        show bg ch7henry10 with dissolve
    else:

        show bg ch7henry2 with dissolve
        h "They can't stop me."
        p "They will damn sure try. We'll get killed."
        show bg ch7henry4 with dissolve
        h "We? *I* will get her out. I'll protect her. I don't need you in the way!"
        p "I'm just trying to help."
        show bg ch7henry5 with dissolve
        h "Some help you've been. You brought this down on our heads! What have you done but make things worse?"
        k "*Yawns* Can you guys wait until a girl gets some coffee to start fighting?"
        show bg ch7henry11 with dissolve


    k "Geez, look at you two. Who died?"
    k "Oh... wait. Who died?"
    p "No one. It's..."
    h "Gloria, she's..."
    show bg ch7henry12 with dissolve
    k "She's what?"
    p "Missing..."
    show bg ch7henry13 with dissolve
    k "What? Why?! You just found her! Where did she go?!"
    p "We don't know for sure, but the hospital seems likely."
    show bg ch7henry14 with dissolve
    k "Baynard?"
    p "That's the one."
    show bg ch7henry15 with dissolve
    k "Why would she go to a hospital run by the people who sent you to get her?"
    p "Apparently, that's where Ellen is."
    show bg ch7henry16 with dissolve
    k "Your friend, Ellen? She's alive?"
    p "Looks that way."
    k "Well, at least we have some good news."
    h "And another reason we need to go and fast. Who knows what Baynard might try on her."
    k "Agreed. When do we leave?"
    show bg ch7henry17 with dissolve
    h "Not a chance."
    show bg ch7henry18 with dissolve
    k "Did either of you do your residency there? Do you know the place like the back of your hand?"
    h "But..."
    k "Do either of you have the medical knowledge to diagnose Ellen and move her safely, if needed?"
    h "No."
    k "You can't win this argument with me, big guy."
    show bg ch7henry19 with dissolve
    k "So, yeah, I'm coming with you."
    p "She's got you, Henry."
    show bg ch7henry20 with dissolve
    b "So then, you three are heading out?"
    show bg ch7henry32 with dissolve
    b "No need to fill me in, I heard what happened. You're very loud when you're agitated, handsome."
    h "Sorry."
    b "You three head to the hospital. I'll have Venus run a scan on the feeds and I'll run overwatch and let you know if anything comes up."
    h "Thank you, Ma'am."
    show bg ch7henry33 with dissolve
    b "Ma'am? Oh, how you wound me."
    show bg ch7henry22 with dissolve
    b "As for you, doctor, no way you are going out like that."
    show bg ch7henry24 with dissolve
    $ renpy.pause(1)
    show bg ch7henry23 with dissolve
    k "There wasn't much here."
    b "I got something just for you, dearie, don't worry your pretty red aura about it."
    show bg ch7henry25 with dissolve
    k "Well, it can't be more revealing than this thing."
    b "A bit less, you'll see. Come with me, you can meet them outside."
    show bg ch7henry26 with dissolve
    k "Alright..."
    scene black with Dissolve(1)
    if h_score >= 4:
        show bg ch7henry27 with dissolve
        h "Look, I didn't mean to raise my voice in there. I've been losing my cool a lot lately."
        p "I understand. Hey, we'll find her. She'll be alright. Gloria's a smart girl and you taught her well."
        h "Knowing she's ok is the only thing that keeps me going most days."
        p "Henry..."
        h "It's true. I didn't think I'd care about anything after the war."
        menu:
            "Pry":
                p "What we saw was bad, but I heard stories about the Augment units."
                p "Even to us spec ops, you guys were legends."
                h "Hardly."
                if h_score >= 5:
                    p "When you fought the Red Moon you said you had to face your past. What happened?"
                    n "Henry goes silent for a few seconds."
                    call ch7japan from _call_ch7japan
                    play music audio.space fadein 2.0 fadeout 2.0

                    p "So that's why it's personal between you and the Red Moon."
                    h "Yeah..."
                    show bg ch7henry29 with dissolve

                    p "Shit, here comes Katie, you ready?"
                else:


                    h "That's personal."
                    p "Haven't you told anyone?"
                    h "I said it's personal."
                    p "I shouldn't have pried, sorry."
            "Let it go":

                p "She kept you sane and grounded."
                h "Yeah..."
                show bg ch7henry29 with dissolve
                p "Hey, here comes Katie, you ready?"
    else:


        show bg ch7henry28 with dissolve
        h "No funny business. We find her and Ellen and get out of there."
        p "Agreed."
        show bg ch7henry29 with dissolve
        p "Enough talk, here comes Katie."

    h "Yeah."
    show bg ch7henry30 with dissolve
    k "What are you two staring at?"
    p "Nothing."
    show bg ch7henry31 with dissolve
    k "Well, no time to wait. Let's head off."
    jump ch7hospital
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
