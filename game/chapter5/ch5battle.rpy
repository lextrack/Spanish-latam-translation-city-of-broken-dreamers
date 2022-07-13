

image bg ch5battle1 = "ch5battle1"
image bg ch5battle2 = "ch5battle2"
image bg ch5battle3 = "ch5battle3"
image bg ch5battle4 = "ch5battle4"
image bg ch5battle5 = "ch5battle5"
image bg ch5battle6 = "ch5battle6"
image bg ch5battle7 = "ch5battle7"
image bg ch5battle8 = "ch5battle8"
image bg ch5battle9 = "ch5battle9"
image bg ch5battle10 = "ch5battle10"
image bg ch5battle11 = "ch5battle11"
image bg ch5battle12 = "ch5battle12"
image bg ch5battle13 = "ch5battle13"
image bg ch5battle14 = "ch5battle14"
image bg ch5battle15 = "ch5battle15"
image bg ch5battle16 = "ch5battle16"
image bg ch5battle17 = "ch5battle17"
image bg ch5battle18 = "ch5battle18"
image bg ch5battle19 = "ch5battle19"
image bg ch5battle20 = "ch5battle20"
image bg ch5battle21 = "ch5battle21"
image bg ch5battle22 = "ch5battle22"
image bg ch5battle23 = "ch5battle23"
image bg ch5battle24 = "ch5battle24"
image bg ch5battle25 = "ch5battle25"
image bg ch5battle26 = "ch5battle26"
image bg ch5battle27 = "ch5battle27"
image bg ch5battle28 = "ch5battle28"
image bg ch5battle29 = "ch5battle29"
image bg ch5battle30 = "ch5battle30"
image bg ch5battle31 = "ch5battle31"
image bg ch5battle32 = "ch5battle32"
image bg ch5battle33 = "ch5battle33"
image bg ch5battle34 = "ch5battle34"
image bg ch5battle35 = "ch5battle35"
image bg ch5battle36 = "ch5battle36"
image bg ch5battle37 = "ch5battle37"
image bg ch5battle38 = "ch5battle38"
image bg ch5battle39 = "ch5battle39"
image bg ch5battle40 = "ch5battle40"
image bg ch5battle41 = "ch5battle41"
image bg ch5battle42 = "ch5battle42"
image bg ch5battle43 = "ch5battle43"
image bg ch5battle44 = "ch5battle44"
image bg ch5battle45 = "ch5battle45"
image bg ch5battle46 = "ch5battle46"
image bg ch5battle47 = "ch5battle47"
image bg ch5battle48 = "ch5battle48"
image bg ch5battle49 = "ch5battle49"
image bg ch5battle50 = "ch5battle50"
image bg ch5battle51 = "ch5battle51"
image bg ch5battle52 = "ch5battle52"
image bg ch5battle53 = "ch5battle53"
image bg ch5battle54 = "ch5battle54"
image bg ch5battle55 = "ch5battle55"
image bg ch5battle56 = "ch5battle56"
image bg ch5battle57 = "ch5battle57"
image bg ch5battle58 = "ch5battle58"
image bg ch5battle59 = "ch5battle59"
image bg ch5battle60 = "ch5battle60"
image bg ch5battle61 = "ch5battle61"



label ch5battle:
    stop music fadeout 2.0
    scene black with Dissolve(1)
    show bg ch5battle5 with dissolve
    if "ch5gloriamad" in extraevents:
        p "(Why the hell did I let my hands wander like that... Fucking idiot...)"
    else:
        p "(Finally, some food. I haven't eaten much since yesterday. Pfft, brunch...)"

    n "Down the hallway, shuffling can be heard"
    play music audio.stress fadein 2.0 fadeout 2.0
    show bg ch5battle4 with dissolve
    p "Fuck!"
    "Police Bot" "Target Acquired. Engaging."
    show bg ch5battle1 with dissolve
    "The door squeaks open"
    e "But that singing voice! You may want to just stay on the guitar."
    g "I can't be that-"
    show bg ch5battle2 with dissolve
    p "Guys! Hide!"
    e "Wait, what?!"
    show bg ch5battle3 with dissolve
    p "Fucking hide now! They found us."
    g "Already?"
    g "But where do we hide!"
    p "Anywhere!"
    show bg ch5battle6 with dissolve
    e "Come on, Gloria, under the bed!"
    g "That's the first place they'll look!"
    show bg ch5battle8 with dissolve
    $ renpy.pause(1)
    show bg ch5battle9 with dissolve
    p "Good, stay there. Just stay under cover."
    e "[p], I can help."
    p "Don't argue with me, not right now."
    show bg ch5battle7 with dissolve
    e "[p], how the fuck did I let you sucker me into this?"
    p "Because you know it's right. Protect her, Ellen."
    show bg ch5battle10 with dissolve
    p "(Come on, what are you waiting for?)"
    n "More commotion, along with voices, can be heard outside the door"
    show bg ch5battle11 with dissolve
    j "[p], we know you're in there. You know how this works, so please make this simple and come out."
    p "Sonja, how the hell did you find us so quick?"
    if "ch1ellen" in extraevents:
        j "We found out your fuck buddy was missing. Asked some of her bandmates. Some weird dude named Thor just flat out told us. Didn't even have to pay him!"
    else:
        j "We found out your fixer was missing. Asked some of her bandmates. Some weird dude named Thor just flat out told us. Didn't even have to pay him!"
    e "Thor, you fucking imbecile."
    j "Okay, take it down."
    play sound audio.metalcrash
    show bg ch5battle12 with quickflash
    n "With a ringing clang, the steel door smashes onto the floor"
    j "More of these dumbass bots are on their way, [p]. Just let us finish this job, then we can all go home."
    p "..."
    show bg ch5battle13 with dissolve
    $ insult = renpy.random.choice(insults)
    j "[p], you [insult]. Don't cause any trouble, we're com-"
    play sound audio.smg
    show bg ch5battle14 with hpunch
    p "Sonja, fuck off!"
    show bg ch5battle15 with dissolve
    j "Yeah, you kind of got your point across."
    p "Sonja, it's Caracas all over again. You need to understand! We can't take her to Meredith."
    show bg ch5battle17 with dissolve
    j "That's impossible, [p]!"
    p "Sonja, you have to believe me, it is and she's proof!"
    j "[p]... Please..."
    t "He's fucking lying, Sonja. Trying to get into your head."
    show bg ch5battle16 with dissolve
    j "Would you shut the fuck up, Tex."
    show bg ch5battle18 with dissolve
    t "Fucking, hell. I knew you were a liability!"
    t "Alright, rook, you're going in!"
    show bg ch5battle19 with dissolve
    $ renpy.pause(1)
    play sound audio.smg
    show bg ch5battle20 with hpunch
    n "Your gun lights up as the first Ghost enters the room"
    show bg ch5battle21 with dissolve
    "Ghost" "Arrrgh!!!"
    show bg ch5battle22 with dissolve
    p "Keep 'em coming."
    "Ghost" "My leg! He shot my fucking leg!"
    show bg ch5battle24 with dissolve
    p "Why can't you believe me, Sonja?"
    j "Even if it was true, [p]..."
    p "It fucking is! You have any idea what Vostok will do to her!"
    show bg ch5battle23 with dissolve
    j "Tex, hold up. This isn't right."
    t "Not right?!"
    show bg ch5battle26 with dissolve
    j "I married the jackass. I know when he is lying."
    t "You've grown soft, Sonja. If you won't do it, I will."
    show bg ch5battle27 with dissolve
    $ renpy.pause(1)
    show bg ch5battle28 with dissolve
    p "Shit, Tex, they had to drag you along as well?"
    show bg ch5battle29 with dissolve
    t "It's Charlie, [p]! I'm from fucking Vermont!"
    p "If I called you Charlie, would you turn tail and head back the way you came?"
    t "Not a chance."
    p "Fine then, Brokeback."
    t "Oh, fuck this. Get 'em!"
    play sound audio.smg
    show bg ch5battle30 with dissolve
    p "Fuck me!"
    t "It's over, [p]. Throw your gun down!"
    show bg ch5battle31 with dissolve
    p "Too late for that, Tex."
    t "Come on, man! It's just a job."
    p "Not this time it's not!"


    show bg ch5battle33 with dissolve
    "Ghost" "Now's time for payday. Rook my ass."
    show bg ch5battle34 with dissolve
    e "*Whispers* It's going to be okay, Gloria. Trust me."
    show bg ch5battle35 with dissolve
    e "[p], 10 o'clock!"
    show bg ch5battle36 with dissolve
    "Ghost" "Goddammit!"
    show bg ch5battle37 with dissolve
    $ renpy.pause(1)
    play sound audio.smg
    show bg ch5battle38 with dissolve
    p "Holy shit! Ellen, stay down!"
    show bg ch5battle39 with hpunch
    e "You're fucking welcome!"
    show bg ch5battle41 with dissolve
    p "Just do it!"
    t "You can't stay there forever, [p]."
    show bg ch5battle42 with dissolve
    t "And where is your new friend!"
    h "*Clears throat*"
    show bg ch5battle43 with dissolve
    t "Why did I say anything..?"
    show bg ch5battle44 with dissolve
    play sound audio.puncheffect
    n "Tex's head smashes into the concrete wall"
    show bg ch5battle45 with dissolve
    j "Oh... fuck me."
    h "You never learn."
    show bg ch5battle46 with dissolve
    p "Henry, no!"
    j "I-I knew I should have shot you when I had the chance."
    show bg ch5battle48 with dissolve
    j "MMPPHH!!!!!"
    n "Henry's hand grips tightly around Sonja's face, the pressure of his paw crushing inward"
    show bg ch5battle49 with dissolve
    h "You won't be following us anymore."
    show bg ch5battle47 with dissolve
    p "Henry, stop! That's my wife!"
    show bg ch5battle50 with dissolve
    h "The hell? She's your what?!"
    j "MMMMMPPPHHH!!"
    p "Please..."
    show bg ch5battle51 with hpunch
    play sound audio.guneffect
    j "Oh fuck..."
    show bg ch5battle52 with dissolve
    h "I barely even felt that."
    j "..."
    h "Out of respect for our friend here, I won't kill you."
    show bg ch5battle53 with dissolve
    n "Henry whips Sonja to the floor"
    show bg ch5battle55 with dissolve
    e "This is some prime fucked up shit, now. Fucking Thor..."
    p "Forget Thor. Be thankful they didn't hurt the dumbass."
    g "Wha... What do we do now?"
    show bg ch5battle56 with dissolve
    e "Yeah, [p]. What plan do you have now?"
    p "None... But we have to get out of here. More of them are on the way."
    show bg ch5battle57 with dissolve
    g "It's her..."
    g "Why is she fighting against you?"
    p "Because it's her job, it's what she does."
    g "Well, what do we do with her?"
    menu:
        "Leave her":
            p "Leave her, she's had worse. Henry, lead the way."
        "Put her on the bed":
            $ extraevents.append("ch5sonjabed")
            p "Help me for a second."
            scene black with dissolve
            show bg ch5battle58 with dissolve
            p "You always have to be so stubborn. Damn, I wish you would listen to me just once..."
            if "ch5visitkay" in extraevents:
                p "I should have told your hacker friend everything... Maybe you wouldn't be lying here."
            else:
                p "If you knew everything, maybe you wouldn't be lying here."
            h "[p], we need to go."

    scene black with dissolve
    show bg ch5battle61 with dissolve
    h "Tram tunnels are down this way. We can get anywhere with them. A lot of security, though, so be careful. Gloria, honey, stick close."
    g "Yeah..."
    e "Still mad at me for helping out?"
    p "No. sorry for yelling, you did good."
    e "Hey, you had bullets flying past your head, I get it."
    jump ch5redmoon
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
