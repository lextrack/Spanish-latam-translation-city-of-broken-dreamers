image bg ch1intro1 = "ch1intro1"
image bg ch1intro2 = "ch1intro2"
image bg ch1intro3 = "ch1intro3"
image bg ch1intro4 = "ch1intro4"
image bg ch1intro5 = "ch1intro5"
image bg ch1intro6 = "ch1intro6"
image bg ch1intro7 = "ch1intro7"
image bg ch1intro8 = "ch1intro8"

image bg ch1introb = "ch1introb"
image bg ch1introa = "ch1introa"


image ch1ghostmov = Movie(play='video/chapter-1-video/ch1ghost.webm', loop=False)
image bg ch1ghost movie:
    "ch1ghostmov"
    pause 2.0
    "ch1ghost"

image bg ch1prologue:
    "ch1prologue"
    yalign 0.5
    zoom 0.5
    alpha 1.0
    pause 1.0
    easeout 3.0 zoom 0.6 alpha 0.0


image bg ch1shots:
    "ch1introa"
    pause 0.10
    "ch1introa-2"
    pause 0.04
    "ch1introa"
    pause 0.04
    "ch1introa-2"
    pause 0.04
    "ch1introa"
    pause 0.04
    "ch1introa-2"
    pause 0.04
    "ch1introa"
    pause 0.2
    "ch1introa-2"
    pause 0.04
    "ch1introa"
    pause 0.04
    "ch1introa-2"
    pause 0.04
    "ch1introa"
    pause 0.04
    "ch1introa-2"
    pause 0.04
    "ch1introa"




label prologue:
    scene black with Dissolve(3)

    show bg ch1prologue with Dissolve(2)
    $ renpy.pause(2)
    scene black with Dissolve(3)
    play music audio.windeffect fadein 2.0
    show bg ch1introb with Dissolve(3)
    n "Los Angeles: 2042"
    show bg ch1introa with dissolve
    "???" "Lo juro... No sabemos nada."
    "???" "¡Déjanos en paz, por favor! No queremos..."
    play sound audio.silencer1

    show bg ch1shots

    "..."
    show bg ch1ghost movie with dissolve

    "Fantasma Alfa" "¿Por qué tuviste que hacer eso?"
    "Fantasma Beta" "Te has enterado de lo que le pasó al último equipo, ¿verdad?"
    show bg ch1intro4 with dissolve
    "Fantasma Beta" "Tienes que ser más cuidadoso."
    show bg ch1intro1 with dissolve
    "Fantasma Alfa" "¿Eres idiota?"
    show bg ch1intro2 with dissolve
    "Fantasma Beta" "Como si te importaran unos monstruos muertos."
    "Fantasma Alfa" "Quieres que te paguen, ¿verdad? La próxima vez sigue mis órdenes.{w} Ahora, mira si el grande y feo tiene algo. Tendré que buscar pistas, ya que no podemos interrogar a los muertos."
    show bg ch1intro3 with dissolve

    "Fantasma Beta" "Putos Milchers, cada día son más."
    "Hombre moribundo de aspecto extraño" "*Su respiración se ralentiza y se detiene*"
    "Fantasma Beta" "El bastardo está limpio. Solo tiene calzoncillos."
    show bg ch1intro5 with dissolve
    "Fantasma Alfa" "Eh, este podría pasar por humano. Me pregunto cuál fue su trato."
    "*Un teléfono suena*"
    "Fantasma Alfa" "Parece que estamos de suerte. Mira quién llama."
    show bg ch1intro6 with dissolve
    "Fantasma Beta" "No me jodas."
    show bg ch1intro7 with dissolve
    g "Chicos, ¿dónde están? Ellen está a punto de subir al escenario. Vengan rápido. ¿Tienes idea de lo difícil que es tener una mesa en el Noir?"
    "Fantasma Alfa" "Tenemos suerte."
    "Fantasma Beta" "¿Noir?"
    show bg ch1intro8 with dissolve
    "Fantasma Alfa" "El Tech Noir, un club en Mil-town. Venga, vamos. Es hora de cobrar."

    jump prologueclub
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
