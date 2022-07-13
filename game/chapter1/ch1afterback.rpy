


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
    pt "(Allí está.)"
    if "ch1chandra" in extraevents:
        pt "(Mierda, llego tarde. Se va a enojar.)"
    else:
        pt "(Justo a tiempo.)"
    hide screen hidden_item
    show bg ch1afterback23 with dissolve
    pt "Interesante compañía."
    show bg ch1afterback30 with dissolve
    p "¿Qué pasa, Ellen? Me has hecho venir apresuradamente en mitad de la noche. ¿Voy a recibir una explicación?"
    $ e_met = True
    e "Ven aquí, [p]."
    show bg ch1afterback10 with dissolve
    p "Tenemos toda la zona VIP para nosotros. Eso no es barato. Eso significa trabajo corporativo."
    e "Ven, [pl]."
    show bg ch1afterback11 with dissolve
    e "Nunca me dicen más de lo que necesitas saber."
    p "Sí, sí."
    e "Siéntate."
    if "ch1chandra" in extraevents:
        e "Antes de empezar, dije 30 minutos."
        p "Sí, lo siento. ¿Pero qué esperabas? Apenas llego a tiempo cuando me avisas con un día de antelación. Pero con 30 minutos, tienes suerte de que esté aquí."
    else:
        e "Llegas a tiempo por una vez. ¿Quieres arruinar mi buen humor?"
        p "Solo intento ser un poco más puntual."
    show bg ch1afterback22 with Dissolve(1)
    "*Mujer encapuchada desconocida*" "Hola agente [pl]."
    show bg ch1afterback24 with dissolve
    "*Mujer encapuchada desconocida*" "Ya está aquí."
    "*Mujer encapuchada desconocida*" "..."
    "*Mujer encapuchada desconocida*" "Entiendo. Lo haré. Mantendré los ojos en él, no te preocupes."
    show bg ch1afterback25 with dissolve
    "*Hombre desconocido*" "Oye, ¿por qué te escondes aquí sola??"
    "*Mujer encapuchada desconocida*" "¿Eh?"
    show bg ch1afterback26 with dissolve
    "*Hombre desconocido*" "¿Por qué la capucha? ¿Eres una especie de monstruo con SDG o algo así? Y me parece bien; todo el mundo sabe que los Milchers son increíbles en la cama..."
    "*Mujer encapuchada desconocida*" "Disculpe, señorita."
    show bg ch1afterback27 with dissolve
    $ renpy.pause(0.5)
    show bg ch1afterback28 with hpunch
    "*Hombre desconocido*" "¡AHH!"
    show bg ch1afterback29 with dissolve
    "*Mujer encapuchada desconocida*" "Mucho mejor. Lo siento, solo una pequeña cosa de la que debía ocuparme. Me disculpo."
    "*Hombre desconocido*" "*Tose y jadea.*"
    "*Mujer encapuchada desconocida*" "¿Ahora qué?"
    if "ch1chandra" in extraevents:
        show bg ch1afterback6 with dissolve
        e "Cada vez que te doy un trabajo mi reputación entra en juego."
        e "Te vendo como el mejor Fantasma que conozco y la mitad de las veces ni siquiera aceptas el puto trabajo."
        e "¿Sabes cómo me hace ver eso?"
        menu:
            "Te da igual":
                p "Llegué unos minutos tarde. ¿Cuál es el problema?"
                call ch1afterbackangry from _call_ch1afterbackangry
            "Razona con ella":
                $ e_score += 1
                p "Mierdas que pasan. Lo sabes mejor que nadie. ¿Podemos proseguir?"
                p "Dame los detalles. Será mejor que no sea otro robo."
                e "Han pasado, ¿cuánto, dos meses desde tu último trabajo? Supongo que pagar las facturas hará que aceptes algo, eventualmente..."
            "Pide disculpas":
                p "Hola, lo siento, me he topado con alguien de camino aquí."
                e "No me importa. Somos profesionales y no me gusta que me hagan perder el tiempo."
                p "¡Relájate, Ellen! Solo fueron un par de minutos. ¿Cuál es el problema?"
                call ch1afterbackangry from _call_ch1afterbackangry_1
    else:
        $ e_score += 1
        show bg ch1afterback4 with dissolve
        e "Me alegro de que seas puntual, espero que lo conviertas en un hábito."
        p "Y espero que no me hayas traído para otro robo."
        show bg ch1afterback6 with dissolve
        e "Es lo que hay. No es mi culpa que seas tan exigente."
        e "Y los necesito. Tú sigues rechazando estos trabajos y eso nos perjudica a los dos."
        p "No voy a ir tras otro fugitivo que tiene problemas con su padre."
        show bg ch1afterback5 with dissolve
        e "Oh, conozco al padre en este caso. Te aseguro que no está involucrado. ¿Quieres verlo o no?"
        p "Muy bien, muéstramelo."
    show bg ch1afterback14 with dissolve

    e "Los detalles son limitados, pero sé algunas cosas."
    show bg ch1afterback15 with dissolve
    p "¿Una fuga? ¿Qué mierda, Ellen? Solo es una niña."
    e "Simplemente léelo. En serio... esto es personal."

    show bg ch1afterback16 with dissolve



    e "Aquí está la información. Anoche, un escuadrón de Fantasmas intentó detener a una mujer durante un espectáculo."
    e "El pánico fue absoluto. Nadie sabe qué pasó exactamente, pero cuando terminó, los tres Fantasmas estaban muertos y la niña no aparecía por ningún lado."
    p "¿Quién la ayudó?"
    e "No lo sé. Pero, mi suposición, es que por eso el cliente quiere que la traigan."
    p "Tremendo espectáculo."
    e "Sí, fue justo en el callejón."

    p "Entonces, Gloria Conner, ¿eh?"
    p "Veamos qué tenemos aquí."

    $ resetmenu()
    jump ch1padmenu



label ch1padmenu:
    menu:
        "¿Tech Noir?" if menu1 == True:
            $ menu1 = False
            p "¿El Tech Noir? Ese es el lugar en el que actúas, ¿verdad?"
            e "Ya no... no después del incidente. Así que eso me convierte en una contratista a tiempo completo."
            p "¿No puedes cantar en otro sitio?"
            e "Sabes que eso no va a pasar."
            jump ch1padmenu
        "¿Escuadrón de Fantasmas?" if menu2 == True:
            $ menu2 = False
            p "¿Un grupo de Fantasmas fuertemente armados entran y acaban muertos? ¿Cómo?"
            e "Ni idea... Yo estaba allí, pero una vez que los vi entrar me fui del escenario. Estaban bien preparados, [p]."
            p "¿Quiénes eran?"
            e "Bishop, Frost y Hudson."
            p "Bishop la iba a palmar tarde o temprano. Era un idiota. No me entristece verlo partir. Frost y Hudson, sin embargo, sabían lo que hacían."
            e "La pregunta es, ¿quién la ayudó?"
            p "Alguien astuto. Hudson era de primer nivel, incluso yo me preocuparía por si lo molestara. Llegó y provocó el pánico en el club. Su equipo tenía la ventaja. Quien sea que se haya librado de ellos, tiene que ser muy bueno."
            p "¿Sabes quién contrató a Hudson y su equipo?"
            e "No..."
            p "¿Qué pasa con el otro equipo en el atentado anterior? ¿Alguna idea?"
            e "Una vez más, ni idea."
            jump ch1padmenu
        "¿Es una Milcher?" if menu3 == True:
            $ menu3 = False
            p "SDG, entonces, ¿es una Milcher? No lo parece."
            e "No todos tienen escamas y colmillos, [p]. Ya lo sabes. Y no es que sea importante."
            e "Por cierto, la razón por la que sé que su padre no está pagando esto es porque se deshizo de ella justo después de que desarrollara los síntomas."
            p "Suena como un puto príncipe..."
            e "Más bien un rey. ¿Te diste cuenta del apellido?"
            p "¿Conner?"
            e "Como Alexis Conner."
            p "Eso explica que sea personal."
            e "Sí..."
            p "Lo personal nunca se mezcla bien con los negocios, Lane. ¿Por qué no dejarlo pasar?"
            e "No la he visto en años, pero... Gloria es una buena chica. O lo era, en aquel entonces."
            e "A su padre no le importa nada. Alguien debería cuidar de ella, al menos."
            e "Si alguien va a ir tras ella, prefiero que seas tú."
            p "Te lo agradezco, pero si es la mitad de imbécil que dices que es... que te involucres del todo puede hacer que tu lista negra sea permanente."
            e "Si me importara una mierda, no estaría aquí ahora mismo."
            jump ch1padmenu
        "Bien, con eso bastara.":
            p "¿Algo más?"
            e "Eso es todo."
            jump ch1afterback2

label ch1afterbackangry:
    show bg ch1afterback2 with dissolve
    e "¿El problema? [p], no has aceptado un trabajo en dos meses."
    e "Pierdo mi tiempo reuniéndome contigo cada vez que hacemos esto. ¡Lo tomas como un juego!"
    p "Tal vez aceptaría si no todos los trabajos fueran de robos."
    show bg ch1afterback3 with dissolve
    e "¡Oye, necesito que me paguen! El hecho de que quieras estar sobándote el culo todo el día no significa que yo pueda permitírmelo. ¿Crees que disfruto haciendo esta mierda?"
    e "Ahora solo céntrate en el trabajo. Confía en mí. Merece la pena, cabrón."
    p "Maldita sea. De acuerdo, ¡si con eso dejas de molestar!"
    return




label ch1afterback2:
    show bg ch1afterback17 with dissolve
    p "Por donde se le mire se ve que es una mala noticia."
    show bg ch1afterback18 with dissolve
    e "¿Cómo es eso?"
    p "¿Quién lo financia?"
    p "¿A dónde la llevo una vez que la encuentre?"
    p "Hay muchas preguntas sin respuesta aquí, Ellen."
    show bg ch1afterback19 with dissolve
    e "Siempre ha funcionado así. Vamos, por una vez acepta el trabajo."
    menu:
        "Ni hablar":
            p "De ninguna manera. Necesito más detalles. Lamento que esto sea personal para ti, pero no me fío."
            show bg ch1afterback20 with dissolve
            e "Mierda… necesito encontrar a alguien más apto."
            e "Vete a casa, [p]."
            p "No te pongas así."
            e "Vete a la mierda, vete..."
            jump ch1homealone
        "Tengo que pensarlo":

            p "Necesito pensar en ello."
            show bg ch1afterback20 with dissolve
            e "No lo pienses mucho. Ambos necesitamos la paga."
            p "Solo dame la noche. Déjame dormir."
            show bg ch1afterback7 with dissolve
            e "*Suspira* Te gusta hacer las cosas difíciles, ¿no?"
            show bg ch1afterback6 with dissolve
            e "De verdad te debe gustar mantenerme en suspenso."
            menu:
                "Así es más divertido":
                    $ e_score += 1
                    p "Es más divertido así. Me gusta verte sufrir."
                    e "Estoy segura de que sí."
                    p "Es lo que te gusta de mí."
                    show bg ch1afterback9 with dissolve
                    e "No te enorgullezcas tanto."
                    menu:
                        "Quizá pueda convencerme":
                            p "Tal vez, ¿necesito un poco de convencimiento?"
                            if e_score >= 2:
                                jump ch1afterconvince
                            else:
                                e "Esta noche no, [p]. No estoy de humor."
                                e "Notifícame tu decisión mañana."
                                p "Lo haré. Buenas noches, Ellen."
                                jump ch1homealone
                        "Debería irme":
                            p "Debería volver a casa."
                            show bg ch1afterback13 with dissolve
                            e "Avísame mañana, ¿de acuerdo?"
                            p "Lo haré. Buenas noches, Ellen."
                            jump ch1homealone
                "No es mi intención":


                    p "Solo necesito tiempo. Ya sabes cómo son las cosas."
                    e "Con el tiempo, lo superarás."
                    e "Probablemente deberías irte a casa. Hazme saber mañana lo que decidas."
                    p "Lo haré. Buenas noches, Ellen."
                    jump ch1homealone


        "Podría ser convencido" if e_score > 0:
            $ e_lust += 1
            jump ch1afterconvince

label ch1afterconvince:
    p "Siempre me vendría bien un cuerpo caliente a mi lado esta noche. Puedes ayudarme a decidir."
    show bg ch1afterback12 with dissolve
    e "Creo que eso puede arreglarse."
    show bg ch1afterback31 with dissolve
    e "Probablemente fue una de las razones por la que te llame esta noche, idiota."
    show bg ch1afterback33 with dissolve
    p "¿Fue ahora?"
    e "Siempre es lo mismo contigo."
    show bg ch1afterback32 with dissolve
    p "Es por eso que eres mi contratista. El último no tenía un cuerpo como el tuyo."
    show bg ch1afterback34 with dissolve
    e "El último fue un nativo americano de 300 libras llamado Hank."
    p "Como dije, no tenía un cuerpo como el tuyo. Sin embargo, me consiguió buenos trabajos."
    e "Ja ja. Púdrete, [p]."
    show bg ch1afterback35 with dissolve
    e "Ahora, necesitamos más tragos."
    show bg ch1afterback36 with dissolve
    e "Sígueme."
    show bg ch1afterback37 with dissolve
    e "¿Ahora qué?"
    p "Nada. Solo tú."
    show bg ch1afterback38 with dissolve
    e "Justo lo que quiero. Al grano."
    show bg ch1afterback40 with dissolve
    p "No hay razón para perder el tiempo con las bebidas."
    show bg ch1afterback39 with dissolve
    p "Tengo todo lo que quiero aquí."
    show bg ch1afterback41 with dissolve
    e "¿En tu casa?"
    p "Por supuesto."
    jump ch1ellen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
