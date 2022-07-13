

image bg ch2alexis1 = "ch2alexis1"
image bg ch2alexis2 = "ch2alexis2"
image bg ch2alexis3 = "ch2alexis3"
image bg ch2alexis4 = "ch2alexis4"
image bg ch2alexis5 = "ch2alexis5"
image bg ch2alexis6 = "ch2alexis6"
image bg ch2alexis7 = "ch2alexis7"
image bg ch2alexis8 = "ch2alexis8"
image bg ch2alexis9 = "ch2alexis9"
image bg ch2alexis10 = "ch2alexis10"
image bg ch2alexis11 = "ch2alexis11"
image bg ch2alexis12 = "ch2alexis12"
image bg ch2alexis13 = "ch2alexis13"
image bg ch2alexis14 = "ch2alexis14"
image bg ch2alexis15 = "ch2alexis15"
image bg ch2alexis16 = "ch2alexis16"
image bg ch2alexis17 = "ch2alexis17"
image bg ch2alexis18 = "ch2alexis18"
image bg ch2alexis19 = "ch2alexis19"
image bg ch2alexis20 = "ch2alexis20"

image bg ch2elevatorday0 = "ch2elevatorday0"
image bg ch2elevatorday1 = "ch2elevatorday1"
image bg ch2elevatorday2 = "ch2elevatorday2"

image ch2shanlonpan = Movie(play='video/chapter-2-video/ch2shanlonpan.webm', loop=False)
image bg ch2shanlonpanmov movie:
    "ch2shanlonpan"
    pause 7.0
    "ch2shanlonpan-end"


label ch2alexis:

    scene black with Dissolve(2)
    show text "{=trans}UNA HORA DESPUÉS, ACERCÁNDOSE AL CONDOMINIO DE ALEXIS CONNER{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)

    show bg ch2elevatorday0 with dissolve
    "Robot de seguridad" "Indique sus intenciones."
    p "He venido a ver al Sr. Conner."
    "Robot de seguridad" "..."
    "Robot de seguridad" "Acceso concedido. Puede entrar."

    show bg ch2elevatorday1 with dissolve
    p "(Maldita sea, y yo que pensaba que la casa de Meredith era elegante.)"
    show bg ch2elevatorday2 with dissolve
    p "(Una de las ventajas de ser tan rico es que puedes hacer lo que quieras y no arrepentirte.)"

    scene black with Dissolve(1)
    show bg ch2alexis3 with dissolve
    sh "*Suspira* La entrega estaba prevista para ayer."
    p "¿Perdón?"
    sh "No tienes excusa. Y antes de que preguntes, sí, soy la mujer de LAN, así que puedes dejar de mirar. Solo deja el paquete y vete. Y no esperes una propina."
    p "Escucha, señorita, no soy un repartidor y me importa una mierda lo que necesites. Así que deja de actuar así."
    show bg ch2alexis1 with dissolve
    sh "Mierda. Más vale que llegue pronto o habrá problemas. Necesito ese vestido."
    p "Eso es trágico y todo, pero..."
    sh "Bien, ¿qué necesitas? Si no eres el repartidor, ¿quién eres?"
    p "Soy un Fantasma, estoy aquí para ver a Alexis."
    show bg ch2alexis2 with dissolve
    sh "¿Se trata de su hija Milcher?"
    p "¿Está aquí o no?"
    show bg ch2alexis4 with dissolve
    sh "Puedo ir a buscarlo por ti."
    sh "Sería genial para ti. Tener a gente importante haciéndote favores."
    p "¿Disculpa?"
    show bg ch2alexis5 with dissolve
    if dep >= 2:
        p "(Acabo de conocerla y ya quiero abofetearla.)"
    else:
        p "(Si Katie pudiera verme ahora.)"
    show bg ch2alexis6 with dissolve
    sh "Eso es lo que haces, ¿no?"
    p "¿A qué te refieres?"
    sh "Recuperar los juguetes perdidos y llevarlos de vuelta a sus amos."
    menu:
        "Dile lo que se merece":
            $ s_lust += 1
            p "Yo también soy un hombre ocupado y, ¿sabes lo que no necesito? Una perra millonaria que descarga sus frustraciones en mí porque su vestido llamativo y caro no apareció."
        "Dile que no aprecias su tono":
            p "Mira, solo estoy aquí para hacer algunas preguntas, no para que me reprendan personas como tú."
    show bg ch2alexis7 with dissolve
    if s_lust == 1:
        sh "Bueno, puede que no seas un perro, pero eso es un ladrido infernal. Mis disculpas, señor..."
    else:
        sh "Mis disculpas, señor..."
    p "[pl]."
    sh "¿Y cómo te llamaron tus padres?"
    menu:
        "Dile tu nombre":
            p "[p]."
        "No se lo digas":
            $ extraevents.append("ch2noname")
            $ s_lust += 1
            p "¿Quieres que te lo diga? Que mal..."
    show bg ch2alexis8 with dissolve
    if s_lust == 2:
        sh "Un hombre solitario y agresivo. Caes justo en los clichés, ¿no? Espero que haya algo más en ti que solo eso."
        p "Una rica Reina del Hielo coqueteando. Tampoco estás libre del cliché. He conocido a un montón de mujeres como tú."
    elif s_lust == 1 and "ch2noname" in extraevents:
        sh "Bien, no me lo digas. No me importa."
    else:
        sh "Ojalá tuvieras mi pedido, [p]. Eso podría haber sido mucho más agradable."
    window hide
    show bg ch2shanlonpanmov movie with dissolve
    $ renpy.pause()
    window show
    if s_lust == 2:
        sh "Bueno, no lo sabes todo."
        p "Siempre hay algo que aprender."
        show bg ch2alexis12 with dissolve
        p "(Carajo, la televisión no les hace justicia.)"
        show bg ch2alexis11 with dissolve
        sh "Entonces, ¿Sr. [pl]?"
        show bg ch2alexis9 with dissolve
        p "..."
        sh "¿Te lo traigo?"
        p "Por favor."
    else:
        sh "Dejemos esto y empecemos de nuevo."
        p "Solo trae a tu novio."
        show bg ch2alexis9 with dissolve
        sh "Novio... eh, por supuesto. Un minuto."

    show bg ch2alexis13 with dissolve
    sh "Espera aquí fuera. A Alexis no le gustan los invitados inesperados."
    show bg ch2alexis14 with dissolve
    p "(Putas celebridades.)"
    show bg ch2alexis15 with dissolve
    p "..."
    p "(¿Pueden tardar más?)"

    show bg ch2alexis16 with dissolve
    p "(Ahí está.)"
    show bg ch2alexis17 with dissolve
    a "¿Sr. [pl]?"
    p "Alexis Conner, supongo."
    a "Hola, siento lo de Shanlon. Ha estado de muy mal humor últimamente."
    a "¿En qué puedo ayudarte? Y rápido, por favor, estoy en medio de algo."
    p "Estoy buscando a su hija, Gloria. ¿La ha visto recientemente?"
    show bg ch2alexis18 with dissolve
    a "No. Se fue hace mucho tiempo. No la he visto en años."
    p "¿Nunca intentó ponerse en contacto usted o viceversa?"
    show bg ch2alexis19 with dissolve
    a "No. ¡Y no veo qué diferencia habría si lo hiciera! ¡No está aquí y no sé dónde está!"
    p "Podría estar en peligro, Sr. Conner, cualquier información que tenga podría ayudar."
    show bg ch2alexis20 with dissolve
    a "Si eso es todo, me iré. Ahora, si me disculpa, tengo planes para esta noche y tengo que prepararme."
    p "Espere un segundo. ¡No hemos terminado aquí!"
    a "Espero que encuentre la salida. Me voy."
    show bg ch2alexis15 with dissolve
    p "(¿Qué mierda le pasa a esta gente?)"
    p "(A la mierda con esto, volveré a casa y luego buscare a algunos contactos.)"
    call ch2gloriaday from _call_ch2gloriaday
    jump ch2home
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
