

image bg ch4leave1 = "ch4leave1"
image bg ch4leave2 = "ch4leave2"

label ch4leave:
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with Dissolve(2)
    show bg ch4leave1 with Dissolve(2)
    if "ch4vicsex" in extraevents:
        p "(How is it that I'm more confused than when I came in?)"
        s "Signal is clear, Sir."
        p "Signal?"
        s "The bug, Sir. I have been able to infiltrate her Hope AI unit."
        p "Right..."
        show bg ch4leave2 with dissolve
        s "You seem preoccupied, Sir. Everything okay?"
        p "Yeah, Sam. It's fine. Everything's fine."
        jump ch4end

    if "ch4vicdep" in extraevents:
        p "Give me the good news, Sam."
        s "Yes, Sir. The Hope AI unit is now compromised."
        p "Good."
        show bg ch4leave2 with dissolve
        s "Sir, I need not remind you that you have been acting recklessly as of late."
        p "Shut up, Sam. I know what I'm doing."
        jump ch4end
    if "ch4vicaccept" in extraevents:
        p "(Need to go get her...)"
        s "Signal is clear, Sir."
        p "The what..?"
        s "The bug, Sir. I have been able to infiltrate the Hope AI unit."
        p "Why do we need..?"
        show bg ch4leave2 with dissolve
        s "Are you feeling alright, Sir? This was the plan."
        p "Yes... Yes, it was..."
        jump ch4end


    if "ch4vicgoodbye" in extraevents:
        p "(That didn't go quite as planned.)"
        s "Did you learn anything, Sir?"
        p "Not enough... what about you?"
        s "Yes, Sir. The Hope AI unit is now compromised."
        p "Okay..."
        show bg ch4leave2 with dissolve
        s "You don't seem pleased, Sir? Is everything okay?"
        p "Yeah, Sam. It's fine. Everything's fine."
        jump ch4end


    p "Sam, did it work?"
    s "Yes, Sir, I have infiltrated Miss Shields Hope AI unit."
    show bg ch4leave2 with dissolve
    p "Okay, good. That should help -- time to turn the tables."
    p "Maybe now we can be one step ahead."
    jump ch4end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
