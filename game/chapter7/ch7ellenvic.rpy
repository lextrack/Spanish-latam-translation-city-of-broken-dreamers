

image bg ch7vic1 = "ch7vic1"
image bg ch7vic2 = "ch7vic2"
image bg ch7vic3 = "ch7vic3"
image bg ch7vic4 = "ch7vic4"
image bg ch7vic5 = "ch7vic5"
image bg ch7vic6 = "ch7vic6"
image bg ch7vic7 = "ch7vic7"
image bg ch7vic8 = "ch7vic8"
image bg ch7vic9 = "ch7vic9"
image bg ch7vic10 = "ch7vic10"
image bg ch7vic11 = "ch7vic11"
image bg ch7vic12 = "ch7vic12"
image bg ch7vic13 = "ch7vic13"
image bg ch7vic14 = "ch7vic14"
image bg ch7vic15 = "ch7vic15"
image bg ch7vic16 = "ch7vic16"
image bg ch7vic17 = "ch7vic17"
image bg ch7vic18 = "ch7vic18"
image bg ch7vic19 = "ch7vic19"
image bg ch7vic20 = "ch7vic20"
image bg ch7vic21 = "ch7vic21"
image bg ch7vic22 = "ch7vic22"
image bg ch7vic23 = "ch7vic23"
image bg ch7vic24 = "ch7vic24"
image bg ch7vic25 = "ch7vic25"
image bg ch7vic26 = "ch7vic26"
image bg ch7vic27 = "ch7vic27"
image bg ch7vic28 = "ch7vic28"
image bg ch7vic29 = "ch7vic29"
image bg ch7vic30 = "ch7vic30"
image bg ch7vic31 = "ch7vic31"
image bg ch7vic32 = "ch7vic32"
image bg ch7vic33 = "ch7vic33"
image bg ch7vic34 = "ch7vic34"
image bg ch7vic35 = "ch7vic35"
image bg ch7vic36 = "ch7vic36"
image bg ch7vic37 = "ch7vic37"
image bg ch7vic38 = "ch7vic38"
image bg ch7vic39 = "ch7vic39"
image bg ch7vic40 = "ch7vic40"
image bg ch7vic41 = "ch7vic41"
image bg ch7vic42 = "ch7vic42"
image bg ch7vic43 = "ch7vic43"
image bg ch7vic44 = "ch7vic44"
image bg ch7vic45 = "ch7vic45"
image bg ch7vic46 = "ch7vic46"
image bg ch7vic47 = "ch7vic47"
image bg ch7vic48 = "ch7vic48"
image bg ch7vic49 = "ch7vic49"



label ch7ellenvic:

    $ resetsexmenu()






    scene black with Dissolve(1)
    play music audio.futurenoir fadein 2.0 fadeout 2.0
    show text "{=trans}MEANWHILE, AT BAYNARD HOSPITAL{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)

    if v_score < 4 and "ch4vicgoodbye" in extraevents:
        $ sexmenu1 = True
        $ sexmenu2 = True
        $ sexmenu3 = False
    elif "ch4vicaccept" in extraevents:
        $ sexmenu1 = True
        $ sexmenu2 = False
        $ sexmenu3 = False
    elif v_score < 4:
        $ sexmenu1 = True
        $ sexmenu2 = False
        $ sexmenu3 = True
    else:

        $ sexmenu1 = False
        $ sexmenu2 = True
        $ sexmenu3 = False

    if sexmenu1 == True and sexmenu3 == True:
        show bg ch7vic2 with dissolve
        v "{i}This will all end soon enough. Ellen, you're going to consider yourself lucky after all this.{/i}"
    if sexmenu1 == True and sexmenu3 == False:
        show bg ch7vic1 with dissolve
        v "{i}What have I done..?{/i}"
    if sexmenu1 == False:
        show bg ch7vic2 with dissolve
        v "{i}God. What a night...{/i}"

    show bg ch7vic3 with dissolve
    n "Victoria quietly approaches the side of Ellen's bed"
    v "Ellen?"
    show bg ch7vic4 with dissolve
    $ renpy.pause(1)
    show bg ch7vic5 with dissolve

    if sexmenu1 == True:

        v "If you thought you hated me yesterday..."
        show bg ch7vic7 with dissolve
        v "You will never forgive me after last night."
        e "Ugh... The hell...?"
        show bg ch7vic16 with dissolve
        e "Forgive you for what? Another diabolical plot twist? And what damn time is it?"
    else:

        v "I wish I could tell you what I just did..."
        show bg ch7vic6 with dissolve
        v "Part of you would be pretty proud, I would imagine."
        e "Ugh... The hell...?"
        show bg ch7vic16
        e "Proud of you? Doubtful... And what god damn time is it?"
    show bg ch7vic8 with dissolve
    v "It's early, I didn't mean to wake you."
    if sexmenu1 == True:
        show bg ch7vic29 with dissolve
        e "Well, I'm fucking up now, so answer the question. What did you do?!"
        e "Did you get Gloria? Is that it?"
        show bg ch7vic9 with dissolve
        v "No. Not that."
        e "So, what is it?"
        v "Some business. Nothing I'd particularly like to share. Just know it is something I am not proud of."
        show bg ch7vic29 with dissolve
        e "Cry me a fucking river. You're not getting any sympathy from me."
        show bg ch7vic8 with dissolve
        v "I don't expect any."
        e "Good. Now that that's over, why in the prime hell am I always waking up to you half-naked?"
        v "Huh. I suppose that would be rather off-putting."
        e "Fuck me, you're really something else, you know that?"
        show bg ch7vic10 with dissolve
        v "To answer your question, it's a matter of convenience and efficiency."
        v "This location is ideal. My residence is further out."
        show bg ch7vic11 with dissolve
        v "Time is money, is it not?"
        show bg ch7vic13 with dissolve
        e "Surprised people like you don't have that tattooed on your ass."
        v "I don't have any tattoos. They aren't allowed."
        show bg ch7vic15 with dissolve
        v "I did have another reason for coming here. Ellen, you can still be of assistance."
        e "Get fucked..."
        show bg ch7vic25 with dissolve
        v "It would be well worth your while. And help assure the best outcome for all involved."
        e "Even if I did know, which I already told you, I fucking don't... I wouldn't tell you shit."
        show bg ch7vic29 with dissolve
        e "So, cut the vixen bullshit, I'm not helping you."
        v "I was afraid you would act this way."
        show bg ch7vic34 with dissolve
        v "Listen to me, Ellen. Just tell me where they are."
        e "Bite me."
        show bg ch7vic35 with dissolve
        v "We can help her. Besides, do you really think [p] has her best interests in mind?"
        if e_score >= 3:
            e "Yeah, I do."
        else:
            e "More than you do."

        show bg ch7vic36 with dissolve
        v "Ellen... Just tell me, then everything will be alright."
        e "What are you..."
        show bg ch7vic37 with dissolve
        v "That's it. Now, think back. They might have mentioned something, some clue you overlooked."
        e "I..."
        v "Anything at all. And you can get your old life back again."
        show bg ch7vic38 with dissolve
        e "As if I'd want it! Find 'em yourself."
        v "Now Elle---"
        e "*Bursts out laughing* Ha! Your voodoo shit doesn't work!"
        show bg ch7vic40 with dissolve
        e "Now get your plastic ass out of my room!"
        show bg ch7vic41 with dissolve
        v "*Sigh* We will continue this later."
        e "Don't rush on my account."
        show bg ch7vic43 with dissolve
        n "Victoria's attention is drawn away as she begins to listen intently"
        v "Yes, ma'am. Of course."
        show bg ch7vic44 with dissolve
        v "My apologies, Miss Lane, but I am afraid our conversation must end abruptly."
        e "Just when I thought we were bonding."
        show bg ch7vic45 with dissolve
        v "Redondo Beach?"
        e "Who are you talking to?!"
        show bg ch7vic46 with dissolve
        v "Yes. I'll direct our assets there now."
        e "Go run your errands..."
        show bg ch7vic47 with dissolve
        v "May we continue this conversation later?"
        e "Not like I have a choice, do I?"
        show bg ch7vic49 with dissolve
        $ renpy.pause(1)
        show bg ch7vic48 with dissolve
        e "Back to staring at the ceiling..."
        jump ch7stairwayprep
    else:



        show bg ch7vic29 with dissolve
        e "The fuck are you doing here again? Can't even let me sleep?"
        show bg ch7vic8 with dissolve
        v "Apologies, I just needed a change of clothes."
        show bg ch7vic28 with dissolve
        e "And your corporate blood money doesn't let you afford a home?"
        show bg ch7vic10 with dissolve
        v "Of course it does."
        e "Then why?"
        v "A few reasons."
        e "Like?"
        show bg ch7vic11 with dissolve
        v "My place is well outside the city center. It's more convenient here."
        show bg ch7vic21 with dissolve
        e "You mean Baynard needs you here."
        show bg ch7vic13 with dissolve
        v "Actually, no. This visit is off the books. Well, as off the books as it gets in a Baynard hospital."
        e "Bullshit."
        show bg ch7vic14 with dissolve
        n "Victoria's accent falls back to her soft Midwestern tone"
        v "Ellen, I told you yesterday I wasn't lying to you. I'm still not. And I won't."
        show bg ch7vic22 with dissolve
        e "..."
        e "How the fuck am I supposed to believe that?"
        show bg ch7vic17 with dissolve
        v "I suppose you would be a fool to."
        e "Now that I can agree with."
        show bg ch7vic19 with dissolve
        v "Still. I haven't lied to you. Not once..."
        e "Sure..."
        show bg ch7vic20 with dissolve
        v "You have no reason to believe me, but it needed to be said."
        v "This situation continues to spiral out of control. I want you to know that I'll make sure nothing happens to you."
        show bg ch7vic18 with dissolve
        e "What are you saying?"
        v "My superior has been acting... Irrationally. I can't say for certain just how far she will go."
        e "Wait, you think you're protecting me?"
        show bg ch7vic24 with dissolve
        v "In a manner of speaking, yes."
        e "Umm... you are fucking weird you know that?"
        show bg ch7vic27 with dissolve
        v "*chuckles* Yes I do. I haven't lived a normal life for a long time."
        v "I can't even remember the last time I visited a friend."
        show bg ch7vic28 with dissolve
        e "Is that what you think we are?"
        show bg ch7vic30 with dissolve
        v "It doesn't matter. Friends are a liability."
        show bg ch7vic33 with dissolve
        e "So tell me this, I'm just a down-on-her-luck fixer..."
        e "Why me?"
        show bg ch7vic32 with dissolve
        v "Ellen, do you know why I kept contracting with you?"
        e "Probably because of my contacts with [p] and Gloria."
        v "No. If anything, your links with Ms. Conner should have disqualified you."
        e "So why?"
        show bg ch7vic31 with dissolve
        v "Ellen, you're honest."
        v "You never put on airs and you are true to yourself, often to your own detriment."
        e "Thanks?"
        v "I'm not afforded that luxury. In many ways I envy you."
        e "..."
        show bg ch7vic23 with dissolve
        v "I'm sorry, I should go. This was a mistake."
        v "Get well. I won't bother you again."

        show bg ch7vic28 with dissolve
        e "Wait... Do you know what you need to do?"
        show bg ch7vic19 with dissolve
        v "Can I hazard a guess? \"Get Fucked?\""
        show bg ch7vic33 with dissolve
        e "No. Not that it would be hard with those tits."
        e "Tell your boss to eat a dick. Go right up to her and drop the bomb."
        e "I can see that you want to. You want to be honest? Start there."

        show bg ch7vic41 with dissolve
        v "In a sense, I did just that earlier tonight."
        e "No shit?"
        call ch7meredith from _call_ch7meredith
        show bg ch7vic40 with dissolve
        e "Well, not exactly honest. But you're getting there."
        e "Next time, you should take a shit on her desk."
        show bg ch7vic42 with dissolve
        v "I'll take it under consideration."
        show bg ch7vic39 with dissolve
        e "And just so you know. I still don't trust you."
        e "But at least you sound like a human for once."
        show bg ch7vic41 with dissolve
        v "Hey, I-"
        show bg ch7vic43 with dissolve
        n "Victoria's attention is drawn away as she begins to listen intently. Her accent snaps back to normal."
        v "Yes, ma'am. Of course."
        show bg ch7vic44 with dissolve
        v "Yes. I'll direct our assets there now."
        e "There goes that idea of sounding human..."
        show bg ch7vic45 with dissolve
        v "My apologies, Miss Lane, but I am afraid our conversation must end abruptly."

        e "Where the hell are you going?"
        show bg ch7vic46 with dissolve
        e "Hey, I'm talking to you!"
        show bg ch7vic47 with dissolve
        v "I'm glad we had this conversation."
        e "Great... whatever..."
        show bg ch7vic49 with dissolve
        $ renpy.pause(1)
        show bg ch7vic48 with dissolve
        e "You could at least have turned on the feeds."
        jump ch7stairwayprep
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
