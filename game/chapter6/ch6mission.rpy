image bg ch6mission1 = "ch6mission1"
image bg ch6mission2 = "ch6mission2"
image bg ch6mission3 = "ch6mission3"
image bg ch6mission4 = "ch6mission4"
image bg ch6mission5 = "ch6mission5"
image bg ch6mission6 = "ch6mission6"
image bg ch6mission7 = "ch6mission7"
image bg ch6mission8 = "ch6mission8"
image bg ch6mission9 = "ch6mission9"
image bg ch6mission10 = "ch6mission10"
image bg ch6mission11 = "ch6mission11"
image bg ch6mission12 = "ch6mission12"
image bg ch6mission13 = "ch6mission13"
image bg ch6mission14 = "ch6mission14"
image bg ch6mission15 = "ch6mission15"
image bg ch6mission16 = "ch6mission16"
image bg ch6mission17 = "ch6mission17"
image bg ch6mission18 = "ch6mission18"
image bg ch6mission19 = "ch6mission19"
image bg ch6mission20 = "ch6mission20"
image bg ch6mission21 = "ch6mission21"
image bg ch6mission22 = "ch6mission22"
image bg ch6mission23 = "ch6mission23"
image bg ch6mission24 = "ch6mission24"
image bg ch6mission25 = "ch6mission25"
image bg ch6mission26 = "ch6mission26"
image bg ch6mission27 = "ch6mission27"
image bg ch6mission28 = "ch6mission28"
image bg ch6mission29 = "ch6mission29"
image bg ch6mission30 = "ch6mission30"
image bg ch6mission31 = "ch6mission31"
image bg ch6mission32 = "ch6mission32"
image bg ch6mission33 = "ch6mission33"
image bg ch6mission34 = "ch6mission34"
image bg ch6mission35 = "ch6mission35"
image bg ch6mission36 = "ch6mission36"
image bg ch6mission37 = "ch6mission37"
image bg ch6mission38 = "ch6mission38"
image bg ch6mission39 = "ch6mission39"
image bg ch6mission40 = "ch6mission40"
image bg ch6mission41 = "ch6mission41"
image bg ch6mission42 = "ch6mission42"
image bg ch6mission43 = "ch6mission43"
image bg ch6mission44 = "ch6mission44"
image bg ch6mission45 = "ch6mission45"
image bg ch6mission46 = "ch6mission46"
image bg ch6mission47 = "ch6mission47"
image bg ch6mission48 = "ch6mission48"
image bg ch6mission49 = "ch6mission49"
image bg ch6mission50 = "ch6mission50"
image bg ch6mission51 = "ch6mission51"
image bg ch6mission52 = "ch6mission52"
image bg ch6mission53 = "ch6mission53"
image bg ch6mission54 = "ch6mission54"
image bg ch6mission55 = "ch6mission55"
image bg ch6mission56 = "ch6mission56"
image bg ch6mission57 = "ch6mission57"
image bg ch6mission58 = "ch6mission58"
image bg ch6mission59 = "ch6mission59"
image bg ch6mission60 = "ch6mission60"
image bg ch6mission61 = "ch6mission61"
image bg ch6mission62 = "ch6mission62"
image bg ch6mission63 = "ch6mission63"
image bg ch6mission64 = "ch6mission64"
image bg ch6mission65 = "ch6mission65"
image bg ch6mission66 = "ch6mission66"
image bg ch6mission67 = "ch6mission67"
image bg ch6mission68 = "ch6mission68"
image bg ch6mission69 = "ch6mission69"
image bg ch6mission70 = "ch6mission70"
image bg ch6mission71 = "ch6mission71"
image bg ch6mission72 = "ch6mission72"
image bg ch6mission73 = "ch6mission73"
image bg ch6mission74 = "ch6mission74"
image bg ch6mission75 = "ch6mission75"
image bg ch6mission76 = "ch6mission76"
image bg ch6mission77 = "ch6mission77"
image bg ch6mission78 = "ch6mission78"
image bg ch6mission79 = "ch6mission79"
image bg ch6mission80 = "ch6mission80"
image bg ch6mission81 = "ch6mission81"


image ch6citymorning = Movie(play='video/chapter-6-video/ch6citymorning.webm', loop=False)
image bg ch6citymorningmovie movie:
    "ch6citymorning"
    pause 14.0

image ch6missionpan = Movie(play='video/chapter-6-video/ch6missionpan.webm', loop=False)
image bg ch6missionpanmovie movie:
    "ch6missionpan"
    pause 8.0
    "ch6missionpanend"


image ch6missionpan2 = Movie(play='video/chapter-6-video/ch6missionpan2.webm', loop=False)
image bg ch6missionpan2movie movie:
    "ch6missionpan2"
    pause 10.0
    "ch6missionpan2end"


label ch6mission:
    scene black with Dissolve(1)
    play music audio.prepare fadein 2.0 fadeout 2.0
    show bg ch6citymorningmovie movie with Dissolve(2)
    n "The two set off on their next goal, finally hoping for a change in fortune"
    show bg ch6mission8 with Dissolve(2)
    p "Well, is this the spot?"
    show bg ch6mission1 with dissolve
    h "Yeah, it should be, according to Betty and it looks like someone's home."
    show bg ch6mission2 with dissolve
    p "Seems pretty quiet."
    h "Yeah, I don't trust quiet."
    show bg ch6mission3 with dissolve
    p "We're dealing with Bolters here, not hardened Ghosts or a damn Red Moon."
    p "The yahoos are probably passed out inside."
    show bg ch6mission5 with dissolve
    h "Don't underestimate them. They're impressive in their own way."
    p "How's that?"
    show bg ch6mission6 with dissolve
    h "They survive."
    p "Yeah, on the backs of others."
    show bg ch6mission7 with dissolve
    h "Sounds familiar."
    menu:
        "Whatever":
            p "What I do is legal. These asswipes are dredges."
            show bg ch6mission6 with dissolve
            h "Correction. What you did... We're no different from them now."
            menu:
                "Agree":
                    $ h_score += 1
                    p "*Sighs* You got a point. But, I still have my code."
                    show bg ch6mission7 with dissolve
                    h "Heh, so do they. Just works a bit different. Let's just try to not kill anyone, alright?"
                    p "I should be telling you that."
                "Disagree":

                    p "They are cheats, liars and worse."
                    h "Not much different than the corporate suits who give you your jobs."
                    p "... Point."
                    show bg ch6mission5 with dissolve
                    h "*Grumbles* Let's just try to not kill anyone."
                    p "No promises."
        "Want another shiner?":

            p "Don't make me give you a matching pair."
            show bg ch6mission4 with dissolve
            h "Heh, you can try."
            p "Yeah, screw that. Shit, how hard did he hit you anyway?"
            show bg ch6mission6 with dissolve
            h "Hard enough to take your head off."
            p "I get the impression you're not exaggerating."
            h "I'm not. Now, why don't we stick to the matter at hand?"
            p "Right, when we go in, try not to crush anyone's head. What is it with you and that anyway?"
            show bg ch6mission5 with dissolve
            h "Best way to truly kill one of those Red Moon bastards."
            p "Great... Come on, no more time to waste."

    scene black with dissolve
    show bg ch6mission9 with dissolve
    p "Alright, Sam. Talk to me."
    s "Two individuals detected inside, Sir."
    p "Just two?"
    show bg ch6mission10 with dissolve
    s "Yes, with both audio and thermal verification, at the northwest side of the complex."
    p "Perfect, Sam. Thank you."
    show bg ch6mission11 with dissolve
    p "Looks like it's our lucky day, Sam says there are only two inside. You ready?"
    h "Yeah, let's get this over with."
    jump ch6missioninside


label ch6missioninside:
    show bg ch6mission12 with dissolve
    p "*Whispering* What a shithole."
    h "*Whispering* I've seen worse."
    p "Come on, let's look around."
    $ resetmenu()
    jump ch6missioninsidemenu

label ch6missioninsidemenu:
    menu:
        "Near door":
            jump ch6missionnear
        "Cell door":
            jump ch6missioncell
        "Far door":
            jump ch6missionfar


label ch6missionnear:
    show bg ch6mission13 with dissolve
    h "Any idea what this place is?"
    p "Looks like a small abandoned police station."
    show bg ch6mission14 with dissolve
    p "I can't see much..."
    h "We can check around more if you want."
    menu:
        "Go inside":
            jump ch6missionnearroom
        "Look around more":
            show bg ch6mission12 with dissolve
            jump ch6missioninsidemenu

label ch6missioncell:
    show bg ch6mission15 with dissolve
    if not persistent.ch6card2:
        $ renpy.notify(['Possible clue', 'alert'])
        show screen hidden_item("ch6card2", "ch6card2", 315, 648, 746, 254)
    h "Anything?"
    p "Looks like I found Glenn's new living space. Minimalist would be putting it kindly."
    if persistent.ch6card2:
        h "Hey, what's that you found?"
        p "Oh... Umm, it's nothing."
        h "Okay..."
    p "Let's look around a bit more."
    hide screen hidden_item
    show bg ch6mission12 with dissolve
    jump ch6missioninsidemenu

label ch6missionfar:
    $ menu2 = False
    p "They must be up here."
    show bg ch6mission16 with dissolve
    h "You see anything?"
    p "One sec."
    show bg ch6mission65 with Dissolve(1)
    h "So?"
    p "Can barely see a thing, but there they are."
    h "Is it the target?"
    p "I think so."
    show bg ch6mission18 with dissolve
    h "I think I can get through that pretty quick."
    menu:
        "Do it":
            h "Alright, step aside."
            show bg ch6mission78 with dissolve
            h "On three."
            h "One."
            h "Two."
            play sound audio.metalcrash
            show bg ch6mission79 with hpunch
            h "THREE!"
            show bg ch6mission81 with dissolve
            sa "WHAT THE...?"
            show bg ch6mission80 with dissolve
            h "Keep away from him!"
            jump ch6missionroomsurprise
        "Hold Up":


            p "Not yet, there may be another way."
            show bg ch6mission17 with dissolve
            h "How about in here?"
            p "Sounds good."
            jump ch6missioninsidemenu


label ch6missionnearroom:
    show bg ch6mission22 with dissolve

    p "Shit, haven't been on this side of an interrogation room in a long time."
    if menu2 == False:
        h "What are they doing in there?"
    else:
        h "[p], look there. I think we found our friends. Curious what they're up to."
    p "Hard to say. A good deal of equipment there."
    show bg ch6mission21 with dissolve
    p "The one of the left looks like our guy."
    h "And on the right? Doesn't look like his girlfriend."
    show bg ch6mission20 with dissolve
    p "One of our Bolters. Curious why she is alone."
    show bg ch6mission24 with dissolve
    h "Does it matter? We have her outnumbered. The glass is tempered, but it shouldn't be a problem to break through and surprise her."
    p "A little shock and awe then? Take her by surprise?"
    h "Unless you have a better idea?"
    menu:
        "Do it":
            p "Do it, but fast, she has a weapon."
            h "Don't you worry about that."
            show bg ch6mission38 with dissolve
            n "Henry heaves back with his fist and thrusts it forward"
            play sound audio.shatter
            show bg ch6mission39 with hpunch
            n "His fist plunges through the tempered glass, sending shattered fragments into the room as they rush in"
            show bg ch6mission66 with dissolve
            sa "What the!?"
            jump ch6missionroomsurprise
        "Wait and watch":
            jump ch6missionwatch


$ bolter = "Bolter"


label ch6missionwatch:
    p "Hold up. More intel never hurts."
    h "No argument from me."
    scene black with dissolve
    show bg ch6mission19 with Dissolve(1)
    "Bolter" "Better?"
    gl "Huh?"
    "Bolter" "That my friends are gone? No more big scaries."
    gl "..."
    "Bolter" "Do I still scare you?"
    gl "No..."
    show bg ch6missionpanmovie movie with dissolve
    "Bolter" "Oh, now-now. It's okay, just get us in that system. The boys will be pretty appreciative if it's done when they get back!"
    "Bolter" "You do that and they will be mad grateful. And Bolters know how to thank right!"
    gl "..."
    show bg ch6mission27 with dissolve
    "Bolter" "Damn, you are a quiet one now? My little bro is just like you, always drowning in a VR set playing Castle Quest or whatever."
    gl "Castle Conquest. Hey, did you know I got the Talismen of Hadur?"
    "Bolter" "I did not! Very prime! But, I have no idea what that is, babydoll."
    show bg ch6mission26 with dissolve
    "Bolter" "Hey, now that I think on it. I got a game that we can play. Keep you motivated."
    gl "..."
    show bg ch6mission28 with dissolve
    "Bolter" "Don't worry I got a good one for ya. It involves something pointy."
    p "What's she doing?"
    h "I don't know, but if I think she is going to hurt him, I'm going in there."
    show bg ch6mission29 with dissolve
    "Bolter" "Now, you see, babydoll... can I call you babydoll?"
    gl "..."
    "Bolter" "The games the boys play get all competitive. People get hurt. I don't think you would like them."
    "Bolter" "You're a nice boy, so there's a different game we can play. I think you'll like it more."
    show bg ch6mission30 with dissolve
    "Bolter" "I see you trying hard to look at me."
    gl "..."
    "Bolter" "Aww, it's okay, babydoll. I like that you want to play. Even if you never have before."
    gl "I ha-"
    show bg ch6mission31 with dissolve
    "Bolter" "With people? Real people?"
    show bg ch6mission32 with dissolve
    "Bolter" "Now, Sesh says he likes this view. How about you?"
    gl "..."
    "Bolter" "Yeah, you do."
    show bg ch6mission33 with dissolve
    "Bolter" "Don't stare too hard, the game is just starting."
    show bg ch6mission34 with dissolve
    "Bolter" "Do what the boys need, then I'll let you touch. Would you like that?"
    show bg ch6mission35 with dissolve
    "Bolter" "Of course he does. So do your thing and we can play the game even more. But if not?"
    "Bolter" "Pity pity."
    show bg ch6mission36 with dissolve
    "Bolter" "Then you will have to play with the boys.."
    show bg ch6mission37 with dissolve
    h "Alright, enough of this."
    p "No, Henry wait!"
    show bg ch6mission38 with dissolve
    $ renpy.pause(1)
    play sound audio.shatter
    show bg ch6mission39 with hpunch
    n "Henry's fist plunges through the tempered glass, sending shattered fragments into the room as they rush in"
    show bg ch6mission41 with dissolve
    "Bolter" "What the fuck!?"
    show bg ch6mission42 with dissolve
    h "Get your hands off him!"
    show bg ch6mission43 with dissolve
    "Bolter" "Back off, big man! Or I give him a red necklace!"
    show bg ch6mission48 with dissolve
    $ renpy.pause(1)
    show bg ch6mission49 with dissolve
    p "Alright, big guy, hold up. We can talk this through like proper adults. Right?"
    "Bolter" "You're making a huge mistake, you know that?"
    p "I seem to be making lots of those lately. Just add another to the pile."
    show bg ch6mission75 with dissolve
    h "Don't trust anything she says."
    p "I'll decide on that."
    show bg ch6mission49 with dissolve
    p "Now as for you..."
    $ resetmenu()
    jump ch6missionintermenu



init python:
    def ch6interimage(int):
        if int == 0:
            renpy.transition(dissolve)
            renpy.show("bg ch6mission47")
        if int == 1:
            renpy.transition(dissolve)
            renpy.show("bg ch6mission44")
        if int == 2:
            renpy.transition(dissolve)
            renpy.show("bg ch6mission46")
        if int == 3:
            renpy.transition(dissolve)
            renpy.show("bg ch6mission45")


label ch6missionintermenu:

    if sa_int >= 4:
        jump ch6missionintersurrender
    elif sa_int <= -1:
        jump ch6missionintershoot

    if menu1 == False and menu2 == False and menu3 == False and menu4 == False and menu5 == False and menu6 == False and menu7 == False:
        sa "This has gone on long enough..."
        if sa_int > 2:
            jump ch6missionintersurrender
        else:
            jump ch6missionintershoot


    menu:
        "Ask her name" if menu1:
            $ menu1 = False
            jump ch6intername
        "Why are you alone?" if menu2:
            $ menu2 = False
            jump ch6interalone
        "Why do this?" if menu3:
            $ menu3 = False
            jump ch6interwhy
        "Calm her" if menu4:
            $ menu4 = False
            jump ch6intercalm
        "Threaten her" if menu5:
            $ menu5 = False
            jump ch6interthreat
        "Threaten her with Henry" if menu6:
            $ menu6 = False
            jump ch6interhenry

label ch6intername:
    $ sa_int += 1
    p "Let's try to take things down a notch. My name is [p], and you are?"
    $ ch6interimage(sa_int)
    sa "Wait, what?"
    $ sa_name = "Sasha"
    p "Your name. If we're going to talk, I'd rather not refer to you as \"Hey You.\""
    sa "Sasha, just call me Sasha."
    p "Good, now that is out of the way. Okay, let's talk this over."
    jump ch6missionintermenu

label ch6interalone:
    p "So, where are your friends?"
    sa "Coming in a hot second. You're going to wish-"
    p "No, they're not here, whole building is clean. Again, where are they?"
    sa "Those fucking clowns..."
    menu:
        "Bolters, what else...":
            p "Shit, you didn't know, did you?"
            sa "Told them to leave me alone, took me too seriously."
            p "They're bolters, if you expected backup, that's on you."
            $ sa_int -= 1
            $ ch6interimage(sa_int)
            sa "Quit spewing shit! Bolters always look out for each other. Not like you outsiders."
            p "How's that working out for you?"
        "Need better friends":
            $ sa_int += 1
            $ ch6interimage(sa_int)
            p "Maybe you need to pick some smarter friends. Let me guess, they left you here to go get high?"
            sa "Exactly! They're loyal, but lacking on the IQ scale."
            p "I know I would have at least left some backup."
            sa "That's what I told them."
    jump ch6missionintermenu

label ch6interwhy:
    p "What do you want with him anyway?"
    if sa_int >= 2:
        $ ch6interimage(sa_int)
        sa "You tell me first."
        p "I'm not the one who brought a knife to a gunfight."
        sa "*Sighs* We need IDs, real ones. No docs means no meds, no school."
        p "You're telling me you want a degree? Why do I doubt that?"
        sa "My little bro. He's smart. So smart he should be living the high life. Right now, he can't get beyond basic ed."
        $ sa_int += 1
        $ ch6interimage(sa_int)
        sa "I mean what's an older sister for?"
    else:
        $ ch6interimage(sa_int)
        $ sa_int -= 1
        sa "Why should I tell you?"
        p "Uh, because I'm the one that brought a gun to a knife fight."
        $ ch6interimage(sa_int)
        sa "Then shoot me already, tired of hearing this bullshit."
    jump ch6missionintermenu

label ch6intercalm:
    p "Let's just calm down."
    $ ch6interimage(sa_int)
    if sa_int < 1:
        sa "Calm down? You're not the one standing in front of a gun and that massive fella!"
        p "Point taken..."
    else:
        $ sa_int += 1
        $ ch6interimage(sa_int)
        $ extraevents.append("ch6missionhenrythreat")
        sa "I can be calm, just keep that freak away from me."
        p "Well you did threaten his family, but I think he might be willing to do that."
        p "How about it Henry?"
        h "I'll think about it."
        p "Best I can do."
        sa "Since he gonna kill me, can you at least lower the gun?"
        p "He's a big teddy bear once you get to know him. As for the gun, sorry, no can do."
    jump ch6missionintermenu


label ch6interthreat:
    p "Let me make this clear, you hurt him, I'm dropping you. Do you understand?"
    $ ch6interimage(sa_int)
    sa "Do your worst, mask. I can take him out fast."
    menu:
        "Doubtful":
            $ sa_int -= 1
            p "Not that fast. You'll be on the floor as soon as that knife nicks his skin. I don't miss."
            sa "I'll take my chances."
        "Worth it?":

            p "You hurt him, you go down. For good. You willing to take that chance?"
            $ sa_int += 2
            $ ch6interimage(sa_int)
            sa "Fuck me... Just why in the prime fuck are you guys here anyway?"
            p "Same as you, we want to have a chat with old Glenn here."
            sa "Dude is in high demand."
    jump ch6missionintermenu



label ch6interhenry:
    p "You know, if you keep giving us trouble, I'll sic this guy on ya."
    show bg ch6mission75 with dissolve
    if "ch6missionhenrythreat" in extraevents:
        sa "Hey, you promised he'd back off!"
        p "I said I'd ask him to think about it."
        h "I thought about it."
    else:
        p "You have no idea what he can do to a skull. I still have nightmares."
        h "..."
    sa "What? Why is he staring at me like that?"
    p "Oh, I know that look. Have any next of kin?"
    if sa_int < 2:

        $ sa_int -= 1
        $ ch6interimage(sa_int)
        sa "If you were going to do something, you would have done it by now!"
    else:
        $ sa_int += 1
        sa "Who the fuck {i}are{/i} you two?"
    jump ch6missionintermenu


label ch6missionroomsurprise:
    $ extraevents.append("ch6missionsurprise")
    show bg ch6mission67 with dissolve
    n "The woman crashes into the ground, as her knife slides across the floor"
    h "Amateurs."
    show bg ch6mission68 with dissolve
    sa "Ugh... Who the..."
    h "Stay right where you are."
    show bg ch6mission69 with dissolve
    sa "Fuck that noise!"
    show bg ch6mission70 with dissolve
    sa "Well... Ummm... Shit? I guess..?"
    show bg ch6mission73 with dissolve
    h "Show's over. Just keep nice and still."
    p "I'd listen to him. Hell, this is the most well-mannered I have seen him in days."
    show bg ch6mission71 with dissolve
    sa "Umm... look, I don't know what you want, but don't lay a finger on me."
    p "We just want Glenn."
    show bg ch6mission72 with dissolve
    sa "*Sighs in relief* Those two assholes just had to leave me alone, didn't they... Priming fuck, we're almost done!"
    p "Not my problem. He's ours now."
    sa "Can we have him back, once-?"
    show bg ch6mission56 with dissolve
    gl "I'm in. Just need to..."
    sa "Shit! For real? Please let him finish!"
    show bg ch6mission57 with dissolve
    gl "Okay, all done. So, are you rescuing me?"
    p "Umm, more like kidnapping, actually."
    gl "Oh... I guess it could be worse."
    show bg ch6mission72 with dissolve
    sa "If he's done, then, by all means, take him. Just leave me alone, mask."
    show bg ch6mission74 with dissolve
    h "What do we do with her?"
    p "Good question."
    show bg ch6mission72 with dissolve
    sa "I don't need him anymore, take him and go."
    p "Pleasure doing business with you."
    show bg ch6mission57 with dissolve
    gl "So, where are you kidnapping me to?"
    p "Just follow us."
    jump ch6ellen

label ch6missionintershoot:
    $ extraevents.append("ch6missionshoot")
    sa "No, fuck this!"
    p "Wait!"
    play sound audio.guneffect
    show bg ch6mission52 with vpunch
    n "The blast goes off in the room, leaving you with a ringing echo in your ears"
    show bg ch6mission53 with dissolve
    h "Goddammit, [p]!"
    p "I had no choice!"
    show bg ch6mission76 with dissolve
    h "Please tell me that wasn't a real round?"
    p "Blunter round... Still, at that range, she is going to be out for a while."
    show bg ch6mission77 with dissolve
    h "Well, she'll live. Now, what about him?"
    show bg ch6mission55 with dissolve
    p "Hey, Glenn, right? Are you okay?"
    gl "You interrupted me. Almost done."
    p "Hey, we need to go."
    show bg ch6mission56 with dissolve
    gl "And... done."
    show bg ch6mission54 with dissolve
    gl "So, are you rescuing me?"
    p "Umm, more like kidnapping, actually."
    gl "Oh... I guess it could be worse."
    show bg ch6mission76 with dissolve
    h "Not to interrupt, [p], but we need to go."
    p "Agreed, let's get out of here before her friends come back."
    jump ch6ellen


label ch6missionintersurrender:
    $ extraevents.append("ch6missionsurrender")
    show bg ch6mission50 with dissolve
    $ achievement.grant("STAYCALM")
    init:
        $ achievement.register("STAYCALM")
    $ achievement.Sync()

    sa "Fuck, they are going to kill me."
    show bg ch6mission51 with dissolve
    sa "But I'll take my chances..."
    p "Thank you for seeing reason, now get those hands over your head."
    show bg ch6mission61 with dissolve
    sa "Under different circumstances, this could be kinda hot."
    p "Yeah, well, it's not."
    show bg ch6mission75 with dissolve
    h "I'd check her for more weapons."
    show bg ch6mission61 with dissolve
    p "He's right. Up against the wall."
    show bg ch6missionpan2movie movie with dissolve
    sa "Forced to be against a wall by two strangers..."
    sa "Yeah, different circumstances for sure."
    show bg ch6mission62 with dissolve
    sa "Not every day you put a strange half-naked girl in this position. Gonna make Sesh jealous."
    p "This isn't going there."
    show bg ch6mission63 with dissolve
    p "She's clean. If she was hiding something else, I'd have no clue as to where."
    sa "Can I turn around now?"
    p "Yeah, go ahead."
    show bg ch6mission64 with dissolve
    sa "You just had to show up now, huh? He was so close."
    p "Sorry, but we need him."
    show bg ch6mission56 with dissolve
    gl "I'm almost in. Inserted your brother's file. Just need a minute."
    sa "Please! Just another minute. If my friends are wasted, they aren't coming back soon."

    p "Fuck, fine..."
    show bg ch6mission60 with dissolve
    sa "Holy shit, he really is!"
    gl "Almost there."
    show bg ch6mission58 with dissolve
    gl "Done!"
    gl "So, are you rescuing me?"
    p "Umm, more like kidnapping, actually."
    gl "Oh... I guess it could be worse."
    show bg ch6mission59 with dissolve
    sa "He did it! Now, be my guest, take him!"
    p "Uh, thanks?"
    show bg ch6mission58 with dissolve
    gl "So, where are you kidnapping me to?"
    p "Just follow us."
    jump ch6ellen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
