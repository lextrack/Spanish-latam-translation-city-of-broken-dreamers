
image bg ch7japan1 = "ch7japan1"
image bg ch7japan2 = "ch7japan2"
image bg ch7japan3 = "ch7japan3"
image bg ch7japan4 = "ch7japan4"
image bg ch7japan5 = "ch7japan5"
image bg ch7japan6 = "ch7japan6"
image bg ch7japan7 = "ch7japan7"
image bg ch7japan8 = "ch7japan8"
image bg ch7japan9 = "ch7japan9"
image bg ch7japan10 = "ch7japan10"
image bg ch7japan11 = "ch7japan11"
image bg ch7japan12 = "ch7japan12"
image bg ch7japan12 = "ch7japan12"
image bg ch7japan12 = "ch7japan12"
image bg ch7japan13 = "ch7japan13"
image bg ch7japan14 = "ch7japan14"


image ch7henry = Movie(play='video/chapter-7-video/ch7henry.webm', loop=False)
image bg ch7henrymovie movie:
    "ch7henry"
    pause 10.0
    "ch7henry-end"

label ch7japan:
    show bg ch7henry34 with dissolve
    h "Were you part of the mainland invasion?"
    p "No. I've heard stories, though."
    play music audio.futurenoir fadein 2.0 fadeout 2.0
    show bg ch7japan1 with Dissolve(3)
    h "Whatever you heard, it was worse."
    h "Our unit was tasked with destroying the Red Moon production facilities, cut off the head of the snake."
    show bg ch7japan2 with dissolve
    h "Intel had us attack a suspected location in Neo Kobe."
    show bg ch7japan3 with dissolve
    $ renpy.pause(1)
    "Soldier" "CLEAR!!!"
    play sound explosioneffect
    show bg ch7japan4 with dissolve

    $ renpy.pause(1)
    show bg ch7japan5 with dissolve
    "Soldier" "Alright, Gibson, next building."
    h "There were so many of them..."
    p "Red Moon?"
    show bg ch7japan6 with dissolve
    h "Civilians. Akatsuki employees. It was a massacre."
    p "It was war, Henry. You know shit gets fucked up quick."
    h "More than you think. We learned something after all those people died."
    p "What's that?"
    show bg ch7japan7 with dissolve
    h "That the Red Moon did not take kindly when we hit civilian targets."
    show bg ch7japan8 with dissolve
    h "They countered that night. It was hard-fought, but we managed."
    show bg ch7japan9 with dissolve
    h "Half of us, that is."
    show bg ch7japan10 with dissolve
    h "And that was just the beginning."
    p "What do you mean?"
    show bg ch7japan11 with dissolve
    h "We no longer targeted the facilities."
    h "Allied intel couldn't find them. We couldn't cut them off at the source, but we could draw them out."
    show bg ch7japan13 with dissolve
    $ renpy.pause(1)
    play sound audio.guneffect
    show bg ch7japan14 with dissolve
    h "One or two at a time, all it took was a few dozen dead civilians."
    show bg ch7japan12 with dissolve
    p "Fuck me... How long did this go on?"
    h "A few times..."
    show bg ch7henrymovie movie

    if not persistent.glos_newyears:
        $ persistent.glos_newyears = True
        $ renpy.notify(['Glossary Updated', 'glossary'])
    h "It wasn't long before China launched the {color=#359eff}New Year's strikes{/color}."
    p "And the war was over."
    h "But not for us. This shit in my neck, it does a lot. But what they never told us was that it suppressed our conscience."
    h "We murdered civilians, pointlessly, and we didn't care."
    h "Until we did. Within a year our inhibitors started breaking down. And suddenly the realization of everything you have become hits you."
    $ achievement.grant("AFEWDOZEN")
    init:
        $ achievement.register("AFEWDOZEN")
    $ achievement.Sync()
    h "You're a soldier without an army, the war is over, but your guilt lasts forever."


    $ extraevents.append("ch7henrystory")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
