
image bg ch2vichome1 = "ch2vichome1"
image bg ch2vichome2 = "ch2vichome2"
image bg ch2vichome3 = "ch2vichome3"
image bg ch2vichome4 = "ch2vichome4"
image bg ch2vichome5 = "ch2vichome5"
image bg ch2vichome6 = "ch2vichome6"

image bg ch2vichome8 = "ch2vichome8"
image bg ch2vichome9 = "ch2vichome9"
image bg ch2vichome10 = "ch2vichome10"
image bg ch2vichome11 = "ch2vichome11"
image bg ch2vichome12 = "ch2vichome12"
image bg ch2vichome13 = "ch2vichome13"
image bg ch2vichome14 = "ch2vichome14"
image bg ch2vichome15 = "ch2vichome15"
image bg ch2vichome16 = "ch2vichome16"
image bg ch2vichome17 = "ch2vichome17"
image bg ch2vichome18 = "ch2vichome18"
image bg ch2vichome19 = "ch2vichome19"
image bg ch2vichome20 = "ch2vichome20"
image bg ch2vichome21 = "ch2vichome21"
image bg ch2vichome22 = "ch2vichome22"
image bg ch2vichome23 = "ch2vichome23"
image bg ch2vichome24 = "ch2vichome24"
image bg ch2vichome25 = "ch2vichome25"
image bg ch2vichome26 = "ch2vichome26"
image bg ch2vichome27 = "ch2vichome27"
image bg ch2vichome28 = "ch2vichome28"
image bg ch2vichome29 = "ch2vichome29"
image bg ch2vichome30 = "ch2vichome30"
image bg ch2vichome31 = "ch2vichome31"
image bg ch2vichome32 = "ch2vichome32"
image bg ch2vichome33 = "ch2vichome33"
image bg ch2vichome34 = "ch2vichome34"
image bg ch2vichome35 = "ch2vichome35"
image bg ch2vichome36 = "ch2vichome36"
image bg ch2vichome37 = "ch2vichome37"
image bg ch2vichome38 = "ch2vichome38"
image bg ch2vichome39 = "ch2vichome39"
image bg ch2vichome40 = "ch2vichome40"
image bg ch2vichome41 = "ch2vichome41"
image bg ch2vichome42 = "ch2vichome42"
image bg ch2vichome43 = "ch2vichome43"
image bg ch2vichome44 = "ch2vichome44"
image bg ch2vichome45 = "ch2vichome45"
image bg ch2vichome46 = "ch2vichome46"
image bg ch2vichome47 = "ch2vichome47"


image ch2homepanmov = Movie(play='video/chapter-2-video/ch2homepan.webm', loop=False)
image bg ch2homepanmovie movie:
    "ch2homepanmov"
    pause 7
    "ch2homepanend"



label ch2home:
    scene black with Dissolve(2)
    show text "{=trans}UNA HORA DESPUÉS, DE VUELTA EN EL DEPARTAMENTO{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    p "(De vuelta, por fin.)"
    show bg ch2vichome1 with dissolve
    p "Sam, me muero de hambre... ¿puedes prepararme algo? Estoy pensando en algo italiano."
    if "ch1vic" in extraevents:
        "..."
        p "¿Sam?"
        show bg ch2vichome2 with dissolve
        p "No es gracioso, Sam. No me hagas desactivar tu protocolo de sarcasmo."
        show bg ch2vichome3 with dissolve
        p "¿Sam?"
        show bg ch2vichome4 with dissolve
        if not persistent.ch2card2:
            $ renpy.notify(['Posible pista', 'alert'])
            show screen hidden_item("ch2card2", "ch2card2", 631, 491, 56, 59)
        v "Buenas tardes, agente."
        p "..."
        hide screen hidden_item
        play music audio.futurenoir fadein 2.0 fadeout 2.0
        p "¡¿Qué mierda haces aquí?!"
        show bg ch2vichome5 with dissolve
        v "Tengo mis métodos, agente."
        show bg ch2vichome6 with dissolve
        v "Sam, ¿podrías prepararle al Sr. [pl] algo de cenar? Estoy pensando en algo italiano."
        s "Por supuesto, señora."
        show bg ch2vichome5 with dissolve
        v "Sam, llámame señorita."
        s "Sí, señorita."
        show bg ch2vichome8 with dissolve
        p "¿Qué le has hecho a mi IA?"
        v "Nada en absoluto. Soy experta en hacer amigos. Somos amigos, ¿no es así, agente?"
        p "Vuelve a la normalidad."
        p "¡Ahora!"
        show bg ch2vichome9 with dissolve
        v "Pronto. Necesito que te ocupes de algo."
        p "Va a ser que no."
        show bg ch2vichome10 with dissolve
        v "¿Incluso si la tarea es bastante beneficiosa para ti?"
        p "¿Cómo?"
        v "Creo que es obvio. Todavía intentas encontrar a la señorita Conner."
        show bg ch2vichome12 with dissolve
        v "Y yo personalmente estaría muy... agradecida."
        p "Agradecida."
        show bg ch2vichome13 with dissolve
        v "Sí, por un trabajo bien hecho."
        p "Solo porque nosotros..."
        v "¿Tuvimos sexo?"
        p "Eso no significa que puedas obligarme..."
        show bg ch2vichome14 with dissolve
        v "¿Obligarte a qué, agente?"
        v "¿Me deseas?"
        v "¿Me necesitas?"
        menu:
            "Sí...":
                show bg ch2vichome15 with dissolve
                p "Sí, te necesito..."
                if "ch1spellbound" not in extraevents:
                    $ extraevents.append("ch1spellbound")

                v "Mmm... Por supuesto que sí."
                show bg ch2vichome16 with dissolve
                v "Esto puede esperar. Primero, debo devolver lo que es tuyo."
            "Rompe su hechizo":
                $ v_score += 1
                if "ch1spellbound" in extraevents:
                    $ extraevents.remove("ch1spellbound")
                p "¡Solo devuélveme a Sam! Entonces podremos hablar."
                show bg ch2vichome16 with dissolve
                v "Como quieras."

        show bg ch2vichome17 with dissolve
        v "Ya me he divertido. Te devolveré el control de tu IA."
        p "Por favor."
        show bg ch2vichome20 with dissolve
        v "Su modelo está algo desfasado."
        p "Funciona muy bien."
        show bg ch2vichome21 with dissolve
        v "Sam, sé bueno y transfiere el control administrativo al agente [p] [pl]."
        s "Se requiere una frase de acceso Señorita."
        show bg ch2vichome22 with dissolve
        v "\"Todos crecen menos yo.\""
        s "Control administrativo transferido a [p] [pl]."
        show bg ch2vichome23 with dissolve
        v "El control vuelve a ser tuyo."
        p "¿Sam?"
        s "¿Sí, señor?"
        p "Nada Sam, está bien."
        menu:
            "Pregúntale qué quiere":
                p "Ahora dime qué quieres."
                jump ch2vichomeinfo
            "Enfádate":
                $ dep += 1
                show bg ch2vichome31 with dissolve
                p "¿Qué mierda te pasa? ¡Entras en mi casa, y te haces con mi IA! ¿Debería echarte a la calle?"
                v "Guárdate tus berrinches para alguien a quien le afecte."
                show bg ch2vichome32 with dissolve
                v "Estoy aquí para ayudarte, no se que estas pensando."
                p "Es raro. La mayoría de la gente quiere ayudar, dicen \"¡Oye, [p]! ¡Yo puedo ayudar\". Luego no hacen nada."
                v "¿Eso es lo que piensas?"
                p "¡Maldita sea!"
                show bg ch2vichome33 with dissolve
                v "¿Ya terminaste?"
                p "Solo dime qué quieres."
                jump ch2vichomeinfo
    else:

        s "¿Para uno o dos, señor?"
        show bg ch2vichome2 with dissolve
        p "¿A qué te refieres, Sam?"
        show bg ch2vichome3 with dissolve
        s "Tienes a una invitada."
        show bg ch2vichome4 with dissolve
        if not persistent.ch2card2:
            $ renpy.notify(['Posible pista', 'alert'])
            show screen hidden_item("ch2card2", "ch2card2", 631, 491, 56, 59)
        v "Hola, agente [pl]."
        p "..."
        hide screen hidden_item
        play music audio.futurenoir fadein 2.0 fadeout 2.0
        p "¡¿Cómo demonios has entrado aquí?!"
        show bg ch2vichome5 with dissolve
        v "Tengo mis métodos, agente."
        p "Tengo que conseguir mejores cerraduras."
        show bg ch2vichome8 with dissolve
        v "Sea como sea... ¿Supongo que no tienes ninguna información importante del Sr. Conner?"
        p "¿Qué, me estabas siguiendo?"
        show bg ch2vichome9 with dissolve
        v "Eres un activo caro, aunque algo volátil. Este es un contrato importante. Si estuvieras dirigiendo esta operación, harías lo mismo."
        p "¿Y eso amerita entrar a mi casa?"
        show bg ch2vichome10 with dissolve
        v "Confía en mí, ese no es mi objetivo principal."
        p "¿Confianza? La confianza se gana."
        show bg ch2vichome16 with dissolve
        if v_score >= 1:
            v "Mis disculpas, [p]."
            p "¿Te disculpas? Vas en serio."
        else:
            v "Sí, eso hace que esta situación sea lamentable."
        show bg ch2vichome18 with dissolve
        v "No he venido a discutir, agente [pl]."
        show bg ch2vichome17 with dissolve
        v "Estoy, a pesar de las apariencias, aquí para ayudarte."
        p "¿En qué sentido?"
        show bg ch2vichome19 with dissolve
        v "Alexis Conner va a dar una fiesta esta noche."
        p "Lo sé. ¿Y qué?"
        show bg ch2vichome20 with dissolve
        v "Tu anterior encuentro con él fue un desastre... y tenemos razones para creer que hay más que aprender de él."
        p "No me digas. Pero Conner no quiere hablar. No sé por qué tiene ese problema con su hija, pero algo pasa."
        show bg ch2vichome21 with dissolve
        v "Tal vez. Sería mejor evitarlo por completo. Estoy segura de que podría haber más información en su casa..."
        p "Si puedo entrar, sin duda me ayudaría. Me gustaría echar un vistazo a su casa."
        show bg ch2vichome22 with dissolve
        v "De ahí los festejos de esta noche. Hay una invitación para ti y un invitado. Estás en el registro. Todo está permitido."
        p "¿Un invitado? ¿Una cita?"
        show bg ch2vichome23 with dissolve
        v "Sí. Podría ir contigo para asegurarme de que las cosas van bien."

        menu:
            "Acompáñala para vigilarla":
                $ extraevents.append("ch2choosevic")
                p "Sí, por mí está bien. Si estás conmigo, no vas a irrumpir en mi casa y joder a Sam."
                show bg ch2vichome24 with dissolve
                v "Eso es cierto, agente."
                show bg ch2vichome35 with dissolve
                v "Recuerda que no puedes llevar eso. Este evento es... elaborado."
                p "He tratado con esta gente antes. No te preocupes, puedo disfrazarme."
                show bg ch2vichome36 with dissolve
                v "Muy bien."
                show bg ch2vichome37 with dissolve
                v "Tengo que prepararme para la noche. Volveré pronto."
                show bg ch2vichome38 with dissolve
                p "(Esto debería ser interesante.)"
                show bg ch2vichome39 with dissolve
                play music audio.calm fadein 2.0 fadeout 2.0
                p "*Se truena el cuello* (Sin embargo, si no encontramos nada allí, va a ser muy difícil localizarla.)"
                jump ch2before


            "Pídele a Victoria que te acompañe" if v_score >= 1:
                $ extraevents.append("ch2choosevic")
                p "Entonces, vamos."
                show bg ch2vichome24 with dissolve
                v "Tiene sentido. Así puedes vigilarme. Es lo que yo haría."
                p "Tal vez, pero esa no es la razón principal."
                show bg ch2vichome26 with dissolve
                v "Entonces, ¿por qué?"
                p "Porque estoy tratando de entenderte, Victoria Shields. Pones la cara de una esclava de la corporación... Llámame loco... Pero creo que en realidad te preocupa la chica."
                show bg ch2vichome25 with dissolve
                v "..."
                v "Muy bien. Iremos juntos."
                p "¿Tengo razón?"
                show bg ch2vichome35 with dissolve
                v "Ella puede ayudar a muchos. Y ella es... necesaria para Baynard."
                p "No es una respuesta."
                window hide
                show bg ch2homepanmovie movie with dissolve
                $ renpy.pause()
                window show
                v "Tómalo como quieras."
                p "Ahí está de nuevo. Una grieta en la fachada. La vi antes cuando la Sra. White te susurró algo al oído."
                v "No sé a qué te refieres."
                show bg ch2vichome37 with dissolve
                v "Si me disculpas, tengo que prepararme para esta noche. Volveré en pronto."
                show bg ch2vichome38 with dissolve
                p "(Perece que he tocado una fibra sensible.)"
                show bg ch2vichome39 with dissolve
                p "*Se truena el cuello* (Espero que podamos encontrar algo allí. Si no es así, tengo que empezar acudir a unos contactos.)"

                jump ch2before

            "Elige a otra persona" if k_score >=2 or e_score >= 1:
                p "Tengo algunas ideas en mente."
                show bg ch2vichome35 with dissolve
                p "He tratado con esta gente antes. No te preocupes, puedo disfrazarme."
                p "Me pondré mi mejor traje."
                show bg ch2vichome36 with dissolve
                v "Ahora, si me disculpas."
                show bg ch2vichome37 with dissolve
                v "Tengo otros asuntos que atender."
                show bg ch2vichome38 with dissolve
                p "(Genial, una fiesta llena de imbéciles super ricos. No puedo esperar...)"
                show bg ch2vichome39 with dissolve
                p "*Se truena el cuello* A ver si alguien se anima a ir."
                jump ch2homepick





label ch2vichomeinfo:

    show bg ch2vichome27 with dissolve
    v "Lo mismo que tú. Información. Alexis Conner va a dar una fiesta esta noche."
    p "Lo sé. ¿Y qué?"
    show bg ch2vichome28 with dissolve
    v "Tu anterior encuentro con él fue un desastre... y tenemos razones para creer que podemos sacarle más información."
    p "No me digas. Pero Conner no quiere hablar. No sé por qué tiene ese problema con su hija, pero algo pasa."
    show bg ch2vichome30 with dissolve
    v "Tal vez. Sería mejor evitarlo por completo. Estoy segura de que podría haber más información en su casa..."
    p "Si puedo entrar, sin duda ayudaría. Me gustaría echar un vistazo a su casa."
    show bg ch2vichome35 with dissolve
    v "De ahí los festejos de esta noche. Hay una invitación para ti y un invitado. Estás en el registro. Todo está permitido."
    p "¿Un invitado? ¿Una cita?"
    if k_score >= 2 or e_score >= 1:
        p "Tengo algunas ideas en mente."
        v "Muy bien."
    else:
        v "Sería lo mejor."
    v "Esta es una fiesta de la alta sociedad. Supongo que no necesitas que te diga que te vistas adecuadamente."
    p "Tengo un atuendo decente, Victoria."
    show bg ch2vichome36 with dissolve
    v "Perfecto. Entonces, buenas noches, agente y buena suerte."
    if k_score >=2 or e_score >= 1:
        menu:
            "Elige Victoria":
                jump ch2vichomechoose
            "Elige a otra persona":
                show bg ch2vichome38 with dissolve
                p "(Genial, una fiesta llena de imbéciles super ricos. No puedo esperar.)"
                jump ch2homepick
    else:
        jump ch2vichomechoose

label ch2vichomechoose:
    $ extraevents.append("ch2choosevic")
    p "Espera..."
    show bg ch2vichome37 with dissolve
    v "¿Sí, agente?"
    p "Te vienes conmigo."
    v "Tiene sentido. Así puedes vigilarme. Es lo que yo haría."
    p "Correcto."
    v "Muy bien. Volveré pronto, con la vestimenta adecuada."
    v "Disfruta la cena, agente."
    show bg ch2vichome38 with dissolve
    play music audio.calm fadein 2.0 fadeout 2.0
    p "(Genial, una fiesta para un grupo de ricachones.)"
    p "¿Cuánto falta para que la cena esté lista, Sam?"
    s "Quince minutos con doce segundos."
    show bg ch2vichome39 with dissolve
    p "Perfecto. Gracias, Sam."
    jump ch2before

label ch2homepick:
    play music audio.calm fadein 2.0 fadeout 2.0
    if k_score >= 2 and e_score >= 1:
        menu:
            "Elige a Katie":
                jump ch2homepickkatie
            "Elige a Ellen":
                jump ch2homepickellen

    if k_score >= 2:
        jump ch2homepickkatie

    if e_score >= 1:
        jump ch2homepickellen


label ch2homepickkatie:
    $ extraevents.append("ch2choosekatie")
    p "Sam, llama a la doctora Hamilton por mí."
    show bg ch2vichome47 with dissolve
    s "Sí, señor. Llamando a la doctora Hamilton."
    p "..."
    show bg ch2vichome40 with dissolve
    k "Sí, siento que los resultados estén tardando más de lo que pensaba."
    p "Está bien, no es por eso que estoy llamando. Necesito tu ayuda de nuevo."
    show bg ch2vichome41 with dissolve
    k "Después de lo que paso esta mañana, me asusta oírte decir eso."
    p "Nada de esconderse esta vez, lo prometo."
    k "¿Y los tiroteos?"
    p "Nada de eso. Esto mplica vestirse de forma elegante."
    show bg ch2vichome42 with dissolve
    k "..."
    k "¿Me estás pidiendo una cita? No sé si..."
    p "No del todo, Doc. Hay una fiesta esta noche a la que tengo que asistir."
    k "Sigue pareciendo una cita."
    p "Es por el trabajo. Necesito que venga un acompañante y he pensado en ti."
    k "Déjame adivinar... ¿esta noche?"
    p "Sí, en un par de horas."
    show bg ch2vichome40 with dissolve
    k "Claro... pero no me das tiempo..."
    p "Lo siento."
    k "Dame una hora para prepararme y luego nos vemos en tu casa."
    p "Te veré pronto entonces."
    k "Genial."
    show bg ch2vichome39 with dissolve
    p "¿Cuánto falta para que la comida esté lista, Sam?"
    s "Catorce minutos con treinta y cinco segundos, señor."
    p "Bien..."
    jump ch2before

label ch2homepickellen:
    $ extraevents.append("ch2chooseellen")
    p "Sam, llama a Ellen Lane de mi parte."
    show bg ch2vichome47 with dissolve
    s "Sí, señor. Llamando a Ellen Lane."
    p "..."
    show bg ch2vichome46 with dissolve
    e "Ugh... ¿Qué?"
    p "Soy [p]."
    show bg ch2vichome45 with dissolve
    e "¿Qué carajo, [p]? ¡Me has despertado!"
    p "¿Te has despertado? ¡Son como las 6 de la tarde!"
    e "¡Me has despertado! Más vale que esto sea bueno."
    p "¿No siempre es así? Espera, no respondas a eso."
    e "Voy a colgar ahora mismo."
    p "Es sobre el trabajo de Connor. Necesito tu ayuda. Una gran fiesta y necesito un acompañante. Pensé que querrías venir."
    show bg ch2vichome43 with dissolve
    e "Siempre estoy lista para una fiesta, lo sabes, imbécil."
    p "Una advertencia: esto es menos juerguista de lo que crees. Es más bien vino y caviar, en otras palabras, una fiesta elegante y rica."
    show bg ch2vichome44 with dissolve
    e "Buena suerte con eso. Me voy a mimir."
    p "Oye, acepté el trabajo. Ahora necesito un poco de ayuda."
    e "Sabes que lo único bueno de estar al margen es no tener que vestirse para estas fiestas de mierda, ¿cierto?{w} Te echare un cable. Estaré allí en una hora."
    p "Gracias, Ellen. Nos vemos pronto."
    e "*Dice en voz baja* Si me visto como ricachona atraerá mirada"
    show bg ch2vichome39 with dissolve
    p "¿Cuánto falta para que la comida esté lista, Sam?"
    s "Catorce minutos con treinta y siete segundos, señor."
    p "Bien."
    jump ch2before
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
