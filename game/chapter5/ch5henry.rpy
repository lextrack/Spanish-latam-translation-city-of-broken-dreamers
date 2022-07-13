
image bg ch5tunnel1 = "ch5tunnel1"
image bg ch5tunnel2 = "ch5tunnel2"
image bg ch5tunnel3 = "ch5tunnel3"
image bg ch5tunnel4 = "ch5tunnel4"
image bg ch5tunnel5 = "ch5tunnel5"
image bg ch5tunnel6 = "ch5tunnel6"
image bg ch5tunnel7 = "ch5tunnel7"
image bg ch5tunnel8 = "ch5tunnel8"
image bg ch5tunnel9 = "ch5tunnel9"
image bg ch5tunnel10 = "ch5tunnel10"
image bg ch5tunnel11 = "ch5tunnel11"

label ch5henry:
    play music audio.prepare fadein 2.0 fadeout 2.0
    scene black with Dissolve(1)
    show bg ch5tunnel11 with dissolve
    p "(Alright lets see what the big guy is up to.)"
    p "(And hopefully he didn't go from EMP's to frags.)"
    show bg ch5tunnel1 with dissolve
    p "There you are. I was looking all over for you."
    show bg ch5tunnel2 with dissolve
    h "I figured the girls could use some time alone. Don't need me looming over everything."
    h "Just nice to see her happy again."
    p "Relatively, I suppose."
    show bg ch5tunnel3 with dissolve
    h "So what brings you down here, Ghost?"
    p "Just checking up on you."
    show bg ch5tunnel4 with dissolve
    if h_score >= 2:
        h "I'm doing alright. Just trying to lay down a defense."
        p "Any luck?"
        h "Not much... Three ways in. Decent amount of traffic, especially here in the tram tunnels. Hard to keep a proper eye."
        show bg ch5tunnel6 with dissolve
        h "Sorry if I came off harsh last night..."
        p "Don't worry about it."
        h "Well, did you learn anything?"
        if "ch4vicgoodbye" in extraevents or "ch4vicsex" in extraevents:
            p "No... But."
            show bg ch5tunnel9 with dissolve
            h "But what?"
            menu:
                "Tell him of Victoria":
                    $ h_score += 1
                    p "Met an agent from Baynard. Yes, that Baynard."
                    show bg ch5tunnel7 with dissolve
                    h "Are you crazy?! What if they tracked you back here?!"
                    show bg ch5tunnel8 with dissolve
                    p "This is what I do. I'm not some amateur. Keep your cool."
                    p "I think she can help us."
                    show bg ch5tunnel7 with dissolve
                    h "She? Well she is one of them. How can you trust her?"
                    p "I can't. But she's in the dark on this. I think if she found out why, she may become an asset rather than a liability."
                    show bg ch5tunnel9 with dissolve
                    h "Sounds like a stretch, I hope you know what you're doing."
                    p "Heh, so do I."
                    if "ch5gloriamad" in extraevents:
                        p "Look, I'm gonna head back up and see how those two are doing."
                    else:
                        p "Look, we grabbed some food, head up when you get hungry."
                        h "Thanks. Just give me a bit."
                    show bg ch5tunnel10 with dissolve
                    h "Just remember, Ghost, most people in this world are wolves. Don't trust them."
                    p "Hey, it's why I got you. Wolves are scared of bears, aren't they?"
                    h "For their sake, I hope so."
                    jump ch5battle
                "Nothing":

                    p "Ahh, it's nothing."
                    show bg ch5tunnel7 with dissolve
                    h "Look, we are working together, right?"
                    p "Kinda have to."
                    h "Then be honest with me. Spill it."
                    show bg ch5tunnel8 with dissolve
                    p "Look, my private affairs are not yours."
                    h "They are if they can come back to hurt us."
                    if "ch5gloriamad" in extraevents:
                        p "It won't come to that. I know what I'm doing. Now if you excuse me, I'll let you do whatever it is you're doing down here."
                    else:
                        p "It won't come to that. I know what I'm doing. We grabbed some food earlier. Head up when you get hungry."
                        h "Yeah, thanks. Give me a bit."
                    show bg ch5tunnel10 with dissolve
                    h "Just remember, Ghost, most people in this world are wolves. Don't trust them."
                    p "Hey, it's why I got you. Wolves are scared of bears, aren't they?"
                    h "For their sake, I hope so."
                    jump ch5battle
        else:
            call ch5tunnelnothing from _call_ch5tunnelnothing
            jump ch5battle
    else:
        h "I'm more curious what you did last night."
        p "I told you. I had to figure things out with a \"friend.\""
        show ch5tunnel5 with dissolve
        h "A friend, huh? How do I know this friend isn't on their way right now?"
        show ch5tunnel8 with dissolve
        p "It's not how it works."
        h "Then enlighten me. You vanish last night after we get situated. We should be laying low."
        menu:
            "That won't work":
                $ h_score += 1
                p "You know they won't stop on their own. We need to make them stop. Laying low just buys us time for the inevitable."
                show bg ch5tunnel7 with dissolve
                h "So, you decided to be reckless and put us all in jeopardy?"
                p "No. I thought maybe she could be useful to us."
                h "She? And how will she be useful?"
                show bg ch5tunnel9 with dissolve
                p "I hope... She can get us information from Baynard; see what they are planning."
                h "And how will she do that."
                p "That I'll keep close to my chest."
                call ch5tunnelnothing from _call_ch5tunnelnothing_2
                jump ch5battle
            "Maybe you're right":


                p "Maybe, you're right. But, I had to risk it."
                show bg ch5tunnel7 with dissolve
                h "It was a mistake. You never should have left. Whatever it was, I doubt it was worth the risk."
                p "I was just trying to help."
                h "Then help around here."
                show bg ch5tunnel10 with dissolve
                h "Go back and check on the girls. I'll be up soon. We can talk more."
                p "Sure..."
                call ch5tunnelnothing from _call_ch5tunnelnothing_3
                jump ch5battle


            "I didn't find anything anyway" if "ch4vicaccept" in extraevents:
                $ extraevents.append("ch5henrysaynothing")
                p "It didn't work out anyway."
                h "What, you didn't find out anything?"
                call ch5tunnelnothing from _call_ch5tunnelnothing_1
                jump ch5battle



label ch5tunnelnothing:
    p "Nothing... It was a dead end."
    show bg ch5tunnel7 with dissolve
    h "So, what do we do now."
    p "We wait. Come up with a plan. You keep figuring out how to secure this place."
    show bg ch5tunnel9 with dissolve
    h "And you?"
    p "I gotta see what friends I have left or someone I can lean on. Past that, our options are limited."
    h "Hmmm..."
    p "Look, I'm out of here. Keep doing what you're doing. I'll be upstairs."
    show bg ch5tunnel10 with dissolve
    h "You know I still have my eye on you."
    p "I know..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
