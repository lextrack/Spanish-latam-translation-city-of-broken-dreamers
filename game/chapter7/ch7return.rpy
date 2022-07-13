
image bg ch7return1 = "ch7return1"
image bg ch7return2 = "ch7return2"
image bg ch7return3 = "ch7return3"
image bg ch7return4 = "ch7return4"
image bg ch7return5 = "ch7return5"
image bg ch7return6 = "ch7return6"
image bg ch7return7 = "ch7return7"
image bg ch7return8 = "ch7return8"
image bg ch7return9 = "ch7return9"
image bg ch7return10 = "ch7return10"
image bg ch7return11 = "ch7return11"
image bg ch7return12 = "ch7return12"


image bg ch7returnoutside1 = "ch7returnoutside1"
image bg ch7returnoutside2 = "ch7returnoutside2"
image bg ch7returnoutside3 = "ch7returnoutside3"
image bg ch7returnoutside4 = "ch7returnoutside4"
image bg ch7returnoutside5 = "ch7returnoutside5"
image bg ch7returnoutside6 = "ch7returnoutside6"
image bg ch7returnoutside7 = "ch7returnoutside7"
image bg ch7returnoutside8 = "ch7returnoutside8"
image bg ch7returnoutside9 = "ch7returnoutside9"
image bg ch7returnoutside10 = "ch7returnoutside10"
image bg ch7returnoutside11 = "ch7returnoutside11"
image bg ch7returnoutside12 = "ch7returnoutside12"

image bg ch7hospleave movie = Movie(play='video/chapter-7-video/ch7hospitaltransition.webm', loop=False)


label ch7return:
    scene black with dissolve
    show bg ch7hospital100 with dissolve
    e "Oh hell, am I glad to be out of there."
    p "My car is just up this way. Fuck, this will be a tight squeeze."
    show bg ch7hospital102 with dissolve
    sh "These ongoing riots prove Congress made the right decision when they passed the law. We cannot allow our country to fall into..."
    "Ellen and Katie" "God! I hate that bitch!"
    show bg ch7hospital101 with dissolve
    e "Heh, you may be pretty cool after all."
    k "You're not so bad yourself."
    p "Alright guys, back to Betty's."
    show bg ch7hospleave movie with Dissolve(1)
    $ renpy.pause(4)
    scene black with Dissolve(2)
    show bg ch7returnoutside1 with Dissolve(2)
    e "Umm... Henry where are we going?"
    h "I'll just let you see it for yourself."
    show bg ch7returnoutside2 with dissolve
    $ renpy.pause(2)
    show bg ch7returnoutside3 with dissolve
    n "The sound of the motorcycles comes to a halt"
    show bg ch7returnoutside4 with dissolve
    sa "Damn girl. They almost brought us back home."
    show bg ch7returnoutside5 with dissolve
    "Bolter" "Well, Sasha girl, we jump 'em?"
    show bg ch7returnoutside6 with dissolve
    sa "We can't rush this, understand? I mean it. Those dudes will fuck us up."
    "Bolter" "We call in the crew, then."
    sa "No. Crew can't take them. Not head-on."
    sa "We follow them till we see her. We move when the time is right."
    "Bolter" "Cake and pie. Sesh gonna flip."
    sa "Burn Sesh, that Cinder-head will fuck the plan. We do this smart, we don't need backup. Grab her, take her. Fifty fifty, baby."
    sa "You keep eyes on here, I'm gonna watch them ancient wheels."
    scene black with Dissolve(1)
    show bg ch7return1 with dissolve
    p "Betty, we're back! Got another one for you."
    e "What. The. Fuck."
    show bg ch7return3 with dissolve
    e "Why am I not surprised you have been hiding in a whorehouse?"
    p "I'll never hear the end of this, will I?"
    show bg ch7return2 with dissolve
    e "Oh, no, gonna tell this shit to your grandkids."
    e "\"Let old Auntie Ellen tell you the story of the time your grandad hid out in a sex dungeon for robots.\""

    show bg ch7return4 with dissolve
    k "Surprisingly it's not bad. Cleaner than I expected and the owner has been really welcoming."
    e "Good, need something normal and chill in my life."
    k "Well... Okay, never mind that, you need a place to recover."
    show bg ch7return5 with dissolve
    k "It's not the most comfortable option but I think the couch would be best, in her condition."
    p "Not a bed?"
    k "They're too... Umm... Bouncy? She needs something stiffer."
    e "*Lets out a quick laugh* That's what she said."
    e "Ow. Laughing hurts."
    b "You're back..."
    show bg ch7return6 with dissolve
    ve "Another sister!"
    b "Venus, relax girl... I take it you didn't find Gloria."
    p "No."
    b "We'll keep looking. I need you to find her because if we don't, I'll be out of rooms at this rate."
    p "You know I owe you, right, Betty?"
    show bg ch7return7 with dissolve
    b "Screw it. Put her wherever."
    show bg ch7return8 with dissolve
    b "*Sighs* I'm going back to Glenn. He's tracking down your friend, hopefully he found something. Venus, see that our new guest is taken care of."
    show bg ch7return9 with dissolve
    ve "I overheard a couch would be preferable. We can take her to the recreational room as before."
    p "Sounds good. Keep an eye on her."
    ve "Of course."
    show bg ch7return10 with dissolve
    p "Henry, I'm heading back to my place."
    h "Why?"
    p "Supplies... Betty has guns a-plenty here and ammo. But with the Red Moon out there, I need something with a bit more punch."
    h "Be quick. I'll help Betty."
    jump ch7apartment
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
