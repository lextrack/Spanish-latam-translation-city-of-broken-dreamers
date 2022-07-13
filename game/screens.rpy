










init -1 style default:
    properties gui.text_properties()
    language gui.language

init -1 style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

init -1 style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

init -1 style gui_text:
    properties gui.text_properties("interface")


init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

init -1 style prompt_text is gui_text:
    properties gui.text_properties("prompt")


init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    unscrollable "hide"

init -1 style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    unscrollable "hide"

init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



init -1 style trans is text:
    color "#158eff"
    size 44
    font "fonts/Futura.ttc"

init 499 image trantext = ParameterizedText(style="trans")




















init -501 screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

        text what id "what"




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue:
    italic True
    color "#dddddd"




init -1 style namebox is default
init -1 style namebox_label is say_label

init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

init -1 style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    color gui.text_color













init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default

init -1 style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

init -1 style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










init -501 screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define -1 config.narrator_menu = True


init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    ypos 480
    yanchor 0.5
    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")







init -501 screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Volver") action Rollback()
            textbutton _("Historial") action ShowMenu('history')
            textbutton _("Saltar") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto avance") action Preference("auto-forward", "toggle")
            textbutton _("Guardar") action ShowMenu('save')
            textbutton _("Guardado rápido") action QuickSave()
            textbutton _("Carga rápida") action QuickLoad()
            textbutton _("Preferencias") action ShowMenu('preferences')




init -1 python:
    config.overlay_screens.append("quick_menu")

default -1 quick_menu = True

init -1 style quick_button is default
init -1 style quick_button_text is button_text

init -1 style quick_button:
    properties gui.button_properties("quick_button")

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")











init -501 screen navigation():

    vbox:
        style_prefix "navigation"
        at fade_in
        xpos gui.navigation_xpos
        yalign 0.5


        spacing gui.navigation_spacing

        if _in_replay:

            textbutton _("Finalizar") action EndReplay(confirm=True)

        if main_menu:

            textbutton _("Comenzar") action Start()

        else:

            textbutton _("Guardar") action ShowMenu("save")

        textbutton _("Cargar") action ShowMenu("load")

        textbutton _("Preferencias") action ShowMenu("preferences")







        if not main_menu:

            textbutton _("Menú principal") action MainMenu()

        textbutton _("Galería de escenas") action ShowMenu("replayGallery")

        textbutton _("Galería de fotos") action ShowMenu("gallery")

        textbutton _("Música") action ShowMenu("musicbox")


        textbutton _("Acerca de") action ShowMenu("about")



        if renpy.variant("pc"):


            if renpy.exists("cobd-guide.pdf"):
                textbutton _("Ayuda y guía") action ShowMenu("help")
            else:
                textbutton _("Ayuda") action ShowMenu("help")


            textbutton _("Salir") action Quit(confirm=not main_menu)


init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

init -1 style statframe_frame:
    background "#0008"
init -1 style namestyle:
    size 12
    bold True
    outlines [(2,"#000",0,0)]
init -1 style titlestyle:
    bold True
    size 14
    underline True

init -1 style namestylephone:
    size 20
    bold True
    outlines [(2,"#000",0,0)]
init -1 style titlestylephone:
    bold True
    size 22
    underline True

init -1 style titlescorestyle is titlestyle
init -1 style titleluststyle is titlestyle
init -1 style titlescorestyle:
    color "#6677ff"

init -1 style titleluststyle:
    color "#ff4466"

init -1 style titlescorestylephone is titlestylephone
init -1 style titleluststylephone is titlestylephone
init -1 style titlescorestylephone:
    color "#6677ff"

init -1 style titleluststylephone:
    color "#ff4466"



init -501 screen pat_logo():

    hbox:
        style_prefix "pat_logo"
        xpos gui.navigation_xpos


        if renpy.exists("cobd-guide.pdf"):
            imagebutton auto "common/guide_%s.png" action OpenURL("file:///" + config.basedir + "/game/cobd-guide.pdf")


        null width 20
        imagebutton auto "common/discord_%s.png" action OpenURL("https://discord.gg/TReQu7z")
        yalign 1.0
        yoffset -40





init -501 screen control():
    style_prefix "statbox"
    zorder 100
    frame:
        has vbox:
            xalign 0.02
            yalign 0.02
        if pdastart:
            textbutton "Información" action [If(renpy.get_screen("closearea"), Hide("closearea"), Show("closearea")), If(renpy.get_screen("pda"), Hide("pda"), Show("pda")), If(renpy.get_screen("pda_content"), Hide("contacts"), Show("contacts")), If(renpy.get_screen("glossary"), Hide("glossary")), If(renpy.get_screen("replayGalleryPDA"), Hide("replayGalleryPDA")), If(renpy.get_screen("galleryPDA"), Hide("galleryPDA"))]







init -501 screen pda() tag menu:


    style_prefix "pda"
    zorder 100

    frame at pda_appear:
        xalign 0.5
        padding (40,40)
        background Frame("gui/overlay/pda.png", Borders(25,25,25,25), tile=gui.frame_tile)


        xysize (780, 800)
        has frame:
            background None
            xysize (500, 70)
            xalign 0.5
        hbox:
            textbutton "Contactos" action Show("contacts")
            textbutton "Glosario" action Show("glossary")
            textbutton "Imágenes" action Show("galleryPDA")







transform -1 pda_appear:
    on show:
        alpha 0
        ypos 150
        linear 0.5 alpha 1.0 ypos 100
    on hide:
        linear 0.5 alpha 0.0 ypos 150

init -1 style pda_frame is empty
init -1 style pda_window is empty
init -1 style statbox_frame is empty


transform -1 pda_contents:
    on show:
        alpha 0
        ypos 270
        linear 0.5 alpha 1.0 ypos 220
    on hide:
        linear 0.5 alpha 0.0 ypos 270
    on replace:
        ypos 220
        alpha 0
        pause 0.5
        linear 0.5 alpha 1.0
    on replaced:
        ypos 220
        alpha 1.0
        linear 0.5 alpha 0.0

transform -1 pda_contents_hide:
    on hide:
        alpha 1.0
        ypos 250
        linear 0.5 alpha 0.0 ypos 300
    on replace:
        ypos 250
        alpha 0
        pause 0.5
        linear 0.5 alpha 1.0
    on replaced:
        ypos 250
        alpha 1.0
        linear 0.5 alpha 0.0

init -501 screen closearea():
    zorder 99
    vbox at closearea_appear:
        imagebutton auto "gui/pdabackground_%s.png" action [Hide("closearea"),Hide("pda"),Hide("contacts"), Hide("glossary"), Hide("replayGalleryPDA"), Hide("galleryPDA")]

transform -1 closearea_appear:
    on show:
        alpha 0
        linear 0.5 alpha 0.5
    on hide:
        linear 0.5 alpha 0.0



init -501 screen contacts() tag pda_content:



    zorder 101
    frame at pda_contents:
        on "replaced" action With(Fade(0.2))
        on "replace" action With(Fade(0.2))
        background None

        xysize (680, 620)
        xalign 0.5

        ypos 250

        side "c r":
            area (0, 0, 680, 620)

            viewport id "vp":
                draggable True
                mousewheel True
                has vbox:
                    spacing 10
                null width 270
                if k_met:
                    label "Katie Hamilton {size=-4}{color=#fff}(Puntos a favor: {b}[k_score]{/b} Puntos de lujuria: {b}[k_lust]{/b}){/color}{/size}"
                    hbox:
                        spacing 10
                        add "gui/portraits/katie.jpg"
                        vbox:
                            text k_bio size 18

                else:
                    null height 20

                if e_met:
                    label "Ellen Lane {size=-4}{color=#fff}(Puntos a favor: {b}[e_score]{/b} Puntos de lujuria: {b}[e_lust]{/b}){/color}{/size}"
                    hbox:
                        spacing 10
                        add "gui/portraits/ellen.jpg"
                        vbox:
                            text e_bio size 18
                else:
                    null height 20


                if v_met:
                    label "Victoria Shields {size=-4}{color=#fff}(Puntos a favor: {b}[v_score]{/b} Puntos de lujuria: {b}[v_lust]{/b}){/color}{/size}"
                    hbox:
                        spacing 10
                        add "gui/portraits/victoria.jpg"
                        vbox:
                            text v_bio size 18
                else:
                    null height 20

                if c_met:
                    label "Chandra White {size=-4}{color=#fff}(Puntos a favor: {b}[c_score]{/b} Puntos de lujuria: {b}[c_lust]{/b}){/color}{/size}"
                    hbox:
                        spacing 10
                        add "gui/portraits/chandra.jpg"
                        vbox:
                            text c_bio size 18
                else:
                    null height 20

                if g_met:
                    label "Gloria Conner {size=-4}{color=#fff}(Puntos a favor: {b}[g_score]{/b} Puntos de lujuria: {b}[g_lust]{/b}){/color}{/size}"
                    hbox:
                        spacing 10
                        add "gui/portraits/gloria.jpg"
                        vbox:
                            text g_bio size 18
                else:
                    null height 20



            vbar value YScrollValue("vp")







init -501 screen glossary() tag pda_content:



    zorder 101
    frame at pda_contents_hide:
        on "replaced" action With(Fade(0.2))
        on "replace" action With(Fade(0.2))
        background None
        xysize (680, 620)
        xalign 0.5
        ypos 250

        side "c r":
            area (0, 0, 680, 620)

            viewport id "vp":

                draggable True
                mousewheel True
                has vbox:
                    style_prefix "terms"
                if persistent.glos_augment:
                    vbox:
                        label "Augment"
                        text "El programa Augment fue creado por Baynard durante la Guerra de Asia Oriental. Utilizado para ayudar a potenciar la habilidad de un soldado en la batalla, el programa se adaptó posteriormente para otras habilidades. Al parecer, Baynard puso fin a su uso debido a la alta tasa de mortalidad."
                if persistent.glos_bay:
                    vbox:
                        label "Industrias Baynard"
                        text "Una empresa con sede en Estados Unidos que alcanzó el éxito durante la Guerra de Asia Oriental. Centrada principalmente en la biotecnología y la investigación médica, también ha ayudado al ejército en varios proyectos clasificados."
                if persistent.glos_bolters:
                    vbox:
                        label "Bolters"
                        text "Un grupo de delincuentes e inadaptados que utilizan Lakewood para esconderse de las autoridades. En el último año su número se ha duplicado, lo que les ha permitido dominar la región."
                if persistent.glos_gds:
                    vbox:
                        label "SDG"
                        text "Síndrome de daño genético: Una enfermedad que apareció por primera vez hace 20 años en todo el mundo. Los síntomas se manifiestan cuando el sujeto llega a la adolescencia. El número de nuevos casos registrados ha aumentado año tras año. Hasta ahora no se ha podido determinar su causa ni encontrar ningún tratamiento eficaz. Los individuos afectados suelen desarrollar deformidades físicas. Y, en raras ocasiones, estas mutaciones pueden aportar ventajas, como la mejora de la fuerza, la velocidad y las capacidades cognitivas."
                if persistent.glos_ghost:
                    vbox:
                        label "Fantasmas"
                        text "Mercenarios a sueldo utilizados casi exclusivamente por el mundo empresarial y las élites. Los Fantasmas trabajan en una zona gris, con licencia del Estado y están efectivamente por encima de la ley. Son utilizados para el espionaje corporativo y la adquisición de objetivos. El término Fantasma se utilizó debido a su reputación de no dejar rastro de sus actividades. En los últimos años, el nombre se ha mantenido a pesar de que cada vez más Fantasmas actúan abiertamente y, a menudo, con muchos prejuicios. Los Fantasmas reciben sus contratos a través de un tercero, conocido como contratista."
                if persistent.glos_milcher:
                    vbox:
                        label "Milcher"
                        text "El término comenzó en Alemania, donde el público se resentía de que los enfermos se estuvieran \"aprovechando\" del gobierno. Como la humanidad es muy parecida en todo el mundo, el nombre se impuso rápidamente en cualquier lugar en el que la población con SDG alcanzara un nivel notable."
                if persistent.glos_miltown:
                    vbox:
                        label "Mil-town"
                        text "En muchas ciudades, las personas afectadas por SDG acaban viviendo en un espacio geográfico concentrado. O bien se ven obligados a abandonar otras zonas, o se trasladan para vivir cerca de otros como ellos. Estas zonas, comúnmente llamadas Mil-Town, han desarrollado sus propias culturas, pero a menudo son barrios marginales. El Mil-Town de Los Ángeles se conoce como Lakewood."

                if persistent.glos_nanofluid:
                    vbox:
                        label "Nanofluido"
                        text "Compuesto médico experimental perfeccionado por Industrias Baynard. Se han desarrollado numerosas iteraciones del fluido para mantener su longevidad y eficacia. Sus aplicaciones más exitosas han sido: la regeneración dérmica, la sustitución de nervios y la terapia contra el cáncer."
                if persistent.glos_newyears:
                    vbox:
                        label "Ataques de Año Nuevo"
                        text "El ataque que puso fin al Conflicto de Asia Oriental, en el que armas nucleares de alta potencia destruyeron la mayor parte de Tokio y Osaka. Los ataques se produjeron justo después de la medianoche del 1 de enero de 2030, durante lo que se pensaba que era un armisticio. Según fuentes de la RPC, los misiles fueron enviados en represalia a un primer intento de ataque por parte de Japón. No se ha encontrado ninguna evidencia de que Japón haya lanzado misiles nucleares."

                if persistent.glos_redmoon:
                    vbox:
                        label "Lunas rojas"
                        text "Soldados cibernéticos de élite creados por la Corporación Akatsuki para las Fuerzas de Defensa japonesas. A día de hoy, son el mayor logro derivado de la cibernética."
                if persistent.glos_sculptor:
                    vbox:
                        label "Escultor"
                        text "Su oficio; es modificar los registros del perfil de ADN de un individuo, de modo que difieran de la persona real, o los configuran para que coincidan con otro individuo. El mapeo tiene que estar configurado de manera que los diagnósticos automáticos de la IA no detecten nada que pueda ser marcado como falso o manipulado."
                if persistent.glos_vostok:
                    vbox:
                        label "Vostok"
                        text "Una multinacional rusa que es líder mundial en robótica. Antes de la guerra, eran uno de los pioneros en la industria de la cibertecnología. Durante la guerra, sin embargo, vendieron su tecnología a ambos bandos y posteriormente fueron fuertemente sancionados por ello. A día de hoy, tienen prohibida cualquier investigación en cibertecnología."




            vbar value YScrollValue("vp")


init -1 style terms_vbox:
    spacing 10

init -1 style terms_text:
    size 18








































































































init -501 screen hidden_item(cardimage, pername, xpos, ypos, xsize, ysize):
    imagebutton:
        hover cardimage + "_hover"
        idle cardimage + "_idle"
        xpos xpos
        ypos ypos
        xsize xsize
        ysize ysize
        action [SetField(persistent, pername, True), Hide("hidden_item", dissolve), Show("notify", message = ['Secreto encontrado', 'alert'])]

init -501 screen patreon_link_end():
    imagebutton:
        hover "link_hover"
        idle "link_idle"
        xpos 910
        ypos 508
        xsize 321
        ysize 41
        action OpenURL(website)









init 499 image main_menu = Movie(channel="main_menu", play="gui/menumovie.webm")


init -501 screen main_menu() tag menu:




    style_prefix "main_menu"
    add "main_menu"



    frame




    use navigation
    use pat_logo

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"
            text "[config.version]":
                style "main_menu_version"





init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text

init -1 style main_menu_frame:
    xsize 280
    yfill True



init -1 style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -10

init -1 style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

init -1 style main_menu_title:
    color "#ffffff"
    size 12
    properties gui.text_properties("title")

init -1 style main_menu_version:
    size 12
    color "#ffffff"
    properties gui.text_properties("version")











init -502 screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial 1.0

                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Volver"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar

init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text

init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text

init -1 style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    xsize 340
    yfill True

init -1 style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

init -1 style game_menu_viewport:

    xsize 1400
init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 10

init -1 style game_menu_label:
    xpos 50
    ysize 120

init -1 style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30









init -501 screen about() tag menu:






    use game_menu(_("Acerca de"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define -1 gui.about = ""


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size





init -501 screen replayGalleryPDA() tag pda_content:

    python:
        import math
        replays = []
        replays.append([persistent.ch1chan, "#", "ch1chan", "ch1alley"])
        replays.append([persistent.ch1ellen, "#", "ch1ellen", "ch1ellen"])
        replays.append([persistent.ch1futa, "#", "ch1futa", "ch1homealone"])
        replays.append([persistent.ch1vic, "#", "ch1vic", "ch1dinner2"])

        replays.append([persistent.ch2ellen, "#", "ch1ellen", "ch2partyellen"])
        replays.append([persistent.ch2vic, "#", "ch1vic", "ch2vicstart"])
        replays.append([persistent.ch2shanlon, "#", "ch1shanlon", "ch2shanlonstart"])

        replays.append([persistent.ch3venusprincess, "#", "ch3venusprincess", "ch3venusprincess"])
        replays.append([persistent.ch3venusslut, "#", "ch3venusslut", "ch3venusslut"])
        replays.append([persistent.ch3chandra, "#", "ch3chandra", "ch3chandra"])


        replaylength = len(replays)
        colcount = 2
        rowcount = int(math.ceil((float(replaylength) / colcount)))
        remainder = (replaylength % colcount)



    zorder 101
    frame at pda_contents:
        on "replaced" action With(Fade(0.2))
        on "replace" action With(Fade(0.2))
        background None

        xysize (680, 620)
        xalign 0.5

        ypos 250

        side "c r":
            area (0, 0, 680, 620)

            viewport id "vp":
                draggable True
                mousewheel True
                has vbox:
                    style_prefix "about"


                label _("Scene Gallery")

                null height 20

                grid colcount rowcount:
                    spacing 10

                    for i in replays:
                        if i[0]:
                            imagebutton:
                                idle i[2] + "_idle"
                                hover i[2] + "_hover"
                                action Replay(i[3])
                        else:
                            imagebutton:
                                idle i[2] + "_locked"


                    if remainder == 1:
                        null height 20


            vbar value YScrollValue("vp")











init -501 screen replayGallery() tag menu:

    python:
        import math
        replays = []
        replays.append([persistent.ch1chan, "#", "ch1chan", "ch1alley",[]])
        replays.append([persistent.ch1ellen, "#", "ch1ellen", "ch1ellen",[]])
        replays.append([persistent.ch1futa, "#", "ch1futa", "ch1homealone",[persistent.ch1futa1]])
        replays.append([persistent.ch1vic, "#", "ch1vic", "ch1dinner2",[persistent.ch1vic1]])

        replays.append([persistent.ch2ellen, "#", "ch2ellen", "ch2partyellen",[]])
        replays.append([persistent.ch2vic, "#", "ch2vic", "ch2vicstart",[]])
        replays.append([persistent.ch2shanlon, "#", "ch2shanlon", "ch2shanlonstart",[persistent.ch2shanlon1]])
        replays.append([persistent.ch3venusprincess, "#", "ch3venusprincess", "ch3venusprincess",[]])

        replays.append([persistent.ch3venusslut, "#", "ch3venusslut", "ch3venusslut",[]])
        replays.append([persistent.ch3chandra, "#", "ch3chandra", "ch3chandra",[persistent.ch3chandra1,persistent.ch3chandra2,persistent.ch3chandra3,persistent.ch3chandra4]])
        replays.append([persistent.ch4doc, "#", "ch4doc", "ch4wakeupcont",[persistent.ch4doc1]])
        replays.append([persistent.ch4vicdep, "#", "ch4vicdep", "ch4vicdep",[]])

        replays.append([persistent.ch4vic, "#", "ch4vic", "ch4vickiss", [persistent.ch4vic1]])
        replays.append([persistent.ch5chandrasex, "#", "ch5chandra", "ch5chandra",[]])
        replays.append([persistent.ch5ellensex, "#", "ch5ellen", "ch5ellensex",[persistent.ch5ellen1]])

        replays.append([persistent.ch6venussex, "#", "ch6venussex", "ch6venusslutscene",[]])
        replays.append([persistent.ch6vicsex, "#", "ch6vicsex", "ch6venusvictoria",[]])
        replays.append([persistent.ch6carlisex, "#", "ch6carli", "ch6carli",[]])
        replays.append([persistent.ch6katiesex, "#", "ch6katiesex", "ch6docstart",[persistent.ch6katiesex1,persistent.ch6katiesex2,persistent.ch6katiesex3,persistent.ch6katiesex4]])

        replays.append([persistent.ch7katiesex, "#", "ch7katiesex", "ch7katiestart",[]])
        replays.append([persistent.ch7vicdep, "#", "ch7vicdep", "ch7meredithsex",[]])
        replays.append([persistent.ch7vicsex, "#", "ch7vicsex", "ch7vicsex",[persistent.ch7vicsex1,persistent.ch7vicsex2]])
        replays.append([persistent.ch7ellensex, "#", "ch7ellensex", "ch7stairwayellenexplore",[persistent.ch7ellenanal]])


        replaylength = len(replays)
        colcount = 4
        rowcount = int(math.ceil((float(replaylength) / colcount)))
        remainder = (replaylength % colcount)




    use game_menu(_("Galería de escenas"), scroll="viewport"):

        style_prefix "about"


        label _("Galería de escenas")
        text _("Selecciona las escenas desbloqueadas a continuación. La repetición utilizará el apellido y los nombres de las personas que hayas conocido. Las escenas que tienen varias casillas indican que hay extras en la escena que se pueden desbloquear.")

        null height 20

        grid colcount rowcount:
            spacing 30

            for i in replays:
                if i[0]:
                    vbox:
                        imagebutton:
                            idle i[2] + "_idle"
                            hover i[2] + "_hover"
                            action Replay(i[3])
                        if len(i[4]) > 0:
                            hbox:
                                add "gui/check.png"
                                for n in i[4]:
                                    if n == True:
                                        add "gui/check.png"
                                    else:
                                        add "gui/uncheck.png"

                        else:
                            hbox:
                                add "gui/check.png"


                else:
                    vbox:
                        imagebutton:
                            idle i[2] + "_locked"


            if remainder == 3:
                null height 20
            if remainder == 2:
                null height 20
                null height 20

            if remainder == 1:
                null height 20
                null height 20
                null height 20














init -502 screen save() tag menu:
    $ globals() ["currentScreenName"] = "save"



    use file_slots(_("Save"))


init -502 screen load() tag menu:
    $ globals() ["currentScreenName"] = "load"



    use file_slots(_("Load"))



init -502 screen modal_input:
    zorder 200
    modal True
    style_prefix "modal_input"
    frame:
        align (0.5, 0.5)
        xysize (600, 250)

        has vbox:
            xalign 0.5
            yoffset -7

        text prompt style "input_prompt" xalign 0.5
        if not renpy.variant("pc"):
            hbox:
                xsize 400
                vbox:
                    xalign 0.0
                    input id "input" style "input_text" length 29
                vbox:
                    xalign 1.0
                    textbutton ">>Enter<<" action Function(renpy.end_interaction,renpy.get_widget("modal_input", "input"))
        else:
            input id "input" style "input_text" length 29 xalign 0.5 yoffset 25

init -2 style modal_input_prompt is default

init -2 style modal_input_prompt:
    xalign gui.dialogue_text_xalign
    yalign 0.5
    properties gui.text_properties("input_prompt")

init -2 style modal_input:
    xalign gui.dialogue_text_xalign
    yalign 0.5
    xmaximum 400

init -2 style modal_input_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding


init -4 python:
    class get_save_name(FileSave):
        def __init__(self, name, confirm=True, newest=True, page=None, cycle=False):
            super(get_save_name,self).__init__(name=name,confirm=confirm,newest=newest,page=page,cycle=cycle)
        def __call__(self):
            renpy.call_in_new_context("get_save_name")
            return super(get_save_name,self).__call__()

label get_save_name():


    if not renpy.variant("pc"):
        $ save_name_tmp = renpy.call_screen("modal_input", prompt= _("Introduce un nombre para la partida:"), default = "", length=29)
        $ save_name = save_name_tmp.content if isinstance(save_name_tmp, Text) else save_name_tmp
    else:
        $ save_name = renpy.call_screen("modal_input", prompt= _("Introduce un nombre para la partida:"), default = "", length=29)
    $ renpy.retain_after_load()
    return


default -2 persistent.pages = 1






init -501 screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Guardo automatico"), quick=_("Guardado rapido"))

    use game_menu(title):

        fixed:



            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:


                        if title == "Save" and persistent.saveNaming == True:
                            action [SetVariable("save_name",""), get_save_name(slot)]
                        else:
                            action FileAction(slot)

                        add FileScreenshot(slot) xalign 0.5
                        key "save_delete" action FileDelete(slot)
                        vbox:
                            xalign 0.5
                            yalign 1.0


                            text FileSaveName(slot):
                                style "slot_name_text"
                                size 17


                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("guardado vacío")):
                                style "slot_time_text"


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


init -502 screen file_slots2(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:



            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:



                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style page_label:
    xpadding 50
    ypadding 3

init -1 style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color


init -1 style page_button:




    left_padding 30
    right_padding 30


init -1 style page_button_text:
    properties gui.button_text_properties("page_button")

init -1 style slot_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")









init -501 screen preferences() tag menu:



    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Preferencias"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Pantalla")
                        textbutton _("Ventana") action Preference("display", "window")
                        textbutton _("Pantalla completa") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Desactivado") action Preference("rollback side", "disable")
                    textbutton _("Izquierda") action Preference("rollback side", "left")
                    textbutton _("A la derecha") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Saltar")
                    textbutton _("Texto no visto") action Preference("skip", "toggle")
                    textbutton _("Después de elegir") action Preference("after choices", "toggle")
                    textbutton _("Transiciones") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    style_prefix "radio"
                    label _("Color de los diálogos")

                    textbutton _("Blanco") action gui.SetPreference("diacolor", "#ffffff")
                    textbutton _("Azul") action gui.SetPreference("diacolor", "#a3e0ff")
                    textbutton _("Dorado") action gui.SetPreference("diacolor", "#fdf6be")
                    textbutton _("Verde") action gui.SetPreference("diacolor", "#befdc9")

                vbox:
                    style_prefix "check"
                    label _("Guardados personalizados")
                    if persistent.saveNaming:
                        textbutton _("Activado"):
                            action SetField(persistent, "saveNaming", False)
                            text_color "#fff"
                    elif not persistent.saveNaming or persistent.saveNaming == None:
                        textbutton _("Desactivado"):
                            action SetField(persistent, "saveNaming", True)








            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Velocidad del texto")

                    bar value Preference("text speed")

                    label _("Tiempo de auto-avance")

                    bar value Preference("auto-forward time")






                vbox:

                    if config.has_music:
                        label _("Volumen de la música")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Volumen de efectos")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Probar") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Volumen de la voz")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Probar") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Silenciar todo"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox

init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

init -1 style pref_label_text:
    yalign 1.0

init -1 style pref_vbox:
    xsize 285

init -1 style radio_vbox:
    xsize 265
    spacing gui.pref_button_spacing

init -1 style radio_button:
    properties gui.button_properties("radio_button")



init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")


init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")



init -1 style check_button_text:
    properties gui.button_text_properties("check_button")

init -1 style slider_slider:
    xsize 350

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")

init -1 style slider_vbox:
    xsize 450










init -501 screen history() tag menu:




    predict False

    use game_menu(_("Historial"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("El historial de diálogos está vacío.")


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5








init -501 screen help() tag menu:



    default device = "keyboard"

    use game_menu(_("Ayuda"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:


                textbutton _("Teclado") action SetScreenVariable("device", "keyboard")
                textbutton _("Ratón") action SetScreenVariable("device", "mouse")


                if renpy.exists("cobd-guide.pdf"):
                    textbutton _("Official Guide") action OpenURL("file:///" + config.basedir + "/game/cobd-guide.pdf")


                if GamepadExists():
                    textbutton _("Mando") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


init -501 screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Espacio")
        text _("Avanza el diálogo sin seleccionar opciones.")

    hbox:
        label _("Teclas direccionales")
        text _("Navega por la interfaz.")

    hbox:
        label _("Esc")
        text _("Accede al menú del juego.")

    hbox:
        label _("Ctrl")
        text _("Se salta el diálogo mientras se mantiene pulsado.")

    hbox:
        label _("Tab")
        text _("Activa la omisión de diálogos.")

    hbox:
        label _("Page Up")
        text _("Vuelve al diálogo anterior.")

    hbox:
        label _("Page Down")
        text _("Avanza al diálogo posterior.")

    hbox:
        label "H"
        text _("Oculta la interfaz de usuario.")

    hbox:
        label "S"
        text _("Toma una captura de pantalla.")

    hbox:
        label "V"
        text _("Activa las voces con {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


init -501 screen mouse_help():

    hbox:
        label _("Clic izquierdo")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Boton central del ratón")
        text _("Oculta la interfaz de usuario.")

    hbox:
        label _("Clic derecho")
        text _("Accede al menú del juego.")

    hbox:
        label _("Rueda del ratón hacia arriba")
        text _("Vuelve al diálogo anterior.")

    hbox:
        label _("Rueda del ratón hacia abajo")
        text _("Avanza al diálogo posterior.")


init -501 screen gamepad_help():

    hbox:
        label _("LT")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("LB")
        text _("Vuelve al diálogo anterior.")

    hbox:
        label _("RB")
        text _("Avanza al diálogo posterior.")

    hbox:
        label _("Cruceta")
        text _("Navega por la interfaz.")

    hbox:
        label _("Start")
        text _("Accede al menú del juego.")

    hbox:
        label _("Y")
        text _("Oculta la interfaz de usuario.")

    textbutton _("Calibrar") action GamepadCalibrate()


init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text

init -1 style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

init -1 style help_button_text:
    properties gui.button_text_properties("help_button")

init -1 style help_label:
    xsize 250
    right_padding 20

init -1 style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















init -501 screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Sí") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action


init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")

init -1 style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:
        has hbox:
            spacing 6

        text _("Adelantando")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    xalign 0.5
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)


    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:


    font "DejaVuSans.ttf"









init -501 screen notify(message):
    zorder 100
    if isinstance(message, list):
        style_prefix message[1]
        frame at notify_appear:
            text message[0]
        timer 5.25 action Hide('notify')
    else:
        style_prefix "notify"

        frame at notify_appear:
            text message
        timer 3.25 action Hide('notify')



transform -1 notify_appear:
    on show:
        alpha 0
        xalign -0.2
        linear 1.0 alpha 1.0 xalign 0.0
    on hide:

        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    properties gui.text_properties("notify")




transform -1 alert_appear:
    on show:
        alpha 0
        xpos -60
        linear .5 xpos 0 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style alert_frame is empty
init -1 style alert_text is gui_text

init -1 style alert_frame:
    ypos 500

    background Frame("gui/alert.png", Borders(1,20,20,20), tile=gui.frame_tile)
    padding (40, 21, 30, 21)

init -1 style alert_text:
    properties gui.text_properties("alert")



transform -1 unlock_appear:
    on show:
        alpha 0
        xpos -60
        linear .5 ypos 0 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style unlock_frame is empty
init -1 style unlock_text is gui_text

init -1 style unlock_frame:
    ypos 820

    background Frame("gui/unlock.png", Borders(1,20,20,20), tile=gui.frame_tile)
    padding (40, 21, 30, 21)

init -1 style unlock_text:
    properties gui.text_properties("alert")



transform -1 glossary_appear:
    on show:
        alpha 0
        xpos -60
        linear .5 ypos 0 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style glossary_frame is empty
init -1 style glossary_text is gui_text

init -1 style glossary_frame:
    ypos 880

    background Frame("gui/glossary.png", Borders(1,20,20,20), tile=gui.frame_tile)
    padding (40, 21, 30, 21)

init -1 style glossary_text:
    properties gui.text_properties("alert")











init -501 screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


init -501 screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define -1 config.nvl_list_length = 6

init -1 style nvl_window is default
init -1 style nvl_entry is default

init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue

init -1 style nvl_button is button
init -1 style nvl_button_text is button_text

init -1 style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

init -1 style nvl_entry:
    xfill True
    ysize gui.nvl_height

init -1 style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

init -1 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init -1 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







init -1 style pref_vbox:
    variant "medium"
    xsize 450



init -501 screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


init -1 style window:
    variant "small"
    background "gui/phone/textbox.png"

init -1 style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

init -1 style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

init -1 style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    variant "small"
    xsize 340

init -1 style game_menu_content_frame:
    variant "small"
    top_margin 0

init -1 style pref_vbox:
    variant "small"
    xsize 400

init -1 style slider_pref_vbox:
    variant "small"
    xsize None

init -1 style slider_pref_slider:
    variant "small"
    xsize 600
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
