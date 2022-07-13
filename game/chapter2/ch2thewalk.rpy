

image bg ch2walknight1 = "ch2walknight1"
image bg ch2walknight2 = "ch2walknight2"
image bg ch2walknight3 = "ch2walknight3"
image bg ch2walknight4 = "ch2walknight4"
image bg ch2walknight5 = "ch2walknight5"
image bg ch2walknight6 = "ch2walknight6"
image bg ch2walknight7 = "ch2walknight7"
image bg ch2walknight8 = "ch2walknight8"
image bg ch2walknight9 = "ch2walknight9"
image bg ch2walknight10 = "ch2walknight10"
image bg ch2walknight11 = "ch2walknight11"
image bg ch2walknight12 = "ch2walknight12"
image bg ch2walknight13 = "ch2walknight13"
image bg ch2walknight14 = "ch2walknight14"
image bg ch2walknight15 = "ch2walknight15"
image bg ch2walknight16 = "ch2walknight16"
image bg ch2walknight17 = "ch2walknight17"
image bg ch2walknight18 = "ch2walknight18"
image bg ch2walknight19 = "ch2walknight19"
image bg ch2walknight20 = "ch2walknight20"
image bg ch2walknight21 = "ch2walknight21"
image bg ch2walknight22 = "ch2walknight22"



label ch2thewalk:
    scene black with Dissolve(2)
    show text "{=trans}UNA HORA DESPUÉS, DE CAMINO AL CONDOMINIO DE ALEXIS CONNERS{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)


    if "ch2choosekatie" in extraevents:
        show bg ch2walknight9 with dissolve
        k "Espera... ¿vamos a ir al Hills Luxe?"
        p "Sí."
        k "¿Qué? ¿A quién conoces allí? ¿Los condominios allí valen por lo menos 50 millones de dólares?"
        p "Algo así... más dinero del que nunca veré. Nos dirigimos al ático."
        show bg ch2walknight10 with dissolve
        k "Ni hablar. Esto es demasiado."
        p "Oye, ¿qué pasa? Pensé que te gustaría una fiesta elegante."
        show bg ch2walknight11 with dissolve
        k "Sí. Pero hay lujo y luego está esto. Lo máximo a lo que he ido es a una gala de ex alumnos..."
        k "Me hare notar mucho."
        show bg ch2walknight12 with dissolve
        p "Ni siquiera lo pienses. Dada la opción, prefiero comer en el sitio coreano contigo que el puto caviar con cualquiera de ellos."
        k "¿Qué quieres decir eso?"
        p "¿Has hablado alguna vez con esta gente? Aburrimiento es un eufemismo."
        p "Y tú, en realidad eres una buena persona. Aquí, solo le pagan a la gente para que piensen que lo son."
        show bg ch2walknight13 with dissolve
        k "Gracias."
        p "¿Estamos bien?"
        k "Sí. Yo... eso me hace sentir un poco mejor."
        p "Bien, además, esto es trabajo. Mezclarse no está en la agenda."
        show bg ch2walknight14 with dissolve
        k "Aun así. Supongo que un poco de mezcla no sería tan malo."
        p "Lo dejaré en tus manos, entonces. ¿Vamos?"

    if "ch2chooseellen" in extraevents:
        show bg ch2walknight15 with dissolve
        e "Entonces, ¿a dónde diablos vamos?"
        p "Está más adelante."
        show bg ch2walknight16 with dissolve
        e "Sabes, la mayoría de la gente mataría por ir a una de estas cosas... Que estúpidos."
        e "Dame una fiesta en una casa en Lakewood cualquier día del..."
        p "¿Ellen?"
        show bg ch2walknight17 with dissolve
        e "¡Púdrete, [p]!"
        p "Sí, sé que lo odias, pero..."
        e "¿Por qué no me lo dijiste antes?"
        p "Porque dirías que no."
        e "¡Por supuesto que diría que no! ¡Ve tú solo o contrata a una prostituta! No me importa."
        show bg ch2walknight18 with dissolve
        p "¡Ellen, por favor!"
        e "Vete al carajo."
        p "Prácticamente has vivido allí durante un tiempo. Conoces el lugar."
        e "Y no quiero volver nunca más. Sabes lo que me hizo esa escoria."
        p "Sí, lo sé."
        e "*Solloza* Él... él me arruinó. Mi vida... mi carrera. ¡Todo se fue al carajo!"
        show bg ch2walknight19 with dissolve
        e "¡No me toques!"
        p "Mira, Ellen, yo..."
        show bg ch2walknight20 with dissolve
        e "Si dices \"lo siento,\" te daré una patada en los huevos."
        p "Ellen, mira, necesito tu ayuda. Lo conoces mejor que nadie. No quiere hablar de la chica, pero necesito algo para seguir adelante."
        p "No necesitas hablar con él. Es incluso mejor si no... No te lo pediría si no fuera importante."
        show bg ch2walknight22 with dissolve
        e "Bien, pero solo si me prometes que vas a cagar en su escritorio."
        p "¿Qué? ¡No!"
        e "Para ser un tipo duro… Te comerían vivo en el mundo del espectáculo. No me extraña que me necesites."
        p "¿Te {i}vas a{/i} cagar en su escritorio?"
        e "No sería lo peor que he hecho en una juerga, pero tengo una idea mejor."
        p "¿Entonces? ¿Vas a ir?"
        e "Sí, iré, Fantasma. Pero no esperes que me cuelgue de tu brazo."
        p "Gracias, Ellen."
        e "El favor que me vas a deber después de esto..."




    if "ch2choosevic" in extraevents:
        show bg ch2walknight1 with dissolve
        v "Entonces, asumo que tienes un plan."
        p "Esta noche no. En situaciones como esta, sigo mis instintos."
        show bg ch2walknight2 with dissolve
        v "En ese caso, déjame tomar la iniciativa. Fui hecha para {i}situaciones como esta.{/i}"
        if "ch1vic" in extraevents:

            p "También para otras cosas."
            show bg ch2walknight3 with dissolve
            v "No tienes pelos en la lengua, ¿verdad?"
            p "Contigo, no creo que tenga que hacerlo."
            show bg ch2walknight4 with dissolve
            v "Mmmm, estamos en público, [vicsexname]. Alguien podría vernos."
            p "Me da igual."
            show bg ch2walknight5 with dissolve
            v "Me deseas ahora mismo."
            p "No te hagas la tímida ahora. Sé cómo eres."
            show bg ch2walknight6 with dissolve
            v "Más tarde. Cuando hayamos terminado con Conner. Así podremos tomarnos el tiempo que queramos."
            p "Qué astuta."
            show bg ch2walknight7 with dissolve
            v "Además, he dejado algo especial en tu casa para nosotros esta noche."
            p "Algo que me gustará, espero."
            v "Te aseguro que \"gustar\", es una palabra muy pequeña."
            show bg ch2walknight8 with dissolve
            v "Date prisa, no queremos llegar tarde."
        else:
            p "Solo ten cuidado. No puedes ser tan rico y no ser un tiburón."
            v "Gracias por tu preocupación. Pero soy bastante capaz de manejarme a mí misma... y a cualquiera."
            show bg ch2walknight7 with dissolve
            p "Sin duda."
            v "Ahora, ¿vamos?"
            show bg ch2walknight8 with dissolve
            p "Vamos. No queremos llegar tarde."

    jump ch2elevator
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
