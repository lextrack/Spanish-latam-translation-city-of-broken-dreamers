image bg ch7morning1 = "ch7morning1"
image bg ch7morning2 = "ch7morning2"
image bg ch7morning3 = "ch7morning3"
image bg ch7morning4 = "ch7morning4"
image bg ch7morning5 = "ch7morning5"
image bg ch7morning6 = "ch7morning6"
image bg ch7morning7 = "ch7morning7"
image bg ch7morning8 = "ch7morning8"
image bg ch7morning9 = "ch7morning9"
image bg ch7morning10 = "ch7morning10"
image bg ch7morning11 = "ch7morning11"
image bg ch7morning12 = "ch7morning12"
image bg ch7morning13 = "ch7morning13"
image bg ch7morning14 = "ch7morning14"
image bg ch7morning15 = "ch7morning15"
image bg ch7morning16 = "ch7morning16"
image bg ch7morning17 = "ch7morning17"
image bg ch7morning18 = "ch7morning18"
image bg ch7morning19 = "ch7morning19"
image bg ch7morning20 = "ch7morning20"
image bg ch7morning21 = "ch7morning21"
image bg ch7morning22 = "ch7morning22"
image bg ch7morning23 = "ch7morning23"
image bg ch7morning24 = "ch7morning24"
image bg ch7morning25 = "ch7morning25"
image bg ch7morning26 = "ch7morning26"
image bg ch7morning27 = "ch7morning27"
image bg ch7morning28 = "ch7morning28"
image bg ch7morning29 = "ch7morning29"
image bg ch7morning30 = "ch7morning30"
image bg ch7morning31 = "ch7morning31"
image bg ch7morning32 = "ch7morning32"
image bg ch7morning33 = "ch7morning33"
image bg ch7morning34 = "ch7morning34"
image bg ch7morning35 = "ch7morning35"
image bg ch7morning36 = "ch7morning36"
image bg ch7morning37 = "ch7morning37"



image bg chapter7 movie = Movie(play='video/intros/chapter7.webm')


label ch7wake:

    show bg chapter7 movie with dissolve
    $ renpy.pause(2.9)

    play music audio.space fadein 2.0
    if "ch6katiesex" in extraevents:

        show bg ch7morning6 with Dissolve(2)
        p "Ugh! Fuck... *Breathes in heavily*"
        show bg ch7morning3 with dissolve
        s "Another bad dream, Sir?"
        p "Yeah, Sam. The same one as always."
        s "Can I get you something to help you sleep?"
        show bg ch7morning1 with dissolve
        p "Ugh... Nah, that's okay. Hey, what time is it?"
        s "It is currently 2:45 in the morning. May I suggest a slight stroll to get your mind off things?"
        p "Good idea."
        jump ch7katie
    else:




        show bg ch7morning5 with Dissolve(2)
        p "Ugh! Fuck... *Breathes in heavily*"
        show bg ch7morning4 with dissolve
        s "Another bad dream, Sir?"
        p "Yeah, Sam. The same one as always."
        s "Can I get you something to help you sleep?"
        show bg ch7morning2 with dissolve
        p "Ugh... Nah, that's okay. Hey, what time is it?"
        s "It is currently 2:45 in the morning. May I suggest a slight stroll to get your mind off things?"

        if "ch4vicaccept" in extraevents:
            menu:
                "Enact Victoria's plan":
                    p "I have a better idea."
                    s "Sir?"
                    jump ch7vicsplan
                "Just take a small walk":
                    p "Good idea."
                    jump ch7stairwaynight

        p "Good idea."
        jump ch7stairwaynight
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
