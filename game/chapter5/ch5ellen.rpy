
image bg ch5ellen1 = "ch5ellen1"
image bg ch5ellen2 = "ch5ellen2"
image bg ch5ellen3 = "ch5ellen3"
image bg ch5ellen4 = "ch5ellen4"
image bg ch5ellen5 = "ch5ellen5"
image bg ch5ellen6 = "ch5ellen6"
image bg ch5ellen7 = "ch5ellen7"
image bg ch5ellen8 = "ch5ellen8"
image bg ch5ellen9 = "ch5ellen9"
image bg ch5ellen10 = "ch5ellen10"
image bg ch5ellen11 = "ch5ellen11"
image bg ch5ellen12 = "ch5ellen12"
image bg ch5ellen13 = "ch5ellen13"
image bg ch5ellen14 = "ch5ellen14"
image bg ch5ellen15 = "ch5ellen15"
image bg ch5ellen16 = "ch5ellen16"
image bg ch5ellen17 = "ch5ellen17"
image bg ch5ellen18 = "ch5ellen18"
image bg ch5ellen19 = "ch5ellen19"
image bg ch5ellen20 = "ch5ellen20"
image bg ch5ellen21 = "ch5ellen21"
image bg ch5ellen22 = "ch5ellen22"
image bg ch5ellen23 = "ch5ellen23"
image bg ch5ellen24 = "ch5ellen24"
image bg ch5ellen25 = "ch5ellen25"
image bg ch5ellen26 = "ch5ellen26"
image bg ch5ellen27 = "ch5ellen27"
image bg ch5ellen28 = "ch5ellen28"
image bg ch5ellen29 = "ch5ellen29"
image bg ch5ellen30 = "ch5ellen30"
image bg ch5ellen31 = "ch5ellen31"
image bg ch5ellen32 = "ch5ellen32"
image bg ch5ellen33 = "ch5ellen33"
image bg ch5ellen34 = "ch5ellen34"
image bg ch5ellen35 = "ch5ellen35"
image bg ch5ellen36 = "ch5ellen36"
image bg ch5ellen37 = "ch5ellen37"
image bg ch5ellen38 = "ch5ellen38"
image bg ch5ellen39 = "ch5ellen39"
image bg ch5ellen40 = "ch5ellen40"
image bg ch5ellen41 = "ch5ellen41"
image bg ch5ellen42 = "ch5ellen42"
image bg ch5ellen43 = "ch5ellen43"
image bg ch5ellen44 = "ch5ellen44"
image bg ch5ellen45 = "ch5ellen45"
image bg ch5ellen46 = "ch5ellen46"
image bg ch5ellen47 = "ch5ellen47"
image bg ch5ellen48 = "ch5ellen48"
image bg ch5ellen49 = "ch5ellen49"
image bg ch5ellen50 = "ch5ellen50"
image bg ch5ellen51 = "ch5ellen51"
image bg ch5ellen52 = "ch5ellen52"
image bg ch5ellen53 = "ch5ellen53"
image bg ch5ellen54 = "ch5ellen54"
image bg ch5ellen55 = "ch5ellen55"
image bg ch5ellen56 = "ch5ellen56"
image bg ch5ellen57 = "ch5ellen57"
image bg ch5ellen58 = "ch5ellen58"
image bg ch5ellen59 = "ch5ellen59"
image bg ch5ellen60 = "ch5ellen60"
image bg ch5ellen61 = "ch5ellen61"
image bg ch5ellen62 = "ch5ellen62"
image bg ch5ellen63 = "ch5ellen63"
image bg ch5ellen64 = "ch5ellen64"
image bg ch5ellen65 = "ch5ellen65"
image bg ch5ellen66 = "ch5ellen66"
image bg ch5ellen67 = "ch5ellen67"
image bg ch5ellen68 = "ch5ellen68"
image bg ch5ellen69 = "ch5ellen69"
image bg ch5ellen70 = "ch5ellen70"
image bg ch5ellen71 = "ch5ellen71"
image bg ch5ellen72 = "ch5ellen72"
image bg ch5ellen73 = "ch5ellen73"
image bg ch5ellen74 = "ch5ellen74"
image bg ch5ellen75 = "ch5ellen75"
image bg ch5ellen76 = "ch5ellen76"
image bg ch5ellen77 = "ch5ellen77"
image bg ch5ellen78 = "ch5ellen78"
image bg ch5ellen79 = "ch5ellen79"
image bg ch5ellen80 = "ch5ellen80"
image bg ch5ellen81 = "ch5ellen81"
image bg ch5ellen82 = "ch5ellen82"
image bg ch5ellen83 = "ch5ellen83"

image bg ch5ellen84 = "ch5ellen84"
image bg ch5ellen85 = "ch5ellen85"
image bg ch5ellen86 = "ch5ellen86"
image bg ch5ellen87 = "ch5ellen87"
image bg ch5ellen88 = "ch5ellen88"
image bg ch5ellen89 = "ch5ellen89"
image bg ch5ellen90 = "ch5ellen90"
image bg ch5ellen91 = "ch5ellen91"
image bg ch5ellen92 = "ch5ellen92"
image bg ch5ellen93 = "ch5ellen93"
image bg ch5ellen94 = "ch5ellen94"
image bg ch5ellen95 = "ch5ellen95"
image bg ch5ellen96 = "ch5ellen96"
image bg ch5ellen97 = "ch5ellen97"
image bg ch5ellen98 = "ch5ellen98"
image bg ch5ellen99 = "ch5ellen99"
image bg ch5ellen100 = "ch5ellen100"
image bg ch5ellen101 = "ch5ellen101"
image bg ch5ellen102 = "ch5ellen102"
image bg ch5ellen103 = "ch5ellen103"
image bg ch5ellen104 = "ch5ellen104"
image bg ch5ellen105 = "ch5ellen105"
image bg ch5ellen106 = "ch5ellen106"
image bg ch5ellen107 = "ch5ellen107"
image bg ch5ellen108 = "ch5ellen108"
image bg ch5ellen109 = "ch5ellen109"
image bg ch5ellen110 = "ch5ellen110"
image bg ch5ellen111 = "ch5ellen111"
image bg ch5ellen112 = "ch5ellen112"
image bg ch5ellen113 = "ch5ellen113"
image bg ch5ellen114 = "ch5ellen114"
image bg ch5ellen115 = "ch5ellen115"







image ch5ellenpan1 = Movie(play='video/chapter-5-video/ch5ellenpan1.webm', loop=False)
image bg ch5ellenpan1movie movie:
    "ch5ellenpan1"
    pause 9.0
    "ch5ellenpan1end"



label ch5ellen:

    if "ch5visitchandra" not in extraevents or "ch5visitdoc" not in extraevents or "ch5visitkay" not in extraevents:
        s "I should point out, Ellen's is quite far from our current location. It will take some time to get there."
        p "True... so if I go, that's probably it for the night."
        menu:
            "Still head back to Ellen's":
                jump ch5ellengo
            "Rethink this":
                jump ch5locationmenu
    else:
        jump ch5ellengo

label ch5ellengo:
    if "ch5downtown" not in extraevents:
        call ch5driving from _call_ch5driving
        $ extraevents.append("ch5downtown")
    show bg ch5drive12 with dissolve
    p "Sam, lock the car down."
    s "Locking the car down, Sir."
    show bg ch5ellen1 with dissolve
    p "(Well, that took longer than I thought. I hope everyone is okay.)"
    p "(Nothing is on fire, so that's a good sign.)"
    show bg ch5ellen2 with dissolve
    e "It took you long enough."
    p "I'm still working on that punctuality thing."
    show bg ch5ellen5 with dissolve
    e "I keep telling you that you have to act like a professional. It's hard enough getting you to work as is."
    p "Don't think that's going to be an issue anymore."
    e "Where were you?"
    p "I had some stuff to take care of."
    show bg ch5ellen3 with dissolve
    e "Some stuff?"
    p "It's done."
    e "I'm fine, by the way. Gloria's out cold. Henry, too."
    e "The odds on that couch making it through the night, though. Thor's gonna go full-spectrum if that happens."
    p "If anything, say it broke during a party. He'll buy that coming from you."
    show bg ch5ellen4 with dissolve
    e "Broken is one thing. Permanent gigantic ass imprint is another. But..."
    e "Damn it."
    p "What's wrong?"
    e "What's wrong? We're fucked six ways from Sunday, that's what's wrong."
    e "I'm out of work, probably forever. And you're gonna be lucky to make it out of this alive."
    if "ch4vicaccept" in extraevents:
        p "Relax. I've got a plan to make it through this -- both of us."
        show bg ch5ellen5 with dissolve
        e "Great, so we're good. What about Gloria and Henry?"
        p "..."
        e "Why the silence?"
        p "Nothing... Trust me. It's handled."
        e "It better be."
        show bg ch5ellen9 with dissolve
        e "I'm trusting you on this. Don't let me down."
        p "As I said, I fucked this up. I'll unfuck it."
        $ e_score -= 1
        e "..."
        e "You should know better than anyone; once something is fucked, there is no unfucking it."
        p "You know what I mean."
        e "Yeah, I think I do. Fine, fuck it, no use in worrying anyway. Come on."
        p "Where?"
        e "To the van, you need to sleep, right?"
        p "You brought your car? I told you, no tech!"
        e "Relax, it's like your car, grandfathered."
        jump ch5ellenvan
    else:

        p "I know... I didn't plan for any of this, Ellen."
        show bg ch5ellen5 with dissolve
        e "Not used to seeing you without a plan."
        p "And I'm used to having one, so imagine how I feel."
        e "Fuck."
        show bg ch5ellen6 with dissolve
        p "Hey. I got us in this fucked up situation; I'll get us out."
        e "Honestly, that's not what's even bothering me."
        show bg ch5ellen7 with dissolve
        p "Imminent arrest and/or death isn't bothering you? Then what is?"
        e "Nothing. Forget it."
        p "Ellen..."
        show bg ch5ellen8 with dissolve
        e "Anyway, I'm fine. I need a drink. Come on, my van's around the corner."
        p "I said don't bring any tech."
        e "Tech? Ha."
        jump ch5ellenvan

label ch5ellenvan:
    scene black with Dissolve(1)
    $ renpy.pause(0.5)
    show bg ch5ellenpan1movie movie with dissolve
    p "You're right, tech was certainly an overstatement."
    e "A classic, so it's tracker-free. I gutted the inside pretty well, though."
    p "Why even bother?"
    show bg ch5ellen10 with dissolve
    e "Can you not talk shit for at least five minutes?"
    p "Shit is an understatement."
    e "Sorry, don't have a cock to compensate for, so no over the top hot rod that has the steering wheel on the wrong side."
    p "Talk shit about my girl again and we're not friends anymore."
    show bg ch5ellen11 with dissolve
    e "Then I guess you get to sleep in the street, while I put my legs up, down some Jack and laugh at you when it rains."
    p "It's going to rain?"
    e "Fuck if I know, spook. Get in."
    show bg ch5ellen12 with Dissolve(1)
    e "Eating your words yet?"
    p "As the kids would say, it's pretty prime."
    show bg ch5ellen14 with dissolve
    e "[p], I say prime all the fucking time."
    p "I stand by my words."
    e "Ass. Still, it's fucking pr-, sweet, right?"
    p "I have to admit, never judge a book by its cover."
    show bg ch5ellen13 with dissolve
    e "Make yourself comfortable. You can sleep back here. I'll take the front."
    p "Ellen?"
    e "Yeah?"
    p "Are you alright?"
    show bg ch5ellen15 with dissolve
    e "Like I said, [p], I'm fine."
    if e_score >= 1:
        p "No, you're not."
        jump ch5ellencouch
    else:
        show bg ch5ellen14 with dissolve
        e "I said I'm fine. I need some fucking sleep. You're to blame, getting me up at noon like some fucking heathen. Asshole."
        p "Sorry..."
        e "Yeah, yeah. You'll make it up to me eventually."
        show bg ch5ellen43 with dissolve
        p "(Shit...)"
        show bg ch5ellen74 with Dissolve(1)
        p "(Well, let's make do, I guess)"
        p "Lights..."
        show bg ch5ellen75 with dissolve
        if "ch4vicaccept" in extraevents:
            p "(I need to find a way to get Gloria to Victoria. Ellen will understand once it's done. This has to be for the best.)"
        elif "ch4vicgoodbye" in extraevents or "ch4vicsex" in extraevents:
            p "(What the hell am I even doing? I need to come up with something fast or we're all dead.)"
        p "(We'll see what the morning brings.)"
        jump ch5dream

label ch5ellencouch:
    e "Who the fuck are you to tell me what I am?"
    show bg ch5ellen16 with dissolve
    p "Ellen, it's me. I'm not fucking blind."
    e "Fine, park your ass here."
    show bg ch5ellen17 with dissolve
    e "It's just... The last few days have been hard."
    p "I can imagine."
    e "I've been in some shit in my life. I've been arrested, been in fights, protests, even a riot or two. All part of the image, you know?"
    e "And one thing I pride myself on is not looking back, not regretting the things I can't change."
    p "You don't do guilt?"
    e "Fuckin' right, I don't. But, [p]... I'm responsible for this. I almost handed Gloria over to Baynard. Hell, I sent you after her."
    p "You're too hard on yourself, you know that?"
    e "Fuck that! Like you're not ten times worse than me."
    p "Point. So how about we both lay off our past mistakes."
    e "Yeah, when you figure out how, let me know."
    if "ch2chooseellen" in extraevents:
        p "And just so we're out in the open here. I am sorry for dragging you to see Alexis Conner."
        show bg ch5ellen18 with dissolve
        e "You should be. But, I DID say yes... eventually. And I knew it was a bad idea."
        p "I backed you into a corner and I didn't even..."
        e "It's done. Over, and. But what's not is that scared girl in there. We can't let her down."
        p "I'll do what I can."
    else:
        p "Guessing seeing Gloria again brought back some old memories."
        show bg ch5ellen18 with dissolve
        e "Yeah, good and bad. Gonna try to focus on the good ones. Not the ones with her dad."
        p "Hey, we'll figure it out."
    show bg ch5ellen19 with dissolve
    e "I know you'll try, but you have to do better. No matter what happens, we have to fix this. Gloria's been through enough shit."
    p "So have you, we all have."
    e "We're not the important ones here."
    p "Umm, thanks, I guess."
    play music audio.visitors fadein 5.0 fadeout 5.0

    show bg ch5ellen21 with dissolve
    e "Well, it's true. Here's hoping things don't go sideways like they always do."
    p "Oh, come on. Since when?"
    show bg ch5ellen20 with dissolve
    e "Ha, gee, let me think. Since forever."
    e "The Spitzer pick up? Definition of sideways."
    p "No one else could have gotten that done."
    e "You're not wrong, but it was still sideways."
    p "Fine, name one other time."
    show bg ch5ellen19 with dissolve
    e "Only one, fuck it. If I'm gonna school you, I need some solvent."
    p "You need some what?"
    e "Turpentine. Or close enough to it."
    show bg ch5ellen22 with dissolve
    e "There you are."
    show bg ch5ellen23 with dissolve
    e "This shit is as old as me. Kicks like a mule."
    p "With everything that's going on, you think now is the best time?"
    show bg ch5ellen24 with dissolve
    e "Fuck yeah, I do!"
    n "Ellen takes a large swig from the bottle, downing it effortlessly"
    show bg ch5ellen25 with dissolve
    e "Feel that burn! That's what I'm talking about. Come on, join me."
    p "You know I toned that crap down."
    e "Shit. Sorry. I keep forgetting."
    menu:
        "Ah, fuck it, pass it over":
            $ extraevents.append("ch5drink")
            $ dep += 1
            p "Then again, we might all be dead tomorrow."
            e "Hey, don't make me be the one that knocks you off the wagon."
            p "Hell, not like I go to meetings or anything, just wasn't fun anymore."
            show bg ch5ellen26 with dissolve
            e "You sure, [p]?"
            p "Yeah yeah, Ellen. Now hand it over."
            show bg ch5ellen31 with dissolve
            p "Gah! Holy hell, it has been a while."
            e "Oh come on, don't puss out on me now."
            p "Just need a second, relax."
            show bg ch5ellen33 with dissolve
            e "It makes me think. When was the last time we did this?"
        "No thanks":

            p "I'll pass. It's all yours."
            show bg ch5ellen27 with dissolve
            e "You sure? I don't want to make you uncomfortable."
            p "It's not that big a deal."
            show bg ch5ellen32 with dissolve
            e "Perfect then, more for me!"
            p "See, I knew you didn't want to share."
            show bg ch5ellen33 with dissolve
            e "True enough. This would'a been wasted on you anyway."
            e "When's the last time we just hung out, no fucking, no work?"

    p "Hank's retirement party."
    e "Shit... that long?"
    p "Yep, that long. Pretty much gave up drinking after that night, too."
    show bg ch5ellen34 with dissolve
    e "I hope he's doing well. Moved to Mex, I think."
    p "That's what I heard. Hank did speak highly of you; he's why I gave you a chance in the first place."
    e "Hank's good people. You know, he got me into this biz."
    p "How'd that work?"
    e "He had some ties to Spartan and heard about my situation. Knew I needed the money bad."
    p "Was he a fan?"
    show bg ch5ellen33 with dissolve
    e "No, but his kid was."
    p "Oh, that little shit..."
    e "Yeah. Hank said me speaking out stopped his kid from doing something stupid. He was probably blowing smoke up my ass. But yeah, few introductions later, there I was."
    e "Hank was too soft. Not like I did anything special."
    p "Still..."
    e "Hell of a retirement party, though."
    p "Yep..."
    show bg ch5ellen39 with dissolve
    e "Remember the bet with the bartender."
    p "I told you I could get her home."
    e "Yeah, cost me fifty bucks."
    if "ch5drink" in extraevents:
        e "You never told me how you enjoyed your night."
        p "Just give me that drink."
        show bg ch5ellen36 with dissolve
        e "OOH! What happened?"
        p "Don't act like you don't know."
        show bg ch5ellen37 with dissolve
        e "I want to hear it from you."
        p "She was receptive, eager. Did I mention hot?"
        e "Ha, and?"
        p "And she was packing heat. Bigger than me, I swear it was!"
        if "ch1futafull" in extraevents:
            p "And I wasn't as open-minded back then."
            show bg ch5ellen36 with dissolve
            e "Back then? Wait, what?"
            p "Maybe I'll tell you the story when I'm more drunk."
        elif "ch1futapartial" in extraevents:
            p "That shit keeps happening to me."
            e "Keeps happening?"
            p "Maybe when I'm more drunk. Maybe never. Yeah, never."
        else:
            p "Certainly freaked me out."
            e "Would love to have seen your face."
            p "I'm sure you would."
    else:
        e "You never told me how you enjoyed your night."
        p "Don't act like you don't know."
        show bg ch5ellen38 with dissolve
        e "I want to hear it from you."
        p "She was receptive, eager. Did I mention hot?"
        show bg ch5ellen33 with dissolve
        e "Ha, and?"
        p "And she was packing heat. Bigger than me, I swear it was!"
        if "ch1futafull" in extraevents:
            p "And I wasn't as open-minded back then."
            show bg ch5ellen36 with dissolve
            e "Back then? Wait, what?"
            p "See, if I still drank, I'd tell you that story. Shame, I'm sober."
        elif "ch1futapartial" in extraevents:
            p "I bolted. That was not what I was expecting."
            p "I swear, that shit keeps happening to me."
            e "Keeps happening?"
        else:
            p "Certainly freaked me out."
            e "Would love to have seen your face."
            p "I'm sure you would."

    show bg ch5ellen38 with dissolve
    if "ch1futafull" in extraevents:
        e "You really should have hit that."
        p "You're not wrong."
        e "I would have, especially if she were as hung as you say."
        p "Not sure if I'm up for receiving."
        e "Don't knock it..."
    else:
        e "I still would have hit it. Especially that night."
        p "Well, I probably came off as a total ass. I was surprised, you know?"
        e "You should be more open-minded."
        p "There's open-minded, then there's worrying about the integrity of my sphincter."


    if e_score >= 2:
        show bg ch5ellen39 with dissolve
        e "We do have stories. Remember when you brought in that corporate war criminal?"
        p "Yup. The only time I didn't feel even a little bad taking someone in to get liquidated. World's better without him."
        show bg ch5ellen40 with dissolve
        e "No doubt. But I meant what happened after. Unless *hic*, you didn't remember a certain outfit?"
        p "How the fuck could I forget?"
        jump ch5ellenlewd
    else:
        e "Shit. I think I drank too fast..."
        show bg ch5ellen41 with dissolve
        p "Ellen, you alright?"
        e "Ugh... Yeah, I'll be fine."
        show bg ch5ellen42 with dissolve
        e "Don't worry about me, spook. Just put your feet up, get some sleep. I'll pass out upfront."
        p "Umm, thanks."
        show bg ch5ellen43 with dissolve
        e "*From behind the curtain* And if you snore loud I'll smash this bottle over your..."
        show bg ch5ellen74 with Dissolve(1)
        p "Ellen?"
        e "..."
        p "Damn, that shit snuck up on her."
        if "ch5drink" in extraevents:
            p "Me too, if I'm honest."
        p "Lights..."
        show bg ch5ellen75 with dissolve
        if "ch4vicaccept" in extraevents:
            p "(It's been a hell of a long night, but it'll be over soon. I just need to figure out how to get Gloria to Victoria... Once I do...)"
            p "(She'll fix it all. It will all work out.)"
        elif "ch4vicgoodbye" in extraevents or "ch4vicsex" in extraevents:
            p "(Long night... Victoria, take care of yourself. I have faith that you'll do the right thing.)"
        p "(We'll see what the morning brings.)"
        jump ch5dream
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
