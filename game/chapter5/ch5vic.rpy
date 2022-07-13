
image bg ch5office1 = "ch5office1"
image bg ch5office2 = "ch5office2"
image bg ch5office3 = "ch5office3"
image bg ch5office4 = "ch5office4"
image bg ch5office5 = "ch5office5"
image bg ch5office6 = "ch5office6"
image bg ch5office7 = "ch5office7"
image bg ch5office8 = "ch5office8"
image bg ch5office9 = "ch5office9"
image bg ch5office10 = "ch5office10"
image bg ch5office11 = "ch5office11"
image bg ch5office12 = "ch5office12"
image bg ch5office13 = "ch5office13"
image bg ch5office14 = "ch5office14"
image bg ch5office15 = "ch5office15"
image bg ch5office16 = "ch5office16"
image bg ch5office17 = "ch5office17"
image bg ch5office18 = "ch5office18"
image bg ch5office19 = "ch5office19"
image bg ch5office20 = "ch5office20"
image bg ch5office21 = "ch5office21"
image bg ch5office22 = "ch5office22"
image bg ch5office23 = "ch5office23"
image bg ch5office24 = "ch5office24"
image bg ch5office25 = "ch5office25"
image bg ch5office26 = "ch5office26"
image bg ch5office27 = "ch5office27"

label ch5office:
    scene black with Dissolve(2)
    show text "{=trans}EARLIER AT BAYNARD INDUSTRIES{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    play music audio.futurenoir fadein 2.0 fadeout 2.0
    if "ch4vicgoodbye" in extraevents or "ch4vicsex" in extraevents:
        show bg ch5office1 with Dissolve(1)
        v "Hope, you can verify that Mrs. White is not in the building?"
        "Hope" "That is correct."
        show bg ch5office2 with dissolve
        v "(Strange, where is she? Still, that does give me a chance to check on something.)"
        v "Something [p] said, bothered me..."
        show bg ch5office3 with dissolve
        n "Victoria moves towards Meredith's desk"
        show bg ch5office5 with dissolve
        v "Am I logged in, Hope?"
        "Hope" "Yes, Miss. Running silent."
        v "Good. Where is Mrs. White now?"
        "Hope" "Unknown. She is not on the grid."
        v "At all?"
        "Hope" "That is correct."
        v "What was her last location?"
        "Hope" "Classified."
        v "Why's it classified?"
        "Hope" "I can't access that."
        v "That was rhetorical."
        show bg ch5office4 with dissolve
        v "Hope, log me into Baynard's operation archives."
        "Hope" "Passphrase required."
        v "We are not interested in the possibilities of defeat; they do not exist."
        show bg ch5office6 with dissolve
        "Hope" "Logged in."
        v "Show me all logs of flights leaving in the last 24 hours."
        show bg ch5office7 with dissolve
        v "Hmm... A US Navy transport from last night. Hope, where was this headed?"
        "Hope" "Unknown."
        v "*Under her breath* Where did you go...?"
        v "Very well, Hope, access and copy any information on Caracas in the last five years."
        "Hope" "Classified."
        v "Of course. Run program---"
        n "Victoria's concentration is broken when she hears footsteps approaching the office door"
        show bg ch5office8 with dissolve
        v "Log me out. Now."
        show bg ch5office9 with dissolve
        m "Ugh... what a night..."
        v "Ma'am, there you are."
        show bg ch5office10 with dissolve
        m "Victoria? What are you doing in here?"
        v "I was attempting to locate you, Ma'am. Your locator beacon was off."
        show bg ch5office11 with dissolve
        m "*sighs* Just give me a minute."
        v "You appear to have had a difficult night, Mrs. White."
        m "You have no idea, Ms. Shields. Now, what was so important that you were on my computer?"
        show bg ch5office12 with dissolve
        v "Vostok is on the move again and with Agent [pl]-"
        m "It's handled, Victoria."
        v "With all due respect, Ma'am... Vostok has acquired at least half a dozen active ghosts, including Sonja [pl]."
        show bg ch5office13 with dissolve
        m "Sonja, eh? Shame. I really liked her."
        v "Ma'am?"
        m "It is of no consequence. As I mentioned, it is handled."
        show bg ch5office14 with dissolve
        v "We have no other agents who can activate -- none of consequence that is."
        m "We do, actually."
        v "Who?"
        m "Hope has just been forwarded his comm information. You will be running the operation as before."
        show bg ch5office17 with dissolve
        v "Meredith, I can't be effective if I am in the dark."
        m "Just follow your orders and I would watch that tone, {i}Ms. Shields.{/i}."
        show bg ch5office19 with dissolve
        v "I apologize. It's just..."
        m "Sit down, please."
        show bg ch5office20 with dissolve
        m "Despite what others think, you're still human. We all make mistakes, dear."
        m "I simply expect less of them from you."
        v "I apologize."
        show bg ch5office22 with dissolve
        m "With Agent [pl]'s history, this was always a risk. Though I still have faith, he will come to his senses."
        m "This new asset is simply backup."
        v "I understand. Again, my apologies."
        show bg ch5office23 with dissolve
        m "No more apologies. You won't need them. I know you will succeed."
        m "Besides, how can someone resist you?"
        show bg ch5office25 with dissolve
        m "And, you know? These you wear well. You should think about wearing them far more often."
        m "That look suits you, by the way -- classic and elegant."
        show bg ch5office26 with dissolve
        v "Thank you..."
        m "Of course."
        show bg ch5office27 with dissolve
        m "Now, if you don't mind, have Hope send the details of the Vostok team to our new Agent."
        v "I will. Get some rest, Ma'am."
        jump ch5officeend
    else:

        show bg ch5office9 with dissolve
        m "Ugh..."
        m "Rather deal with Chandra."
        show bg ch5office11 with dissolve
        m "*Let's out a drawn breath* Maya, is Victoria here yet?"
        "Meredith's AI responds"
        "Maya" "She's just outside your door, Ma'am."
        show bg ch5office13 with dissolve
        m "Good. Send her in."
        n "A knock is heard on the other side of the door."
        show bg ch5office14 with dissolve
        m "Come in, Victoria."
        show bg ch5office16 with dissolve
        $ renpy.pause(1)
        show bg ch5office15 with dissolve
        m "I hope you have some good news for me?"
        v "I have news, difficult to say its type. Vostok is on the move again, half a dozen agents, including Sonja [pl] and Charles Anderson."
        m "And our agent?"
        if "ch4vicaccept" in extraevents:
            show bg ch5office18 with dissolve
            v "Still unknown, but I believe he will return to us, given time."
            show bg ch5office21 with dissolve
            m "Time is a luxury we don't seem to have, but again, good work, Victoria."
            v "Thank you, Ma'am."
        else:
            show bg ch5office17 with dissolve
            v "He is proving quite difficult. He followed me last night."
            show bg ch5office20 with dissolve
            m "Followed you? What did he do?"
            v "My hooks are only partly in him. He proved to be un-receptive to our offer."

        v "You seem unconcerned, might I inquire as to why?"
        show bg ch5office24 with dissolve

        m "I managed to acquire a backup for our agent, just in case things fall through. Plus, it may be more incentive for [p] to come back."
        v "May I ask who? All agents of consequence have been recruited by Vostok."
        m "Hope has just been forwarded his comm information. You will be running the operation as before..."
        v "How am I supposed to run an operation when I don't know..."
        m "A Red Moon."
        v "That's not possible."
        m "We must not fail."
        show bg ch5office25 with dissolve
        m "Now, I must say it's no wonder our agent is fascinated by you. Has he seen you in these stockings before?"
        v "No, he has not."
        m "The way you wear these. I think all our issues would be over if he saw you in them. You know, perhaps you should wear these more often."
        v "Gladly."
        show bg ch5office27 with dissolve
        m "Thank you for the update. Now, if you excuse me, I need some rest. Wake me on any developments."
        v "Yes, Ma'am."
        jump ch5officeend

label ch5officeend:
    if "ch5gloriamad" in extraevents:
        jump ch5henry
    else:
        jump ch5walk
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
