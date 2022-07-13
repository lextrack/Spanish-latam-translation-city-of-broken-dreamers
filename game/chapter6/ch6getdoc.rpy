
image bg ch6katie1 = "ch6katie1"
image bg ch6katie2 = "ch6katie2"
image bg ch6katie3 = "ch6katie3"
image bg ch6katie4 = "ch6katie4"
image bg ch6katie5 = "ch6katie5"
image bg ch6katie6 = "ch6katie6"
image bg ch6katie7 = "ch6katie7"
image bg ch6katie8 = "ch6katie8"
image bg ch6katie9 = "ch6katie9"
image bg ch6katie10 = "ch6katie10"
image bg ch6katie11 = "ch6katie11"
image bg ch6katie12 = "ch6katie12"
image bg ch6katie13 = "ch6katie13"
image bg ch6katie14 = "ch6katie14"
image bg ch6katie15 = "ch6katie15"
image bg ch6katie16 = "ch6katie16"
image bg ch6katie17 = "ch6katie17"
image bg ch6katie18 = "ch6katie18"
image bg ch6katie19 = "ch6katie19"
image bg ch6katie20 = "ch6katie20"


image bg ch6stairkatie1 = "ch6stairkatie1"
image bg ch6stairkatie2 = "ch6stairkatie2"
image bg ch6stairkatie3 = "ch6stairkatie3"
image bg ch6stairkatie4 = "ch6stairkatie4"
image bg ch6stairkatie5 = "ch6stairkatie5"
image bg ch6stairkatie6 = "ch6stairkatie6"
image bg ch6stairkatie7 = "ch6stairkatie7"
image bg ch6stairkatie8 = "ch6stairkatie8"
image bg ch6stairkatie9 = "ch6stairkatie9"
image bg ch6stairkatie10 = "ch6stairkatie10"
image bg ch6stairkatie11 = "ch6stairkatie11"

image bg ch6docapproach1 = "ch6docapproach1"
image bg ch6docapproach2 = "ch6docapproach2"
image bg ch6docapproach3 = "ch6docapproach3"

image bg ch6gloriavenus movie = Movie(play="video/chapter-6-video/ch6gloriavenus.webm")



label ch6getdoc:
    play music audio.space fadein 8.0 fadeout 2.0
    scene black with Dissolve(2)
    show bg ch6docapproach2 with Dissolve(2)
    n "The usual bustling commotion rings outside of Katie's hotel"
    ve "Is this the location?"
    b "Just another block, dear."
    show bg ch6docapproach1 with dissolve
    "Angry Woman" "Pfft, are they letting those things walk around now?"
    show bg ch6docapproach3 with dissolve
    b "That's it, darling."
    ve "Thank you."
    scene black with Dissolve(1)
    show bg ch6katie1 with dissolve
    k "Dammit, Gus, your results don't make a lick of sense!"
    k "How did she not have any side effects from that sedative?"
    show bg ch6katie3 with dissolve
    n "A knock on the door startles Katie"
    show bg ch6katie2 with dissolve
    k "*Under her breath* Oh, crap..."
    n "The knock is repeated"
    show bg ch6katie4 with dissolve
    k "Oh, [p], that better be you..."
    show bg ch6katie5 with dissolve
    k "*In a gruff voice* I'm busy, come back later."
    p "Katie, it's me."
    show bg ch6katie6 with dissolve
    k "It's about time!"

    if "ch5katiebanchan" in extraevents:
        p "I brought some banchan like I said I would."
        show bg ch6katie9 with dissolve
        $ renpy.pause(1)
        show bg ch6katie7 with dissolve
        k "Oh, thank god, I could use a real meal!"


    elif "ch5katiemeds" in extraevents:
        p "I got those medical supplies."
        show bg ch6katie9 with dissolve
        $ renpy.pause(1)
        show bg ch6katie7 with dissolve
        k "Perfect. Hopefully we won't need them."
    else:

        p "Katie, I need your help."
        show bg ch6katie9 with dissolve
        $ renpy.pause(1)
        show bg ch6katie7 with dissolve
        k "[p], what's wrong?!"

    show bg ch6katie8 with hpunch
    k "Gah! Who are you!?"
    show bg ch6katie10 with dissolve
    ve "My apologies, miss. It was not my intent to frighten."
    show bg ch6katie12 with dissolve
    k "Answer the question! Who are you!? I-I don't know anything!"
    ve "My owner has requested your service."
    k "Not interested!"
    show bg ch6katie11 with dissolve
    ve "My presence caused you to drop your belongings."
    show bg ch6katie13 with dissolve
    k "What are you doing here!? What do you want? Who... Wait. You're that Venus thing plastered everywhere."
    ve "Yes, I was activated just recently. "
    k "I'm not interested in what you're selling."
    ve "My regulations state that I am not allowed to sell my services outside of pre-approved establishments."
    show bg ch6katie14 with dissolve
    ve "I believe you dropped this."
    show bg ch6katie15 with dissolve
    k "Umm, thanks... I guess?"
    ve "Again, your services are required."
    k "For whom?"
    n "Through Venus, you speak"
    if "ch5katiebanchan" in extraevents:
        p "Katie, it's me, I told you I was going to grab you some banchan the other night."
    elif "ch5katiemeds" in extraevents:
        p "Katie, it's me, I told you I was going to get you more supplies. Well I may have found some."
    else:
        p "Katie, a few days ago before we went into Lakewood together, a little boy got pus all over you."

    k "[p]?"
    p "Yeah, it's me. We need your help -- fast. Henry is hurt pretty bad."


    show bg ch6katie16 with dissolve
    if k_score >= 3:
        k "What about you, [p]? Please tell me you're alright?"
        p "I'll be fine, don't worry about me."
        k "*sighs in relief*"
    k "This is insane! And I just put my clothes in the laundry! Whatever, take me to them."

    jump ch6vic

label ch6getdocstairway:

    scene black with Dissolve(2)
    show text "{=trans}BACK AT THE STAIRWAY TO HEAVEN{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)

    play music audio.space fadein 8.0 fadeout 2.0
    scene black with Dissolve(2)
    show bg ch6katie17 with dissolve
    ve "Here we are."
    show bg ch6katie18 with dissolve
    k "What on earth?"
    ve "Welcome to my home. The Stairway to Heaven is the premier lounge for the pursuit of erotic delights."
    k "It's, uh... nice."
    ve "Thank you!"
    show bg ch6katie19 with dissolve
    k "Do you \"sleep\" in one of these, too?"
    ve "I was told you are curious. But, yes, sometimes."
    show bg ch6katie20 with dissolve
    ve "Your friends are out back. If you will follow me?"
    k "Yeah, umm, lead the way."
    show bg ch6stairkatie1 with Dissolve(1)
    k "[p]? Please tell me you're here."
    p "Yeah, Katie. Back here."
    show bg ch6stairkatie2 with dissolve
    k "Jesus..."
    ve "Delivered as promised, Ma'am."
    b "Good work, Venus!"
    show bg ch6stairkatie6 with dissolve
    ve "I used my voice modulation for the first time, Ma'am. Are you proud?!"
    show bg ch6stairkatie9 with dissolve
    b "Of course, Venus! But we can talk later. Now stay out of the way, unless our new friend needs help."
    ve "Yes, Ma'am."
    show bg ch6stairkatie5 with dissolve
    k "[p], she scared the bejesus out of me. I thought it was you!"
    k "Forget it... Okay, Henry, let's take a look at you."
    h "*Grumbles*"
    show bg ch6stairkatie4 with dissolve
    k "What happened to him?"
    p "He took some pretty bad hits, we got him here then he dropped like a rock. We had to resuscitate the big guy."
    show bg ch6stairkatie3 with dissolve
    k "Okay, Henry, I'm going to take a look. [p], you resuscitated him? How?"
    p "With a shot of adrenaline."
    show bg ch6stairkatie8 with dissolve
    k "Okay, that should be fine. If you feel really tired now, Henry, that's why."
    h "*Grunts* It's my limiter, it was already starting to break down."
    k "Your what?"
    show bg ch6stairkatie7 with dissolve
    h "Back here. Keeps my body from tearing itself apart."
    k "Interesting. This is going to be more complicated than I thought."
    show bg ch6stairkatie10 with dissolve
    k "Ahh. I'll need some time with this. Henry, I'd like to take you out front, can you move at all?"
    h "A bit, sure."
    show bg ch6stairkatie11 with dissolve
    k "Okay, good. Just take your time."
    k "[p], if you get a chance, meet me out front, okay?"
    p "Will do, Doc."
    show bg ch6gloriavenus movie with Dissolve(1)
    $ extraevents.append("ch6inroom")
    $ resetmenu()


    jump ch6stairwaymenu






label ch6stairwaymenu:




    menu:
        "Check on Gloria" if "ch6checked" not in extraevents:
            $ extraevents.append("ch6checked")
            $ extraevents.append("ch6inroom")
            $ menu6 = False
            jump ch6stairwaygloria

        "Search Lockers" if "ch6inroom" in extraevents and "ch6secret" not in extraevents and menu4 == True:
            jump ch6stairwaylockers

        "Talk to Betty" if menu3 == True:
            if "ch6inroom" in extraevents:
                $ extraevents.remove("ch6inroom")
            $ menu3 = False
            jump ch6stairwaybetty

        "Talk to Katie and Henry" if menu2 == True:
            if "ch6inroom" in extraevents:
                $ extraevents.remove("ch6inroom")
            $ menu2 = False
            jump ch6stairwaykatie




        "Check on Katie" if menu7 == True and "ch6katietease" in extraevents:
            if "ch6inroom" in extraevents:
                $ extraevents.remove("ch6inroom")
            $ menu7 = False
            jump ch6stairwaycleanup




        "Check your room" if menu3 == False and menu4 == True:
            if "ch6inroom" in extraevents:
                $ extraevents.remove("ch6inroom")
            $ menu4 = False
            jump ch6stairwayroom

        "Check on Gloria again" if menu5 == True and "ch6checked" in extraevents and "ch6inroom" not in extraevents:

            $ extraevents.append("ch6gloriaawake")
            $ menu5 = False
            jump ch6stairwaygloria2

        "Go to Sleep" if menu4 == False and "ch6gloriaawake" in extraevents:
            jump ch6morning

    if "ch6checked" in extraevents and menu6 == False and menu2 == False and menu3 == False and menu4 == False:

        show bg ch6stairway0 with dissolve
        n "On your way out of Gloria's room, you hear commotion behind you"
        $ extraevents.append("ch6gloriaawake")
        $ menu5 = False
        jump ch6stairwaygloria2



image bg ch6locker1 = "ch6locker1"
image bg ch6locker2 = "ch6locker2"
image bg ch6locker3 = "ch6locker3"

label ch6stairwaylockers:
    show bg ch6locker1 with dissolve
    p "Let's see what other crazy stuff you have in here."
    s "Betty may not be pleased."
    show bg ch6locker2 with dissolve
    if not persistent.ch6card1:
        $ renpy.notify(['Possible clue', 'alert'])
        show screen hidden_item("ch6card1", "ch6card1", 1052, 57, 168, 380)
    p "I can't help it, sorry."

    $ extraevents.append("ch6secret")
    p "What's this?"
    s "An older data disk. It is encoded, but with time, I can decrypt it."
    hide screen hidden_item
    show bg ch6locker3 with dissolve
    p "Might be useful. Do it."
    show bg ch6gloriavenus movie with Dissolve(1)
    jump ch6stairwaymenu

image bg ch6stairvenus1 = "ch6stairvenus1"
image bg ch6stairvenus2 = "ch6stairvenus2"
image bg ch6stairvenus3 = "ch6stairvenus3"
image bg ch6stairvenus4 = "ch6stairvenus4"
image bg ch6stairvenus5 = "ch6stairvenus5"
image bg ch6stairvenus6 = "ch6stairvenus6"
image bg ch6stairvenus7 = "ch6stairvenus7"


label ch6stairwaygloria:
    scene black with dissolve
    show bg ch6stairvenus1 with dissolve
    n "Venus hums as she brushes Gloria's hair"
    p "How's she doing?"
    show bg ch6stairvenus6 with dissolve
    ve "Unknown. She is very quiet."
    ve "Heh, like a mouse."
    p "I've heard that before."
    show bg ch6stairvenus2 with dissolve
    ve "What is she like? Will she like me when she wakes up?"
    p "Well, she may be a bit taken aback at first."
    show bg ch6stairvenus3 with dissolve
    ve "But why?"
    p "Well, you're not like most, Venus."
    p "Just give her time to adjust and I am sure you will get along. She's surprisingly optimistic. Especially considering everything she's been through."
    show bg ch6stairvenus4 with dissolve
    ve "Fantastic. I hope we can be friends, just like sisters!"
    menu:
        "Hopefully":
            p "Yeah, hopefully, you can. It could be fun."
            ve "I hope so, I always wanted a sister."
            p "You were born a few days ago."
            ve "And?"
            p "Never mind."
        "May want to ease back":
            $ extraevents.append("ch6venusholdback")
            p "Well, I wouldn't be so forward about it. Don't put too much pressure on her."
            show bg ch6stairvenus5 with dissolve
            ve "Why?"
            p "It may make her uncomfortable."
            ve "Why?"
            p "She doesn't know you yet, so if you put too much pressure on her she might not take it well."
            ve "Why?"
            p "*Sighs* Just trust me on this, and don't say \"why,\" again."
            show bg ch6stairvenus4 with dissolve
            ve "How come?"
            p "Okay, I'm leaving."
    show bg ch6stairvenus7 with dissolve
    p "Just, keep her comfortable for now."
    ve "I will!"
    show bg ch6gloriavenus movie with Dissolve(1)
    jump ch6stairwaymenu

image bg ch6stairexam1 = "ch6stairexam1"
image bg ch6stairexam2 = "ch6stairexam2"
image bg ch6stairexam3 = "ch6stairexam3"
image bg ch6stairexam4 = "ch6stairexam4"
image bg ch6stairexam5 = "ch6stairexam5"
image bg ch6stairexam6 = "ch6stairexam6"
image bg ch6stairexam7 = "ch6stairexam7"
image bg ch6stairexam8 = "ch6stairexam8"
image bg ch6stairexam9 = "ch6stairexam9"
image bg ch6stairexam10 = "ch6stairexam10"
image bg ch6stairexam11 = "ch6stairexam11"
image bg ch6stairexam12 = "ch6stairexam12"
image bg ch6stairexam13 = "ch6stairexam13"
image bg ch6stairexam14 = "ch6stairexam14"
image bg ch6stairexam15 = "ch6stairexam15"
image bg ch6stairexam16 = "ch6stairexam16"
image bg ch6stairexam17 = "ch6stairexam17"
image bg ch6stairexam18 = "ch6stairexam18"
image bg ch6stairexam19 = "ch6stairexam19"
image bg ch6stairexam20 = "ch6stairexam20"
image bg ch6stairexam21 = "ch6stairexam21"
image bg ch6stairexam22 = "ch6stairexam22"



label ch6stairwaykatie:
    scene black with dissolve
    show bg ch6stairexam1 with dissolve
    k "Okay, Henry, let's see what's wrong here."
    show bg ch6stairexam2 with dissolve
    k "First, has it caused you problems before?"
    show bg ch6stairexam3 with dissolve
    h "Yeah, but not like this."
    k "Like what, then?"
    h "Headaches, mainly. Sometimes it gets hard to control my strength for a few minutes."
    k "How do you handle it?"
    h "We learned how to handle ourselves in the field. Self-maintain. Small fixes here and there."
    show bg ch6stairexam4 with dissolve
    h "But, after taking a blow like that... I don't know, it feels worse."
    k "How long since you saw a specialist?"
    h "Three years?"
    show bg ch6stairexam6 with dissolve
    k "We'll figure it out. I mean how hard can it be, right?"
    p "Everything going okay?"
    show bg ch6stairexam7 with dissolve
    k "Yeah, this thing may be old, but, holy cow, the components alone are worth a fortune."
    k "Now, Henry, sit still and no talking. I just want to run a few quick tests."
    if "ch6henryjoke" in extraevents:
        h "[p], I just want to apologies for trying to make a joke on the way here."
        h "It was-"
        k "Henry. Shh... Just relax."
        p "It's fine."
        $ h_score += 1

    show bg ch6stairexam9 with dissolve
    k "This tech is crazy. I've heard of some of it, but half of it still isn't cleared for regular use."
    p "Have you ever seen anything like it before?"
    k "Yeah, to a degree. Something similar is used for severe spinal damage, but it's nowhere near this complex."
    k "I mean, it uses nano-tech. Do you have any idea how hard that is to acquire?"
    h "Yeah, that makes it hard to re-"
    show bg ch6stairexam5 with dissolve
    k "HEY! Quiet, mister! If you talk, it will screw up the scan and who knows what else."
    h "..."
    show bg ch6stairexam9 with dissolve
    k "Thank you. Now, just stare forward."

    menu:
        "Need Help?":
            $ extraevents.append("ch6katiehelp")
            p "Need any help, Katie?"
            show bg ch6stairexam8 with dissolve
            k "Yeah, actually. Keep an eye on his pupils. Looking for any rapid expansion."
            p "Yeah, I can do that."
            show bg ch6stairexam14 with dissolve
            k "Anything?"
            p "All looks normal to me."
            show bg ch6stairexam16 with dissolve
            k "Okay, let me crank this up. Henry nod your head if you feel discomfort."
            show bg ch6stairexam15 with dissolve
            k "Anything, [p]?"
            p "Everything looks normal."
            k "Okay, let's try this."
            show bg ch6stairexam13 with dissolve
            n "You hear a spike go off from Katie's monitor"
            show bg ch6stairexam12 with dissolve
            h "HUUUGGGMPPHH!!"
            show bg ch6stairexam18 with dissolve
            k "..."
            h "..."
            p "..."
            p "I'm so glad you didn't eat today. That could have been so much worse."
            show bg ch6stairexam17 with dissolve
            if h_score < 3:
                h "I should feel bad about that, but I really don't."
                p "I'm sure."
            else:
                h "[p], I'm sorry. I didn't mean to do that."
                p "Obviously..."
            show bg ch6stairexam19 with dissolve
            k "Heh, [p], maybe you should go clean up."
            p "Try not to puke on Katie, please."
            $ achievement.grant("EWWW")
            init:
                $ achievement.register("EWWW")
            $ achievement.Sync()
            h "I'll do my best."

            jump ch6stairwaycleanup
        "Talk to Henry":


            $ extraevents.append("ch6katietease")
            p "Heh, Henry, looks like you're being put in your place."
            h "She has her ways."
            k "I said no talking! Am I going to have to ask you to leave, [p]?"
            show bg ch6stairexam10 with dissolve
            n "You hear a spike go off from Katie's monitor."
            k "Uh-oh!"
            show bg ch6stairexam11 with dissolve
            h "HUUUGGGMPPHH!!"
            k "..."
            h "..."
            p "..."
            show bg ch6stairexam20 with dissolve
            h "I-I didn't..."
            show bg ch6stairexam22 with dissolve
            k "*Cracks out laughing* Henry, are you okay?"
            h "I should be asking you that."
            show bg ch6stairexam21 with dissolve
            k "Heh, I've had worse, trust me. You two wait here, I think I should probably clean up."
            scene black with dissolve
            show bg ch6stairexam4 with dissolve
            h "Talk about embarrassing..."
            p "She's seen much worse. Trust me."
            h "Still..."

            jump ch6stairwaymenu




label ch6stairwayroom:
    scene black with Dissolve(1)
    show bg ch6watch54 with Dissolve(1)

    p "*Exhales* Fucking hell."
    s "Sir, you need to sit."
    show bg ch6watch1 with dissolve
    p "You're right."
    s "Did you want to talk? I can load a psychologist profile."
    p "Are you kidding me?"
    s "It may help, Sir."
    p "I appreciate it, Sam, but I'll pass."
    p "Sam, I'm going to go stir crazy. You have anything for me?"
    s "There was activity at Miss Shields's apartment. Would you like me to play it?"
    p "Anything important?"

    if "ch3venusprincess" in extraevents or "ch3venusslut" in extraevents:
        show bg ch6watch56 with dissolve
        ve "*From outside the door* Sir, would you like some company?"
        p "I thought you were watching over Gloria?"
        show bg ch6watch57 with dissolve
        if "ch6gloriaawake" in extraevents:
            ve "She is browsing the networks currently."
        else:
            ve "She is still asleep."
        menu:
            "Go back and keep an eye on her":
                p "You should probably go back and keep an eye on her."
                show bg ch6watch56 with dissolve
                ve "Okay! I hope I didn't disturb you."
                p "It's fine."
                show bg ch6watch1 with dissolve
                p "Sorry, Sam, go on."
                jump ch6stairwayroomstir
            "Sure come in":
                $ extraevents.append("ch6venuswatch")
                jump ch6vicbathalone
    else:

        jump ch6stairwayroomstir


label ch6stairwayroomstir:

    s "It's nothing pertaining to our situation if that is what you mean by important."
    p "Whatever, play it."
    jump ch6vicbathalone


image bg ch6vic1 = "ch6vic1"
image bg ch6vic2 = "ch6vic2"
image bg ch6vic3 = "ch6vic3"
image bg ch6vic4 = "ch6vic4"
image bg ch6vic5 = "ch6vic5"
image bg ch6vic6 = "ch6vic6"
image bg ch6vic7 = "ch6vic7"
image bg ch6vic8 = "ch6vic8"
image bg ch6vic9 = "ch6vic9"
image bg ch6vic10 = "ch6vic10"
image bg ch6vic11 = "ch6vic11"
image bg ch6vic12 = "ch6vic12"
image bg ch6vic13 = "ch6vic13"
image bg ch6vic14 = "ch6vic14"
image bg ch6vic15 = "ch6vic15"
image bg ch6vic16 = "ch6vic16"
image bg ch6vic17 = "ch6vic17"
image bg ch6vic18 = "ch6vic18"
image bg ch6vic19 = "ch6vic19"
image bg ch6vic20 = "ch6vic20"
image bg ch6vic21 = "ch6vic21"
image bg ch6vic22 = "ch6vic22"
image bg ch6vic23 = "ch6vic23"
image bg ch6vic24 = "ch6vic24"



label ch6vicbathalone:
    if "ch6venuswatch" not in extraevents:
        show bg ch6watch1 with dissolve
        $ renpy.pause(1)
        show bg ch6watch2 with dissolve
        $ renpy.pause(1)
        show bg ch6vic1 with Dissolve(2)
        "Hope" "Playing last message from Meredith White as instructed."
        show bg ch6vic2 with dissolve
        $ renpy.pause(1)
        show bg ch6vic3 with dissolve
        m "Hello, Victoria. No need to return this call. This is simply a status update on our current negotiations."
        show bg ch6vic4 with dissolve
        m "The chief arrived with a spring in her step. Even if she didn't rave about your time together, I would know she was pleased with you."
        show bg ch6vic5 with dissolve
        m "We have her on the hook, now all we need to do is finish reeling her in."
        show bg ch6vic9 with dissolve
        $ renpy.pause(1)
        show bg ch6vic10 with dissolve
        m "Her current objections are akin to those of a demure school girl on prom night. She knows what she wants, but doesn't care to admit it."
        show bg ch6vic6 with dissolve
        m "I knew you wouldn't let me down, dear."
        show bg ch6vic7 with dissolve
        $ renpy.pause(1)
        show bg ch6vic8 with dissolve
        m "She wants to see you again. I told her you were at her disposal tomorrow. One encounter with you can be pleasant, but two, that is a burgeoning addiction."
        show bg ch6vic11 with dissolve
        m "Again, very good work. Take the rest of the day off."
        m "Let's close this deal tomorrow."
        show bg ch6vic12 with dissolve
        p "Sam, turn this off."
        s "Are you sure, Sir?"

        jump ch6stairwayroomcontinue
    else:


        show bg ch6watch9 with dissolve
        ve "What are you doing, Daddy?"
        p "About to watch a video feed."
        ve "May I join you?"
        p "Sure. Sam, play it."
        show bg ch6watch3 with dissolve
        "Hope" "Playing last message from Meredith White as instructed."
        show bg ch6vic2 with dissolve
        $ renpy.pause(1)
        show bg ch6vic3 with dissolve
        m "Hello, Victoria. No need to return this call. This is simply a status update on our current negotiations."
        show bg ch6watch7 with dissolve
        ve "I like her hair."
        show bg ch6vic4 with dissolve
        m "The chief arrived with a spring in her step. Even if she didn't rave about your time together, I would know she was pleased with you."
        show bg ch6vic5 with dissolve
        m "Her current objections as transparent as those of a demure school girl on prom night. She knows what she wants, but doesn't care to admit it."
        show bg ch6vic9 with dissolve
        $ renpy.pause(1)
        show bg ch6vic10 with dissolve
        m "Hopefully, we shall have their cooperation going forward."
        show bg ch6vic6 with dissolve
        m "I knew you wouldn't let me down, dear."
        show bg ch6vic7 with dissolve
        $ renpy.pause(1)
        show bg ch6vic8 with dissolve
        m "She wants to see you again. I told her you were at her disposal tomorrow. One encounter with you can be pleasant, but two, that is a burgeoning addiction."
        show bg ch6watch6 with dissolve
        ve "Does she turn you on?"
        p "What?"
        ve "Does she turn you on? You can pretend I'm her if you would like?"
        show bg ch6watch8 with dissolve
        ve "She can nibble on your ear."
        show bg ch6watch10 with dissolve
        ve "Have her hand move between your legs."
        show bg ch6watch11 with dissolve
        ve "Does this please you, Daddy?"


        if dep <= 1:

            p "Just stop. This isn't right."
            ve "Are you sure, Daddy?"
            p "Just go."
            show bg ch6watch12 with dissolve
            ve "Very well, [p]."
            show bg ch6watch54 with dissolve
            p "*Sighs* Fuck me..."
            s "Did you wish to continue watching the feed?"
            jump ch6stairwayroomcontinue
        else:
            show bg ch6watch13 with dissolve
            ve "You can punish her. I bet you want to do that don't you?"
            menu:
                "Yes":
                    play music audio.tensesexy fadein 2.0 fadeout 2.0
                    p "You have no idea."
                    show bg ch6watch14 with dissolve
                    ve "Mmm, I bet you want her to submit to you."
                    ve "Lights."
                    show bg ch6watch15 with dissolve
                    p "She always wants to be in control."
                    ve "Then take it from her. Treat her how she deserves."
                    show bg ch6watch15vic with Dissolve(2)
                    show bg ch6watch15 with Dissolve(2)
                    n "The feed continues to play in the background, with your attention drawn elsewhere"
                    jump ch6venusslut
                "Stop":
                    p "Just stop. This isn't right."
                    ve "Are you sure, Master?"
                    p "Just go."
                    show bg ch6watch12 with dissolve
                    ve "Very well, [p]."
                    show bg ch6watch54 with dissolve
                    p "*Sighs* Fuck me..."
                    s "Did you wish to continue watching the feed?"

                    jump ch6stairwayroomcontinue

image ch6vicscream = Movie(play='video/chapter-6-video/ch6vicscream.webm', loop=False)
image bg ch6vicscreammovie movie:
    "ch6vicscream"
    pause 11.0
    "ch6vicscreamend"

label ch6stairwayroomcontinue:
    menu:
        "Stop watching":
            p "We don't need to watch this."
        "Keep watching":
            $ extraevents.append("ch6bathcomplete")
            show bg ch6vic13 with dissolve
            $ renpy.pause(1)
            show bg ch6vic14 with dissolve
            p "Where did the audio go?"
            show bg ch6vic15 with dissolve
            s "No receiver in the room, Sir."
            show bg ch6vic16 with dissolve
            s "I could only route in the message from Mrs. White."
            show bg ch6vic17 with dissolve
            $ renpy.pause(1)
            show bg ch6vic18 with dissolve
            p "No problem, Sam."
            show bg ch6vic20 with dissolve
            $ renpy.pause(1)
            show bg ch6vic19 with dissolve
            n "Victoria gently sets her glass of wine down on the side of the tub"
            show bg ch6vic21 with dissolve
            n "Lifting herself, Victoria stares into the calm water"
            show bg ch6vic22 with dissolve
            $ renpy.pause(1)
            show bg ch6vicscreammovie movie with dissolve
            p "..."
            p "Fuck me..."
            s "I told you it did not pertain to our situation."
            show bg ch6vic23 with hpunch
            n "After knocking the glass away Victoria becomes still and stares ahead"
            show bg ch6watch5 with dissolve


    p "Shut it off..."
    s "Are you certai..."
    p "Yes! I've had enough of this horrible shit for one day."
    show bg ch6watch55 with dissolve
    s "Of course, Sir. I'll leave you be."
    p "No, Sam, wait."
    s "Yes, Sir?"
    p "Can you tell me about Ellen's family? She never mentioned anything to me."
    s "Checking... Her mother is alive. Father deceased. Only child."
    p "Tell me about her mother?"
    s "Yasuko Lane. Born 1992, Portland Oregon. Married Michael Lane in 2014."
    s "Currently residing in Bloomington, Idaho."
    p "What happened to her father?"
    s "He died due to complications with Leukemia in 2021. Anything else?"
    p "So much for no more depressing shit..."
    s "Sorry, Sir. Will there be anything else?"
    p "That's fine."

    if "ch6secret" in extraevents:
        s "Wait, Sir. That data chip you found has just finished processing."
        p "And?"
        s "It's a VR simulation, Sir. This room has a VR set. I could hook you in if you wish?"
        if "ch1futapartial" in extraevents:
            p "With your \"Special,\" choices. No thank you."
            s "Special, yes, but not in that fashion. Also, an AI. Not a live connection. It would be good for you, Sir."
        else:
            p "I don't know, Sam."
            s "It would be good for you. Just an AI, not a live connection."
        menu:
            "Alright fine":
                s "On the dresser to the left."
                show bg ch6watch58 with dissolve
                call ch6carli from _call_ch6carli
                p "Okay, Sam. Maybe I'll take you up on those offers more often."
                s "Glad to be of service."
            "Not now":
                p "Sam, I know you're just trying to cheer me up. I get it, but I'm good."
                s "Of course, Sir. I'll leave you be."
    jump ch6stairwaymenu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
