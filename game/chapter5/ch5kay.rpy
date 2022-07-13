
image bg ch5kay1 = "ch5kay1"
image bg ch5kay2 = "ch5kay2"
image bg ch5kay3 = "ch5kay3"
image bg ch5kay4 = "ch5kay4"
image bg ch5kay5 = "ch5kay5"
image bg ch5kay6 = "ch5kay6"
image bg ch5kay7 = "ch5kay7"
image bg ch5kay8 = "ch5kay8"
image bg ch5kay9 = "ch5kay9"
image bg ch5kay10 = "ch5kay10"
image bg ch5kay11 = "ch5kay11"
image bg ch5kay12 = "ch5kay12"
image bg ch5kay13 = "ch5kay13"
image bg ch5kay14 = "ch5kay14"
image bg ch5kay15 = "ch5kay15"
image bg ch5kay16 = "ch5kay16"
image bg ch5kay17 = "ch5kay17"
image bg ch5kay18 = "ch5kay18"
image bg ch5kay19 = "ch5kay19"
image bg ch5kay20 = "ch5kay20"
image bg ch5kay21 = "ch5kay21"
image bg ch5kay22 = "ch5kay22"
image bg ch5kay23 = "ch5kay23"
image bg ch5kay24 = "ch5kay24"


image ch5kayanim = Movie(play='video/chapter-5-video/ch5kayanim.webm', loop=False)
image bg ch5kayanimmovie movie:
    "ch5kayanim"
    pause 6.0
    "ch5kayanimend"


label ch5kay:
    play music audio.worried fadein 2.0 fadeout 2.0
    scene black with Dissolve(2)
    show bg ch5kay1 with Dissolve(2)
    p "Is this the right address, Sam?"
    s "It appears so, Sir."
    show bg ch5kay2 with dissolve
    p "Heh, serves them right. I'll be back in a bit."
    show bg ch5kay3 with Dissolve(2)
    p "Hello?"
    p "..."
    show bg ch5kay4 with dissolve
    p " It's been a long night, so come out if you're coming. If it's a trap, spring it."
    show bg ch5kay5 with dissolve
    "Unknown Female" "Hey there. Take the mask off."
    p "When you get that light out of my face."
    "Unknown Female" "Mask first. I'm not going to shoot you."
    p "Fine. Sonja hasn't sniped me yet, so I figure this is clear."
    show bg ch5kay6 with dissolve
    "Unknown Female" "Were you followed?"
    p "No. Give me some credit, at least."
    "Unknown Female" "Alright."
    if "ch1futapartial" in extraevents or "ch1futafull" in extraevents:
        p "Wait, what the fuck?"
        show bg ch5kay7 with dissolve
        klx "You gotta be kidding me."
        "Both of you" "Sonja, you bitch!"
        p "So umm..."
        show bg ch5kay9 with dissolve
        klx "Yeah... Awkward."
        p "I thought that was Sam..."
        klx "I thought it was odd when you were surprised."
        if "ch1futafull" in extraevents:
            p "Hey, I had fun. You had fun. Nobody got hurt."
        else:
            p "I didn't want to be rude, but that was a tad shocking to me."
            show bg ch5kay10 with dissolve
            klx "You're not the first..."
            p "Maybe you should be a bit more upfront next time."
            klx "It's why I go opt-in, less... problems that way. Still, The look on your face was worth it."
            p "..."
        p "Wait, if you're Sonja's partner, how didn't you know about me?"
        show bg ch5kay11 with dissolve
        klx "Of course, I know about you, I know everything about you."
        p "And you didn't recognize me before?"
        klx "I said I knew about you, but faces... that's not important."
        p "What?"
        klx "I'm in a hurry and I'm feeling naked out here, so let's get to business."
    else:
        "Unknown Female" "Can never be too careful."
        p "So, you're Kay, huh?"
        show bg ch5kay8 with dissolve
        klx "Sonja calls me that for short. The name is Kleo. Kleo Love Xavier."
    klx "So, you got your mark, but you didn't bring her in. Why?"
    p "Just skipping the foreplay."
    klx "As I said, a hurry."
    p "And if I don't want to tell you?"
    show bg ch5kay10 with dissolve
    klx "Then I'll figure it out anyway. I just wanted to speed things up."
    p "Knock yourself out."
    show bg ch5kay12 with dissolve
    klx "Okie-dokes. First, this job doesn't follow your typical *Grunts* pattern. You go for sure things, real scumbags, not grey calls."
    show bg ch5kay13 with dissolve
    klx "But you took this one. Why? She's not a friend, no link between you."
    klx "Your fixer is a different story. Ellen Lane, a regular client, she knows the girl and she convinced you."
    p "Not bad. But nothing Sonja wouldn't already know."
    klx "And not the interesting part. See, what has me confused is our dead but not dead friend, Henry Gibson."
    show bg ch5kay14 with dissolve
    klx "Thing is, after the meeting, you're both alive, weird enough, but possible. But now, you're working together, why is that?"
    p "You tell me."
    show bg ch5kay15 with dissolve
    klx "You're both ex-military, but so are 87.6%% of active ghosts. You never served together, that much is clear."
    klx "Your contract with Baynard is still active."
    klx "So it's not about money. And nothing else links you. So..."
    klx "..."
    show bg ch5kay16 with dissolve
    klx "It's the girl! That's all that's left. But again, why?"
    menu:
        "Brush her off":
            p "Keep guessing. Not everything is on the net. That's why you're stumped."
        "Tell her":
            $ extraevents.append("ch5tellkay")
            p "You're getting warm. It is about the girl."
            klx "I knew it! It's not a sex thing, right? Because that would be boring."
            p "Uh no."
            klx "Good, because you've done better."
            p "How much have you read on me?"
    show bg ch5kay17 with dissolve
    klx "I'm almost there, now to bring it home. Everything about everyone is online. I just need to find it."
    klx "I know my marks better than they know themselves. It's exhilarating!"
    p "And creepy."
    show bg ch5kay18 with dissolve
    klx "Potato, potahto."
    p "Surprised Sonja isn't here yet. Not like her to be this late."
    show bg ch5kayanimmovie movie with dissolve


    klx "About that..."
    p "This wasn't her idea?"
    klx "Not as such."
    p "Then, why?"
    show bg ch5kay22 with dissolve
    klx "She wants to know what's going on, but she can't ask. So I took the initiative."
    if "ch5tellkay" in extraevents:
        p "Look, I know Sonja wants answers. Tell her this. Caracas."
        klx "What? What does that mean?"
        p "It looks like you don't know everything, after all."
        show bg ch5kay21 with dissolve
        klx "I know I have something new to explore. Kind of makes me hard."
        p "Yeah, you're going back to creepy."
        klx "So you know, Tex is watching your wife like a hawk."
    else:
        p "Tell Sonja to keep her distance. She doesn't want to get involved in this."
        klx "Sorry, spook. She's already involved. She gave you the night and almost got reamed for it. Tex saw that a mile away."

    p "Fuck me, is Tex on this too?"
    show bg ch5kay19 with dissolve
    klx "Everyone is. No open Ghosts in the city right now."
    p "Baynard moved fast."
    klx "More Vostok and at least two other major corps contracted them all."
    show bg ch5kay20 with dissolve
    "Kay's eyes glaze for a second as she gets a message"
    klx "That's the boss, gotta run. Go out the way you came. I'll go out the back -- all spy-like."
    show bg ch5kay23 with dissolve
    klx "Now, if you don't mind, I gotta get back and start tracking your ass again. Don't worry, this is off the books."
    p "Seriously, why are you doing this?"
    show bg ch5kay24 with dissolve
    klx "I told you, I know what you normies will do before you do. I know the outcome if you and Sonja keep on this."
    p "So which one of us wins?"
    klx "Nobody, that's the problem."
    scene black with Dissolve(2)
    show ch5kay1 with Dissolve(2)
    s "Was she nice, Sir?"
    if "ch1futapartial" in extraevents or "ch1futafull" in extraevents:
        p "\"She\" was odd, Sam."
    else:
        p "Odd, Sam."
    s "Most in that profession tend to be. Anything useful?"
    p "If she is telling the truth, Sonja did try to buy me some time. But she'll be coming regardless."
    p "She takes our old code far too seriously, even when others ignore it."
    s "Do you admire that?"
    menu:
        "Yes":
            $ extraevents.append("ch5sonjaadmire")
            p "In a way, I do. You always know where she stands."
            p "Duty is important to her. Hell, it probably keeps her sane."
        "No":
            p "It's silly, Sam. Long gone code only a few of us follow."
            p "She lets her stubbornness control her."
    p "Fuck it, let's get out of here."
    jump ch5locationmenu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
