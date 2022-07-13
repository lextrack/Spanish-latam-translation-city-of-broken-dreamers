image bg ch1afterout0 = "ch1afterout0"
image bg ch1afterout0a = "ch1afterout0a"
image bg ch1afterout1 = "ch1afterout1"
image bg ch1afterout2 = "ch1afterout2"
image bg ch1afterout3 = "ch1afterout3"
image bg ch1afterout4 = "ch1afterout4"

image bg ch1aftermath1 = "ch1aftermath1"
image bg ch1aftermath2 = "ch1aftermath2"
image bg ch1aftermath3 = "ch1aftermath3"
image bg ch1aftermath4 = "ch1aftermath4"
image bg ch1aftermath5 = "ch1aftermath5"
image bg ch1aftermath6 = "ch1aftermath6"
image bg ch1aftermath7 = "ch1aftermath7"
image bg ch1aftermath8 = "ch1aftermath8"
image bg ch1aftermath9 = "ch1aftermath9"
image bg ch1aftermath10 = "ch1aftermath10"
image bg ch1aftermath11 = "ch1aftermath11"
image bg ch1aftermath12 = "ch1aftermath12"
image bg ch1aftermath13 = "ch1aftermath13"
image bg ch1aftermath14 = "ch1aftermath14"
image bg ch1aftermath15 = "ch1aftermath15"
image bg ch1aftermath16 = "ch1aftermath16"




label ch1aftermath:
    scene black with dissolve
    show text "{=trans}EN CAMINO Al AFTERMATH{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    show bg ch1afterout0a with dissolve
    pt "(La ciudad está en auge esta noche. Solo tengo que abrirme paso.)"
    show bg ch1afterout0 with dissolve
    pt "(Justo hacia el callejón de adelante.)"
    $ renpy.music.set_volume(0.1, 0, 'music')
    play music audio.aftermath fadein 2.0 fadeout 2.0
    show bg ch1afterout1 with dissolve
    pt "(A Ellen le debe encantar hacerme sufrir. Odio este maldito lugar.)"
    show bg ch1afterout2 with dissolve
    $ renpy.music.set_volume(0.2, 0, 'music')
    pt "(Los típicos ricachones.)"
    $ renpy.music.set_volume(0.3, 0, 'music')
    show bg ch1afterout4 with dissolve
    p "Oye, soy [p] [pl]. Déjame entrar."
    show bg ch1afterout3 with dissolve
    "*Sistema de seguridad*" "Por favor, quédese quieto para el escaneo de identificación."
    p "Sí, apúrate."
    "*Sistema de seguridad*" "Identidad confirmada. Bienvenido al Aftermath, [p] [pl]."
    $ renpy.music.set_volume(0.6, 0, 'music')
    show bg ch1aftermath6 with Dissolve(3)
    p "¿[c]? Tienes que estar de broma."
    c "¡La virgen puta, [p]! Ya me iba y AHORA las cosas se ponen interesantes."
    p "No lo creo, [c]. Estoy ocupado."
    show bg ch1aftermath5 with dissolve
    c "¡Ah, vamos! Tienes un par de minutos para una vieja amiga, ¿verdad?"
    p "En serio. Estoy aquí por negocios."
    "*Mujer desconocida*" "Mmm, parece divertido."
    "*Hombre desconocido*" "De ninguna manera, nena. Es espeluznante."
    show bg ch1aftermath7 with dissolve
    p "¿Sabe tu madre que estás aquí, [c]?"
    c "Que se joda esa perra. ¿Qué va a hacer, castigarme otra vez?"
    show bg ch1aftermath8 with dissolve
    c "Y no se lo vas a decir. La odias más que yo."
    p "..."
    c "Puedo verlo en tus ojos. Venga, vamos."
    $ renpy.music.set_volume(1, 0, 'music')
    show bg ch1aftermath3 with dissolve
    $ renpy.pause(2)
    show bg ch1aftermath4 with dissolve
    p "(Mierda, esta música es ensordecedora.)"
    c "¡OYE! ¡LOS OJOS SOBRE MÍ!"
    show bg ch1aftermath12 with dissolve
    p "¿QUÉ?"
    c "¡DIJE QUE DEJARAS DE MIRAR A ESA ZORRA!"
    p "¿ME CULPAS?"
    show bg ch1aftermath11 with dissolve
    c "¡ESTÁ MUY BUENA! ASÍ QUE..."
    show bg ch1aftermath1 with dissolve
    c "¡SUPONGO QUE NO!"
    show bg ch1aftermath2 with dissolve
    c "¡PERO ES VIEJA QUE TE CAGAS! ¡PODRÍA SER MEJOR!"
    show bg ch1aftermath13 with dissolve
    c "ALGO MÁS JOVEN, FRESCO, ¡PROHIBIDO! ¿QUÉ TE PARECE?"
    p "¡NO TENGO TIEMPO PARA ESTO CHANDRA!"
    menu:
        "Persíguela":
            p "¡EH, VUELVE AQUÍ!"
            show bg ch1aftermath9 with dissolve
            pt "(¿A dónde se fue la pendeja malcriada esa?)"
            show bg ch1aftermath10 with dissolve
            p "¡¿DÓNDE DEMONIOS HAS IDO?!"
            c "¡BOO!"
            show bg ch1aftermath15 with dissolve
            c "¡ME ATRAPASTE! ¡SUPONGO QUE ERES EL MEJOR FANTASMA EN EL NEGOCIO DESPUÉS DE TODO!"
            c "A MAMÁ LE DARíA UN PUTO INFARTO SI SUPIERA DONDE ESTOY, ¡SI SUPIERA QUE ESTOY CONTIGO!"
            p "NO ESTOY CONTIGO."
            c "¡PODRÍAS ESTARLO!"
            show bg ch1aftermath16 with dissolve
            c "¡VAMOS!"
            menu:
                "Síguela":
                    p "¡A la mierda...{w} VAMOS!"
                    jump ch1alley
                "Recházala":
                    p "¡ESTA VEZ NO, CHANDRA! {w}TENGO QUE IRME."
                    show bg ch1aftermath14 with dissolve
                    c "¡CARAJO! ¡LA PRÓXIMA VEZ ENTONCES! {w} ¡ANDA! ¡VE A HACER TUS MIERDA!"
                    jump ch1afterback
        "Llegaré tarde":
            pt "(Está demasiado loca, incluso para mí. Sin mencionar que si vuelvo a llegar tarde, Ellen me castrará...)"
            pt "(Vamos a la parte de atrás.)"
            jump ch1afterback
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
