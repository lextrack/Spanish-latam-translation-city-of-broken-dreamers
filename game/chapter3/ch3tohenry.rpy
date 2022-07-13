


image bg ch3tohenry1 = "ch3tohenry1"
image bg ch3tohenry2 = "ch3tohenry2"
image bg ch3tohenry3 = "ch3tohenry3"
image bg ch3tohenry4 = "ch3tohenry4"
image bg ch3tohenry5 = "ch3tohenry5"
image bg ch3tohenry6 = "ch3tohenry6"
image bg ch3tohenry7 = "ch3tohenry7"
image bg ch3tohenry8 = "ch3tohenry8"
image bg ch3tohenry9 = "ch3tohenry9"
image bg ch3tohenry10 = "ch3tohenry10"
image bg ch3tohenry11 = "ch3tohenry11"
image bg ch3tohenry12 = "ch3tohenry12"
image bg ch3tohenry13 = "ch3tohenry13"
image bg ch3tohenry14 = "ch3tohenry14"
image bg ch3tohenry15 = "ch3tohenry15"
image bg ch3tohenry16 = "ch3tohenry16"
image bg ch3tohenry17 = "ch3tohenry17"
image bg ch3tohenry18 = "ch3tohenry18"
image bg ch3tohenry19 = "ch3tohenry19"
image bg ch3tohenry20 = "ch3tohenry20"
image bg ch3tohenry21 = "ch3tohenry21"
image bg ch3tohenry22 = "ch3tohenry22"
image bg ch3tohenry23 = "ch3tohenry23"
image bg ch3tohenry24 = "ch3tohenry24"
image bg ch3tohenry25 = "ch3tohenry25"
image bg ch3tohenry26 = "ch3tohenry26"
image bg ch3tohenry27 = "ch3tohenry27"
image bg ch3tohenry28 = "ch3tohenry28"
image bg ch3tohenry29 = "ch3tohenry29"
image bg ch3tohenry30 = "ch3tohenry30"
image bg ch3tohenry31 = "ch3tohenry31"
image bg ch3tohenry32 = "ch3tohenry32"
image bg ch3tohenry33 = "ch3tohenry33"


image ch3citypanmovie = Movie(play='video/chapter-3-video/ch3citypan.webm', loop=False)
image bg ch3citypanmov movie:
    "ch3citypanmovie"
    pause 12.0
    "black"

label ch3tohenry:
    scene black with Dissolve(1)
    show bg ch3stairway43 with Dissolve(1)
    stop music fadeout 2.0
    if "ch3venusslut" in extraevents or "ch3venusprincess" in extraevents:
        p "Sonja, wait!"
        j "Wow, always following your dick."
        show bg ch3stairway45 with dissolve
        j "I hope you learned something."
        j "And by something, I mean, learned something about your little target? Not about Voskok's latest product."
        p "I did. Look, Betty asked me for a favor, testing out her new model, just trying to stay on her good side!"
        show bg ch3stairway46 with dissolve
        j "Ugh! Too much information. I don't need to hear about your oddball conquests."
        p "That doesn't sound like the crazy woman I married."
        show bg ch3stairway44 with dissolve
        $ insult = renpy.random.choice(insults)
        j "Things change, [insult], and you don't mix business and pleasure. Come on, let's find your little blondie."
        jump ch3tohenrycont
    else:

        p "Hey, Sonja, wait up."
        if "ch3sonjatruth" in extraevents:
            show bg ch3stairway45 with dissolve
            j "You could have told me she was one of your contacts. Fuck me, that was embarrassing."
            p "One, this is my job. Two, we're in the same line of work, so we're going to have some overlap. And, finally, I've known Betty longer than I've known you."
            j "And she never came up?"
            p "Not like I was a regular at this place before we got married."
            show bg ch3stairway44 with dissolve
            j "She wouldn't talk to me anyway. So, win-win, I guess."
            p "I got what I need. It's close."
            jump ch3tohenrycont
        else:
            j "Did you learn anything?"
            p "Yeah, not far from here, actually."
            show bg ch3stairway44 with dissolve
            j "So what are we waiting for? Let's find her."
            jump ch3tohenrycont

label ch3tohenrycont:
    scene black with Dissolve(1)
    show bg ch3tohenry2 with Dissolve(1)
    play music audio.prepare fadein 2.0 fadeout 2.0
    p "The last bastion of LAPD security before we get in deeper."
    show bg ch3tohenry1 with dissolve
    j "And she is near here, you think? It's not far from the original incident."
    p "Best place to hide. Half the people in Mil-town are off the grid already. And someone like him wouldn't stand out as much, not that they are looking for him."
    show bg ch3tohenry3 with dissolve
    j "And this \"him\"? How's he connected to our little runaway?"
    p "He's her old bodyguard. Big guy. Looks to be a gen-one augment. He's supposed to be dead, but I'm not convinced."
    j "Why is that?"
    p "Eight-foot-tall wall of muscle starts showing up right when all of this shit goes down? It's not a leap, Sonja."
    show bg ch3tohenry4 with dissolve
    j "What's he want with the girl? Is he competition?"
    p "I don't think so."
    j "You sure about that?"
    p "No. Just a feeling."
    $ insult = renpy.random.choice(insults)
    j "Then I trust it. But, [p], if this guy really is a gen-one..."
    p "I know the risks."
    j "This is more than a fucking risk! We're talking human killing machine, known psychological problems and that's just the start. Those fuckers went toe to toe with Red Moon's half breeds."
    p "I said I know the risks."
    j "Best hope he became a pacifist in his old age, shitbrick."
    p "Doubtful."
    show bg ch3tohenry5 with dissolve
    j "On the bright side, if he kills your dumb ass, I won't have to file the divorce papers."
    p "Always looking on the bright side, aren't you?"
    j "It's a gift."

    scene black with Dissolve(2)
    show text "{=trans}AFTER SOME TIME SEARCHING THE MAYBANK AREA{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    j "Nothing..."
    show bg ch3tohenry6 with dissolve
    p "Did you check down there?"
    show bg ch3tohenry7 with dissolve
    $ renpy.pause(1)
    show bg ch3tohenry8 with dissolve
    j "Nope."
    show bg ch3tohenry9 with dissolve
    j "Are you coming?"
    p "Hold on."
    show bg ch3tohenry10 with dissolve
    $ insult = renpy.random.choice(insults)
    j "You're not just getting soft, [insult], slow as-"
    p "Sonja, stop!"
    show bg ch3tohenry11 with dissolve
    j "Shit, thanks..."
    p "Thank the smog."
    p "I may be slow, but I'm careful."
    show bg ch3tohenry12 with dissolve
    j "Now I feel like the amateur. What do you think this is tied to?"
    p "Most likely a perimeter alarm. Just keep a lookout."
    n "The sound of a door opening can be heard further down the alley."
    show bg ch3tohenry13 with hpunch
    $ renpy.pause(1)
    show bg ch3tohenry14 with dissolve
    j "Psst! Hide!"
    p "(Come on, where are you?)"
    show bg ch3tohenry17 with dissolve
    j "*Whispering* [p], I can take him out."
    p "Not yet! You miss we're fucked."
    show bg ch3tohenry16 with dissolve
    n "The ominous sounds of heavy footsteps can be heard ahead."
    j "Anything?!?"
    show bg ch3tohenry15 with dissolve
    p "(Looking pretty good for a dead man, eh, motherfucker?)"
    show bg ch3tohenry18 with dissolve
    p "(Sonja, don't you do it.)"
    j "Fuck this..."
    p "Wait!"
    show bg ch3tohenry19 with dissolve
    j "Where the fuck did he go?! He didn't spot us, did he?"
    p "He's not trying to crush our skulls, so I don't think so."
    show bg ch3tohenry17 with dissolve
    j "But that was the guy? The Bodyguard."
    p "Yeah, it was... pictured him even bigger."
    j "Well then, what now? We know this is where he lives and he doesn't know we know. I say we come back tonight?"

    $ resetmenu()
    menu:
        "Leave":
            p "Not a bad idea. Let's get back to your place -- one too many close calls for now."
            j "OOH! Do you think I can use Stella this time?"
            p "For him? Be my guest."
            jump ch3sonjaleave
        "Investigate further":
            jump ch3tohenryinv



label ch3tohenryinv:
    p "No way that tripwire was his only security."
    j "If I tag him from across the way, it won't matter."
    p "And if it spooks the target and he has some alternate exits? We need to know what else we're dealing with."
    j "Lead the way."
    show bg ch3tohenry19 with dissolve
    p "Keep low and get ready to bug out."
    show bg ch3tohenry20 with dissolve
    p "This place looks normal, but he's got it locked down like a fortress."
    j "Yeah, I can get through, but it will take some time."
    j "I'd call Kay, but something tells me these are old school. Off the net."
    p "We're not going in yet. At least right now."
    show bg ch3tohenry21 with dissolve
    j "All the windows are barred. That door looks military grade."

    jump ch3tohenrymenu


label ch3tohenrymenu:

    if menu1 == False and menu2 == False and menu3 == False:
        jump ch3sonjaleave

    menu:
        "Check the door" if menu1:
            $ menu1 = False
            $ extraevents.append("ch3henrydoor")
            p "Curious about this door."
            show bg ch3tohenry22 with dissolve
            j "Yeah, military grade just like I thought. Where did he get this? Kay couldn't even get through this thing without being onsite."
            p "A few shaped charges could crack the bastard, but there goes any sense of surprise."
            j "I don't know, explosions are surprising."
            p "Not to someone like him."
            j "Hey, shithead, check this out."
            show bg ch3tohenry23 with dissolve
            p "I wonder where that leads?"
            j "Only one way to find out."
            jump ch3tohenrymenu

        "Check the windows" if menu2:
            $ menu2 = False
            $ extraevents.append("ch3henrywindow")
            p "Okay, the windows might be a better bet."
            scene black with dissolve
            show bg ch3tohenry29 with dissolve
            p "It looks like the cleaning drone didn't replace the grating over there."
            p "That could work."
            j "I don't know..."
            show bg ch3tohenry33 with dissolve
            j "You're going to need a grapple to get up there, which makes you a sitting duck on the way up. Plus, we don't know where it goes."
            p "Right and if I get stuck up there. I have no easy way out."
            show bg ch3tohenry32 with dissolve
            j "Getting out is easy. Surviving the landing, that's the hard part."
            jump ch3tohenrymenu
        "Check the hatch" if menu1 == False and menu3 != False:
            $ menu3 = False
            p "Okay, let's go down."
            scene black with Dissolve(1)
            show bg ch3tohenry24 with Dissolve(3)
            n "The sound of pumps and machinery fills the dark basement. The hot sticky air clings to your face."
            j "*Whispering* Damn, it's dark down here."
            p "It may lead upstairs."
            j "Yeah, but if it does, why didn't he lock it?"
            p "Good point..."
            j "[p], I think we should leave."
            menu:
                "Not yet":
                    $ extraevents.append("ch3henrybasement")
                    p "We're not done here yet."
                    show bg ch3tohenry25 with dissolve
                    p "See? A way upstairs. Be ready for anything."
                    j "You're going so far in front, it's not funny."
                    show bg ch3tohenry26 with dissolve
                    j "Careful."
                    p "I clear the traps and you get the locks, that's how it works."
                    j "Yeah, but unlike me, you haven't dealt with this level of shit in a while."
                    p "What, scared I'll get hurt? I'm touched."
                    j "..."
                    p "I thought so. Now, what do we have here?"
                    show bg ch3tohenry27 with dissolve
                    j "What do you see?"
                    p "Mark II, EMP. Knock any bot out cold. We would just be pissing our pants and talking backward for a week."
                    p "He must have this whole place rigged."
                    show bg ch3tohenry28 with dissolve
                    j "Now, let's get the fuck out of here."
                    p "Yeah, Need a proper scanner to get through this. One false move and it's blown along with my bladder. "
                "Leave":
                    p "Yeah, now can we out of here."
                    jump ch3tohenrymenu


        "Leave" if menu1 == False or menu2 == False or menu3 == False:
            jump ch3sonjaleave


label ch3sonjaleave:
    if menu1 == False or menu2 == False or menu3 == False:
        j "Finally, let's get out of here."
    else:
        j "That was quick. Let's get out of here."
    window hide
    show bg ch3citypanmov movie with dissolve
    $ renpy.pause(12)
    window show
    scene black with dissolve
    show bg ch3tohenry30 with dissolve
    stop music fadeout 3.0
    j "Well, you got what you needed. So, what now?"
    p "It'll go down tonight. You game?"
    j "Fuck yeah, I am! Like you have to ask?"
    p "Okay, I need to follow up on another lead. I'll call you when we're good to go."
    show bg ch3tohenry31 with dissolve
    j "Don't wait too long shitstreak. This'll be fun."
    jump ch3doc
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
