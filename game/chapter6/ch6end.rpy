image bg ch6end1 = "ch6end1"
image bg ch6end2 = "ch6end2"
image bg ch6end3 = "ch6end3"
image bg ch6end4 = "ch6end4"
image bg ch6end5 = "ch6end5"
image bg ch6end6 = "ch6end6"
image bg ch6end7 = "ch6end7"
image bg ch6end8 = "ch6end8"


label ch6end:
    scene black with Dissolve(2)
    play music audio.darkcalm fadein 5.0 fadeout 5.0
    show bg ch6end1 with Dissolve(2)
    g "..."
    show bg ch6end5 with dissolve
    ve "Would you like to play a game? How about a nice game of chess?"
    show bg ch6end2 with dissolve
    g "No thanks..."
    ve "Oh..."
    ve "According to my database, the correct music can help a customer with their moods."
    ve "I'll find you something music related."
    show bg ch6end6 with dissolve
    n "The tv turns on and begins to cycle through channels"
    show bg ch6end7 with dissolve
    g "I'm not in the mood-"
    show bg ch6end8 with dissolve
    $ renpy.pause(1)
    show bg ch6end3
    g "Wait, stop!"
    show bg ch6end8 with dissolve
    sh "Real or cheap publicity stunt, we don't know."
    sh "But it has been confirmed that former star Ellen Lane has been hospitalized at Baynard General."
    sh "An unnamed source has told me that the self-proclaimed \"Milcher Rights\" activist is still in critical condition after a drug induced accident."
    show bg ch6end4 with Dissolve(1)
    g "Ellen!"
    jump ch7start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
