image bg ch1subway0 = "ch1subway0"
image bg ch1subway1 = "ch1subway1"
image bg ch1subway2 = "ch1subway2"
image bg ch1subway3 = "ch1subway3"
image bg ch1subway4 = "ch1subway4"
image bg ch1subway5 = "ch1subway5"
image bg ch1subway6 = "ch1subway6"
image bg ch1subway7 = "ch1subway7"

image bg ch1corpvisit1 = "ch1corpvisit1"
image bg ch1corpvisit2 = "ch1corpvisit2"
image bg ch1corpvisit3 = "ch1corpvisit3"

image bg ch1hallway1 = "ch1hallway1"
image bg ch1hallway2 = "ch1hallway2"
image bg ch1hallway3 = "ch1hallway3"

image bg ch1iwastired1 = "ch1iwastired1"
image bg ch1iwastired2 = "ch1iwastired2"

image ch1panshot = Movie(play='video/chapter-1-video/panshot_car.webm', loop=False)
image bg ch1panshotmovie movie:
    "ch1panshot"
    pause 10.0
    "panshot_car"

image ch1ele = Movie(play='video/chapter-1-video/ch1iwastired.webm', loop=False)
image bg ch1elemovie movie:
    "ch1ele"
    pause 1.6
    "ch1iwastired2"

label ch1headtooffice:
    scene black with fade
    play music audio.tense fadein 2.0 fadeout 2.0
    show text "{=trans}DE CAMINO A INDUSTRIAS BAYNARD{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    show bg ch1subway0 with Dissolve(2)
    pt "(Aquí entramos al vientre de la bestia.)"
    show bg ch1subway1 with dissolve
    pt "(Pobre hombre. Probablemente no tenga más de treinta años, pero parece un anciano.)"
    show bg ch1subway2 with dissolve
    pt "(Lo lleva peor que la mayoría.)"
    show bg ch1subway3 with dissolve
    pt "(Probablemente limpiando para las élites ricas del centro de la ciudad. Pobre bastardo...)"
    show bg ch1subway4 with dissolve
    pt "(Bueno, el tranvía me llevará allí.)"
    show bg ch1subway5 with dissolve
    pt "(Quizá anticuado, pero siempre fiable.)"
    show bg ch1subway6 with dissolve
    pt "(Me pregunto qué es tan importante para que tenga que ir.)"
    show bg ch1subway7 with dissolve
    pt "(¿Qué mierda querrá?)"
    scene black with Dissolve(2)
    play sound audio.subway loop fadein 2.0
    show bg ch1panshotmovie movie with Dissolve(2)
    pt "(Tiene el valor de pedirme que vuelva.)"
    pt "(Especialmente después de la mierda que hizo.)"
    scene black with Dissolve(2)
    stop sound fadeout 2.0
    $ renpy.pause(1)
    show bg ch1corpvisit1 with dissolve
    if not persistent.glos_bay:
        $ persistent.glos_bay = True
        $ renpy.notify(['Glosario actualizado', 'glossary'])
    pt "(Aquí estamos... {color=#359eff}Industrias Baynard{/color}.)"
    show bg ch1corpvisit2 with dissolve
    pt "(Son un montón de basuras con doble moral.)"
    show bg ch1corpvisit3 with dissolve
    pt "(Actúan como si les importara.)"
    show bg ch1iwastired1 with dissolve
    pt "(Ha pasado mucho tiempo...)"
    show bg ch1elemovie movie with dissolve
    pt "(Ahora, al nido de la bruja.)"
    show bg ch1hallway1 with Dissolve(1)
    $ renpy.pause(1)
    show bg ch1hallway2 with dissolve
    pt "(Pero no tengo ganas de hacer esto.)"
    show bg ch1hallway3 with dissolve
    m "La puerta está abierta, agente."
    jump ch1meredith
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
