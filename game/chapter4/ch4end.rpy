
image bg ch4end1 = "ch4end1"
image bg ch4end2 = "ch4end2"
image bg ch4end3 = "ch4end3"
image bg ch4end4 = "ch4end4"
image bg ch4end5 = "ch4end5"
image bg ch4end6 = "ch4end6"
image bg ch4end7 = "ch4end7"
image bg ch4end8 = "ch4end8"
image bg ch4end9 = "ch4end9"
image bg ch4end10 = "ch4end10"


image ch4planemovie = Movie(play='video/chapter-4-video/ch4plane.webm', loop=False)
image bg ch4plane movie:
    "ch4planemovie"
    pause 12.0

label ch4end:
    scene black with Dissolve(3)
    play music audio.jet fadein 2.0 fadeout 2.0
    show bg ch4plane movie with dissolve
    "Pilot" "Sorry about the turbulence, Mrs. White."
    m "It's fine, pilot. How much longer?"
    "Pilot" "We're heading over the coordinates now, preparing for landing."
    scene black with Dissolve(2)
    $ renpy.music.set_volume(1.0, 2.0, 'music')

    play music audio.creepy fadein 2.0 fadeout 2.0
    show bg ch4end2 with dissolve
    m "Remember. You never took me here. Do you understand?"
    "Pilot" "Yes, Ma'am. What you did for my brother's son and daughter ensures my lips are sealed."

    show bg ch4end1 with Dissolve(1)
    m "Good. You stay here, I need to go in alone. Keep the engines running."
    show bg ch4end3 with dissolve
    n "Walking through the cold air, Meredith approaches a cave with a soft glow emanating from within"
    m "Hello?"
    show bg ch4end4 with Dissolve(2)
    "Girl" "We were... umm... expecting."
    m "Ahh... of course. You got my message?"
    "Girl" "Follow."
    show bg ch4end5 with dissolve
    m "Do you get many visitors up here? It must get lonely."
    "Girl" "..."
    m "You know, I used to explore caves like this at your age."
    "Girl" "..."
    show bg ch4end6 with dissolve
    m "Food, your supplies? How do- *Gasps*"
    "Girl" "No questions... Enter."
    m "Ahh, thank you. What's your name?"
    show bg ch4end7 with dissolve
    "Unknown" "She won't give you her name."
    m "Oh... Umm... Why not..?"
    show bg ch4end8 with dissolve
    "Unknown" "Because she doesn't have one, none of them do. Your people took that from them."
    m "Tha.. that wasn't my fault."
    "Unknown" "Spare me your sophistry."
    show bg ch4end9 with dissolve
    "Unknown" "Speak as to what you came here for."
    m "I need your help... "
    "Unknown" "And why should I help you? You know your money is meaningless to me."
    show bg ch4end10 with dissolve
    m "An augment from the war..."
    "Unknown" "I'm listening."
    jump ch5start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
