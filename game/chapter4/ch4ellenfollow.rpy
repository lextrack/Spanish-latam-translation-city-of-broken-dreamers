image bg ch4ellenfollow1 = "ch4ellenfollow1"
image bg ch4ellenfollow2 = "ch4ellenfollow2"
image bg ch4ellenfollow3 = "ch4ellenfollow3"
image bg ch4ellenfollow4 = "ch4ellenfollow4"
image bg ch4ellenfollow5 = "ch4ellenfollow5"

image bg ch4ellenfollow7 = "ch4ellenfollow7"
image bg ch4ellenfollow8 = "ch4ellenfollow8"
image bg ch4ellenfollow9 = "ch4ellenfollow9"
image bg ch4ellenfollow10 = "ch4ellenfollow10"
image bg ch4ellenfollow11 = "ch4ellenfollow11"
image bg ch4ellenfollow12 = "ch4ellenfollow12"
image bg ch4ellenfollow13 = "ch4ellenfollow13"


label ch4ellenfollow:
    scene black with Dissolve(2)
    show bg ch4ellenfollow1 with Dissolve(2)
    p "Ellen! Will you wait just a second."
    show bg ch4ellenfollow2 with dissolve
    e "*Let's out a long breath* Fucking ghost. I stormed out for a reason."
    p "And I followed you."
    show bg ch4ellenfollow3 with dissolve
    e "Don't you fucking start."
    e "Don't act like it's normal that this sweet little kid I used to know is a fucking fre-"
    p "A what? Say it!"
    show bg ch4ellenfollow4 with hpunch
    e "Fuck you!"
    p "You pissed at me? Or yourself!?"
    show bg ch4ellenfollow5 with dissolve
    e "You! Me! Fucking both of us! Do you know what ANY of these bloodsucking corps would do if they got their hands on her?"
    p "That's why she's here."
    show bg ch4ellenfollow7 with dissolve
    e "I picked you. I thought it would be for her own good. That they would want to help her. Fuck, I'm stupid."
    p "They would have known you were linked to her and to me."
    show bg ch4ellenfollow8 with dissolve
    e "And that I'd send you on this one. That fucking bitch played me!"
    p "Who?"
    show bg ch4ellenfollow9 with dissolve
    e "I should have known something was weird when she started showing up to my shows off hours."
    e "No fucking contact is that friendly. But her jobs always panned out. And she seemed pretty cool."
    show bg ch4ellenfollow10 with dissolve
    e "The fuck was wrong with me? I am gonna kill that cow-titted bitch!"
    menu:
        "Ask her if she means Victoria":
            $ e_score += 1
            $ extraevents.append("ch4ellenknowvic")
            p "Victoria Shields? Redhead, body out of a pornscape?"
            show bg ch4ellenfollow11 with dissolve
            e "You know her? Shit. She played this perfectly."
            p "Not quite. I don't think she planned on this."
            if "ch2choosevic" in extraevents:
                p "She was helping me with the case. Helped me get into Alexis' penthouse."
                e "Well, then, you know..."
            else:
                p "Yeah, Meredith White introduced me. Seems she is running the op."
                e "Operate, my ass. She is all over this, [p]."
            show bg ch4ellenfollow12 with dissolve
            e "That bitch is good. I can't explain it. She tells someone to do something and they just {i}want{/i} to do it."
            if "ch1spellbound" in extraevents:
                p "I know..."
            else:
                p "They want to... But they don't have to."
        "Play dumb":
            p "Cow-titted?"
            e "Victoria Shields, right hand to some high-end uppity bitch or other, I think. She's good, too..."
            show bg ch4ellenfollow12 with dissolve
            e "She asks you to do something and you just want to do it. Hard to explain."

    p "Know anything else about her?"
    show bg ch4ellenfollow13 with dissolve
    e "Like what?"
    $ resetmenu()
    jump ch4ellenmenu


label ch4ellenmenu:
    menu:
        "What does she like?" if menu1:
            $ extraevents.append("ch4viclikes")
            $ menu1 = False
            p "What does she like?"
            e "\"What does she like?\" Can you sound more like a high school boy trying to hook up with her? You're not quite there yet."
            p "Just answer the question, Ellen."
            show bg ch4ellenfollow11 with dissolve
            e "I don't fucking know! Music, I guess. She knows a lot. Not just popular shit. She was talking about my influences and knew shit even old school fans of mine didn't."
            if "ch2vic" in extraevents:
                p "(I can attest to that.)"
            p "Anything else?"
            e "What else? Not like we were best buds."
            p "What about..."
            jump ch4ellenmenu

        "Does she have any friends?" if menu2:
            $ extraevents.append("ch4vicfriends")
            $ menu2 = False
            p "Does she have any friends? Someone we can press to learn more?"
            show bg ch4ellenfollow12 with dissolve
            e "Doubt it. Hell, I was probably the closest thing to it."
            p "Why do you say that?"
            e "Most people I saw her talk to, they were all business or just waiting to fuck her. I mean, she is pretty fucking hot."
            if "ch3vicnothanks" in extraevents:
                p "(I can see why people would think that.)"
            else:
                p "(Not wrong there.)"
            show bg ch4ellenfollow9 with dissolve
            e "Hell, even I thought about hooking up with her without a cock in the picture."
            p "Seriously?"
            e "I was pretty drunk that night."
            p "She live alone?"
            e "Pretty sure. She never mentioned a boyfriend or girlfriend either. Or any friends at all."
            p "Okay, what else?"
            jump ch4ellenmenu


        "Know anything of her past?" if menu3:
            $ extraevents.append("ch4vicpast")
            $ menu3 = False
            p "What about her past? Family, where she grew up?"
            e "Nope. Actually, wait. I got her to drink with me after a show once. Tried to get her plastered, just to see."
            p "What did she say?"
            show bg ch4ellenfollow12 with dissolve
            e "Not much. She fucking outdrank me."
            p "Impressive, but not that helpful."
            show bg ch4ellenfollow11 with dissolve
            e "Fuck you too. I was getting to the good part. I remember her saying she had a lot of parents. She was adopted or some shit."
            p "Foster parents?"
            show bg ch4ellenfollow13 with dissolve
            e "Yeah."
            p "That can be a rough life."
            show bg ch4ellenfollow9 with dissolve
            e "Yeah, but she didn't seem angry about it. She mentioned getting adopted by a couple, seemed happy... then really sad."
            p "Sounds tragic. Maybe they died when she was growing up?"
            e "As I said, the night was blurry, but no, not dead. Pretty sure."
            p "That's... almost helpful."
            e "Next time you down a fifth of Cuervo we'll talk. See how well you remember."
            p "Anyway..."
            jump ch4ellenmenu
        "Move on":


            jump ch4ellenfollowend

label ch4ellenfollowend:
    p "Alright, forget Victoria. We've got more important things to deal with right now."
    show bg ch4ellenfollow7 with dissolve
    e "Fuck... Gloria... that was a prime bitch move running off like that."
    p "Hey, Ellen, I get it."
    show bg ch4ellenfollow8 with dissolve
    e "You get being fucking awful to people who don't deserve it?"
    p "Ask Sonja about that."
    show bg ch4ellenfollow9 with dissolve
    if "ch1ellen" in extraevents:
        e "Hard Pass."
    else:
        e "Who's that?"
        p "Long story."
    p "You just got scared, seeing that. It's understandable. And no matter how shitty you feel, Gloria feels worse."
    p "I can't do much for how you feel right now, but you can do a lot for her."
    e "You've turned into a pussy, [p]. Shit... I did too."
    e "[p], we almost got this girl fucked over, didn't we?"
    p "Almost. Now, get back in there, please."
    e "I'd tell you to fuck off, but right now I should be saying that to myself. I have an idea. Shall we?"
    p "Thanks, Ellen."
    scene black with Dissolve(1)
    jump ch4ellenshowreturn
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
