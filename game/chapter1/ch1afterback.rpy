


image bg ch1afterback2 = "ch1aftermathback2"
image bg ch1afterback3 = "ch1aftermathback3"
image bg ch1afterback4 = "ch1aftermathback4"
image bg ch1afterback5 = "ch1aftermathback5"
image bg ch1afterback6 = "ch1aftermathback6"
image bg ch1afterback7 = "ch1aftermathback7"
image bg ch1afterback8 = "ch1aftermathback8"
image bg ch1afterback9 = "ch1aftermathback9"
image bg ch1afterback10 = "ch1aftermathback10"
image bg ch1afterback11 = "ch1aftermathback11"
image bg ch1afterback12 = "ch1aftermathback12"
image bg ch1afterback13 = "ch1aftermathback13"
image bg ch1afterback14 = "ch1aftermathback14"
image bg ch1afterback15 = "ch1aftermathback15"
image bg ch1afterback16 = "ch1aftermathback16"
image bg ch1afterback17 = "ch1aftermathback17"
image bg ch1afterback18 = "ch1aftermathback18"
image bg ch1afterback19 = "ch1aftermathback19"
image bg ch1afterback20 = "ch1aftermathback20"
image bg ch1afterback21 = "ch1aftermathback21"
image bg ch1afterback22 = "ch1aftermathback22"
image bg ch1afterback23 = "ch1aftermathback23"
image bg ch1afterback24 = "ch1aftermathback24"
image bg ch1afterback25 = "ch1aftermathback25"
image bg ch1afterback26 = "ch1aftermathback26"
image bg ch1afterback27 = "ch1aftermathback27"
image bg ch1afterback28 = "ch1aftermathback28"
image bg ch1afterback29 = "ch1aftermathback29"
image bg ch1afterback30 = "ch1aftermathback30"
image bg ch1afterback31 = "ch1aftermathback31"
image bg ch1afterback32 = "ch1aftermathback32"
image bg ch1afterback33 = "ch1aftermathback33"
image bg ch1afterback34 = "ch1aftermathback34"
image bg ch1afterback35 = "ch1aftermathback35"
image bg ch1afterback36 = "ch1aftermathback36"
image bg ch1afterback37 = "ch1aftermathback37"
image bg ch1afterback38 = "ch1aftermathback38"
image bg ch1afterback39 = "ch1aftermathback39"
image bg ch1afterback40 = "ch1aftermathback40"
image bg ch1afterback41 = "ch1aftermathback41"





label ch1afterback:
    show bg ch1afterback21 with dissolve
    $ renpy.music.set_volume(0.4, 0, 'music')
    if not persistent.ch1card1:
        $ renpy.notify(['Posible pista', 'alert'])
        show screen hidden_item("ch1card1", "ch1card1", 1298, 165, 171, 274)
    pt "(All?? est??.)"
    if "ch1chandra" in extraevents:
        pt "(Mierda, llego tarde. Se va a enojar.)"
    else:
        pt "(Justo a tiempo.)"
    hide screen hidden_item
    show bg ch1afterback23 with dissolve
    pt "Interesante compa????a."
    show bg ch1afterback30 with dissolve
    p "??Qu?? pasa, Ellen? Me has hecho venir apresuradamente en mitad de la noche. ??Voy a recibir una explicaci??n?"
    $ e_met = True
    e "Ven aqu??, [p]."
    show bg ch1afterback10 with dissolve
    p "Tenemos toda la zona VIP para nosotros. Eso no es barato. Eso significa trabajo corporativo."
    e "Ven, [pl]."
    show bg ch1afterback11 with dissolve
    e "Nunca me dicen m??s de lo que necesitas saber."
    p "S??, s??."
    e "Si??ntate."
    if "ch1chandra" in extraevents:
        e "Antes de empezar, dije 30 minutos."
        p "S??, lo siento. ??Pero qu?? esperabas? Apenas llego a tiempo cuando me avisas con un d??a de antelaci??n. Pero con 30 minutos, tienes suerte de que est?? aqu??."
    else:
        e "Llegas a tiempo por una vez. ??Quieres arruinar mi buen humor?"
        p "Solo intento ser un poco m??s puntual."
    show bg ch1afterback22 with Dissolve(1)
    "*Mujer encapuchada desconocida*" "Hola agente [pl]."
    show bg ch1afterback24 with dissolve
    "*Mujer encapuchada desconocida*" "Ya est?? aqu??."
    "*Mujer encapuchada desconocida*" "..."
    "*Mujer encapuchada desconocida*" "Entiendo. Lo har??. Mantendr?? los ojos en ??l, no te preocupes."
    show bg ch1afterback25 with dissolve
    "*Hombre desconocido*" "Oye, ??por qu?? te escondes aqu?? sola??"
    "*Mujer encapuchada desconocida*" "??Eh?"
    show bg ch1afterback26 with dissolve
    "*Hombre desconocido*" "??Por qu?? la capucha? ??Eres una especie de monstruo con SDG o algo as??? Y me parece bien; todo el mundo sabe que los Milchers son incre??bles en la cama..."
    "*Mujer encapuchada desconocida*" "Disculpe, se??orita."
    show bg ch1afterback27 with dissolve
    $ renpy.pause(0.5)
    show bg ch1afterback28 with hpunch
    "*Hombre desconocido*" "??AHH!"
    show bg ch1afterback29 with dissolve
    "*Mujer encapuchada desconocida*" "Mucho mejor. Lo siento, solo una peque??a cosa de la que deb??a ocuparme. Me disculpo."
    "*Hombre desconocido*" "*Tose y jadea.*"
    "*Mujer encapuchada desconocida*" "??Ahora qu???"
    if "ch1chandra" in extraevents:
        show bg ch1afterback6 with dissolve
        e "Cada vez que te doy un trabajo mi reputaci??n entra en juego."
        e "Te vendo como el mejor Fantasma que conozco y la mitad de las veces ni siquiera aceptas el puto trabajo."
        e "??Sabes c??mo me hace ver eso?"
        menu:
            "Te da igual":
                p "Llegu?? unos minutos tarde. ??Cu??l es el problema?"
                call ch1afterbackangry from _call_ch1afterbackangry
            "Razona con ella":
                $ e_score += 1
                p "Mierdas que pasan. Lo sabes mejor que nadie. ??Podemos proseguir?"
                p "Dame los detalles. Ser?? mejor que no sea otro robo."
                e "Han pasado, ??cu??nto, dos meses desde tu ??ltimo trabajo? Supongo que pagar las facturas har?? que aceptes algo, eventualmente..."
            "Pide disculpas":
                p "Hola, lo siento, me he topado con alguien de camino aqu??."
                e "No me importa. Somos profesionales y no me gusta que me hagan perder el tiempo."
                p "??Rel??jate, Ellen! Solo fueron un par de minutos. ??Cu??l es el problema?"
                call ch1afterbackangry from _call_ch1afterbackangry_1
    else:
        $ e_score += 1
        show bg ch1afterback4 with dissolve
        e "Me alegro de que seas puntual, espero que lo conviertas en un h??bito."
        p "Y espero que no me hayas tra??do para otro robo."
        show bg ch1afterback6 with dissolve
        e "Es lo que hay. No es mi culpa que seas tan exigente."
        e "Y los necesito. T?? sigues rechazando estos trabajos y eso nos perjudica a los dos."
        p "No voy a ir tras otro fugitivo que tiene problemas con su padre."
        show bg ch1afterback5 with dissolve
        e "Oh, conozco al padre en este caso. Te aseguro que no est?? involucrado. ??Quieres verlo o no?"
        p "Muy bien, mu??stramelo."
    show bg ch1afterback14 with dissolve

    e "Los detalles son limitados, pero s?? algunas cosas."
    show bg ch1afterback15 with dissolve
    p "??Una fuga? ??Qu?? mierda, Ellen? Solo es una ni??a."
    e "Simplemente l??elo. En serio... esto es personal."

    show bg ch1afterback16 with dissolve



    e "Aqu?? est?? la informaci??n. Anoche, un escuadr??n de Fantasmas intent?? detener a una mujer durante un espect??culo."
    e "El p??nico fue absoluto. Nadie sabe qu?? pas?? exactamente, pero cuando termin??, los tres Fantasmas estaban muertos y la ni??a no aparec??a por ning??n lado."
    p "??Qui??n la ayud???"
    e "No lo s??. Pero, mi suposici??n, es que por eso el cliente quiere que la traigan."
    p "Tremendo espect??culo."
    e "S??, fue justo en el callej??n."

    p "Entonces, Gloria Conner, ??eh?"
    p "Veamos qu?? tenemos aqu??."

    $ resetmenu()
    jump ch1padmenu



label ch1padmenu:
    menu:
        "??Tech Noir?" if menu1 == True:
            $ menu1 = False
            p "??El Tech Noir? Ese es el lugar en el que act??as, ??verdad?"
            e "Ya no... no despu??s del incidente. As?? que eso me convierte en una contratista a tiempo completo."
            p "??No puedes cantar en otro sitio?"
            e "Sabes que eso no va a pasar."
            jump ch1padmenu
        "??Escuadr??n de Fantasmas?" if menu2 == True:
            $ menu2 = False
            p "??Un grupo de Fantasmas fuertemente armados entran y acaban muertos? ??C??mo?"
            e "Ni idea... Yo estaba all??, pero una vez que los vi entrar me fui del escenario. Estaban bien preparados, [p]."
            p "??Qui??nes eran?"
            e "Bishop, Frost y Hudson."
            p "Bishop la iba a palmar tarde o temprano. Era un idiota. No me entristece verlo partir. Frost y Hudson, sin embargo, sab??an lo que hac??an."
            e "La pregunta es, ??qui??n la ayud???"
            p "Alguien astuto. Hudson era de primer nivel, incluso yo me preocupar??a por si lo molestara. Lleg?? y provoc?? el p??nico en el club. Su equipo ten??a la ventaja. Quien sea que se haya librado de ellos, tiene que ser muy bueno."
            p "??Sabes qui??n contrat?? a Hudson y su equipo?"
            e "No..."
            p "??Qu?? pasa con el otro equipo en el atentado anterior? ??Alguna idea?"
            e "Una vez m??s, ni idea."
            jump ch1padmenu
        "??Es una Milcher?" if menu3 == True:
            $ menu3 = False
            p "SDG, entonces, ??es una Milcher? No lo parece."
            e "No todos tienen escamas y colmillos, [p]. Ya lo sabes. Y no es que sea importante."
            e "Por cierto, la raz??n por la que s?? que su padre no est?? pagando esto es porque se deshizo de ella justo despu??s de que desarrollara los s??ntomas."
            p "Suena como un puto pr??ncipe..."
            e "M??s bien un rey. ??Te diste cuenta del apellido?"
            p "??Conner?"
            e "Como Alexis Conner."
            p "Eso explica que sea personal."
            e "S??..."
            p "Lo personal nunca se mezcla bien con los negocios, Lane. ??Por qu?? no dejarlo pasar?"
            e "No la he visto en a??os, pero... Gloria es una buena chica. O lo era, en aquel entonces."
            e "A su padre no le importa nada. Alguien deber??a cuidar de ella, al menos."
            e "Si alguien va a ir tras ella, prefiero que seas t??."
            p "Te lo agradezco, pero si es la mitad de imb??cil que dices que es... que te involucres del todo puede hacer que tu lista negra sea permanente."
            e "Si me importara una mierda, no estar??a aqu?? ahora mismo."
            jump ch1padmenu
        "Bien, con eso bastara.":
            p "??Algo m??s?"
            e "Eso es todo."
            jump ch1afterback2

label ch1afterbackangry:
    show bg ch1afterback2 with dissolve
    e "??El problema? [p], no has aceptado un trabajo en dos meses."
    e "Pierdo mi tiempo reuni??ndome contigo cada vez que hacemos esto. ??Lo tomas como un juego!"
    p "Tal vez aceptar??a si no todos los trabajos fueran de robos."
    show bg ch1afterback3 with dissolve
    e "??Oye, necesito que me paguen! El hecho de que quieras estar sob??ndote el culo todo el d??a no significa que yo pueda permit??rmelo. ??Crees que disfruto haciendo esta mierda?"
    e "Ahora solo c??ntrate en el trabajo. Conf??a en m??. Merece la pena, cabr??n."
    p "Maldita sea. De acuerdo, ??si con eso dejas de molestar!"
    return




label ch1afterback2:
    show bg ch1afterback17 with dissolve
    p "Por donde se le mire se ve que es una mala noticia."
    show bg ch1afterback18 with dissolve
    e "??C??mo es eso?"
    p "??Qui??n lo financia?"
    p "??A d??nde la llevo una vez que la encuentre?"
    p "Hay muchas preguntas sin respuesta aqu??, Ellen."
    show bg ch1afterback19 with dissolve
    e "Siempre ha funcionado as??. Vamos, por una vez acepta el trabajo."
    menu:
        "Ni hablar":
            p "De ninguna manera. Necesito m??s detalles. Lamento que esto sea personal para ti, pero no me f??o."
            show bg ch1afterback20 with dissolve
            e "Mierda??? necesito encontrar a alguien m??s apto."
            e "Vete a casa, [p]."
            p "No te pongas as??."
            e "Vete a la mierda, vete..."
            jump ch1homealone
        "Tengo que pensarlo":

            p "Necesito pensar en ello."
            show bg ch1afterback20 with dissolve
            e "No lo pienses mucho. Ambos necesitamos la paga."
            p "Solo dame la noche. D??jame dormir."
            show bg ch1afterback7 with dissolve
            e "*Suspira* Te gusta hacer las cosas dif??ciles, ??no?"
            show bg ch1afterback6 with dissolve
            e "De verdad te debe gustar mantenerme en suspenso."
            menu:
                "As?? es m??s divertido":
                    $ e_score += 1
                    p "Es m??s divertido as??. Me gusta verte sufrir."
                    e "Estoy segura de que s??."
                    p "Es lo que te gusta de m??."
                    show bg ch1afterback9 with dissolve
                    e "No te enorgullezcas tanto."
                    menu:
                        "Quiz?? pueda convencerme":
                            p "Tal vez, ??necesito un poco de convencimiento?"
                            if e_score >= 2:
                                jump ch1afterconvince
                            else:
                                e "Esta noche no, [p]. No estoy de humor."
                                e "Notif??came tu decisi??n ma??ana."
                                p "Lo har??. Buenas noches, Ellen."
                                jump ch1homealone
                        "Deber??a irme":
                            p "Deber??a volver a casa."
                            show bg ch1afterback13 with dissolve
                            e "Av??same ma??ana, ??de acuerdo?"
                            p "Lo har??. Buenas noches, Ellen."
                            jump ch1homealone
                "No es mi intenci??n":


                    p "Solo necesito tiempo. Ya sabes c??mo son las cosas."
                    e "Con el tiempo, lo superar??s."
                    e "Probablemente deber??as irte a casa. Hazme saber ma??ana lo que decidas."
                    p "Lo har??. Buenas noches, Ellen."
                    jump ch1homealone


        "Podr??a ser convencido" if e_score > 0:
            $ e_lust += 1
            jump ch1afterconvince

label ch1afterconvince:
    p "Siempre me vendr??a bien un cuerpo caliente a mi lado esta noche. Puedes ayudarme a decidir."
    show bg ch1afterback12 with dissolve
    e "Creo que eso puede arreglarse."
    show bg ch1afterback31 with dissolve
    e "Probablemente fue una de las razones por la que te llame esta noche, idiota."
    show bg ch1afterback33 with dissolve
    p "??Fue ahora?"
    e "Siempre es lo mismo contigo."
    show bg ch1afterback32 with dissolve
    p "Es por eso que eres mi contratista. El ??ltimo no ten??a un cuerpo como el tuyo."
    show bg ch1afterback34 with dissolve
    e "El ??ltimo fue un nativo americano de 300 libras llamado Hank."
    p "Como dije, no ten??a un cuerpo como el tuyo. Sin embargo, me consigui?? buenos trabajos."
    e "Ja ja. P??drete, [p]."
    show bg ch1afterback35 with dissolve
    e "Ahora, necesitamos m??s tragos."
    show bg ch1afterback36 with dissolve
    e "S??gueme."
    show bg ch1afterback37 with dissolve
    e "??Ahora qu???"
    p "Nada. Solo t??."
    show bg ch1afterback38 with dissolve
    e "Justo lo que quiero. Al grano."
    show bg ch1afterback40 with dissolve
    p "No hay raz??n para perder el tiempo con las bebidas."
    show bg ch1afterback39 with dissolve
    p "Tengo todo lo que quiero aqu??."
    show bg ch1afterback41 with dissolve
    e "??En tu casa?"
    p "Por supuesto."
    jump ch1ellen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
