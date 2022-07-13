

image bg ch7ellenhome1 = "ch7ellenhome1"
image bg ch7ellenhome2 = "ch7ellenhome2"
image bg ch7ellenhome3 = "ch7ellenhome3"
image bg ch7ellenhome4 = "ch7ellenhome4"
image bg ch7ellenhome5 = "ch7ellenhome5"
image bg ch7ellenhome6 = "ch7ellenhome6"
image bg ch7ellenhome7 = "ch7ellenhome7"
image bg ch7ellenhome8 = "ch7ellenhome8"
image bg ch7ellenhome9 = "ch7ellenhome9"
image bg ch7ellenhome10 = "ch7ellenhome10"
image bg ch7ellenhome11 = "ch7ellenhome11"
image bg ch7ellenhome12 = "ch7ellenhome12"
image bg ch7ellenhome13 = "ch7ellenhome13"
image bg ch7ellenhome14 = "ch7ellenhome14"
image bg ch7ellenhome15 = "ch7ellenhome15"
image bg ch7ellenhome16 = "ch7ellenhome16"
image bg ch7ellenhome17 = "ch7ellenhome17"
image bg ch7ellenhome18 = "ch7ellenhome18"
image bg ch7ellenhome19 = "ch7ellenhome19"
image bg ch7ellenhome20 = "ch7ellenhome20"
image bg ch7ellenhome21 = "ch7ellenhome21"
image bg ch7ellenhome22 = "ch7ellenhome22"
image bg ch7ellenhome23 = "ch7ellenhome23"
image bg ch7ellenhome24 = "ch7ellenhome24"
image bg ch7ellenhome25 = "ch7ellenhome25"
image bg ch7ellenhome26 = "ch7ellenhome26"
image bg ch7ellenhome27 = "ch7ellenhome27"
image bg ch7ellenhome28 = "ch7ellenhome28"
image bg ch7ellenhome29 = "ch7ellenhome29"
image bg ch7ellenhome30 = "ch7ellenhome30"
image bg ch7ellenhome31 = "ch7ellenhome31"
image bg ch7ellenhome32 = "ch7ellenhome32"
image bg ch7ellenhome33 = "ch7ellenhome33"
image bg ch7ellenhome34 = "ch7ellenhome34"
image bg ch7ellenhome35 = "ch7ellenhome35"
image bg ch7ellenhome36 = "ch7ellenhome36"
image bg ch7ellenhome37 = "ch7ellenhome37"
image bg ch7ellenhome38 = "ch7ellenhome38"
image bg ch7ellenhome39 = "ch7ellenhome39"
image bg ch7ellenhome40 = "ch7ellenhome40"
image bg ch7ellenhome41 = "ch7ellenhome41"
image bg ch7ellenhome42 = "ch7ellenhome42"
image bg ch7ellenhome43 = "ch7ellenhome43"
image bg ch7ellenhome44 = "ch7ellenhome44"
image bg ch7ellenhome45 = "ch7ellenhome45"
image bg ch7ellenhome46 = "ch7ellenhome46"
image bg ch7ellenhome47 = "ch7ellenhome47"
image bg ch7ellenhome48 = "ch7ellenhome48"
image bg ch7ellenhome49 = "ch7ellenhome49"
image bg ch7ellenhome50 = "ch7ellenhome50"
image bg ch7ellenhome51 = "ch7ellenhome51"
image bg ch7ellenhome52 = "ch7ellenhome52"
image bg ch7ellenhome53 = "ch7ellenhome53"
image bg ch7ellenhome54 = "ch7ellenhome54"
image bg ch7ellenhome55 = "ch7ellenhome55"
image bg ch7ellenhome56 = "ch7ellenhome56"
image bg ch7ellenhome57 = "ch7ellenhome57"
image bg ch7ellenhome58 = "ch7ellenhome58"
image bg ch7ellenhome59 = "ch7ellenhome59"
image bg ch7ellenhome60 = "ch7ellenhome60"
image bg ch7ellenhome61 = "ch7ellenhome61"
image bg ch7ellenhome62 = "ch7ellenhome62"
image bg ch7ellenhome63 = "ch7ellenhome63"
image bg ch7ellenhome64 = "ch7ellenhome64"
image bg ch7ellenhome65 = "ch7ellenhome65"
image bg ch7ellenhome66 = "ch7ellenhome66"
image bg ch7ellenhome67 = "ch7ellenhome67"
image bg ch7ellenhome68 = "ch7ellenhome68"
image bg ch7ellenhome69 = "ch7ellenhome69"
image bg ch7ellenhome70 = "ch7ellenhome70"
image bg ch7ellenhome71 = "ch7ellenhome71"
image bg ch7ellenhome72 = "ch7ellenhome72"
image bg ch7ellenhome73 = "ch7ellenhome73"
image bg ch7ellenhome74 = "ch7ellenhome74"
image bg ch7ellenhome75 = "ch7ellenhome75"
image bg ch7ellenhome76 = "ch7ellenhome76"
image bg ch7ellenhome77 = "ch7ellenhome77"
image bg ch7ellenhome78 = "ch7ellenhome78"
image bg ch7ellenhome79 = "ch7ellenhome79"
image bg ch7ellenhome80 = "ch7ellenhome80"
image bg ch7ellenhome81 = "ch7ellenhome81"





label ch7stairwayellen:
    scene black with Dissolve(1)
    show bg ch7ellenhome7 with dissolve
    p "Ellen, how ya doing?"
    show bg ch7ellenhome6 with dissolve
    e "Just fucking peachy. How does it look like I'm doing?"
    p "Not gonna lie, you look like shit."
    e "Oh thanks! If I could feel much, I'm sure I'd feel like it too."
    p "If you wanna be alone, I can leave."
    show bg ch7ellenhome5 with dissolve
    e "Fuck no! I've had enough of sitting in a room staring at the walls. Or when that gets boring, the ceiling."
    p "Heh, alright."
    show bg ch7ellenhome8 with dissolve
    p "So, what's on your mind?"
    e "Oh, you know. The realization of my fragile mortality. Shit like that."
    p "What happened? When you fell, I thought..."
    show bg ch7ellenhome1 with dissolve
    e "I did too. After the fall, the next thing I remember was waking up in the hospital."
    e "According to Victoria, that freak saved me."
    p "Soft spot for a fellow countryman?"

    show bg ch7ellenhome2 with dissolve
    e "I'm American, you jack-off. Both my parents were born and raised here. Plus, I doubt he checked my DNA while I was fucking falling."
    p "Yeah, dumb point."
    p "At the hospital, did they hurt you?"
    e "Nah... just asked some questions. I told them jack fucking shit."


    if "ch4followellen" in extraevents and "ch4ellenknowvic" not in extraevents:
        e "It was Victoria Shields that was asking the questions. You know her and don't pretend you don't like last time."
        menu:
            "Apologize":
                p "Sorry, I should have told you I knew her."
                e "Kind of important, don't ya think?"
                if vicsexcount > 0:
                    show bg ch7ellenhome3 with dissolve
                    e "And a great lay too, right?"
                    jump ch7stairellenvicfuck
                else:
                    e "I'm still fucking amazed you didn't stick your dick in her."
                    jump ch7stairellencontinue
            "I didn't want you to know":

                p "I felt it wasn't the right time to let you know."
                p "I just wanted you to go back inside and make sure Gloria would be okay."
                show bg ch7ellenhome4 with dissolve
                e "Well, fuck..."
                $ e_score += 1
                if vicsexcount > 0:
                    e "So how was she in the sack?"
                    p "Gloria? Shit, Ellen, I barely know her!"
                    show bg ch7ellenhome3 with dissolve
                    e "No, you stupid shit, Victoria."
                    jump ch7stairellenvicfuck
                else:
                    e "I'm still fucking amazed you didn't stick your dick in her."
                    p "Gloria!?"
                    e "No, you stupid shit, Victoria."
                    jump ch7stairellencontinue
    else:
        e "Victoria was the only one asking questions. She wants to find you, bad."
        p "She can be pretty persuasive. She get anything?"
        e "Screw off. Course I didn't tell her shit. She did try her voodoo on me, didn't work."
        if vicsexcount > 0:
            e "Guess I have a stronger will than you.."
            p "What do you mean?"
            show bg ch7ellenhome3 with dissolve
            e "Don't play coy, you horny shit. She's gotta be an epic fuck."
            jump ch7stairellenvicfuck
        else:
            e "Apparently it didn't work on you either."
            p "Oh, she tried."
            jump ch7stairellencontinue

label ch7stairellenvicfuck:
    menu:
        "She's not what you think":
            p "The more I get to know her, the more her facade falls away."
            p "I think she's just as trapped as the rest of us, in her own way."

            if v_score >= 5:
                show bg ch7ellenhome2 with dissolve
                e "I got that too. But I know players like her. You sure that isn't part of her plan?"
                p "No, I don't think so. I've seen how she acts when no one is watching."
                e "Yeah, I caught her little accent change. You think that's real?"
                p "That's one of the things I noticed, and yeah."
                show bg ch7ellenhome4 with dissolve
                e "Creepy, but ok. Doesn't matter, we can't trust her anyway. Remember, Victoria's the enemy, like it or not."
                $ e_score += 1
                p "I know. I just wish things were different."



                call ch7stairwellwhatsshelike from _call_ch7stairwellwhatsshelike
                jump ch7stairwellellenvicoption
            else:

                show bg ch7ellenhome2 with dissolve
                e "Bullshit she's not. She's manipulative as fuck. You should have seen how she tried to play me in the hospital."
                p "..."
                e "She is fucking dangerous, [p]. Stop thinking with your dick!"
                $ e_score -= 1
                jump ch7stairellenreject
        "Couldn't resist her":


            p "I couldn't help it..."
            show bg ch7ellenhome4 with dissolve
            e "Oh, couldn't resist the pull of the high class pussy, eh?"
            e "Or was it her charms that got to you?"

            menu:
                "Charms":
                    $ e_score -= 1
                    p "Yeah, I tried to resist her. Failed, still not sure it wasn't worth it."
                    p "She gets into your head."

                    e "*Sigh* I fucking get it. Still, I thought you would be stronger than that."
                    p "Sorry..."
                    jump ch7stairellenreject
                "The high class":
                    p "Ellen... I'm a guy. I have certain needs."
                    e "Oh fuck the hell off! Are you serious!"
                    p "And you wouldn't? Bullshit."
                    show bg ch7ellenhome2 with dissolve
                    e "Pfft, don't deflect onto me."
                    p "Who's deflecting? It's a simple question. Would you?"
                    show bg ch7ellenhome4 with dissolve
                    e "Yeah... I probably would... Still doesn't excuse you."
                    call ch7stairwellwhatsshelike from _call_ch7stairwellwhatsshelike_1
                    jump ch7stairwellellenvicoption
        "I had to":
            p "I had to. Keep your enemies closer type thing. If she thought she was playing me, maybe she'd let her guard down."
            show bg ch7ellenhome3 with dissolve
            e "That is one convo-fucking-luted excuse for banging someone you shouldn't. Did it work at least?"
            p "Maybe. Time will tell."
            jump ch7stairellenreject



label ch7stairellenreject:
    e "You should probably go and see how the others are making out."
    e "I'll be fine, you just go find our girl."
    p "Yeah, Ellen, you're probably right. I'll come back and check on you in a bit."
    e "Not like I'm going anywhere.."
    scene black with Dissolve(1)
    p "Hey, I'm back."
    jump ch7scanfind



label ch7stairwellwhatsshelike:
    $ extraevents.append("ch7ellenvic")
    e "Well... since we're on the topic. How good was she?"
    p "In bed? You are actually asking me that?"
    show bg ch7ellenhome2 with dissolve
    e "Yeah we're going down that road, over the river and through the woods too. Details, mother fucker, I want 'em."
    p "She's creative, she likes to please you, but she never lets you doubt who is in control."
    e "Wonder if they train you in fuck techniques at Baynard."
    p "No idea. But I'm pretty sure she came up with some ideas on her own.."
    if "ch2vicsex" in extraevents:
        p "Should have seen the massage she gave me."
    $ e_lust += 1
    show bg ch7ellenhome4 with dissolve
    e "Fuck. Now I'm jealous, you ass."
    return

label ch7stairwellellenvicoption:
    if e_score >= 3:

        menu:
            "Flirt, but drop talk of Victoria":
                play music audio.visitors fadein 2.0 fadeout 2.0
                p "You look like you need some cheering up."
                e "Yeah, how?"
                jump ch7stairwayellenexplore
            "Flirt with her about Victoria":
                jump ch7stairwayellensexvic
            "Go check on Betty":
                p "Look, I should probably get back to Betty. See if she has had any luck."
                show bg ch7ellenhome4 with dissolve
                e "Yeah, we are just wasting time here. More important things to do."
                p "Thanks, Ellen. I'm glad we got you out of there."
                show bg ch7ellenhome1 with dissolve
                e "[p], thank you, by the way."
                p "Don't mention it."
                scene black with Dissolve(1)
                p "Hey, I'm back."
                jump ch7scanfind
    else:
        p "Look, I should probably get back to Betty. See if she has had any luck."
        show bg ch7ellenhome4 with dissolve
        e "Yeah, we are just wasting time here. More important things to do."
        p "Thanks, Ellen. I'm glad we got you out of there."
        show bg ch7ellenhome1 with dissolve
        e "[p], thank you, by the way."
        p "Don't mention it."
        scene black with Dissolve(1)
        p "Hey, I'm back."

        jump ch7scanfind

label ch7stairellencontinue:
    $ e_score += 1
    $ e_lust += 1
    e "Heh, well aren't you a saint. I don't know if I could have resisted, under normal circumstances."
    p "I don't know how I did it, but hey, I did."
    if e_score >= 3:
        menu:
            "Flirt with Ellen":
                play music audio.visitors fadein 2.0 fadeout 2.0
                p "You look like you need some cheering up."
                e "Yeah, how?"
                jump ch7stairwayellenexplore
            "Go check on Betty":

                p "Look, I should probably get back to Betty. See if she has had any luck."
                show bg ch7ellenhome4 with dissolve
                e "Yeah, we are just wasting time here. More important things to do."
                p "Thanks, Ellen. I'm glad we got you out of there."
                show bg ch7ellenhome1 with dissolve
                e "[p], thank you, by the way."
                p "Don't mention it."
                scene black with Dissolve(1)
                p "Hey, I'm back."

                jump ch7scanfind
    else:
        p "Look, I should probably get back to Betty. See if she has had any luck."
        show bg ch7ellenhome4 with dissolve
        e "Yeah, we are just wasting time here. More important things to do."
        p "Thanks, Ellen. I'm glad we got you out of there."
        show bg ch7ellenhome1 with dissolve
        e "[p], thank you, by the way."
        p "Don't mention it."
        scene black with Dissolve(1)
        p "Hey, I'm back."

        jump ch7scanfind



label ch7stairwayellensexvic:
    $ extraevents.append("ch7ellenvic")
    play music audio.visitors fadein 2.0 fadeout 2.0
    p "Ellen, I wouldn't compare yourself to her."
    show bg ch7ellenhome11 with dissolve
    e "I ain't comparing shit. It's the fact you got to fuck her."
    p "OH!"
    show bg ch7ellenhome9 with dissolve
    p "Well she does do this pretty hot thing where she will suck your thumb."
    show bg ch7ellenhome10 with dissolve
    e "[p], I'm not sucking your thumb."
    p "Ha, okay, fine."
    e "Hell... I am not doing much of anything right now."
    p "You know it's temporary. Hey, we can probably figure something out."
    e "Like?"
    jump ch7stairwayellenexplore



image ch7ellenhomepan = Movie(play='video/chapter-7-video/ch7ellenhomepan.webm', loop=False)
image bg ch7ellenhomepanmovie movie:
    "ch7ellenhomepan"
    pause 10.0
    "ch7ellenhomepanend"

image bg ch7ellenhomepussyrub movie = Movie(play='video/chapter-7-video/ch7ellenhomepussyrub.webm')

label ch7stairwayellenexplore:
    if _in_replay:
        $ setReplay()
        play music audio.visitors fadein 2.0 fadeout 2.0

        if persistent.ch7ellenanal == True:
            $ e_lust = 2
    if ellensexname == False:
        $ ellensexname = p

    show bg ch7ellenhome12 with dissolve
    p "Let's start down here."
    e "Umm..."
    show bg ch7ellenhome13 with dissolve
    p "What?"
    show bg ch7ellenhome14 with dissolve
    e "I can't feel that at all and you're not allowed to have all the fun."
    show bg ch7ellenhome15 with dissolve
    p "How about this?"
    show bg ch7ellenhome16 with dissolve
    e "Zero, zilch, na-da."
    p "Damn, a bit further then."
    e "I'm not stopping you."
    show bg ch7ellenhome17 with dissolve
    p "Can you feel that?"
    e "Maybe... Explore a bit-"
    show bg ch7ellenhomepussyrub movie with dissolve
    e "Right, down there..."
    p "How about this?"
    e "Ohhh... Maybe..."
    show bg ch7ellenhome18 with dissolve
    p "Oh, you certainly can feel that."
    e "I'm not telling."
    show bg ch7ellenhome19 with dissolve
    p "Now, how about up here."
    show bg ch7ellenhome20 with dissolve
    e "Who knows, jackass."
    menu:
        "Softly touch":
            show bg ch7ellenhome21 with dissolve
            p "Feels good to me."
            e "Heh, I'm sure it does."
            show bg ch7ellenhome22 with dissolve
            e "Just don't you dare go soft on me, [p]."
            p "Never."
            show bg ch7ellenhome27 with dissolve
            e "Now, help me get this dress off."
            p "That I can do."
        "Pinch":

            p "How about..."
            show bg ch7ellenhome23 with dissolve
            p "This!"
            e "Ow! Fuck!"
            show bg ch7ellenhome24 with dissolve
            $ renpy.pause(1)
            play sound audio.slapeffect
            show bg ch7ellenhome25 with dissolve
            p "Fuck me! Okay, you can feel that!"
            show bg ch7ellenhome26 with dissolve
            $ e_lust += 1
            e "Fucking right I can. Don't think I won't hurt you."
            show bg ch7ellenhome27 with dissolve
            e "Now help me get this damn dress off."
            p "Let me get my senses back..."
            e "Hurry up, you wuss."
            p "Okay, good."

    show bg ch7ellenhome28 with dissolve
    e "Remember, you have to do most of the work this time."
    show bg ch7ellenhome29 with dissolve
    if "ch7ellenvic" in extraevents:
        e "Ha, fuck, now I am the missionary girl."
    else:
        e "Should be pretty easy going for me."
        p "You sly devil."
    e "[p], just pull this dress off."
    show bg ch7ellenhome30 with dissolve
    p "Off we go."
    show bg ch7ellenhomepanmovie movie with dissolve
    p "There, now there is nothing you can do to stop me."
    e "Just wow..."
    e "Come on, get over here."
    show bg ch7ellenhome31 with dissolve
    e "Well, don't expect me to be leading this. It's all up to you."
    $ resetsexmenu()
    jump ch7stairwayellensex









image bg ch7ellenfuck1 movie = Movie(play='video/chapter-7-video/ch7ellenfuck1.webm')
image bg ch7ellenfuck2 movie = Movie(play='video/chapter-7-video/ch7ellenfuck2.webm')


image bg ch7ellenblow movie = Movie(play='video/chapter-7-video/ch7ellenblow.webm')
image bg ch7ellenboobs movie = Movie(play='video/chapter-7-video/ch7ellenboobs.webm')
image bg ch7ellendrums movie = Movie(play='video/chapter-7-video/ch7ellendrums.webm')
image bg ch7ellenanal movie = Movie(play='video/chapter-7-video/ch7ellenanal.webm')


label ch7stairwayellensex:
    menu:
        "Play with her tits":
            $ sexmenu1 = False
            $ sexmenu2 = True
            jump ch7stairwayellensextits
        "Blowjob":
            $ sexmenu1 = False
            $ sexmenu2 = True
            jump ch7stairwayellensexblow
        "Spread her legs":
            $ sexmenu1 = False
            $ sexmenu2 = True
            jump ch7stairwayellensexfuck
        "Flip her over" if sexmenu1 == False:
            jump ch7stairwayellensexstomach


label ch7stairwayellensextits:
    show bg ch7ellenhome32 with dissolve
    p "There we go."
    e "I just wanna make one thing damn clear..."
    show bg ch7ellenhome33 with dissolve
    p "And what's that?"
    e "I may not be able to kick you right now, but I sure as shit can slap the fuck out of you."
    show bg ch7ellenboobs movie with dissolve
    p "I'll be extra nice then."
    e "Did I ask for nice, just don't do any of your stupid shit."
    p "What the hell do you mean by that?!"
    show bg ch7ellenhome34 with dissolve
    e "Just shut up and get that cock up here."
    show bg ch7ellenhome35 with dissolve
    p "I got an idea..."
    e "Oh!"
    show bg ch7ellendrums movie with dissolve
    p "You need a new drummer? I think I've got what it takes."
    e "..."
    p "What?!"
    show bg ch7ellenhome36 with dissolve
    e "See, this is the stupid shit I was talking about."
    show bg ch7ellenhome37 with dissolve
    e "Fuck stupid, that might be the most spectrumed fucking thing you've ever said."
    p "Just trying to cheer you up..."
    e "You get one. Next time, I slap the shit out of you."
    jump ch7stairwayellensex

label ch7stairwayellensexblow:
    e "Alright, get your ass up here."
    show bg ch7ellenhome39 with dissolve
    p "You cool to do this?"
    e "You even have to ask?"
    show bg ch7ellenhome40 with dissolve
    p "Damn, I love it when you look at me like that."
    e "Well I have to keep a close eye on you."
    if "ch7ellenvic" in extraevents and e_lust >= 2:
        e "If I don't, some slutty redhead might take you away."
        p "If it happens again, I promise I'll invite you."
        e "Good."
    else:
        e "No telling where you'll stick your dick next."
    e "Just remember how good I am at this."
    show bg ch7ellenhome38 with dissolve
    n "As you push the tip of your cock to her mouth her tongue darts back and forth across the head"
    p "Ohhh... shiiiiit."
    e "Yeah, mouth works fine."
    show bg ch7ellenblow movie with dissolve
    n "You push deeper feeling the playfulness of her tongue"
    e "Mmm..."
    p "Fuck me, your blowjobs are fantastic."
    show bg ch7ellenhome41 with dissolve
    e "Well, I expect payback."
    p "I think I can do that."
    e "Oh and..."
    show bg ch7ellenhome42 with dissolve
    e "Could you get off my arm... I'm losing feeling in it and I consider that pretty important at this moment."
    p "Of shit! Of course."
    jump ch7stairwayellensex



label ch7stairwayellensexfuck:
    show bg ch7ellenhome43 with dissolve
    p "There we are."
    e "Ha, you'll have to hold my legs up."
    p "I got it, don't worry."
    show bg ch7ellenhome44 with dissolve
    p "You ready?"
    e "Stop always asking me that, of course I am!"
    show bg ch7ellenhome45 with dissolve
    p "Heh, noted for the future."
    show bg ch7ellenfuck1 movie with dissolve
    e "Holy fuck, yeah, right fucking there!"
    p "Glad to be of service."
    show bg ch7ellenhome46 with dissolve
    e "Oh, fuck me! Keep it up."
    p "Shit, not too loud, the others might hear us!"
    show bg ch7ellenfuck1 movie with dissolve
    e "You should have... UGH! Thought of that before we started this!"
    p "Damn, you love to get me in trouble!"
    e "More fun that way!"
    show bg ch7ellenhome47 with dissolve
    e "WOW! Damn, that hit the spot!"
    show bg ch7ellenhome48 with dissolve
    e "But, uh... Now what?"
    p "I got some ideas."
    jump ch7stairwayellensex


label ch7stairwayellensexstomach:
    if sexmenu2:
        p "Let me flip you on your stomach."
    show bg ch7ellenhome50 with dissolve
    p "How's that?"
    show bg ch7ellenhome49 with dissolve
    e "It could be better..."
    p "How so?"
    e "Hate lying flat, I like the angle better when my ass is up a bit."
    show bg ch7ellenhome51 with dissolve
    p "Well then, I think I have a solution. It's pretty high tech stuff."
    e "Ha, you ass. That's perfect."
    show bg ch7ellenhome52 with dissolve
    e "Someone should patent this tech."
    p "I'd make millions."
    show bg ch7ellenhome53 with dissolve
    e "What is it with you always staring at my pussy? It's the same as it ever was.."
    show bg ch7ellenhome54 with dissolve
    p "Hey, sorry, I can't help it."
    e "Well stop staring and get to work."
    show bg ch7ellenhome56 with dissolve
    e "I am so glad I can feel that."
    p "It would be very odd for me if you couldn't."
    show bg ch7ellenhome57 with dissolve
    e "Just fuck me, [ellensexname]."
    show bg ch7ellenfuck2 movie with dissolve
    e "Oh fuck, yes! Thank god!"
    p "I take it this is working?"
    e "Less talking, more fucking! I'm gonna fucking pop!"
    show bg ch7ellenhome55 with dissolve
    e "OH, fucking prime, [ellensexname]!"
    menu:
        "Suggest something more" if e_lust >= 2:
            $ persistent.ch7ellenanal = True
            jump ch7stairwayellenanal
        "Cum on her back":
            jump ch7stairwayellencumback
        "Cum in her":
            jump ch7stairwayellencuminside
        "Do something else":
            jump ch7stairwayellensex

label ch7stairwayellenanal:
    p "Maybe we can try something else."
    e "Like?"
    show bg ch7ellenhome58 with dissolve
    p "Well, there is one road we never walked down."
    e "I guess there's a first time for everything."

    $ achievement.grant("PILLOWTALK")
    init:
        $ achievement.register("PILLOWTALK")
    $ achievement.Sync()

    show bg ch7ellenhome61 with dissolve
    e "Besides, not like I can feel it much, so this is the best time to break her in."
    show bg ch7ellenhome60 with dissolve
    p "I'll go slow then."
    show bg ch7ellenhome62 with dissolve
    p "Damn Ellen, this is..."
    show bg ch7ellenanal movie with dissolve
    p "We should have done this ages ago."
    e "Ugh! I think... WOW! You were too scared to ask!"
    show bg ch7ellenhome63 with dissolve
    e "Jesus fuck, even being numb down there, I can feel that!"
    show bg ch7ellenanal movie with dissolve
    p "Just let me know if I should stop."
    e "Not till I cum, [ellensexname]!"
    e "Which is right...!"
    show bg ch7ellenhome69 with dissolve
    e "Now... Agreed, why the hell haven't we done this before?!"
    p "Ha, no clue."
    menu:
        "Cum":
            p "Fuck, I'm going to cum."
            show bg ch7ellenhome72 with quickflash
            e "Just don't make a giant mess like you normally-"
            show bg ch7ellenhome73 with dissolve
            e "*Sighs* Do..."
            p "Heh, I'll help you clean it up."
            show bg ch7ellenhome67 with dissolve
            e "Well, at least it wasn't the face this time."
            jump ch7ellensexendscene
        "Move on":
            jump ch7stairwayellensex



label ch7stairwayellencumback:
    p "Fuck I'm going to cum."
    show bg ch7ellenhome64 with dissolve
    e "Just don't make a giant mess like you normally-"
    show bg ch7ellenhome65 with quickflash
    $ renpy.pause(1)
    show bg ch7ellenhome66 with dissolve
    e "*Sighs* Do..."
    p "Heh, I'll help you clean it up."
    show bg ch7ellenhome67 with dissolve
    e "Well, at least it wasn't the face."
    jump ch7ellensexendscene

label ch7stairwayellencuminside:
    p "Fuck I'm going to cum."
    show bg ch7ellenhome70 with dissolve
    e "Just don't make a giant mess like you normally-"
    show bg ch7ellenhome71 with quickflash
    e "*Sighs* Do..."
    p "Heh, I'll help you clean it up."
    show bg ch7ellenhome68 with dissolve
    e "Well, at least it wasn't the face."
    jump ch7ellensexendscene


label ch7ellensexendscene:
    scene black with Dissolve(1)
    show bg ch7ellenhome74 with dissolve
    e "God, I feel like a pile of shit now."
    p "Why's that?"
    e "Gloria is still out there..."
    p "They're looking, Ellen."
    show bg ch7ellenhome76 with dissolve
    e "Yeah, but you and me aren't."
    p "Look, there are times you need to know what you can and can't do. You and I, we'd just be in the way right now."
    e "I know. But..."
    $ extraevents.append("ch7ellensex")
    $ renpy.end_replay()
    if not persistent.ch7ellensex:

        $ renpy.notify(['Scene Unlocked', 'unlock'])
        $ persistent.ch7ellensex = True
    p "She's a tough one, Ellen. She'll be alright, I'm sure of it."
    if "ch5ellenkiss" in extraevents:
        e "I hope so."
        show bg ch7ellenhome77 with dissolve
        p "Hey, it's going to be okay."
        e "You like to say that, but [p]..."
        show bg ch7ellenhome78 with dissolve
        e "Fuck it, can you just kiss me."
        show bg ch7ellenhome79 with dissolve
        $ renpy.pause(1)
        show bg ch7ellenhome80 with dissolve
        p "Better?"
        e "Much, thank you."
        p "Look, I should probably get back."
        e "I know."
    else:

        p "Although, I should probably see if they have made any progress."
        e "Yeah..."
        p "You going to be okay here?"
        e "Better than where I use to be."

    show bg ch7ellenhome81 with dissolve
    play music audio.space fadein 2.0 fadeout 2.0
    e "Hey, [p]."
    p "Yeah?"
    e "Bring her home, okay...?"
    p "I will."
    scene black with Dissolve(1)
    p "Hey, I'm back."
    jump ch7scanfind
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
