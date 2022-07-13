




label ch4docupstairschoices:
    menu:
        "Try to get some sleep":
            jump ch4docupstairssleep
        "Go check downstairs" if menu3:
            $ menu3 = False
            jump ch4docupstairscheck
        "Approach Katie while she sleeps" if menu4:
            $ menu4 = False
            jump ch4docupstairsapproach


label ch4docupstairscheck:
    p "(Should check on our \"guests,\" see how they are doing.)"

    show bg ch4docupstairs84 with dissolve
    p "(Well, Gus, seeing how you handled the lights, it's the ladder for me.)"
    show bg ch4docs36 with dissolve
    p "(You just sleep tight, Gloria Conner.)"
    if "ch4fightkill" in extraevents:
        h "Checking up on us, Ghost? Scared I took her and ran?"
        p "The thought crossed my mind."
        show bg ch4docs31 with dissolve
        h "Thought about it, but her health is more important. And you haven't called anyone in."
    else:


        h "She hasn't moved much. Still as a mouse. Peaceful."
        h "She's sleeping better than she has since..."
        h "She's doing well."
        show bg ch4docs31 with dissolve
        p "That's good. Hey, can I ask you a question?"
        h "I'm not stopping you."
        p "Why didn't you try to run? She seems stable."
        show bg ch4docs32 with dissolve
        h "Yeah, she does, but I didn't want to risk it."
        h "And, well, if you tried something now... I learned a lot about you in our last fight. Might not go down the same way."
        p "I could have called backup."
        h "You haven't."

    p "How would you know that?"
    show bg ch4docs32 with dissolve
    h "It's a feeling I get, perks of the Augment program."
    p "That's a handy thing to have."
    h "Sure, it sounds nice, until you have a middle-schooler who can't stop talking on the phone. All... the... time."
    p "You had a rough life, Gibson."
    h "Eh, she's worth it."
    show bg ch4docs33 with dissolve
    h "*Grunts in pain*"
    p "Hey-hey you alright?!"
    show bg ch4docs34 with dissolve
    h "*Grunts* I'm fine!"
    if "ch3reportlimter" in extraevents:
        p "Your limiter acting up?"
        h "*Grunts* Would make sense you know about that. Yeah, no point in hiding it."
    else:
        p "That thing on the back of your neck?"
        h "*Grunts* Don't miss a thing, do you? Yeah, no point in hiding it."
    p "Let me grab you something for the pain."
    h "It'll pass."
    show bg ch4docs35 with dissolve
    h "*The muscles in his body relax as his breathing becomes normal*"
    h "*Draws in a deep breath* So, anything else? Or can you let an old man get some sleep?"
    jump ch4dochenrymenu

label ch4dochenrymenu:
    menu:
        "Go to sleep":
            jump ch4docshenrysleep

        "Ask about the device on his neck" if "ch3reportlimiter" not in extraevents and menu1 == True:
            $ menu1 = False
            p "Besides letting you hear comms what does that thing on the back of your neck do?"
            show bg ch4docs32 with dissolve
            h "My limiter? A few things. Most are outdated now..."
            p "Like what?"
            h "H.U.D. display, for instance. That hasn't worked in years. Can also receive tactical maps, but those are useless now."
            if "ch3vicgoodluck" not in extraevents:
                p "I heard you can see Tokyo."
                show bg ch4docs31 with dissolve
                h "Unfortunately... it's a little like living in my own personal hell. I probably deserve it..."
                p "... but you learned to live with it?"
                h "Says a man still living in his?"
                p "Something like that."
            p "What else?"
            show bg ch4docs31 with dissolve
            h "Heh, I can't reveal all my secrets, can I? Just think of it like a traffic light and we'll leave it at that."
            p "I'll keep that in mind."
            h "Anything else?"
            jump ch4dochenrymenu

        "Ask about the limiter" if "ch3reportlimiter" in extraevents and menu1 == True:
            $ menu1 = False
            p "I did some research on your limiter. I know some of the basics. Comm suppression, tactical maps, how it helps you in battle. Anything else?"
            show bg ch4docs32 with dissolve
            h "At this point, it's a crutch. Most of its features are either outdated or stopped working."
            p "Like what?"
            h "You like to pry, don't you? *Sighs* H.U.D. display, that doesn't work anymore. I liked that one."
            p "If you feel it's a hindrance, why not get it removed?"
            show bg ch4docs31 with dissolve
            h "Half the time I wish I could, but it's more than a crutch, it's a reminder. Everyone has forgotten what happened in the war."
            p "We still talk about it all the time."
            h "Bad choice of words. To forget, you would have to know it in the first place. Anyway, the point is moot."
            p "Yeah, but..."
            h "That's enough for tonight, Ghost."
            jump ch4dochenrymenu



        "Ask about Gloria" if menu2 == True:
            $ menu2 = False
            p "So you two are pretty close?"
            show bg ch4docs32 with dissolve
            h "Look, I made a promise to Gloria's father that I would keep her safe. I don't plan to break it."
            p "No offense, but I met him. Alexis Conner doesn't seem like someone you bother keeping a promise to."
            h "He wasn't always that way. He was a decent man before. The fact that he hired me when others would shun us vets showed me the person he was."
            show bg ch4docs31 with dissolve
            p "I believe people are who they are and he was always a prick, he just hadn't had the chance to show it."
            h "Interesting view, what does that say about people like us?"
            p "Nothing good."
            h "The death of his wife might have broken him or maybe you were right. Either way, he put Gloria in my life, I will always owe him for that."
            p "And then he kicked you both to the curb."
            h "He did it when I was on vacation; smart bastard to do it then. I come back, no job, no Gloria. I thought that was it."
            h "I felt like the world was telling me it was time to go. The nightmares..."
            h "No one needed me."
            h "Checking up on Gloria gave me purpose...a reason to keep going, when most of the others just..."
            show bg ch4docs32 with dissolve
            h "A sixteen year-old girl, living on her own, finding a job, finding a place to live. She did it all on her own."
            p "Hell of a girl."
            h "Yeah, I was proud of her. I helped from afar when I was able. I just wanted her to be happy and forget the past. She didn't need me around. And she thought I was dead, anyway."
            p "And what about her powers?"
            show bg ch4docs34 with dissolve
            h "*Grunts* That's what got her kicked out. I don't know how long she had them. She hid them from everyone."
            show bg ch4docs32 with dissolve
            p "You never caught on?"
            h "Eventually, but I never let on I knew. It was basic stuff; saw her move a glass once. But that was the most of it. She always hid her ears, too."
            p "You worried she might become dangerous?"
            h "No."
            show bg ch4docs36 with dissolve
            h "Does she look dangerous to you?"
            p "No, she doesn't, but, as I've been learning, looks can be deceiving."
            h "That incident wasn't her fault... it..."
            p "Incident?"
            h "We're done here, alright?"
            h "Anything else?"
            jump ch4dochenrymenu

label ch4docshenrysleep:
    p "Nah, we're good. You rest. I'd rather you be up when Gloria wakes. A familiar face and all."
    show bg ch4docs31 with dissolve
    h "See you in the morning, Ghost."
    menu:
        "Go back upstairs":
            p "Yeah, see ya."
        "Crack a joke":
            $ h_score += 1
            p "So if I strap a note to a pigeon asking all my buddies to come over, will you know?"
            show bg ch4docs32 with dissolve
            h "*Smirks* Maybe. You want to risk it?"
            p "Morse code it is, then. Now, get some sleep."
    jump ch4docbackup



label ch4docbackup:
    show bg ch4docupstairs85 with dissolve
    p "(Well, Doc, I see how you keep your figure.)"

    show bg ch4docupstairs14 with dissolve
    jump ch4docupstairschoices
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
