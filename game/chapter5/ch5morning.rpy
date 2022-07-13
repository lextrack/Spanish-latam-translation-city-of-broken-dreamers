
image bg ch5morning1 = "ch5morning1"
image bg ch5morning2 = "ch5morning2"
image bg ch5morning3 = "ch5morning3"
image bg ch5morning4 = "ch5morning4"
image bg ch5morning5 = "ch5morning5"
image bg ch5morning6 = "ch5morning6"
image bg ch5morning7 = "ch5morning7"
image bg ch5morning8 = "ch5morning8"
image bg ch5morning9 = "ch5morning9"
image bg ch5morning10 = "ch5morning10"
image bg ch5morning11 = "ch5morning11"
image bg ch5morning12 = "ch5morning12"
image bg ch5morning13 = "ch5morning13"
image bg ch5morning14 = "ch5morning14"
image bg ch5morning15 = "ch5morning15"
image bg ch5morning16 = "ch5morning16"
image bg ch5morning17 = "ch5morning17"
image bg ch5morning18 = "ch5morning18"
image bg ch5morning19 = "ch5morning19"
image bg ch5morning20 = "ch5morning20"
image bg ch5morning21 = "ch5morning21"
image bg ch5morning22 = "ch5morning22"
image bg ch5morning23 = "ch5morning23"
image bg ch5morning24 = "ch5morning24"
image bg ch5morning25 = "ch5morning25"
image bg ch5morning26 = "ch5morning26"
image bg ch5morning27 = "ch5morning27"
image bg ch5morning28 = "ch5morning28"
image bg ch5morning29 = "ch5morning29"
image bg ch5morning30 = "ch5morning30redo"
image bg ch5morning31 = "ch5morning31redo"
image bg ch5morning32 = "ch5morning32redo"
image bg ch5morning33 = "ch5morning33redo"
image bg ch5morning34 = "ch5morning34redo"
image bg ch5morning35 = "ch5morning35redo"
image bg ch5morning36 = "ch5morning36redo"
image bg ch5morning37 = "ch5morning37redo"
image bg ch5morning38 = "ch5morning38redo"
image bg ch5morning39 = "ch5morning39redo"
image bg ch5morning40 = "ch5morning40redo"
image bg ch5morning40b = "ch5morning40b"

image bg ch5morning41 = "ch5morning41"
image bg ch5morning42 = "ch5morning42"
image bg ch5morning43 = "ch5morning43"
image bg ch5morning44 = "ch5morning44"
image bg ch5morning45 = "ch5morning45"
image bg ch5morning46 = "ch5morning46"
image bg ch5morning47 = "ch5morning47"
image bg ch5morning48 = "ch5morning48"
image bg ch5morning49 = "ch5morning49"
image bg ch5morning50 = "ch5morning50"
image bg ch5morning51 = "ch5morning51"
image bg ch5morning52 = "ch5morning52"
image bg ch5morning53 = "ch5morning53"
image bg ch5morning54 = "ch5morning54"
image bg ch5morning55 = "ch5morning55"

image ch5morningpan = Movie(play='video/chapter-5-video/ch5morningpan.webm', loop=False)
image bg ch5morningpanmovie movie:
    "ch5morningpan"
    pause 10.0
    "ch5morningpanend"

label ch5morning:
    scene black with Dissolve(2)
    p "Ugh..."
    p "(Shit, that was a rough night...)"
    e "Wakey wakey..."
    show bg ch5morning1 with dissolve
    p "Ellen?"
    play music audio.verycalm fadein 2.0 fadeout 2.0
    if e_score >= 3:
        show bg ch5morning2 with dissolve
        e "Since when do you sleep in? I've been up for ages."
        e "Are you okay?"
    else:
        show bg ch5morning3 with dissolve
        e "Yeah. Came back to check on you. You were pretty much knocked out."
        e "Are you okay?"

    p "I guess so..."
    show bg ch5morning4 with dissolve
    e "You'd better be. That girl is counting on you."
    p "Yeah, sorry. How's she doing??"
    show bg ch5morning5 with dissolve
    e "Gloria's putting on a strong face, but she's antsy. I can't blame her."
    p "And the big guy?"
    show bg ch5morning6 with dissolve
    e "Not sure, off doing what giants do."
    p "And that is?"
    e "Fuck if I know, [p]."
    p "He's probably setting up a perimeter. Keep your eyes open for tripwires and mines."
    e "Very funny. But just in case, you walk in front from now on."
    p "..."
    scene black with dissolve
    show bg ch5morning7 with dissolve
    e "You know they can't stay here forever. Any ideas for a more permanent spot to lay low?"
    p "Permanent? Not a chance, not yet. But I have a few ideas that could work for a while."
    p "I know some people. I'll talk it over with Henry and finalize the plan."
    if "ch4vicaccept" in extraevents:
        show bg ch5morning9 with dissolve
        e "Speaking of plans. You said you had a way to make this right. What did you mean?"
        p "I'll fill you in later. But, running around like we are is not doing any good."
    else:
        show bg ch5morning8 with dissolve
        if h_score >= 2:
            e "You two seem to get along. Seems odd."
            p "We have some common ground. It helps."
        else:
            e "From what I could see last night, I'm not sure I should leave you two alone with each other."
            if "ch4fightspare" in extraevents or "ch4fightskill" in extraevents:
                p "Well, I did try to kill him. That doesn't make a good first impression."
            else:
                p "Please don't. If it weren't for Gloria, I'd probably be dead."
    e "Well, anyway, let's head inside."
    scene black with Dissolve(1)
    show bg ch5morning10 with dissolve
    e "So that you know, she seemed a bit..."
    p "A bit what?"
    show bg ch5morning11 with dissolve
    e "I don't know, just, off this morning."
    p "Huh... well, she's got a lot on her mind."
    e "Just try not to treat her like a freak or special or whatever."
    p "But she is, special, I mean."
    e "Fuck off. You know what I'm saying, [p]."
    show bg ch5morning12 with dissolve
    e "Hey, babe, I'm back."
    g "Shh!"
    show bg ch5morning24 with dissolve
    $ renpy.pause(1)
    show bg ch5morning25 with dissolve
    g "Come on... move already."
    show bg ch5morning26 with dissolve
    p "You changed your hair again?"
    show bg ch5morning27 with dissolve
    n "As you speak, you break Gloria's concentration and the cue ball darts through the air."
    g "GAH!"
    show bg ch5morning28 with dissolve
    g "*Giggles* Woops! Sorry about that..."
    p "Ha, don't worry about it."
    show bg ch5morning29 with dissolve
    g "But, yeah. New clothes, thanks to Ellen, required new hair. I think they go together, right?"
    p "Hey, I like it."
    show bg ch5morning41 with dissolve
    e "Yeah, she tried green first, but I like her in red. Get a giant tattoo of a dragon across that cheek and that look will be prime as fuck."
    show bg ch5morning29 with dissolve
    g "Ummm...."
    p "Yeah, don't take advice from Ellen."
    g "Which cheek?"
    e "You got four, pick one."
    show bg ch5morning30 with dissolve
    g "Maybe later. Anyhow, Ellen, I was hoping I could have a word alone with, [p]."
    show bg ch5morning42 with dissolve
    e "Now, be careful with this one, not that he's not a lion in the sack, but I don't think you're ready yet."
    g "ELLEN!"
    p "The fuck?"
    e "Just fuckin around. I'll see what Henry's up to."
    g "He went underground. Seems there's a subway tunnel right beneath us."
    show bg ch5morning43 with dissolve
    e "Don't do anything I wouldn't do."
    show bg ch5morning31 with dissolve
    g "So...?"
    p "Yeah..."

    show bg ch5morning32 with dissolve
    g "That was... Awkward, still is a bit, you know."
    p "I'm sure. I'm sorry."
    show bg ch5morning33 with dissolve
    g "It's not your fault. It's crazy. It's been, what, two years now and it still sneaks up on me. That night, everything changed."
    g "Whenever I dream about it, I see myself as I am now. It's still me. I'm the one killing him."
    p "It wasn't your fault."
    g "Tell that to my subconscious."
    g "I'm just glad you didn't see the worst part of it -- the look on Papa's face when he realized what had happened."
    show bg ch5morning34 with dissolve
    p "You don't have to talk about it."
    g "Thanks, but it's somewhat late for that now."
    g "That's the thing, though. I didn't want to talk about it. Even Bigs only knows what happened second hand."
    p "But why me? You have powers... or gifts or whatever you want to call them. But me? Why are we linked?"
    g "I don't know."
    show bg ch5morningpanmovie movie with dissolve
    g "These tragic moments, we share them... "
    g "The road, that strange hallway, now this."
    menu:
        "No idea":
            $ g_score += 1
            p "Our."
            g "Trauma."
            show bg ch5morning35 with dissolve
            g "That hallway. What happened there?"
            p "A job down south that went south. Too many dead."
            g "The woman there, the one who cares about you. Sonja, right?"
            p "Yeah... We were married then. Well, technically, we still are, but life happens."
            g "She didn't come out of there the same person, did she?"
            p "She doesn't show it, but she didn't. I certainly didn't..."
            g "And you never forgave her for that."
            p "It's not what she did. It's what I didn't do."
            show bg ch5morning44 with dissolve
            g "Sorry, I shouldn't pry."
            p "Hey, it's fine. It's a bit too late to worry about invasions of privacy."
            g "I guess you're right."
            show bg ch5morning38 with dissolve
            g "On the bright side, any other trauma in my life is going to be pretty tame by comparison."
            p "I'll be looking forward to some time you didn't study for a history test or something."
            g "Mrs. Birdsong's world history was unicorns and happiness by comparison."
            p "Heh, I'll pass on the unicorns unless they have rainbows shooting out of their ass."
            g "Oh, Mom loved that game! She loved retro stuff. How did that song go?"
            p "Don't you dare!"
            g "Pa pa PAPA papa PA PA PAPAPA..."
            p "NEW TRAUMA!"
            g "Fine, no singing, how about we eat? Nothing around here but stale chips, and, well, that thing growing in the corner {i}might{/i} be edible."
            p "Are you always this hungry in the morning?"
            show bg ch5morning51 with dissolve
            g "Growing girl has to eat."
            jump ch5morningend
        "Comfort her":


            show bg ch5morning37 with dissolve
            p "So how about we make a promise?"
            g "A promise?"
            p "I'll make you one anyway. No matter what we saw or might see down the line, it stays between us."
            g "Do you swear?"
            p "I do."
            g "Then I do, too."
            if "ch5donut" in extraevents:
                $ g_score += 1
            if g_score >= 3 and "ch4vicaccept" not in extraevents:
                show bg ch5morning39 with dissolve
                p "No matter what happens, I will get you out of this. I swear to that, too."
                g "Well, I don't think I have any more boogeymen to dig out of my past."
                if "ch5donut" in extraevents:
                    p "Not even a psychotic talking bear?"
                    g "*Giggles* That was a first, he certainly doesn't talk."
                    p "Good, because that was nightmare fuel."

                menu:
                    "Grab her waist":
                        show bg ch5morning40 with dissolve
                        p "I can only promise you I'll do my best."
                        g "I know you will."
                        show bg ch5morning45 with dissolve
                        g "So, umm... I am a bit hungry."
                        p "Up for some breakfast?"
                        n "Gloria pushes away from you"
                        show bg ch5morning51 with dissolve
                        g "Actually..."
                        $ g_lust += 1
                        jump ch5morningend
                    "Explore a little":


                        show bg ch5morning40b with dissolve
                        p "I can only promise you I'll do my best."
                        show bg ch5morning46 with dissolve
                        g "Hey!!!"
                        show bg ch5morning47 with quickflash
                        g "BACK OFF!"
                        p "AHH!!"
                        n "You smash into the wall, Gloria standing above you."
                        show bg ch5morning48 with dissolve
                        g "God, I'm sorry."
                        p "I asked for that..."
                        show bg ch5morning49 with dissolve
                        g "No, I... Look, it's kind of a reaction. Usually I just smack the guy."
                        p "As I said, that was my fault -- no idea what came over me."
                        g "I kind of understand, probably some residual memories from last night."
                        p "It won't happen again."
                        show bg ch5morning50 with dissolve
                        g "Good... I'm not mad... I just need a minute."
                        p "I know, I'm sorry..."
                        $ extraevents.append("ch5glorialittlemad")
                        g "Now, I need some food to calm my nerves."
            else:

                show bg ch5morning45 with dissolve
                p "Everything will work out. I'll make sure of it."
                g "Will it, though?"
                menu:
                    "Grab her waist":
                        show bg ch5morning40 with dissolve
                        p "I can only promise you I'll do my best."
                        if "ch4vicaccept" in extraevents:
                            show bg ch5morning45 with dissolve
                            g "For who?"
                            p "What do you mean?"
                            g "Forget it. I just need some food."
                            jump ch5morningend
                        else:
                            g "Okay, this is slightly awkward..."
                            g "Especially after..."
                            jump ch5morningend
                    "Explore a little":
                        show bg ch5morning40b with dissolve
                        p "I can only promise you I'll do my best."
                        show bg ch5morning46 with dissolve
                        g "Hey, what are you doing!"
                        g "Get-"
                        show bg ch5morning47 with quickflash
                        g "OFF!"
                        p "AHH!!"
                        n "You smash into the wall, Gloria standing above you."
                        show bg ch5morning48 with dissolve
                        g "..."
                        p "I asked for that..."
                        show bg ch5morning50 with dissolve
                        $ extraevents.append("ch5gloriamad")
                        g "Now, I think you should leave me alone."

label ch5morningend:
    g "Hey Ellen!"
    show bg ch5morning53 with dissolve
    $ renpy.pause(1)
    show bg ch5morning52 with dissolve
    e "Hey?"
    if "ch5gloriamad" in extraevents:
        show bg ch5morning55 with dissolve
        e "[p], what the fuck happened?"
        p "Nothing..."
        e "Some nothing."
        g "He was an ass, is what."
        show bg ch5morning14 with dissolve
        g "*Tugging on her boot* Can you just leave?."
        p "I'll go find Henry..."
        show bg ch5morning13 with dissolve
        $ g_score -= 1
        $ g_lust -= 1
        g "Good!"
        jump ch5office
    else:

        g "You can stop listening now. I need to get out of here. I haven't seen the sun in days."
        show bg ch5morning54 with dissolve
        e "I wasn't... fuck, fine I was."
        show bg ch5morning55 with dissolve
        e "But go outside? [p], do you think that is a good idea?"
        if "ch5glorialittlemad" in extraevents:
            p "The girl can throw us across the room with her mind. I'm not arguing."
        else:
            p "Nope. But she is right, we need some food and the fresh air will do her good."
        show bg ch5morning15 with dissolve
        g "So, it's fine?"
        p "I guess. I won't stop you."
        show bg ch5morning16 with dissolve
        g "Cool! I hope this is okay? I won't draw too much attention and all that?"
        p "Don't get too excited."
        show bg ch5morning17 with dissolve
        g "Why not? I get to go out in the sun for the first time in what feels like forever."
        p "We did go out yesterday."
        g "That SO doesn't count."
        p "Ok, if we go out, I have ground rules."
        g "That's fine! Just need some fresh air. Bigs is great and all, but wow, he needs a shower!"
        e "Needs to get laid is what."
        g "Oh gross! Mental image I DID NOT NEED!"
        p "Ha! Come on, let's go."
        jump ch5office
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
