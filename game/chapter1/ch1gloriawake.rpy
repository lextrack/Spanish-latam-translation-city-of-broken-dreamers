image bg ch1gloriawake1 = "ch1gloriawake1"
image bg ch1gloriawake2 = "ch1gloriawake2"
image bg ch1gloriawake3 = "ch1gloriawake3"
image bg ch1gloriawake4 = "ch1gloriawake4"
image bg ch1gloriawake5 = "ch1gloriawake5"
image bg ch1gloriawake6 = "ch1gloriawake6"
image bg ch1gloriawake7 = "ch1gloriawake7"
image bg ch1gloriawake8 = "ch1gloriawake8"
image bg ch1gloriawake9 = "ch1gloriawake9"
image bg ch1gloriawake10 = "ch1gloriawake10"
image bg ch1gloriawake11 = "ch1gloriawake11"
image bg ch1gloriawake12 = "ch1gloriawake12"
image bg ch1gloriawake13 = "ch1gloriawake13"
image bg ch1gloriawake14 = "ch1gloriawake14"
image bg ch1gloriawake15 = "ch1gloriawake15"
image bg ch1gloriawake16 = "ch1gloriawake16"
image bg ch1gloriawake17 = "ch1gloriawake17"



label ch1gloriawake:
    scene black with Dissolve(3)
    show bg ch1gloriawake3 with Dissolve(3)
    $ renpy.pause(1)
    show bg ch1gloriawake1 with dissolve
    $ renpy.pause(1)
    show bg ch1gloriawake2 with dissolve
    play music audio.worried fadein 2.0
    g "*Respira profundamente* ¿Eh?"
    show bg ch1gloriawake4 with dissolve
    g "*Respirar con dificultad* ¿Hola?"
    show bg ch1gloriawake5 with dissolve
    g "(¿Dónde estoy? Oh Dios, ¿dónde está mi ropa?)"
    n "Se oyen ruidos de tráfico en el exterior"
    g "(Tengo que salir de aquí...)"
    show bg ch1gloriawake10 with dissolve
    $ renpy.pause(1)
    show bg ch1gloriawake6 with dissolve
    g "*Golpea la pared suavemente*"
    show bg ch1gloriawake7 with dissolve
    g "(¿Está abierto? Oh, gracias.)"
    show bg ch1gloriawake8 with Dissolve(3)
    $ renpy.pause(2)
    scene black with Dissolve(3)
    show bg ch1gloriawake9 with Dissolve(3)
    "Hombre desconocido" "*Deja escapar un profundo suspiro* Maldita sea..."
    scene black with Dissolve(3)
    show bg ch1gloriawake11 with Dissolve(3)
    g "*Jadea mucho*"
    show bg ch1gloriawake12 with dissolve
    g "(Necesito encontrar ayuda.)"
    show bg ch1gloriawake13 with dissolve
    g "Ugh... Funcionará..."
    show bg ch1gloriawake14 with dissolve
    g "..."
    show bg ch1gloriawake15 with dissolve
    g "Oh, es asqueroso..."
    show bg ch1gloriawake16 with dissolve
    g "(Ahora, por la ayuda... ¿Pero dónde?)"
    n "El sonido del tráfico se hace más fuerte a medida que ella se acerca al final del callejón"
    g "(La policía... Iré a la policía...)"
    show bg ch1gloriawake17 with dissolve
    g "O no... ¡Mierda!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
