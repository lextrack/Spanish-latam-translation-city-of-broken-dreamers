

image bg ch2katiehome1 = "ch2katiehome1"
image bg ch2katiehome2 = "ch2katiehome2"
image bg ch2katiehome3 = "ch2katiehome3"
image bg ch2katiehome4 = "ch2katiehome4"
image bg ch2katiehome5 = "ch2katiehome5"
image bg ch2katiehome6 = "ch2katiehome6"
image bg ch2katiehome7 = "ch2katiehome7"
image bg ch2katiehome8 = "ch2katiehome8"
image bg ch2katiehome9 = "ch2katiehome9"
image bg ch2katiehome10 = "ch2katiehome10"
image bg ch2katiehome11 = "ch2katiehome11"
image bg ch2katiehome12 = "ch2katiehome12"
image bg ch2katiehome13 = "ch2katiehome13"


image bg ch2ellenhome1 = "ch2ellenhome1"
image bg ch2ellenhome2 = "ch2ellenhome2"
image bg ch2ellenhome3 = "ch2ellenhome3"
image bg ch2ellenhome4 = "ch2ellenhome4"
image bg ch2ellenhome5 = "ch2ellenhome5"
image bg ch2ellenhome6 = "ch2ellenhome6"
image bg ch2ellenhome7 = "ch2ellenhome7"
image bg ch2ellenhome8 = "ch2ellenhome8"
image bg ch2ellenhome9 = "ch2ellenhome9"
image bg ch2ellenhome10 = "ch2ellenhome10"

image bg ch2victoriahomenight1 = "ch2victoriahomenight1"
image bg ch2victoriahomenight2 = "ch2victoriahomenight2"
image bg ch2victoriahomenight3 = "ch2victoriahomenight3"
image bg ch2victoriahomenight4 = "ch2victoriahomenight4"
image bg ch2victoriahomenight5 = "ch2victoriahomenight5"
image bg ch2victoriahomenight6 = "ch2victoriahomenight6"
image bg ch2victoriahomenight7 = "ch2victoriahomenight7"
image bg ch2victoriahomenight8 = "ch2victoriahomenight8"
image bg ch2victoriahomenight9 = "ch2victoriahomenight9"
image bg ch2victoriahomenight10 = "ch2victoriahomenight10"
image bg ch2victoriahomenight11 = "ch2victoriahomenight11"
image bg ch2victoriahomenight12 = "ch2victoriahomenight12"
image bg ch2victoriahomenight13 = "ch2victoriahomenight13"
image bg ch2victoriahomenight14 = "ch2victoriahomenight14"
image bg ch2victoriahomenight15 = "ch2victoriahomenight15"
image bg ch2victoriahomenight16 = "ch2victoriahomenight16"
image bg ch2victoriahomenight17 = "ch2victoriahomenight17"
image bg ch2victoriahomenight18 = "ch2victoriahomenight18"
image bg ch2victoriahomenight19 = "ch2victoriahomenight19"
image bg ch2victoriahomenight20 = "ch2victoriahomenight20"
image bg ch2victoriahomenight21 = "ch2victoriahomenight21"
image bg ch2victoriahomenight22 = "ch2victoriahomenight22"
image bg ch2victoriahomenight23 = "ch2victoriahomenight23"
image bg ch2victoriahomenight24 = "ch2victoriahomenight24"
image bg ch2victoriahomenight25 = "ch2victoriahomenight25"
image bg ch2victoriahomenight26 = "ch2victoriahomenight26"
image bg ch2victoriahomenight27 = "ch2victoriahomenight27"
image bg ch2victoriahomenight28 = "ch2victoriahomenight28"
image bg ch2victoriahomenight29 = "ch2victoriahomenight29"
image bg ch2victoriahomenight30 = "ch2victoriahomenight30"
image bg ch2victoriahomenight31 = "ch2victoriahomenight31"
image bg ch2victoriahomenight32 = "ch2victoriahomenight32"
image bg ch2victoriahomenight33 = "ch2victoriahomenight33"
image bg ch2victoriahomenight34 = "ch2victoriahomenight34"
image bg ch2victoriahomenight35 = "ch2victoriahomenight35"
image bg ch2victoriahomenight36 = "ch2victoriahomenight36"
image bg ch2victoriahomenight37 = "ch2victoriahomenight37"
image bg ch2victoriahomenight38 = "ch2victoriahomenight38"
image bg ch2victoriahomenight39 = "ch2victoriahomenight39"
image bg ch2victoriahomenight40 = "ch2victoriahomenight40"
image bg ch2victoriahomenight41 = "ch2victoriahomenight41"
image bg ch2victoriahomenight42 = "ch2victoriahomenight42"

image bg ch2vichand movie = Movie(play="video/chapter-2-video/ch2vichand.webm")
image bg ch2vicnuru movie = Movie(play="video/chapter-2-video/ch2vicnuru.webm")
image bg ch2vicride movie = Movie(play="video/chapter-2-video/ch2vicride.webm")

image ch2cityzoommov = Movie(play='video/chapter-2-video/ch2cityzoom.webm', loop=False)
image bg ch2cityzoommovie movie:
    "ch2cityzoommov"
    pause 10.0
    "ch2cityzoomend"

label ch2after:

    scene black with Dissolve(2)
    window hide
    show bg ch2cityzoommovie movie with dissolve
    $ renpy.pause()
    n "Ambos regresan, dejando el condominio de Alexis"


    play music audio.calm fadein 2.0 fadeout 2.0
    scene black
    show text "{=trans}UNA HORA DESPU??S, DE VUELTA AL DEPARTAMENTO{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)

    if "ch2choosekatie" in extraevents:

        show bg ch2katiehome1 with dissolve
        k "Oye, s?? que esto puede ser atrevido... pero estoy muy cansada... ??te importa si paso la noche aqu???"
        n "A??ade Katie apresuradamente"
        k "En tu sof?? quiero decir. No en la cama."
        p "S??, no hay problema. Pero te advierto que no es lo m??s c??modo del mundo."
        k "No pasa nada. He dormido en la oficina algunas veces. Y despu??s de lo sucedido hoy..."
        p "??Despu??s de hoy? ??Est??s bien?"
        show bg ch2katiehome2 with dissolve
        k "Tienes que prometer que no te burlar??s de m??."
        p "No."
        k "Lo digo en serio."
        p "Lo prometo."
        k "Es que... Hoy ha sido una locura. Tengo un poco de miedo de ir a casa sola. Es una tonter??a. Entiendo que..."
        p "Toma la cama. Me voy al sof??."
        show bg ch2katiehome3 with dissolve
        k "No, no... No podr??a."
        p "Bueno, me quedo con el sof??. Si quieres dormir conmigo, puedes acompa??arme all??. La cama se queda abierta de cualquier manera."
        k "Gracias, eso es..."
        show bg ch2katiehome4 with dissolve
        k "Espera, ??no te vas a burlar de m?? por estar asustada?"
        p "Lo acabo de prometer, ??no?"
        k "S??, pero..."
        menu:
            "B??rlate de ella":
                p "??Unos cuantos pandilleros armados, un misterioso cad??ver y un allanamiento de morada son demasiado para ti?"
                p "Pens?? que ibas a morir del susto."
                k "??[p]!"
                p "Has vuelto a sacar el tema."
            "S?? amable":
                $ k_score += 1
                p "Doc, para m??, estar a punto de recibir un disparo es un lunes en la ma??ana para m??, es normal. Pero ese soy yo, no t??. C??lmate."
                k "Gracias por la comprensi??n."


        p "??Quieres ver una pel??cula o algo?"
        k "Pero nada de pel??culas de terror, por favor. O de cr??menes, o de asesinatos. Algo relajante."
        p "No hay problema, veamos qu?? tenemos."
        if "ch1futafull" in extraevents:
            show bg ch2katiehome6 with dissolve
            klx "Ohhh, [p]. ??Te he echado de menos! ??Necesito tu polla gigante dentro de m??!"
            show bg ch2katiehome9 with dissolve
            k "??[p]? Esto califica, supongo."
            p "Gracias Sam, esto sucede a veces. Cambia de canal, Sam."
            s "Por supuesto."
            k "??Es eso un...?"
            p "??Sam, cambia el canal, o voy a reemplazarte!"
            s "Cambiando, se??or."
            show bg ch2katiehome7 with dissolve
            p "Ya est??, ??qu?? tal esto?"
            k "No lo s??. Ese parec??a interesante. Quiero decir, claramente te gust??."
            p "Yo, eh..."
            k "*Se r??e*"
        else:
            show bg ch2katiehome7 with dissolve
            k "Ya he visto esto, pero est?? bien."
            p "??Segura?"
        show bg ch2katiehome8 with dissolve
        k "No pasa nada. Estoy bastante cansada."
        k "Ciertamente haces que una cita sea emocionante. Lo reconozco."
        p "Gracias, supongo."
        show bg ch2katiehome10 with dissolve
        k "Mira, estoy feliz de ayudar. No har??a esto por cualquiera."
        p "??Por qu?? soy un caso especial?"
        k "Intentas hacer el bien a la gente. Eso es raro."
        p "Lo dices porque no me conoces. Pero, lo aprecio."
        show bg ch2katiehome11 with dissolve
        k "Me alegro. *Bosteza* Vaya, creo que voy a caer rendida..."
        show bg ch2katiehome12 with dissolve
        p "??Tan r??pido? Bueno, te ves bastante mal."
        show bg ch2katiehome13 with dissolve
        p "Sam, aten??a las luces."
        s "Bajando las luces, se??or."
        p "Si necesitas algo, p??deselo a Sam."
        if "ch1futafull" in extraevents:
            k "Esa chica ten??a unas... *Asiente con la cabeza*"
        p "Buenas noches, Katie."
        scene black with Dissolve(3)
        p "Yo tambi??n deber??a dormir."
        jump ch2nextmorning




    if "ch2chooseellen" in extraevents:
        show bg ch2ellenhome2 with dissolve
        p "??C??mo te encuentras?"
        e "Me siento bastante bien en realidad, el haberle dado un pu??etazo me ha ayudado. Me quito un gran peso de encima."
        e "Casi hace que llevar esta maldita cosa valga la pena."
        p "Puedo traerte algo m??s c??modo."
        e "Estoy bien."
        show bg ch2ellenhome3 with dissolve
        e "Puedo dormir con cualquier cosa. Casi."
        p "??Dormir? ??No te acabas de despertar?"
        e "No me he \"despertado.\" Me {i}despertaste{/i} demasiado temprano."
        e "Necesito mi sue??o reparador, [p]."
        show bg ch2ellenhome4 with dissolve
        p "*Suspira* Sam, aten??a las luces."
        s "Bajando las luces, se??or."
        show bg ch2ellenhome5 with dissolve
        e "As?? que crees que el tercero es Henry, ??eh?"
        p "Todo coincide."
        show bg ch2ellenhome6 with dissolve
        e "Excepto que, ya sabes, est?? muerto."
        p "??Est??s segura?"
        e "Bastante segura, pero no vi el cuerpo. Estaba con Conner en otro sitio cuando sucedi?? eso. En todo caso, si alguien pudiera morir y no estar muerto, ser??a ese tipo."
        e "Era una bestia."
        show bg ch2ellenhome7 with dissolve
        e "En fin, hora de dormir."
        p "??Acabas de decir que es hora de dormir?"
        show bg ch2ellenhome8 with dissolve
        e "??Vas a venir o qu???"
        p "S??, lo siento. ??Tambi??n quieres un oso de peluche?"
        show bg ch2ellenhome9 with dissolve
        e "Sabes, si ese tipo es Henry..."
        p "??S???"
        e "Te partir?? por la mitad y no en el buen sentido."
        p "??Cu??l una buena manera?"
        e "S??, como un hueso de pollo."
        p "Gracias por el voto de confianza."
        show bg ch2ellenhome10 with dissolve
        e "Nunca conociste al cabr??n. Esa foto no dice ni la mitad."
        e "Solo le vi un par de veces, como cuando llev?? a Gloria a los bastidores y cosas as??. Pero, de lo poco que vi, ??l era m??s padre, que su propio padre."
        e "Recibir??a una bala por ella."
        p "Si es como dices, espero que no tenga que hacerlo. Venga, vamos a dormir un poco. Despu??s de esta noche, creo que lo necesitas."
        e "Me alegro de que estuvieras all??. No s?? qu?? habr??a hecho si no me hubieras detenido."
        p "T?? misma lo has dicho. No est??s cegada como ??l. Vamos, duerme un poco."
        scene black with Dissolve(3)
        jump ch2nextmorning




    if "ch2choosevic" in extraevents:
        show bg ch2victoriahomenight1 with dissolve
        v "Lo ves, puedo ser de mucha ayuda, agente."
        p "Al menos por ahora."
        show bg ch2victoriahomenight2 with dissolve
        v "Seguimos en el mismo bando. Aprecio tus esfuerzos."
        p "Tienes una extra??a manera de demostrarlo."
        show bg ch2victoriahomenight4 with dissolve
        if v_score >= 2:
            v "Si quieres, puedo mostrarlo de otra manera. Una forma m??s ??ntima."
        else:
            v "Promet?? mostrarlo de otra manera, ??no es as??? Una forma que disfrutar??as."

        menu:
            "No es necesario":
                $ extraevents.append("ch2vicrefuse")
                jump ch2aftervicrefuse
            "Me gustar??a":
                $ extraevents.append("ch2vicsex")
                jump ch2aftervicsex


label ch2aftervicrefuse:
    p "Gracias, pero paso. Buenas noches, Victoria."
    show bg ch2victoriahomenight3 with dissolve
    v "Yo... por supuesto."
    v "Buenas noches a ti tambi??n, [p]."
    show bg ch2victoriahomenight41 with dissolve
    p "*Se truena el cuello* Sam, apaga las luces, es hora de dormir."
    show bg ch2victoriahomenight42
    s "Apagando las luces, se??or."
    scene black with Dissolve(3)
    show bg ch2dream1 with dissolve
    p "Tiene que haber algo. Podemos hacer algo m??s... cualquier cosa."
    show bg ch2dream2 with dissolve
    p "??Maldita seas, Meredith!"
    scene black with Dissolve(3)
    jump ch2nextmorning


label ch2aftervicsex:
    if "ch1vic" in extraevents:
        p "Me has {i}hecho{/i} esperar, ??verdad?"
    else:
        p "Me gustar??a mucho."

    show bg ch2victoriahomenight5 with dissolve
    if vicsexname:
        v "Has demostrado una gran moderaci??n. Las cosas buenas llegan a los que esperan. ??No es as??, [vicsexname]?"
        show bg ch2victoriahomenight6 with dissolve
        p "S??."
    else:

        v "Has mostrado moderaci??n. Creo que eso deber??a ser recompensado. ??Verdad, agente?"
        v "Pero llamarte agente me parece bastante formal para lo que est?? por venir. ??Prefieres otro apodo?"
        menu:
            "[p], est?? bien":
                p "[p], est?? bien."
                $ vicsexname = p
            "Ll??mame...":
                python:
                    vicsexname = renpy.input("??C??mo quieres que te llame?")
                    vicsexname = vicsexname.strip()

                    if not vicsexname:
                        vicsexname = p
                if vicsexname == "Agent" or vicsexname == "agent":
                    v "Ja ja, muy gracioso."
                    v "Tal vez me equivoqu?? contigo. [vicsexname], se queda, entonces."
                $ persistent.vicsexname = vicsexname



        show bg ch2victoriahomenight6 with dissolve
        v "Muy bien, [vicsexname]."
    show bg ch2victoriahomenight8 with dissolve
    v "Cuando estuve aqu?? antes, te dej?? una sorpresa."
    if v_score <= 0:
        p "Espero que no sea letal."
        v "Ser?? letal. M??s vale que tu coraz??n est?? preparado para ello."
    else:
        p "??Qu?? ser??a?"
        v "No ser??a una sorpresa si te lo dijera, ??verdad?"
    show bg ch2victoriahomenight10 with dissolve
    jump ch2vicstart


label ch2aftermusic:
    menu:
        "Algo sexy":
            p "Sam, play Amertume."
            play music audio.tensesexy fadein 2.0 fadeout 2.0
            v "Fitting."
        "Canciones de Ellen":
            p "Play Plastic Console, Sam."
            play music audio.console fadein 2.0 fadeout 2.0
            v "Ahh, Ellen Lane hizo los coros para esto."
            p "Buen o??do."
        "Algo m??s relajado":
            p "Haz lo tuyo, Sam."
            play music audio.moments fadein 2.0 fadeout 2.0
            v "Me gusta."


    return

label ch2vicstart:
    if _in_replay:
        show bg ch2victoriahomenight10 with dissolve
        $ setReplay()
    $ extraevents.append("ch2vic")
    v "Ahora, [vicsexname], s??gueme."
    p "Por supuesto."
    show bg ch2victoriahomenight11 with dissolve
    if "ch1vic" in extraevents:
        v "Sam, toca algo apropiado."
        s "Por supuesto, se??orita."
        p "??Espera! Pens?? que..."
        show bg ch2victoriahomenight12 with dissolve
        v "??Qu?? pensabas, [vicsexname]?"
        v "C??lmate. Arreglar?? a Sam m??s tarde."
        v "Si te hace sentir mejor, ??por qu?? no eliges?"
        call ch2aftermusic from _call_ch2aftermusic
    else:
        v "??Tal vez algo de m??sica?"
        call ch2aftermusic from _call_ch2aftermusic_1

        show bg ch2victoriahomenight12 with dissolve
        v "S?? que puedo parecer distante, pero es hora de mostrarte mi otro lado, [vicsexname]."
        v "Te vas a llevar una buena sorpresa."
    show bg ch2victoriahomenight13 with dissolve
    p "(Oh, Dios...)"
    v "La pregunta es, ??puedes conmigo, [vicsexname]?"
    show bg ch2victoriahomenight14 with dissolve
    v "??Est??s nervioso? No esperar??a eso teniendo en cuenta tu reputaci??n."
    p "Los nervios y la excitaci??n son dos cosas muy diferentes."
    show bg ch2victoriahomenight15 with dissolve
    v "Bueno, las cosas se pondr??n emocionantes."
    p "Ya lo est??n."
    v "Y ni siquiera has visto mi regalo."
    show bg ch2victoriahomenight18 with dissolve
    p "Ahora mismo, todo lo que necesito es lo que tengo delante."
    show bg ch2victoriahomenight16 with dissolve
    v "Todo un encanto, [vicsexname]. Ahora, si eres tan amable, qu??tate la ropa y acu??state."
    p "Por supuesto."
    scene black with dissolve
    show bg ch2victoriahomenight19 with dissolve
    v "??Sabes qu?? es esto? Es bastante raro."
    p "No s?? qu?? es."
    show bg ch2victoriahomenight20 with dissolve
    v "Aceite de algas nuri y flor de cerezo blanco. Solo se fabricaba en Jap??n, se perdi?? despu??s de la guerra."
    v "Se sabe que es bastante... sensual."
    show bg ch2victoriahomenight21 with dissolve
    v "Hay un masaje especializado. Bastante er??tico y bastante placentero."
    v "Har?? que te corras como nunca antes lo has hecho."
    show bg ch2victoriahomenight22 with dissolve
    v "Mmm, mira c??mo brilla. Hipnotizante."
    p "S??..."
    show bg ch2victoriahomenight23 with dissolve
    v "Primero, te calentar??... rel??jate y pi??rdete en la sensaci??n de mi cuerpo sobre el tuyo."
    show bg ch2victoriahomenight25 with dissolve
    v "Siente c??mo me deslizo por tu pecho. Mis pezones recorriendo tu piel."
    p "*Respira profundamente* Mierda, eso se siente incre??ble."
    show bg ch2victoriahomenight24 with dissolve
    v "Me alegro de que te guste, [vicsexname]. Ser??a una pena que se desperdiciara."
    if v_score >= 2:
        p "Gracias por compartirlo conmigo."
        v "Por supuesto."
    else:
        p "Vali?? la pena."
    show bg ch2victoriahomenight26 with dissolve
    v "Ahora, [vicsexname] parece que est??s listo para empezar."
    p "??Qu?? es lo que...?"
    show bg ch2vichand movie with dissolve
    p "Ohhh..."
    v "Disfruta, mi mano aceitada desliz??ndose arriba y abajo de esa dura verga tuya. Mmm..."
    p "Normalmente, esto es solo para calentar... *Respira profundamente*"
    show bg ch2victoriahomenight27 with dissolve
    v "Tienes que aguantar. M??s tarde podr??s eyacular."
    show bg ch2victoriahomenight28 with dissolve
    v "Mmm, [vicsexname]."
    v "Ahora, aqu?? es donde se ve para qu?? sirve realmente este aceite."
    show bg ch2vicnuru movie with dissolve
    v "Nuestros cuerpos se convierten en uno... siente c??mo mis pezones se deslizan por tu piel. Respira conmigo."
    v "Ni demasiado fuerte, ni demasiado suave."
    show bg ch2victoriahomenight29 with dissolve
    p "??D??nde aprendiste...?"
    v "Shhh..."
    show bg ch2vicnuru movie with dissolve
    v "Disfr??talo. Cierra los ojos y deja que mis pechos te complazcan."
    p "..."
    v "??Quieres cogerme ahora?"
    show bg ch2victoriahomenight30 with dissolve
    jump ch2victorianightmenu

label ch2victorianightmenu:
    menu:
        "Masajea m??s":
            jump ch2vicnuru
        "Quiero sentir tu mano de nuevo":
            jump ch2vichandjob
        "Qu??tale los calzones":
            jump ch2vicfuck

label ch2vichandjob:
    p "Quiero volver a sentir tu mano sobre m??."
    show bg ch2victoriahomenight26 with dissolve
    v "Oh, [vicsexname], ??lo disfrutaste?"
    p "Normalmente no me hace nada, pero eso fue incre??ble."
    show bg ch2vichand movie with dissolve
    v "Me gusta c??mo miras mis pechos aceitados mientras te acaricio."
    v "??Contin??o? Puedo hacer esto toda la noche."
    p "Es tentador, pero hagamos otra cosa."
    jump ch2victorianightmenu

label ch2vicnuru:
    p "Quiero volver a sentir tus pechos."
    show bg ch2victoriahomenight28 with dissolve
    v "Mmm, s??, [vicsexname]."
    show bg ch2vicnuru movie with dissolve
    p "Ohhh, gracias."
    v "Es un placer. Son tuyos. Yo soy tuya."
    v "??Ya quieres cogerme, [vicenombre]?"
    jump ch2victorianightmenu

label ch2vicfuck:
    p "S??, te necesito ahora."
    show bg ch2victoriahomenight30 with dissolve
    v "Lo s??. Puedo verlo en tus ojos."
    show bg ch2victoriahomenight31 with dissolve
    v "Aqu?? vamos."
    if "ch1vic" in extraevents:
        v "Ahora d??jame montarte de nuevo."
    else:
        v "Ahora d??jame montarte."
    show bg ch2victoriahomenight32 with dissolve
    if v_score >= 1:
        p "Hermoso..."
    else:
        p "Eres incre??ble."
    v "??Te gusta lo apretada que est?? mi vagina?"
    show bg ch2victoriahomenight33 with dissolve
    p "*Gime de placer*"
    v "S??, si??nteme."
    show bg ch2vicride movie with dissolve
    v "??C??GEME!"
    p "??M??ntame!"
    v "??Oh, Dios, s??! Te lo dije... *Gime de alegr??a* ??valdr??a la pena esperar!"
    p "Dios, puedo sentir que te aprietas m??s."
    v "Mmmm... [vicsexname], Voy a correrme por ti."
    show bg ch2victoriahomenight34 with hpunch
    v "S??, [vicsexname]!"
    v "*Jadeando fuertemente* Ahora te toca a ti."
    show bg ch2victoriahomenight35 with dissolve
    v "Falta poco, para que te liberes."
    v "Todo lo que necesitas es..."
    show bg ch2victoriahomenight36 with dissolve
    v "*Sopla suavemente tu pene* La m??s m??nima sensaci??n..."
    p "??Ooooh!"
    show bg ch2victoriahomenight37 with vpunch
    p "??Dios!"
    show bg ch2victoriahomenight38 with dissolve
    v "Para que te liberes."
    p "??D??nde mierda has aprendido eso? Nunca he... eres incre??ble."
    v "Gracias, [vicsexname]. Ahora no s?? t??, pero a m?? me vendr??a bien dormir un poco."
    $ renpy.end_replay()
    if not persistent.ch2vic:
        $ renpy.notify(['Escena desbloqueada', 'unlock'])
        $ persistent.ch2vic = True
    scene black with Dissolve(1)
    stop music fadeout 7.0
    show bg ch2victoriahomenight39 with dissolve
    v "Entonces, ??ma??ana te reunir??s con este Shanlon Russell?"
    p "Eso planeo."
    show bg ch2victoriahomenight40 with dissolve
    if "ch1vic" in extraevents:
        v "Conf??o en que no tendr??s problemas para tratar con alguien como ella."
        p "Tengo mis m??todos."
    else:
        v "??Est??s acostumbrado a manejar mujeres como ella?"
        p "No te preocupes, ella es solo una celebridad con un ego inflado. Estar?? bien."
        v "No te diviertas mucho."
        p "Lo intentar??."
    scene black with Dissolve(3)
    jump ch2nextmorning
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
