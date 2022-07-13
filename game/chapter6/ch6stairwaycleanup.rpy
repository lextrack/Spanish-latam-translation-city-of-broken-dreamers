

image bg ch6stairchange1 = "ch6stairchange1"
image bg ch6stairchange2 = "ch6stairchange2"
image bg ch6stairchange3 = "ch6stairchange3"
image bg ch6stairchange4 = "ch6stairchange4"
image bg ch6stairchange5 = "ch6stairchange5"
image bg ch6stairchange6 = "ch6stairchange6"
image bg ch6stairchange7 = "ch6stairchange7"
image bg ch6stairchange8 = "ch6stairchange8"
image bg ch6stairchange9 = "ch6stairchange9"
image bg ch6stairchange10 = "ch6stairchange10"
image bg ch6stairchange11 = "ch6stairchange11"
image bg ch6stairchange12 = "ch6stairchange12"
image bg ch6stairchange13 = "ch6stairchange13"
image bg ch6stairchange14 = "ch6stairchange14"
image bg ch6stairchange15 = "ch6stairchange15"
image bg ch6stairchange16 = "ch6stairchange16"
image bg ch6stairchange17 = "ch6stairchange17"
image bg ch6stairchange18 = "ch6stairchange18"
image bg ch6stairchange19 = "ch6stairchange19"
image bg ch6stairchange20 = "ch6stairchange20"
image bg ch6stairchange21 = "ch6stairchange21"
image bg ch6stairchange22 = "ch6stairchange22"
image bg ch6stairchange23 = "ch6stairchange23"
image bg ch6stairchange24 = "ch6stairchange24"
image bg ch6stairchange25 = "ch6stairchange25"
image bg ch6stairchange26 = "ch6stairchange26"


image bg ch6cleanup1 = "ch6cleanup1"
image bg ch6cleanup2 = "ch6cleanup2"
image bg ch6cleanup3 = "ch6cleanup3"
image bg ch6cleanup4 = "ch6cleanup4"
image bg ch6cleanup5 = "ch6cleanup5"
image bg ch6cleanup6 = "ch6cleanup6"
image bg ch6cleanup7 = "ch6cleanup7"
image bg ch6cleanup8 = "ch6cleanup8"
image bg ch6cleanup9 = "ch6cleanup9"
image bg ch6cleanup10 = "ch6cleanup10"
image bg ch6cleanup11 = "ch6cleanup11"
image bg ch6cleanup12 = "ch6cleanup12"



image ch6stairchange = Movie(play='video/chapter-6-video/ch6stairchange.webm', loop=False)
image bg ch6stairchangemovie movie:
    "ch6stairchange"
    pause 11.0
    "ch6stairchangeend"

image ch6stairchangeforehead = Movie(play='video/chapter-6-video/ch6stairchangeforehead.webm', loop=False)
image bg ch6stairchangeforeheadmovie movie:
    "ch6stairchangeforehead"
    pause 8.0
    "ch6stairchangeforheadend"



image bg ch6stairkiss movie = Movie(play='video/chapter-6-video/ch6stairkiss.webm')



label ch6stairwaycleanup:
    scene black with Dissolve(1)
    if "ch6katietease" in extraevents:
        show bg ch6stairchange2 with Dissolve(1)
        k "Ugh, it could be worse."
        show bg ch6stairchange3 with dissolve
        k "God, [p], what have you gotten me into?"
        k "Dad would say, stay strong, Kiddo. Well, Dad... I'm trying."
        show bg ch6stairchange4 with dissolve
        k "Great... Now I'm talking to myself... (Let's just get changed.)"
        scene black with Dissolve(2)
        show bg ch6stairchange1 with dissolve
        p "Katie, you down here?"
        show bg ch6stairchange5 with dissolve
        k "Yeah, just changing. Selection here is... Small."
        p "Sorry..."
        show bg ch6stairchange6 with dissolve
        k "It's not your fault."
        p "Look, I just want to say I'm sorry about tonight. Well, not just tonight, but the last few days."
        show bg ch6stairchange7 with dissolve
        k "It's fine."
        p "No, it's not. You deserve better. I turned everything you know upside down."
        if k_score >= 4:

            show bg ch6stairchange8 with dissolve
            k "[p]... What you're doing is nuts, but it's also right."
            p "Sometimes I don't know about that..."
            show bg ch6stairchange9 with dissolve
            k "I know you think that, but it is."
            show bg ch6stairchange12 with dissolve
            $ renpy.pause(1)
            show bg ch6stairchange11 with dissolve
            k "Hey..."

            menu:
                "Enter":
                    show bg ch6stairchangemovie movie with dissolve
                    p "Hi..."
                    p "God, you're beautiful."
                    k "Thank you."
                    show bg ch6stairchange13 with dissolve
                    p "I just need to be close to you right now."
                    k "You're upset..."
                    show bg ch6stairchange14 with dissolve
                    k "You can talk to me, [p]."
                    show bg ch6stairchange15 with dissolve
                    k "Come on."
                    p "Katie..."
                    show bg ch6stairchange16 with dissolve
                    k "Come on, sit down. Something is really bothering you."
                    p "I don't know if what I'm doing is right."
                    show bg ch6stairchange17 with dissolve
                    k "It is. My Dad said, \"The noble pave the way for the betterment of all.\""
                    p "Not everyone..."
                    k "[p]?"
                    p "People are getting hurt, Katie. People I care about."
                    k "[p], what happened?"
                    p "Ellen... Gloria, she..."
                    k "Ellen, the singer?"
                    p "..."
                    show bg ch6stairchange18 with dissolve
                    k "It's okay, I'm here."
                    p "I think she may be hurt... or worse..."
                    show bg ch6stairchange19 with dissolve
                    p "I just don't know what I will do if anything happens to you."
                    k "Look at me."
                    show bg ch6stairchange20 with dissolve
                    k "I could have run and left this behind. But I didn't. I made my own choice."
                    p "You're too good for this world, you know that?"
                    show bg ch6stairchange22 with dissolve
                    k "I'm where I need to be."
                    show bg ch6stairkiss movie with dissolve
                    p "..."
                    n "Your lips lock and in that fleeting moment, it's just the two of you"
                    show bg ch6stairchange25 with dissolve
                    k "I'm right here, with you."
                    show bg ch6stairchange24 with dissolve
                    k "Umm, in a strange brothel..."
                    p "Heh... Yeah, that wasn't the plan. Look, I should probably let you finish up."
                    show bg ch6stairchange26 with dissolve
                    k "Thanks. I should get back and check on Henry. He probably feels awful."
                    p "Yeah, he seemed pretty upset about it. I'll leave you to it."
                    $ k_score += 1
                "Stay outside":
                    k "I have faith in you, [p]."
                    p "It's just... People are already being hurt..."
                    p "Ellen... I think she may be hurt, or worse, and I don't want to see the same thing happen to you or anyone else."
                    show bg ch6stairchange14 with dissolve
                    k "[p], I could have run and left this behind. But I didn't. I made my own choice."
                    p "You're too good for this world, you know that?"
                    k "I'm where I need to be."
                    p "Katie, thank you. I'll let you finish up here."
                    show bg ch6stairchange5 with dissolve
                    k "Thanks. I should get back and check on Henry after. He probably feels awful."
                    p "Yeah, he seemed pretty upset about it. I'll leave you to it."
        else:

            k "You did, but it doesn't change the fact they need my help."
            show bg ch6stairchange10 with dissolve
            k "Besides, you won't let me go back to my clinic, so let me do what I can here."
            p "Katie, thank you."
            show bg ch6stairchange5 with dissolve
            k "It's the best I can do, now, if you'll excuse me, I need to finish changing so I can go back and check on Henry. He probably feels awful."
    else:

        scene black with Dissolve(1)
        show bg ch6cleanup1 with dissolve
        s "He seems to have done a number on you, Sir."
        p "Sam, not now."
        s "Sorry, Sir. Poor timing."
        s "May I suggest you relax and try to take your mind off things."
        show bg ch6cleanup2 with dissolve
        p "So, you care for me now?"
        s "Even when you tell me to shut it, you know I do, Sir."
        show bg ch6cleanup3 with dissolve
        p "Well, I'm glad I have one friend in this world."
        s "That's why you purchased me."
        if k_score >= 4:
            k "You have more than one friend..."
            show bg ch6cleanup4 with dissolve
            p "Thanks, Katie, right now is when I can use them. I don't know if what I'm doing is right..."
            show bg ch6cleanup6 with dissolve
            k "It is. My Dad said, \"The noble pave the way for the betterment of all.\""
            p "Not everyone..."
            show bg ch6cleanup7 with dissolve
            k "[p]?"
            p "People are getting hurt, Katie. People I care about."
            k "[p], what happened?"
            p "Ellen... Gloria, she..."
            k "Ellen, the singer?"
            p "..."
            menu:
                "Let her approach":
                    show bg ch6cleanup8 with dissolve
                    k "It's okay, I'm here. Talk to me, [p]."
                    p "I think she may be hurt, or worse..."
                    k "[p], I'm sorry..."
                    p "I just don't know what I will do if anything happens to you."
                    show bg ch6cleanup9 with dissolve
                    k "Look at me."
                    k "I could have run and left this behind. But I didn't. I made my own choice."
                    show bg ch6cleanup10 with dissolve
                    p "You're too good for this world, you know that?"
                    k "I'm where I need to be."
                    show bg ch6stairchangeforeheadmovie movie with dissolve
                    p "..."
                    n "As both of you comfort each other, the simple smell of Katie's hair makes you forget everything of the outside world"
                    show bg ch6cleanup11 with dissolve
                    k "Right here, with you. In a brothel..."
                    p "Heh... Yeah, that wasn't the plan."
                    k "I'll let you finish changing. I should get back and check on Henry. He probably feels awful."
                    if h_score >= 4:
                        p "Oh, he is probably pretty proud of himself."
                        show bg ch6cleanup12 with dissolve
                        k "[p]!"
                        p "What?"
                        show bg ch6cleanup11 with dissolve
                        $ k_lust += 1
                        k "I'll meet you back upstairs, just take your time."
                "Keep it friendly":
                    k "It's okay, I'm here. Talk to me, [p]."
                    p "I think she may be hurt, or worse..."
                    show bg ch6cleanup9 with dissolve
                    k "[p], I'm sorry..."
                    p "I just don't know what I will do if anything happens to you."
                    k "Look at me."
                    k "I could have run and left this behind. But I didn't. I made my own choice."
                    p "You're too good for this world, you know that?"
                    k "I'm where I need to be."
                    show bg ch6cleanup11 with dissolve
                    k "In a brothel..."
                    p "Heh... Yeah, that wasn't the plan."
                    k "I'll let you finish changing. I should get back and check on Henry. He probably feels awful."
                    if h_score >= 4:
                        p "Oh, he is probably pretty proud of himself."
                        show bg ch6cleanup12 with dissolve
                        k "[p]!"
                        p "What?"
                        show bg ch6cleanup11 with dissolve
                        $ k_lust += 1
                        k "I'll meet you back upstairs, just take your time."
                    p "Thanks, Katie."
                    show bg ch6cleanup3 with dissolve
    jump ch6stairwaymenu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
