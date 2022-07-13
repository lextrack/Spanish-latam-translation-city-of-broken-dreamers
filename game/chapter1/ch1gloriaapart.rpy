
image bg ch1gloriaapart1 = "ch1gloriaapart1"
image bg ch1gloriaapart2 = "ch1gloriaapart2"
image bg ch1gloriaapart3 = "ch1gloriaapart3"
image bg ch1gloriaapart4 = "ch1gloriaapart4"
image bg ch1gloriaapart5 = "ch1gloriaapart5"
image bg ch1gloriaapart6 = "ch1gloriaapart6"
image bg ch1gloriaapart7 = "ch1gloriaapart7"
image bg ch1gloriaapart8 = "ch1gloriaapart8"
image bg ch1gloriaapart9 = "ch1gloriaapart9"
image bg ch1gloriaapart10 = "ch1gloriaapart10"
image bg ch1gloriaapart11 = "ch1gloriaapart11"

label ch1gloriaapart:
    scene black with dissolve
    stop music fadeout 3.0
    show text "{=trans}MÁS TARDE ESA NOCHE EN EL DEPARTAMENTO DE LOS AMIGOS DE GLORIA{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    show bg ch1gloriaapart4 with Dissolve(3)
    g "(¿Por qué no aparecieron la otra noche?)"
    show bg ch1gloriaapart2 with dissolve
    $ renpy.pause(1)
    show bg ch1gloriaapart1 with dissolve
    g "*Sale nerviosa a la calle y mira el edificio de sus amigos*"
    show bg ch1gloriaapart3 with dissolve
    play music audio.stress
    g "(Por favor, que esté bien...)"
    n "El sonido de las puertas delanteras abriéndose"
    show bg ch1gloriaapart9 with dissolve
    "Robot policial" "Número de la escena del crimen 7.8.4.5.2.2 catalogada. Traslado a la escena 7.8.4.5.2.3."
    "Robot policial" "Corrección, nuevas instrucciones. {w}Objetivo detectado."
    show bg ch1gloriaapart10 with dissolve
    "Robot policial" "Sospechosa Gloria Conner. Queda arrestada por el asesinato de Cassie y Jeremy Rocksford."
    show bg ch1gloriaapart5 with vpunch
    g "¿¡QUÉ!?"
    "Robot policial" "Ríndase o se utilizará la fuerza letal."
    show bg ch1gloriaapart6 with hpunch
    "Meca policial" "Objetivo encontrado."
    show bg ch1gloriaapart7 with dissolve
    "Meca policial" "Preparándose para participar. Ciudadano, mantenga la calma y levante las manos."
    show bg ch1gloriaapart8 with dissolve
    "Meca policial" "Esta es su última advertencia."
    show bg ch1gloriaapart11 with dissolve
    "Meca policial" "Perseguir el objetivo."
    scene black with Dissolve(3)
    jump ch1dinner
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
