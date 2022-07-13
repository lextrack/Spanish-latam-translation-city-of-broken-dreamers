image bg ch7wakeup14 = "ch7wakeup14"
image bg ch7wakeup15 = "ch7wakeup15"
image bg ch7wakeup16 = "ch7wakeup16"
image bg ch7wakeup17 = "ch7wakeup17"
image bg ch7wakeup18 = "ch7wakeup18"
image bg ch7wakeup19 = "ch7wakeup19"
image bg ch7wakeup20 = "ch7wakeup20"
image bg ch7wakeup21 = "ch7wakeup21"
image bg ch7wakeup22 = "ch7wakeup22"
image bg ch7wakeup23 = "ch7wakeup23"
image bg ch7wakeup24 = "ch7wakeup24"
image bg ch7wakeup25 = "ch7wakeup25"
image bg ch7wakeup26 = "ch7wakeup26"
image bg ch7wakeup27 = "ch7wakeup27"
image bg ch7wakeup28 = "ch7wakeup28"
image bg ch7wakeup29 = "ch7wakeup29"
image bg ch7wakeup30 = "ch7wakeup30"
image bg ch7wakeup31 = "ch7wakeup31"
image bg ch7wakeup32 = "ch7wakeup32"
image bg ch7wakeup33 = "ch7wakeup33"
image bg ch7wakeup34 = "ch7wakeup34"

label ch7vicsplan:
    $ extraevents.append("ch7nabgloria")
    scene black with Dissolve(1)
    show bg ch7wakeup14 with dissolve
    s "Sir, what you are doing?"
    p "Shut it, Sam."
    show bg ch7wakeup15 with dissolve
    s "Before I do, let me restate that this is highly dangerous and unethical."
    p "Since when do you care about ethics?"
    s "One of us should, Sir."

    show bg ch7wakeup16 with dissolve
    n "A muffled conversation can be heard between Gloria and Venus"
    g "Please, Venus, just go."
    ve "As you wish."
    show bg ch7wakeup17 with dissolve
    ve "Hello, [p]. You are up late. Trouble sleeping? I can be of service if you like."
    p "Not right now."
    show bg ch7wakeup18 with dissolve
    ve "If you change your mind, I will be recharging."
    p "Leave. Now."
    ve "Of course."
    show bg ch7wakeup19 with dissolve
    g "That should work... God this place barely has-"
    show bg ch7wakeup20 with dissolve
    g "[p]? I knew this was coming, I just hoped I was wrong."
    p "..."
    show bg ch7wakeup21 with dissolve
    g "Nah, that's a lie. I guess I kinda hoped it would happen, just to end all of this."
    p "It's better for everyone this way."
    show bg ch7wakeup22 with dissolve
    $ renpy.pause(1)
    show bg ch7wakeup23 with dissolve
    g "Better for you. Better for Henry, better for Ellen. I get that, but I'm not going with you."
    p "I was promised you would be safe."
    show bg ch7wakeup24 with dissolve
    g "Do you actually believe them? Is that what you're telling yourself?"
    p "We have to end this."
    g "I agree. But not your way. Not like this."
    n "The smell of ozone fills the room"
    show bg ch7wakeup25 with dissolve
    p "Oh, fuck! No you don't!"
    show bg ch7wakeup26 with dissolve
    g "Back off!"
    play sound audio.emp
    show bg ch7wakeup27 with dissolve
    n "Gloria blasts a wave of energy in your direction, knocking you clear across the room in an instant"
    show bg ch7wakeup28 with dissolve
    g "Don't look for me. You won't find me."
    show bg ch7wakeup29 with dissolve
    g "I'm ending this, but I have things to do first."
    show bg ch7wakeup30 with dissolve
    $ achievement.grant("DIABOLICAL")
    init:
        $ achievement.register("DIABOLICAL")
    $ achievement.Sync()
    g "*Sniffs* I almost trusted you. After what I saw, I thought you understood. My mistake."
    $ g_score -= 3
    show bg ch7wakeup31 with dissolve
    n "As you gasp for breath, the room goes dark"
    scene black with Dissolve(2)
    n "..."
    n "..."
    ve "[p], are you alright?"
    show bg ch7wakeup32 with dissolve
    p "Ugh... What? Where am I?"
    show bg ch7wakeup33 with dissolve
    ve "The recreational room. On the floor. Are you alright?"
    p "Shit, where's Gloria?!"
    show bg ch7wakeup34 with dissolve
    ve "She left."
    p "Fuck, what about Henry?"
    show bg ch7wakeup33 with dissolve
    ve "I believe he is still asleep in his room."
    p "Good..."
    ve "Shall I retrieve him?"
    p "No!"
    ve "May I ask what happened?"
    p "Help me up first..."
    show bg ch7wakeup6 with dissolve
    ve "I've helped you. What happened?"
    p "Ugh... Gloria was trying to leave. When I tried to stop her, she blasted me across the room."
    p "Happy?"
    ve "Thank you."
    p "Now, did she tell you anything? Where she was going?"
    ve "Nothing, I am sorry."
    jump ch7stairwaymorningcont
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
