image bg ch1gloriaware1 = "ch1gloriaware1"
image bg ch1gloriaware2 = "ch1gloriaware2"
image bg ch1gloriaware3 = "ch1gloriaware3"
image bg ch1gloriaware4 = "ch1gloriaware4"
image bg ch1gloriaware5 = "ch1gloriaware5"
image bg ch1gloriaware6 = "ch1gloriaware6"
image bg ch1gloriaware7 = "ch1gloriaware7"
image bg ch1gloriaware8 = "ch1gloriaware8"
image bg ch1gloriaware9 = "ch1gloriaware9"
image bg ch1gloriaware10 = "ch1gloriaware10"
image bg ch1gloriaware11 = "ch1gloriaware11"
image bg ch1gloriaware12 = "ch1gloriaware12"
image bg ch1gloriaware13 = "ch1gloriaware13"
image bg ch1gloriaware14 = "ch1gloriaware14"
image bg ch1gloriaware15 = "ch1gloriaware15"
image bg ch1gloriaware16 = "ch1gloriaware16"
image bg ch1gloriaware17 = "ch1gloriaware17"
image bg ch1gloriaware18 = "ch1gloriaware18"
image bg ch1gloriaware19 = "ch1gloriaware19"
image bg ch1gloriaware20 = "ch1gloriaware20"
image bg ch1gloriaware21 = "ch1gloriaware21"
image bg ch1gloriaware22 = "ch1gloriaware22"
image bg ch1gloriaware23 = "ch1gloriaware23"
image bg ch1gloriaware24 = "ch1gloriaware24"
image bg ch1gloriaware25 = "ch1gloriaware25"
image bg ch1gloriaware26 = "ch1gloriaware26"
image bg ch1gloriaware27 = "ch1gloriaware27"

image bg ch1afterdinner1 = "ch1afterdinner1"
image bg ch1afterdinner2 = "ch1afterdinner2"
image bg ch1afterdinner3 = "ch1afterdinner3"
image bg ch1afterdinner4 = "ch1afterdinner4"

label ch1glorianight:
    scene black with dissolve
    stop music fadeout 3.0
    show bg ch1afterdinner1 with Dissolve(3)
    pt "Bueno, Gloria Conner.{w} Es hora de saber dónde te has metido."
    play music audio.storm fadein 2.0
    play sound audio.thunder
    show bg ch1afterdinner2 with quickflash
    n "Los truenos iluminan el cielo nocturno."
    show bg ch1afterdinner3 with dissolve
    pt "Creo que es hora de dar por terminada la noche."
    show bg ch1afterdinner4 with Dissolve(3)
    $ renpy.pause(1)
    show bg ch1gloriaware1 with Dissolve(3)
    g "*Respira con fuerza*"
    show bg ch1gloriaware2 with dissolve
    g "Jeremy...{w} Cassie..."
    n "Se escuchan unos sonidos metálicos"
    show bg ch1gloriaware3 with dissolve
    g "¿Eh?"
    show bg ch1gloriaware6 with dissolve
    $ renpy.pause(1)
    show bg ch1gloriaware7 with dissolve
    "Meca policial" "Escaneando área."
    show bg ch1gloriaware4 with dissolve
    g "*Jadea y empieza a temblar*"
    show bg ch1gloriaware5 with dissolve
    "Robot policial" "Fuerza letal autorizada.{w} Encontrar el objetivo."
    play music audio.metalheavy fadein 8.0 fadeout 8.0
    scene black with Dissolve(2)
    show bg ch1gloriaware11 with Dissolve(2)
    "Hombre desconocido" "*Respiración rítmica*"
    "Hombre desconocido" "*En voz baja, susurra*{w} No encontrarás nada hoy."
    show bg ch1gloriaware12 with dissolve
    $ renpy.pause(1)
    show bg ch1gloriaware13 with dissolve
    "Hombre desconocido" "¡¡ARRRGGHH!!"
    n "Con un fuerte sonido, la bestia de acero se tambalea hacia adelante por el impacto"
    show bg ch1gloriaware14 with dissolve
    "Robot policial" "Encontrando nuevo objetivo."
    show bg ch1gloriaware15 with vpunch
    play sound audio.metalsmash
    n "El sonido de metal contra metal se estrella en una ráfaga de chispas, mientras un gigante se cae encima del otro"


    show bg ch1gloriaware8 with dissolve
    g "¡¡AHHHH!!"
    show bg ch1gloriaware16 with dissolve
    $ renpy.pause(1)
    show bg ch1gloriaware17 with dissolve
    "Hombre desconocido" "*GAARRHH*"
    show bg ch1gloriaware18 with dissolve
    $ renpy.pause(0.8)
    play sound audio.metalpunch
    show bg ch1gloriaware19 with hpunch
    n "*Sonido de golpe metálico*"
    play sound audio.metalpunch
    show bg ch1gloriaware20 with hpunch
    n "Los sonidos metálicos y de la carne resuenan junto al cielo lluvioso"
    show bg ch1gloriaware23 with dissolve
    "Hombre desconocido" "Es hora de que esto acabe."
    show bg ch1gloriaware21 with dissolve
    "Hombre desconocido" "*Grita con furia y rabia*"
    show bg ch1gloriaware22 with dissolve
    play sound audio.metalcrush
    n "El robot se queda corto mientras su cráneo es aplastado por las bestiales manos de su agresor"
    show bg ch1gloriaware24 with dissolve
    "Hombre desconocido" "*Respira con fuerza*"
    show bg ch1gloriaware25 with dissolve
    $ renpy.pause(2)
    show bg ch1gloriaware26 with dissolve
    n "El sonido de la batalla llega a su fin. Además de la lluvia, el único sonido es el suave llanto de Gloria"
    show bg ch1gloriaware10 with Dissolve(2)
    g "*¿Qué...?*"
    show bg ch1gloriaware27 with dissolve
    "Hombre desconocido" "No deberías haber huido."
    jump ch2gloria
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
