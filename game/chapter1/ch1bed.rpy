image bg ch1morning1a = "ch1morning1a"

image bg ch1morning1 = "ch1morning1"
image bg ch1morning2 = "ch1morning2"
image bg ch1morning3 = "ch1morning3"
image bg ch1morning4 = "ch1morning4"
image bg ch1morning5 = "ch1morning5"
image bg ch1morning6 = "ch1morning6"
image bg ch1morning7 = "ch1morning7"

image bg ch1dream1 = "ch1dream"
image bg ch1dream2 = "ch1dream2"
image bg ch1dream3 = "ch1dream3"
image bg ch1dream4 = "ch1dream4"

image bg ch1apartsleep = "ch1apartsleep"

label ch1bed:
    stop music fadeout 1.0
    p "Sam, apaga las luces. Quiero dormir."
    show bg ch1apartsleep with Dissolve(2)
    pt "*Bosteza* (Qué día... Lo consultaré con la almohada y le daré mi respuesta a Ellen mañana.)"
    scene black with Dissolve(3)
    show bg ch1dream1 with Dissolve(3)
    p "¡Esto es una mierda!"
    show bg ch1dream2 with dissolve
    j "Nos quedamos sin opciones, [p]."
    p "No podemos hacer esto. Sonja, es..."
    show bg ch1dream3 with dissolve
    j "No hay otra manera."
    p "No me importa... haremos esto... no hay que sentirse mal."
    show bg ch1dream4 with dissolve
    j "*Se ahoga* Lo sé..."


    call ch1gloriawake from _call_ch1gloriawake



    scene black with Dissolve(3)
    play music audio.calmmorning fadein 3.0 fadeout 3.0
    show bg ch1morning1a with Dissolve(3)
    $ renpy.pause(1)
    show bg ch1morning1 with Dissolve(2)
    p "*Gruñidos* Supongo que debería levantarme..."
    show bg ch1morning2 with dissolve
    p "*Se truena el cuello*"
    p "Sam, ¿qué hora es?"
    s "9:11 am, señor."
    show bg ch1morning3 with dissolve
    p "Bien, haz café."
    s "Sí, señor."
    s "Señor, tiene una llamada entrante."
    show bg ch1morning4 with dissolve
    p "¿Quién es?"
    s "Es Meredith White de Industrias Baynard."
    p "A la mierda. Cuelga."
    p "No espera... Contesta."
    show bg ch1morning5 with dissolve
    m "Levántate agente, [pl]."
    p "Ya no soy tu agente, Meredith."
    m "Como sea, espero que la mañana te este tratando bien."
    p "Que te den. Cuando Sonja apareció de nuevo, tuve el presentimiento de que vería tu cara tarde o temprano. Fuiste tú quien me lanzó este trabajo, ¿no? Debe ser bastante importante."
    show bg ch1morning6 with dissolve
    m "Como siempre, estás al tanto de todo, incluso cuando te esfuerzas por no estarlo. Tienes razón. Esto es importante. A diferencia de lo que pasa en tu 'trabajo', este trabajo importa."
    m "Por lo tanto, quiero que vengas para que podamos discutir esto en persona."
    p "Solo con ver tu cara, me dan menos ganas de hacer este trabajo."
    show bg ch1morning7 with dissolve
    m "Venga, ya me verás. Después de todo, ya sabes lo convincente que puedo ser, agente [pl]."
    p "..."
    show bg ch1morning5 with dissolve
    m "No me mires así, [pl]. No olvidemos que aún te queda un trabajo en tu contrato."
    p "Realmente eres una perra."
    m "¿Envío un dron de la compañía para que te recoja?"
    p "No necesito tu ayuda, llegaré por mi cuenta."
    m "Como quieras. Te estaré esperando en mi oficina. Ya sabes cómo llegar."
    p "Sí. Lo sé."
    jump ch1headtooffice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
