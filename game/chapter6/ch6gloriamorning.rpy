
image bg ch6gloriamorning1 = "ch6gloriamorning1"
image bg ch6gloriamorning2 = "ch6gloriamorning2"
image bg ch6gloriamorning3 = "ch6gloriamorning3"
image bg ch6gloriamorning4 = "ch6gloriamorning4"
image bg ch6gloriamorning5 = "ch6gloriamorning5"
image bg ch6gloriamorning6 = "ch6gloriamorning6"
image bg ch6gloriamorning7 = "ch6gloriamorning7"
image bg ch6gloriamorning8 = "ch6gloriamorning8"
image bg ch6gloriamorning9 = "ch6gloriamorning9"
image bg ch6gloriamorning10 = "ch6gloriamorning10"
image bg ch6gloriamorning11 = "ch6gloriamorning11"
image bg ch6gloriamorning12 = "ch6gloriamorning12"
image bg ch6gloriamorning13 = "ch6gloriamorning13"
image bg ch6gloriamorning14 = "ch6gloriamorning14"
image bg ch6gloriamorning15 = "ch6gloriamorning15"
image bg ch6gloriamorning16 = "ch6gloriamorning16"
image bg ch6gloriamorning17 = "ch6gloriamorning17"
image bg ch6gloriamorning18 = "ch6gloriamorning18"
image bg ch6gloriamorning19 = "ch6gloriamorning19"
image bg ch6gloriamorning20 = "ch6gloriamorning20"
image bg ch6gloriamorning21 = "ch6gloriamorning21"
image bg ch6gloriamorning22 = "ch6gloriamorning22"
image bg ch6gloriamorning23 = "ch6gloriamorning23"


label ch6gloriamorning:
    scene black with Dissolve(2)
    g "I wouldn't look in there!"
    show bg ch6gloriamorning1 with dissolve
    k "It can't be that-"
    show bg ch6gloriamorning2 with dissolve
    k "Bad... How about a different locker..."
    show bg ch6gloriamorning3 with dissolve
    g "Heh, Yeah... I saw that earlier."
    show bg ch6gloriamorning4 with dissolve
    k "I guess finding proper clothing in a brothel isn't in the cards."
    k "What I'd do for some nice sweatpants."
    g "You and me, both."
    k "This should do... I guess."
    show bg ch6gloriamorning5 with dissolve
    g "It's a little short... And a little see-through..."
    k "We don't have the luxury, sadly."
    show bg ch6gloriamorning6 with dissolve
    g "Well, they fit..."
    k "Hey, it's better than nothing."
    show bg ch6gloriamorning7 with dissolve
    g "Katie... I turned your life upside down. You didn't deserve this."
    k "Don't worry about me... Here, put this on."
    show bg ch6gloriamorning8 with dissolve
    g "But, I mean it. You're too nice. I feel-"
    show bg ch6gloriamorning9 with dissolve
    k "Hey, look at me."
    show bg ch6gloriamorning10 with dissolve
    k "You guys needed help. It's why I'm here. I could have made you guys leave after I stabilized you back at the clinic, but I didn't."
    g "But..."
    k "Hey, listen kiddo, this is what I do. Plus, with what you can do, I'm honored to help you through it."
    k "Here, sit and relax, we haven't had a chance to chat."
    show bg ch6gloriamorning12 with dissolve
    k "There, you look much more proper now."
    show bg ch6gloriamorning11 with dissolve
    g "Thanks... In what you found to wear though, you look like you belong on a giant billboard... Shit, sorry... I didn't mean-"
    k "Wait, are you in my head, again?"
    show bg ch6gloriamorning12 with dissolve
    g "No, I don't think so. It's just... You're pretty."
    k "Well, thank you, but I'd rather not walk around like this all day."
    show bg ch6gloriamorning13 with dissolve
    k "I found this... Should work well enough."
    g "Heh, everything is see-through here."
    k "No kidding."
    show bg ch6gloriamorning14 with dissolve
    k "Well, how do I look?"
    show bg ch6gloriamorning21 with dissolve
    if "ch5ellendoc" in extraevents:
        g "[p] will really like that."
        k "Excuse me?"
        show bg ch6gloriamorning17 with dissolve
        g "Ahh, I shouldn't have said anything."
        k "No, what is it?"
        g "Umm... Hard to explain, but he kinda likes you."
        k "I've been hurt before, Gloria. They say that-"
        show bg ch6gloriamorning21 with dissolve
        g "He didn't say it. I just know. He's in love with you..."
        show bg ch6gloriamorning18 with dissolve
        k "[p]!? You can't just assume things like that."
        g "Sorry, but it's true."
        k "As if things couldn't get more complicated."
        show bg ch6gloriamorning15 with dissolve
        g "But it's good complicated."
        show bg ch6gloriamorning19 with dissolve
        k "As much as I want to talk about this, we should probably discuss you."
    elif k_score>=3:
        g "[p] will really like that."
        k "Excuse me?"
        show bg ch6gloriamorning17 with dissolve
        g "Ahh, I shouldn't have said anything."
        k "No, what is it?"
        g "Umm... look, I know you really like him."
        k "What? I---"
        g "I'm pretty sure he likes you too."
        show bg ch6gloriamorning21 with dissolve
        k "Did he say something?"
        g "He didn't say it. I just know. Like I know with you."
        show bg ch6gloriamorning18 with dissolve
        k "[p]? Come on, now."
        g "Sorry, but it's true."
        k "As if things couldn't get more complicated."
        show bg ch6gloriamorning15 with dissolve
        g "But it's good complicated. Isn't it?"
        show bg ch6gloriamorning19 with dissolve
        k "As much as I want to talk about this, we should probably discuss you."
    else:
        g "Perfecto! It's really cute."
        k "You think?"
        g "Yep!"
        show bg ch6gloriamorning19 with dissolve
        k "Great, so now we should talk about you a bit."

    show bg ch6gloriamorning16 with dissolve
    g "How so?"
    k "Well, how are you holding up? These last few days are something nobody should have to go through."
    g "Not great, if that's what you're asking... Really, I'd rather not talk about how I'm feeling."
    show bg ch6gloriamorning19 with dissolve
    k "I'm sorry, Gloria. I heard about your friend."
    show bg ch6gloriamorning16 with dissolve
    g "Friends. My roommates are dead too. And I'm wanted for their murder."
    g "You want to know how I feel? It's like all the people I care about are dying. And it's my fault."
    show bg ch6gloriamorning19 with dissolve
    k "Gloria... I..."
    show bg ch6gloriamorning16 with dissolve
    g "It's okay, I know you're trying to help, but can we talk about something else?"
    k "Well, when you're ready, let me know."
    g "Thank you, Katie."
    show bg ch6gloriamorning19 with dissolve
    k "So then, how about we discuss your abilities?"
    k "Would that be okay?"
    show bg ch6gloriamorning17 with dissolve
    g "Yeah, that's fine, I guess. Like my psychic stuff?"
    k "We can start there, can you actually..."
    g "Read minds? No. I just get feelings. I can sense stuff."
    show bg ch6gloriamorning18 with dissolve
    k "Like how you knew my name?"
    g "Yeah. Like that, but other stuff too. I can sense strong emotions from people."
    k "How does that work?"
    show bg ch6gloriamorning14 with dissolve
    g "Usually, I just get a quick tingle, something that lets me know what's up."
    g "But sometimes, when people get really angry, it's like it washes over me; it puts me on edge."
    g "It's hard to explain. But it's not just anger."
    k "Good moods, too?"
    g "Yeah, it can be infectious, but in a good way."
    show bg ch6gloriamorning17 with dissolve
    g "Or sometimes, when my roommates got a little... you know... that would affect me."
    k "Ha, no need to dive deep there."
    g "That was usually my cue to go take a walk. It could get slightly uncomfortable."
    k "I bet."
    show bg ch6gloriamorning18 with dissolve
    k "What about your other powers, like the telekinesis?"
    g "What about them?"
    k "How long has that been happening?"
    g "I first noticed it like two years ago..."
    k "Okay, and that's what causes you to pass out?"
    show bg ch6gloriamorning15 with dissolve
    g "I didn't use to pass out, not that I can remember."
    k "When did it start?"
    g "Maybe a few months ago, but lately it's been getting worse."
    k "And when you use your power, does it always happen or only sometimes?"
    show bg ch6gloriamorning17 with dissolve
    g "Small things are fine. At least, usually. Like moving things around and stuff like that."
    g "Might get a little lightheaded or something."
    k "What about big things like you did to stop [p] and Henry from fighting each other?"
    g "Almost all the time..."
    show bg ch6gloriamorning19 with dissolve
    k "Almost? So sometimes you don't blackout? Can you tell me when?"
    show bg ch6gloriamorning16 with dissolve
    g "Well, the first time was with... Tommy, a boy I liked... I got scared and ended up hurting him very badly."
    k "What scared you?"
    g "It was going to be... my {i}first{/i} time... and I freaked out."
    k "Oh... that would do it. Any other time?"
    if "ch6venusbroken" in extraevents:
        g "That Venus thing. She was, feeling up on me and acting weird. I kinda threw her across the room."
        k "And you were fine after?"
        g "Yeah..."
        k "Okay, anything else?"
    if "ch5glorialittlemad" in extraevents or "ch5gloriamad" in extraevents:
        show bg ch6gloriamorning15 with dissolve
        g "Nope."
        show bg ch6gloriamorning19 with dissolve
        k "I may not have telekinetic superpowers, but I can tell you're not being honest with me."
        g "Sorry, it's just, you may get mad."
        k "Gloria, I need to get the full picture here."
        show bg ch6gloriamorning16 with dissolve
        if "ch5gloriaalittlemad" in extraevents:
            g "Before I say anything. Just know he wasn't quite himself."
            k "This is [p] we are talking about, isn't it?"
            g "Yeah, the other morning we shared a strange experience. A dream, something from my past and we were discussing it after."
            k "Go on..."
            g "He was comforting me, when, well... His hand wandered a bit too far down from where it should have been."
            g "I panicked and threw him across the room."
            if k_score >= 5:
                show bg ch6gloriamorning20 with dissolve
                $ k_score -= 2
                k "God, I'm such an idiot..."
                k "It seems like being sweet was just an act."
                show bg ch6gloriamorning16 with dissolve
                g "It's not his fault! The dream and being around me was just messing with his head. It was some subconscious thing."
                k "I'm sure it was..."
                g "I knew I shouldn't have said anything."
            else:
                show bg ch6gloriamorning20 with dissolve
                $ k_score -= 1
                k "Why am I not surprised."
                show bg ch6gloriamorning16 with dissolve
                k "The dream was just messing with his head. It was some subconscious thing."
                k "I'm sure it was..."
                g "Sorry..."
        else:
            g "So, before, I had a friend that was comforting me, but then his hand wandered a bit too far down."
            g "That's when I panicked and flung him across the room."
            p "Who was this friend?"
            g "Just a friend, it happened like a week ago."
            k "Okay..."

    p "Hey girls, I'm not interrupting am I?"
    show bg ch6gloriamorning22 with dissolve
    g "No, I think we're done."
    p "Great, Katie, can I speak to you for a sec?"
    if "ch5glorialittlemad" in extraevents:
        show bg ch6gloriamorning23 with dissolve
        k "Yeah, I think maybe we should."
        p "That doesn't sound good."


    jump ch6docmorning
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
