

image bg ch3subway1 = "ch3subway1"
image bg ch3subway2 = "ch3subway2"
image bg ch3subway3 = "ch3subway3"
image bg ch3subway4 = "ch3subway4"
image bg ch3subway5 = "ch3subway5"
image bg ch3subway6 = "ch3subway6"
image bg ch3subway7 = "ch3subway7"
image bg ch3subway8 = "ch3subway8"
image bg ch3subway9 = "ch3subway9"
image bg ch3subway10 = "ch3subway10"
image bg ch3subway10a = "ch3subway10a"

image bg ch3subway11 = "ch3subway11"
image bg ch3subway12 = "ch3subway12"
image bg ch3subway13 = "ch3subway13"
image bg ch3subway14 = "ch3subway14"
image bg ch3subway15 = "ch3subway15"
image bg ch3subway16 = "ch3subway16"
image bg ch3subway17 = "ch3subway17"
image bg ch3subway18 = "ch3subway18"
image bg ch3subway19 = "ch3subway19"
image bg ch3subway20 = "ch3subway20"
image bg ch3subway21 = "ch3subway21"
image bg ch3subway22 = "ch3subway22"
image bg ch3subway23 = "ch3subway23"
image bg ch3subway24 = "ch3subway24"
image bg ch3subway25 = "ch3subway25"
image bg ch3subway26 = "ch3subway26"
image bg ch3subway27 = "ch3subway27"
image bg ch3subway28 = "ch3subway28"
image bg ch3subway29 = "ch3subway29"
image bg ch3subway30 = "ch3subway30"
image bg ch3subway31 = "ch3subway31"
image bg ch3subway32 = "ch3subway32"
image bg ch3subway33 = "ch3subway33"
image bg ch3subway34 = "ch3subway34"
image bg ch3subway35 = "ch3subway35"
image bg ch3subway36 = "ch3subway36"
image bg ch3subway37 = "ch3subway37"



image ch3subwayanimmovie = Movie(play='video/chapter-3-video/ch3subwayanim.webm', loop=False)
image bg ch3subwayanimmov movie:
    "ch3subwayanimmovie"
    pause 7.9
    "ch3subwayanim"


label ch3subwayalone:
    scene black with Dissolve(1)
    show bg ch3subway1 with dissolve
    p "(Let's get home and check out these reports.)"
    show bg ch3subway4 with dissolve
    p "(See if Victoria is as good at this as she thinks she is.)"
    scene black with Dissolve(1)
    show bg ch3subway5 with dissolve
    play sound audio.subway loop fadein 2.0
    p "(Everyone's just getting out of work. Which means they're too tired to bother me. Thankfully.)"
    c "You ditched me again! The fuck is wrong with you?"
    p "..."
    show bg ch3subway8 with dissolve
    c "You don't get off that easy, Spook."
    p "You can't take a hint, can you?"
    show bg ch3subway7 with dissolve
    c "When have I ever?"
    jump ch3subwayquestion


label ch3subway:
    scene black with Dissolve(1)
    show bg ch3subway2 with dissolve
    p "Alright, Chandra, where to?"
    c "It's a surprise."
    p "..."
    c "Don't you trust me?"
    p "You don't want me to answer that."
    show bg ch3subway3 with dissolve
    c "Quit being such a tight ass."
    p "What's your game?"
    c "Can't a girl just have some fun?"
    p "That's not the part that worries me."
    show bg ch3subway8 with dissolve
    play sound audio.subway loop fadein 2.0
    c "You always this paranoid? Just relax."
    jump ch3subwayquestion



label ch3subwayquestion:
    menu:
        "Fine!":
            $ extraevents.append("ch3chandrago")
            p "Fuck it, might as well see where this goes."
            show bg ch3subway6 with dissolve
            c "There we go! Just relax and have fun."
            p "Can I get a general location at least?"
            show bg ch3subway9 with dissolve
            c "Downtown. So it's not far from your place."
            p "Since when do you know where I live."
            show bg ch3subway10 with dissolve
            c "My Mom is Meredith White, how'd you think?"
            p "She knows you have access to her files?"
            c "I'm still alive, so I think you know the answer to that."
            p "I should tell her. She'd be so pissed at you, she might forget about me."
            show bg ch3subway11 with dissolve
            c "Not likely. It's been a year, and you're still the topic that gets her to drop that ice queen persona."
            c "It doesn't help that I may have hinted that you popped my cherry at the homecoming afterparty."
            p "She didn't buy that."
            c "Nope. But she can never be sure..."
            show bg ch3subway14 with dissolve
            p "Good. Let her sweat."
            c "See? You get me."
            show bg ch3subway10a with dissolve
            c "By the way, you gonna do more than grab my knee? You go gay since I last saw you?"
            p "There are people around."
            show bg ch3subway15 with dissolve
            c "You don't look like the kind of guy who gives a fuck. I certainly don't."
            p "All right then."
            show bg ch3subway16 with dissolve
            n "Her legs widen as your hand firmly grabs her down below."
            c "Ohhh... there you..."
            show bg ch3subway17 with dissolve
            c "Ooooh... god... Keep doing that."
            p "If only your mother could see us now."
            show bg ch3subway19 with dissolve
            p "And what are you hiding under here?"
            c "Take a look and find out."
            show bg ch3subway18 with dissolve
            p "Not bad."
            c "Not bad! Okay, compared to that corp barbie doll perhaps."
            jump ch3endofride
        "What do you want?":
            p "What is it you want, Chandra?"
            c "Good times, strong drugs and a deep dicking. What else?"
            p "Uh-huh."
            show bg ch3subway6 with dissolve
            c "*Voice cracks* Alright, you got me [p]. I also want to... stick it to Mom. You know?"
            p "You're not fooling anyone, Chandra. Least of all me. You only act this way when you're drunk or high."
            show bg ch3subway15 with dissolve
            c "Who says I'm not?"
            p "I say. Don't bullshit a bullshitter. You might be good at playing kids your age, Chandra, try it on them. Or just go home."
            show bg ch3subway21 with dissolve
            c "But!"
            p "No buts. I'm not in the mood for whatever game you're playing."
            show bg ch3subway30 with dissolve
            play music audio.sol fadein 10.0 fadeout 4.0
            c "I hear my Mom in that voice..."
            p "The answer is no. I don't have the time nor the desire to deal with this."
            show bg ch3subway36 with dissolve
            c "*Under her breath* Mom won't help... You won't help..."
            p "Wait. Help with what?"
            c "Fuck off! You're right, I'm just playing."
            menu:
                "Tell me":
                    p "Chandra. Tell me what's going on. What's really going on."
                    show bg ch3subway31 with dissolve
                    c "Why should I? Like you would care. I'm just some spoiled brat, right?"
                    p "Yep, a loudmouthed, annoying spoiled brat. And it sounds like this loudmouth's worried about something. So, out with it."
                    show bg ch3subway32 with dissolve
                    c "Heh, you're such a dick... An honest dick, but a dick."
                    p "What did you get yourself into?"
                    show bg ch3subway33 with dissolve
                    c "It's not me. It's my friend."
                    p "And she's..."
                    c "*Voice cracks* In trouble, the bad kind..."
                    p "And she's in this mysterious place you're taking me to."
                    c "*Nods* I just need you to be there. You... you probably won't need to even do anything."
                    menu:
                        "Help her":
                            $ extraevents.append("ch3chandrahelp")
                            $ c_score += 2
                            p "This is a bad idea."
                            c "I know... I'm sorry..."
                            p "Goddamnit. I don't have time for this, but fine."
                            show bg ch3subway34 with dissolve
                            c "Really?"
                            p "I said fine."
                            c "Fucking aces!"
                            show bg ch3subway37 with dissolve
                            c "Hey everyone! I got a mother fucking Ghost to help me!"
                            p "..."
                            jump ch3endofride
                        "Refuse":

                            show bg ch3subway35 with dissolve
                            p "I'm sorry about your friend, and I'd like to help but... I have to get ready for tonight."
                            c "Wow, you really are a piece of shit. I shouldn't have expected any different."
                            p "Chandra, I'm sorry, but I can't."
                            c "What the fuck ever."
                            jump ch3endofridepissed
                "Ok, then, bye.":

                    $ dep += 1
                    p "Get going then. And next time, don't try this juvenile bullshit with me."
                    show bg ch3subway35 with dissolve
                    c "You're a total piece of shit. Maybe Mom was finally right about something."
                    p "Tell me something I don't already know."
                    c "What the fuck ever."
                    jump ch3endofridepissed




label ch3endofridepissed:
    $ extraevents.append("ch3chandrapissed")
    scene black with Dissolve(2)
    p "(Now I can try and enjoy the rest of the ride)"
    n "The tram begins its deceleration as it approaches the downtown stop"
    show bg ch3subway25 with dissolve
    stop sound fadeout 4.0
    c "I hope you choke on a horse cock!"
    p "Just drop it, Chandra, wow."
    show bg ch3subway26 with dissolve
    c "And I hope you get fucking shot!"
    show bg ch3subway29 with dissolve
    c "Go fuck yourself, [p]!"
    jump ch3reportalone


label ch3endofride:
    c "Oh shit. Next stop."
    show bg ch3subway22 with dissolve
    c "I fucking love this part when we get in the tunnel! It's like I'm in some old sci-fi vid!"
    scene black with Dissolve(1)
    window hide
    show bg ch3subwayanimmov movie with Dissolve(1)
    $ renpy.pause()
    window show
    c "Man, if I were wearing my club outfit from the other night, that would be freaky."
    p "I'm not one for fashion, but I agree."
    show bg ch3subway24 with dissolve
    stop sound fadeout 4.0
    n "The tram begins its deceleration as it approaches the downtown stop"
    if "ch3chandrahelp" in extraevents:
        p "So where is your friend?"
        c "With her cinder dealer."
        p "Fucking perfect."
    else:
        p "You going to tell me where we're going yet?."
        c "Relax, old man. You'll see soon enough."
    show bg ch3subway27 with dissolve
    c "Come on, Ghost. I thought you were supposed to be fast."
    p "Yeah, yeah, I'm coming."
    show bg ch3subway28 with dissolve
    if "ch3chandrahelp" in extraevents:
        c "This is gonna be tight!"
        p "Don't think this is a regular thing. You get one. That's it."
    else:
        c "You should be excited! Let's go!"

    jump ch3chandraapart
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
