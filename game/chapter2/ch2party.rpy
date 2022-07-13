image bg ch2party1 = "ch2party1"
image bg ch2party2 = "ch2party2"
image bg ch2party3 = "ch2party3"
image bg ch2party4 = "ch2party4"
image bg ch2party5 = "ch2party5"
image bg ch2party6 = "ch2party6"
image bg ch2party7 = "ch2party7"
image bg ch2party8 = "ch2party8"
image bg ch2party9 = "ch2party9"
image bg ch2party10 = "ch2party10"
image bg ch2party11 = "ch2party11"
image bg ch2party12 = "ch2party12"


label ch2party:
    play music audio.intro fadein 2.0 fadeout 2.0
    $ renpy.music.set_volume(0.5, 0, 'music')
    scene black with Dissolve(1)
    show bg ch2party1 with dissolve
    "Mujer desconocida" "Bienvenido. Diviértete."
    p "Ugh, gracias."
    show bg ch2party2 with dissolve
    "Mujer desconocida" "*Hablando con otras personas en el jacuzzi* Te deseo."
    show bg ch2party3 with dissolve

    if "ch2choosekatie" in extraevents:
        k "¿Qué fue eso? Ella parece... diferente."
        show bg ch2party6 with dissolve
        k "Bastante extraño."
        p "Estoy de acuerdo. Vigílala."
        show bg ch2party4 with dissolve
        k "Que te puedo decir."
        p "Lo siento, me han cogido con la guardia baja."
        show bg ch2party5 with dissolve
        k "¿A ti? ¿Con la guardia baja? ¿Qué tal si entramos? Necesitas mantenerte concentrado."
        p "Sí, probablemente tengas razón. Vamos."


    if "ch2chooseellen" in extraevents:
        e "Esta gente nunca cambia."
        show bg ch2party11 with dissolve
        p "¿En qué sentido?"
        e "Siempre tan insípidos."
        show bg ch2party10 with dissolve
        e "Siempre metiendo sus tetas falsas y sus cirugías en la cara de los demás. \"¡Mírenme!\" ¡Soy lo que todos quieren!"
        p "Parece que hablas por experiencia."
        e "He aguantado a un montón de perras falsas en mi vida."
        show bg ch2party12 with dissolve
        e "Venga, vamos a emborracharnos dentro. Si tenemos suerte, podremos captar el momento exacto en que un fideicomisario se da cuenta de lo insignificante que es su vida."
        p "¡Qué fría! "
        e "Tal vez, pero quiero verlo y lo sabes. Acabemos con esto."


    if "ch2choosevic" in extraevents:
        v "¿Distraído, agente?"
        show bg ch2party8 with dissolve
        v "Yo me distraigo con facilidad."
        p "Sí, probablemente tengas razón."
        p "¿Amiga tuya, tal vez?"
        show bg ch2party9 with dissolve
        v "Ja, no... Ni mucho menos."
        p "Entonces, ¿la conoces?"
        v "En cierto modo, sí."
        show bg ch2party7 with dissolve
        v "¿Vamos?"

    jump ch2partyindoor
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
