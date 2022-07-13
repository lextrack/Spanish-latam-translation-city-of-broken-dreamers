
image ch5ellendrink = Movie(play='video/chapter-5-video/ch5ellendrink.webm', loop=False)
image bg ch5ellendrinkmovie movie:
    "ch5ellendrink"
    pause 6.0
    "ch5ellendrinkend"

image ch5ellenpan2 = Movie(play='video/chapter-5-video/ch5ellenpan2.webm', loop=False)
image bg ch5ellenpan2movie movie:
    "ch5ellenpan2"
    pause 10.0
    "ch5ellenpan2end"


image bg ch5ellenlick movie = Movie(play="video/chapter-5-video/ch5ellenlick.webm")
image bg ch5ellenblow1 movie = Movie(play="video/chapter-5-video/ch5ellenblow1.webm")
image bg ch5ellenride1 movie = Movie(play="video/chapter-5-video/ch5ellenride1.webm")
image bg ch5ellenride2 movie = Movie(play="video/chapter-5-video/ch5ellenride2.webm")
image bg ch5ellenride3 movie = Movie(play="video/chapter-5-video/ch5ellenride3.webm")
image bg ch5ellenride4 movie = Movie(play="video/chapter-5-video/ch5ellenride4.webm")


image bg ch5ellenbehind1 movie = Movie(play="video/chapter-5-video/ch5ellenbehind1.webm")
image bg ch5ellenbehind2 movie = Movie(play="video/chapter-5-video/ch5ellenbehind2.webm")

image bg ch5ellenfinger movie = Movie(play="video/chapter-5-video/ch5ellenfinger.webm")
image bg ch5ellenspank movie = Movie(play="video/chapter-5-video/ch5ellenspank.webm")
image bg ch5ellendoggy movie = Movie(play="video/chapter-5-video/ch5ellendoggy.webm")

image bg ch5ellenoface movie = Movie(play="video/chapter-5-video/ch5ellenoface.webm")



label ch5ellenlewd:
    e "Alright, just... Whoa, give me a second."
    show bg ch5ellen42 with dissolve
    e "I got somethin' ta show ya."
    p "Oh, and what would that be?"
    show bg ch5ellen41 with dissolve
    e "That's telling. It has to be a surprise. Surprising..."
    p "Ellen, you're not going to puke on me again, are you?"
    show bg ch5ellendrinkmovie movie with dissolve
    e "Fuck off! Now I need to surprise you with that outfit. You're gonna freak."
    p "Umm, Ellen, that's not how surprises work."
    e "Shaddap!"
    show bg ch5ellen43 with dissolve
    n "You hear Ellen shuffling up front, trying to change, albeit with some drunken difficulty"
    p "It's just a bikini, Ellen. What on earth are you doing?"
    e "If I have to tell you to fuck off once more tonight..."
    p "You will."
    e "Close your lips and zip your eyes."
    p "You already spoiled the surprise!"
    e "Shush! Surprise!"
    scene black with Dissolve(2)
    $ renpy.pause(1)
    e "Now."
    show bg ch5ellenpan2movie movie with dissolve
    e "Remember this?"
    p "I already told you I did."
    e "Holy shit, you are slap worthy. I'll hit you!"
    p "You can try."
    show bg ch5ellen46 with dissolve
    e "Don't make me come over there."
    p "Why? What are you going to do?"
    show bg ch5ellen44 with dissolve
    e "Just you... Holy shit... Just you wait."
    menu:
        "Continue":
            $ extraevents.append("ch5ellen")
            jump ch5ellensex
        "Tell her to stop":
            p "Ellen, we should probably just get to sleep."
            show bg ch5ellen45 with dissolve
            e "Bah, the fuck?! Whoever you are, what did you do with, [p]? Did you get your brain jumbled by Baynard or something?"
            p "Ellen. Please."
            show bg ch5ellen47 with dissolve
            e "Pfft! You know I like it when you play hard to get."
            p "I'm not playing, Ellen."
            show bg ch5ellen48 with dissolve
            p "And, you are about half a bottle over your limit."
            e "Hey, that's mine!"
            show bg ch5ellen49 with dissolve
            p "I'm cutting you off."
            e "What the FUCK, [p]?"

            menu:
                "I may have met someone" if "ch4katie" in extraevents or "ch4vicsex" in extraevents:

                    if "ch4vicsex" not in extraevents:
                        call ch5ellendoc from _call_ch5ellendoc
                    elif "ch4katie" not in extraevents:
                        call ch5ellenvic from _call_ch5ellenvic
                    else:
                        menu:
                            "Explain Katie":
                                call ch5ellendoc from _call_ch5ellendoc_1
                            "Explain Victoria":
                                call ch5ellenvic from _call_ch5ellenvic_1




                    show bg ch5ellen112 with dissolve
                    e "[p], *hic* Shit, trying to be serious here."
                    e "[p], I get it, you probably need someone like that in your life and we're not getting any younger. I mean, I feel old as fuck and that makes you a dinosaur."
                    p "You're okay?"
                    e "Listen, [p], we have had lots of laughs, but that's all it was. I'm happy for you. I really am."
                    p "Thanks. You know, that was almost coherent."
                    show bg ch5ellen114 with dissolve
                    e "Fuck off...."
                    p "And she's back."
                    e "Yes, I am! But now I'm beat. After you dropped that bomb, I think the room is all spinny."
                "You're drunk":

                    $ e_score += 1
                    p "Ellen, you're drunk."
                    show bg ch5ellen113 with dissolve
                    e "So? When has that stopped you before?"
                    p "No offense, but so drunk, I'm not sure you will remember this in the morning. Not my jam."
                    show bg ch5ellen114 with dissolve

                    e "That's not... I'm prime fuckable right now!"
                    p "Come on, can we just get some sleep?"
                    e "Shit. Fine, the room just went spinny, don't wanna puke on someone during cowgirl. Again."
                    p "That was me..."
                    e "Oh? Well, shit."
                "Just tired":
                    p "Just not in the mood tonight. Too much shit has been happening lately and we need to be fresh for tomorrow."
                    show bg ch5ellen114 with dissolve

                    e "Oh god, you're no fun."
                    p "Can we just sleep? Please."
                    e "Fuck it, whatever. Heathen."

    show bg ch5ellen78 with dissolve
    e "Alright, scootch. You hog the bed; you ain't waking up."
    p "Then why don't you sleep up front?"
    show bg ch5ellen77 with dissolve
    e "The front sucks. You're comforting. You know what I mean."
    p "*Sighs* Fine..."
    show bg ch5ellen81 with dissolve
    e "Oh, stop crying like a little bitch. Go to sleep."
    p "I'm the one who can't feel my legs."
    e "Live with..."
    show bg ch5ellen82 with dissolve
    e "It..."
    p "*Sighs* Please don't puke tonight is all I ask."
    if "ch4vicaccept" in extraevents:
        p "(I need to find a way to get Gloria to Victoria. Ellen will understand once it's done. This has to be for the best.)"
    elif "ch4vicgoodbye" in extraevents or "ch4vicsex" in extraevents:
        p "(What the hell am I even doing? I need to come up with something fast or we're all dead. I wonder if Victoria's having a better night?)"
    p "(We'll see what the morning brings.)"
    $ extraevents.append("ch5ellentop")
    jump ch5dream


label ch5ellenvic:
    $ extraevents.append("ch5ellenvic")
    p "Ellen, we have always been friends."
    e "With benefits..."
    p "About those..."
    show bg ch5ellen114 with dissolve
    e "Holy shit! Are you breaking up with me? We can't break up if we were never dating... Dumbass."
    p "Okay, look. There's something that might be a thing. Great, now I sound like you."
    if "ch1ellen" in extraevents:
        e "Are you getting back together with the wife? The one I didn't know about?"
        e "She's not gonna kill me now?"
        p "She may, but no, not her."
    show bg ch5ellen115 with dissolve
    e "Wait! SHIT! Did you get a girlfriend?!"
    p "I don't fucking know. It's kinda complicated, I've never met anyone like her before."
    show bg ch5ellen114 with dissolve
    e "You've never been one for complicated, [p]. I thought you liked the straight and narrow?"
    p "Normally sure. It's just something about her. Something I feel I can explore."
    e "Hah, I'm sure exploration is at the top of that list."
    p "Ellen..."

    return

label ch5ellendoc:
    $ extraevents.append("ch5ellendoc")
    p "Ellen, we have always been friends."
    e "With benefits..."
    p "About those..."
    show bg ch5ellen114 with dissolve
    e "Holy shit! Are you breaking up with me? We can't break up if we were never dating... Dumbass."
    p "Okay, look. There's something that might be a thing. Great, now I sound like you."
    if "ch1ellen" in extraevents:
        e "Are you getting back together with the wife? The one I didn't know about?"
        e "She's not gonna kill me now?"
        p "She may, but no, not her."
    show bg ch5ellen115 with dissolve
    e "Wait! SHIT! Did you get a girlfriend?!"
    p "I don't fucking know. She's, well... sweet, and I don't want to hurt her."
    show bg ch5ellen114 with dissolve
    e "Ha, [p]? Sweet? Fuck off! That is so not your style."
    p "Maybe not, but it doesn't matter. She isn't like us. I..."
    return

label ch5ellensex:

    if _in_replay:
        play music audio.visitors fadein 5.0 fadeout 5.0
        $ setReplay()
        if persistent.ch5ellen1 == True:
            $ e_score = 3
        scene black with Dissolve(2)
        $ renpy.pause(1)
        e "Now."
        show bg ch5ellenpan2movie movie with dissolve
        e "Remember this?"
        p "I already told you I did."
        e "Holy shit, you are slap worthy. I'll hit you!"
        p "You can try."
        show bg ch5ellen46 with dissolve
        e "Don't make me come over there."
        p "Why? What are you going to do?"
        show bg ch5ellen44 with dissolve
        e "Just you... Holy shit... Just you wait."


    p "I'm waiting."
    show bg ch5ellen47 with dissolve
    e "Mmm, well, here I am, spooky."
    show bg ch5ellen48 with dissolve
    if "ch5drink" in extraevents:
        p "Give me that."
        e "That's mine, bitch!"
        p "Just one more drink."
        show bg ch5ellen49 with dissolve
        p "Gotta make up for lost time."
        e "Fiiine. Ass."
    else:
        p "No more for you."
        e "Hey, fuck off! That's mine, bitch!"
        show bg ch5ellen49 with dissolve
        p "Not anymore. Now come here."
    e "Fine, you ass."
    show bg ch5ellen50 with dissolve
    p "And since you \"surprised\" me already, I think we can lose the clothes."
    e "Last time I try to be sexamantic."
    p "You'll live and naked is where we were going, anyway."
    show bg ch5ellen58 with dissolve
    e "Still fucking hot as FUCK anyways. Right?"
    p "Do you even have to ask?"
    show bg ch5ellenlick movie with dissolve
    e "Nope. Lay your ass back -- time for this girl to play."
    p "Phew, nice..."
    if "ch5drink" in extraevents:
        e "We need to drink together more."
    else:
        e "We need to do this more often."
    show bg ch5ellen57 with dissolve
    e "So, [p], you just staring or we starting this shit?"
    if ellensexname == False:
        jump ch5nameellensex
    else:
        $ resetmenu()
        jump ch5ellenmenu

label ch5nameellensex:
    menu:
        "Continue on":
            $ ellensexname = p
        "First things first, call me...":

            python:
                ellensexname = renpy.input("What do you want her to call you?")
                ellensexname = ellensexname.strip()
                persistent.ellensexname = ellensexname
            if ellensexname == "Daddy" or ellensexname == "Papa":
                e "Fuck off. Pick something else."
                p "But..."
                e "Nope."
                p "Fine."
                $ achievement.grant("CALLMEMAYBE")
                init:
                    $ achievement.register("CALLMEMAYBE")
                $ achievement.Sync()

                jump ch5nameellensex
            elif ellensexname != p and ellensexname != "spook":
                e "[ellensexname], you want me to call you [ellensexname]? The fuck?"
                p "Hey! I happen to enjoy that."
                e "Eh, I've done weirder, when sober, I shouldn't talk. Alright, then [ellensexname], now what?"
            else:
                e "Umm, okay, [ellensexname]. Are you feeling okay? Nevermind, forget I asked."
    $ resetmenu()
    jump ch5ellenmenu


label ch5ellenmenu:
    menu:
        "Blowjob":
            jump ch5ellenblowjob
        "Doggy":
            jump ch5ellendoggy
        "Cowgirl":
            jump ch5ellencowgirl
        "Sideways Cowgirl" if "ch5ellenkiss" in extraevents:
            jump ch5ellensideways
        "Against the wall":
            jump ch5ellenwall

label ch5ellendoggy:
    p "Let's use this floor. Carpet is handy."
    show bg ch5ellen104 with dissolve
    e "Get down here."
    p "Let me enjoy the view."
    show bg ch5ellen105 with dissolve
    p "You know that ass is awesome."
    e "You've told me that before, fuckwit."
    show bg ch5ellenfinger movie with dissolve
    e "Now enjoy the... ugh... show."
    p "Rather join in."
    e "You can... ahh..."
    show bg ch5ellen106 with dissolve
    e "Wait!"
    p "Are you done? Because I need to play with this for a bit."
    show bg ch5ellenspank movie with dissolve
    e "Gah! You ass. What the hell?"
    p "You made me wait!"
    show bg ch5ellen107 with dissolve
    e "Why don't you just put it in me instead?!"
    show bg ch5ellen108 with dissolve
    p "Pushy pushy!"
    e "Damn straight!"
    show bg ch5ellendoggy movie with dissolve
    e "There ya go!"
    p "Oh, so you are enjoying yourself now?"
    e "Never said I wasn't!"
    show bg ch5ellen109 with dissolve
    e "Hey, I didn't say slow down!"
    p "Of course!"
    show bg ch5ellenoface movie with dissolve
    e "Phew! Fuck me!"
    e "Damn, I needed this!"
    show bg ch5ellen110 with dissolve
    p "You and me both."
    show bg ch5ellen111 with dissolve
    e "Well, shit. Now what?"
    jump ch5ellenmenu


label ch5ellenblowjob:
    $ menu2 = False
    p "Well, it has been a busy day. I could just relax."
    e "Then lay the fuck back and relax already."
    p "Yes, ma'am!"
    show bg ch5ellen100 with dissolve
    e "Now sit back close those eyes... Or watch, don't matter to me! Just don't give me that weird look you do."
    p "Weird look?"
    e "You know the one."
    p "I really don't."
    e "Whatever, not like I give a fuck."
    show bg ch5ellen101 with dissolve
    e "You know, you treat me better than everyone I know, how fucked is that?"
    p "Um..."
    e "Ignore that."
    show bg ch5ellenblow1 movie with dissolve
    p "Wow, fuck me."
    e "Mmmph... mpph gghg prrt fff thlllp pllln."
    p "What?"
    show bg ch5ellen102 with dissolve
    e "Part of the plan, [ellensexname]."
    e "From behind, hard. Against a wall or some shit. Fuckin' pound me."
    if menu1 == True:
        p "That I can do."
        e "Prime fuckin' aces!"
    else:
        p "We already did that."
        e "Then do it a-fucking-gain!"
        p "Yes, Ma'am."
    show bg ch5ellen103 with dissolve
    e "So get on it!"
    p "Maybe, let me think on it."
    e "Don't think too hard; that's why we drink, [ellensexname]."
    jump ch5ellenmenu


label ch5ellencowgirl:
    $ menu1 = False
    p "Climb on top."
    e "Damn, guys like the bronco."
    show bg ch5ellen59 with dissolve
    p "Yep."
    e "And why is that?"
    show bg ch5ellen60 with dissolve
    p "Is it not obvious?"
    e "Titties in the face. I should've known."
    p "Just get on there."
    show bg ch5ellen61 with dissolve
    e "Shit on me!"
    p "I'm starting to think you are into some really strange stuff."
    if "ch2chooseellen" in extraevents:
        e "Ha, what, when I almost shat on Alex's desk?"
        p "Ok, enough of that. Talk about boner killer."
        e "Then just shut the fuck up... getting a rhythm here."
    else:
        e "Just shut the fuck up. Getting a rhythm here."
    show bg ch5ellenride1 movie with dissolve
    p "Fff.... shit...."
    e "See... it's better when you just shut the fuck up..."
    p "(Groans)"
    e "Less... you talk... closer I am..."
    show bg ch5ellenride2 movie with dissolve
    p "You really know how to..."
    e "What the hell did I say? Shut it, [ellensexname]!"
    p "Christ! Fine!"
    e "Here it comes!"
    show bg ch5ellen62 with vpunch
    e "Fuck yes!"
    p "Damn, great work as always."
    show bg ch5ellen84 with dissolve
    e "Gotta enjoy life while you can. Shit changes in an instant."
    if e_score >= 3:
        menu:
            "Kiss her":
                $ persistent.ch5ellenkiss = True
                $ persistent.ch5ellen1 = True
                if "ch5ellenkiss" not in extraevents:
                    $ e_score += 1
                $ extraevents.append("ch5ellenkiss")
                p "Hey, come here."
                show bg ch5ellen88 with dissolve
                n "Your lips press against Ellen's"
                show bg ch5ellen89 with dissolve
                e "Mmmph!"
                p "What?"
                show bg ch5ellen85 with dissolve
                e "What the fuck is wrong with you!"
                p "I thought?!"
                show bg ch5ellen86 with hpunch
                p "Oph! The hell. What is with everyone hitting me lately!"
                e "You fucking asshole! Why the fuck, we had lines. I never said you could..."
                p "I'm sorry."
                show bg ch5ellen87 with dissolve
                e "Yeah, you better be."
                p "Right, just sex no-!"
                show bg ch5ellen91 with dissolve
                n "This time your lips lock as you feel the warmth of her mouth"
                show bg ch5ellen90 with dissolve
                e "Asshole."
                p "I know."
                e "Come on. The night is young."
                jump ch5ellensideways
            "Never know":



                p "That's why I like you, live hard. Play hard."
                e "Live fast, die young."
                p "Gonna fuck me to death?"
                e "Just shut it and fuck me."
                jump ch5ellenmenu

    p "I do. I'm damn pretty."
    e "Well, when you're dead, at least I won't have to give clients excuses for your ass."
    p "Ever the optimist, aren't you?"
    e "Remember what I said about talking, ass?"
    jump ch5ellenmenu




label ch5ellenwall:
    if menu2 == False:
        p "You said something about behind?"
        e "Thank you! About {i}fucking{/i} time, [ellensexname]!"
    else:
        p "How about at the wall or screen or whatever you call that?"
        e "From behind? Perfect!"

    show bg ch5ellen63 with dissolve
    e "Now get that pasty white ass over here."
    p "On my way."
    show bg ch5ellen64 with dissolve
    e "You know what I fucking like, so fucking do it."
    p "Gentle caressing?"
    e "Fuck off!"
    p "Right, hard and fast it is. Don't wanna get murdered in my sleep."
    show bg ch5ellen65 with dissolve
    e "I'll fuckin' do it, too! Don't test me."
    if "ch2chooseellen" in extraevents:
        p "I saw how you decked Alexis. I don't want any of that."
        e "You sure? Maybe a whip, some chains?"
        p "Shut up and bend the fuck over."
    else:
        p "I know you would."
        e "Damn straight. Now come and fuck me."
    show bg ch5ellen66 with dissolve
    p "On the other hand..."
    e "You mother-"
    p "Just kidding."
    show bg ch5ellenbehind1 movie with dissolve
    e "OH fuck! That's it!"
    p "Damn, you have tightened up. You really love this, don't you?"
    e "You have no fucking idea."
    show bg ch5ellen68 with dissolve
    p "Well, don't crush it..."
    e "Quit... AAAH... Fucking... Whining..."
    show bg ch5ellenbehind2 movie with dissolve
    p "I'll deal...."
    e "You... Fucking... Better."
    e "Or I'll... [ellensexname]!"
    show bg ch5ellen67 with hpunch
    e "HOLY SHIT!!!"
    p "*Grunts*"
    menu:
        "Keep going":
            p "(Damn, Gotta hold on. Not ready for this to end.)"
            jump ch5ellenmenu
        "Cum inside her":
            show bg ch5ellen68 with dissolve
            p "Here it comes."
            e "Stop fucking narrating!"
            p "AAAAH!!!"
            show bg ch5ellen69 with quickflash
            p "Why don't we do this more often?"
            e "Because you piss me off sometimes. You finished?"
            p "*Breathes heavily.* Yeah."
            e "Me fucking too. Damn, [p], you do know your shit."
            e "Now I am fucking tired. How about some shut-eye?"
            p "Sounds good."
            jump ch5ellensexend
        "Cum on her":
            p "On your knees."
            show bg ch5ellen70 with dissolve
            e "Of course, [ellensexname]."
            e "Wow, does that dumb shit actually work."
            p "YES!"
            show bg ch5ellen71 with quickflash
            p "A lot!"
            e "Not the face!"
            show bg ch5ellen73 with dissolve
            $ renpy.pause(1)
            show bg ch5ellen72 with dissolve
            e "You're lucky."
            p "You were the one aiming. I was just there for the ride."
            e "[p], you go off like a fucking firehose. It's like holding on in hopes it goes where you want it to."
            p "Heh, sorry."
            e "Yeah, yeah, just let me wipe up. I am fucking tired."
            jump ch5ellensexend





label ch5ellensideways:
    show bg ch5ellen92 with dissolve
    p "*Grunts* Damn! What has gotten into you?"
    e "Just lay back."
    show bg ch5ellen93 with dissolve
    p "Something tells me I don't have a choice."
    e "Fucking right, you don't."
    e "Now let me... "
    show bg ch5ellen94 with dissolve
    p "Ugh! Your knee is completely digging at my side there."
    e "It's not my fault your too damn big."
    p "*Grunts* Just shift maybe to... "
    show bg ch5ellen95 with dissolve
    e "This so isn't going to work on this couch."
    show bg ch5ellen96 with dissolve
    e "Ah-ha! Got it!"
    p "Okay?"
    show bg ch5ellen97 with dissolve
    e "This work for you?"
    p "Fuck yeah, it does!"
    show bg ch5ellenride4 movie with dissolve
    e "Good... Oh, wow! That's good!"
    p "You always made the best out of a tight situation."
    e "Wow, just shut it!"
    show bg ch5ellen99 with dissolve
    p "*Grunts with pleasure* No, I'm serious. You've always been quick on your feet."
    e "God damn! It's why you like me!"
    show bg ch5ellenride3 movie with dissolve
    p "That or I have a thing for being continuously berated."
    e "Fuck off, [ellensexname]!"
    p "I guess I do!"
    e "Ah, you love it!"
    show bg ch5ellen98 with dissolve
    e "Fuuuuuck! Like I love this!"
    p "Fucking fantastic, Ellen."
    e "More to go! What's next?"
    jump ch5ellenmenu


label ch5ellensexend:
    show bg ch5ellen76 with dissolve
    e "Alright, scootch."
    p "Ugh, alright! Good enough?"
    show bg ch5ellen79 with dissolve
    e "Enough."
    p "Good."
    if "ch5ellenkiss" in extraevents:
        e "[p], am I still drunk or did you fucking kiss me?"
        p "I did. You pissed?"
        e "No... Just... You never did that before."
        p "You kissed me too."
        e "Well... after... didn't want to be rude."
    show bg ch5ellen80 with dissolve
    e "Now shut up. Sleepy..."
    show bg ch5ellen83 with dissolve
    p "*Sighs* How does everyone do that?"
    if "ch4vicaccept" in extraevents:
        p "(What the hell am I doing?)"
        p "(I still need to find a way to get Gloria to Victoria. Ellen will understand once it's done. Or kill me. But... This is for the best, for everyone.)"
    elif "ch4vicgoodbye" in extraevents or "ch4vicsex" in extraevents:
        p "(What the hell am I even doing? No matter what I do, it doesn't change things.)"
        p "(I need to come up with something fast, or we're all dead. And it's all my fault. Ellen doesn't deserve that. )"
    p "(We'll see what the morning brings.)"
    $ renpy.end_replay()
    if not persistent.ch5ellensex:
        $ renpy.notify(['Scene Unlocked', 'unlock'])
        $ persistent.ch5ellensex = True
    $ extraevents.append("ch5ellennotop")
    jump ch5dream
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
