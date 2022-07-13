

image bg ch2station0 = "ch2miltown41"
image bg ch2station1 = "ch2station01"
image bg ch2station2 = "ch2station02"
image bg ch2station3 = "ch2station03"
image bg ch2station4 = "ch2station04"
image bg ch2station5 = "ch2station05"
image bg ch2station6 = "ch2station06"
image bg ch2station7 = "ch2station07"
image bg ch2station8 = "ch2station08"
image bg ch2station9 = "ch2station09"
image bg ch2station10 = "ch2station10"
image bg ch2station11 = "ch2station11"
image bg ch2station12 = "ch2station12"
image bg ch2station13 = "ch2station13"
image bg ch2station14 = "ch2station14"
image bg ch2station15 = "ch2station15"
image bg ch2station16 = "ch2station16"
image bg ch2station17 = "ch2station17"
image bg ch2station18 = "ch2station18"
image bg ch2station19 = "ch2station19"
image bg ch2station20 = "ch2station20"
image bg ch2station21 = "ch2station21"
image bg ch2station22 = "ch2station22"
image bg ch2station23 = "ch2station23"
image bg ch2station24 = "ch2station24"



image ch2stationpan = Movie(play='video/chapter-2-video/ch2stationpan.webm', loop=False)
image bg ch2stationpan movie:
    "ch2stationpan"
    pause 6.38
    "ch2stationpan-end"



label ch2miltownstationinside:
    scene black with dissolve
    play music audio.calmmorning fadein 2.0 fadeout 2.0



    show bg ch2station0 with dissolve
    if not persistent.ch2card1:
        $ renpy.notify(['Posible pista', 'alert'])
        show screen hidden_item("ch2card1", "ch2card1", 424, 177, 242, 311)
    "*Huele a humedad, lo que habla de una batalla perdida entre el moho y los productos de limpieza. En una antigua televisión situada en la pared más alejada se emite un reportaje.*"
    hide screen hidden_item
    show bg ch2station1 with dissolve
    k "Se ve peor aquí que afuera."
    p "Bueno, Lakewood no recibe ninguna financiación. Funciona para nosotros, aunque no para muchos policías en este momento."
    k "¿Es un problema?"
    p "No es un problema, per se. La cuestión es que puedo tener autorización, pero eso no significa que pueda ir a mis anchas por donde yo quiera."
    show bg ch2station2 with dissolve
    k "Espera. ¿Esto es ilegal?"
    k "No quiero que me arresten por tu culpa, [p]."
    p "Doc, relájate. No te habría traído si pensara que te ibas a meter en algún problema."
    show bg ch2station3 with dissolve
    k "Tú necesitas un historial limpio para seguir operando. No es que la junta de licencias necesite mucha excusa para cerrar una clínica independiente."
    p "Has hecho trabajos más turbios que este. Tienes que hacerlo."
    k "Esos trabajos \"turbios\" te mantiene vivo a ti y a tus compañeros. Y no implica allanamiento de morada. Pensé que solo íbamos al centro."
    menu:
        "Pide disculpas":
            $ k_score += 1
            p "Tienes razón, debería haberte hecho saber lo que implicaría. Katie, discúlpame."
            k "Es doctora Hamilton. Demasiado tarde para echarse atrás. Solo lidera el camino, amigo."
        "Dile que todo va a estar bien":
            p "Si pasa algo solo di que te obligué a hacerlo. Nadie lo sabrá. En el peor de los casos, te darán un tirón de orejas."
            k "No lo entiendes, ¿verdad? A la mierda, terminemos con esto."
    p "Bien, un segundo."
    show bg ch2station4 with dissolve
    p "Bien, un segundo."
    s "Ahora mismo, señor."
    show bg ch2station5 with dissolve
    s "El acceso ha sido denegado, señor."
    p "Mierda. ¿Puedes darme una razón al menos?"
    s "Parece que su autorización ha sido revocada en este lugar."
    p "Eso fue rápido. Vostok está atento al perecer."
    p "(Si no entro a ver los cadáveres, lo más probable es que desaparezcan en una hora.)"
    show bg ch2station6 with dissolve
    "Presentadora de noticias" "Una vez que controlemos la propagación del SDG, todos, afligidos y gente normal, dormirán más tranquilos."
    "Guardia" "Maldición, mírate."
    show bg ch2station7 with dissolve
    "Guardia" "Podría mirar esas delicias todo el día."
    p "Psst, Doc, ven aquí. Te necesito."
    show bg ch2station8 with dissolve
    k "¿Ahora qué?"
    p "¿Ves ese sujeto? Necesito que lo mantengas ocupado durante unos minutos."
    show bg ch2station9 with dissolve
    k "¿Qué? No. Yo... ¿cómo se supone que voy a mantenerlo ocupado?"
    p "Habla con él un rato. Ha estado sentado solo durante horas."
    k "No sé. No soy buena en las conversaciones improvisadas."
    p "Hablas muy bien conmigo."
    k "Por lo general, estamos hablando de la bala que estoy sacando de tu hombro."
    p "Y tú eres genial en eso. Solo habla con él sobre... No sé... cualquier cosa. Pregunta direcciones, lo que sea."
    p "Solo un par de minutos. Es todo lo que necesito."
    window hide
    show bg ch2stationpan movie with dissolve
    $ renpy.pause()
    window show
    k "¿Solo hablar? Bien. *Suspira* Me debes una."
    p "Eres la mejor, Doc."
    show bg ch2station10 with dissolve
    k "¿Hola? ¿Hay alguien ahí?"
    show bg ch2station11 with dissolve
    "Guardia" "*Gruñidos de disgusto por ser interrumpido* Justo en medio de... ¡un segundo!"
    show bg ch2station12 with dissolve
    "Guardia" "¿Quién es usted, señorita, y qué quiere?"
    show bg ch2station13 with dissolve
    k "Bueno, umm, yo estaba... Hola..."
    "Guardia" "Más alto, señorita, apenas puedo oírla."
    show bg ch2station14 with dissolve
    k "Esperaba conseguir algo de ayuda. Estoy buscando la oficina del Jefe."
    "Guardia" "¿Oficina del jefe? ¿Aquí? ¿Segura de que estás en la estación correcta? Dios, ya ni siquiera tenemos un capitán."
    k "Oh... ¿entonces quién está a cargo?"
    "Guardia" "Bueno, lo estoy ahora mismo. ¿Qué hace un bombón como tú aquí en Mil-town? ¿Te has perdido?"
    show bg ch2station15 with dissolve
    k "¿Perdón? ¿bombón?"
    "Guardia" "Me apunto si necesitas una escolta policial. No queremos que ningún puto Milcher te agarre ahora, ¿verdad?"
    show bg ch2station17 with dissolve
    "Guardia" "No creerás la mierda que les he visto hacer a las chicas."
    show bg ch2station16 with dissolve
    k "*Jadea* ¡Qué! ¡Esto es totalmente inapropiado!"
    "Guardia" "Como sea..."
    n "El guardia pone los ojos en blanco y regresa al televisor"
    show bg ch2station19 with dissolve
    k "[p], ¿puedes creerle a ese hombre?"
    p "¡Shhh!"
    show bg ch2station18 with dissolve
    k "¡No me hagas callar! ¡Ese hombre era asqueroso!"
    p "¿Qué pasó?"
    show bg ch2station20 with dissolve
    k "Me trató como a un pedazo de carne, ¡me comió con los ojos todo el tiempo! Además, es un intolerante."
    p "Katie, cálmate. Lo hiciste bien. Tengo la puerta abierta. Ahora solo tenemos que pasar a escondidas."
    show bg ch2station22 with dissolve
    k "Todo es sobre ti. Dios, eres igual que mi padre."
    show bg ch2station21 with dissolve
    p "Espero que eso sea un cumplido. Vamos."
    show bg ch2station23 with dissolve
    p "Quédate tranquila, estoy detrás de ti."
    show bg ch2station24 with dissolve
    k "*Susurra en voz baja* Hoy debería haber dormido hasta tarde."
    jump ch2thedead
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
