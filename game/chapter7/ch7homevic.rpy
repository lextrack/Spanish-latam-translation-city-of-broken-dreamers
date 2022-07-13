label ch7homevic:
    show bg ch7home10 with dissolve
    if v_score >= 4:
        jump ch7vicnice
    else:
        jump ch7vicaccept


label ch7vicaccept:
    play music audio.futurenoir fadein 2.0 fadeout 2.0

    v "Agent."
    p "Victoria... What are you doing here?!"
    show bg ch7home135 with dissolve
    v "Spare me the questions, Agent. I am the one who will be asking them."
    p "Then ask."
    show bg ch7home136 with dissolve
    v "My reports are telling me Miss Conner is on the run. Did you lose control?"
    if "ch7nabgloria" in extraevents:
        p "I tried to bring her in last night."
        v "And it would appear you have failed us once again."
        p "..."
    else:
        p "She took off early in the morning. I don't know where she went, but we're looking."
    show bg ch7home137 with dissolve
    v "My patience has run thin. Mrs. White would rather have you removed from the situation entirely."
    p "Why haven't you? The fact you still have any trust in me is remarkable."
    show bg ch7home139 with dissolve
    v "My trust in you vanished long ago, but..."
    p "But what?"
    v "You're a means to an end. I need you to succeed. I put too much at stake in hiring you. You won't fail me."
    v "You would be horribly disappointed if you did. So many things you would miss."

    show bg ch7home140 with dissolve
    v "Like these."
    v "You like my thighs don't you."
    p "Yes..."
    show bg ch7home141 with dissolve
    v "You want to spread them wide? Bury yourself in my warmth?"
    p "Yes..."
    show bg ch7home138 with dissolve
    v "Umm. I have a story to tell you."
    show bg ch7home142 with dissolve
    $ renpy.pause(1)
    show bg ch7home143 with dissolve
    v "Come closer, Agent..."
    p "What is it?"
    v "A story. One that tells of how pleasurable it can be when a new deal goes well. Would you like the hear it?"
    menu:
        "Tell me everything":
            v "Are you sure?"
            menu:
                "Yes":
                    p "I am."
                    jump ch7meredithsex
                "Just get to the point":
                    jump ch7homevicgettopoint
        "Just get to the point":

            jump ch7homevicgettopoint

label ch7homevicgettopoint:
    p "Not particularly."
    show bg ch7home144 with dissolve
    v "Is that a hint of jealously I sense? Fine, I'll spare you the details."
    p "What was this deal?"
    show bg ch7home150 with dissolve
    v "A bold one."
    p "What do you mean?"
    v "You will see soon enough."
    jump ch7homevicafter


label ch7homevicafterstory:
    p "And what about me? Am I just a game?"
    $ achievement.grant("NEGOTIATIONS")
    init:
        $ achievement.register("NEGOTIATIONS")
    $ achievement.Sync()
    $ extraevents.append("ch7vicdep")
    $ renpy.end_replay()
    if not persistent.ch7vicdep:

        $ renpy.notify(['Scene Unlocked', 'unlock'])
        $ persistent.ch7vicdep = True


    show bg ch7home150 with dissolve
    v "Of course you are. Just a far more interesting player."
    jump ch7homevicafter


label ch7homevicafter:
    menu:
        "Ask her to leave":
            p "I think you should go."
            v "Very well."
            show bg ch7home166 with dissolve
            v "But know this, Agent. I won't accept any more delays. The time for subtlety is over."
            show bg ch7home167 with dissolve
            p "..."
            s "Sir, we should probably leave."
            p "Fuck, that girl that was following us, is she still outside?"
            s "Yes, Sir."
            menu:
                "We will lose her on the road":
                    p "Rather not stir up more shit."
                    jump ch7apartmentignore
                "Confront her":
                    p "Let's see what she wants, shall we?"
                    jump ch7apartmentrush
        "Get angry":

            show bg ch7home145 with vpunch
            v "Agh!"
            p "You're just a god damn snake!"
            show bg ch7home146 with dissolve
            $ renpy.pause(1)
            show bg ch7home147 with dissolve
            n "Victoria forcefully pulls your hand away"
            show bg ch7home148 with dissolve
            v "Don't you dare do anything like that again."
            menu:
                "Apologize":
                    p "I'm sorry... I don't know what came over me."
                    show bg ch7home149 with dissolve
                    v "I understand this is stressful for you, but that is not an excuse."
                    show bg ch7home166 with dissolve
                    v "I will leave you to your own devices, Agent. But know this, the situation must come to its conclusion swiftly."
                    show bg ch7home167 with dissolve
                    p "..."
                    s "Sir, we should probably leave."
                    p "Fuck, that girl that was following us, is she still outside?"
                    s "Yes, Sir."
                    menu:
                        "We will lose her on the road":
                            p "Rather not stir up more shit."
                            jump ch7apartmentignore
                        "Confront her":
                            p "Let's see what she wants, shall we?"
                            jump ch7apartmentrush
                "Hit her":
                    $ dep += 1
                    $ extraevents.append("ch7vicredmoon")
                    p "I'll do what I want!"
                    show bg ch7home152 with dissolve
                    $ renpy.pause(1)
                    show bg ch7home153 with dissolve
                    v "Huh?"
                    $ v_score -= 2

                    n "Mid-swing, your intended blow is abruptly stopped, followed by intense pain, as a cold hand begins to crush down on yours"
                    p "AGGGHH!"
                    show bg ch7home154 with dissolve
                    "Red Moon" "So uncivilized... To imagine, even I am more human than you."
                    "Red Moon" "With this world filled with people like you, perhaps it is best left to rot."
                    show bg ch7home155 with dissolve
                    n "With a quick motion, you are flung across the room"
                    show bg ch7home156 with dissolve
                    "Red Moon" "What's this? Was that meant for me?"
                    p "Ugh... What?"
                    show bg ch7home168 with dissolve
                    "Red Moon" "Hmmm, I think not. You shall not be needing this."
                    if "ch7ammo" in extraevents:
                        $ extraevents.remove("ch7ammo")

                    show bg ch7home169 with vpunch
                    p "Fuck me..."
                    show bg ch7home157 with dissolve
                    "Red Moon" "Now, get up!"
                    show bg ch7home158 with hpunch
                    p "*Gasping for breath* I-I!"
                    "Red Moon" "Why they let you live is a mystery to me. I'd sooner squash you like an ant."
                    "Red Moon" "Your only mercy is that it will be quick."
                    show bg ch7home159 with dissolve
                    v "Stop... He may be still be of use."
                    "Red Moon" "I highly doubt that. He only complicates matters."
                    v "It's my call. He may be juvenile, but that doesn't deserve a death sentence. Now let him go before you kill him."
                    "Red Moon" "Very well."
                    show bg ch7home161 with dissolve
                    p "*Takes in a huge breath*"
                    v "Leave him. He knows what he needs to do."
                    show bg ch7home160 with dissolve
                    v "After he does, you can settle matters with this Mr. Gibson in whatever manner you see fit."
                    show bg ch7home162 with Dissolve(1)
                    p "*Coughing* Sam... Ugh, fuck..."
                    s "Are you alright, Sir?"
                    p "No, I'm not alright."
                    s "Sorry, my biological scans where focused on that individual. Sir, he is almost entirely machine."
                    p "No shit..."
                    s "May I also make another observation?"
                    p "Sure."
                    show bg ch7home163 with dissolve
                    s "Next time, don't be an ass."
                    p "Yeah, yeah... I lost my cool."
                    s "Clearly, sir. But, ethically, that is no excuse."
                    s "By the way, my scans are still detecting that same individual in the hallway."
                    show bg ch7home162 with dissolve
                    p "Great... Just give me a minute."
                    s "Of course, what are you plans for her?"
                    menu:
                        "We will lose her on the road":
                            p "Rather not stir up more shit. Especially after that."
                            jump ch7apartmentignore
                        "Confront her":
                            p "Ugh.. Let's just see what she wants."
                            jump ch7apartmentrush



image ch7homepanout = Movie(play='video/chapter-7-video/ch7homepanout.webm', loop=False)
image bg ch7homepanoutmovie movie:
    "ch7homepanout"
    pause 10.0
    "ch7homepanout-end"

image ch7homedance = Movie(play='video/chapter-7-video/ch7homedance.webm', loop=False)
image bg ch7homedancemovie movie:
    "ch7homedance"
    pause 7.0
    "ch7homedance-end"

image ch7homecumshot = Movie(play='video/chapter-7-video/ch7homecumshot.webm', loop=False)
image bg ch7homecumshotmovie movie:
    "ch7homecumshot"
    pause 13.0
    "ch7homecumshot-end"


image bg ch7homeanal1 movie = Movie(play="video/chapter-7-video/ch7homeanal1.webm")
image bg ch7homeanal2 movie = Movie(play="video/chapter-7-video/ch7homeanal2.webm")
image bg ch7homeanal3 movie = Movie(play="video/chapter-7-video/ch7homeanal3.webm")
image bg ch7homeblow movie = Movie(play="video/chapter-7-video/ch7homeblow.webm")
image bg ch7homeeat movie = Movie(play="video/chapter-7-video/ch7homeeat.webm")
image bg ch7homefacesit movie = Movie(play="video/chapter-7-video/ch7homefacesit.webm")
image bg ch7homefuck1 movie = Movie(play="video/chapter-7-video/ch7homefuck1.webm")
image bg ch7homefuck2 movie = Movie(play="video/chapter-7-video/ch7homefuck2.webm")
image bg ch7homefuck3 movie = Movie(play="video/chapter-7-video/ch7homefuck3.webm")
image bg ch7homefuck4 movie = Movie(play="video/chapter-7-video/ch7homefuck4.webm")
image bg ch7homefuck5 movie = Movie(play="video/chapter-7-video/ch7homefuck5.webm")

image bg ch7homethroat1 movie = Movie(play="video/chapter-7-video/ch7homethroat1.webm")
image bg ch7homethroat2 movie = Movie(play="video/chapter-7-video/ch7homethroat2.webm")
image bg ch7homethroat3 movie = Movie(play="video/chapter-7-video/ch7homethroat3.webm")
image bg ch7homethroat4 movie = Movie(play="video/chapter-7-video/ch7homethroat4.webm")

image bg ch7hometitplay movie = Movie(play="video/chapter-7-video/ch7hometitplay.webm")
image bg ch7hometits movie = Movie(play="video/chapter-7-video/ch7hometits.webm")



label ch7vicnice:

    play music audio.futurenoir fadein 2.0 fadeout 2.0

    v "[p]..."
    show bg ch7homepanoutmovie movie with dissolve
    if "ch3findbug" in extraevents:
        p "Victoria... What are you doing here?"
        if "ch3disablebug" in extraevents:
            p "Victoria... How did you know I was here?"
            v "I have other means than a simple camera, but that is not important. It's why I'm here."
    else:
        p "Victoria... How did you know I was here?"
        v "How I am here is not important. It's why I'm here."
    v "I have information for you."
    v "Important information."
    show bg ch7home11 with dissolve
    p "You seem nervous about it."
    v "Yes, well, my presence here could easily result in my termination."

    show bg ch7home12 with dissolve
    v "I still don't understand your motives regarding Miss Connor... But..."
    p "But what?"
    v "My intel suggests she is on the move... Vostok has been attempting to track her location."
    v "Her last confirmed location was in Redondo Beach."
    $ extraevents.append("ch7victell")
    show bg ch7home14 with dissolve
    v "She ran, didn't she?"
    p "Sam, send that info to our friends. See if it can help them."
    s "Done, Sir."
    p "I appreciate the help, Victoria. But why help me? Why now?"
    show bg ch7home13 with dissolve
    v "I made a mistake. I should never have selected you for this job."
    v "I didn't know the full scope of your last mission with Baynard. Thus, I made a critical error."
    p "Didn't expect me to have a conscience? To be fair, I thought I lost it long ago."

    if "ch3vicnothanks" in extraevents:
        show bg ch7home18 with dissolve
        v "It was my failure, [p]. And what bothers me is that I think it might be for the best."
        v "You have no idea the sacrifices I have made to get where I am. Now I feel it might all have been for nothing."
        show bg ch7home19 with dissolve
        p "You knew what you had signed up for when joining with Baynard."
        show bg ch7home14 with dissolve
        v "I am not asking for pity I don't deserve. If we meet again, Agent, I hope it is on better terms."
        p "I hope so too. Thank you."
        v "Of course. I'll leave you now."
        show bg ch7home164 with dissolve
        v "One last thing. There is a suspicious-looking girl outside your place."
        p "I'm well aware."
        v "Of course. Goodbye, [p]."
        show bg ch7home165 with dissolve
        p "Alright, Sam, we need to move."
        s "And said girl, Sir?"
        menu:
            "We will lose her on the road":
                p "Rather not stir up more shit."
                jump ch7apartmentignore
            "Confront her":
                p "Let's see what she wants, shall we?"
                jump ch7apartmentrush
    else:
        v "Hiring you was a mistake."
        show bg ch7home19 with dissolve
        menu:
            "Move closer to her":
                jump ch7vicsex
            "Agree with her":
                p "Maybe, but it was also the right thing to do. If that location helps us..."
                show bg ch7home14 with dissolve
                v "I felt you deserved my help. It won't be enough, but it might give her a fighting chance."
                p "Thank you."
                v "I have to go. Be careful, [p]. Let us hope we never see each other again."
                p "No, that's something I won't hope for."
                v "Thank you."
                show bg ch7home164 with dissolve
                v "One last thing. There is a suspicious-looking girl outside your place."
                p "I'm well aware."
                v "Of course. Goodbye, [p]."
                show bg ch7home165 with dissolve
                p "Alright, Sam, we need to move."
                s "And said girl, Sir?"
                menu:
                    "We will lose her on the road":
                        p "Rather not stir up more shit."
                        jump ch7apartmentignore
                    "Confront her":
                        p "Let's see what she wants, shall we?"
                        jump ch7apartmentrush

label ch7vicsex:
    if _in_replay:
        show bg ch7home19 with dissolve
        v "Hiring you was a mistake."
        $ setReplay()
        if persistent.ch7vicsexanal == True:
            $ v_lust = 2
        if persistent.ch7vicsex1 == True:
            $ dep = 1
        if persistent.ch7vicsex2 == True:
            $ v_lust = 2

    play music audio.cybernight fadein 5.0 fadeout 2.0
    $ extraevents.append("ch7vic")
    p "Was it?"
    show bg ch7home14 with dissolve
    v "Yes..."
    show bg ch7home15 with dissolve
    p "Is that what you really think?"
    v "No..."
    show bg ch7home16 with dissolve
    n "Victoria relaxes her breathing and slowly presses her lips against your hand"
    show bg ch7home20 with dissolve
    v "I needed to see you."
    p "Well, here I am."
    show bg ch7home21 with dissolve
    p "Feeling better?"
    v "Much, though, we so shouldn't be doing this. The world is spiraling out of control all around us."
    p "Right now that doesn't matter. Only you do."
    v "[p]. Kiss me."
    show bg ch7home22 with dissolve
    n "Your lips lock together, the tip of her tongue dances with yours"
    show bg ch7home23 with dissolve
    n "You hold her body close, as her breasts squeeze against your chest"
    show bg ch7home21 with dissolve
    p "Is it safe for you? Helping me, that is?"
    v "It doesn't matter anymore."
    show bg ch7home24 with dissolve
    v "I need this and I can tell you feel the same."
    show bg ch7home25 with dissolve
    p "I do."
    show bg ch7home26 with dissolve
    v "However, I won't be needing this."
    show bg ch7homedancemovie movie
    p "When you said you needed this as much as I do..."
    v "Yes?"
    p "That may not have been entirely accurate."
    show bg ch7home27 with dissolve
    v "Well, why argue the details? Now, come closer."
    p "Of course."
    show bg ch7home28 with dissolve
    v "Mmm, I love the way you touch me."
    p "Your body is irresistible."
    show bg ch7home29 with dissolve
    v "Then take my panties off so you can enjoy more of it."
    show bg ch7home30 with dissolve
    $ renpy.pause(1)
    show bg ch7home31 with dissolve
    $ renpy.pause(1)
    show bg ch7home32 with dissolve
    v "I take it that is more to your liking?"
    p "You would be very correct."
    show bg ch7home36 with dissolve
    v "Take your clothes off. All of them."
    scene black with Dissolve(1)
    show bg ch7home33 with Dissolve(1)

    if vicsexname == False:
        v "Do you have a pet name you like, perhaps?"
        menu:
            "Have her call you something else":
                p "That being said, would you mind calling me..."
                v "Calling you what?"
                python:
                    vicsexname = renpy.input("What do you want her to call you?")
                    vicsexname = vicsexname.strip()

                    if not vicsexname:
                        vicsexname = p
                if vicsexname == "Agent" or vicsexname == "agent":
                    v "Heh, very funny."
                    v "You're a strange one. [vicsexname], it stays, then."
                $ persistent.vicsexname = vicsexname
                v "Very well, [vicsexname]."
            "[p] is fine":

                $ vicsexname = p

    v "Much better. Now, [vicsexname], I want you to come to me."
    v "I need you inside me."
    show bg ch7home34 with dissolve
    n "You get behind Victoria, the heat from her pussy rising around you"
    v "Mmmm... "
    show bg ch7home35 with dissolve
    p "You don't want to waste any time do you?"
    v "I need you to fuck me first, then we can have more fun."
    show bg ch7home37 with dissolve
    n "As Victoria stares at you, you push your cock into her dripping wet pussy"
    v "Ahh... Thank you. Now, deeper."
    show bg ch7home40 with dissolve
    n "Lifting her leg up, you do just as she asks, pushing in even deeper"
    v "Now, fuck me, [vicsexname]!"
    show bg ch7homefuck1 movie with dissolve
    n "In the heat of the moment, you start fucking her against the wall"
    v "God yes!"
    p "Shit, you are so tight!"
    show bg ch7home39 with dissolve
    v "Ohhh yes!"
    n "Victoria lets out a huge breath as her pussy pulsates around your cock"
    show bg ch7home38 with dissolve
    v "Mmm.. That was a good start."
    p "Yeah?"
    show bg ch7home41 with dissolve
    $ renpy.pause(1)
    show bg ch7home42 with dissolve
    v "It's funny. When I was younger, I thought Romeo and Juliet was silly. Yet, here we are."
    v "I know we shouldn't be doing this."
    v "Different sides. Each with our own obligations, we shouldn't be doing this."

    p "Damn what we should and shouldn't. I just want you."
    show bg ch7home43 with dissolve
    v "Likewise. And you have to admit, the forbidden nature of this adds a little spice."
    p "Don't forget, it's dangerous too."
    show bg ch7home44 with dissolve
    v "How could I ever forget that?"
    v "Heh, I see you where your eyes are. Go ahead."
    show bg ch7hometits movie with dissolve
    v "Mmm... I like that."
    p "I can tell."
    v "I do, but no need to be so gentle."
    show bg ch7home45 with dissolve
    v "Ah..."
    show bg ch7home46 with dissolve
    v "Mmm, now come here and let me pleasure you."
    $ resetsexmenu()
    jump ch7vicsexmenu1

label ch7vicsexmenu1:
    menu:
        "Let her pleasure you":
            $ sexmenu1 = False
            jump ch7homeblow1
        "Pleasure her instead":

            jump ch7homepussy
        "Cum" if sexmenu1 == False or sexmenu2 == False:
            jump ch7homecum1


label ch7homeblow1:
    show bg ch7home47 with dissolve
    if sexmenu2 == False:
        v "Now it's your turn."
    else:
        v "Now, come here."
    p "Shit, you are sexy."
    v "Let me taste you."
    show bg ch7home48 with dissolve
    v "Mmmm..."
    p "Ohhh..."
    show bg ch7homeblow movie with dissolve
    v "Do you...Mmmm... Like.... That?"
    p "I have an idea."
    v "Mmmm... Yes?"
    show bg ch7home49 with dissolve
    v "Oh? And what kind of idea is this?"
    show bg ch7home50 with dissolve
    v "So you want to be adventurous I see, [vicsexname]."
    p "With you, always."
    v "Just let me."
    show bg ch7home55 with dissolve
    p "Phew... That's it."
    v "Shall I begin?"
    show bg ch7home54 with dissolve
    p "Mmm. You taught me to be patient. Always pays off."
    v "Mmmhmmm."
    show bg ch7homethroat2 movie with dissolve
    n "Slowly Victoria inhales your length into her mouth"
    n "As she pulls back, licking the bottom of your shaft, she gives you a wink of accomplishment"
    p "You naughty devil."
    if dep >= 2:
        menu:
            "Let her keep the lead":
                p "Oh wow, keep going."
                show bg ch7home52 with dissolve
                n "Victoria takes a breath, getting ready to challenge herself"
                show bg ch7home170 with dissolve
                n "In one motion, she takes you down all the way to the base"
                p "Holy shit. Tap me if you get uncomfortable."
                show bg ch7homethroat4 movie with dissolve
                n "You feel Victoria chuckle in response as she continues to take you deep into her throat"
                p "God, I don't know how much longer I can last."
                v "Mmm!"
                show bg ch7home55 with dissolve
                v "I hope that took your mind off things."
                p "It most certainly did."
                jump ch7vicsexmenu1
            "Force yourself in harder":

                $ persistent.ch7vicsex1 = True
                show bg ch7home51 with dissolve
                p "Let's see how much more you can take."
                show bg ch7homethroat1 movie with dissolve
                v "Mmph!"
                n "You force down into her mouth as her hand tries to pull away from the wall"
                show bg ch7home76 with dissolve
                v "Ah! Not that hard. I prefer to have a bit more control when we do that."
                p "Sorry... I-"
                $ v_lust -= 1
                v "You got a little carried away. Let's just move on."
                jump ch7vicsexmenu1
    else:
        p "Oh wow, keep going."
        show bg ch7home52 with dissolve
        n "Victoria takes a breath, getting ready to challenge herself"
        show bg ch7home170 with dissolve
        n "In one motion, she takes you down all the way to the base"
        p "Holy shit. Tap me if you get uncomfortable."
        show bg ch7homethroat4 movie with dissolve
        n "You feel Victoria chuckle in response as she continues to take you deep into her throat"
        p "God, I don't know how much longer I can last."
        v "Mmm!"
        show bg ch7home55 with dissolve
        v "I hope that took your mind off things."
        p "It most certainly did."
        jump ch7vicsexmenu1





label ch7homepussy:
    p "You know, sometimes you should be the one rewarded. Doesn't always have to be me."
    show bg ch7home77 with dissolve
    v "Heh, is that so?"
    show bg ch7home78 with dissolve
    p "Absolutely. You are named for a queen after all."
    v "Just don't bow to me, I don't know how I would react."
    show bg ch7home79 with dissolve
    n "Your hand moves down and teases her hard exposed nipple"
    p "Damn, you are perfect."
    v "Mmm, so what is my reward, [vicsexname]?"
    show bg ch7home80 with dissolve
    p "I think you have a pretty good idea."
    v "Mmmm. Keep going."
    show bg ch7home81 with dissolve
    n "As your finger traces down her belly, Victoria's grip gets tighter in anticipation"
    show bg ch7home82 with dissolve
    v "Oooh..."
    n "Your finger stimulates her clitoris as she grips even tighter"
    p "Feel good?"
    show bg ch7home83 with dissolve
    v "Ohh yes!"
    n "Her pussy drips as you continue to rub her"
    v "I want to taste it."
    show bg ch7home84 with dissolve
    v "Hmmm..."
    p "A little naughty."
    v "Well, the royalty were never saints, no matter what they wanted you to believe."
    if sexmenu2 == True and sexmenu1 == True:
        $ v_lust += 1

    p "I won't bow, but I will kneel."
    show bg ch7home86 with dissolve
    v "Ha! Oh god..."
    p "Was that a laugh I just heard?"
    show bg ch7homeeat movie with dissolve
    v "Ummm, no!"
    v "Mmm, okay, fine! Yes!"
    v "Wow, [vicsexname], that's amazing! Heh, oh my god!"
    show bg ch7home85 with dissolve
    v "Oh... My... God..."
    show bg ch7home86 with dissolve
    if sexmenu2 == True and sexmenu1 == True:
        v "You just earned some points with that, [vicsexname]."
        p "Did I now?"
    else:
        v "Mmm, that was great."
    $ sexmenu2 = False
    jump ch7vicsexmenu1

label ch7homecum1:
    p "I need to cum..."
    show bg ch7home56 with dissolve
    v "Already? But we've only just started."
    p "Heh, don't worry, this always happens. I've got plenty left in the tank."
    show bg ch7homecumshotmovie movie with dissolve
    v "Good, because I am not even close to done with you yet."
    p "You? Done with me?"
    v "Just cum alrea-"
    p "AHH!"
    v "Dy..."
    show bg ch7home57 with dissolve
    v "*Bursts into laughter* You sure you can keep going?!"
    p "More than ever."
    show bg ch7home58 with dissolve
    v "One sec."
    p "You okay?"
    v "Heh, yeah I'm fine. Help me with my bra?"
    show bg ch7home59 with dissolve
    p "You know, you have an amazing laugh."
    v "Yeah?"
    show bg ch7home60 with dissolve
    p "I'd love to hear it more often, that and see your beautiful smile."
    v "That's... just hold me like this for a minute."
    p "Is something wrong."
    v "No... Nothing at all. I'm not used to feeling..."
    show bg ch7home61 with dissolve
    p "Happy?"
    v "Is that what you humans call it?"
    p "..."
    v "I'm joking. But yes, with you I am."
    show bg ch7hometitplay movie with dissolve
    v "Heh, what are you doing?"
    p "My reward for suffering your horrible comedic timing."
    v "Well, [vicsexname], I can think of better things than that."
    show bg ch7home62 with dissolve
    if "ch2vic" in extraevents:
        v "Come on. We haven't used your couch yet."
    else:
        v "Come on."
    show bg ch7home63 with dissolve
    v "So, [vicsexname], what other things should we do?"
    $ resetsexmenu()
    jump ch7vicsexmenu2

label ch7vicsexmenu2:
    menu:
        "Pussy":
            jump ch7vicpussy
        "Pleasure her":
            jump ch7vicpleasure
        "Anal" if v_lust >= 2 or v_score >= 6:
            jump ch7vicanal


label ch7vicpussy:
    show bg ch7home100 with dissolve
    v "So, [vicsexname], did you want to fuck me?"
    p "Dunno... feeling pretty tired."
    show bg ch7home101 with dissolve
    v "Your comedic timing is worse than mine."
    p "Bullshit, my jokes are great!"
    show bg ch7home102 with dissolve
    v "But if you really don't want to."
    p "..."
    show bg ch7home104 with dissolve
    v "I guess I'll just handle myself, [vicsexname]."
    p "You talked me into it."
    show bg ch7home105 with dissolve
    v "I'd keep the teasing going, but the anticipation is..."
    v "Fuck me..."
    show bg ch7home106 with dissolve
    n "You push deep into Victoria's pussy as she lets out a soft moan"
    v "Yes, [vicsexname]. Like that."
    show bg ch7homefuck2 movie with dissolve
    v "Hah... hah..."
    p "Holy shit..."
    v "Mmm..."
    show bg ch7home107 with dissolve
    n "Victoria locks eyes with you, moaning wordlessly as you pound her"

    show bg ch7homefuck3 movie with dissolve
    v "Mmm... [vicsexname]."
    n "Victoria's pussy tighens around your cock as you continue to drive into her"
    v "Oh my god! Keep going!"
    v "OH FUCK YES!"
    v "*Panting heavily* Now let me get on top."
    show bg ch7home109 with dissolve
    v "I forgot to mention, I have a new mission for you."
    p "Yeah?"
    v "Make me cum. Again."
    p "I accept."
    show bg ch7home110 with dissolve
    v "You act as if refusal was an option."
    p "Heh, come here and sit that beautiful body on me."
    show bg ch7home111 with dissolve
    v "Mmm, suck on my nipples while I ride you."
    p "As you wish."
    show bg ch7home113 with dissolve
    v "Taste the sweat off my body."
    p "Mmm..."
    show bg ch7home112 with dissolve
    v "Oh that is perfect."
    p "Do you want to taste yourself."
    v "Mmm, yes..."
    show bg ch7home114 with dissolve
    n "Victoria takes your finger in her mouth and begins to suck her sweat off of it"
    show bg ch7home115 with dissolve
    v "I think the mission... is almost... complete."
    p "Cum for me."
    show bg ch7homefuck4 movie with dissolve
    v "Mmm..."
    n "As she glides up and down on you, you can feel her juices pouring from her"
    v "*Breathing heavily* Here we go... Hold onto me..."
    show bg ch7home117 with dissolve
    v "Oh my god, I'm going to explode!"
    show bg ch7home116 with dissolve
    n "With a swift convulsion and arch of her back, Victoria erupts in ecstasy"
    v "YES! OH GOD! YES!"
    show bg ch7home118 with dissolve
    v "Oh that was perfect! Are you going to cum?"
    menu:
        "Not yet":
            p "Oh, I'm not ready yet."
            v "Heh, good."
            jump ch7vicsexmenu2
        "Cum in her pussy":
            p "Keep fucking me I'm close."
            v "I can help with that."
            show bg ch7homefuck5 movie with dissolve
            p "Oh god, here it comes."
            v "Come for me, [vicsexname]!"
            p "AGGH! YES!"
            show bg ch7home119 with dissolve
            v "Inside me and all over me. I take it you enjoyed that as much as I did."
            show bg ch7home120 with dissolve
            v "So, are you glad I came by?"
            p "I am... Though you should try knocking next time. Or give me a call. I'll leave the door unlocked."
            v "Well, I guess there are some forms of etiquette I still need to adjust for."
            p "You're lucky I'm so forgiving."
            show bg ch7home121 with dissolve
            v "You truly are. I don't understand how you can forgive me for all of this."
            p "Nothing to forgive. If you hadn't hired me, we never would have met."
            v "That's not what I meant."
            p "Then, what?"
            v "Even after everything, I still hope you'll give up."
            p "You know I can't."
            v "..."

            show bg ch7home122 with dissolve
            v "If you knew what was coming, you'd..."
            p "Victoria. Just stop. I have to do this."
            v "I... I need to go."
            p "Already?"
            v "I'm sorry, [p]."
            show bg ch7home167 with dissolve
            p "Shit..."
            jump ch7vicend


label ch7vicpleasure:
    p "For a change, what would you like."
    show bg ch7home123 with dissolve
    v "Heh, let me think about that. Anything?"
    p "I hope I don't regret that, but sure."
    v "Then lay on the couch and let me sit on you."
    show bg ch7home124 with dissolve
    p "Ummph! Oh, I see how it is."
    v "Enjoy it, [vicsexname]."
    show bg ch7home125 with dissolve
    p "*Muffled Voice* I will!"
    show bg ch7homefacesit movie with dissolve
    v "Ohhh, that is delightful."
    n "Victoria bounces up and down on your face as her juices pour into your mouth"
    v "Heh, I should probably let you breathe."
    show bg ch7home126 with dissolve
    v "You okay down there?"
    p "I'm in heaven."
    show bg ch7home127 with dissolve
    v "Not yet you're not, but you will be soon."
    p "I like the sound of that."
    show bg ch7home128 with dissolve
    v "You play with me, it is only fair I play with you."
    show bg ch7home132 with dissolve
    n "Victoria's lips wrap around your tip. A small bit of saliva rolls down your shaft as she begins to take it in"
    show bg ch7homethroat3 movie with dissolve
    n "Then, without effort, she swallows you whole"
    n "The two of you continue to please each other, with only the sounds of moans filling the room"
    if v_lust >= 2:
        show bg ch7home129 with dissolve
        n "With Victoria's pussy pushed down on your face and her mouth filled with your manhood, you spread her ass cheeks"
        show bg ch7home130 with dissolve
        $ renpy.pause(1)
        show bg ch7home131 with dissolve
        n "As you push your finger into her asshole, her mouth tightens around your cock as she lets out a soft moan"
    show bg ch7home133 with dissolve
    n "Victoria pushes all the way down and holds it"
    p "Mmm..."
    n "Your cock pulses as she holds it, on the brink of exploding"
    show bg ch7home134 with dissolve
    n "Feeling this she pulls away"
    v "We're not quite done yet. Like me, I'm sure you want this to go on a little longer."
    p "What are you thinking?"
    jump ch7vicsexmenu2


label ch7vicanal:

    $ persistent.ch7vicsexanal = True
    $ persistent.ch7vicsex2 = True
    if "ch4vicanal" in extraevents:
        p "Well, we can try what we did last time."
    else:
        p "Well, I have something a bit more in mind."
    show bg ch7home64 with dissolve
    v "And what would that be?"
    p "I think you know."
    show bg ch7home65 with dissolve
    v "Maybe something like this?"
    p "Wow, holy shit. Okay."
    show bg ch7home66 with dissolve
    v "By your reaction, I'm guessing you approve."
    p "*Gulps* Yeah, one hundred percent."
    show bg ch7home67 with dissolve
    if "ch4vicanal" in extraevents:
        v "Remember, take it slow at first. I'll work my way into it in time."
    else:
        v "Start off slow, alright? I'll need time to adjust."
    show bg ch7home68 with dissolve
    p "Of course. Let me know if you're alright."
    n "Victoria's ass flexes as you slowly push into her tight hole"
    show bg ch7home69 with dissolve
    p "Ugh. Good?"
    show bg ch7home70 with dissolve
    v "Mmm. Yes, [vicsexname]. Go ahead."
    v "Oh, that feels good."
    show bg ch7homeanal1 movie with dissolve
    n "Carefully, you push in slowly, feeling every inch as you go deeper and deeper"
    v "Mmm. Yes, [vicsexname]!"
    p "Still fine?"
    show bg ch7home71 with dissolve
    v "Ugh, fuck yes. Keep going. After this, I'm going to show you something amazing."
    p "I can't wait."
    show bg ch7homeanal1 movie with dissolve
    v "Ugh. It's fun keeping you in suspense."
    p "You love to do that, don't you?"
    v "I-"
    show bg ch7home73 with dissolve
    n "Victoria goes silent as you push in even deeper, feeling the sweat of her ass bouncing against your waist"
    show bg ch7home72 with hpunch
    v "Ohhhhhh... Wow."
    v "My god, [vicsexname]..."
    show bg ch7home74 with dissolve
    v "Now it's my turn. Get on the floor."
    p "Right here?"
    show bg ch7home75 with dissolve
    v "Perfect. Stay right there."
    p "What are you going to do."
    show bg ch7home87 with dissolve
    n "Victoria eases her ass down onto your hard cock pushing all the way down"
    v "Ride you without relent."
    show bg ch7home88 with dissolve
    v "I hope you're ready."
    p "Not sure if-"
    show bg ch7homeanal2 movie with dissolve
    p "OH FUCK! I am..."
    v "Yes, [vicsexname], let me fuck you."
    v "Go deep inside. Fill every inch of me!"
    v "AH YES!"
    show bg ch7homeanal3 movie with dissolve
    n "Victoria drives her ass down on you relentlessly"
    p "God damn!"
    v "Feel that ass tighten around you as I fuck you, [vicsexname]!"
    v "Cum for me!"
    menu:
        "Not yet":
            p "Not yet."
            show bg ch7home90 with dissolve
            v "Mmm. More fun then?"
            p "What would you like to do?"
            show bg ch7home89 with dissolve
            v "With you? Anything."
            jump ch7vicsexmenu2
        "Cum in her ass":

            show bg ch7home90 with dissolve
            v "[vicsexname], cum in me."
            p "Damn, I'm close."
            show bg ch7homeanal3 movie with dissolve
            v "I'll help with that."
            p "Fuuuuck!!!"
            show bg ch7home91 with quickflash
            p "UUGH!! Fuck me. WOW!"
            show bg ch7home92 with dissolve
            v "Very good work. Now are you done?"
            p "Heh, yeah, you drained me."
            $ achievement.grant("DEARLORD")
            init:
                $ achievement.register("DEARLORD")
            $ achievement.Sync()

            scene black with Dissolve(1)
            show bg ch7home94 with dissolve
            v "So, are you glad I came by?"
            p "I am... Though you should try knocking next time. Or give me a call. I'll leave the door unlocked."
            show bg ch7home95 with dissolve
            v "Well, I guess there are some forms of etiquette I still need to adjust for."
            p "Well, you're lucky I'm so forgiving."

            show bg ch7home96 with dissolve
            v "You truly are. I don't understand how you can forgive me for all of this."
            p "Nothing to forgive. If you hadn't hired me we never would have met."
            v "That's not what I meant."
            p "Then, what?"
            show bg ch7home97 with dissolve
            v "Even after everything, I still hope you'll give up."
            show bg ch7home98 with dissolve
            p "You know I can't."
            v "..."
            v "If you knew what was coming you'd..."
            p "Victoria. Just stop. I have to do this."
            show bg ch7home99 with dissolve

            v "I... I need to go."
            p "Already?"
            v "I'm sorry, [p]."
            show bg ch7home167 with dissolve
            p "Shit..."
            jump ch7vicend

label ch7vicend:
    $ extraevents.append("ch7vicsex")
    $ renpy.end_replay()
    if not persistent.ch7vicsex:

        $ renpy.notify(['Scene Unlocked', 'unlock'])
        $ persistent.ch7vicsex = True

    s "Not to interrupt, Sir."
    p "You're not, Sam. What's up?"
    s "We should probably get back. Though that individual is still waiting outside."
    p "Seriously? Still?"
    menu:
        "We will lose her on the road":
            p "Rather not stir up more shit."
            jump ch7apartmentignore
        "Confront her":
            p "Let's see what she wants, shall we?"
            jump ch7apartmentrush
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
