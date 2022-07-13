image bg ch5doc1 = "ch5doc1"
image bg ch5doc2 = "ch5doc2"
image bg ch5doc3 = "ch5doc3"
image bg ch5doc4 = "ch5doc4"
image bg ch5doc5 = "ch5doc5"
image bg ch5doc6 = "ch5doc6"
image bg ch5doc7 = "ch5doc7"
image bg ch5doc8 = "ch5doc8"
image bg ch5doc9 = "ch5doc9"



image bg ch5docredo1 = "ch5docredo1"
image bg ch5docredo2 = "ch5docredo2"
image bg ch5docredo3 = "ch5docredo3"
image bg ch5docredo4 = "ch5docredo4"
image bg ch5docredo5 = "ch5docredo5"
image bg ch5docredo6 = "ch5docredo6"
image bg ch5docredo7 = "ch5docredo7"
image bg ch5docredo8 = "ch5docredo8"
image bg ch5docredo9 = "ch5docredo9"
image bg ch5docredo10 = "ch5docredo10"
image bg ch5docredo11 = "ch5docredo11"
image bg ch5docredo12 = "ch5docredo12"
image bg ch5docredo13 = "ch5docredo13"
image bg ch5docredo14 = "ch5docredo14"
image bg ch5docredo15 = "ch5docredo15"
image bg ch5docredo16 = "ch5docredo16"
image bg ch5docredo17 = "ch5docredo17"
image bg ch5docredo18 = "ch5docredo18"
image bg ch5docredo19 = "ch5docredo19"




label ch5doc:










    jump ch5docgo

label ch5driving:
    show bg ch5drive9 with dissolve
    p "Yeah, back to downtown, Sam."
    show bg ch5drive10 with dissolve
    p "Any other chatter trying to get through?"
    s "None, Sir."
    call ch5shanlon from _call_ch5shanlon
    scene black with Dissolve(1)
    show text "{=trans}AN HOUR LATER, AFTER REACHING DOWNTOWN{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    return



label ch5docgo:
    if "ch5downtown" not in extraevents:
        call ch5driving from _call_ch5driving_1
        $ extraevents.append("ch5downtown")
    $ extraevents.append("ch5downtown")
    $ extraevents.append("ch5doc")
    show bg ch5doc1 with dissolve
    p "So, Sam, any advice for what to say to Katie?"
    s "You always tell me to \"Shut it!\". You could try that."
    p "Sam..."
    s "Yes, Sir?"
    p "Shut it."
    show bg ch5doc2 with dissolve
    p "(Knowing Katie, she should still be up.)"
    p "(Certainly not her type of place. Shit, could it be worse?)"
    show bg ch5doc3 with dissolve
    "Prostitute" "Hey there, hun. Need company? Let Diamond give you a good time."
    p "I'm busy."
    show bg ch5doc4 with dissolve
    "Protitute" "One hundred percent organic. You don't know what you're missing."
    if dep >= 3:
        p "Oh yeah?"
        "Prostitute" "I'll suck you off right here and now for thirty. Twenty if it's cash."
        p "Let me think it over."
        "Prostitute" "Don't think too long, sugar. Diamond may not be here when you get back."
    else:

        p "Some other time."
        show bg ch5doc5 with dissolve
        "Prostitute" "Your loss. Now get moving."

    play music audio.calm fadein 2.0 fadeout 2.0
    scene black with Dissolve(1)
    show bg ch5doc6 with Dissolve(1)
    k "Not nearly as bad as I was expecting. Not many places have tubs anymore. With hottish water even."
    "*You rap on the door lightly*"
    show bg ch5doc7 with dissolve
    k "*whisper* Oh crap! Did they track me down?"
    k "..."
    p "I can hear you in there, Katie."
    k "Oh, damn it."
    k "Give me a sec, alright?"
    show bg ch5doc9 with dissolve
    k "Just another minute!"
    show bg ch5docredo11 with dissolve
    if k_score < 4:
        k "*Under her breath* What does he want anyway..."
        p "I heard that."
    k "Okay, coming!"
    scene black with dissolve
    show bg ch5docredo12 with dissolve
    k "[p]? What are you doing here?"
    p "Just checking up on my favorite street doc."
    show bg ch5docredo13 with dissolve
    if not persistent.ch5card2:
        $ renpy.notify(['Possible clue', 'alert'])
        show screen hidden_item("ch5card2", "ch5card2", 1469, 117, 160, 74)
    k "After relocating her to... here."
    p "Yeah. I did want to make sure you were doing okay after everything."
    k "Thanks. So uh... yeah. Come in, check out my new office."
    hide screen hidden_item
    show bg ch5docredo14 with dissolve
    p "Hey, it could be worse... In fact, it's not that bad."
    k "Well, it's not cardboard, so there is that. As for equipment... No net, no holo network. However, we do have a church next door."
    p "A church?"
    show bg ch5docredo2 with dissolve
    k "What else can it be? There are some very loud chants of \"OH GOD!\" coming through the walls."
    if k_score >= 3 and "ch4katie" in extraevents:
        p "Heh, you crack me up sometimes."
        k "It's either that, or if you prefer, we could discuss the effects of compound B4132 on small children."
        p "Compound what? Yeah, no thanks."

    if k_score >= 3:
        p "Heh, so are you holding up alright?"
        k "I guess I'm fine. Just really... really bored."
        p "Sorry."
        show bg ch5docredo1 with dissolve
        k "Nothing to do but sit here, worry about you guys and listen to people \"pray.\""
        k "I'll survive, don't worry. What about Gloria and Henry, are they safe?"
        p "Yeah, Gloria was pretty depressed, but Ellen cheered her right up. It was kind of weird seeing Ellen act all caring for once."
        show bg ch5docredo2 with dissolve
        k "Ellen? Your fixer, right? Are you two close?"
        p "Not as close as she and Gloria are. I get the impression they used to be like family and they kind of still are."
        jump ch5doccontinue
    else:
        p "Heh, so are you doing okay here?"
        show bg ch5docredo2 with dissolve
        k "Physically I'm fine. But I'm restless. Thanks to your dumb butt, I can't exactly see my patients. So I'm sitting here on pause, hoping that the clinic will be fine while I'm gone."
        p "You will be back to that in no time."
        show bg ch5docredo1 with dissolve
        k "Will I?"
        p "..."
        k "Look, [p], I appreciate you coming by to check on me, but I just need some sleep."
        p "Yeah... Of course... I'll check back when I can. Just hold tight."
        k "Bye, [p]..."
        scene black with Dissolve(2)
        show bg ch5docredo18 with dissolve
        $ renpy.pause(1)
        show bg ch5docredo19 with dissolve
        p "Yeah, Sam. Pretty sure she hates me now. Can't say I blame her."
        s "Quite astute, Sir."
        p "Sam?"
        s "Shut it, Sir?"
        p "Shut it."
        jump ch5locationmenu

label ch5doccontinue:

    k "God, I need to sit down..."
    show bg ch5docredo4 with dissolve
    k "Like sisters, close?"
    p "Well, it seems that way. It feels like they could have been if not for what happened with her father."
    if "ch2choosedoc" in extraevents:
        k "The guy is awful, for sure. It's strange; there's a poster of Ellen up in Gloria's old room. Funny that her father kept it up if he hates Ellen so much."
        p "I stopped trying to figure out why assholes do what they do a long time ago."
    show bg ch5docredo3 with dissolve
    k "Look, I appreciate you coming to see me. I do. But after everything... I need some time to think."
    show bg ch5docredo6 with dissolve
    p "Hey, I understand. Maybe tomorrow I can bring you some..."
    menu:
        "Banchan":
            $ extraevents.append("ch5katiebanchan")
            p "Banchan, I probably can't get it at your spot near the clinic, but I'll find something decent, promise."
            show bg ch5docredo5 with dissolve
            k "Heh, I'd like that."
            p "Maybe some candles and a bit of wine?"
            k "You never stop, do you? Even in the middle of all this insanity."
            p "Hey! Place like this, power has to be iffy. Never know?"
            k "*Sighs* Go home, [p]. Before you push your luck a little too far. See you tomorrow."
        "Medical Supplies":

            $ extraevents.append("ch5katiemeds")
            p "Some more meds, I can probably lift some from somewhere. You never know."
            show bg ch5docredo5 with dissolve
            k "Well, I did take some with me. Never leave home without kind of thing, you know?"
            p "Oh-"
            k "Hey, with the mess we are in. I have a feeling I may be needing them. You never know. I am light on pain killers, so anything for that."
            p "Sure, I'll see what I can find."

    p "Okay, I'll let you get some sleep. I'll check back soon."
    if k_score >= 4:
        k "Aren't you forgetting something?"
        menu:
            "Hug Her":
                $ k_score += 1
                show bg ch5docredo9 with dissolve
                p "Sorry, come here."
                show bg ch5docredo10 with dissolve
                k "When you say, you will check back soon. How soon?"
                p "Hopefully tomorrow."
            "Kiss Her":

                $ k_lust += 1
                show bg ch5docredo8 with dissolve
                p "Come here."
                show bg ch5docredo17 with dissolve
                "Her body slides up yours to meet your lips in a soft embrace."
                show bg ch5docredo16 with dissolve
                p "Better?"
                show bg ch5docredo15 with dissolve
                k "Yeah, I needed that."
                p "Same..."
        show bg ch5docredo5 with dissolve
        k "Now, I wasn't lying. I'm probably going to pass out soon, so goodnight, [p]."
    else:
        k "Goodnight, [p]."
    p "Night, Katie."
    scene black with Dissolve(2)
    show bg ch5docredo18 with dissolve
    $ renpy.pause(1)
    show bg ch5docredo19 with dissolve
    s "Where to now, Sir?"
    jump ch5locationmenu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
