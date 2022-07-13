image bg ch3chandrastreet1 = "ch3chandrastreet1"
image bg ch3chandrastreet2 = "ch3chandrastreet2"
image bg ch3chandrastreet3 = "ch3chandrastreet3"
image bg ch3chandrastreet4 = "ch3chandrastreet4"
image bg ch3chandrastreet5 = "ch3chandrastreet5"


image bg ch3chandraapart1 = "ch3chandraapart1"
image bg ch3chandraapart2 = "ch3chandraapart2"
image bg ch3chandraapart3 = "ch3chandraapart3"
image bg ch3chandraapart4 = "ch3chandraapart4"
image bg ch3chandraapart5 = "ch3chandraapart5"
image bg ch3chandraapart6 = "ch3chandraapart6"
image bg ch3chandraapart7 = "ch3chandraapart7"
image bg ch3chandraapart8 = "ch3chandraapart8"
image bg ch3chandraapart9 = "ch3chandraapart9"
image bg ch3chandraapart10 = "ch3chandraapart10"
image bg ch3chandraapart11 = "ch3chandraapart11"
image bg ch3chandraapart12 = "ch3chandraapart12"
image bg ch3chandraapart13 = "ch3chandraapart13"
image bg ch3chandraapart14 = "ch3chandraapart14"
image bg ch3chandraapart15 = "ch3chandraapart15"
image bg ch3chandraapart16 = "ch3chandraapart16"
image bg ch3chandraapart17 = "ch3chandraapart17"
image bg ch3chandraapart18 = "ch3chandraapart18"
image bg ch3chandraapart19 = "ch3chandraapart19"
image bg ch3chandraapart20 = "ch3chandraapart20"
image bg ch3chandraapart21 = "ch3chandraapart21"
image bg ch3chandraapart22 = "ch3chandraapart22"
image bg ch3chandraapart23 = "ch3chandraapart23"
image bg ch3chandraapart24 = "ch3chandraapart24"
image bg ch3chandraapart25 = "ch3chandraapart25"
image bg ch3chandraapart26 = "ch3chandraapart26"
image bg ch3chandraapart27 = "ch3chandraapart27"
image bg ch3chandraapart28 = "ch3chandraapart28"
image bg ch3chandraapart29 = "ch3chandraapart29"
image bg ch3chandraapart30 = "ch3chandraapart30"

image bg ch3chandraapart31 = "ch3chandraapart31"
image bg ch3chandraapart32 = "ch3chandraapart32"
image bg ch3chandraapart33 = "ch3chandraapart33"
image bg ch3chandraapart34 = "ch3chandraapart34"
image bg ch3chandraapart35 = "ch3chandraapart35"
image bg ch3chandraapart36 = "ch3chandraapart36"
image bg ch3chandraapart37 = "ch3chandraapart37"
image bg ch3chandraapart38 = "ch3chandraapart38"
image bg ch3chandraapart39 = "ch3chandraapart39"
image bg ch3chandraapart40 = "ch3chandraapart40"
image bg ch3chandraapart41 = "ch3chandraapart41"
image bg ch3chandraapart42 = "ch3chandraapart42"
image bg ch3chandraapart43 = "ch3chandraapart43"
image bg ch3chandraapart44 = "ch3chandraapart44"
image bg ch3chandraapart45 = "ch3chandraapart45"
image bg ch3chandraapart46 = "ch3chandraapart46"



label ch3chandraapart:
    scene black with Dissolve(2)
    play audio audio.traffic fadein 4.0
    c "It's just up this way."
    show bg ch3chandrastreet1 with dissolve
    if "ch3chandrahelp" in extraevents:
        c "Man, when Josh sees you, he is going to shit bricks."
        p "Chandra. Look at me."
        show bg ch3chandrastreet2 with dissolve
        c "Yeah?"
        p "You need to take this seriously. I said I'll help your friend and I will. I'm not here to start anything. Do you understand me?"
        c "Sure..."
        p "I mean it. If you start something, people {i}will{/i} get hurt. And I can't always control who."
        c "Yeah, [p], I get it."

        scene black with dissolve
        show bg ch3chandrastreet4 with dissolve
        c "Boom. Here we are."
        $ renpy.music.set_volume(0.2, 2.0, 'music')

        play music audio.industrial fadein 2.0 fadeout 2.0
        n "The sound of dampened bass reverberates beyond the doorway"
        p "Lead the way. These are your people, not mine."
        c "Come on then."
        jump ch3apartinside
    else:
        c "This is gonna be great! The look on his face is going to be legendary."
        p "Whose face?"
        show bg ch3chandrastreet3 with dissolve
        c "Uh, your face!"
        p "Bullshit."
        show bg ch3chandrastreet2 with dissolve
        c "It's nothing! You coming, or what?"
        scene black with dissolve
        show bg ch3chandrastreet4 with dissolve

        c "We're here, babe."
        $ renpy.music.set_volume(0.2, 2.0, 'music')
        play music audio.industrial fadein 2.0 fadeout 2.0
        n "The sound of dampened bass reverberates beyond the doorway"
        p "This place looks like a cinder den. What the fuck are you into."
        c "Nothing, just follow me."
        p "And did you call me babe?"
        show bg ch3chandrastreet5 with dissolve
        c "You coming or what?"
        menu:
            "No":
                p "No. You've been lying to me."
                c "The fuck I have!"
                p "Somehow you never mentioned we were going to a cinder den. What happened, did that slip your mind?"
                show bg ch3chandrastreet4 with dissolve
                c "*Stammers* Please... Just come in. You don't have to do anything!"
                c "In and out, I promise."
                menu:
                    "Follow her":
                        p "Fine, but you're going in first."
                        c "Sure..."
                    "Leave":
                        p "Screw this. I wasted enough time on your games, Chandra."
                        c "WAIT!"
                        show ch3chandraapart36 with dissolve
                        p "I'm done with you, you little brat."
                        jump ch3reportalone
            "Fuck it":
                p "Fine, let's go."

        p "(What am I getting into.)"
        jump ch3apartinside

label ch3apartinside:
    stop audio fadeout 2.0
    scene black with dissolve
    $ renpy.music.set_volume(1.0, 2.0, 'music')
    show bg ch3chandraapart1 with dissolve
    c "Well, here we are."
    p "Lovely spot."
    c "Let me check up ahead."
    show bg ch3chandraapart2 with dissolve
    "Unknown Male" "Huh... Chandy? You came back after all."
    c "Shut the fuck up, Kyle."
    "Unknown Male" "Abby totally misses you."
    c "Go back to sleep."
    show bg ch3chandraapart4 with dissolve
    if "ch3chandrahelp" in extraevents:
        p "Is your friend here?"
    else:
        p "What are you doing?"
    c "One sec."
    show bg ch3chandraapart3 with dissolve
    n "A cacophony of raw sex erupts from beyond the curtain, overtaking the music."
    if "ch3chandrahelp" in extraevents:
        p "Well, is she there?"
        show bg ch3chandraapart5 with dissolve
        c "Yeah, jackpot."
        p "So let's get this done. Fast."
    else:
        p "Chandra, what the fuck?!"
        show bg ch3chandraapart5 with dissolve
        c "Quiet! She's in here."
        p "Who is \"She?!\""
        c "Seriously, [p]-"
        p "I know... \"Just follow me.\""

    show bg ch3chandraapart6 with dissolve
    "Unknown Girl" "Oh God! Yes, let me fuck you!"
    "Unknown Man" "There you go, just like that."
    show bg ch3chandraapart7 with dissolve
    "Unknown Man" "You getting wet over there, Abby? You're next!"
    ab "*Stares towards the wall without a response*"
    show bg ch3chandraapart8 with dissolve
    "Unknown Man" "Come on, girl, you need to put that fine ass to use. We could make a killing."
    show bg ch3chandraapart9 with dissolve
    "Unknown Man" "Hell, we can stream that shit. Not many hot milchers around."
    ab "*Glances over at the man, in a dejected state*"

    show bg ch3chandraapart10 with dissolve
    if not persistent.ch3card3:
        $ renpy.notify(['Possible clue', 'alert'])
        show screen hidden_item("ch3card3", "ch3card3", 145, 150, 118, 118)
    c "That ass is mine, Josh, and you can steer clear from it or I'll cut that noodle you call a dick off."
    ab "Chandy..?"
    hide screen hidden_item
    show bg ch3chandraapart11 with dissolve
    "Josh" "What the fuck, Chandra? Rich bitches ain't allowed unless you're here for the high!"
    "Josh" "Go back home to your Mommy!"
    show bg ch3chandraapart12 with dissolve
    c "I don't need my Mommy, I brought my Daddy and if you try anything, he will fuuuuck you up."
    show bg ch3chandraapart13 with dissolve
    if "ch3chandrahelp" not in extraevents:
        p "*Sighs* (Chandra, what did you get me into...?)"
    p "How you doing, Josh, is it?"
    "Josh" "Uhhh... I'm okay... I guess."
    p "Great. Glad to hear it. Let's hope you stay that way."
    "Josh" "Yeah, umm, okay!"
    show bg ch3chandraapart14 with dissolve
    c "Abby, babe, you alright?"
    ab "Chandra..?"
    c "Yeah, it's me. Let's get out of here, okay?"
    show bg ch3chandraapart15 with dissolve
    ab "I like it here. Josh promised me some cinder if I..."
    c "Damn, Abby, how much did you take?"
    ab "How much did I take? I took... lots."
    show bg ch3chandraapart16 with dissolve
    if "ch3chandrahelp" not in extraevents:
        p "Well, it all makes sense now."
    c "Help me move her."
    p "Yeah, of course."
    c "Come on, upsie-daisy!"
    show bg ch3chandraapart17 with dissolve
    c "Ohhh, hold on to me. I got ya."
    c "There, careful. Stay with me."
    show bg ch3chandraapart18 with dissolve
    c "Thank you, [p]."
    if "ch3chandrahelp" in extraevents:
        p "Yeah..."
    else:
        "..."
    c "Abby, you probably won't remember this later, but this is, [p]. [p], this my BFF, Abby."
    p "Just move, Chandra..."
    show bg ch3chandraapart19 with dissolve
    if dep > 2:
        "(Why do I let myself get involved in this bullshit? I wasted a lot of time.)"
    else:
        "(How did a rich girl like her even get involved in this shit?)"
    c "One step at a time. Fresh air will do you good."
    scene black with dissolve
    play music audio.darkcalm fadein 2.0 fadeout 2.0
    show bg ch3chandraapart20 with dissolve
    if "ch3chandrahelp" in extraevents:
        c "Again, [p], I mean it. Thanks. I owe you."
        p "She usually like this?"
        c "Not this bad. Fuck..."
        show bg ch3chandraapart22 with dissolve
        p "I don't think she's going to OD or anything, but she needs to lie down. Maybe sleep it off."
        show bg ch3chandraapart23 with vpunch
        ab "*Moans*"
        c "SHIT! ABBY!"
        jump ch3chandranice
    else:
        c "Thanks, [p]..."
        show bg ch3chandraapart22 with dissolve
        p "What the hell was that, Chandra?"
        c "Look, I'm fucking sorry! You wouldn't have helped me otherwise."
        show bg ch3chandraapart21 with dissolve
        p "You don't know that!"
        c "\"Oh, sure, Chandra! Of course, I'll walk into a cinder den to help your junkie milcher friend. Why wouldn't I?\""
        c "All you care about is pussy and money."
        p "Oh, don't you try to manipulate-"
        show bg ch3chandraapart23 with vpunch
        ab "*Moans*"
        c "SHIT! ABBY!"
        show bg ch3chandraapart24 with dissolve
        p "Ummph! "
        c "[p], I..."
        menu:
            "Help her out":
                jump ch3chandranice
            "This is Chandra's problem":
                jump ch3chandramean


label ch3chandramean:
    $ extraevents.append("ch3chandramean")
    $ dep += 1
    p "I've been more than patient this entire fucking time."
    show bg ch3chandraapart26 with dissolve
    p "You're nothing but a manipulative little tramp."
    c "You fuck! I thought you were different!"
    p "Then why didn't you just ask me? She's your problem. Deal with it."
    show bg ch3chandraapart27 with dissolve
    c "You really are a prime ass discharge. I fucking hope you die."
    p "Yeah, yeah... You may get your wish soon enough."
    show bg ch3chandraapart36
    p "Fuck this. I got shit to do. Glad your friend's not dead."
    jump ch3reportalone

label ch3chandranice:
    $ extraevents.append("ch3chandranice")
    $ c_met = True
    $ c_score += 1
    show bg ch3chandraapart24 with dissolve
    p "I gotcha... Chandra, look at me, is there anywhere she can go?"
    c "Not like this."
    p "Where does she live? Does she have a roommate?"
    c "Um... she lives in the hills, with her parents."
    p "She still lives with her parents? Not Mil-town?"
    show bg ch3chandraapart25 with dissolve
    c "Nah, her parents don't give a shit about that. They're cool, unlike most."
    p "Perfect. Taxi!"
    show bg ch3chandraapart28 with dissolve
    c "What the fuck are you doing?!"
    p "Flagging down a cab, help me out! Arms are quite full here."
    show bg ch3chandraapart29 with dissolve
    c "She can't go home like this! Her parents will fucking crucify her!"
    p "In my experience, they absolutely won't. "
    c "This is bullshit, [p]!"
    p "I can't take her to my place, your mom sure as shit won't let her into yours. If we take her to the hospital they will have to report her."
    c "Shit..."
    show bg ch3chandraapart30 with dissolve
    p "You said they were cool, right?"
    c "Yeah..."
    p "And if she's your best friend, they have to be used to some crazy shit."
    c "I guess."
    p "And they stood by her, even after she turned?"
    c "Yeah, they even told Mom to get jacked when she offered to put Abby in a clinic. They said her horns were as beautiful as she was."
    p "I like them already, Chandra. I wish I had support like that. Now, get that cab."
    show bg ch3chandraapart31 with dissolve
    c "Fuck, Abby, you are gonna be pissed at me. *Whistles and waves out to the road.*"
    show bg ch3chandraapart32 with dissolve
    c "Here, damn... This is fucked up."
    p "The whole world is. But you did right by her, kid. Wish you went about it a little different."
    show bg ch3chandraapart33 with dissolve
    c "It worked, didn't it?"
    p "Barely. Help me put her in."
    show bg ch3chandraapart34 with dissolve
    n "Chandra gives the cab a name and address."
    show bg ch3chandraapart35 with dissolve
    c "She is going to hate me for this."
    p "For a while. She'll get over it."

    $ achievement.grant("JUSTSAYNO")
    init:
        $ achievement.register("JUSTSAYNO")
    $ achievement.Sync()

    show bg ch3chandraapart37 with dissolve
    c "So what now?"
    if c_score >= 2:
        menu:
            "I have to go":
                jump ch3chandraapartleave
            "I still have time":
                jump ch3chandraaparttime

    jump ch3chandraapartleave

label ch3chandraaparttime:
    if "ch1chandra" in extraevents:
        p "How is it you always find a way to pull me away from my work?"
        c "I'm just that fucking hot?"
        p "That fucking annoying."
        c "Don't tell me you didn't have fun last time."
        p "Oh, I did. What about you?"
        show bg ch3chandraapart43 with dissolve
        c "I barely remember it, but I'm like 90%% sure I did."
    else:
        p "Heh, You always show up at the worst times. You know that?"
        show bg ch3chandraapart43 with dissolve
        c "The life of a Ghost, always fucking busy."
    p "Well, I've already wasted this much time... want to waste some more?"
    show bg ch3chandraapart44 with dissolve
    c "I think I might be willing to spend some time with the big old hero."
    p "Old?"
    show bg ch3chandraapart45 with dissolve
    c "Shut up. How far is your place?"
    p "Don't you know?"
    show bg ch3chandraapart46 with dissolve
    c "Actually..."
    p "You little minx... I can't believe I fell for that."
    p "You're just full of surprises tonight."
    show bg ch3chandraapart42 with dissolve
    c "You haven't seen anything yet."
    jump ch3chandra

label ch3chandraapartleave:
    p "I have to get back home."
    c "Again, thank you."
    show bg ch3chandraapart36 with dissolve
    p "(Damn, what the hell has she been getting into...)"
    jump ch3reportalone
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
