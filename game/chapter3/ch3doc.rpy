
image bg ch3doc1 = "ch3doc1"
image bg ch3doc2 = "ch3doc2"
image bg ch3doc3 = "ch3doc3"
image bg ch3doc4 = "ch3doc4"
image bg ch3doc5 = "ch3doc5"
image bg ch3doc6 = "ch3doc6"
image bg ch3doc7 = "ch3doc7"
image bg ch3doc8 = "ch3doc8"
image bg ch3doc9 = "ch3doc9"
image bg ch3doc10 = "ch3doc10"
image bg ch3doc11 = "ch3doc11"
image bg ch3doc12 = "ch3doc12"
image bg ch3doc13 = "ch3doc13"
image bg ch3doc14 = "ch3doc14"
image bg ch3doc15 = "ch3doc15"
image bg ch3doc16 = "ch3doc16"
image bg ch3doc17 = "ch3doc17"
image bg ch3doc18 = "ch3doc18"
image bg ch3doc19 = "ch3doc19"
image bg ch3doc20 = "ch3doc20"
image bg ch3doc21 = "ch3doc21"
image bg ch3doc22 = "ch3doc22"
image bg ch3doc23 = "ch3doc23"
image bg ch3doc24 = "ch3doc24"
image bg ch3doc25 = "ch3doc25"
image bg ch3doc26 = "ch3doc26"
image bg ch3doc27 = "ch3doc27"
image bg ch3doc28 = "ch3doc28"
image bg ch3doc29 = "ch3doc29"
image bg ch3doc30 = "ch3doc30"


image ch3katiemovie = Movie(play='video/chapter-3-video/ch3katie.webm', loop=False)
image bg ch3katiemov movie:
    "ch3katiemovie"
    pause 8.0
    "ch3katie"


label ch3doc:
    scene black with Dissolve(2)
    show text "{=trans}A SHORT WHILE LATER, AT DR. HAMILTON'S CLINIC{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    play music audio.calm fadein 2.0 fadeout 2.0
    hide text with Dissolve(1)
    if k_score >= 3:
        p "Hey Katie, you here?"
    else:
        p "Hey Doc, you around?"
    show bg ch3doc1 with dissolve
    k "Yeah, in here."
    show bg ch3katiemov movie with dissolve
    k "Hey, how are you?"
    if "ch2choosekatie" in extraevents:
        p "I'm good and you?"
        k "I'm... fine."
        show bg ch3doc2 with dissolve
        p "Hey, what's the matter?"
        show bg ch3doc3 with dissolve
        p "You looked like you couldn't get out of my place fast enough. What happened?"
        show bg ch3doc4 with dissolve
        k "It's nothing. I just had to run."
        p "If I did something last night to make you uncomfortable..."
        show bg ch3doc5 with dissolve
        k "It's nothing you did. It's... how do I explain?"
        k "Last night was just a bit too much for me. You know?"
        p "I did throw a lot at you."
        show bg ch3doc7 with dissolve
        k "Yeah."
        k "It's okay. I'm glad you did."
        p "Glad usually doesn't mean running out the door as you did. "
        k "How do I explain? You're not like the others."
        show bg ch3doc6 with dissolve
        p "Others?"
        k "The other Ghosts. I'm just another piece of equipment to them."
        k "You treat me with respect... What other Ghost would ever ask for my help other than to stitch up a wound?"
        p "Hey, come here."
        show bg ch3doc8 with dissolve
        p "Most people in this business are out for themselves. But you? You remind me that there are still good people out there."
        k "You mean that?"
        show bg ch3doc11 with dissolve
        p "I do, I really do."
        menu:
            "Let your hands wander":
                show bg ch3doc27 with dissolve
                if k_lust >= 1 and k_score >= 3:
                    $ k_lust += 1
                    k "[p]..."
                    p "Yeah?"
                    show bg ch3doc26 with dissolve
                    k "I'm a traditional girl."
                    p "So, what does that mean?"
                    k "It means time and place. And not so fast, Romeo."
                else:
                    $ k_lust -= 1
                    k "Umm, [p]?"
                    p "Sorry, I..."
                    show bg ch3doc26 with dissolve
                    k "It's okay."
            "You're a gentleman":
                $ k_score += 1
                k "[p]..."
                p "I mean it, this world needs more people like you."
                show bg ch3doc11 with dissolve
                k "Ha! Who would have thought that the big bad Ghost is a softie at heart?"
                p "Hey, I have a reputation to keep!"
                k "My lips are sealed."
        k "Moving on..."
        k "You're here for the results?"
        p "Yeah..."
        k "I wish I had better news."
        show bg ch3doc12 with dissolve
        $ renpy.pause(1)
        show bg ch3doc13 with dissolve
        $ renpy.pause(1)
        show bg ch3doc15 with dissolve
        p "This doesn't sound like it's going to be good."
        show bg ch3doc16 with dissolve
        k "I didn't find much... "
        p "What did you find?"
        show bg ch3doc17 with dissolve
        k "Well, the good news is, I was right."
        p "What do you mean?"
        k "These wounds aren't possible. At least not by any means I know of."
        k "And that's the bad news. Whatever tech did this, it is generations ahead of anything I have ever seen."
        p "Then I best hope they don't use it on me."
        k "This isn't a joke! You need to be careful, [p]."
        p "I always am."
        show bg ch3doc14 with dissolve
        k "Just promise me you won't end up like your friends from the other night."
        p "I won't."
        show bg ch3doc17 with dissolve
        k "I mean it, [p]. Promise me you won't get yourself killed."
        p "Trust me. That's the last thing I want."
        show bg ch3doc19 with dissolve
        k "[p], I said promise."
        p "Doc, I promise."
        show bg ch3doc18 with dissolve
        k "It's Katie..."
        p "I promise you, Katie. I'll come back."



    elif k_score >= 1:
        p "I'm good, and you?"
        call ch3katieexplain from _call_ch3katieexplain
        p "Doesn't sound like your lucky day."
        show bg ch3doc4 with dissolve
        k "Better than yours. I'm not facing something that can melt my brain."
        p "I'll be careful."
        show bg ch3doc5 with dissolve
        k "I've heard that before."
        p "..."
        show bg ch3doc7 with dissolve
        k "Damn, why do you have to be so nice?"
        menu:
            "Where is this coming from?":
                $ k_score += 1
                p "Why wouldn't I be nice to you?"
                k "I just hear things about you. You know?"
                show bg ch3doc6 with dissolve
                p "Look at me. I don't know what you have heard, but I'm not such a bad guy."
                k "I know. You're not like the others, but you try to make people think you are."
                p "Look, I don't know what it is, but something is bothering you. You can come clean with me, Doc."
                show bg ch3doc11 with dissolve
                k "I guess I'm just scared. I don't want to see you hurt, or worse. I keep a distance from my clients for a reason."
                p "I have a job that I need to do."
                k "I know..."
                call ch3katiewalkaway from _call_ch3katiewalkaway
            "Reach out to her":

                p "Come here."
                if k_score >= 2:
                    $ k_lust += 1
                    show bg ch3doc9 with dissolve
                    k "[p], I..."
                    p "It's okay. I know you're scared. Truth is, I get anxious before a job too."
                    p "It'll be alright."
                    k "Just hold me..."
                    show bg ch3doc8 with dissolve
                    k "I finally meet a Ghost who I kind of like and then he runs off into God knows what."
                    p "You met a Ghost you like? Do I know him?"
                    show bg ch3doc24 with dissolve
                    k "*Laughs* [p], there you go again."
                    p "There's that smile."
                    show bg ch3doc11 with dissolve
                    k "You can't stop teasing me, can you?"
                    p "Nope."
                    show bg ch3doc25 with dissolve
                    k "I am really worried, [p]. Five Ghosts have died on this run already. Don't be number six."
                    call ch3katiewalkaway from _call_ch3katiewalkaway_1
                else:
                    show bg ch3doc23 with dissolve
                    k "Look, [p], you have more important things to worry about than me."
                    show bg ch3doc12 with dissolve
                    $ renpy.pause(1)
                    show bg ch3doc13 with dissolve
                    $ renpy.pause(1)
                    show bg ch3doc15 with dissolve
                    k "Like, shouldn't you be planning a kidnapping for your megacorp? Do you even know why they want this girl?"
                    p "It's the job, Katie."
                    show bg ch3doc14 with dissolve
                    k "It just seems so wrong. Does it ever bother you? Doing what you do?"
                    p "This is the world we live in and you know that. We do what we can to survive. You're part of this world too."
                    show bg ch3doc16 with dissolve
                    k "I try to save lives."
                    p "The lives of kidnappers and mercenaries."
                    k "What can I say? They get shot more often than regular folks."
    else:
        p "Doing okay. You?"
        call ch3katieexplain from _call_ch3katieexplain_1
        p "And?"
        show bg ch3doc4 with dissolve
        k "It doesn't make any sense."
        show bg ch3doc5 with dissolve
        k "I can tell you this, though, whoever hired you, they probably aren't paying you enough."
        p "Well, we can agree on that."
        k "Sorry, I wish I had more."
        p "You tried, that's what counts."


    call ch3katiephone from _call_ch3katiephone
    jump ch3office

label ch3katiephone:
    n "The familiar buzz of your phone goes off."
    p "Sorry, one sec."
    s "Sir, a Meredith White is calling."
    show bg ch3doc28 with dissolve
    p "Damn, Katie, sorry I have to take this. Answer it, Sam."
    show bg ch3doc29 with dissolve
    m "I need a status report, Agent. Come to my office. Now."
    p "*Sighs* I'll be there shortly."
    m "Good, time is of the essence."
    show bg ch3doc30 with dissolve
    if k_score >= 3:
        p "Sorry, Katie, I have to go."
        show bg ch3doc21 with dissolve
        k "Goodbye, [p]."
    else:
        p "Well, Doc, I have to run."
        show bg ch3doc20 with dissolve
        k "I'll see you later, [p]."
    return


label ch3katiewalkaway:

    show bg ch3doc12 with dissolve
    $ renpy.pause(1)
    show bg ch3doc13 with dissolve
    $ renpy.pause(1)
    show bg ch3doc14 with dissolve
    k "Just promise me you won't end up like your friends from the other night."
    p "I won't."
    show bg ch3doc17 with dissolve
    k "I mean it, [p]. Promise me you won't get yourself killed."
    p "Trust me. That's the last thing I want."
    show bg ch3doc19 with dissolve
    k "[p], I said promise."
    p "Doc, I promise."
    show bg ch3doc18 with dissolve
    k "It's Katie..."
    p "I promise you, Katie. I'll come back."
    return

label ch3katieexplain:
    show bg ch3doc2 with dissolve
    k "Not bad, just looking this stuff over..."
    p "And?"
    show bg ch3doc3 with dissolve
    k "Still makes no sense. Nothing could do this."
    k "At least nothing I know of."
    k "Like, look at this."
    show bg ch3doc22 with dissolve
    p "His skull. That much I can gather. Past that I don't know what I'm looking at."
    show bg ch3doc3 with dissolve
    k "I figured when I got it to the lab, I would find something that makes sense."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
