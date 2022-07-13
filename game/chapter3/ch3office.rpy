image bg ch3office1 = "ch3office1"
image bg ch3office2 = "ch3office2"
image bg ch3office3 = "ch3office3"
image bg ch3office4 = "ch3office4"
image bg ch3office5 = "ch3office5"
image bg ch3office6 = "ch3office6"
image bg ch3office7 = "ch3office7"
image bg ch3office8 = "ch3office8"
image bg ch3office9 = "ch3office9"
image bg ch3office10 = "ch3office10"
image bg ch3office11 = "ch3office11"
image bg ch3office12 = "ch3office12"
image bg ch3office13 = "ch3office13"
image bg ch3office14 = "ch3office14"
image bg ch3office15 = "ch3office15"
image bg ch3office16 = "ch3office16"
image bg ch3office17 = "ch3office17"
image bg ch3office18 = "ch3office18"
image bg ch3office19 = "ch3office19"
image bg ch3office20 = "ch3office20"
image bg ch3office21 = "ch3office21"
image bg ch3office22 = "ch3office22"
image bg ch3office23 = "ch3office23"
image bg ch3office24 = "ch3office24"
image bg ch3office25 = "ch3office25"
image bg ch3office26 = "ch3office26"
image bg ch3office27 = "ch3office27"
image bg ch3office28 = "ch3office28"
image bg ch3office29 = "ch3office29"
image bg ch3office30 = "ch3office30"

image bg ch3office31 = "ch3office31"
image bg ch3office32 = "ch3office32"
image bg ch3office33 = "ch3office33"
image bg ch3office34 = "ch3office34"
image bg ch3office35 = "ch3office35"
image bg ch3office36 = "ch3office36"
image bg ch3office37 = "ch3office37"
image bg ch3office38 = "ch3office38"
image bg ch3office39 = "ch3office39"
image bg ch3office40 = "ch3office40"
image bg ch3office41 = "ch3office41"







label ch3office:

    scene black with Dissolve(2)
    show text "{=trans}A WHILE LATER, AT BAYNARD INDUSTRIES{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    show bg ch1hallway1 with dissolve
    $ renpy.pause(1)
    show bg ch1hallway2 with dissolve
    p "(Here we go again...)"
    show bg ch1hallway3 with dissolve
    if not persistent.ch3card2:
        $ renpy.notify(['Possible clue', 'alert'])
        show screen hidden_item("ch3card2", "ch3card2", 861, 211, 175, 125)
    p "(I wish she would just let me do my job. Status updates...)"
    n "A muffled argument can be heard on the other side of the door"
    hide screen hidden_item

    scene black with dissolve
    show bg ch3office1 with dissolve
    play music audio.futurenoir fadein 2.0 fadeout 2.0
    c "That's it! We're done, {i}Mom{/i}!"
    m "Done? I think not. We will finish this discussion later, young lady!"
    c "Yeah right..."
    show bg ch3office2 with dissolve
    m "Chandra, I don't have time for your tantrums."
    show bg ch3office3 with dissolve
    c "Pfft. Whatever... *Under her breath* Bitch..."
    m "Excuse me?"
    if "ch1chandra" in extraevents:
        show bg ch3office5 with dissolve
        c "Mmm, {i}hello{/i}."
        p "(Oh fuck...)"
        p "Chandra..."
        show bg ch3office6 with dissolve
        c "You know what I like about [p], Mom? He doesn't bullshit! Or make excuses!"
        c "You could learn a thing or two."
    else:
        show bg ch3office4 with dissolve
        c "Well, look who it is. Didn't know you were working for her again."
        p "Didn't want to be."
        show bg ch3office6 with dissolve
        c "Have a good meeting! And if you happen to lose your temper with that ice queen over there and she flies out that window..."
        c "I won't ask questions."

    show bg ch3office7 with dissolve
    n "With a sharp bang, the door slams."
    m "*Sighs* If ever the inclination strikes you, Agent, for your own sanity, don't procreate."
    p "Wasn't planning on it."
    m "They begin as adorable, loving, and attentive. They make each day worth living."
    show bg ch3office8 with dissolve
    m "Yet, soon enough..."
    p "They're ditching my protection detail to get drunk at the newest club in town?"
    m "I long for those simpler days."
    show bg ch3office10 with dissolve
    m "But that's beside the point, this wasn't our first altercation, nor will it be our last. Now to business, Agent."
    m "It's been two days. I see a disturbing lack of progress, despite Ms. Shields' attempts to persuade me otherwise."
    show bg ch3office12 with dissolve
    menu:
        "These things take time":
            p "These jobs take time, Meredith. If you wanted someone to jump in feet first, you should have called Sonja."
            p "Besides, you haven't exactly been forthright with me about this job."
            show bg ch3office11 with dissolve
            m "Oh? Should I whisper my secrets in your ear? Shall I tell the formula for Euphorirem as well?!"
            m "Stop mewling. You are to deliver results, Agent. If you cannot do this, I will procure an asset who can."
            p "Good luck with that."
            show bg ch3office13 with dissolve
            m "Can you at least assure me you are close to locating the target?"
            p "I know where she is."
            m "Where!?"
            p "Heh, I don't think so, Meredith. She'll be in your hands by morning, but I do it on my own. Keep the fuck away from it."
            m "I demand..."
            p "Deal with it or fire me. Take your pick."
            show bg ch3office14 with dissolve
            m "Very well. This conversation is tiring. I have already dealt with one too many petulant children today. Victoria has additional information you will find useful."
            m "Mayhap you will be less rude to her."
            if "ch1vic" in extraevents or "ch2vicsex" in extraevents:
                m "You seem to enjoy her company quite a bit. Or so I am told."
            elif v_score >= 3:
                m "She has taken quite a liking to you. Why that is, remains a mystery."
            m "Victoria, come in, please."
            jump ch3officevic
        "Piss off":

            $ dep += 1
            p "Piss off, Meredith."
            p "You don't get to tell me how to do my job. Never again."
            m "Incredible, your ability to cling to the past never ceases to amaze me."
            show bg ch3office13 with dissolve
            m "Very well. This conversation will be tiring. I have already dealt with one too many petulant children today. Victoria has additional information you will find useful."
            m "Mayhap you will be less rude to her."
            if "ch1vic" in extraevents or "ch2vicsex" in extraevents:
                m "You seem to enjoy her company quite a bit. Or so I am told."
            elif v_score >= 3:
                m "She has taken quite a liking to you. Why that is, remains a mystery."
            m "Victoria, come in, please."
            jump ch3officevic



label ch3officevic:
    show bg ch3office15 with dissolve
    v "Yes, Ma'am."
    if v_score >= 2:
        v "How are you, Agent?"
    else:
        v "Agent."
    m "Please be so kind as to educate Mr. [pl] and I on what you recently learned."
    show bg ch3office16 with dissolve
    if "ch2choosevic" in extraevents:
        v "Well, Agent [pl] believes the bodyguard of the target is alive."
    else:
        v "After doing more research, we believe that the bodyguard may still be alive."
        if "ch3findbug" in extraevents:
            p "(I wonder what led you to that...)"


    show bg ch3office20 with dissolve
    m "Which bodyguard was this?"
    v "A Henry Gibson, decorated two bronze stars, a purple heart and a medal of valor. 132 confirmed kills and two Red Moon hybrids eliminated in single combat."
    v "He was part of the original augment program during the war. Now, one of the last."
    m "I remember now. However that avenue of investigation was eliminated on account of Gibson's suicide, was it not?"
    show bg ch3office19 with dissolve
    v "That is what we thought at the time, ma'am. Outside of health issues due to their implants, suicide rates among veteran augments unable to readjust to civilian life were abnormally high."
    v "Gibson's suicide matched the pattern. However, after comparing archived video, there is a high probability of a match."
    p "It is a match."
    show bg ch3office18 with dissolve
    v "Enlighten me, Agent."
    p "I've seen him. I won't tell you where, but he is alive. My guess is, he has her."
    show bg ch3office17 with dissolve
    v "Your silence does nothing but endanger the mission, Agent. However, as you have full operational control, the choice is yours."
    v "I have uploaded all the information we have on this Henry Gibson to your AI. I highly suggest you look it over."
    p "Thank you. I will."
    v "Do not enter this conflict blindly. Anyone, augment or not, who can destroy a Red Moon agent should not be trifled with."
    show bg ch3office21 with dissolve
    m "Victoria, can you please continue the Agent's debrief alone? I need to speak with my daughter..."
    v "Of course, ma'am."
    show bg ch3office22 with dissolve
    m "*Under her breath* What am I going to do with you?"
    p "(That could have gone worse. Barely.)"


    if v_score >= 2:
        jump ch3victalk
    else:
        jump ch3vicseduce

label ch3victalk:
    show bg ch3office23 with dissolve
    v "So, you located the bodyguard?"
    p "I did. I'll be heading out tonight with the proper gear to handle it."
    show bg ch3office24 with dissolve
    v "Do be careful, Agent."
    p "I really wish people would stop saying that."
    show bg ch3office31 with dissolve
    v "Unlike others you may have talked to, I know what you are up against."
    p "What can you tell me about him?"
    show bg ch3office32 with dissolve
    v "I have only begun my research, but I have learned some concerning facts. The first generation augments pushed and exceeded the limits of both physical and mental capabilities for any human."
    p "So this wasn't regular gene therapy."
    v "Hardly. My augmentation was difficult, but Mr. Gibson's was something else entirely. Candidates for the program suffered a fifty percent mortality rate in the beginning."
    p "You're shitting me!"
    v "Those numbers were never made public. The program did succeed in creating its super soldiers. Those that survived were gifted with strength, speed, tactical knowledge, and senses that verged on the superhuman."
    v "And that was just the beginning."
    p "What else could they need?"
    show bg ch3office33 with dissolve
    v "Real-time connection to sat navs, communication suppression, subdermal armor and reinforced muscles."
    p "Are you telling me he can see an overworld map from a sat nav in real time, anywhere?"
    show bg ch3office41 with dissolve
    v "To a degree. He only has access to one region."
    p "Which is?"
    show bg ch3office34 with dissolve
    v "Their last theater of operation. For Mr. Gibson, it would be the burned out remains of Tokyo."
    v "Just another reminder of the world that once was."
    show bg ch3office35 with dissolve
    v "May I ask you something, Agent?"
    p "Go ahead."
    if "ch1turndown" in extraevents:
        v "The first night we met, I offered you something and you refused. Can I ask why?"
        menu:
            "You're not my type" if "ch2vicsex" not in extraevents:
                $ extraevents.append("ch3vicnothanks")
                p "I don't mean to offend, but you're not my type. Busty redheads aren't my thing."
                show bg ch3office36 with dissolve
                v "Blunt. I appreciate it. We all have our own tastes. No offense was given. I do respect the professionalism."
            "I didn't trust you":
                $ v_score += 1
                p "I knew you were using yourself as a powerplay against me. Maybe you thought it would get me under your thumb. Maybe not."
                show bg ch3office37 with dissolve
                v "..."
                p "Then again, maybe you were ordered to. Either way, it didn't feel right."
                v "I understand."
            "That's not how I do business":
                $ extraevents.append("ch3vicbusiness")
                $ v_score += 2
                p "I don't know what passes for normal in the corp world, maybe fucking's the new handshake. When it comes to business, I don't do that."
                show bg ch3office38 with dissolve
                v "Then what is it you do?"
                p "I'm not a saint, but I could see what was happening. Meredith asked you to do that. It wasn't right."
                show bg ch3office36 with dissolve
                v "... I-"
                p "You don't need to respond to that. You're a person, not a tool."
                show bg ch3office35 with dissolve
                v "..."
                p "What?"
                v "That statement is naive, but appreciated nonetheless."
    else:
        v "You have treated me with respect. Surprising, for one in your business. This was -- unexpected..."
        p "You're asking me why?"
        v "Yes."
        menu:
            "You're doing your job":
                $ v_score +=1
                p "You're doing your job. We may not see eye to eye, but I'm not going to give you shit for following orders."
                show bg ch3office37 with dissolve
                v "Do you believe its all under orders?"
                p "I absolutely do."
                v "Very well."
            "There is more to you":

                p "You try to hide it, but you can't fool me. There's more to you than you let on."
                show bg ch3office36 with dissolve
                $ v_score += 1

                v "Do you truly think so? Is this all just an act?"
                if "ch2vicsex" in extraevents:
                    v "Even last night?"
                    menu:
                        "Sadly, I do":
                            p "I wish I didn't. But... I do."
                            v "Very well."
                        "I don't know":
                            $ extraevents.append("ch3vicknow")
                            $ v_lust += 1
                            p "I don't know. I'd like to think it wasn't."
                            show bg ch3office37 with dissolve
                            v "Everyone is an actor, Agent [pl]."
                            v "We play out the roles that we are assigned. The difference is how much heart goes into the performance."
                            p "That's a pretty pessimistic view."
                            show bg ch3office35 with dissolve
                            v "So is distrust. Perhaps we should try a little less of both."
                else:
                    p "Unfortunatly, I do."
                    v "Very well."
            "Best to keep your enemies close":


                p "I don't trust you, Victoria. Not in the least."
                show bg ch3office37 with dissolve
                v "So, best to not wake the dragon?"
                p "Precisely. I'll have enough to deal with shortly. Rather ensure you're on my good side."
                v "Very well."

    if "ch3vicbusiness" in extraevents or "ch3vicknow" in extraevents:
        show bg ch3office39 with dissolve
    else:
        show bg ch3office40 with dissolve
    v "I'll let you take your leave now, Agent. We expect delivery tomorrow."
    p "You'll have it."
    v "Good luck, Agent."
    jump ch3leaveoffice


label ch3vicseduce:
    $ extraevents.append("ch3vicgoodluck")
    show bg ch3office23 with dissolve
    v "So, Agent, you know where Miss Conner is at?"
    p "I think so."
    show bg ch3office24 with dissolve
    v "Hmm, so we should expect delivery soon?"
    p "In the morning, yeah."
    show bg ch3office25 with dissolve
    v "Good, are you {i}sure{/i} you don't require assistance?"
    p "I'll be fine."
    show bg ch3office26 with dissolve
    v "Perhaps, but we would like to have some insurance."
    p "I said I'll be fine."
    show bg ch3office27 with dissolve
    v "I know that, but your further cooperation would be highly appreciated."
    p "I..."
    v "Yes, Agent?"
    show bg ch3office28 with dissolve
    v "Do you have something you wish to share with me? I think you do."
    show bg ch3office29 with dissolve
    v "And once you have finished this contract, we can see each other in more... casual circumstances. And telling me will let that happen sooner."
    p "I... what? Stop! I'm not telling you anything. You'll get your mark. That's all you need to know."
    show bg ch3office30 with dissolve
    v "Then I have no choice but to wait."
    p "Yeah."
    v "Good luck, Agent. Do try to stay alive."
    jump ch3leaveoffice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
