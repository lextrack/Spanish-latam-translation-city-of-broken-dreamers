
image ch7morningcum = Movie(play='video/chapter-7-video/ch7morningcum.webm', loop=False)
image bg ch7morningcummovie movie:
    "ch7morningcum"
    pause 10.0
    "ch7morningcumend"



image bg ch7morningnibble movie = Movie(play='video/chapter-7-video/ch7morningnibble.webm')
image bg ch7morningeat movie = Movie(play='video/chapter-7-video/ch7morningeat.webm')
image bg ch7morningboob movie = Movie(play='video/chapter-7-video/ch7morningboob.webm')
image bg ch7morningride1 movie = Movie(play='video/chapter-7-video/ch7morningride.webm')
image bg ch7morningride2 movie = Movie(play='video/chapter-7-video/ch7morningride2.webm')
image bg ch7morningcum movie = Movie(play='video/chapter-7-video/ch7morningcum.webm')
image bg ch7morningblow movie = Movie(play='video/chapter-7-video/ch7morningblow.webm')




label ch7katiestart:
    if _in_replay:
        $ setReplay()

    show bg ch7morning13 with dissolve
    k "Say, I have an idea to help you sleep."
    p "Oh?"

    play music audio.doves fadein 2.0 fadeout 2.0

    n "Katie moves down your body. Her warm breath dances over you."
    show bg ch7morning16 with dissolve
    p "I think I am going to like this idea."
    k "You better."
    show bg ch7morning15 with dissolve
    n "Katie's lips softly touch your base as her breasts rub against your stomach"
    show bg ch7morningnibble movie with dissolve
    p "Ahh... That feels good."
    k "Shush!"
    p "*Whispering* As ordered."
    show bg ch7morning14 with dissolve
    k "Now, the question is. Do I keep doing this, or something else?"
    $ resetsexmenu()
    jump ch7katiemenu

label ch7katiemenu:
    menu:
        "Eat her out":
            $ sexmenu1 = False
            jump ch7katie69
        "Her on top":
            $ sexmenu2 = False
            jump ch7katieride
        "Cum" if sexmenu1 == False or sexmenu2 == False:
            jump ch7katiecum


label ch7katie69:
    p "Why don't you get up here."
    show bg ch7morning18 with dissolve
    k "Heh, maybe this will keep your voice down."
    p "Mmmhmm."
    show bg ch7morning29 with dissolve
    k "OH!!!"
    p "And you're telling me to keep it down!"
    show bg ch7morningeat movie with dissolve
    k "Quiet you! Just keep doing... OH GOD!"
    n "You continue to taste Katie and she gets more and more wet"
    show bg ch7morning17 with dissolve
    k "Mmmmm... I'm going to need to return the favor."
    show bg ch7morning20 with dissolve
    p "Mmm... Take... Your time."
    k "If you say so, [katiesexname]."
    show bg ch7morning19 with dissolve
    n "Katie takes you in her mouth as her tongue swirls around the tip of your cock"

    show bg ch7morningblow movie with dissolve
    p "Ohh, Katie, that feels nice. Thank you."
    k "Mmmhmm..."
    p "Remind me to wake you more often. Always seems to turn out well."
    show bg ch7morning18 with dissolve
    k "Don't get used to it, mister."
    p "Hard not to."
    jump ch7katiemenu

label ch7katieride:
    p "Hey, get yourself up here."
    show bg ch7morning21 with dissolve
    p "Wow, look at you."
    k "What?"
    show bg ch7morning22 with dissolve
    p "Heh, you know exactly what."
    show bg ch7morning23 with dissolve
    k "Thanks, now, you just relax."
    p "That is hard for me to do looking at you like that."
    show bg ch7morning24 with dissolve
    k "Shhh..."
    p "Of course."
    show bg ch7morning25 with dissolve
    k "Just enjoy."
    show bg ch7morningride1 movie with dissolve
    n "Katie begins to slowly grind on top of you. She gets tighter after every passing moment"
    p "*Quietly speaking* Phew, keep going. Just like that."
    show bg ch7morning26 with dissolve
    k "Yes, [katiesexname]."
    show bg ch7morningride2 movie with dissolve
    k "I want you to come with me."
    p "I'd like that."
    show bg ch7morning28 with dissolve
    k "Are you ready?"
    jump ch7katiemenu



label ch7katiecum:
    show bg ch7morning27 with dissolve
    p "I'm so close. Just keep grinding slowly like that."
    show bg ch7morning30 with dissolve
    p "*Grunts* Gah, yes, here it comes."
    show bg ch7morning33 with dissolve
    k "Mmmph... Oh, [katiesexname], I'm cumming!"
    show bg ch7morning34 with dissolve
    k "*Takes in a deep breath* You have more?"
    p "Always. May need some motivation, though."
    show bg ch7morning31 with dissolve
    k "Is that so?"
    k "How about this?"
    show bg ch7morningboob movie with dissolve
    k "Is that motivating enough?"
    p "Yep!"
    p "Shit, here it comes."
    show bg ch7morningcummovie movie with dissolve
    k "Cum for me, [katiesexname]!"
    p "H-here we go!"
    p "ARRGH!"
    show bg ch7morning26 with dissolve


    k "Better?"
    p "Much, thank you."
    show bg ch7morning12 with dissolve
    play music audio.space fadein 2.0 fadeout 2.0
    k "Heh, good. Now, get to sleep, you."
    p "I'll try."
    show bg ch7morning11 with dissolve
    k "*Begins to snore lightly*"
    $ achievement.grant("TRUELOVE")
    init:
        $ achievement.register("TRUELOVE")
    $ achievement.Sync()

    p "Seriously, how does she do that?"
    $ extraevents.append("ch7katiesex")
    $ renpy.end_replay()
    if not persistent.ch7katiesex:

        $ renpy.notify(['Scene Unlocked', 'unlock'])
        $ persistent.ch7katiesex = True


    jump ch7stairwaynightbefore
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
