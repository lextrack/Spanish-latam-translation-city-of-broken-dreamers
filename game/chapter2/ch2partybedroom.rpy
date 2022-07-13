image bg ch2bedroom1 = "ch2bedroom1"
image bg ch2bedroom2 = "ch2bedroom2"
image bg ch2bedroom3 = "ch2bedroom3"
image bg ch2bedroom4 = "ch2bedroom4"
image bg ch2bedroom5 = "ch2bedroom5"
image bg ch2bedroom6 = "ch2bedroom6"
image bg ch2bedroom7 = "ch2bedroom7"
image bg ch2bedroom8 = "ch2bedroom8"
image bg ch2bedroom9 = "ch2bedroom9"
image bg ch2bedroom10 = "ch2bedroom10"
image bg ch2bedroom11 = "ch2bedroom11"
image bg ch2bedroom12 = "ch2bedroom12"
image bg ch2bedroom13 = "ch2bedroom13"
image bg ch2bedroom14 = "ch2bedroom14"
image bg ch2bedroom15 = "ch2bedroom15"
image bg ch2bedroom16 = "ch2bedroom16"
image bg ch2bedroom17 = "ch2bedroom17"
image bg ch2bedroom18 = "ch2bedroom18"
image bg ch2bedroom19 = "ch2bedroom19"
image bg ch2bedroom20 = "ch2bedroom20"
image bg ch2bedroom21 = "ch2bedroom21"
image bg ch2bedroom22 = "ch2bedroom22"
image bg ch2bedroom23 = "ch2bedroom23"
image bg ch2bedroom24 = "ch2bedroom24"
image bg ch2bedroom25 = "ch2bedroom25"
image bg ch2bedroom26 = "ch2bedroom26"
image bg ch2bedroom27 = "ch2bedroom27"
image bg ch2bedroom28 = "ch2bedroom28"

image bg ch2shower1 = "ch2shower1"
image bg ch2shower2 = "ch2shower2"
image bg ch2shower3 = "ch2shower3"
image bg ch2shower4 = "ch2shower4"
image bg ch2shower5 = "ch2shower5"
image bg ch2shower6 = "ch2shower6"
image bg ch2shower7 = "ch2shower7"
image bg ch2shower8 = "ch2shower8"
image bg ch2shower9 = "ch2shower9"
image bg ch2shower10 = "ch2shower10"
image bg ch2shower11 = "ch2shower11"
image bg ch2shower12 = "ch2shower12"
image bg ch2shower13 = "ch2shower13"


label ch2partybedroom:

    if "ch2choosekatie" in extraevents:
        show bg ch2bedroom8 with dissolve
        p "No se ha manipulado nada de esta habitación."
        show bg ch2bedroom9 with dissolve
        k "¿Tal vez significa que una parte de él quiere que ella vuelva?"
        show bg ch2bedroom10 with dissolve
        p "Oye, ¿ves ese poster? Es mi amiga Ellen."
        k "¿Tu contratista es Ellen Lane? Siempre me he preguntado qué pasó con ella, simplemente desapareció."
        show bg ch2bedroom12 with dissolve
        p "Sí, es una larga historia. Venga, vamos a ver."
        k "¿Y qué buscamos exactamente?"
        show bg ch2bedroom11 with dissolve
        p "Cualquier cosa, algo que pueda ser una pista de dónde puede haber ido."
        show bg ch2bedroom13 with dissolve
        k "Tengo que decir que era adorable cuando era una niña. Mira esto y dime que no te produce ternura."
        p "¿Quién demonios es ese?"
        k "Es ella."
        show bg ch2bedroom14 with dissolve
        p "Ella no, ese monstruo sobre el que está sentada. Ese tipo tiene que medir dos metros por lo menos."
        show bg ch2bedroom15 with dissolve
        k "No lo sé, pero parece agradable."
        p "Si es quien creo que es... no estaría tan seguro."
        show bg ch2bedroom16 with dissolve
        k "Supongo, pero parece muy feliz en esa foto. Me recuerda a cuando jugaba con mi padre."
        p "Venga, vamos. Ya hemos tardado demasiado. Lo último que necesitamos es que nos atrapen aquí."
        scene black with dissolve
        n "Después de unos minutos revisando la habitación"
        p "¿Ves algo?"
        show bg ch2partyhallway10 with dissolve
        k "Escuché algo en el pasillo."
        show bg ch2partyhallway11 with dissolve
        k "¡Oh! Alguien viene."
        p "Rápido, sígueme."
        scene black with dissolve
        show bg ch2shower13 with dissolve
        p "Escóndete detrás de la esquina."
        k "¡Pero, [p]!"
        p "¡Ahora!"
        show bg ch2shower12 with dissolve
        p "¡Shhhh!"
        k "..."
        show bg ch2shower3 with dissolve
        n "Se oyen voces que se aproximan"
        sh "¡Mi puto vestido, Alexis! ¡Esa maldita bastarda!"
        a "Podemos comprarte un vestido nuevo."
        sh "El dinero es la respuesta a todo, ¿no?"
        a "Responde a muchas cosas. Y no veo que te quejes de nuestra situación."
        sh "¿Por qué? Estoy saliendo con el hombre más poderoso de la ciudad, supuestamente."
        a "¿Supuestamente?"
        sh "Sin tu dinero... todo ese poder no existiría. Te estarías vendiendo en las calles de Lakewood."
        a "Voy a fingir que no he oído eso."
        sh "Ni siquiera lo niegas. Bien, vete a dormir al sofá, marica. No quiero verte hasta que vuelvas de tu viaje."
        n "La puerta se cierra de golpe"
        show bg ch2shower2 with dissolve
        $ renpy.pause(1)
        show bg ch2shower1 with dissolve
        k "*En voz baja* ¡[p]! ¿Qué está pasando?"
        play sound audio.shower loop fadein 2.0
        k "¿Se está duchando?"
        show bg ch2shower5 with dissolve
        $ renpy.pause(2)
        show bg ch2shower6 with Dissolve(2)
        p "Ahh, sí."
        show bg ch2shower7 with dissolve
        sh "Alexis no puedes ni siquiera enfrentarte a mí..."
        show bg ch2shower8 with dissolve
        sh "Si fueras siquiera la mitad de... mmmm..."
        sh "Ohhh... sí..."
        show bg ch2shower9 with dissolve
        sh "Mmm, házmelo... Mete esas manos... Mmmm..."
        show bg ch2shower10 with dissolve
        k "*Deja escapar una risita*"
        p "Shh..."
        k "*Intenta contener la risa*"
        show bg ch2shower11 with hpunch
        p "Bien, nos vamos ahora mismo."
        k "¡Uh, eh!"
        stop sound fadeout 2.0
        jump ch2after



    if "ch2chooseellen" in extraevents:
        show bg ch2bedroom17 with dissolve
        p "Ellen, aquí estás."
        e "*Sollozando* Oye... ¿Has encontrado algo?"
        show bg ch2bedroom18 with dissolve
        $ renpy.pause(1)
        show bg ch2bedroom19 with dissolve
        p "No mucho. Shanlon, quiere que vaya mañana. Algún tipo de propuesta."
        e "No confíes en esa perra. Créeme."
        p "No tenía previsto hacerlo."
        show bg ch2bedroom20 with dissolve
        e "Dios, no confíes en nadie aquí."
        menu:
            "Pregúntale si esta todo bien":
                p "Ellen, ¿te encuentras bien?"
                show bg ch2bedroom22 with dissolve
                e "Por supuesto que lo estoy, imbécil. Soy Ellen Lane."
                p "Ellen..."
                e "Ya déjalo..."
            "Déjala un momento":
                $ e_score += 1
                e "Entonces, ¿qué esperas?"
                show bg ch2bedroom21 with dissolve
                p "Estaba mirando por ahí. ¿Encontraste algo?"
                e "No, ni siquiera sé qué buscar."

        show bg ch2bedroom24 with dissolve
        e "Oye, [p], mira esto. Gloria era realmente una belleza en ese entonces."
        p "¿La conoces?"
        show bg ch2bedroom25 with dissolve
        e "Quiero decir... más o menos. Pasaba más tiempo con su madre por aquel entonces, pero fue la primera niña que me impresionaba."
        p "¿Se impresionaba?"

        e "Helena la trajo a los bastidores después de un show, justo antes de que yo me hiciera conocida."
        show bg ch2bedroom27 with dissolve
        e "En ese momento pensaba que lo había hecho todo mal, pero aparece esta niña... y se me queda mirando como si yo fuera la cosa más genial que hubiera visto nunca."
        p "Una gran inyección de ego."
        show bg ch2bedroom26 with dissolve
        e "No me digas. Ella era muy fanática. Probablemente yo avivé un poco la cosa. Soy un pedazo de mierda a veces."
        p "¿Quién es el grandote?"
        show bg ch2bedroom28 with dissolve
        e "Ese es Henry, era su guardaespaldas. Vino después de la muerte de Helena... los dos eran casi inseparables."
        p "Espera, ¿sabías de esto y nunca mencionaste que podría ser una maldita máquina matar?"
        e "No lo mencioné porque el tipo se suicidó hace unos años."
        e "Pero no me sorprendió. Henry era uno de esos Augment de la guerra. Duró más que la mayoría."
        p "Sí, las consecuencias psicológicas fueron duras."
        e "La vida es un asco, luego te mueres."
        show bg ch2bedroom23 with dissolve
        e "Bueno, mierda, esto se puso morboso rápidamente. Necesito que me animen. ¿Quieres ir a robar algo de la oficina del gran imbécil."
        p "Sí, venga, vamos."
        jump ch2partyellen


    if "ch2choosevic" in extraevents:
        show bg ch2bedroom1 with dissolve
        p "(Su dormitorio no ha sido manipulado...)"
        show bg ch2bedroom2 with dissolve
        p "(Bien, echemos un vistazo.)"
        show bg ch2bedroom3 with dissolve
        p "(Ni siquiera sé lo que estoy buscando.)"
        show bg ch2bedroom4 with dissolve
        p "Hmm... Linda chica. ¿Quién diablos es esa bestia?"
        v "Está muerto."
        show bg ch2bedroom5 with hpunch
        p "Mierda, qué susto me has dado."
        v "Mis disculpas, has estado ausente durante bastante tiempo, así que pensé que te vendría bien mi ayuda."
        p "¿Y Conner?"
        show bg ch2bedroom6 with dissolve
        v "En el jacuzzi. Soñando con un día en el que me convierta en una de sus actrices."
        p "¿No eres una cantante?"
        v "Tengo muchos talentos. El canto no está entre ellos. ¿Has encontrado algo?"
        p "Tal vez. Shanlon dice que tiene algo. Me reuniré con ella mañana."
        show bg ch2bedroom7 with dissolve
        v "Muy bien, buen trabajo agente. Puede que no sea mucho, pero creo que hemos agotado este recurso. Creo que es hora de que nos vayamos."
        jump ch2after
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
