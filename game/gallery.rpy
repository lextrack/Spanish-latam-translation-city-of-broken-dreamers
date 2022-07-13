



init python:


    galitems = []

    galitems.append(["ch1tut", "persistent.ch1tut"])


    galitems.append(["ch1bonus1", "persistent.ch1card1"])
    galitems.append(["ch1bonus2", "persistent.ch1card2"])
    galitems.append(["ch1bonus3", "persistent.ch1card3"])

    galitems.append(["ch2bonus1", "persistent.ch2card1"])
    galitems.append(["ch2bonus2", "persistent.ch2card2"])
    galitems.append(["ch2bonus3", "persistent.ch2card3"])

    galitems.append(["ch3bonus1", "persistent.ch3card1"])
    galitems.append(["ch3bonus2", "persistent.ch3card2"])
    galitems.append(["ch3bonus3", "persistent.ch3card3"])

    galitems.append(["ch4bonus1", "persistent.ch4card1"])
    galitems.append(["ch4bonus2", "persistent.ch4card2"])
    galitems.append(["ch4bonus3", "persistent.ch4card3"])

    galitems.append(["ch5bonus1", "persistent.ch5card1"])
    galitems.append(["ch5bonus2", "persistent.ch5card2"])
    galitems.append(["ch5bonus3", "persistent.ch5card3"])

    galitems.append(["ch6bonus1", "persistent.ch6card1"])
    galitems.append(["ch6bonus2", "persistent.ch6card2"])
    galitems.append(["ch6bonus3", "persistent.ch6card3"])

    galitems.append(["ch7bonus1", "persistent.ch7card1"])
    galitems.append(["ch7bonus2", "persistent.ch7card2"])
    galitems.append(["ch7bonus3", "persistent.ch7card3"])

    gal = Gallery()


    for i in galitems:
        gal.button(i[0])
        gal.condition(i[1])
        gal.image(i[0])
        gal.transition = dissolve









screen galleryPDA() tag pda_content:

    zorder 101
    frame at pda_contents:
        on "replaced" action With(Fade(0.2))
        on "replace" action With(Fade(0.2))
        background None

        xysize (600, 620)
        xalign 0.5

        ypos 250

        side "c r":
            area (0, 0, 600, 620)

            viewport id "vp":
                draggable True
                mousewheel True
                has vbox:
                    style_prefix "about"
                label _("Photo Gallery")
                null height 20
                grid 2 11:
                    spacing 10
                    for i in galitems:
                        add gal.make_button(i[0], i[0]+"_btn", locked="cglocked", xpadding=0, ypadding=0)



            vbar value YScrollValue("vp")

screen gallery() tag menu:


    python:







        colcount = 4

        remainder = (2 % 4)


    use game_menu(_("Galería de fotos"), scroll="viewport"):
        style_prefix "about"
        label _("Galería de fotos")

        null height 20


        grid 4 6:
            spacing 30

            for i in galitems:
                add gal.make_button(i[0], i[0]+"_btn", locked="cglocked", xpadding=0, ypadding=0)


            null height 20
            null height 20
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
