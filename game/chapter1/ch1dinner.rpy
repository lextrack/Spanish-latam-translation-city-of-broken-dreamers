image bg ch1dinner1 = "ch1dinner1"
image bg ch1dinner2 = "ch1dinner2"
image bg ch1dinner3 = "ch1dinner3"
image bg ch1dinner4 = "ch1dinner4"
image bg ch1dinner5 = "ch1dinner5"
image bg ch1dinner6 = "ch1dinner6"
image bg ch1dinner7 = "ch1dinner7"
image bg ch1dinner8 = "ch1dinner8"
image bg ch1dinner9 = "ch1dinner9"
image bg ch1dinner10 = "ch1dinner10"
image bg ch1dinner11 = "ch1dinner11"
image bg ch1dinner12 = "ch1dinner12"
image bg ch1dinner13 = "ch1dinner13"
image bg ch1dinner14 = "ch1dinner14"
image bg ch1dinner15 = "ch1dinner15"
image bg ch1dinner16 = "ch1dinner16"
image bg ch1dinner17 = "ch1dinner17"
image bg ch1dinner18 = "ch1dinner18"
image bg ch1dinner19 = "ch1dinner19"
image bg ch1dinner20 = "ch1dinner20"
image bg ch1dinner21 = "ch1dinner21"
image bg ch1dinner22 = "ch1dinner22"
image bg ch1dinner23 = "ch1dinner23"
image bg ch1dinner24 = "ch1dinner24"
image bg ch1dinner25 = "ch1dinner25"
image bg ch1dinner26 = "ch1dinner26"
image bg ch1dinner27 = "ch1dinner27"
image bg ch1dinner28 = "ch1dinner28"
image bg ch1dinner29 = "ch1dinner29"

image bg ch1dinner31 = "ch1dinner31"
image bg ch1dinner32 = "ch1dinner32"
image bg ch1dinner33 = "ch1dinner33"
image bg ch1dinner34 = "ch1dinner34"
image bg ch1dinner35 = "ch1dinner35"
image bg ch1dinner36 = "ch1dinner36"
image bg ch1dinner37 = "ch1dinner37"
image bg ch1dinner38 = "ch1dinner38"
image bg ch1dinner39 = "ch1dinner39"
image bg ch1dinner40 = "ch1dinner40"
image bg ch1dinner41 = "ch1dinner41"
image bg ch1dinner42 = "ch1dinner42"
image bg ch1dinner43 = "ch1dinner43"
image bg ch1dinner44 = "ch1dinner44"
image bg ch1dinner45 = "ch1dinner45"
image bg ch1dinner46 = "ch1dinner46"
image bg ch1dinner47 = "ch1dinner47"
image bg ch1dinner48 = "ch1dinner48"
image bg ch1dinner49 = "ch1dinner49"
image bg ch1dinner50 = "ch1dinner50"
image bg ch1dinner51 = "ch1dinner51"
image bg ch1dinner52 = "ch1dinner52"
image bg ch1dinner53 = "ch1dinner53"
image bg ch1dinner54 = "ch1dinner54"
image bg ch1dinner55 = "ch1dinner55"
image bg ch1dinner56 = "ch1dinner56"
image bg ch1dinner57 = "ch1dinner57"
image bg ch1dinner58 = "ch1dinner58"
image bg ch1dinner59 = "ch1dinner59"
image bg ch1dinner60 = "ch1dinner60"
image bg ch1dinner61 = "ch1dinner61"
image bg ch1dinner62 = "ch1dinner62"
image bg ch1dinner63 = "ch1dinner63"
image bg ch1dinner64 = "ch1dinner64"
image bg ch1dinner65 = "ch1dinner65"
image bg ch1dinner66 = "ch1dinner66"
image bg ch1dinner67 = "ch1dinner67"
image bg ch1dinner68 = "ch1dinner68"
image bg ch1dinner69 = "ch1dinner69"
image bg ch1dinner70 = "ch1dinner70"
image bg ch1dinner71 = "ch1dinner71"
image bg ch1dinner72 = "ch1dinner72"
image bg ch1dinner73 = "ch1dinner73"
image bg ch1dinner74 = "ch1dinner74"
image bg ch1dinner75 = "ch1dinner75"
image bg ch1dinner76 = "ch1dinner76"
image bg ch1dinner77 = "ch1dinner77"
image bg ch1dinner78 = "ch1dinner78"
image bg ch1dinner79 = "ch1dinner79"
image bg ch1dinner80 = "ch1dinner80"
image bg ch1dinner81 = "ch1dinner81"
image bg ch1dinner82 = "ch1dinner82"
image bg ch1dinner83 = "ch1dinner83"

image bg ch1dinner30:
    "ch1dinner30"
    xalign 0.0
    yalign 0.5
    zoom 0.7 subpixel True
    ease 8 zoom 0.5 xalign 0.0

image ch1dinnerpan = Movie(play='video/chapter-1-video/ch1dinnerpan.webm', loop=False)
image bg ch1dinnerpanmovie movie:
    "ch1dinnerpan"
    pause 7.0
    "ch1dinnerpan-end"

image bg ch1vicride movie = Movie(play="video/chapter-1-video/ch1vicride.webm")
image bg ch1vicblow1 movie = Movie(play="video/chapter-1-video/ch1vicblow1.webm")
image bg ch1vicblow2 movie = Movie(play="video/chapter-1-video/ch1vicblowhard.webm")

image bg ch1victhumb movie = Movie(play="video/chapter-1-video/ch1victhumb.webm")
image bg ch1victits movie = Movie(play="video/chapter-1-video/ch1victits.webm")

image bg ch1vicbehind movie = Movie(play="video/chapter-1-video/ch1vicbehind.webm")
image bg ch1vicbehind2 movie = Movie(play="video/chapter-1-video/ch1vicbehind2.webm")

image bg ch1vicdoggy1 movie = Movie(play="video/chapter-1-video/ch1vicdoggy1.webm")
image bg ch1vicdoggy2 movie = Movie(play="video/chapter-1-video/ch1vicdoggy2.webm")
image bg ch1vicdoggy3 movie = Movie(play="video/chapter-1-video/ch1vicdoggy3.webm")


label ch1dinner:

    scene black with fade
    play music audio.sax fadein 2.0 fadeout 2.0
    show text "{=trans}YA DE NOCHE, EN EL SKY LOUNGE{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    show bg ch1dinner7 with dissolve
    if not persistent.ch1card2:
        $ renpy.notify(['Posible pista', 'alert'])
        show screen hidden_item("ch1card2", "ch1card2", 884, 537, 48, 98)
    pt "(??D??nde est?? todo el mundo?)"
    pt "(Normalmente este lugar est?? lleno.)"
    hide screen hidden_item
    show bg ch1dinner8 with dissolve
    v "Hola, agente.{w} Le estaba esperando."
    p "??Hubo un esc??ndalo de intoxicaci??n alimentaria que me perd??? Por lo general, los z??nganos de las corporaciones siempre est??n aqu??."
    show bg ch1dinner1 with dissolve
    v "Bueno, por tu perfil supuse que preferir??as un lugar m??s privado mientras terminamos nuestra discusi??n.{w} ??No es apropiado?"
    p "Est?? bien. Es que...{w} ??La empresa pag?? por esto?"
    show bg ch1dinner2 with dissolve
    v "Ciertamente no fui yo. Mi trabajo est?? bien pagado, pero no tanto."
    p "Estoy seguro de que les dijiste algo."
    show bg ch1dinner6 with dissolve
    v "Bueno, me encanta el salm??n a la parrilla aqu??. Pero si me permites un secreto, soy como t??. Disfruto de la privacidad. Como \"z??ngano de la corporaci??n\" encuentro a mis compa??eros bastante... ins??pidos."
    show bg ch1dinner3 with dissolve
    v "Por no mencionar que nos permite discutir las cosas mucho m??s... abiertamente. Sin o??dos indiscretos ni ojos vigilantes."
    p "Muy inteligente."
    v "Siempre.{w} Ahora, ??hablamos de negocios?"
    menu:
        "P??dele mucho":
            $ extraevents.append("ch1money")
            p "Mi paga, estoy buscando mucho m??s de lo habitual para esto."
            v "Por supuesto."
            p "Siempre est?? el peligro. Es as?? la cosa, pero esto es diferente."
            v "Entendido, me han autorizado a compensarle por ello."
            v "Podemos pagarle cinco veces su tarifa est??ndar."
            p "Tambi??n odio a tu jefa, as?? que hay un recargo por eso."
            p "As?? que, ??qu?? tal diez?"
            v "Ocho."
            show bg ch1dinner10 with dissolve
            v "??Le parece bien?"
            p "Tal vez..."
            show bg ch1dinner9 with dissolve
            v "Y puedo a??adir algunos beneficios {i}extra.{/i}"
            show bg ch1dinner5 with dissolve
            v "??Ser??a m??s atractivo?"
            menu:
                "Ocho es suficiente, mantengamos esto profesional.":
                    $ v_score += 1
                    $ extraevents.append("ch1turndown")
                    p "No hay necesidad de los extras. Encontrar?? a esta chica."
                    show bg ch1dinner4 with dissolve
                    v "??Eh? Yo... s??, por supuesto. Me alegro de trabajar con usted, agente."
                    p "Bien."
                    $ achievement.grant("UNEXPECTED")
                    init:
                        $ achievement.register("UNEXPECTED")
                    $ achievement.Sync()
                    v "As?? es, agente,{w} hemos terminado aqu??."
                    p "Bueno, te avisar?? cuando encuentre m??s informaci??n."
                    v "Perfecto."
                    jump ch1dinnerend
                "??C??mo podr??a resistirme?":
                    p "Una oferta muy tentadora. ??C??mo puedo resistirme?"
                    show bg ch1dinner11 with dissolve
                    v "No se puede. {w} D??jeme mostrarle c??mo es trabajar conmigo."
                    jump ch1dinner2
        "Pide una cantidad razonable":


            p "P??game cinco veces mi tarifa habitual y estaremos bien."
            v "Muy bien. Entonces est?? acordado. Usted encuentra a la chica y nosotros le pagamos cinco veces el precio habitual."
            p "Hecho.{w} ??Eso es todo?"
            show bg ch1dinner4 with dissolve
            v "As?? es, agente,{w} hemos terminado aqu??."
            p "Te avisar?? cuando encuentre m??s informaci??n."
            v "Perfecto."
            jump ch1dinnerend

        "A la mierda los negocios" if dep >= 2 or "ch1spellbound" in extraevents:
            $ v_lust += 1
            p "Aceptar?? el trabajo con una condici??n."
            v "Contin??e."
            p "Que lleguemos a trabajar muy estrechamente."
            show bg ch1dinner9 with dissolve
            v "Mmm, ??qu?? tan cerca?"
            p "Cerca."
            show bg ch1dinner11 with dissolve
            v "Bien, d??jeme mostrarle c??mo es trabajar conmigo."
            jump ch1dinner2


label ch1dinner2:
    if _in_replay:
        $ setReplay()
        if persistent.ch1vic1 == True:
            $ dep = 2
        play music audio.sax fadein 2.0 fadeout 2.0
    $ extraevents.append("ch1vic")
    show bg ch1dinner12 with dissolve
    v "S??game, agente."
    p "Con gusto."
    show bg ch1dinner15 with dissolve
    v "Le mostrar?? cosas maravillosas."
    show bg ch1dinner14 with dissolve
    v "S?? que le gustar??."
    v "Ahora, ay??deme a quitarme este vestido."
    show bg ch1dinner16 with dissolve
    v "No tan r??pido. No se ponga ansioso."
    v "Mmm, deje que le ense??e m??s."
    show bg ch1dinner17 with dissolve
    v "??Le gusta mi suave piel?"
    p "S??..."
    show bg ch1dinner15 with dissolve
    v "??Mis labios?"
    p "S??..."
    v "Muy bien."
    v "Ahora, agente, cierre los ojos."
    scene black with dissolve
    p "??Cu??ndo puedo abrirlos?"
    v "Ahora puede echar un vistazo."
    show bg ch1dinnerpanmovie movie with dissolve
    v "Ohh, se siente bien la brisa en mi piel."
    p "..."
    v "Emp??pese, agente."
    p "Ufff..."
    v "??Le apetece nadar?"
    p "Me apetecen otras cosas."
    show bg ch1dinner19 with dissolve
    v "Muy bien."
    show bg ch1dinner20 with dissolve
    $ renpy.pause(1)
    show bg ch1dinner21 with dissolve
    v "No no no."
    show bg ch1dinner22 with dissolve
    v "Todav??a no.{w} Pronto tendr?? su diversi??n."
    show bg ch1dinner23 with dissolve
    v "Yo, por mi parte, quiero sentir esta agua sobre mi piel."
    show bg ch1dinner24 with dissolve
    v "Observe si lo desea."
    show bg ch1dinner25 with dissolve
    v "Ahh, el agua se siente divina."

    show bg ch1dinner26 with dissolve
    v "No sabe lo que se pierde, agente."
    show bg ch1dinner27 with dissolve
    v "??Seguro no quiere venir?"
    p "Creo que deber??as venir."
    show bg ch1dinner28 with dissolve
    v "??As???"
    show bg ch1dinner29 with dissolve
    p "S??."
    v "Aqu?? estoy."
    p "Ahora sal de la piscina."
    v "Todav??a no. Encu??ntrame en la parte menos profunda, agente."
    show bg ch1dinner30 with dissolve
    v "Muy bien.{w} Nuestro tiempo juntos ser?? inolvidable."
    v "Apres??rese."
    show bg ch1dinner33 with dissolve
    v "Qu??tese la ropa."
    show bg ch1dinner32 with dissolve
    v "No puedo esperar a sentir sus manos por todo mi cuerpo."
    show bg ch1dinner31 with dissolve
    v "Perfecto. Ahora, ac??rquese."
    v "Por lo que s??, no le gusta que me refiera a usted como \"Agente.\""
    p "No especialmente."
    v "??Prefiere que le llame de otra manera, quiz??s solo, [p]?"
    menu:
        "[p], est?? bien":
            p "[p], est?? bien."
            $ vicsexname = p
            v "Muy bien, [vicsexname]."
        "Ll??mame...":
            python:
                vicsexname = renpy.input("??C??mo quieres que te llame?")
                vicsexname = vicsexname.strip()
                persistent.vicsexname = vicsexname
                if not vicsexname:
                    vicsexname = p
            if vicsexname == "Agent" or vicsexname == "agent":
                v "Ja, muy gracioso."
                v "As?? que tal vez me equivoqu?? contigo. [vicsexname], ser?? entonces."
            else:
                v "[vicsexname] ser?? entonces."
            $ persistent.vicsexname = vicsexname

    show bg ch1dinner34 with dissolve
    v "Mmm, [vicsexname], quiero mostrarte esto."
    show bg ch1dinner35 with dissolve
    v "Te aseguro que son magn??ficos. Suaves, pero firmes. Quiero que los aprietes. Que los lamas. {w}Dales duro."
    v "Ahora d??jame ver el hombre que eres."
    show bg ch1dinner36 with dissolve
    p "D??jame ver esas tetas."
    show bg ch1dinner37 with dissolve
    v "S??... ??y mi mano te gusta?"
    p "S??, pero quiero m??s."
    v "Por supuesto. ??Para qu?? est??n los socios comerciales?"
    show bg ch1dinner38 with dissolve
    v "Mira lo que hago con mis tetas... Mmm.{w} Puedo sentir tu pulso contra mi piel."
    show bg ch1victits movie with dissolve
    p "Uf... se siente muy bien."
    v "??Te sientes bien entre mis suaves y h??medos pechos?"
    v "Oh, [vicsexname], se te est?? poniendo muy dura."
    show bg ch1dinner39 with dissolve
    p "*Gru??e de placer* Dios, eres incre??ble."
    v "S??, lo soy.{w} Y ni siquiera hemos empezado."
    v "Incl??nate hacia atr??s."
    show bg ch1dinner40 with dissolve
    v "Mmm, [vicsexname], agarra esas tetas y aprietalas."
    show bg ch1dinner41 with dissolve
    v "S??... {w} Ya puedo sentirte."
    show bg ch1dinner42 with dissolve
    v "Mmm... imagina lo que estos labios pueden hacer por ti."
    show bg ch1victhumb movie with dissolve
    v "*Lo chupa suavemente*"
    p "Incre??ble. Vas a dar muchos problemas, ??no?"
    show bg ch1dinner43 with dissolve
    v "??Solo si quieres que as?? sea?"
    p "Oh, quiero que lo sea."
    show bg ch1dinner44 with dissolve
    v "Entonces, ??debo quitarme todo?"
    p "D??jame ver todo."
    show bg ch1dinner45 with dissolve
    v "Qu??talos."
    show bg ch1dinner46 with dissolve
    v "R??pido."
    show bg ch1dinner47 with dissolve
    v "Mmm, ch??pame las tetas."
    show bg ch1dinner48 with dissolve
    v "Ahora, m??rame."
    show bg ch1dinner49 with dissolve
    v "Quiero complacerte. Dime c??mo."
    $ resetmenu()
    jump ch1dinnermenu

label ch1dinnermenu:
    menu:
        "S??bete encima de mi":
            jump ch1dinnerride
        "Por detr??s":
            jump ch1dinnerbehind
        "De perrito":
            jump ch1dinnerdoggy
        "Mamada":
            jump ch1dinnerblow

label ch1dinnerride:
    p "Si??ntate encima y m??ntame; m??ntame como si no hubiera un ma??ana."
    show bg ch1dinner50 with dissolve
    v "S??, [vicsexname]."
    show bg ch1dinner51 with dissolve
    v "*Jadeos* Si..."
    show bg ch1dinner53 with dissolve
    v "??OH! {w}*respira con fuerza*"
    p "??Ahora, mu??strame de qu?? est??s hecha!"
    v "S??, [vicsexname]."
    show bg ch1vicride movie with dissolve
    v "S??, [vicsexname]!{w} ??Deja que te coja!"
    p "??All?? vamos!{w} ??M??s fuerte!"
    v "Deja que las tetas reboten en tu cara."
    v "??Oh, Dios, podr??a montarte toda la noche!"
    p "Me parecer??a bien."
    v "Vas a hacer que me corra, [vicsexname]."
    v "Siente c??mo me aprieto m??s..."
    p "Maldita sea, est??s a punto."
    show bg ch1dinner52 with vpunch
    v "????OH!! ??Ah?? vamos!"
    p "Dale con todo.{w} ??Eres hipnotizante!"
    jump ch1dinnermenu

label ch1dinnerbehind:
    show bg ch1dinner57 with dissolve
    v "Ven aqu?? y t??mame por detr??s. Quiero que me agarres los pechos mientras lo haces."
    show bg ch1dinner54 with dissolve
    v "S??... {w} No es necesario ser gentil."
    show bg ch1vicbehind2 movie with dissolve
    p "Ahh, guau."
    v "Mmmm, [vicsexname], sigue."
    show bg ch1dinner54 with dissolve
    v "Golp??ame las tetas.{w} Mu??strame el hombre que eres."
    show bg ch1vicbehind movie with dissolve
    v "??Ah! ??S??!"
    v "Sabes c??mo tratar a una mujer."
    show bg ch1dinner56 with dissolve
    p "Este trabajo se perfila como muy bueno."
    v "As?? es, [vicsexname]."
    show bg ch1dinner55 with dissolve
    v "*Deja salir una profunda exhalaci??n de aire*{w} Ahhhh..."
    jump ch1dinnermenu





label ch1dinnerdoggy:
    p "Ahora ag??chate."
    show bg ch1dinner58 with dissolve
    v "Como quieras, [vicsexname]..."
    show bg ch1dinner59 with dissolve
    p "Oh, esto va a ser bueno."
    show bg ch1dinner61 with dissolve
    v "??Ah! Ahora follame."
    show bg ch1vicdoggy1 movie with dissolve
    p "??Oh, eres un problema!"
    v "??AH! [vicsexname], ??siempre!"
    show bg ch1vicdoggy2 movie with dissolve
    v "Soy tu chica problem??tica."
    p "Puedo acostumbrarme a eso."
    v "Sigue."
    show bg ch1vicdoggy3 movie with dissolve
    v "Puedo sentir que est??s cerca. ??Te vas a correr?"
    v "Me encantar??a sentir tu hombr??a rociada por toda mi espalda."
    menu:
        "A??n no":
            p "Todav??a no he terminado."
            show bg ch1vicdoggy2 movie with dissolve
            v "??Ahhh, qu?? bien!"
            p "Podr??a cogerte toda la noche."
            v "Ser??a una haza??a.{w} Seguro que despu??s te escuecen los m??sculos."
            show bg ch1dinner62 with dissolve
            v "??Quieres que haga algo m??s?"
            jump ch1dinnermenu
        "S??":
            p "Mierda, me voy a correr."
            v "Bien. ??C??geme, [vicsexname], hasta que explotes!"
            show bg ch1vicdoggy2 movie with dissolve
            v "??Ah, s??!"
            p "??Aqu?? viene!"

            show bg ch1dinner67 with dissolve
            p "??Oh, carajo!"
            show bg ch1dinner68 with quickflash
            p "??AHHH!"
            show bg ch1dinner69 with dissolve
            p "*Voz temblorosa* Ohhh. ??Guau!"
            show bg ch1dinner70 with dissolve
            v "Buen trabajo, [vicsexname]."
            v "Me alegro de que podamos trabajar juntos."
            p "Igualmente."
            show bg ch1dinner73 with dissolve
            v "Ahora, ??nos vestimos? Creo que nuestra reservaci??n aqu?? terminar?? pronto."
            p "Por supuesto."
            $ renpy.end_replay()
            if not persistent.ch1vic:
                $ renpy.notify(['Escena desbloqueada', 'unlock'])
                $ persistent.ch1vic = True
            jump ch1dinnerend

label ch1dinnerblow:
    p "Creo que has hablado mucho en el ??ltimo tiempo."
    v "??Te gustar??a que mi boca hiciera otra cosa?"

    show bg ch1dinner76 with dissolve
    v "??Quiz?? pueda hacer esto?"
    p "Deja de hablar."
    show bg ch1vicblow1 movie with dissolve
    v "*Ruidos de arcadas*"
    p "??Uf! Eres buena."
    v "??Mmmm!"
    show bg ch1dinner77 with dissolve
    p "Oh, no te atrevas a parar."

    p "Dios, s??."
    v "*Contin??a deslizando tu pene en su boca con ligeros ruidos de succi??n*"
    show bg ch1dinner78 with dissolve
    p "??Maldita sea, vas a hacer que me corra!"
    menu:
        "Aguanta":
            pt "(Todav??a no.)"
            jump ch1dinnermenu
        "Eyacular":
            jump ch1dinnercum

        "Utiliza su boca con m??s fuerza" if dep >= 2:
            $ persistent.ch1vic1 = True
            if menu2:
                $ v_score -= 1
                $ v_lust += 1
                $ menu2 = False
            p "Quiero ver que puedes hacer realmente."
            show bg ch1dinner63 with dissolve
            v "Entonces te mostrar??."
            show bg ch1dinner64 with dissolve
            v "Estoy lista."
            show bg ch1dinner65 with hpunch
            v "*La sujetas mientras tu pene entra profundamente en su boca*"
            show bg ch1vicblow2 movie with dissolve
            p "Mierda, eres excelente.{w} Incre??ble."
            v "*Contin??a con las arcadas mientras lo metes con fuerza en su boca*"
            menu:
                "Eyacular":
                    jump ch1dinnercum
                "Haz otra cosa":
                    pt "(Hagamos otra cosa.)"
                    jump ch1dinnermenu


label ch1dinnercum:
    p "??Mierda, me voy a correr!"
    show bg ch1dinner79 with dissolve
    v "C??rrete sobre m??."
    show bg ch1dinner80 with quickflash
    p "????ARRGGH!!"
    show bg ch1dinner74 with dissolve
    v "Buen trabajo."
    show bg ch1dinner75 with dissolve
    v "Mmmm. Sabes bien. Estaba preocupada. La pr??xima vez mi boca puede ser la tuya.{w} Te lo has ganado."
    show bg ch1dinner71 with dissolve
    p "Trabajar contigo deber??a ser interesante."
    v "As?? ser??."
    show bg ch1dinner72 with dissolve
    v "Deber??amos vestirnos. Me temo que nuestra reserva est?? llegando a su fin."
    p "Por supuesto."
    $ renpy.end_replay()
    if not persistent.ch1vic:
        $ renpy.notify(['Escena desbloqueada', 'unlock'])
        $ persistent.ch1vic = True
    jump ch1dinnerend

label ch1dinnerend:

    scene black with Dissolve(3)
    show bg ch1dinner81 with Dissolve(3)
    v "As?? que, agente, ??podemos esperar que empiece con esto pronto?"
    p "A primera hora de la ma??ana."
    show bg ch1dinner82 with dissolve
    v "Bien, eso espero."
    p "No te preocupes. Ella estar?? en tus manos antes de que te des cuenta."
    v "Gracias. Que tengas buena noche, agente."
    scene black with Dissolve(1)
    show bg ch1dinner83 with dissolve
    v "S??, se??ora, ha aceptado. "
    if "ch1vic" in extraevents:
        v "Ha sido necesario persuadirlo, pero ya est?? hecho."
    if "ch1turndown" in extraevents:
        v "Debo decirlo. Hay algo intrigante en ??l."
    jump ch1glorianight
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
