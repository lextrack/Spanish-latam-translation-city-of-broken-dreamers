
image ch4docsidepanmovie = Movie(play='video/chapter-4-video/ch4docsidepan.webm', loop=False)
image bg ch4docsidepan movie:
    "ch4docsidepanmovie"
    pause 10.0
    "ch4docsidepanend"

image bg ch4doctits movie = Movie(play="video/chapter-4-video/ch4doctits.webm")
image bg ch4docnips movie = Movie(play="video/chapter-4-video/ch4docnipsuck.webm")


label ch4docupstairssleep:
    show bg ch4docupstairs15 with dissolve
    p "([p], you're in the shit now. What the fuck am I even doing? Sonja's going to kill me. Maybe literally this time.)"
    p "*Yawns*"
    p "(Well, I made my choice. Now I have to live with it.)"
    scene black with Dissolve(2)
    n "A sharp pain rips through your back, waking you up"
    p "*Grunts*"
    show bg ch4docupstairs14 with Dissolve(2)
    p "(Shit, Henry did a number on me...)"
    n "You shift around and let out a groan as your back throbs"
    show bg ch4docupstairs16 with vpunch
    k "[p]! What's wrong?"
    p "Didn't mean to wake you, Doc."
    k "Well, I'm up, so what is it?"
    menu:
        "It's just a little back pain":
            p "Just a little sore from the fight, I'll be fine."
            k "Are you sure?"
            p "Positive. Just get some sleep, Katie."
            k "Ok, I'm here if you need me."
            show bg ch4docupstairs76 with dissolve
            n "Katie lies back down and is asleep in a second. You soon fall asleep yourself."
            scene black with Dissolve(2)
            jump ch4vicmer
        "Tease Katie and play up the pain":

            jump ch4wakeup


label ch4wakeup:
    p "ARRGH! Damn, my back!"
    show bg ch4docupstairs17 with dissolve
    k "I'm here. You need to tell me where it hurts."
    show bg ch4docupstairs18 with dissolve
    k "Christ, I should have taken a closer look at you."
    show bg ch4docupstairs25
    k "Okay. Now listen, on a scale of one to ten, what would you rate your pain."
    p "Umm, maybe a three?"
    show bg ch4docupstairs19 with dissolve
    k "A three? You woke me up and got me out of bed for a three?"
    p "It's a painful three!"
    k "..."
    show bg ch4docupstairs21 with dissolve
    k "You asshole!"
    p "Whoa, wait!"
    show bg ch4docupstairs22 with dissolve
    $ renpy.pause(1)
    show bg ch4docupstairs23 with hpunch
    p "*In a squeaky voice* Ohhh! That's a ten! Definitely a ten!"
    show bg ch4docupstairs24 with dissolve
    p "What happened to do no harm!?"
    if k_score < 3:
        show bg ch4docupstairs22 with dissolve
        k "Want another one?"
        p "Ok, sorry! I deserved that!"
        show bg ch4docupstairs26 with dissolve
        k "Now let me sleep. *Under her breath* You're like a little kid, I swear..."
        show bg ch4docupstairs76 with dissolve
        n "Katie hits her pillow and in an instant, is fast asleep"
        p "(I deserved that...)"
        p "(Hopefully, she will forgive me in the morning...)"
        n "After a few minutes, you doze off"
        jump ch4vicmer
    else:
        jump ch4wakeupcont

label ch4wakeupcont:

    if _in_replay:
        play music audio.calm fadein 2.0 fadeout 2.0
        $ setReplay()
        if persistent.ch4doc1 == True:
            $ k_score = 4
            $ k_lust = 2

    show bg ch4docupstairs27 with dissolve
    k "Oh my God! I didn't-"
    p "*Let's out a few quick breaths*"
    show bg ch4docupstairs28 with dissolve
    k "I just meant to hit you in the stomach."
    p "Note to self, *cough* Doc gets cranky when she is woken up."
    show bg ch4docupstairs29 with dissolve
    k "I'm sorry. Just one tease too far, [p]."
    p "My fault. Totally deserved it. Let me make it up to you."
    show bg ch4docupstairs30 with dissolve
    k "Ohh! [p]!?"
    show bg ch4docupstairs31 with dissolve
    k "What are you doing? Stop joking around."
    show bg ch4docupstairs32 with dissolve
    p "I'm not. Not this time."
    p "Come here."
    show bg ch4docupstairs33 with dissolve
    n "The background of the city and the hum of machinery fade away at the sweetness of her lips touches yours"
    p "Are you okay?"
    k "I'm fine, why wouldn't I be?"
    show bg ch4docupstairs35 with dissolve
    p "In that case, hold on."
    k "Hold-?"
    show bg ch4docupstairs36 with dissolve
    k "Ahh! *Giggles* I- [p]!"
    p "What?"
    show bg ch4docupstairs37 with dissolve
    k "I think we..."
    p "Don't overthink."
    show bg ch4docupstairs38 with dissolve
    k "*Sigh* I'm just not ready. Been way too long and I'm not..."
    k "It's not med school anymore; not really up for anything where people can hear."
    k "Ah, I can't believe I just said that. Any of that. Can you ignore the \"been way too long\" part and..."
    if dep > 2:
        p "(Well, shit...)"
    else:
        "(She is the last person I'd push.)"
    show bg ch4docupstairs39 with dissolve
    p "It's okay, Katie. I'll let you sleep. Sorry if I made you uncomfortable. Just forget I said or did anything."
    k "I didn't say... what I mean is... there's room in the bed if you want. Better for your back, right?"
    p "You sure?"
    k "Positive, now lay down with me."
    show bg ch4docsidepan movie with dissolve
    k "You're staring, why are you staring?"
    p "You really are beautiful."
    k "..."
    p "What?"
    show bg ch4docupstairs40 with dissolve
    k "You say things like that, a girl might think you mean it."
    p "Katie, I do mean it."
    show bg ch4docupstairs41 with dissolve
    k "I never figured you for a sweetheart."
    p "Not my M.O., true."
    k "But... You are with me. Why?"
    p "Because... I don't know. Something about your brings it out."
    show bg ch4docupstairs42 with dissolve
    k "That's it?"
    p "Yes? It's hard not to act different around you... well, except when I'm teasing you, I guess."
    k "Just be quiet and come over here."
    $ resetmenu()
    jump ch4docupstairssleepmenu

label ch4docupstairssleepmenu:
    menu:
        "Focus on her eyes and lips" if menu1:
            $ menu1 = False
            jump ch4docupstairsface
        "Focus on her chest" if menu2:
            $ menu2 = False
            jump ch4docupstairsbreasts
        "Explore a bit lower" if menu3:
            $ menu3 = False
            jump ch4docupstairslower
        "Help her up" if menu1 == False or menu2 == False or menu3 == False:
            jump ch4docupstairskiss

label ch4docupstairsface:
    show bg ch4docupstairs44 with dissolve
    k "Hi... So, I, uh, might have morning breath... even if it's not morning."
    p "Hey... relax."
    show bg ch4docupstairs45 with dissolve
    k "Sorry..."
    p "No need to be sorry. In fact, it's rather cute."
    k "Endearing perhaps, but you are probably-"
    show bg ch4docupstairs46 with dissolve
    p "Katie, it's fine. I promise we won't go any farther than you're comfortable with."
    k "Well, you promised you wouldn't die tonight; so far you're batting one thousand."
    p "Batting one thousand?"
    k "One thousand. Baseball, silly. God, I miss that. "
    p "I never really followed baseball."
    show bg ch4docupstairs45 with dissolve
    k "I used to love going to games with my Dad. You know he took me to the last Major League World Series. Twins vs. Marlins."
    "Katie looks distant for a moment as she loses herself in the memory"
    if "ch4katiespast" in extraevents:
        menu:
            "He cared for you":
                $ k_score += 1
                p "He truly cared about you, didn't he?"
                k "He...*sniffs* Yeah, I really miss him."
                k "Enough about my family, what about yours?"
            "Must have been fun":

                p "That must have been fun."
                k "It was. Always something magical about going to a game."
                k "What about you? Ever do things like that with your folks?"
    else:
        p "That must have been fun."
        k "It was. Always something magical about going to a game."
        k "What about you? Ever do things like that with your folks?"

    p "Barely knew Dad, and Mom didn't have the time or money to take me out to sports."
    p "I see her once every few years. Dad I haven't seen since basic."
    k "Oh, I'm sorry."
    p "You keep saying that, don't be."
    k "Maybe we should stop talking about our parents."
    p "Good plan."
    jump ch4docupstairssleepmenu


label ch4docupstairsbreasts:
    p "Lay back."
    show bg ch4docupstairs51 with dissolve
    p "So, you think I was teasing when I said you're beautiful?"
    k "It's not that I didn't believe you, exactly."
    show bg ch4docupstairs52 with dissolve
    p "I wasn't. Teasing, that is."
    k "I'm just not great at taking compliments and I'm not one of those fancy LA girls."
    k "Everywhere I look I see supermodels or that bitch newscaster plastered on every billboard."
    show bg ch4doctits movie with dissolve
    p "I'd prefer you up there."
    p "A big giant holographic Katie dancing in the streets. Even the AI cars couldn't stop but stare."
    k "And now is when I think you're teasing again, [p]."
    p "I'll just say this once and know I mean it..."
    show bg ch4docupstairs53 with dissolve
    p "You're perfect."
    k "I... thank you."
    jump ch4docupstairssleepmenu

label ch4docupstairslower:
    show bg ch4docupstairs54 with dissolve
    p "You're in great shape. All that climbing?"
    k "Did a lot of sports back in school. Guess it stuck with me."
    show bg ch4docupstairs55 with dissolve
    p "I said perfect before and I meant it."
    k "[p]..."
    show bg ch4docupstairs56 with dissolve
    k "I'm... just not there yet."
    p "Can't blame a guy for trying."
    show bg ch4docupstairs57 with dissolve
    k "You're not upset?"
    p "Why would I be?"
    if menu1 == False and menu2 == False and menu3 == False:
        jump ch4docupstairskiss
    else:
        jump ch4docupstairssleepmenu

label ch4docupstairskiss:
    p "Grab my hand."
    show bg ch4docupstairs58 with dissolve
    $ renpy.pause(1)
    show bg ch4docupstairs59 with dissolve
    k "What are you doing?"
    p "Upsie-daisy."
    show bg ch4docupstairs60 with dissolve
    if menu3 == False:
        p "Is that better?"
        k "I guess... thank you."
        show bg ch4docupstairs61 with dissolve
        k "So, why did you sit me up?"
    else:


        p "There we go."
        k "Why do I think this is all part of some evil plan? "
        show bg ch4docupstairs61 with dissolve
        p "No plan. Just..."
        k "Just what?"
    show bg ch4docupstairs62 with dissolve
    p "Easier to kiss you in this position."
    k "Then kiss me."
    show bg ch4docupstairs63 with dissolve
    n "Your lips touch hers. Together, your breathing slows. Her worries and yours melt away."
    k "Mhmmm..."
    show bg ch4docupstairs70 with dissolve
    k "Hands, buster."
    p "It's as far as I go."
    show bg ch4docupstairs64 with dissolve
    k "Since you're my patient, us getting involved creates about a dozen ethics violations."
    p "*Chuckles* Such a rebel."
    k "You know me. Always living on the edge."
    p "Well, I won't tell if you won't."


    if k_score >= 4 and k_lust >= 2:
        $ persistent.ch4doc1 = True
        show bg ch4docupstairs69 with dissolve
        k "*Looks down to her chest* [p]... I don't mind your hands everywhere."
        show bg ch4docupstairs65 with dissolve
        p "That so? Are you okay with them here?"
        k "A bit to the side..."
        show bg ch4docupstairs66 with dissolve
        $ renpy.pause(1)
        show bg ch4docupstairs67 with dissolve
        p "Katie..."
        show bg ch4docupstairs68 with dissolve
        k "Tell me again I'm beautiful."
        p "You're beautiful."
        show bg ch4docnips movie with dissolve
        "*Soft kissing sounds*"
        k "Mmmm..."
        k "*Giggles* Okay, that's good. Any more and I'm not gonna be able to stop you."
        show bg ch4docupstairs71 with dissolve
        k "Which is probably the dumbest thing I could have said to you, now that I think about it."
        p "Not an invitation."
        k "No... I mean..."
        k "It's enough for tonight, ok?"

    show bg ch4docupstairs71 with dissolve
    k "We really should get some sleep."
    p "Yeah... sleep. Got a cold shower up here?"
    k "Downstairs, sorry."
    scene black with dissolve
    show bg ch4docupstairs72 with dissolve
    k "So, what do you think of our guests?"
    p "They're interesting. Beyond that, it's hard to say."
    k "Not afraid they are going to run?"
    p "Run where? He knows that these tests are the best thing for her. Her being safe? That's what he cares about."
    k "But she could be dangerous. Do you think she is?"
    p "Worried?"
    k "Don't dodge the question."
    show bg ch4docupstairs73 with dissolve
    p "Maybe? She stopped Henry and I from killing each other, so let's say I hope she's not."
    k "What do you mean?"
    p "A while back..."
    "*You abruptly stop speaking*"
    p "A kid like that shouldn't have that on her shoulders."
    k "Maybe tomorrow we can get some answers when she wakes."
    k "Right. Now I need to... *yawns*"
    show bg ch4docupstairs74 with dissolve
    k "*Begins to snore*"
    p "(You waste no time.)"
    p "Gus, turn off the lights."
    p "..."
    p "Lights off... Turn off the lights? I wish the lights were off?"
    p "..."
    p "Please?"
    $ extraevents.append("ch4katie")
    show bg ch4docupstairs75 with dissolve
    p "Huh, that actually worked."
    $ achievement.grant("FAKINGIT")
    init:
        $ achievement.register("FAKINGIT")
    $ achievement.Sync()
    p "(Well, should get Sonja to take a look at him.)"
    scene black with Dissolve(3)
    $ renpy.end_replay()
    if not persistent.ch4doc:
        $ renpy.notify(['Scene Unlocked', 'unlock'])
        $ persistent.ch4doc = True
    jump ch4vicmer
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
