
image bg ch4shower1 = "ch4shower1"
image bg ch4shower2 = "ch4shower2"
image bg ch4shower3 = "ch4shower3"
image bg ch4shower4 = "ch4shower4"
image bg ch4shower5 = "ch4shower5"
image bg ch4shower6 = "ch4shower6"
image bg ch4shower7 = "ch4shower7"
image bg ch4shower8 = "ch4shower8"
image bg ch4shower9 = "ch4shower9"
image bg ch4shower10 = "ch4shower10"
image bg ch4shower11 = "ch4shower11"
image bg ch4shower12 = "ch4shower12"
image bg ch4shower13 = "ch4shower13"
image bg ch4shower14 = "ch4shower14"
image bg ch4shower15 = "ch4shower15"
image bg ch4shower16 = "ch4shower16"
image bg ch4shower17 = "ch4shower17"
image bg ch4shower18 = "ch4shower18"
image bg ch4shower19 = "ch4shower19"
image bg ch4shower20 = "ch4shower20"
image bg ch4shower21 = "ch4shower21"






label ch4vicmer:
    play music audio.futurenoir fadein 2.0 fadeout 2.0
    show text "{=trans}THE NEXT MORNING, AT BAYNARD INDUSTRIES{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    show bg ch4shower1 with dissolve
    n "The falling water of the shower dances across the floor"
    v "*Humming to herself*"
    show bg ch4shower2 with dissolve
    $ renpy.pause(2)
    show bg ch4shower3 with dissolve
    $ renpy.pause(2)
    show bg ch4shower4 with dissolve
    v "*Slowly exhales as the water pours over her*"
    show bg ch4shower5 with dissolve
    m "Victoria?"
    v "Yes, ma'am?"
    m "Where is our Agent, Victoria? I expected him as of this morning."
    v "As did I."
    show bg ch4shower6 with dissolve
    m "You had one job, Victoria. Please don't make me regret putting you on it."
    m "Be such a waste."
    show bg ch4shower7 with dissolve
    v "I won't let you down, ma'am."

    if v_score >=4:
        v "Agent [pl] is not like most. He will require more persuading."
        show bg ch4shower8 with dissolve
        m "[pl] can be truculent, but at the end of the day, he's a grunt. Controlling him should be child's play for one with your skills and experience."
        show bg ch4shower9 with dissolve
        v "I will make another attempt."
        m "Attempt, Victoria? You will not just attempt, but succeed. Don't make me regret raising you up."
        if "ch3vicnothanks" in extraevents:
            v "I will succeed, then. Try different avenues, if I must."
            m "You do that."
        else:
            v "I will succeed, then."
            m "You do that."
        show bg ch4shower12 with dissolve
        v "Do you require anything else?"
        m "Actually. Come here, Victoria."
        show bg ch4shower14 with dissolve
        m "Remember the day I recommended you for the trials? You were so plain then, but you had that fire in you."
        m "Look at you now. As beautiful as science could make you. Amazing, really."
        v "Ma'am?"
        show bg ch4shower15 with dissolve
        m "Shame that fire seems extinguished. Well, nearly so."
        v "I've never failed you before."
        show bg ch4shower16 with dissolve
        m "No, never. No matter what work needed to be done, you did it. Unquestioningly."
        v "..."
        show bg ch4shower17 with dissolve
        m "You truly could bend them to your will."
        m "But now, I am not so sure."
        show bg ch4shower18 with dissolve
        m "This power of yours has made you weak. Have you forgotten that I picked you for your brains?"
        v "My apologies, ma'am."
        show bg ch4shower19 with dissolve
        m "Not all our problems can be solved with this. I need a whore at times, but one with the drive and wits to use those charms as a scalpel and not a broadsword."
        v "..."
        m "I'm glad we understand each other."
        show bg ch4shower20 with dissolve
        m "Now, go find Agent [pl]. We need that girl before Vostok finds her."
        v "I will..."
        show bg ch4shower21 with dissolve
        m "There is also the very real possibility that our agent is dead. Gibson is a powerhouse after all."
        v "It is possible, though I don't think..."
        m "Well, if he is dead, all is not lost. I will procure a new asset to assist us."
        v "A new asset?"
        m "Don't concern yourself with that, instead focus on locating our runaway."
        v "Of course, ma'am."


    elif "ch3vicgoodluck" in extraevents:
        show bg ch4shower10 with dissolve
        v "I can manage him."
        if "ch1spellbound" in extraevents:
            v "Besides, I tell him to jump. He will jump."
        v "If he was successful in acquiring the girl, he will bring her to us. Mark my words."
        show bg ch4shower11 with dissolve
        m "Regardless, I have found an alternate in case our agent did not survive the night."
        v "Who, ma'am?"
        show bg ch4shower12 with dissolve
        m "For now, that is not your concern. Now go find out what happened last night."
        v "As you say, ma'am."


    jump ch4katiemorning
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
