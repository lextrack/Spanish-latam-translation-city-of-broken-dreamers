image bg ch2morning1 = "ch2morning1"
image bg ch2morning2 = "ch2morning2"
image bg ch2morning3 = "ch2morning3"
image bg ch2morning4 = "ch2morning4"
image bg ch2morning5 = "ch2morning5"
image bg ch2morning6 = "ch2morning6"
image bg ch2morning7 = "ch2morning7"
image bg ch2morning8 = "ch2morning8"
image bg ch2morning9 = "ch2morning9"
image bg ch2morning10 = "ch2morning10"





label ch2nextmorning:

    play music audio.calmmorning fadein 2.0 fadeout 2.0
    scene black with Dissolve(2)
    show text "{=trans}A LA MAÑANA SIGUIENTE{/=trans}" with Dissolve(1)
    $ renpy.pause(2)

    if "ch2chooseellen" in extraevents:
        jump ch2morningellen
    if "ch2choosevic" in extraevents and "ch2vic" in extraevents:
        jump ch2morningvic
    if "ch2choosekatie" in extraevents:
        jump ch2morningkatie
    if "ch2vicrefuse" in extraevents:
        show bg ch2morning2 with Dissolve(2)
        jump ch2morningover

label ch2morningellen:
    show bg ch2morning1 with Dissolve(2)
    e "Oye, idiota, me voy."
    p "¿No dormirás hasta el atardecer?"
    e "No, pasamos demasiado tiempo juntos y podrías hacerte una idea equivocada. Pero, si encuentras algo más sobre Gloria, házmelo saber."
    p "Sí, sí..."
    show bg ch2morning2 with dissolve
    jump ch2morningover


label ch2morningvic:
    show bg ch2morning3 with Dissolve(2)
    v "*Toma un largo respiro*"
    p "¿Estás bien?"
    v "Por supuesto, agente, ¿por qué no iba a estarlo?"
    if v_score >= 2:
        p "Te noto pensativa."
        show bg ch2morning4 with dissolve
        v "Por supuesto que sí. Esto está tardando más de lo que debería. Empezamos esta carrera tarde y seguimos perdiendo terreno."
        p "Sí, eso puede ser cierto, pero creo que es más que eso."
        v "..."
        if v_score >= 3:
            v "Tal vez. Además, antes de irme, debo disculparme por la inesperada visita de ayer."
            p "Eh... claro."
    show bg ch2morning5 with dissolve
    v "Ahora, si me perdonas, tengo que volver a la oficina. La Sra. White querrá una actualización."
    p "Meredith pide mucho."
    show bg ch2morning2 with dissolve
    jump ch2morningover

label ch2morningkatie:
    show bg ch2morning6 with Dissolve(2)
    $ renpy.pause(2)
    show bg ch2morning7 with Dissolve(2)
    k "*Bosteza* ¿Dónde estoy?"
    show bg ch2morning8 with dissolve
    k "[p], ¿estás despierto?"
    p "Sí. Buenos días, doctora. ¿Dormiste bien?"
    k "Mejor que tú, parece."
    p "He dormido en lugares peores, créeme."
    k "Deberías haber cogido la cama... Quiero decir..."
    p "¿Es una invitación?"
    show bg ch2morning9 with dissolve
    k "Yo... no... solo..."
    k "Debería haber ido a casa... Lo siento. Tengo que irme. Gracias por aguantarme."
    show bg ch2morning10 with dissolve
    p "Katie... ¡espera!"
    p "(Maldita sea.)"

label ch2morningover:
    p "*Suspira* El reloj está corriendo. Cuanto más tiempo pase, peores serán mis posibilidades."
    p "Necesito conseguir algo hoy. Y rápido."
    p "Sam, café. Un café doble."
    s "Sí, señor. Inmediatamente."
    p "Vamos a ver qué tiene Shanlon Russell para mí."
    jump ch2shanlon
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
