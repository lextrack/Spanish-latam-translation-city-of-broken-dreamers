
image bg ch2before1 = "ch2before1"
image bg ch2before2 = "ch2before2"
image bg ch2before3 = "ch2before3"
image bg ch2before4 = "ch2before4"
image bg ch2before5 = "ch2before5"

image bg ch2before7 = "ch2before7"
image bg ch2before8 = "ch2before8"
image bg ch2before9 = "ch2before9"
image bg ch2before10 = "ch2before10"
image bg ch2before11 = "ch2before11"
image bg ch2before12 = "ch2before12"
image bg ch2before13 = "ch2before13"
image bg ch2before14 = "ch2before14"
image bg ch2before15 = "ch2before15"
image bg ch2before16 = "ch2before16"
image bg ch2before17 = "ch2before17"
image bg ch2before18 = "ch2before18"
image bg ch2before19 = "ch2before19"


image ch2beforekatiemov = Movie(play='video/chapter-2-video/ch2beforekatie.webm', loop=False)
image bg ch2beforekatiemovie movie:
    "ch2beforekatiemov"
    pause 7.3
    "ch2beforekatieend"

image ch2beforevicmov = Movie(play='video/chapter-2-video/ch2beforevic.webm', loop=False)
image bg ch2beforevicmovie movie:
    "ch2beforevicmov"
    pause 7
    "ch2beforevicend"

image ch2beforeellenmov = Movie(play='video/chapter-2-video/ch2beforeellen.webm', loop=False)
image bg ch2beforeellenmovie movie:
    "ch2beforeellenmov"
    pause 7
    "ch2beforeellenend"

label ch2before:
    scene black with Dissolve(2)
    show text "{=trans}UNA HORA DESPUÉS{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    n "Se oye un ligero golpe en la puerta."
    show bg ch2before1 with Dissolve(2)
    p "Oye, pasa."
    show bg ch2before2 with dissolve
    n "La puerta se abre con un suave chirrido."

    if "ch2choosekatie" in extraevents:
        window hide
        show bg ch2beforekatiemovie movie with dissolve
        $ renpy.pause()
        window show
        p "Doc, te ves... Te ves muy bien."
        k "Gracias, temía que no encajara. La cosa estaba enterrada en el fondo de mi armario en una caja. Nunca tengo una razón para usarlo."
        p "Es una pena. Te vistes muy bien."
        show bg ch2before4 with dissolve
        k "Oye, déjate de halagos, que me vas a hacer sonrojar."
        show bg ch2before3 with dissolve
        k "A menos que estés jugando. No te estás metiendo conmigo otra vez, ¿verdad?"
        p "Tal vez más tarde, pero no ahora. Te ves muy bien."
        show bg ch2before5 with dissolve
        k "Sí, pero, con toda la gente que hay allí, ¿no crees que esto es demasiado sencillo? Quiero decir, ¿encajaré?"
        p "Estarás bien, Katie."
        show bg ch2before7 with dissolve
        p "Pero vamos, tenemos que irnos."
        show bg ch2before8 with dissolve
        k "Me alegro de que me hayas dicho que esto no era una cita porque, en realidad, se siente como una cita."
        jump ch2thewalk

    if "ch2choosevic" in extraevents:
        show bg ch2before10 with dissolve
        v "¿Estás preparado, agente?"
        p "Solo necesito arreglar mi collar y estamos bien."
        show bg ch2before9 with dissolve
        v "He conseguido un vestido nuevo para la ocasión. Creo que me queda bien."
        v "¿Estás de acuerdo?"
        p "..."
        window hide
        show bg ch2beforevicmovie movie with dissolve
        $ renpy.pause()
        window show
        p "Vaya... sí... Ahora siento que voy yo mal vestido."
        v "Has elegido bien. Tu traje aburrido no llamará la atención y eso es exactamente lo que necesitamos."
        p "Especialmente con todos los ojos puestos en ti."
        show bg ch2before11 with dissolve
        v "Esa es la intención… Cuanta más atención tenga yo, menos tendrás tú."
        p "El equipo perfecto."
        v "Totalmente."
        if v_score >= 0:
            p "Con ese aspecto, dudo que Conner sea capaz de mantener sus ojos o, joder, sus manos fuera de ti."
            show bg ch2before12 with dissolve
            v "A pesar de lo que pueda pensar, ese no es el plan. Verás que puedo mantenerlo entretenido con una conversación agradable, no más que eso."
        show bg ch2before13 with dissolve
        v "¿Vamos?"
        p "(No se equivoca. Nadie se va a fijar en mí con ella cerca.)"
        show bg ch2before14 with dissolve
        v "Tenemos un horario. Si quieres mirar fijamente, entonces mira fijamente en el camino."
        p "Perdón, voy justo detrás de ti."
        jump ch2thewalk

    if "ch2chooseellen" in extraevents:

        window hide
        show bg ch2beforeellenmovie movie with dissolve
        $ renpy.pause()
        window show
        p "¡La virgen puta!"
        e "Cállate."
        p "Es que te he visto de muchas maneras, pero nunca con un vestido así."
        e "Bueno, disfrútalo, porque no volverá a suceder."
        show bg ch2before16 with dissolve
        e "*Gime de disgusto* Es incómodo que te cagas. Parezco una prostituta con esta mierda."
        p "Te ves muy bien, Ellen."
        show bg ch2before15 with dissolve
        e "Solo lo dices para que me sienta mejor."
        p "¡Vete a la mierda! ¿Cuándo te he alagado yo falsamente? Como si necesitaras un AUMENTO de ego en primer lugar."
        show bg ch2before17 with dissolve
        e "¡Oh, púdrete! No me hable de ego, Sr. \"Demasiado bueno para el trabajo normal.\""
        p "¿Por qué te tengo que soportar siempre?"
        show bg ch2before18 with dissolve
        e "Todos los demás contratistas odian tu quisquilloso culo. Soy la única que trata contigo."
        p "Tú eres buena en la cama."
        e "Sí, sí, desde luego."
        p "¿Lista para salir?"
        show bg ch2before19 with dissolve
        e "Mierda, por supuesto. ¿Algo que deba saber sobre la multitud?"
        p "¿La multitud? Uh... no. Solo los típicos imbéciles ricos."
        e "Bueno, vamos a enseñarles cómo se festeja."
        p "Y no olvides que esto es negocio."
        e "Que te den, [p]. Me metiste en este maldito vestido, me divertiré mientras trabajas."
        jump ch2thewalk
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
