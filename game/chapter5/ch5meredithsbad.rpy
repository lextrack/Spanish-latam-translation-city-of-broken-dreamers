
image bg ch5chandrablink:
    "ch5chandra115"
    pause 1.0
    "ch5chandra115a"
    repeat


label ch5meredithsbad:
    p "(Great, the brat's home. Lovely.)"
    show bg ch5chandra72 with dissolve
    p "(Hope her Mom's not here too. That would make this one hell of a trip.)"
    show bg ch5chandra73 with dissolve
    "Chandra nervously begins fidgeting with her hand"
    c "Goddamn it. All my fault."
    p "(What do you have there?)"
    show bg ch5chandra74 with dissolve
    p "(Green Cinder... Fuck me. There's getting high and being a fucking idiot. Didn't expect her to be this dumb.)"
    menu:
        "Do nothing":
            $ extraevents.append("ch5chandradrug")
            p "(Her choice, her problem.)"
            p "(And if she's high off her ass, it should be easier to sneak around.)"
            show bg ch5chandra75 with dissolve
            c "*Gulps down the drug* Sorry... So sorry..."
            c "I get it, though, this feels nice..."
            show bg ch5chandra80 with dissolve
            p "You stupid kid..."
            "Chandra begins to move her hand between her legs"
            show bg ch5chandra81 with dissolve
            menu:
                "Watch":
                    $ extraevents.append("ch5chandrawatch")
                    jump ch5chandrabadmast
                "Back to the car":

                    p "(I've got a bad feeling about this. Fuck it. I'm out of here. )"
                    show bg ch5drive1 with dissolve
                    s "That was faster than expected, Sir. And as I haven't noticed any silent alarms..."
                    p "It was a bust, Sam."
                    p "Let's get out of here."
                    jump ch5locationmenu
        "Rap on the window":

            $ extraevents.append("ch5chandrastop")
            jump ch5chandrabadint

label ch5chandrabadmast:
    p "*Sighs* (Let's watch and see what she gets up to.)"
    show bg ch5chandra82 with dissolve
    c "I thought you were different. But you're just like her. Maybe worse... she at least pretends to care."
    show bg ch5chandra83 with dissolve
    c "Not like it matters anymore, you cumstain."
    c "You could have had this. You could be doing this... fucking me..."
    show bg ch5chandra84 with dissolve
    c "Like the dirty girl I am. Punish me. Deep. Hard."
    show bg ch5chandra85 with dissolve
    p "(Kid definitely has issues.)"
    c "Mmmm. Yes!"
    p "(What does it say about me that I'm here watching?)"
    show bg ch5chandra88 with dissolve
    c "Fuck, yes! That feels amazing!"
    show bg ch5chandra87 with dissolve
    c "Harder. Faster! Treat me like your bad little thing."
    c "You like this young pussy? Better than your old wrinkled oaks?"
    show bg ch5chandra86 with dissolve
    c "You're making me cum! I don't deserve it."
    c "*Chandra's breath shudders as her body tenses up* Ohhh..."
    show bg ch5chandra89 with dissolve
    p "(Fuck me... that's some self-loathing right there.)"
    c "*Begins to sway slightly* Ugh..."
    show bg ch5chandra90 with dissolve
    c "What... What the hell..."
    c "OH FUCK!"
    show bg ch5chandra91 with dissolve
    c "MMMMPH!"
    show bg ch5chandra92 with dissolve
    $ renpy.pause(1)
    show bg ch5chandra93 with dissolve
    $ renpy.pause(1)
    show bg ch5chandra94 with dissolve
    p "You have to be fucking kidding me. Chandra, you are a train wreck. Maybe I should have some more sympathy for Meredith..."
    if dep >= 2:
        p "Nah... Forget that."

    p "(Okay, fuck this, I should go.)"
    show bg ch5drive1 with dissolve
    s "That was faster than expected, Sir. I haven't noticed any silent alarms..."
    p "It was a bust, Sam."
    p "Let's get out of here."
    jump ch5locationmenu


label ch5chandrabadint:
    show bg ch5chandra76 with dissolve
    p "(She might be annoying as hell, but I can't let her do this.)"
    p "(This shit is serious.)"
    show bg ch5chandra77 with dissolve
    "You bang on the window, making sure you get her attention"
    show bg ch5chandra78 with dissolve
    c "What?"
    p "Boo!"
    show bg ch5chandra95 with dissolve
    c "AAAH! What the splack?"
    p "Just open up?"
    show bg ch5chandra96 with dissolve
    c "Oh, NOW you want to talk, you shithead. Fuck shit and die."
    p "Chandra. Open the fuck up."
    show bg ch5chandra97 with dissolve
    c "Fine, whatever."
    show bg ch5chandra99 with dissolve
    c "Now what in the prime f--"
    p "Are you a fucking idiot?"
    show bg ch5chandra98 with dissolve
    c "Fuck you!"
    show bg ch5chandra100 with hpunch
    p "Cinder? Chandra, do you know what that shit can do?"
    c "You're gonna lecture me, Daddy?"
    p "I should do a fuck load more than that. This isn't just some upper."
    c "You think I give a fuck?"
    c "You angry, Daddy? You gonna hit me?"
    show bg ch5chandra101 with dissolve
    c "Get rough, punish me?"
    p "What the fuck happened to you?"
    c "Never took you for a narc. Disappointing."
    show bg ch5chandra102 with dissolve
    p "Drop that fucking shit!"
    c "Gah, fuck!"
    show bg ch5chandra103 with dissolve
    c "The fuck? I need that!"
    p "You want them?"
    show bg ch5chandra104 with vpunch
    p "Go get them!"
    c "YOU SHIT DRIPPING GHOST, FUCK! I'LL KILL YOU!"
    show bg ch5chandra105 with dissolve
    p "You'll thank me for this someday."
    c "Fuck you! I can always get more. Not like I don't have the cred."
    show bg ch5chandra106 with dissolve
    p "What the hell do you need this shit for anyway?"
    c "So I can fuck old assholes like you without puking."
    p "*Sighs* Come on, sit up."
    show bg ch5chandra107 with dissolve
    c "So, now you are pretending to be nice? It's too late."
    p "Come on, once the need for a fix passes, you'll feel better."
    c "*Sniffles* I fucked everything up..."
    p "What do you mean?"
    show bg ch5chandra108 with dissolve
    c "My friends..."
    p "You have friends?"
    show bg ch5chandra110 with dissolve
    c "You know what. Fuck it. I'm done with your bullshit."
    p "Sorry, force of habit. What happened?"
    show bg ch5chandra109 with dissolve
    c "Some assholes. They hurt someone I care about..."
    c "She just wanted to have a fun night out, you know?"
    p "And?"
    c "The people I introduced her to... Fuck, I'm a stupid bitch."
    p "Let me guess. The same assholes you got the Green Cinder from?"
    show bg ch5chandra108 with dissolve
    c "Yeah..."
    p "How did you even get involved with guys like that?"
    c "I like to party and I only took gels once or twice before."
    c "They were fun and Abby needed a good night."
    p "Once you saw your friend on it..."
    c "It was scary."
    p "What happened?"
    show bg ch5chandra110 with dissolve
    c "Can we not? Look, you're here for a reason, so what is it? Mom's not home, obviously."
    p "She needed me to pick something up from her office."
    c "Bullshit, spook."
    c "No way she'd let you into her system up there, she won't even let ME on."
    p "It's complicated."
    show bg ch5chandra111 with dissolve
    c "Whatever, doesn't matter. You can't get in."
    c "But knock yourself out, I'm out of fucks to give."
    p "Be right back."
    show bg ch5chandra112 with dissolve
    p "Sam, we should set a bug here."
    s "Negative, Sir. This residence has countermeasures for that. I can't prevent it from being detected."
    p "Figures..."
    show bg ch5chandra113 with dissolve
    p "Well, let's see if we can get lucky here."
    show bg ch5chandra114 with dissolve
    $ renpy.pause(1)
    c "I wouldn't touch that. Any failed log on and it will back up the video feed and send it to her."
    show bg ch5chandrablink with dissolve
    p "Sam?"
    s "Unfortunately, Sir, I can't verify what Miss White is saying. But it is entirely plausible."
    p "Damn it."
    show bg ch5chandra117 with dissolve
    c "Mom's paranoid as fuckballs. You know this."
    p "Yeah, she is."
    c "But I think we can come to an arrangement here. You help me; I get you what you want."
    p "How?"
    c "Sometimes she doesn't log off when she's at home."
    p "And you'd be willing to do that for me?"
    c "Carpe pro squid, spooky."
    p "You mean, quid pro quo."
    show bg ch5chandra116 with dissolve
    c "Whatever, I take care of your problem and you take care of mine."
    p "Save your friend?"
    c "That would have been nice, but no. I want revenge."
    p "I'm not a murderer."
    c "So cripple the fuckers. But make it hurt."
    p "Do you know what you're asking?"
    c "Yes. Do we have a deal?"

label chandradealyesno:
    menu:
        "Yes":
            $ extraevents.append("ch7chandrahelpbad")
            show bg ch5chandra116 with dissolve
            p "Fine. Deal."
            c "And I want pictures. Video if you can. Abby can't get that night back. They won't either."
            p "Sure."
            c "Tonight."
            p "No."
            p "When you get me something worthwhile. I'll do what you want."
            show bg ch5chandra117 with dissolve
            c "But-"
            p "No \"buts,\" that is the deal. Take it or leave it."
            c "*Sighs* I'll get you whatever I can. Then you fuck them up, then we never fucking see each other again."
            p "Sounds good to me."
            c "Get the fuck out, then."
            p "Gladly."
            show bg ch5drive1 with dissolve
            p "That may prove useful."
            s "She may have the best-secured network on the market, but that does not prevent young Miss White from gaining access if unlocked."
            p "Hopefully, she can get something... For now, let's get out of here."
            jump ch5locationmenu



        "I said no" if "ch5chandradealno" in extraevents:
            $ extraevents.append("ch5chandrareallybad")
            p "Chandra, you fucked this up, you have to live with it."
            p "It's not my job to fix your fucked up life."
            show bg ch5chandra116 with dissolve
            c "I know I fucked up. But I need--"
            p "You {i}need{/i} to take responsibility for your own fuck ups. We're done."
            show bg ch5chandra117 with dissolve
            c "Just go..."
            show bg ch5drive1 with dissolve
            p "Fuck my life..."
            s "Everything alright, Sir?"
            p "No... Let's just get out of here."
            jump ch5locationmenu
        "No":

            $ extraevents.append("ch5chandradealno")
            p "No. Not a chance."
            c "I don't think you thought this through."
            p "I know you didn't. So no."
            c "You fucking do this or I rat you out, right the fuck now."
            c "This was your fault too."
            jump chandradealyesno
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
