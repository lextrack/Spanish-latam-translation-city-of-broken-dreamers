image bg ch5dream1 = "ch5dream1"
image bg ch5dream2 = "ch5dream2"
image bg ch5dream3 = "ch5dream3"
image bg ch5dream4 = "ch5dream4"
image bg ch5dream5 = "ch5dream5"
image bg ch5dream6 = "ch5dream6"
image bg ch5dream7 = "ch5dream7"
image bg ch5dream8 = "ch5dream8"
image bg ch5dream9 = "ch5dream9"
image bg ch5dream10 = "ch5dream10"
image bg ch5dream11 = "ch5dream11"
image bg ch5dream12 = "ch5dream12"
image bg ch5dream13 = "ch5dream13"
image bg ch5dream14 = "ch5dream14"
image bg ch5dream15 = "ch5dream15"
image bg ch5dream16 = "ch5dream16"
image bg ch5dream17 = "ch5dream17"
image bg ch5dream18 = "ch5dream18"
image bg ch5dream19 = "ch5dream19"
image bg ch5dream20 = "ch5dream20"
image bg ch5dream21 = "ch5dream21"
image bg ch5dream22 = "ch5dream22"
image bg ch5dream23 = "ch5dream23"
image bg ch5dream24 = "ch5dream24"
image bg ch5dream25 = "ch5dream25"
image bg ch5dream26 = "ch5dream26"
image bg ch5dream27 = "ch5dream27"
image bg ch5dream28 = "ch5dream28"
image bg ch5dream29 = "ch5dream29"
image bg ch5dream30 = "ch5dream30"
image bg ch5dream31 = "ch5dream31"
image bg ch5dream32 = "ch5dream32"
image bg ch5dream33 = "ch5dream33"
image bg ch5dream34 = "ch5dream34"
image bg ch5dream35 = "ch5dream35"
image bg ch5dream36 = "ch5dream36"
image bg ch5dream37 = "ch5dream37"
image bg ch5dream38 = "ch5dream38"
image bg ch5dream39 = "ch5dream39"
image bg ch5dream40 = "ch5dream40"
image bg ch5dream41 = "ch5dream41"
image bg ch5dream42 = "ch5dream42"
image bg ch5dream43 = "ch5dream43"
image bg ch5dream44 = "ch5dream44"
image bg ch5dream45 = "ch5dream45"
image bg ch5dream46 = "ch5dream46"

image bg whitescreen = "white"

image ch5dreampan = Movie(play='video/chapter-5-video/ch5dreampan.webm', loop=False)
image bg ch5dreampanmovie movie:
    "ch5dreampan"
    pause 8.0
    "ch5dreampanend"

label ch5dream:
    play music audio.creepy fadein 2.0 fadeout 2.0
    scene black with Dissolve(2)
    n "During the night, the room fills with heat, waking you up"
    show bg ch5dream1
    p "Gah! What the fuck! Ellen!?"
    p "(What the hell is going on!?)"
    show bg ch5dream2 with dissolve
    p "(Have to get out of here!)"
    scene black with Dissolve(1)
    n "Your feet hit the cold cement"
    p "Ugh..."
    show bg ch5dream3 with Dissolve(2)
    p "(This isn't right... Where is everyone?)"
    g "Hey..."
    show bg ch5dream4 with dissolve

    p "Gloria?"
    g "..."
    show bg ch5dream5 with dissolve
    p "What are you doing out here?"
    n "Gloria looks towards you but says nothing"
    show bg ch5dream6 with dissolve
    g "I thought you weren't coming."
    g "Come on."

    menu:
        "I wouldn't miss this":
            $ ch5dream += 1
            p "You and me, alone for once? It took me a while, but I'm here."
            scene black with Dissolve(1)
            show bg ch5dream8 with dissolve
            $ renpy.pause(1)
            show bg ch5dream7 with dissolve
            g "Yeah, well, with your record, nothing's a given."
            p "You're not letting that go, ever, are you?"
            g "Nope."
        "What are you talking about?":


            p "I was just out with Ellen for a few; I wasn't going anywhere."
            scene black with Dissolve(1)
            show bg ch5dream8 with dissolve
            $ renpy.pause(1)
            show bg ch5dream7 with dissolve
            g "Hah, you always said you hated her. I knew you were a secret fan!"
            p "Uh... right..."
            p "Seriously, what's going on?"

    g "And don't worry about Bigs, he talks a big game, but I think he actually likes you."
    p "What do you mean, he's right over..."
    show bg ch5dream9 with dissolve
    g "Well, he doesn't hate you and that's almost as good."
    p "..."
    show bg ch5dream10 with dissolve
    g "Come on."

    if ch5dream > 0:
        p "Yeah, right. You never had to get \"the talk\" from him. I almost shit myself."
        g "I know, I saw."
        p "You were watching me."
        show bg ch5dream12 with dissolve
        g "How could I not? Your face was adorable."
        p "Do you like seeing me in pain?"
        g "Only a little bit."
    else:
        p "Where are we going? I still don't have an answer to that."
        show bg ch5dream11 with dissolve
        g "My room. Geez... make me just come out and say it."
        p "Your room? We're at Ellen's."
        g "I wish."

    show bg ch5dream13 with dissolve
    g "It's right up here."
    show bg ch5dreampanmovie movie with dissolve
    g "Okay, here we are."
    g "Do you want to come in?"

    menu:
        "Of course":
            $ ch5dream += 1
            p "Finally!"
            g "Class. Pure Class."
            p "Well, one, your Dad's not here."
            show bg ch5dream14 with dissolve
            g "Papa's never here. He's out with \"her.\""
            p "I'm sure they'll break up sooner or later."
            g "Can we not talk about them?"
        "How are we here?":
            p "This doesn't make any sense."
            show bg ch5dream15 with dissolve
            g "No, it doesn't. "
            p "I mean it. We aren't... here."
            g "Shush."

    show bg ch5dream16 with dissolve
    g "Now. I uh... have a surprise for you."
    g "Turn around."
    p "What?"
    show bg ch5dream17 with dissolve
    g "Just do it, doofus."
    show bg ch5dream18 with dissolve

    if not persistent.ch5card3:
        $ renpy.notify(['Possible clue', 'alert'])
        show screen hidden_item("ch5card3", "ch5card3", 1143, 478, 120, 120)
    p "Fine."
    n "You hear shuffling behind you"
    hide screen hidden_item

    menu:
        "Stare at the poster":
            $ g_score += 1
            show bg ch5dream19 with dissolve
            p "This was the tour that was canceled, right?"
            g "No way. I had front row seats. Papa got them for me."
            p "Oh. Right... I must have forgotten."
            g "You can turn around now. You were good."
        "Stare at Donut":
            $ extraevents.append("ch5donut")
            show bg ch5dream20 with dissolve
            p "Nice bear."
            "Donut" "What are you looking at?"
            p "Huh?"
            show bg ch5dream21 with dissolve
            "Donut" "I'm watching you, pal. The girl is under MY protection."
            p "Fuck me! Your bear talks?!"
            g "If you're gonna make fun of Donut again..."
            p "I wasn't, I swear!"
            "Donut" "Be good."
            show bg ch5dream22
            "Donut" "Or"
            show bg ch5dream23
            "Donut" "Else!"
            p "What in the...?!"
            show bg ch5dream20 with dissolve
            g "You can turn around now."
        "Turn around":
            $ g_lust += 1
            show bg ch5dream24 with dissolve
            g "Wha..."
            g "Hey! I said, wait!"
            p "Sorry, I thought you were done."
            g "Dumb boys. Fine... not like you weren't going to see."

    show bg ch5dream26 with dissolve
    g "I uh... dang it. I had this all worked out and sexy like. And now..."
    g "I mean... you've been patient with me. And I know that I'm not like Cindy. So..."
    p "(Cindy?)"
    show bg ch5dream25 with dissolve
    g "Can you say something? Or..."

    menu:
        "This isn't real" if ch5dream <= 2:
            p "Uh... Gloria, I think we're in another dream."
            show bg ch5dream27 with dissolve
            g "What do you mean, Tommy? This isn't funny."
            if p == "Tommy":
                p "I'm not your Tommy. I wasn't here."
            else:
                p "I'm not Tommy."
            show bg ch5dream28 with dissolve
            g "No... this is real. This happened. It was supposed to be perfect."
            $ g_score += 1

            if g_score >= 3:
                show bg ch5dream41 with dissolve
                g "It was supposed to be perfect. OK, really awkward. But it has to be, right?"
                g "I was ready for him to see everything, just not these..."
                show bg ch5dream43 with dissolve
                g "When he saw them..."
                p "Your ears?"
                show bg ch5dream45 with quickflash
                $ renpy.pause(1)
                show bg ch5dream42 with Dissolve(1)
                g "I just freaked out. I... didn't mean to."
                p "I get that."
                show bg ch5dream41 with dissolve
                g "I... need to be alone now."
                g "Goodbye."
                show bg whitescreen with Dissolve(2)
                jump ch5dreamgoodwake


            show bg ch5dream38 with quickflash
            $ renpy.pause(0.5)
            show bg ch5dream39 with quickflash
            $ renpy.pause(0.5)
            show bg ch5dream40 with quickflash
            $ renpy.pause(0.5)
            show bg ch5dream45 with dissolve
            g "No... this... not again."
            p "Gloria?"
            show bg ch5dream46 with dissolve
            g "Get out! Just GET OUT!"
            show bg whitescreen with Dissolve(2)
            jump ch5dreambadwake
        "Kiss her":
            $ g_lust += 1
            p "You're gorgeous."
            show bg ch5dream31 with dissolve
            g "Really?"
            p "More than really."
            g "Because I know Cindy's got way bigger... I just..."
            jump ch5dreamscene





label ch5dreamscene:
    show bg ch5dream32 with dissolve
    p "Shh... It's okay."
    show bg ch5dream33 with dissolve
    n "You kiss Gloria, and she tenses up when your lips meet hers."
    show bg ch5dream35 with dissolve
    g "I think I'm ready... you know, really ready."
    p "Just relax."
    show bg ch5dream36 with dissolve
    p "That okay?"
    g "Yeah..."
    menu:
        "Keep going.":
            $ g_score -= 1
            show bg ch5dream37 with dissolve
            g "Tommy... keep..."
            p "What in the? Your ears?!"
            show bg ch5dream38 with dissolve
            g "DON'T!"
            show bg ch5dream39 with dissolve
            g "Wait... you're not Tommy."
            if p == 'Tommy':
                g "Not that Tommy."
            p "No... I'm not."
            g "Then why are you here? This is private."
            p "I'm sorry, I have no idea."





            show bg ch5dream40 with dissolve
            g "GET OUT! GET OUT!!!!"
            show bg ch5dream45 with quickflash
            $ renpy.pause(1)
            show bg ch5dream46 with quickflash
            g "NOW!!!"
            show bg whitescreen with Dissolve(2)
            jump ch5dreambadwake
        "This isn't right":

            show bg ch5dream42 with dissolve
            p "Gloria, this isn't real."
            g "Sure it is. This is my first time, with... it was supposed to be perfect."
            p "I was never here."
            show bg ch5dream41 with dissolve
            g "I... know."
            g "You're not Tommy, are you?"
            if p == 'Tommy':
                g "Not that Tommy, anyway."
            p "No. I'm not. I'm sorry."
            if g_score >= 3:
                g "It was supposed to be perfect. OK, really awkward. But it has to be, right?"
                g "I was ready for him to see everything, just not these..."
                show bg ch5dream43 with dissolve
                g "When he saw them..."
                p "Your ears?"
                show bg ch5dream45 with quickflash
                $ renpy.pause(1)
                show bg ch5dream42 with Dissolve(1)
                g "I just freaked out. I... didn't mean to."
                p "I get that."
                show bg ch5dream41 with dissolve
                g "I... need to be alone now."
                g "Goodbye."
                show bg whitescreen with Dissolve(2)
                jump ch5dreamgoodwake
            else:
                g "This is PRIVATE! YOU DON'T BELONG HERE!"
                show bg ch5dream40 with dissolve
                g "GET OUT! GET OUT!!!!"
                show bg ch5dream46 with quickflash
                $ renpy.pause(0.5)
                show bg whitescreen with Dissolve(2)
                jump ch5dreambadwake

label ch5dreambadwake:
    stop music fadeout 2.0
    $ extraevents.append("ch5dreambadwake")
    if "ch5ellennotop" in extraevents:
        p "AAAAH!"
        show bg ch5ellen76 with dissolve
        e "The fuck was that?"
        p "Nothing, just a bad dream."
        e "Damn. I didn't know you had nightmares."
        p "Sometimes..."
        e "Just go back the fuck to sleep. It's still early."
    elif "ch5ellentop" in extraevents:
        p "AAAAH!"
        show bg ch5ellen77 with dissolve
        e "The fuck was that?"
        p "Nothing, just a bad dream."
        e "Damn. I didn't know you had nightmares."
        p "Sometimes..."
        e "Just go back the fuck to sleep. It's still early."
    else:

        p "AAAAH!"
        show bg ch5ellen75 with dissolve
        e "*From upfront* The fuck is wrong with you?"
        p "Sorry, bad dream."
        e "No fucking shit! Hard enough to sleep as is."
        p "Don't I know it. Sorry to wake you, Ellen."
        e "Just don't do it again."

    jump ch5morning


label ch5dreamgoodwake:
    stop music fadeout 2.0

    if "ch5ellennotop" in extraevents or "ch5ellentop" in extraevents:
        show bg ch5ellen83 with Dissolve(2)
    else:
        show bg ch5ellen75 with Dissolve(2)
    p "(Gloria, you poor girl...)"
    jump ch5morning
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
