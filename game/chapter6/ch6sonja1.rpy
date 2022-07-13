



image bg ch6sonja1 = "ch6sonja1"
image bg ch6sonja2 = "ch6sonja2"
image bg ch6sonja3 = "ch6sonja3"
image bg ch6sonja4 = "ch6sonja4"
image bg ch6sonja5 = "ch6sonja5"
image bg ch6sonja6 = "ch6sonja6"
image bg ch6sonja7 = "ch6sonja7"
image bg ch6sonja8 = "ch6sonja8"
image bg ch6sonja9 = "ch6sonja9"
image bg ch6sonja10 = "ch6sonja10"
image bg ch6sonja11 = "ch6sonja11"
image bg ch6sonja12 = "ch6sonja12"
image bg ch6sonja13 = "ch6sonja13"
image bg ch6sonja14 = "ch6sonja14"
image bg ch6sonja15 = "ch6sonja15"
image bg ch6sonja16 = "ch6sonja16"
image bg ch6sonja17 = "ch6sonja17"


image ch6gunship = Movie(play='video/chapter-6-video/ch6gunship.webm', loop=False)
image bg ch6gunshipmovie movie:
    "ch6gunship"



label ch6sonja1:
    scene black with Dissolve(3)

    if "ch5sonjabed" in extraevents:
        show bg ch6sonja1 with Dissolve(1)
        $ renpy.pause(2)
        play sound audio.jet fadein 2.0 fadeout 6.0
        show bg ch6gunshipmovie movie with dissolve
        $ renpy.pause(7.5)
        show bg ch6sonja2 with Dissolve(2)
        stop sound fadeout 3.0
        j "The hell?"
        show bg ch6sonja3 with dissolve
        j "Well, I'm alive. And on a bed..."
        j "Christ, [p]. This doesn't make us even."
        $ j_score += 1
    else:


        show bg ch6sonja4 with Dissolve(1)
        $ renpy.pause(2)
        play sound audio.jet fadein 2.0 fadeout 6.0
        show bg ch6gunshipmovie movie with dissolve
        $ renpy.pause(7.5)

        show bg ch6sonja5 with dissolve
        stop sound fadeout 3.0

        j "The hell?"
        show bg ch6sonja6 with dissolve
        j "Well, I'm alive. That I didn't expect."




    n "Commotion can be heard from the hallway"
    show bg ch6sonja7 with dissolve
    j "Looks like he's alive too."
    show bg ch6sonja8 with dissolve
    j "Hey Tex. Get up!"
    "Tex" "Ugh..."
    show bg ch6sonja9 with dissolve
    j "Watch where you're going!"
    "Doctor" "We need to seal this area."
    show bg ch6sonja10 with dissolve
    "Doctor" "You two, get these men out of here."
    j "Hey, I am talking to you, asshole!"
    "Doctor" "Not now. Get your squad and report to quarantine."
    show bg ch6sonja11 with dissolve
    "Unknown Male" "Sir, there is evidence of a kinetic discharge in the tram tunnel."
    "Doctor" "Incredible! Take me there, immediately."
    show bg ch6sonja13 with dissolve
    "Tex" "Ugh..."
    j "'Bout time you woke up, Brokeback."
    show bg ch6sonja12 with dissolve
    "Tex" "Ughh... great. I'm Brokeback now."
    j "Get up. This whole situation smells like a Venezuelan whorehouse."
    show bg ch6sonja14 with dissolve
    "Tex" "I said give me a second, will you?"
    j "This ain't normal. The fuck are all these labcoats doing here?"
    "Tex" "How would I know? I'm fine, by the way. Thanks for asking."
    show bg ch6sonja15 with dissolve
    j "Cry me a river, Tex. I'm being fucking serious."
    "Tex" "You and I both know Vostok is a little... extreme."
    j "They've got a fucking gunship outside!"
    show bg ch6sonja12 with dissolve
    "Tex" "Like I said, extreme."
    j "This ain't a milk run, Tex. Those are police bots over there."
    "Tex" "Yeah, so? We know that V has that contract."
    show bg ch6sonja16 with dissolve
    j "Cops, Corp Security and us. I knew this was big, but not this big."
    "Tex" "Sonja, we aren't paid to ask questions. We're paid to get the job done."
    "Tex" "And you fucked that up."
    show bg ch6sonja15 with dissolve
    j "Say that again."
    "Tex" "I don't have to. You know it."
    j "Your ass was on the ground, just like mine."
    "Tex" "I didn't give up a perfect kill shot."
    j "Wasn't..."
    show bg ch6sonja17 with dissolve
    "Unknown Male" "Your entire team was told to report to quarantine."
    j "Metetelo por tu culo come mierda!"
    show bg ch6sonja12 with dissolve
    "Tex" "She means, of course. Right away."
    j "No I didn't, I said shove it up your-"
    "Tex" "Sonja! Shut your fucking mouth for once in your life. Let's get cleared and get the hell out of here."
    j "Christ, fine!"
    jump ch6start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
