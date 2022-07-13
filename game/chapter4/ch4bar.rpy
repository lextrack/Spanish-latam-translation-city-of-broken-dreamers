image bg ch4breakfast1 = "ch4breakfast1"
image bg ch4breakfast2 = "ch4breakfast2"
image bg ch4breakfast3 = "ch4breakfast3"
image bg ch4breakfast4 = "ch4breakfast4"
image bg ch4breakfast5 = "ch4breakfast5"
image bg ch4breakfast6 = "ch4breakfast6"
image bg ch4breakfast7 = "ch4breakfast7"
image bg ch4breakfast8 = "ch4breakfast8"
image bg ch4breakfast9 = "ch4breakfast9"
image bg ch4breakfast10 = "ch4breakfast10"
image bg ch4breakfast11 = "ch4breakfast11"
image bg ch4breakfast12 = "ch4breakfast12"
image bg ch4breakfast13 = "ch4breakfast13"
image bg ch4breakfast14 = "ch4breakfast14"
image bg ch4breakfast15 = "ch4breakfast15"
image bg ch4breakfast16 = "ch4breakfast16"
image bg ch4breakfast17 = "ch4breakfast17"
image bg ch4breakfast18 = "ch4breakfast18"
image bg ch4breakfast19 = "ch4breakfast19"
image bg ch4breakfast20 = "ch4breakfast20"
image bg ch4breakfast21 = "ch4breakfast21"
image bg ch4breakfast22 = "ch4breakfast22"
image bg ch4breakfast23 = "ch4breakfast23"
image bg ch4breakfast24 = "ch4breakfast24"
image bg ch4breakfast25 = "ch4breakfast25"
image bg ch4breakfast26 = "ch4breakfast26"
image bg ch4breakfast27 = "ch4breakfast27"
image bg ch4breakfast28 = "ch4breakfast28"
image bg ch4breakfast29 = "ch4breakfast29"
image bg ch4breakfast30 = "ch4breakfast30"
image bg ch4breakfast31 = "ch4breakfast31"
image bg ch4breakfast32 = "ch4breakfast32"
image bg ch4breakfast33 = "ch4breakfast33"
image bg ch4breakfast34 = "ch4breakfast34"
image bg ch4breakfast35 = "ch4breakfast35"
image bg ch4breakfast36 = "ch4breakfast36"
image bg ch4breakfast37 = "ch4breakfast37"
image bg ch4breakfast38 = "ch4breakfast38"
image bg ch4breakfast39 = "ch4breakfast39"
image bg ch4breakfast40 = "ch4breakfast40"
image bg ch4breakfast41 = "ch4breakfast41"
image bg ch4breakfast42 = "ch4breakfast42"
image bg ch4breakfast43 = "ch4breakfast43"
image bg ch4breakfast44 = "ch4breakfast44"
image bg ch4breakfast45 = "ch4breakfast45"
image bg ch4breakfast46 = "ch4breakfast46"
image bg ch4breakfast47 = "ch4breakfast47"
image bg ch4breakfast48 = "ch4breakfast48"
image bg ch4breakfast49 = "ch4breakfast49"
image bg ch4breakfast50 = "ch4breakfast50"
image bg ch4breakfast51 = "ch4breakfast51"
image bg ch4breakfast52 = "ch4breakfast52"
image bg ch4breakfast53 = "ch4breakfast53"
image bg ch4breakfast54 = "ch4breakfast54"
image bg ch4breakfast55 = "ch4breakfast55"
image bg ch4breakfast56 = "ch4breakfast56"


image bg ch4walk1 = "ch4walk1"
image bg ch4walk2 = "ch4walk2"
image bg ch4walk3 = "ch4walk3"
image bg ch4walk4 = "ch4walk4"
image bg ch4walk5 = "ch4walk5"
image bg ch4walk6 = "ch4walk6"
image bg ch4walk7 = "ch4walk7"
image bg ch4walk8 = "ch4walk8"
image bg ch4walk9 = "ch4walk9"
image bg ch4walk10 = "ch4walk10"


image ch4hairmovie = Movie(play='video/chapter-4-video/ch4hair.webm', loop=False)
image bg ch4hair movie:
    "ch4hairmovie"
    pause 3.95
    "ch4hairend"

image ch4venusmovie = Movie(play='video/chapter-4-video/ch4venus.webm', loop=False)
image bg ch4venus movie:
    "ch4venusmovie"
    pause 36.0
    "ch4venusend"


label ch4bar:
    play music audio.sol fadein 2.0 fadeout 2.0
    scene black with Dissolve(2)
    show bg ch4walk1 with Dissolve(2)
    p "Yeah, it's just down this way. Just follow the alley, you can't miss it."
    h "What's it called again?"
    p "Just look for a sign that says Barry's."
    show bg ch4walk2 with dissolve
    g "Do you hear that?"
    p "Hear what?"
    n "You stop for a moment and listen. Around the corner, you can hear commotion overtaking the regular morning traffic."
    show bg ch4walk3 with dissolve
    h "It's coming from down this way."
    show bg ch4walk4 with dissolve
    g "Whoa, looks like some kind of protest or something."
    p "Must be Tuesday. Good for us, though. No one will care about some quiet people in the back."
    scene black with Dissolve(1)
    show bg ch4breakfast3 with dissolve
    h "Is this the place?"
    p "Like I said, a dive. Grub's cheap, cops hate it, perfect for us."
    show bg ch4breakfast1 with dissolve
    g "So, we just sit anywhere?"
    p "Yeah, if you wait for one of the waiters to seat you, we'll be here forever."
    show bg ch4breakfast2 with dissolve
    g "When you said dive, I expected worse. You know, a few flowers and this place wouldn't be half bad."
    p "I don't think flowers are in the cards here."
    scene black with dissolve
    show bg ch4breakfast4 with dissolve
    g "Also, um... Henry, do we have any money or anything? I promise to pay you back..."

    if h_score >= 2:
        show bg ch4breakfast5 with dissolve
        h "I can cover the food."
        p "I got it. Don't worry about it."
        h "I can take care of her perfectly well. I don't need you covering us."
    else:
        show bg ch4breakfast6 with dissolve
        h "Don't expect me to be covering your tab, Ghost."
        p "That's fine. I got yours, don't sweat it."
        h "Look here-"
    show bg ch4breakfast7 with dissolve
    g "Hey, stop. This isn't the place."
    h "..."
    show bg ch4breakfast8 with dissolve
    g "If you're going to fight, don't make it about something like the check, okay?"
    h "*Grumbles*"
    h "Fine."
    show bg ch4breakfast9 with dissolve
    g "Thank you, [p]."
    p "Don't mention it. At least not until you don't get food poisoning."
    show bg ch4breakfast10 with dissolve
    h "Sorry... thanks, Ghost."
    g "See, that's not so hard! We're all getting along now."
    "Server" "Welcome to Barry's. What d'ya want?"
    show bg ch4breakfast11 with dissolve
    g "Shit, you scared me."
    show bg ch4breakfast12 with dissolve
    "Server" "Uh, huh. So, what do you want? Coffee?"
    show bg ch4breakfast14 with dissolve
    g "No, anything but coffee. I'll just have bacon and eggs, I guess...?"
    "Server" "Sure thing, toots."
    "Server" "For you?"
    show bg ch4breakfast13 with dissolve
    h "Ahh... eight eggs over easy, ten pancakes, two sides of sausages and bacon, and throw in an orange for good measure."
    p "I think I may take back that offer to pay, now."
    g "I'll get you back sometime. I promise."
    show bg ch4breakfast15 with dissolve
    "Server" "For you?"
    p "Same as her. So, what's with the flakes out there?"
    "Server" "Ahh, I think that milcher law passed or something. I don't know, but they're pissed about it."
    "Server" "Anything else, Sugar?"
    p "Nah, just the food."
    show bg ch4breakfast16 with dissolve
    g "So, Proposition 1019 passed?"
    p "Which one was that again?"
    g "The one that says I need permission to have kids."
    g "*Sighs* It gets worse every day."
    h "Gloria..."
    g "It's not like I was planning on kids anytime soon anyway. It's fine..."
    play music audio.tense fadein 1.0 fadeout 1.0
    show bg ch4breakfast17 with dissolve
    "Police Bot" "Perform perimeter sweep."
    g "Shouldn't they be outside with the protest?!"
    show bg ch4breakfast19 with dissolve
    p "LAPD, they're nothing if not proactive. It's a standard trouble scan. Stay calm."
    p "The problem is that Gloria here is designated trouble."
    show bg ch4breakfast20 with dissolve
    h "I'll cause a distraction. As soon as I do, grab her and run out the back."
    show bg ch4breakfast21 with dissolve
    g "Wait... *Begins to grimace.*"
    h "Gloria, stop!"
    p "Ahh, shit!"
    show bg ch4hair movie with dissolve
    p "Okay, neat trick!"
    p "But, facial recognition will still spot you. Don't let it get a good look."
    p "Act casual..."
    show bg ch4breakfast22 with dissolve
    g "..."
    p "Easy now..."
    show bg ch4breakfast24 with dissolve
    "Police Bot" "Remain calm; this is a standard security sweep."
    p "So, umm, did you catch the game?"
    show bg ch4breakfast25 with dissolve
    h "Oh yes! When the Expos beat the Raptors by a touchdown! Incredible!"
    p "Yeah, I couldn't believe... Okay, enough of that, it's gone."
    show bg ch4breakfast30 with dissolve
    g "That was kind of embarrassing, Henry."
    h "He should have known better than to ask me to lie."
    p "Noted for the future."
    show bg ch4breakfast31 with dissolve
    g "Are more going to show? I don't think we're going to be so lucky next time."
    p "Standard sweeps are every hour in a situation like this, so we have some time to figure it out."
    g "But we still have this protest going on in the neighborhood. Hard to control a situation like that."
    h "Back to Dr. Hamilton?"
    p "We are just buying time at best. We need out of the area."
    g "Don't professional kidnappers like you have a safe house for times like this?"
    p "No! It's not like that. I'd usually drop you off to my..."
    show bg ch4breakfast25 with dissolve
    h "What?"
    p "I know where we can go. But she's going to kill me. "
    h "Who?"
    show bg ch4breakfast26 with dissolve
    h "*Grits his teeth* Agggh... One sec..."
    show bg ch4breakfast28 with dissolve
    g "Henry, what's wrong?"
    h "It's nothing."
    g "That's not a nothing face, Bigs."
    show bg ch4breakfast27 with dissolve
    h "I said it's nothing. I worry about you, remember? Just, give me a second, I need to hit the head before the food gets here."
    p "Of course."
    show bg ch4breakfast31 with dissolve
    play music audio.sol fadein 6.0 fadeout 2.0
    g "It took me three years before I figured out what he meant by saying that."
    p "The head? Yeah, military slang. It sticks."
    g "You military before you became all ghost-y?"
    p "Yeah. Look, I have some questions. You probably do too."
    g "I do, but you go first."
    $ resetmenu()
    jump ch4barmenu


label ch4barmenu:
    menu:
        "Your powers" if menu1:
            $ menu1 = False
            p "So, these powers you have. How do they work?"
            g "Well, you just came out with it, huh?"
            p "Yeah."
            show bg ch4breakfast35 with dissolve
            g "Fair enough. I don't really know how they work. It just happens."
            g "It started a few years ago. I was listening to some music and suddenly, Donut moved."
            p "Donut?"
            g "Sorry... My bear, had it since I was a kid. Mom gave it to me."
            show bg ch4breakfast37 with dissolve
            g "I thought he moved on his own. Some kind of cheap horror movie, you know?"
            g "Anyway, after a while, I figured out I did it. Following that, I started moving little things around."
            g "It was sort of fun. But then... "
            p "Have you ever used it like you did last night?"
            show bg ch4breakfast36 with dissolve
            g "Once or twice... I can't really remember when it happens like that."
            p "That has to be terrifying!"
            show bg ch4breakfast34 with dissolve
            g "Of course it is! Do you know what it's like waking up not knowing if you hurt people?"
            p "You were protecting yourself. "
            g "Yeah, I know. But, I never wanted to hurt anybody."
            p "Sorry... I won't press the matter."
            jump ch4barmenu
        "Your family" if menu2:
            $ menu2 = False
            p "So, I bumped into your father the other night."
            show bg ch4breakfast35 with dissolve
            g "Trying to find out where I was?"
            p "That's the gist of it, yeah."
            g "Is he doing alright?"
            p "I was expecting you to say something different."
            show bg ch4breakfast36 with dissolve
            g "What? That I hate him for throwing me out as a kid?"
            p "Something along those lines."
            g "My friends say...or... well, said I should hate him, but I can't. Mom's passing struck him hard."
            p "Are you ok with that?"
            g "He's lost. I'm sure he had his reasons, but he's not a bad man."
            menu:
                "Mention her room":
                    $ g_score += 1
                    p "I did see your room. It doesn't look like he could ever bring himself to touch it."
                    if menu1 == False:
                        p "I think I met your Donut. Purple bear?"
                        g "*Chokes up* Yeah..."
                    else:
                        g "*Chokes up* Was my bear still there?"
                        p "Purple guy? Yeah, he was."
                    show bg ch4breakfast33 with dissolve
                    g "*Sniffle while holding back tears* And my posters and stuff? He always hated that Ellen poster."
                    p "All there. The room looked pristine."
                    g "I don't know if it makes me feel better or worse."
                    p "I can't tell you that."
                    show bg ch4breakfast32 with dissolve
                    g "What can you tell me?"
                    p "Well, you seem like a good kid. You didn't deserve this."
                    show bg ch4breakfast37 with dissolve
                    g "Thanks."
                    "Gloria takes a deep breath and sits in thought, contemplating her old life. You still feel there is something she's not telling you."
                    if "ch2chooseellen" in extraevents:
                        p "(What has this poor girl been through?)"
                "Mention Shanlon":



                    p "That women he is with can't help."
                    show bg ch4breakfast37 with dissolve
                    g "I'd hoped to hear they broke up."
                    p "If it makes you feel better, I don't think they're particularly happy together."
                    g "She never liked me, from like the first day they started dating. And when she found out..."
                    show bg ch4breakfast36 with dissolve
                    g "I know that she had something to do with kicking me out."
                    p "Evil stepmothers are a cliche for a reason. My Dad's girlfriend... god, I hated that bitch."
                    g "Should we compare notes? Still, I think evil bigot who seduced my Dad wins."
                    p "Don't be too sure."
                    if "ch2broken" in extraevents:
                        p "(Now I really want to give it to that royal bitch queen the next time I see her.)"

            jump ch4barmenu

        "The dreams" if menu3:
            $ menu3 = False
            p "This may sound strange. But I think I saw you in my dreams."
            show bg ch4breakfast35 with dissolve
            g "A red hallway filled with death and pain."
            p "You could put it that way."
            g "You were in a panic, you and a woman."
            p "Also yes."
            g "She cares for you."
            p "Well, two out of three."
            show bg ch4breakfast32 with dissolve
            g "And you were there when my Mom..."
            p "When she died. I was, I'm sorry."
            g "I don't understand, though. I've had these dreams for years, why are we seeing each other now?"
            p "I was hoping you could answer that."
            g "*Shakes her head* ..."
            jump ch4barmenu


        "Ellen" if menu1 == False or menu2 == False or menu3 == False:
            p "Remember how I said we might have a place to go?"
            show bg ch4breakfast35 with dissolve
            g "Yeah?"
            p "And that she may not be too happy about this."
            g "Umm, yeah..."
            p "So that friend is Ellen Lane."
            show bg ch4breakfast37 with dissolve
            g "I think we're past the point of you lying to get me to go home with you."
            p "What? No! I've been friends with Ellen for a while now."
            g "Uh-huh, pull the other one."
            p "I'm serious."
            g "So prove it."
            p "How am I supposed to do that?"
            show bg ch4breakfast41 with dissolve
            g "Huh, good point. Tell me something, only a friend of hers would know."
            p "Uh..."
            menu:
                "She's a demon in the sack.":
                    p "Not sure if what I can say is appropriate."
                    g "So you don't know her."
                    p "Just not sure if she'd want me to say anything."
                    g "Yeah, right. You're just coming up with excuses."
                    p "Ah, who am I kidding, this is Ellen."
                    p "She's a demon in the sack."
                    show bg ch4breakfast39 with dissolve
                    g "What?"
                    p "So, the first time we hooked up, it was after she offered me a job. She was trying to get together with this hot bartender."
                    g "You're not kidding."
                    p "Nope. It turns out the bartender was straight as an arrow, I laughed as she got shut down and next thing I know I'm getting pulled into the back room of the Noir and she's ripping off my pants."
                    show bg ch4breakfast40 with dissolve
                    g "TOO MUCH INFORMATION!"
                    p "Believe me now?"
                    g "Yes. Fine... which makes you pretty cool. And you like to overshare. So I can see why you'd be friends with her."
                "She hates your Dad":
                    $ g_score += 1
                    p "Well, she hates your dad."
                    g "Easy guess."
                    p "Not a guess. She said this job was personal. Had to check your last name twice before I put two and two together."
                    g "Heh, still... That's a shame."
                    p "A shame?"
                    g "I don't know. Ellen was discovered by my Mom, back when I was a kid. Heck, Ellen was probably younger then than I am now."
                    p "But I know your Dad screwed her over."
                    g "Yeah, Dad... changed after Mom died. And Ellen suffered for it. I still don't know the details."
                    p "You never asked her?"
                    g "No. And Dad..."
                    show bg ch4breakfast40 with dissolve
                    g "I can see it in your eyes that you are telling the truth. You really do know her."
                    p "I said I did."
                "She told me about the first time you met" if "ch2chooseellen" in extraevents:
                    $ g_score += 1
                    p "*In the background* Ellen told me your mother, Helena, brought you backstage when she was starting out. Said you gave her-"
                    g "STOP! DO not continue the embarrassing story of tiny me fangirling like an idiot!"
                    p "Lips sealed."
                    g "You're not kidding me, are you?"
                    p "Not in the slightest."
                    show bg ch4breakfast40 with dissolve
                    g "This is prime insane! You know that?"

            if h_score >= 2:
                show bg ch4breakfast42 with dissolve
            else:
                show bg ch4breakfast43 with dissolve
            g "How did you meet?! I have so many questions!"
            show bg ch4breakfast44 with dissolve
            g "Like, does she still play the guitar all the time?! I loved it when she did that."
            p "Not sure about that, actually."
            g "Does she still sing on the balcony? But seriously! HOW DID YOU MEET?"
            p "She's my fixer."
            g "She's your what?"
            p "She's like a go-between, between a client and myself. Fixers get the jobs. Then they dish them out to guys like me."
            g "Wow, so she's like a rock and roll spy?"
            p "Eh, it's not as glamorous as you'd think."
            show bg ch4breakfast46 with dissolve
            h "You seem excited."
            g "Henry! He knows Ellen!"
            if h_score >= 2:
                show bg ch4breakfast47 with dissolve
                h "I heard. Be nice to see a friendly face."
            else:
                show bg ch4breakfast48 with dissolve
                h "So I heard."
            show bg ch4breakfast49 with dissolve
            h "So, Ghost, what now?"
            p "Now, I make a call, then we eat. You can listen in all you want. Just want to secure a place to lay low."
            h "Go ahead."
            jump ch4barellen


label ch4barellen:
    scene black with dissolve
    show bg ch4breakfast56 with dissolve
    menu:
        "Call Ellen":
            p "(Ellen is going to be through the roof.)"
        "Watch Venus Ad":
            p "Huh, may as well."
            play music audio.party fadein 3.0
            scene black with Dissolve(1)
            window hide
            show bg ch4venus movie with dissolve
            $ renpy.pause()
            p "(Wow, they are pulling out all the stops on this one.)"
            p "(Heh, Betty, is going to make a fucking fortune.)"
            p "(Best not waste any more time. Ellen is going to lose her top...)"
            play music audio.sol fadein 2.0 fadeout 2.0

    p "([p], what the fuck are you doing..?)"
    show bg ch4breakfast50 with dissolve
    p "Come on, Ellen. Wake up."
    show bg ch4breakfast53 with dissolve
    e "Ahh, [p]? The fuck is wrong with you?"
    p "Good morning to you, too."
    e "Good morning?! I have a shitload of questions here! One, why the FUCK are you calling for business on an unregistered number?"
    e "Two: Where the FUCK are you! I... people are worried sick!"
    e "And Three: Where is Gloria? Is she ok?"
    p "Ahh, one, I think Sam might be compromised, so I called from here. Two, I'm in a bar. Three, Gloria and her bodyguard are about twenty feet away from me inside of said bar."
    p "And four, you miscounted, she's fine."
    show bg ch4breakfast54 with dissolve
    e "YOU'RE WHAT? You were supposed to take her to Baynard, you moron! Are you spectrumed or something? Get her there before the police..."
    p "No."
    show bg ch4breakfast55 with dissolve
    e "Fuck you, [p], even if this wouldn't tank my fucking rep, and yours, worse than it fucking already is, if the cops find her, she is going to fucking jail."
    p "Ellen, wait..."
    if "ch2chooseellen" in extraevents:
        e "What, you think her piece of shit father is going to give you more for her? I thought I fucking knew you! But if you went to that piece of shit after everything..."
    else:
        e "You should know her dad isn't going to pay more than Baynard for her, you idiot!"
    p "Ellen, stop! Listen for a minute."
    show bg ch4breakfast54 with dissolve
    e "One minute. That's it."
    p "I don't know what Baynard told you, but they aren't looking to help her. That whole cure thing is a cover. She's no cure. She's a weapon."
    e "What the fuck are you talking about? I know that girl, she's no fucking weapon!"
    p "Trust me, Ellen. It will all make sense when I show you."
    e "Don't see how."
    p "In-person..."
    show bg ch4breakfast52 with dissolve
    e "Fine. You can't come here, though."
    p "No shit. I have a better idea. You remember that loft you practiced in?"
    e "Yeah, Thor left me the key. The place is a dump."
    p "Yeah, and you told me the paparazzi don't even know about it. Meet us there, no tech, and make sure you aren't followed."
    e "This is fucking crazy..."
    p "Ellen, please."
    e "If this wasn't Gloria... I'd have fucking called you in by now. I hope you know that."
    p "I know."
    e "*Sighs* I'll meet you there."
    p "Thanks."
    e "Yeah, yeah..."
    show bg ch4breakfast51 with dissolve
    p "(Alright. Problem solved, or made more complicated. Depends how I look at it.)"
    jump ch4docsafter
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
