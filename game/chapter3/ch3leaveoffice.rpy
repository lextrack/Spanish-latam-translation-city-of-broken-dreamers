

image bg ch3hallway1 = "ch3hallway1"
image bg ch3hallway2 = "ch3hallway2"
image bg ch3hallway3 = "ch3hallway3"
image bg ch3hallway4 = "ch3hallway4"
image bg ch3hallway5 = "ch3hallway5"
image bg ch3hallway6 = "ch3hallway6"
image bg ch3hallway7 = "ch3hallway7"
image bg ch3hallway8 = "ch3hallway8"
image bg ch3hallway9 = "ch3hallway9"
image bg ch3hallway10 = "ch3hallway10"
image bg ch3hallway11 = "ch3hallway11"
image bg ch3hallway12 = "ch3hallway12"
image bg ch3hallway13 = "ch3hallway13"
image bg ch3hallway14 = "ch3hallway14"
image bg ch3hallway15 = "ch3hallway15"
image bg ch3hallway16 = "ch3hallway16"
image bg ch3hallway17 = "ch3hallway17"
image bg ch3hallway18 = "ch3hallway18"
image bg ch3hallway19 = "ch3hallway19"
image bg ch3hallway20 = "ch3hallway20"
image bg ch3hallway21 = "ch3hallway21"




label ch3leaveoffice:
    play music audio.calm fadein 2.0 fadeout 2.0
    scene black with Dissolve(1)
    show bg ch3hallway1 with dissolve
    p "(Alright, time to get back home and check out these files on Gibson.)"
    show bg ch3hallway2 with dissolve
    if "ch1chandra" in extraevents:
        $ c_lust += 1
        c "Took you long enough. The fuck were you doing in there? Wait, did Mom hire you as a gigolo?"
        show bg ch3hallway3 with dissolve
        p "Not now Chandra."
        c "Man, you ditch me after our night of passion? You stole my innocence, you know."
        p "You were never innocent. What do you want?"
        show bg ch3hallway4 with dissolve
        c "What in the fuckballs do you think?"
        p "Even if these games of yours weren't annoying as fuck, which they are, I don't have time for this right now."
    else:
        c "So, did you throw her out the window?"
        show bg ch3hallway4 with dissolve
        p "Not now, Chandra."
        c "Not now? What about the club? You ditched me."
        p "I told you I was busy. Still am. Kind of how the real world works, kid."

    show bg ch3hallway5 with dissolve
    c "Oh, there he is again, Mr. \"I got shit to do!\""
    p "Yeah, I did then and do now."
    show bg ch3hallway6 with dissolve
    c "Fuckballs! That sounds boring as shit. Now, if you want to have some fun, why not come with me?"
    p "I can't, because of that whole \"Shit to do\" thing I just mentioned."
    c "Come on! It can wait."
    p "Chandra, why is it you always assume you're going to get what you want?"

    show bg ch3hallway7 with dissolve
    c "Because that's how it works. Trust me and you'll get something you want too."
    c "I know a place that is prime fucking badass."
    p "..."
    show bg ch3hallway8 with dissolve
    c "Well, you coming or what?"
    menu:
        "Enter the elevator":
            show bg ch3hallway10 with dissolve
            c "Tick-tock, [p]!"
            show bg ch3hallway11 with dissolve
            c "Ha! I fucking knew it!"
            p "You're terrible, you know that, right?"
            show bg ch3hallway13 with dissolve
            if "ch1vic" in extraevents or "ch2vicsex" in extraevents:
                c "And you love it. Not to mention you need a tight young thing to get your mind off of Tits McGee over there."
                p "I do, huh?"
                show bg ch3hallway14 with dissolve
                c "Hey, I understand!"
                c "But since massive tits aren't on the board for you right now, maybe you want something else?"
            else:
                c "Oh, you love it. And I'm way more fun than that corp-drone of Mom's."
                p "Wait, are you jealous?"
                show bg ch3hallway14 with dissolve
                c "Fuck that! But I do know what you want!"
                p "And what is that?"
                c "You tell me!"

            menu:
                "A lot of things":
                    show bg ch3hallway15 with dissolve
                    p "I can think of a lot of things."
                    c "Awesome! That sounds {i}much{/i} better than \"I don't have time, Chandra.\""
                    p "But we don't have time. Not here, anyway."
                    show bg ch3hallway17 with dissolve
                    c "Not even for this?"
                    c "You sure?"
                    show bg ch3hallway16 with dissolve
                    p "You're evil."
                    c "Says the man with his hand on the ass of a girl young enough to be his daughter."
                    p "Heh, point taken."
                    show bg ch3hallway21 with dissolve
                    n "The ding of the elevator goes off as it reaches the ground floor."
                    c "Alright, off to the subway!"
                    p "Where are we-"
                    c "Quit it! It'll be prime!"
                "Nothing we can do here":
                    $ c_lust += 1
                    p "Not here."
                    show bg ch3hallway19 with dissolve
                    c "Shitsticks."
                    p "Your fucking mother already hates me enough."
                    show bg ch3hallway20 with dissolve
                    c "Like you're scared of that bitch? Come on, wouldn't it be great if she caught us...?"
                    p "We're almost to the lobby anyway."
                    c "That's what emergency stop buttons are for."
                    p "..."
                    c "Fine..."
                    n "The ding of the elevator goes off as it reaches the ground floor."
            jump ch3subway
        "Ditch her":
            $ c_score -= 1
            $ c_lust += 2
            p "Bye bye!"
            show bg ch3hallway9 with dissolve
            c "Hey! You son of a..."
            show bg ch3hallway12 with dissolve
            p "*Sighs in relief* (That one has a screw loose.)"
            p "Sam, did you receive anything from Baynard?"
            s "Yes, Sir. A few documents have been uploaded. They can only be accessed from direct voice command."
            show bg ch3hallway18 with dissolve
            p "Understood, I'll be home soon."
            jump ch3subwayalone
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
