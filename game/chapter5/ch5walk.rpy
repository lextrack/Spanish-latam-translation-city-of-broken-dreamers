
image bg ch5shanlon1 = "ch5shanlon1"
image bg ch5shanlon2 = "ch5shanlon2"
image bg ch5shanlon3 = "ch5shanlon3"
image bg ch5shanlon4 = "ch5shanlon4"
image bg ch5shanlon5 = "ch5shanlon5"
image bg ch5shanlon6 = "ch5shanlon6"
image bg ch5shanlon7 = "ch5shanlon7"


image bg ch5walk1 = "ch5walk1"
image bg ch5walk2 = "ch5walk2"
image bg ch5walk3 = "ch5walk3"
image bg ch5walk4 = "ch5walk4"
image bg ch5walk5 = "ch5walk5"
image bg ch5walk6 = "ch5walk6"
image bg ch5walk7 = "ch5walk7"
image bg ch5walk8 = "ch5walk8"
image bg ch5walk9 = "ch5walk9"
image bg ch5walk10 = "ch5walk10"
image bg ch5walk11 = "ch5walk11"
image bg ch5walk12 = "ch5walk12"
image bg ch5walk13 = "ch5walk13"
image bg ch5walk14 = "ch5walk14"
image bg ch5walk15 = "ch5walk15"
image bg ch5walk16 = "ch5walk16"
image bg ch5walk17 = "ch5walk17"
image bg ch5walk18 = "ch5walk18"
image bg ch5walk19 = "ch5walk19"
image bg ch5walk20 = "ch5walk20"
image bg ch5walk21 = "ch5walk21"
image bg ch5walk22 = "ch5walk22"
image bg ch5walk23 = "ch5walk23"
image bg ch5walk24 = "ch5walk24"
image bg ch5walk25 = "ch5walk25"
image bg ch5walk26 = "ch5walk26"
image bg ch5walk27 = "ch5walk27"
image bg ch5walk28 = "ch5walk28"
image bg ch5walk29 = "ch5walk29"
image bg ch5walk30 = "ch5walk30"
image bg ch5walk31 = "ch5walk31"


label ch5walk:
    play music audio.sol fadein 2.0 fadeout 2.0
    scene black with Dissolve(2)
    show bg ch5walk1 with Dissolve(2)
    p "Blonde again? Alright. Some fresh air might help clear your head, let you relax a bit."
    p "A few conditions, though."
    g "Like?"
    p "Don't talk to anyone. Don't make eye contact with anyone and, for the love of god, no showing off."
    g "You want me to wear a burkha, too? Less people can see me."
    p "I'm serious."
    g "I understand, but remember, I've been on my own since I was 16 and off the grid for most if it."
    g "Plus... this..."
    show bg ch5walk2 with dissolve
    $ renpy.pause(1)
    show bg ch5walk3 with dissolve
    p "I don't know if I'll ever get used to that."
    show bg ch5walk4 with dissolve
    g "I dunno, it is kind of cool, though, right?"
    p "Kind of, yes. Okay, very."
    show bg ch5walk5 with dissolve
    g "See, who says you're a curmudgeon."
    p "Off the top of my head, Ellen, Doc, Sonja. Most of my clients."
    g "Well, they're right, but thanks for this anyway."
    scene black with Dissolve(1)
    show bg ch5walk6 with Dissolve(1)
    g "Ah! Ok, perfect day, flat out! The real sun, no dust storms either."
    g "You gotta love this, right?"
    p "A bit. But you are standing out a bit here."
    p "Remember what I said. Now, what do you want to eat?"
    show bg ch5walk7 with dissolve
    g "Anything but cereal. So over it. Oh, and no coffee. But I could MURDER some brunch right now."
    p "Fucking brunch... God, I hate that."
    show bg ch5walk8 with dissolve
    g "Ha, what? How can you hate brunch?! That doesn't even make sense. It's like the best meal of the day."
    p "Brunch is the worst. You know why I hate brunch?"
    show bg ch5walk10 with dissolve
    g "Because you're a curmudgeon... But no, why do you hate brunch?"

    menu:
        "It's for rich people":
            p "Rich folks eat brunch. It's a total pretentious meal. Like breakfast or lunch isn't good enough for them, so they had to do something special."
            show bg ch5walk9 with dissolve
            g "Well, I love brunch. Mom and I used to go once a month. Maybe if you don't like it, there's something wrong with you."
            p "Right. Just... I was trying to... Forget I said anything."
            g "It's fine. Not like I can get any around here anyway."
        "Hipsters love brunch":
            $ g_score += 1
            $ extraevents.append("ch5brunch")
            p "Hipsters love brunch. Always posting pics of their meals on the net. As if their meals are special or something."
            show bg ch5walk11 with dissolve
            g "Damn it, you're right. Hipsters do like brunch. Judgmental, pretentious. I can't stand them. Not to mention their fake sympathy. Just to get attention."
            p "Exactly. It's why they have brunch!"
            g "Shit, but you know what? Hipsters ruined coffee for me, but they aren't ruining brunch. Screw hipsters, but they can't have the best meal!"
            p "Well, I tried."
            g "*Laughs* Still the oddest argument ever. I think, if you hate brunch you just haven't had a good one."
            p "No way."
            g "Come on, you, me and Ellen are totally gonna have brunch."
            p "You think Ellen is a brunch person?"
            g "She's awesome, so, yes."
            p "Fine, you win."
        "It's way too fancy":

            p "It's way too fancy. Whatever happened to just a simple coffee, bacon and eggs when you wake up."
            p "Now it has to be some event. And what's with mixing breakfast and lunch. PICK ONE!"
            p "And don't even get me started on that whole fake egg in the wine."
            show bg ch5walk11 with dissolve
            g "Wow, did brunch kill your family or something? Steal your wife?"
            p "No. I just hate it."
            g "To each their own! [p], I think you're missing out."
    show bg ch5walk12 with dissolve
    p "How about some noodles for lunch."
    show bg ch5walk13 with dissolve
    if "ch5brunch" in extraevents:
        g "It's no brunch, but it'll do."
        p "Well, look at it this way, no hipsters."
        g "Exactly!"
    else:
        g "For brunch!"
        p "*sighs*"
        g "This is too funny."
        p "Forget I said anything..."
    show bg ch5walk14 with dissolve
    p "Hello?"
    show bg ch5walk15 with dissolve
    "Cook" "Huh! Oh!"
    show bg ch5walk16 with dissolve
    "Cook" "Well, order!?"
    p "Gloria, how much do you think Henry needs?"
    show bg ch5walk17 with dissolve
    g "No idea, maybe three?"
    p "Okay, six of your specials to go."
    show bg ch5walk20 with dissolve
    "Television" "And now for a special bulletin from Los Angeles News with your host, Shanlon Russell."
    g "Oh great..."
    show bg ch5walk21 with dissolve
    $ renpy.pause(2)
    show bg ch5shanlon2 with dissolve
    sh "What do you mean we're live? You idiot!"
    show bg ch5shanlon1 with dissolve
    sh "Ahh, good morning, Los Angeles."
    sh "In our first story, we have an update on the wanted fugitive, Gloria Conner."
    show bg ch5shanlon3 with dissolve
    sh "LAN has just gotten word that two law enforcement contractors were hospitalized last night in an attempt to apprehend her."
    show bg ch5shanlon4 with dissolve
    sh "Officials again warn that Ms. Conner is highly dangerous and if you see her, contact the LAPD immediately. Do not try to apprehend."
    sh "With me now is Gloria's father, famed recording producer, Alexis Conner."
    show bg ch5shanlon5 with dissolve
    sh "If you could say one thing to your daughter right now, what would it be?"
    show bg ch5shanlon6 with dissolve
    a "Gloria, honey, I don't know what you have gotten yourself into, but people are scared."
    a "If your mother were still with us, she would want you to come home."
    a "I don't know the whole story, but I have the best lawyers in the world ready to help you through this. I'm sure it's all a misunderstanding."
    a "I still don't know why you ran away, but I haven't changed your room one bit."
    show bg ch5shanlon5 with dissolve
    sh "Touching. Is there anything else?"
    show bg ch5shanlon7 with dissolve
    a "Just that I miss you, Gloria. Know that your Papa loves you."
    show bg ch5shanlon3 with dissolve
    sh "Thank you, Mr. Conner."
    sh "Now that is taken care of, yesterday, five police officers were injured in the protests just north of Mil-town."
    show bg ch5walk18 with dissolve
    p "Gloria... are you ok? That can't have been easy."
    g "It's fine... God, I hate that woman."
    p "Katie's not a fan either."
    show bg ch5walk19 with dissolve
    g "Why am I not surprised. Katie is like the Bizarro Shanlon."
    g "Or is it the other way around."
    "Cook" "Order's ready."
    p "Come on, let's get back. Probably taking too big a risk as is, we should get back inside."
    g "Yeah..."
    show bg ch5walk17 with dissolve
    g "Hey, [p]?"
    p "What?"
    g "Do you think Papa..."
    show bg ch5walk18 with dissolve
    g "Never mind. I mean... Do you really think we'll get through this?"
    p "I wish I could tell you. I just don't know."
    show bg ch5walk19 with dissolve
    g "Heh, you're not filling me with confidence here."
    g "Thankfully I have enough for the both of us."
    p "Heh, come on, let's get back."
    scene black with Dissolve(1)
    show bg ch5walk22 with dissolve
    g "Damn... She looks hungry. How can we still have so many homeless?"
    show bg ch5walk25 with dissolve
    g "Hey, kid, here. It's not much, but it's good."
    show bg ch5walk24 with dissolve
    "Kid" "Ummm... thanks."
    menu:
        "No talking":
            $ extraevents.append("ch5glorianotalking")
            show bg ch5walk29 with dissolve
            p "Hey, what did I say!"
            g "Shit, sorry it's just-"
            p "I don't care. Come on; we need to get back."
            scene black with Dissolve(2)
            show bg ch5walk31 with dissolve
            g "I'm sorry, I didn't mean to."
            p "Gloria, look, we have to be careful. What you did was dangerous."
            g "I know..."
            p "Well, don't beat yourself up. We could all learn something from you."
            p "Look, I'll find Henry. You go hang out with Ellen for a bit."
            jump ch5henry
        "Say nothing":



            $ extraevents.append("ch5gloriatalked")

            show bg ch5walk23 with dissolve
            g "You're welcome."
            p "Feel better?"
            show bg ch5walk27 with dissolve
            g "Yeah. It's weird sometimes, I don't know if I do things like that to make them feel better. Or myself."
            p "Does it matter?"
            g "Sure it does. Like if we do everything for selfish reasons?"
            p "I think we do what we can... when we can."
            show bg ch5walk28 with dissolve
            g "Huh. I don't know. I see people like Ellen and Henry, and think that good has to exist, right?"
            p "You're asking the wrong guy."
            show bg ch5walk26 with dissolve
            "Woman" "That was nice of her."
            "Kid" "Yeah she was a nice lady."
            "Kid" "She looks like the famous one."
            "Woman" "Who dear?"
            "Kid" "The girl on the big screens everywhere."
            "Woman" "..."
            scene black with Dissolve(2)
            show bg ch5walk30 with dissolve
            g "You're not mad at me? For breaking one of your rules."
            p "No, I'm not mad, but you do need to be careful. Just try not to do that in the future."
            g "Yeah... Sorry..."
            p "No problem. Go bug Ellen; I'll see if I can find Henry and let him know we got some grub."
            jump ch5henry
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
