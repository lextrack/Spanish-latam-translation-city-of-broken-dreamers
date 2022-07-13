

image bg ch6watch1 = "ch6watch1"
image bg ch6watch2 = "ch6watch2"
image bg ch6watch3 = "ch6watch3"
image bg ch6watch4 = "ch6watch4"
image bg ch6watch5 = "ch6watch5"
image bg ch6watch6 = "ch6watch6"
image bg ch6watch7 = "ch6watch7"
image bg ch6watch8 = "ch6watch8"
image bg ch6watch9 = "ch6watch9"
image bg ch6watch10 = "ch6watch10"
image bg ch6watch11 = "ch6watch11"
image bg ch6watch12 = "ch6watch12"
image bg ch6watch13 = "ch6watch13"
image bg ch6watch14 = "ch6watch14"
image bg ch6watch15 = "ch6watch15"
image bg ch6watch16 = "ch6watch16"
image bg ch6watch17 = "ch6watch17"
image bg ch6watch18 = "ch6watch18"
image bg ch6watch19 = "ch6watch19"
image bg ch6watch20 = "ch6watch20"
image bg ch6watch21 = "ch6watch21"
image bg ch6watch22 = "ch6watch22"
image bg ch6watch23 = "ch6watch23"
image bg ch6watch24 = "ch6watch24"
image bg ch6watch25 = "ch6watch25"
image bg ch6watch26 = "ch6watch26"
image bg ch6watch27 = "ch6watch27"
image bg ch6watch28 = "ch6watch28"
image bg ch6watch29 = "ch6watch29"
image bg ch6watch30 = "ch6watch30"
image bg ch6watch31 = "ch6watch31"
image bg ch6watch32 = "ch6watch32"
image bg ch6watch33 = "ch6watch33"
image bg ch6watch34 = "ch6watch34"
image bg ch6watch35 = "ch6watch35"
image bg ch6watch36 = "ch6watch36"
image bg ch6watch37 = "ch6watch37"
image bg ch6watch38 = "ch6watch38"
image bg ch6watch39 = "ch6watch39"
image bg ch6watch40 = "ch6watch40"
image bg ch6watch41 = "ch6watch41"
image bg ch6watch42 = "ch6watch42"
image bg ch6watch43 = "ch6watch43"
image bg ch6watch44 = "ch6watch44"
image bg ch6watch45 = "ch6watch45"
image bg ch6watch46 = "ch6watch46"
image bg ch6watch47 = "ch6watch47"
image bg ch6watch48 = "ch6watch48"
image bg ch6watch49 = "ch6watch49"
image bg ch6watch50 = "ch6watch50"
image bg ch6watch51 = "ch6watch51"
image bg ch6watch52 = "ch6watch52"
image bg ch6watch53 = "ch6watch53"
image bg ch6watch54 = "ch6watch54"
image bg ch6watch55 = "ch6watch55"
image bg ch6watch56 = "ch6watch56"
image bg ch6watch57 = "ch6watch57"
image bg ch6watch58 = "ch6watch58"
image bg ch6watch15vic = "ch6watch15vic"




label ch6venusslut:
    p "Get over here."
    show bg ch6watch16 with dissolve
    ve "Yes, my Master."
    show bg ch6watch17 with dissolve
    p "You're a bad girl, aren't you?"
    ve "Yes..."
    show bg ch6watch18 with dissolve
    p "Get on the fucking ground."
    ve "OH, Master!"
    ve "You truly want to vent your frustration tonight."
    show bg ch6watch19 with dissolve
    ve "Under the bed, there is a present. It would be... Suitable for your current mood."
    show bg ch6watch20 with dissolve
    p "Mmm, this could be fun."
    ve "Put it in my mouth. Make her yours."
    p "Phew..."
    show bg ch6watch21 with dissolve
    ve "*Behind the gag* Do you like?"
    menu:
        "Just use Venus":
            jump ch6venusslutscene
        "Pretend she is Victoria":

            jump ch6venusvictoria


label ch6venusslutscene:
    if _in_replay:
        play music audio.tensesexy fadein 2.0
        $ setReplay()
        show bg ch6watch16 with dissolve
        p "Get over here."
        ve "Yes, my Master."
        show bg ch6watch17 with dissolve
        p "You're a bad girl, aren't you?"
        ve "Yes..."
        show bg ch6watch18 with dissolve
        p "Get on the fucking ground."
        ve "OH, Master!"
        ve "You truly want to vent your frustration tonight."
        show bg ch6watch19 with dissolve
        ve "Under the bed, there is a present. It would be... Suitable for your current mood."
        show bg ch6watch20 with dissolve
        p "Mmm, this could be fun."
        ve "Put it in my mouth. Make her yours."
        p "Phew..."
        show bg ch6watch21 with dissolve
        ve "*Behind the gag* Do you like?"



    p "Oh, I'm going to do bad things to you."
    ve "Mmm..."
    p "Bend over, let me see that huge ass of yours."
    show bg ch6watch22 with dissolve
    ve "Master, these panties are in the way."
    show bg ch6watch23 with dissolve
    p "We can fix that. Probably need to loosen you up."
    ve "Mmm, yes."
    show bg ch6watch25 with dissolve
    p "You like it when I play with your ass, don't you?"
    ve "Mmmhmm."
    show bg ch6watch26 with dissolve
    $ renpy.pause(1)
    show bg ch6watch27 with dissolve
    $ renpy.pause(1)
    show bg ch6watch28 with dissolve
    p "I think you are ready now."
    show bg ch6watch24 with dissolve
    p "Question is, what do I do with you?"
    $ resetsexmenu()
    jump ch6venusslutmenu


label ch6venusslutmenu:
    menu:
        "Anal on the floor":
            $ sexmenu1 = False
            jump ch6venusslutanal1
        "Tit fuck":
            $ sexmenu1 = False
            jump ch6venussluttits
        "Anal on top":
            $ sexmenu1 = False
            jump ch6venusslutanal2
        "Blow Job and cum":
            $ sexmenu1 = False
            jump ch6venusslutblow


image bg ch6venusanal movie = Movie(play='video/chapter-6-video/ch6venusanal.webm')
image bg ch6venusanal2 movie = Movie(play='video/chapter-6-video/ch6venusanal2.webm')
image bg ch6venusanal3 movie = Movie(play='video/chapter-6-video/ch6venusanal3.webm')
image bg ch6venusanal4 movie = Movie(play='video/chapter-6-video/ch6venusanal4.webm')

image bg ch6venusblow movie = Movie(play='video/chapter-6-video/ch6venusblow.webm')
image bg ch6venustitfuck movie = Movie(play='video/chapter-6-video/ch6venustitfuck.webm')

label ch6venusslutanal1:
    if sexmenu2 == False:
        $ sexmenu2 = True
        p "Get that gag back in your mouth."
    show bg ch6watch29 with dissolve
    ve "Use that ass."
    p "That's the plan. Wait, what's this going to cost me?"
    ve "Nothing, master."
    show bg ch6watch30 with dissolve
    p "That's exactly what I wanted to hear. Now, I hope you are ready."
    ve "Always ready."
    show bg ch6watch31 with dissolve
    p "Fuck me, that is tight."
    ve "Should I get looser?"
    p "I'll handle that."
    show bg ch6venusanal movie with dissolve
    ve "UUGH!!!"
    p "Damn, you bad girl!"
    ve "Yes, I am, Master!"
    show bg ch6watch32 with dissolve
    p "You want more?"
    ve "Mmmph! YES!"
    show bg ch6venusanal2 movie with dissolve
    p "You certainly don't have false advertising!"
    ve "That would be unethical."
    p "Don't think Vostok cares about that, but damn they built you well."
    p "So, what else can we do with you?"
    jump ch6venusslutmenu



label ch6venussluttits:
    if sexmenu2 == False:
        $ sexmenu2 = True
        p "Get that gag back in your mouth and flip over, I want to play with those comic-sized tits."
    else:
        p "Flip over, I want to play with those comic-sized tits."
    show bg ch6watch33 with dissolve
    p "That, I like."
    ve "Mmmm, play with them, Master."
    show bg ch6watch34 with dissolve
    p "This is something I never get tired of. Don't care what others say."
    show bg ch6watch35 with dissolve
    p "Keep your arms back like that."
    ve "Mmph, yes..."
    show bg ch6venustitfuck movie with dissolve
    p "Damn, these feel good, so fucking smooth."
    ve "Mmmhmm..."
    show bg ch6watch36 with dissolve
    p "Playing with these is fun, but there is so much more you can do for me."
    jump ch6venusslutmenu


label ch6venusslutanal2:
    if sexmenu2 == False:
        $ sexmenu2 = True
        p "Get that gag back in your mouth."
    else:
        $ sexmenu2 = False
    p "I want you to get on me. Sit that ass on my cock."
    show bg ch6watch41 with dissolve
    p "FUCK yes! You're my dirty slut, aren't you?"
    show bg ch6watch39 with dissolve
    ve "Mmm!!! Yes!"
    p "That's my girl."
    show bg ch6watch37 with dissolve
    p "Yes, right down on it."
    p "I want you to bounce on it as fast as you can."
    show bg ch6venusanal3 movie
    p "GAH! Holy shit! Not that fast!"
    ve "*With her mouth full* I'm sorry, Master."
    show bg ch6watch38 with dissolve

    p "Fuck me, one slip up and that could have been painful. "
    show bg ch6venusanal4 movie with dissolve
    p "There much better..."
    n "You can feel Venus tighten around your shaft"
    p "Oh fuck..."
    show bg ch6watch40 with vpunch
    ve "OH, MASTER! I'm cu-cumming!"
    p "I'm sure that always has to happen..."
    ve "Of course."
    jump ch6venusslutmenu



label ch6venusslutblow:
    if sexmenu2 == False:
        p "Suck me off till I blow."
    else:
        p "Get that gag out of your mouth and suck me off."
    show bg ch6watch45 with dissolve
    ve "Do you want me to go deep?"
    p "How else?"
    show bg ch6watch43 with dissolve
    ve "Good, because that is all I am programmed to do."
    show bg ch6venusblow movie with dissolve
    p "Wow! Keep going, just like that."
    n "Venus's mouth opens up as she takes you all the way down"
    p "Fuck me I'm almost there."
    show bg ch6watch44 with dissolve
    p "Shit, I'm going to cum!"

    menu:
        "Face":
            show bg ch6watch45 with dissolve
            ve "Feed me, Master!"
            p "Ah, goddammit!"
            show bg ch6watch46 with quickflash
            p "AAARGH!!!"
            show bg ch6watch47 with dissolve
            ve "Very good, I am glad my services could be put to use."
            p "I needed that, especially after today."
            show bg ch6watch48 with dissolve
            ve "Well, you are welcome."
            p "Now, If you don't mind, I need some time to myself."
            show bg ch6watch52 with dissolve
            ve "Very well, I will go back downstairs. If you need anything, let me know."
            p "I'll be fine, but thanks."
            show bg ch6watch53 with dissolve
        "Tits":


            show bg ch6watch45 with dissolve
            ve "Give it to me, Master"
            p "Ah, goddammit!"
            show bg ch6watch46 with quickflash
            p "AAARGH!!!"
            show bg ch6watch49 with dissolve
            ve "Very good, I am glad my services could be put to use."
            p "I needed that, especially after today."
            show bg ch6watch50 with dissolve
            ve "Well, you are welcome."
            p "Now, If you don't mind, I need some time to myself."
            show bg ch6watch51 with dissolve
            ve "Very well, I will go back downstairs. If you need anything, let me know."
            p "I'll be fine, but thanks."
            show bg ch6watch53 with dissolve

    play music audio.space fadein 2.0 fadeout 2.0
    p "Ugh, Sam..."
    s "Yes, Sir? Did you have fun?"
    p "A bit empty..."
    s "I'm sure you are."
    p "Not what I meant, Sam."
    s "May I suggest some rest? But that is up to you, Sir."
    p "Thanks, Sam."
    $ renpy.end_replay()
    if not persistent.ch6venussex:
        $ renpy.notify(['Scene Unlocked', 'unlock'])
        $ persistent.ch6venussex = True
    jump ch6stairwaymenu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
