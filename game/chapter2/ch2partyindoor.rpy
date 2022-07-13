image bg ch2partyindoor1 = "ch2partyindoor1"
image bg ch2partyindoor2 = "ch2partyindoor2"
image bg ch2partyindoor3 = "ch2partyindoor3"
image bg ch2partyindoor4 = "ch2partyindoor4"
image bg ch2partyindoor5 = "ch2partyindoor5"
image bg ch2partyindoor6 = "ch2partyindoor6"
image bg ch2partyindoor7 = "ch2partyindoor7"
image bg ch2partyindoor8 = "ch2partyindoor8"
image bg ch2partyindoor9 = "ch2partyindoor9"
image bg ch2partyindoor10 = "ch2partyindoor10"
image bg ch2partyindoor11 = "ch2partyindoor11"
image bg ch2partyindoor12 = "ch2partyindoor12"
image bg ch2partyindoor13 = "ch2partyindoor13"
image bg ch2partyindoor14 = "ch2partyindoor14"
image bg ch2partyindoor15 = "ch2partyindoor15"
image bg ch2partyindoor16 = "ch2partyindoor16"
image bg ch2partyindoor17 = "ch2partyindoor17"
image bg ch2partyindoor18 = "ch2partyindoor18"
image bg ch2partyindoor19 = "ch2partyindoor19"
image bg ch2partyindoor20 = "ch2partyindoor20"
image bg ch2partyindoor21 = "ch2partyindoor21"
image bg ch2partyindoor22 = "ch2partyindoor22"
image bg ch2partyindoor23 = "ch2partyindoor23"
image bg ch2partyindoor24 = "ch2partyindoor24"
image bg ch2partyindoor25 = "ch2partyindoor25"
image bg ch2partyindoor26 = "ch2partyindoor26"
image bg ch2partyindoor27 = "ch2partyindoor27"
image bg ch2partyindoor28 = "ch2partyindoor28"
image bg ch2partyindoor29 = "ch2partyindoor29"
image bg ch2partyindoor30 = "ch2partyindoor30"
image bg ch2partyindoor31 = "ch2partyindoor31"
image bg ch2partyindoor32 = "ch2partyindoor32"
image bg ch2partyindoor33 = "ch2partyindoor33"
image bg ch2partyindoor34 = "ch2partyindoor34"
image bg ch2partyindoor35 = "ch2partyindoor35"
image bg ch2partyindoor36 = "ch2partyindoor36"
image bg ch2partyindoor37 = "ch2partyindoor37"
image bg ch2partyindoor38 = "ch2partyindoor38"
image bg ch2partyindoor39 = "ch2partyindoor39"
image bg ch2partyindoor40 = "ch2partyindoor40"
image bg ch2partyindoor41 = "ch2partyindoor41"
image bg ch2partyindoor42 = "ch2partyindoor42"
image bg ch2partyindoor43 = "ch2partyindoor43"
image bg ch2partyindoor44 = "ch2partyindoor44"
image bg ch2partyindoor45 = "ch2partyindoor45"
image bg ch2partyindoor46 = "ch2partyindoor46"
image bg ch2partyindoor47 = "ch2partyindoor47"
image bg ch2partyindoor48 = "ch2partyindoor48"
image bg ch2partyindoor49 = "ch2partyindoor49"
image bg ch2partyindoor50 = "ch2partyindoor50"
image bg ch2partyindoor51 = "ch2partyindoor51"
image bg ch2partyindoor52 = "ch2partyindoor52"
image bg ch2partyindoor53 = "ch2partyindoor53"
image bg ch2partyindoor54 = "ch2partyindoor54"
image bg ch2partyindoor55 = "ch2partyindoor55"
image bg ch2partyindoor56 = "ch2partyindoor56"
image bg ch2partyindoor57 = "ch2partyindoor57"
image bg ch2partyindoor58 = "ch2partyindoor58"
image bg ch2partyindoor59 = "ch2partyindoor59"
image bg ch2partyindoor60 = "ch2partyindoor60"

image bg ch2partyindoor61 = "ch2partyindoor61"
image bg ch2partyindoor62 = "ch2partyindoor62"
image bg ch2partyindoor63 = "ch2partyindoor63"
image bg ch2partyindoor64 = "ch2partyindoor64"
image bg ch2partyindoor65 = "ch2partyindoor65"
image bg ch2partyindoor66 = "ch2partyindoor66"
image bg ch2partyindoor67 = "ch2partyindoor67"
image bg ch2partyindoor68 = "ch2partyindoor68"
image bg ch2partyindoor69 = "ch2partyindoor69"
image bg ch2partyindoor70 = "ch2partyindoor70"

image bg ch2partyindoor71 = "ch2partyindoor71"
image bg ch2partyindoor72 = "ch2partyindoor72"
image bg ch2partyindoor73 = "ch2partyindoor73"
image bg ch2partyindoor74 = "ch2partyindoor74"
image bg ch2partyindoor75 = "ch2partyindoor75"
image bg ch2partyindoor76 = "ch2partyindoor76"
image bg ch2partyindoor77 = "ch2partyindoor77"
image bg ch2partyindoor78 = "ch2partyindoor78"
image bg ch2partyindoor79 = "ch2partyindoor79"
image bg ch2partyindoor80 = "ch2partyindoor80"
image bg ch2partyindoor81 = "ch2partyindoor81"


label ch2partyindoor:
    $ renpy.music.set_volume(1, 1, 'music')
    scene black with Dissolve(1)
    show bg ch2partyindoor1 with dissolve
    "Mujer desconocida" "Bienvenido. Diviértete."
    p "(Qué demonios.) De nuevo, gracias."
    show bg ch2partyindoor2 with dissolve
    "Mujer desconocida" "¿Quieres compañía? Sígueme."
    p "Ugh, ¿qué?"
    show bg ch2partyindoor3 with dissolve
    p "(Ahí está. Supongo que ese es el famoso vestido o uno de ellos, al menos.)"
    show bg ch2partyindoor4 with dissolve
    p "(Y ahí está el rey del castillo.)"
    p "(Sabe cómo montar un espectáculo, lo reconozco.)"
    show bg ch2partyindoor5 with dissolve
    n "La mujer del bikini se desliza por la mesa mientras Alexis y Shanlon la observan. En la sala abundan pequeñas discusiones inaudibles, ahogadas por la música circundante."

    if "ch2choosekatie" in extraevents:
        k "¡Espera! ¿Es quien creo que es?"
        p "Sí, es ella."
        show bg ch2partyindoor12 with dissolve
        k "¿Me invitaste a {i}su{/i} fiesta?"
        p "Bueno, técnicamente es la fiesta de su novio."
        show bg ch2partyindoor13 with dissolve
        k "¡[p]!"
        p "No es un gran problema, Katie. Al menos ahora sabes que hablé en serio sobre lo de ir al coreano contigo."
        show bg ch2partyindoor11 with dissolve
        k "Necesito un trago. Sí, un trago. Toda esta gente en todas partes. Y la loca de las noticias también. Perfecto."
        p "Katie, respira. Estarás bien. Vamos."
        menu:
            "Ve a sentarte":
                p "¿Qué tal si nos sentamos? Dejemos que asimiles las cosas un poco."
                k "Sí, por favor. Necesito acostumbrarme a esto."
                jump ch2partykatiesit
            "Acércate a Alexis y Shanlon":

                p "Puedo ver que estás incómoda. Déjame ir a hablar con ellos y terminar con esto."
                k "Adelante. Hay un asiento junto a la barra con mi nombre. Y un trago también."
                p "Bueno, pero no te pierdas."
                jump ch2partykatiealex


    if "ch2chooseellen" in extraevents:
        e "Mierda... ha pasado mucho tiempo."
        p "Mantén la calma, Ellen."
        show bg ch2partyindoor6 with dissolve
        e "Míralos a todos. Demasiado preocupados por su aspecto como para pasar un buen rato. Para alguien como Conner, incluso su diversión es calculada. Me da un poco de pena."
        p "¿En serio?"
        show bg ch2partyindoor8 with dissolve
        e "¡Carajo, no! Espero que se emborrache y se tire por la ventana. Eso me alegraría."
        p "¡Oye, espera! ¿A dónde vas?"
        show bg ch2partyindoor7 with dissolve
        e "¡Mira a tu alrededor! Quieres hablar con él, ¡eso es todo!"
        e "Quizá deberías aceptar la oferta de esa mujer."
        p "(¿Ahora qué?)"
        menu:
            "Ve a sentarte":
                p "(Deberíamos conocer el terreno primero. También tengo curiosidad por esa chica. Quién sabe lo que está haciendo.)"
                jump ch2partyellensit
            "Ve a hablar con Alexis y Shanlon":
                p "(Acabemos con esto.)"
                jump ch2partyellenalex

    if "ch2choosevic" in extraevents:
        v "Bonito vestido, aunque un poco desabrido en la parte delantera."
        p "Me gusta un poco."
        show bg ch2partyindoor9 with dissolve
        v "Y uno de nosotros se encarga de estar perfectamente a la moda en todo momento. Y uno de nosotros es un Fantasma."
        p "Entonces, ¿cuál es el plan?"
        v "Depende de ti. Podemos tomarnos nuestro tiempo o puedo alejarlo de ella por unos minutos."
        menu:
            "Sentémonos un momento":
                p "¿Por qué no nos sentamos?"
                show bg ch2partyindoor10 with dissolve
                v "Muy bien, agente, sígueme."
                jump ch2partyvicsit
            "Terminemos con esto":
                show bg ch2partyindoor10 with dissolve
                v "Muy bien, agente, déjeme empezar."
                jump ch2partyvicalex





label ch2partykatiesit:
    $ extraevents.append("vostokdoc")
    p "Vamos, por aquí."
    show bg ch2partyindoor14 with dissolve
    p "Creo que le gustas."
    k "Muy gracioso..."
    show bg ch2partyindoor15 with dissolve
    k "Esto es demasiado. Quiero decir, aprecio esto. Fue agradable. Pero, sí..."
    p "Bueno, espero que no tengamos que estar aquí mucho tiempo. Solo quería agradecerte tu ayuda."
    show bg ch2partyindoor16 with dissolve
    k "Sí, todo el día ha sido una aventura. Simplemente no encajo con..."
    show bg ch2partyindoor17 with hpunch
    k "¡AHH!"
    p "¿Qué pasa?"
    "Mujer desconocida" "Te deseo."
    show bg ch2partyindoor19 with dissolve
    p "¡No me toques!"
    "Mujer desconocida" "¡Siénteme!"
    k "¡Gah! ¡Suéltame!"
    show bg ch2partyindoor20 with dissolve
    k "¡Dios! ¡No es humana!"
    p "¿¡Hablas en serio!?"
    k "¡Su piel es sintética!"
    show bg ch2partyindoor21 with dissolve
    k "Quiero decir... ¡Esto es realmente, realmente impresionante!"
    p "No sé si debería quitártela ahora o no."
    show bg ch2partyindoor22 with dissolve
    "Hombre desconocido" "Ya, ya, Sarah, deja a la pobre chica en paz."
    k "¿Eres el dueño?"
    show bg ch2partyindoor43 with dissolve
    dr "Creador, en realidad. Bueno, ambos. [dr], a su servicio. Debo decir que estoy impresionado de que te hayas dado cuenta tan rápido."
    show bg ch2partyindoor22 with dissolve
    k "La mayoría de la gente no lo haría. La sensación de calor era casi perfecta y la elasticidad era de primera. Pero la ausencia sudor la delato. Aun así, la sensación es casi real."
    show bg ch2partyindoor44 with dissolve
    dr "Bueno, en gran parte lo es. La piel y los músculos se sintetizan genéticamente y se injertan en el esqueleto. Tenemos un sistema patentado que permite que la piel se regenere, como lo haría un humano."
    show bg ch2partyindoor23 with dissolve
    k "¿Y no tiene ningún signo de necrosis? ¿Qué pasa si se corta? Necesito que me expliques esto."
    show bg ch2partyindoor45 with dissolve
    dr "Ja, qué bueno encontrar a alguien en esta fiesta con quien pueda hablar."
    k "Lo sé."
    dr "Y usted, señor, ¿también está en el campo?"
    p "Oh, no. Yo soy el músculo, ella es el cerebro."
    n "Los dos continúan con el tema. La discusión va más allá de lo que la mayoría entendería."
    show bg ch2partyindoor53 with dissolve
    p "Katie, vuelvo en un minuto. Tengo que ver a algunas personas."
    show bg ch2partyindoor24 with dissolve
    k "Oh, lo siento, yo no..."
    p "No, está bien, diviértete. ¿Estás bien por tu cuenta?"
    k "¡Sí, esto es genial! Pero no tardes mucho."
    p "Volveré en un instante."
    jump ch2partykatiealex


label ch2partykatiealex:
    show bg ch2partyindoor52 with dissolve
    p "(Bueno, me reconocen, y no parecen felices por ello.)"
    show bg ch2partyindoor54 with dissolve
    sh "¿Olvidaste algo, Sr. Repartidor?"
    a "Pensé que había dejado claro que no eras bienvenido aquí."
    p "Me invitaron."
    a "Considérate no invitado."
    show bg ch2partyindoor56 with dissolve
    sh "Tranquila, querido."
    a "¡No debería estar aquí!"
    sh "Si echas a todos los aguafiestas, estaríamos sentados solos. Ve a buscar un trago; yo me encargaré de él."
    show bg ch2partyindoor57 with dissolve
    a "Bien. Será mejor que te vayas cuando vuelva, Fantasma."
    show bg ch2partyindoor64 with dissolve
    sh "De nada."
    p "Gracias..."
    if s_lust >= 1:
        show bg ch2partyindoor65 with dissolve
        sh "Lo primero es lo primero, ¿quién {i}era{/i} la chica con la que entraste? Parece que acaba de bajarse del autobús en el Este de Bumblefuck."
        menu:
            "Cuidado con lo que dices":
                $ s_lust += 1
                p "Cuida tu boca, ¿o no te enseñaron modales en la escuela de perras ricas?"
                show bg ch2partyindoor66 with dissolve
                sh "Parece que toqué una fibra sensible."
                sh "Podría ser mucho más cruel. Pero no esta noche."
            "No digas nada":

                "..."
    else:
        show bg ch2partyindoor67 with dissolve
        sh "Te vi entrar con una joven. ¿A dónde se fue?"
        sh "En fin..."
    jump ch2partyendshanlon





label ch2partyellensit:
    $ extraevents.append("vostokdoc")
    show bg ch2partyindoor25 with dissolve
    p "Mira, me siento halagado, pero esto no va a pasar esta noche, así que déjalo."
    "Mujer desconocida" "Bienvenido, disfrute de su estancia."
    show bg ch2partyindoor26 with dissolve
    p "¿¡Qué!? Espera..."
    "Mujer desconocida" "Te deseo."
    show bg ch2partyindoor27 with dissolve
    p "Sí, apuesto a que sí."
    p "Sí, mira estoy aquí con un..."
    show bg ch2partyindoor28 with dissolve
    "Mujer desconocida" "Siénteme."
    p "Quizás quieras encontrar una habitación tranquila y recostarte."
    show bg ch2partyindoor29 with dissolve
    "Mujer desconocida" "Siénteme."
    p "No me das muchas opciones."
    show bg ch2partyindoor30 with dissolve
    p "Ahora no, cariño. ¡Quita las manos!"
    "Mujer desconocida" "Siénteme."
    p "Sí, eso ya lo dijiste.."
    show bg ch2partyindoor31 with dissolve
    "Mujer desconocida" "Te deseo."
    p "*Suspira* ¿Has venido con alguien?"
    "Hombre desconocido" "Sarah, deja a ese hombre tranquilo.."
    show bg ch2partyindoor46 with dissolve
    "Hombre desconocido" "Lo siento, la configuración errónea estaba activada."
    p "Eso lo explica. No he visto una mujer tan persistente que no fuera mi esposa. Muy realista también. El mejor robot que he visto."
    dr "Gracias, yo la diseñé. [dr] a su servicio. Bastante orgulloso de la piel, adelante, tóquela."
    show bg ch2partyindoor32 with dissolve
    p "Dios santo."
    "Mujer desconocida" "Lo sé, maestro."
    p "No estaba hablando contigo."
    "Mujer desconocida" "Lo siento amo. Por favor, castigue a este desobediente esclavo."
    dr "Lo siento, todavía estoy trabajando en el apagado."
    p "Si no fuera porque repite las mismas líneas una y otra vez, probablemente no me habría dado cuenta."
    show bg ch2partyindoor47 with dissolve
    dr "Sí, pero está aprendiendo. Todavía tiene que quitarse de encima algunas torceduras, ¡si sabes a qué me refiero! ¡Ja ja!"
    p "Lo que sea que te sirva, hombre. ¿Supongo que eres de Vostok con este tipo de equipo?"
    show bg ch2partyindoor48 with dissolve
    dr "Sí, Vostok tiene un poco de mala fama, pero son los únicos que quieren financiar una investigación como la mía. Cuesta una fortuna."
    dr "Mira, será mejor que reinicie su sistema antes de que viole a alguien. Esperaba que le fuera mejor en este tipo de ambiente. Aparentemente, todavía necesita algo de trabajo."
    show bg ch2partyindoor53 with dissolve
    p "Hablando de eso... Yo también tengo que irme."
    p "Buena suerte con el robot."
    show bg ch2partyindoor48 with dissolve
    dr "Espera y verás. Pronto será perfecta."
    jump ch2partyellenalex

label ch2partyellenalex:
    show bg ch2partyindoor52 with dissolve
    p "(Bueno, me reconocen, y no parecen felices por ello.)"
    show bg ch2partyindoor54 with dissolve
    sh "¿Olvidaste algo, Sr. Repartidor?"
    a "Pensé que había dejado claro que no eras bienvenido aquí."
    p "En realidad, me invitaron."
    a "Considérate no invitado."
    show bg ch2partyindoor56 with dissolve
    sh "Tranquila, querido."
    a "¡No debería estar aquí!"
    sh "¿Y qué pasa si lo invito?"
    a "Todavía le diría que se fuera a la mierda."
    sh "¿Qué, tú puedes invitar a esa amante de Milchers y yo no puedo invitar a quien quiera?"
    a "¿Aamante de Milchers?"
    sh "Ellen Lane. Supongo que finalmente volvió arrastrándose hacia ti."
    show bg ch2partyindoor57 with dissolve
    a "¿Qué carajo? ¿Dónde mierda está?"
    show bg ch2partyindoor64 with dissolve
    sh "De nada."
    p "Gracias..."
    if s_lust >= 1:
        sh "Tienes suerte de que la haya visto antes que él. ¿Cómo está la pequeña vagabunda bocona? Ha pasado mucho tiempo."
        menu:
            "Cuidado con lo que dices":
                $ s_lust += 1
                p "Esperando darle una excusa a una perra rica y arrogante. O eso creo yo."
                show bg ch2partyindoor66 with dissolve
                sh "Una buena manera de dar las gracias."
                p "No hables mal de mis amigos."
                sh "Deja de ladrar, perro. Si quisiera ser cruel, lo sabrías..."
            "No digas nada":

                "..."
    else:
        show bg ch2partyindoor67 with dissolve
        sh "Te vi entrar con ella. De todos modos..."

    jump ch2partyendshanlon





label ch2partyvicsit:
    $ extraevents.append("vostokdoc")
    show bg ch2partyindoor33 with dissolve
    p "Parece que también atraes la atención de las mujeres."
    v "¿Yo? No me había dado cuenta."
    if "ch1spellbound" in extraevents:
        show bg ch2partyindoor34 with dissolve
        v "Aquí, agente [pl]."
        show bg ch2partyindoor35 with dissolve
        p "..."
        v "Espabila ya. *chasquea sus dedos*"
    show bg ch2partyindoor36 with dissolve
    v "Ahora vamos. El reloj está en marcha."
    show bg ch2partyindoor53 with dissolve
    p "¿Cómo debemos manejarlos?"
    v "Tú encárgate de la mujer; yo sacaré a Alexis por ti."
    p "Suena bien."
    show bg ch2partyindoor37 with dissolve
    v "Asegúrate de no estar demasiado..."
    show bg ch2partyindoor38 with dissolve
    v "*Suspira* Contundente..."
    "Mujer desconocida" "Te deseo."
    show bg ch2partyindoor39 with dissolve
    v "El sentimiento no es mutuo."
    "Mujer desconocida" "Siénteme."
    show bg ch2partyindoor40 with dissolve
    n "Mientras Victoria la empuja, una luz rosa brillante brota de la mujer."
    v "¡Duérmete!"
    p "¿Era una robot?"
    show bg ch2partyindoor41 with dissolve
    v "Un prototipo de Vostok. Solo es un juguete."
    p "Si no fuera por cómo hablaba, no lo habría adivinado."
    show bg ch2partyindoor42 with dissolve
    "Hombre desconocido" "¡Sarah! ¿Qué has hecho?"
    v "[dr], me disculpo por lo de su muñeca."
    show bg ch2partyindoor50 with dissolve
    dr "¡Maldita sea! ¡No la apagaste correctamente!"
    show bg ch2partyindoor42 with dissolve
    v "Me temo que no sabía que había una forma adecuada."
    show bg ch2partyindoor49 with dissolve
    dr "¿Entiendes lo que has hecho? ¡Eso puede haber corrompido su memoria! ¡Una semana de trabajo perdida!"
    show bg ch2partyindoor41 with dissolve
    v "Deberíamos irnos, [p]."
    p "Eh, sí."
    show bg ch2partyindoor51 with dissolve
    dr "*Se escuchan sus maldiciones de fondo.*"
    p "Creo que le has hecho enfadar."
    v "El hombre es un genio, saldrá adelante."
    jump ch2partyvicalex





label ch2partyvicalex:
    show bg ch2partyindoor52 with dissolve
    p "Bueno, me reconocen y no parecen contentos por ello."
    v "No importa."
    show bg ch2partyindoor54 with dissolve
    sh "¿Olvidaste algo, Sr. Repartidor?"
    a "¿Cómo entraste aquí? No voy a responder a tus preguntas."
    show bg ch2partyindoor58 with dissolve
    v "En realidad, está conmigo."
    a "¿Y tú eres?"
    show bg ch2partyindoor59 with dissolve
    v "Una amiga de algunos de sus inversores más ricos. Sería una pena que no pudiéramos hablar de negocios."
    a "¡Si quieres hablar conmigo pide una cita! Entonces podemos hablar..."
    show bg ch2partyindoor60 with dissolve
    a "Negocios..."
    n "Tanto Alexis como Shanlon miran a Victoria con ojos casi muertos."
    show bg ch2partyindoor61 with dissolve
    v "Sí, Sr. Conner, cualquier negocio que se adapte a su fantasía. Tal vez podamos llevar esta discusión afuera. Prefiero la sensación de la brisa nocturna."
    a "Umm. Por supuesto..."
    show bg ch2partyindoor62 with dissolve
    v "Si me disculpas, querido, tal vez puedas entretenerla a ella."
    p "..."
    show bg ch2partyindoor63 with dissolve
    sh "¿Qué carajo fue eso? ¿Es un truco de Fantasmas?"
    p "No. Solo fue ella. Puede ser muy convincente."
    if s_lust >= 1:
        show bg ch2partyindoor64 with dissolve
        sh "Apuesto a que es buena en la cama."
        if "ch1vic" in extraevents:
            p "Más que eso, créeme."
        else:
            p "No podría decírtelo."
        show bg ch2partyindoor65 with dissolve
        sh "Tiene que serlo. Conozco su tipo... la típica puta de sala de juntas. Elegante por fuera, pero se abre de piernas para quien el jefe le diga."
        menu:
            "Cuidado con lo que dices":
                $ s_lust += 1
                p "La puta más importante de la casa, ¿estás celosa?"
                show bg ch2partyindoor66 with dissolve
                sh "Parece que un perro me ladra."
                p "Es mejor no hablar mal de alguien que ni siquiera conoces."
                sh "O crees que he dado en el clavo. Acaba de robarme a mi novio delante de mis narices."
                sh "Pero si quisiera ser cruel, perrito, lo sabrías. De todos modos... Esta noche no."
            "No digas nada":

                "..."
    else:

        show bg ch2partyindoor67 with dissolve
        sh "Aunque no puedo culpar a Alexis. Yo tampoco puedo dejar de mirarla."
        sh "Ni siquiera es mi tipo."
    jump ch2partyendshanlon


label ch2partyendshanlon:
    sh "Así que... ¿supongo que has venido aquí para obtener más respuestas?"
    show bg ch2partyindoor68 with dissolve
    p "Ese es el trabajo."
    show bg ch2partyindoor67 with dissolve
    sh "Y una vez que sientes el olor, no lo dejas ir. ¿No es así, perrito?"
    p "Estás mezclando metáforas."
    show bg ch2partyindoor69 with dissolve
    sh "Siéntate y hablemos."
    p "Dime, ¿qué sabes?"
    show bg ch2partyindoor70 with dissolve
    sh "Lo suficiente para ayudarte."
    p "Entonces, ¿cuál es la trampa? ¿Qué consigues con esto?"
    show bg ch2partyindoor72 with dissolve
    sh "Paciencia, señor [pl]. Alexis vuela a Londres mañana temprano."
    sh "Puedes venir aquí entonces. Hay menos posibilidades de que nos interrumpan. Podemos... tocar todos los temas."
    p "Podemos hablar ahora. Tengo un horario."
    show bg ch2partyindoor71 with dissolve
    sh "Tú NO mandas aquí. Creo que te olvidas de con quién estás hablando."
    p "Una mujer con un palo metido..."
    sh "Mañana."
    if "ch2choosekatie" in extraevents:
        show bg ch2partyindoor76 with dissolve
        k "Ya está."
        p "Oye, Katie, deberíamos irnos."
        show bg ch2partyindoor73 with dissolve
        sh "Oh, es Bumblefuck del Este."
        k "¿Qué?"
        sh "Nada, solo le decía al perrito este que destacas muchisimo."
        sh "¿Crees que alguien como tú puede entrar en una fiesta con alguien como yo y ser algo más que una curiosidad?"
        sh "No te sientas mal. Cada fiesta tiene una. La chica con un vestido 20 años pasado de moda que no puede dejar de mirar a las personas que realmente importan. "
        show bg ch2partyindoor77 with dissolve
        k "Pero... *Katie contiene sus lágrimas*"
        show bg ch2partyindoor73 with dissolve
        sh "Acéptalo. Esto es lo más cerca que estarás."
        show bg ch2partyindoor78 with dissolve
        k "Deja de hablar, perra clasista."
        show bg ch2partyindoor79 with vpunch
        n "Katie lanza el vino que tiene en su copa hacia Shanlon, tiñéndole el vestido"
        show bg ch2partyindoor74 with dissolve
        p "Oh, mierda..."
        sh "¡AAAH!"
        show bg ch2partyindoor75 with dissolve
        sh "¡MALDITA PERRA! ¡Voy a acabr contigo!"
        k "Yo, eh... ¿perdón?"
        show bg ch2partyindoor80 with dissolve
        p "Katie, vamos, ¡ahora mismo!"
        k "[p], ¡lo siento!"
        p "¡Vámonos de una vez!"
        p "¡Ahora!"
        jump ch2upstairs
    else:

        show bg ch2partyindoor81 with dissolve
        sh "Ahora tengo que encontrar a Alexis, ese maldito idiota."
        p "(Al diablo, está bien, es hora de revisar arriba.)"
    jump ch2upstairs
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
