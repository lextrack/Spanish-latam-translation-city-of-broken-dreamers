image bg ch4docs1 = "ch4docs1"
image bg ch4docs2 = "ch4docs2"
image bg ch4docs3 = "ch4docs3"
image bg ch4docs4 = "ch4docs4"
image bg ch4docs5 = "ch4docs5"
image bg ch4docs6 = "ch4docs6"
image bg ch4docs7 = "ch4docs7"
image bg ch4docs8 = "ch4docs8"
image bg ch4docs9 = "ch4docs9"
image bg ch4docs10 = "ch4docs10"
image bg ch4docs11 = "ch4docs11"
image bg ch4docs12 = "ch4docs12"
image bg ch4docs13 = "ch4docs13"
image bg ch4docs14 = "ch4docs14"
image bg ch4docs15 = "ch4docs15"
image bg ch4docs16 = "ch4docs16"
image bg ch4docs17 = "ch4docs17"
image bg ch4docs18 = "ch4docs18"
image bg ch4docs19 = "ch4docs19"
image bg ch4docs20 = "ch4docs20"
image bg ch4docs21 = "ch4docs21"
image bg ch4docs22 = "ch4docs22"
image bg ch4docs23 = "ch4docs23"
image bg ch4docs24 = "ch4docs24"
image bg ch4docs25 = "ch4docs25"
image bg ch4docs26 = "ch4docs26"
image bg ch4docs27 = "ch4docs27"
image bg ch4docs28 = "ch4docs28"
image bg ch4docs29 = "ch4docs29"
image bg ch4docs30 = "ch4docs30"
image bg ch4docs31 = "ch4docs31"
image bg ch4docs32 = "ch4docs32"
image bg ch4docs33 = "ch4docs33"
image bg ch4docs34 = "ch4docs34"
image bg ch4docs35 = "ch4docs35"
image bg ch4docs36 = "ch4docs36"

image bg ch4docs37 = "ch4docs37"
image bg ch4docs38 = "ch4docs38"
image bg ch4docs39 = "ch4docs39"
image bg ch4docs40 = "ch4docs40"
image bg ch4docs41 = "ch4docs41"
image bg ch4docs42 = "ch4docs42"
image bg ch4docs43 = "ch4docs43"
image bg ch4docs44 = "ch4docs44"
image bg ch4docs45 = "ch4docs45"
image bg ch4docs46 = "ch4docs46"
image bg ch4docs47 = "ch4docs47"
image bg ch4docs48 = "ch4docs48"

image bg ch4intro:
    "ch4intro"
    yalign 0.5
    zoom 1
    alpha 1.0
    pause 1.0
    easeout 3.0 zoom 1.5 alpha 0.0


image bg chapter4 movie = Movie(play='video/intros/chapter4.webm')


label ch4docsdown:

    scene black with Dissolve(2)

    show bg chapter4 movie with dissolve
    $ renpy.pause(4.0)

    scene black with dissolve

    play music audio.worried fadein 2.0 fadeout 2.0
    show text "{=trans}A SHORT WHILE LATER, BACK AT DR. HAMILTON'S{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)

    show bg ch4docs19 with Dissolve(2)
    p "Doc! DOC! Are you here?!"
    h "Is it getting worse? I think it's getting worse."
    show bg ch4docs20 with dissolve
    k "[p]?! What's going on..."
    h "What's going on is you need to help her! Now!"
    k "Put her on the bed!"
    show bg ch4docs21 with dissolve
    k "Jesus H Christ, [p]. Who is ...?"
    p "Katie, just help her."
    k "Is she on something?"
    show bg ch4docs22 with dissolve
    h "It'll be okay, Gloria, you hear me?"
    g "*Quick heavy breathing*"
    k "Big guy! Is she {i}on{/i} something?"
    h "Gloria, please..."
    show bg ch4docs23 with dissolve
    k "Damn it! Out of the way."
    h "*Grunts.*"
    show bg ch4docs24 with dissolve
    k "Look, buster. You want me to help her, I need you to be straight with me."
    show bg ch4docs25 with dissolve
    h "Just help her!"
    k "Is she on something?"
    show bg ch4docs26 with dissolve
    h "*Takes in a deep breath.* I've had enough of-"
    show bg ch4docs27 with dissolve
    k "Enough of what big guy?! You're freaking out, I get it. But you're not my problem right now...she is."
    k "This is what I do. If I can save her, I will."
    show bg ch4docs28 with dissolve
    k "But only if you tell me what I need to know. Now, sit your giant ass in the corner and {i}let me do my damn job.{/i}"
    show bg ch4docs29 with dissolve
    h "She's not on anything..."
    k "Thank you!"
    h "I uh... I'm sorry..."
    k "That's okay. Now, please, just sit down."
    show bg ch4docs30 with dissolve
    k "*Whispers* Holy cow, he's enormous."
    p "Just try not to think about it."
    k "As for you, either help me or get out of my way."
    menu:
        "Offer Help":
            $ extraevents.append("ch4helpdoc")
            p "Is there anything I can do to help?"
            jump ch4dochelp
        "Sit down":
            p "I'll leave you to it. I'll keep an eye on him."
            jump ch4docsitdown


label ch4dochelp:
    show bg ch4docs37 with dissolve
    k "Yeah, hold her down. She isn't seizing badly, but that can change."
    show bg ch4docs38 with dissolve
    p "Like this?"
    k "That's too hard. Don't restrict her movement. The main thing is, don't let her fall off the table."
    show bg ch4docs39 with dissolve
    k "Better."
    g "*Continues to breathe rapidly*"
    k "Okay good. Now, sweetheart, let's see what's wrong."
    show bg ch4docs40 with dissolve
    p "(Alexis kicked her out for that? That's nothing.)"
    k "Do you know if this happened before?"
    p "How should I know? I don't think he does either."
    p "Shit, has she been living like this since her dad kicked her out?"
    show bg ch4docs41 with dissolve
    if "ch2invitekatie" in extraevents:
        k "That guy from the party, yeah?"
        p "Yeah."
        k "And that big guy is..."
        p "Her bodyguard and..."
        k "The Dad she should have had."
    else:
        k "That guy's not her dad?"
        p "No. Her Dad's a dick."
        k "Huh, well the big guy could have fooled me."
    k "Just a little prick, sweetie. You won't feel a thing."
    show bg ch4docs42 with dissolve
    k "There you go. Just relax."
    g "*Breathing starts to slow down*"
    show bg ch4docs43 with dissolve
    k "Now let's see what's happening with you, sweetheart."
    p "So what are you picking up?"
    show bg ch4docs44 with dissolve
    k "I don't think she's in any immediate danger. The sedative is doing its job. If it's a typical seizure, it should pass."
    k "Wait... what in the name of-?"
    play sound audio.emp
    show bg ch4docs45 with hpunch
    n "*The device shatters*"
    k "Jesus!"
    p "Katie, you okay?! What the fuck just happened?"
    show bg ch4docs46 with dissolve
    k "Her EEG spiked and then... [p], I've never... did she just {i}do{/i} that?"
    g "*Breathing calms to a normal pace*"
    p "After what I witnessed, no doubt."
    show bg ch4docs48 with dissolve
    k "My God. The men in the morgue. Do you think that was her?"
    p "I don't think she meant to do it, but I believe so."
    k "No wonder they have her marked as dangerous."
    p "Yeah..."
    k "Jesus..."
    k "Okay, let us slow down a little here. Her health is my main concern right now and it looks like the seizure has passed."
    show bg ch4docs47 with dissolve
    k "I'll keep the monitors on her, but right now her vitals are pretty normal."
    p "Thanks, Doc."
    k "Don't thank me yet. First, I need to talk to the big guy and then after that, we need to have a little chat upstairs."
    jump ch4dochenry


label ch4docsitdown:
    show bg ch4docs1 with dissolve
    p "She's in good hands. I don't trust many people, but our Doc here will do everything she can."
    show bg ch4docs2 with dissolve
    h "I shouldn't have lost my temper with her."
    p "Doc's seen worse. I'll tell you how we met some time."
    h "..."
    p "Yeah, we're not there yet."
    p "Gloria couldn't be in better hands."
    show bg ch4docs3 with dissolve
    if "ch4fightkill" in extraevents:
        h "If something happens to her..."
        h "You'd better pray you're right."
    else:
        h "I hope you're right. If something happens to her, I don't..."
        h "I don't know what I would do."
    menu:
        "You're in love with her?":
            p "You're in love with her?"
            show bg ch4docs9 with dissolve
            h "We don't know each other, so I'm going to let that pass."
            p "..."
            show bg ch4docs7 with dissolve
            h "She's the only thing left in this world worth a damn."
        "She's important to you":

            $ h_score += 1
            p "She's important to you, more than just a job. That's obvious."
            show bg ch4docs6 with dissolve
            h "She did more for me than I ever did for her. Without her... I'd be dead by now. She saved me."
            show bg ch4docs7 with dissolve
            h "You look like someone who knows what it's like to live with things you wish you could forget, Ghost."
            p "Can't say you're wrong."
            h "The war was hell. And I lived in it every day."
            if "ch3reporthenry" in extraevents:
                p "I know. I read your file."
                show bg ch4docs6 with dissolve
                h "Of course you did. I would have, in your position."
                p "After what happened to the other Ghosts, it was prudent."
                if "ch4fightkill" in extraevents:
                    show bg ch4docs6 with dissolve
                    h "Prudent? That it was."
                if "ch4fightspare" in extraevents:
                    show bg ch4docs7 with dissolve
                    h "First thing that was beaten into my head in special ops training. Never go in unprepared. Leave nothing to luck."
                    p "I think I had a little. Shit man, look at you."
                    h "*Chuckles* We'll leave it at that, then."
            else:
                p "I know some of what you did. I heard you were a hero."
                show bg ch4docs6 with dissolve
                h "That's the story. I never felt like one."
                p "Well, there's a girl over there who I'm sure would disagree with you."
                show bg ch4docs4 with dissolve
                h "Yeah... Gloria still thinks the world can be a good place. Even after everything."
                h "Don't have it in me to prove her wrong."
        "Ignore it.":

            "..."

    show bg ch4docs8 with dissolve
    h "So, why here? The smart move would have been to get some drugs from a vet or something."
    p "I told you. I trust her. And I wasn't going to trust this girl to my medic skills."
    h "You trained as a medic?"
    p "Kind of my point."
    show bg ch4docs9 with dissolve
    h "And when this is done? When she's better, are we throwing down again?"
    p "Not unless you want to."
    h "It's not about want."
    p "She's safe from me, Gibson."
    h "Won't that hurt your rep?"
    p "Fuck my rep."
    h "You know what that means, then."
    p "Meredith should have known better than to..."
    p "Hold that thought. Here she comes."
    jump ch4dochenry

label ch4dochenry:
    show bg ch4docs18 with dissolve
    k "Your friend's going to be alright."
    show bg ch4docs16 with dissolve
    h "Thank you... and I am sorry about how I acted. If I scared you-"
    show bg ch4docs15 with dissolve
    k "Hey on a scale of 1 to 10 you were only a 9.5. I've dealt with scared parents before. I understand."
    show bg ch4docs14 with dissolve

    k "I was expecting to patch you up, not her."
    p "I'll be fine. *grunts* Somehow."
    show bg ch4docs17 with dissolve
    h "He can certainly put up a fight. I'll give him that."
    p "Likewise."
    k "Is this a guy thing? Because last I heard you two were going to kill each other."
    p "Sorry to disappoint. Though, Mr. Gibson may still try to kill me, so that may give you something to do in the near future."
    show bg ch4docs13 with dissolve
    k "Very funny..."
    p "Yeah, we'll be fine. I think."
    k "For now... "
    if k_score >= 3:
        show bg ch4docs12 with dissolve
        k "Just don't scare me like that again."
        p "The last thing I wanted to do was scare you."
    show bg ch4docs10 with dissolve
    k "Now, for the girl, it's Gloria, right?"
    h "Yeah."
    k "I have the clinic's AI running tests on her, but it's going to take all night before I can give you more information."
    h "Thank you. Can I stay down here with Gloria?"
    k "I don't see why not."
    show bg ch4docs11 with dissolve
    k "Now, as for you, we need to talk. Follow me."
    jump ch4docupstairs
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
