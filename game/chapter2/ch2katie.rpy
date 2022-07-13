

image bg ch2docmorning1 = "ch2docmorning1"
image bg ch2docmorning2 = "ch2docmorning2"
image bg ch2docmorning3 = "ch2docmorning3"
image bg ch2docmorning4 = "ch2docmorning4"
image bg ch2docmorning5 = "ch2docmorning5"
image bg ch2docmorning6 = "ch2docmorning6"
image bg ch2docmorning7 = "ch2docmorning7"
image bg ch2docmorning8 = "ch2docmorning8"
image bg ch2docmorning9 = "ch2docmorning9"
image bg ch2docmorning10 = "ch2docmorning10"
image bg ch2docmorning11 = "ch2docmorning11"
image bg ch2docmorning12 = "ch2docmorning12"





label ch2katie:
    scene black with Dissolve(1)
    show text "{=trans}45 MINUTOS DESPUÉS, EN LA CLÍNICA DE LA DRA. HAMILTON{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    show bg ch2docmorning1 with Dissolve(2)
    p "¡Eh Doc!, estoy a tiempo por primera vez ¿Estás lista?"
    k "*Se oyen ruidos en la parte de atrás* Dame un minuto."
    p "¿Doctora? ¿Dónde estás?"
    show bg ch2docmorning2 with dissolve
    p "(Oh, mierda.)"
    menu:
        "No digas nada":
            show bg ch2docmorning6 with dissolve
            k "¡Ahí estás! Sabía que no podías esconderte para siempre."
            show bg ch2docmorning5 with dissolve
            k "[p], ¡no te acerques así a una chica!"
            if k_score >= 1:
                p "No me he colado. No te preocupes, no vi nada. Esa taquilla es mucho más opaca que la ducha esa."
                show bg ch2docmorning4 with dissolve
                k "Bueno, vale, bien. Espera... ¿Pudiste ver a través de la puerta de la ducha?"
                p "Un poco, sí."
            else:
                p "No me he colado. No te preocupes, no vi nada."
                k "Bueno, está bien."
            if k_score >=1:
                if k_score >= 2:
                    show bg ch2docmorning3 with dissolve
                    k "¿Cuánto has visto?"
                    p "No mucho, no te preocupes. Sin travesuras. Solo fue un poco incómodo."
                    $ k_lust += 1
                else:
                    k "¿Y te quedaste ahí parado? ¿Mirando fijamente?"
                    p "Fue un momento incómodo."
        "Menciona que puedes verla":

            show bg ch2docmorning11 with dissolve
            p "*Se aclara la garganta* Sabes, la mayoría de los médicos que conozco tienden a ponerse blusas."
            show bg ch2docmorning4 with dissolve
            k "¿Qué crees que intento hacer?"
            p "Yo diría que buscando una blusa. Pero sé que no puede ser tan difícil como lo estás haciendo parecer."

    k "Lo siento. Oye, solo un segundo."
    show bg ch2docmorning12 with dissolve
    p "Pensé que eras una persona madrugadora, Doc. Estás arruinando la imagen que tengo de ti."
    show bg ch2docmorning7 with dissolve
    k "Tienes suerte de que me haya levantado de la cama para esto. Apenas puedo moverme sin cafeína. Debería conectar el café a una intravenosa e inyectarme."
    p "¿No es ilegal medicarse?"
    k "No empieces."
    show bg ch2docmorning8 with dissolve
    k "Entonces, ¿del centro al hospital, supongo?"
    p "Se podría pensar que sí. Pero no. ¿Por qué no vamos a desayunar y te lo explico?"
    show bg ch2docmorning9 with dissolve
    k "El desayuno suele ser el café."
    p "Sí."
    k "Podría ir. Hay un lugar coreano de camino. Sígueme."
    show bg ch2docmorning10 with dissolve
    p "Guíame, Doc."
    jump ch2breakfast
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
