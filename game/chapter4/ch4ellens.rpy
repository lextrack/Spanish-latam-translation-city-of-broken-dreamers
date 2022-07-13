image bg ch4ellens1 = "ch4ellens1"
image bg ch4ellens2 = "ch4ellens2"
image bg ch4ellens3 = "ch4ellens3"
image bg ch4ellens4 = "ch4ellens4"
image bg ch4ellens5 = "ch4ellens5"
image bg ch4ellens6 = "ch4ellens6"
image bg ch4ellens7 = "ch4ellens7"
image bg ch4ellens8 = "ch4ellens8"
image bg ch4ellens9 = "ch4ellens9"
image bg ch4ellens10 = "ch4ellens10"
image bg ch4ellens11 = "ch4ellens11"
image bg ch4ellens12 = "ch4ellens12"
image bg ch4ellens13 = "ch4ellens13"
image bg ch4ellens14 = "ch4ellens14"
image bg ch4ellens15 = "ch4ellens15"
image bg ch4ellens16 = "ch4ellens16"
image bg ch4ellens17 = "ch4ellens17"
image bg ch4ellens18 = "ch4ellens18"
image bg ch4ellens19 = "ch4ellens19"
image bg ch4ellens20 = "ch4ellens20"
image bg ch4ellens21 = "ch4ellens21"
image bg ch4ellens22 = "ch4ellens22"
image bg ch4ellens23 = "ch4ellens23"
image bg ch4ellens24 = "ch4ellens24"
image bg ch4ellens25 = "ch4ellens25"
image bg ch4ellens26 = "ch4ellens26"
image bg ch4ellens27 = "ch4ellens27"
image bg ch4ellens28 = "ch4ellens28"
image bg ch4ellens29 = "ch4ellens29"
image bg ch4ellens30 = "ch4ellens30"
image bg ch4ellens31 = "ch4ellens31"
image bg ch4ellens32 = "ch4ellens32"
image bg ch4ellens33 = "ch4ellens33"
image bg ch4ellens34 = "ch4ellens34"
image bg ch4ellens35 = "ch4ellens35"
image bg ch4ellens36 = "ch4ellens36"
image bg ch4ellens37 = "ch4ellens37"
image bg ch4ellens38 = "ch4ellens38"
image bg ch4ellens39 = "ch4ellens39"


label ch4ellens:
    play music audio.calm fadein 2.0 fadeout 2.0
    scene black with Dissolve(1)
    show text "{=trans}AN HOUR LATER, AT ELLEN'S OLD STUDIO{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    p "Okay, here we are..."
    show bg ch4ellens1 with dissolve
    if not persistent.ch4card1:
        $ renpy.notify(['Possible clue', 'alert'])
        show screen hidden_item("ch4card1", "ch4card1", 1211, 501, 99, 42)
    g "What is that smell?"
    p "Eh, stale beer, broken dreams... maybe an orgy or... yeah."
    h "A little too much intel there, Ghost."
    h "Your friend didn't seem too pleased..."
    p "I just hope she forgives me."
    hide screen hidden_item
    show bg ch4ellens2 with dissolve
    g "Check this out! Ellen's mic!"
    g "This. Is. So. Cool!"
    h "Gloria, that's not yours... maybe you shouldn't touch it."
    menu:
        "Go ahead":
            p "Don't listen to him, go for it."
            show bg ch4ellens4 with dissolve
            g "Heh, really? WOO!"
            g "Can I sing? Singing on Ellen's mic! Prime!"
            p "Yeah, sure. Just not too loud."
            show bg ch4ellens9 with dissolve
            h "Wait! Wait! Gloria, playing around is one thing, but..."
            p "Is there something I should know?"
            show bg ch4ellens2 with dissolve
            g "Don't listen to him! He's just a big baby!"
            show bg ch4ellens8 with dissolve
            h "Gloria, I am not a begging man, but please..."
            p "I'm going to enjoy this!"
            h "No... No, you will not."
            show bg ch4ellens5 with dissolve
            n "With a banshee's wail, Gloria shrieks into the mic"
            g "\"I will see you on the other side!\""
            n "Luckily for you both, the mic does not amplify the horror that emerges"
            show bg ch4ellens6 with dissolve
            g "*Sighs* Dang it, it's not plugged in."
            h "There is a God."
            show bg ch4ellens7 with dissolve
            g "*Giggles* Maybe the cord is around somewhere. Hold up."
            p "Gloria, maybe it's for the best. We don't want to announce our presence."
            g "Phooey."
            h "He has a point."
            g "You lucked out this time, Bigs."
            $ extraevents.append("ch4sing")
            $ g_score += 1
        "Leave it be":



            p "The big guy is right. Ellen can get a little touchy when it comes to her stuff."
            show bg ch4ellens3 with dissolve
            g "Yeah... You're probably right. It's still ultra-prime, though."
            g "Think she'd mind if I look around?"
            p "I can't see the harm."
    if "ch4sing" in extraevents:
        h "Yes, I did."
    else:
        h "After today, I need a breather."
    show bg ch4ellens10 with dissolve
    h "How is Ellen? I haven't seen her in..."
    show bg ch4ellens11 with dissolve
    g "Five years I think. You took me to her last big concert."
    h "Don't remind me."
    show bg ch4ellens12 with dissolve
    p "Heh, not a fan?"
    g "He doesn't like anything that's not a million years old."
    h "The girl had talent, don't get me wrong."
    g "Has, Henry. Has talent."
    show bg ch4ellens13 with dissolve
    h "Has. And my taste isn't that old fashioned, is it?"
    g "Ancient. Like who even heard of the Falcons or whatever?"
    h "The Eagles and..."
    show bg ch4ellens14 with hpunch
    n "Under Henry's immense weight, the chair buckles"
    show bg ch4ellens15 with vpunch
    p "..!"
    h "*Grumbles under his breath* Ow."
    show bg ch4ellens16 with dissolve
    g "Henry! Are you alright?"
    h "I'm fine..."
    show bg ch4ellens17 with dissolve
    g "Don't be too proud, Bigs. Come on, up we go."
    p "Heh, Need help?"
    g "*Grunts* Nope, I got this!"
    show bg ch4ellens18 with dissolve
    g "Phew, there we go."
    p "Not sure how much you contributed there."
    h "It's the effort that counts."
    g "He's just too proud to admit when he needs help."
    p "I won't argue with you there. Gibson, you sure you're okay?"
    show bg ch4ellens19 with dissolve
    h "Just a bruised ego."
    g "You're ultra-heavy by the way. That was a workout."
    show bg ch4ellens20 with dissolve
    g "This is the life. Ellen really has it all."
    p "Not sure how much she'd agree with you."
    h "Wait... If that's what I think it is back there? I'm with the little one."
    show bg ch4ellens21 with dissolve
    g "What are you talking about?"
    h "Behind you."
    show bg ch4ellens23 with dissolve
    h "An actual pool table! Real balls and everything! None of that fake flashy crap."
    show bg ch4ellens24 with dissolve
    p "Not sure how flat it is, but yeah, one of Ellen's bandmates loved that old school shit."
    h "You play?"
    p "I might."
    menu:
        "Want a game?":
            if "ch4fightkill" in extraevents or "ch4fightspare" in extraevents:
                p "Up for a game? If you don't mind me kicking your ass again, that is."
                h "Don't make me stick one of these pool cues up where the sun doesn't shine."
            else:
                p "Up for a game?"
                h "Aren't you scared I'm goning to kick your ass again?"
                p "Not really. Pool's about finesse, not crazy brute strength."
                h "Yeah, shame you don't have either, Ghost."
            jump ch4ellenspool
        "Probably should leave it alone":

            p "Rather not, who knows what Ellen would think."
            h "Ahh, too bad."
            jump ch4ellensgloriatalk


label ch4ellenspool:
    $ h_score += 1
    $ extraevents.append("ch4pool")
    show bg ch4ellens22 with dissolve
    g "Are you guys really about to fight about a silly game?"
    p "It will be less of a fight and more of a slaughter, if he's not too scared that is."
    show bg ch4ellens25 with dissolve
    h "You got balls, Ghost."
    p "Stop talking and rack 'em."
    show bg ch4ellens26 with dissolve
    h "Your funeral."
    g "Well, at least they're not trying to kill each other, so that's a bonus."
    show bg ch4ellens27 with dissolve
    h "You say something, Gloria?"
    g "Nope. Just kick his ass, Henry!"
    p "Hey, that's not fair!"
    g "Why's that?"
    p "Blatant favoritism. He's got his own cheer squad!"
    show bg ch4ellens28 with dissolve
    p "Then again, he needs the home-field advantage."
    g "*sighs* Wow... you two don't stop."
    show bg ch4ellens29 with dissolve
    h "You're up. Let's see if you are as bad a shot with a cue as you are with a rifle."
    p "Time to lay down the pain."
    show bg ch4ellens30 with dissolve
    $ renpy.pause(1)
    show bg ch4ellens31 with dissolve
    $ renpy.pause(1)
    show bg ch4ellens32 with dissolve
    p "Boom."
    h "Nice."
    scene black with Dissolve(2)
    show bg ch4ellens33 with Dissolve(2)
    h "Not bad, [p]. You didn't embarrass yourself."
    p "Have to say, you were better than I thought. Not saying much, but still."
    h "Haven't had that much fun since Guam."
    show bg ch4ellens22 with dissolve
    g "Umm, what just happened? Who won?"
    p "No idea."
    h "Wasn't a standard set."
    g "All that trash talking and you don't even care?"
    p "Sure we do."
    g "Men are just weird sometimes."
    p "It goes both ways."
    h "Ain't that the truth."

label ch4ellensgloriatalk:
    if "ch4pool" in extraevents:
        show bg ch4ellens34 with Dissolve(2)
        g "Well, you had fun, at least."
        p "Of course. The big guy had more finesse than I thought. He surprised me."
        g "He'll do that. First time I met him, he scared the crap out of me."
        p "I can imagine."
        show bg ch4ellens35 with Dissolve(2)
        g "But he's just a big softie at heart, you know? He's not a killer."
        menu:
            "Yes he is":
                p "He might be a softie, but he'll always be dangerous."
                show bg ch4ellens36 with dissolve
                g "That's not fair."
                p "He tries not to be and I'm glad for that. But it doesn't matter in the end."
                g "Henry's a good man."
                p "And a killer. Trust me. It takes one to know one."
                g "So if I think you're a killer what does that say about me?"
                p "(I wish I knew.)"
                p "Uh... so..."
            "Not anymore.":
                p "But he was. In the war he had to have seen some shit."
                show bg ch4ellens36 with dissolve
                g "I know. He did stuff and he's not proud of it, but that's not who he is."
                p "I hope that's true."
                g "Because maybe you can be more than a killer too?"
                p "You in my head again?"
                g "Not this time. I just..."
                g "I know the feeling."
                p "(this poor girl, what the hell has she been through?)"
                p "Uh... so..."
    p "I bet when you woke up this morning, you didn't think you would end up here?"
    g "When I woke up this morning I thought you were coming to kill me."
    p "Killing you was never part of the plan. Hiding you... well that wasn't either."
    show bg ch4ellens35 with dissolve
    g "Life throws you for a loop sometimes."
    p "Well, what you did... It put things in perspective for me."
    show bg ch4ellens36 with dissolve
    g "That's a nice way of saying I scared the crap out of you."
    p "That too. But not for why you think. I was scared for you. What you can do, a lot of people are going to want to use it."
    g "I barely even know what {i}it{/i} is..."
    p "Hey, cheer up. I think Ellen should be here soon."
    show bg ch4ellens37 with dissolve
    g "You're right, I shouldn't be all frowny when she gets here."
    p "One question, though. By the sounds of it, you could have gone and seen her whenever you wanted. Why didn't you?"
    show bg ch4ellens36 with dissolve
    g "After everything that happened with my Dad, the last thing she needed was someone to remind her of it."
    if "ch2chooseellen" in extraevents:
        p "She would have liked seeing you."
        g "I doubt it."
        p "Sounds like an excuse to me."
    p "Well, she'll be here soon."
    show bg ch4ellens38 with Dissolve(5)
    p "(Or not. Damn, Ellen, its been hours. Where are you?)"
    g "Starting to think I was right about you trying to get me alone and all..."
    p "You know Ellen, she's..."
    e "Right behind you, [p]. Now what the fuck is going..."
    show bg ch4ellens39 with dissolve
    g "Ellen!"
    jump ch4ellenshow
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
