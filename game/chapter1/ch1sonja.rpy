


image bg ch1sonja2 = "ch1sonja2"
image bg ch1sonja3 = "ch1sonja3"
image bg ch1sonja4 = "ch1sonja4"
image bg ch1sonja5 = "ch1sonja5"
image bg ch1sonja6 = "ch1sonja6"
image bg ch1sonja7 = "ch1sonja7"
image bg ch1sonja8 = "ch1sonja8"
image bg ch1sonja9 = "ch1sonja9"
image bg ch1sonja10 = "ch1sonja10"
image bg ch1sonja11 = "ch1sonja11"
image bg ch1sonja12 = "ch1sonja12"
image bg ch1sonja13 = "ch1sonja13redo"
image bg ch1sonja14 = "ch1sonja14redo"
image bg ch1sonja15 = "ch1sonja15"
image bg ch1sonja16 = "ch1sonja16"
image bg ch1sonja17 = "ch1sonja17"
image bg ch1sonja18 = "ch1sonja18"
image bg ch1sonja19 = "ch1sonja19"
image bg ch1sonja20 = "ch1sonja20"
image bg ch1sonja21 = "ch1sonja21"
image bg ch1sonja22 = "ch1sonja22"
image bg ch1sonja23 = "ch1sonja23"
image bg ch1sonja24 = "ch1sonja24"
image bg ch1sonja25 = "ch1sonja25"
image bg ch1sonja26 = "ch1sonja26"
image bg ch1sonja27 = "ch1sonja27"
image bg ch1sonja28 = "ch1sonja28"
image bg ch1sonja29 = "ch1sonja29"
image bg ch1sonja30 = "ch1sonja30"
image bg ch1sonja31 = "ch1sonja31"
image bg ch1sonja32 = "ch1sonja32"
image bg ch1sonja33 = "ch1sonja33"
image bg ch1sonja34 = "ch1sonja34"
image bg ch1sonja35 = "ch1sonja35"
image bg ch1sonja36 = "ch1sonja36"
image bg ch1sonja37 = "ch1sonja37"
image bg ch1sonja38 = "ch1sonja38"
image bg ch1sonja39 = "ch1sonja39"
image bg ch1sonja40 = "ch1sonja40"
image bg ch1sonja41 = "ch1sonja41"
image bg ch1sonja42 = "ch1sonja42"
image bg ch1sonja43 = "ch1sonja43"
image bg ch1sonja44 = "ch1sonja44"





label ch1sonja:
    p "¡Sam, apaga la holopantalla!"
    show bg ch1sonja2 with dissolve
    p "Escucha, imbécil, no sé quién eres, pero estás jugando fuego al venir aquí."
    show bg ch1sonja3 with dissolve
    $ insult = renpy.random.choice(insults)
    "Mujer desconocida" "Qué tal, mierdecilla."
    p "Mierda... ¡Sam, luces!"
    show bg ch1sonja4 with dissolve
    "Mujer desconocida" "¡Hola!"
    show bg ch1sonja12 with dissolve
    e "[p], ¿quién demonios es esa?"
    show bg ch1sonja5 with dissolve
    "Mujer desconocida" "Sí, cariño, ¿quién demonios soy yo?"
    p "Ellen, te presento a [j]{w}, mi esposa..."
    show bg ch1sonja7 with dissolve
    j "*Toma un largo trago de cerveza*"
    show bg ch1sonja8 with dissolve
    j "Encantada de conocerte, Ellen."
    show bg ch1sonja6 with dissolve
    j "Ahora, si no te importa, me gustaría hablar con mi marido. A solas."
    show bg ch1sonja9 with dissolve
    e "¡Qué carajo, [p]! ¡Pensé que estabas divorciado!"
    show bg ch1sonja10 with dissolve
    e "A la mierda con esto. No me voy a involucrar en tus mierdas."
    show bg ch1sonja11 with dissolve
    j "Ahora, [p], ven aquí y siéntate. Tenemos que hablar."
    show bg ch1sonja13 with dissolve
    p "¿Era necesario, Sonja? Ella no se merecía eso."
    j "Escucha, [p], lo siento si he asustado a tu nueva compañera de juerga. No era mi intención."
    p "Sí, lo hiciste, [j]."
    show bg ch1sonja41 with dissolve
    j "Bueno, me has pillado. Tal vez lo intenté. Solo por diversión. Deberías probar un poco."
    jump ch1sonjacontinue

label ch1sonjafuta:
    $ renpy.end_replay()
    if not persistent.ch1futa:
        $ persistent.ch1futa = True
        $ renpy.notify(['Escena desbloqueada', 'unlock'])
    show bg ch1sonja26 with hpunch
    p "¿QUÉ MIERDA? ¡Sam, luces!"
    show bg ch1sonja27 with dissolve
    $ insult = renpy.random.choice(insults)
    j "Hola, mierdecilla."
    p "¡Sonja! Vete a la mierda."
    if "ch1futafull" in extraevents:
        show bg ch1sonja29 with dissolve
        j "¿He interrumpido algo?"
        p "*suspira* Me cago en la puta…"
        show bg ch1sonja30 with dissolve
        j "¡JA JA JA! Me alegro mucho de que limpiar esa mierda ya no sea mi responsabilidad."
        p "Ríete."
    else:
        show bg ch1sonja29 with dissolve
        j "Estás un poco pálido, más que de costumbre."
        p "*suspira*"
        show bg ch1sonja30 with dissolve
        j "¡JA JA JA! Lo siento. ¿Sam decidió empujar los límites de nuevo?"
        p "Se podría decir que..."

    p "Bueno, tú siempre en el momento más inoportuno. ¿Solo esperas el momento perfecto para irrumpir?"
    show bg ch1sonja28 with dissolve
    j "Eso es lo que hacen las esposas. O ex esposas. Lo que sea que seamos ahora."


label ch1sonjacontinue:
    p "¿Cómo has entrado?"
    show bg ch1sonja42 with dissolve
    j "Sam me dejó entrar."
    p "¿Sam, pero qué mierda?"
    s "¿Si señor?"
    p "¡Cállate, Sam!"
    show bg ch1sonja14 with dissolve
    j "Memes aparte, [p], vine porque escuché un rumor de que te convertiste en un solitario. Que ahora, básicamente, estás fuera del negocio."
    p "¿Cómo?"
    $ insult = renpy.random.choice(insults)
    show bg ch1sonja43 with dissolve
    j "Vaya pregrunta, estupido. He seguido a Duchamps por cinco países. ¿Crees que vigilar a mi ex es difícil?"
    p "No estoy fuera del juego, Sonja. Solo soy exigente."
    show bg ch1sonja42 with dissolve
    j "Lo siento, su alteza, no sabía que estaba por encima del trabajo honesto."
    p "Yo solo..."
    j "¿Me convertí en un marica?"
    show bg ch1sonja17 with dissolve
    j "¡Vamos! Acepta unos cuantos trabajos. Vuelve al campo de batalla."
    p "Los trabajos han sido una mierda."
    show bg ch1sonja42 with dissolve
    j "Mierda o no, [p], sigue así y dejarás de recibir ofertas. ¿Entonces qué harás?"

    menu:
        "No necesito esto":
            $ dep += 1
            p "Ya tengo suficiente con la mierda esa de Ellen, gracias. No lo necesito."
            show bg ch1sonja39 with dissolve
            j "Perece que le importas. Al menos uno de ustedes debería."
            p "Sonja, déjalo ya."
            j "Tienes que seguir adelante, idiota. Vive tu puta vida."
            p "Me va bien."
            show bg ch1sonja40 with dissolve
            j "Por ahora. ¿Y el año que viene, cuando se te acabe el dinero? O, digamos que renuncias a la vida, ¿entonces qué? ¿Vas a vender seguros? ¿Colocar mesas? Has nacido para el trabajo Fantasma, [p]."
        "Lo sé":

            p "Lo sé, Sonja. Solo... Algo no está bien en este trabajo."
            show bg ch1sonja40 with dissolve
            j "Y esa intuición es la razón por la que te quieren. Sabes que esto no es un simple robo. Sea lo que sea, es grande."
            j "Desde que volví a la ciudad, me han llamado media docena de contratistas y no soy la única. Estoy segura de que está relacionado con esto."

    p "Mira, ya todo está hecho. Solo déjame consultarlo con la almohada."
    show bg ch1sonja41 with dissolve
    j "No estoy aquí para romperte las pelotas. Solo quiero lo mejor para ti. Además, si conseguimos contratos competitivos, puedo finalmente patear tu trasero..."
    p "No tendrías ninguna oportunidad."
    $ insult = renpy.random.choice(insults)
    j "Sigue soñando, puto."
    show bg ch1sonja44 with dissolve
    j "¡Hijo de puta!"
    j "¿Eso es lo que creo?"
    p "¿Qué?"
    show bg ch1sonja18 with dissolve
    j "[p], ¡bastardo negligente!"
    p "¿Y ahora qué, [j]?"
    show bg ch1sonja19 with dissolve
    j "¡Has dejado a Stella sola! Mírala. ¡Está asquerosa!"
    p "Aparte de polvo y falta de cuidado, está tal y como la dejaste."
    show bg ch1sonja21 with dissolve
    j "Oh, cariño, te he echado de menos. Él te dejó sola, pobrecita. Bueno, al menos te mantuvo a salvo."
    show bg ch1sonja22 with dissolve
    j "¿Por qué no la vendiste, [p]?"
    p "¿Vender a Stella? Ni hablar. Lo que sea que haya pasado entre nosotros, [j], nunca fue tu culpa."
    j "Tampoco fue la tuya."
    p "Y me imaginé que volverías por ella algún día. Solo pensé que sería en un mejor momento."
    show bg ch1sonja23 with dissolve
    j "*Besa a Stella*"
    j "¡Gracias!"
    show bg ch1sonja24 with dissolve
    p "Sabes, tu presencia aquí fue sospechosamente perfecta, casi como si alguien te hubiera puesto en esto."
    show bg ch1sonja32 with dissolve
    j "No seas así, [p]. Que yo llegue a la ciudad ahora, es una coincidencia. ¿Lo demás? Como he dicho, tengo mis metodos."
    j "Pero cuando un contrato tan grande flota por ahí, no soy la única que se enterará."
    j "Solo seré la primera."
    p "¿Así que estás aquí para qué? ¿Una charla motivacional?"
    j "¿Por qué no? Pronto nos lo entregarán al resto de nosotros. Deberías tener una ventaja al menos."
    p "Le dije a Ellen que lo pensaría."
    $ insult = renpy.random.choice(insults)
    j "Bueno, no lo pienses mucho, cabrón... te estás quedando rápidamente sin contratistas que quieran trabajar contigo."
    j "Solo haz esta. Por mí, ¿de acuerdo? Será bueno para ti."
    show bg ch1sonja33 with dissolve
    if "ch1ellen" in extraevents:
        j "Es tarde, [p]. Debería volver a casa. Me alegro de haberte encontrado con una mujer y no sosteniendo en una botella."
    else:
        j "Es tarde, [p]. Debería volver a casa. Me alegro de haberte encontrado con la mano en la verga y no sosteniendo en una botella."

    show bg ch1sonja34 with dissolve
    j "Por cierto, puedes quedarte con esa vieja reliquia. Con Stella aquí, ya no necesito esa antigüedad."
    show bg ch1sonja35 with dissolve
    p "Gracias. Probablemente acumulará más polvo."
    show bg ch1sonja36 with dissolve
    j "Oye, duerme un poco. Luego me cuentas tu decisión."
    p "Lo haré."
    $ insult = renpy.random.choice(insults)
    show bg ch1sonja37 with dissolve
    j "Hasta luego, estupido."
    p "Que te den."
    j "No lo digas si no lo sientes."
    jump ch1bed
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
