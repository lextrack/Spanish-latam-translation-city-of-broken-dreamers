image bg ch2partyhallway1 = "ch2partyhallway1"
image bg ch2partyhallway2 = "ch2partyhallway2"
image bg ch2partyhallway3 = "ch2partyhallway3"
image bg ch2partyhallway4 = "ch2partyhallway4"
image bg ch2partyhallway5 = "ch2partyhallway5"
image bg ch2partyhallway6 = "ch2partyhallway6"
image bg ch2partyhallway7 = "ch2partyhallway7"
image bg ch2partyhallway8 = "ch2partyhallway8"
image bg ch2partyhallway9 = "ch2partyhallway9"
image bg ch2partyhallway10 = "ch2partyhallway10"
image bg ch2partyhallway11 = "ch2partyhallway11"
image bg ch2partyhallway12 = "ch2partyhallway12"
image bg ch2partyhallway13 = "ch2partyhallway13"
image bg ch2partyhallway14 = "ch2partyhallway14"
image bg ch2partyhallway15 = "ch2partyhallway15"
image bg ch2partyhallway16 = "ch2partyhallway16"
image bg ch2partyhallway17 = "ch2partyhallway17"



label ch2upstairs:
    play music audio.worried fadein 2.0 fadeout 2.0
    scene black with Dissolve(1)
    show bg ch2partyhallway1 with dissolve
    p "Bien, veamos qué podemos encontrar."
    if "ch2choosekatie" in extraevents:
        show bg ch2partyhallway2 with dissolve
        k "[p], no sé qué me pasó. Te he defraudado."
        p "Katie, no pasa nada."
        show bg ch2partyhallway3 with dissolve
        k "Pero perdí los estribos y causé una escena. Y ahora lo arruiné todo. Y tu trabajo está arruinado porque yo... *Solloza*"
        p "Oye, no lo has estropeado todo. Lo hiciste bien, realmente lo hiciste. Era justo la distracción que necesitábamos para subir. La próxima vez el Banchan corre por mi cuenta."
        k "*Solloza* Te lo dije, el mejor de la ciudad."
        show bg ch2partyhallway4 with dissolve
        p "Además, se lo merecía."
        k "Sí, lo merecía, ¿verdad?"
        p "Maldita sea, es mejor que se olvide. En este momento, debe estar buscándonos."
        show bg ch2partyhallway1 with dissolve
        $ resetmenu()
        jump ch2partyhallwaymenukatie
    else:
        p "(¿Dónde primero?)"
        $ resetmenu()
        jump ch2partyhallwaymenu

label ch2partyhallwaymenukatie:
    menu:
        "Puerta de la izquierda" if menu1:
            $ menu1 = False
            p "Veamos qué hay en esa puerta de la izquierda."
            show bg ch2partyhallway5 with dissolve
            p "¿Algo?"
            k "..."
            show bg ch2partyhallway6 with dissolve
            k "No, nada."
            k "Nada de nada."
            p "¿Qué había allí?"
            show bg ch2partyhallway7 with dissolve
            k "Habitación de invitados o algo así."
            jump ch2partyhallwaymenukatie

        "Puerta del centro" if menu2:
            $ menu2 = False
            p "Central entonces."
            k "De acuerdo."
            call ch2partyhallwayoffice from _call_ch2partyhallwayoffice
            show bg ch2partyhallway1 with dissolve
            jump ch2partyhallwaymenukatie
        "Puerta de la derecha" if menu3:
            $ menu3 = False
            p "¿Qué hay a la derecha?"
            show bg ch2partyhallway8 with dissolve
            k "Déjame comprobarlo."
            p "¿Algo interesante?"
            show bg ch2partyhallway9 with dissolve
            k "[p], deberías ver esto."
            if menu2:
                menu:
                    "¿Qué es esto?":
                        p "¿Qué has encontrado?"
                        k "El dormitorio de la chica... No lo han manipulado ni un poco."
                    "Déjame comprobar esta otra puerta":
                        p "Un segundo, quiero comprobar esta otra puerta."
                        k "Sé rápido. Este allanamiento de morada me pone nerviosa."
                        p "Dame un minuto."
                        call ch2partyhallwayoffice from _call_ch2partyhallwayoffice_1
                        show bg ch2partyhallway9 with dissolve
                        k "¿Algo?"
                        p "Nada."
            else:
                p "¿Qué es esto?"
                k "El dormitorio de la chica... No lo han manipulado ni un poco."
                p "Bien, echemos un vistazo."
            jump ch2partybedroom

label ch2partyhallwaymenu:
    menu:
        "Puerta de la izquierda" if menu1:
            $ menu1 = False
            show bg ch2partyhallway12 with dissolve
            p "(Bien, veamos qué hay aquí.)"
            n "*Unos gruñidos proviene de la habitación*"
            if "vostokdoc" in extraevents and "ch2choosevic" in extraevents:
                show bg ch2partyhallway17 with hpunch
                n "¡No funciona! *gruñe* ¡Pedazo de chatarra!"
                p "(Vale, eso es combustible para pesadillas. Y después de algunas de las cosas que Sam me ha enviado... Esto es demasiado.)"
            else:
                show bg ch2partyhallway16 with dissolve
                "Mujer desconocida" "Siénteme."
                p "(Bien, eso era de esperar...)"
            jump ch2partyhallwaymenu
        "Puerta del centro" if menu2:
            $ menu2 = False
            p "(¿Qué tal esta puerta del centro?)"
            call ch2partyhallwayoffice from _call_ch2partyhallwayoffice_2
            show bg ch2partyhallway1 with dissolve
            jump ch2partyhallwaymenu
        "Puerta de la derecha":
            show bg ch2partyhallway13 with dissolve
            p "Revisemos esto."
            if menu1 or menu2:
                p "(Esto podría ser importante. Tal vez debería revisar las otras puertas primero.)"
                menu:
                    "Continua":
                        jump ch2partybedroom
                    "Comprueba las otras puertas":
                        jump ch2partyhallwaymenu
            jump ch2partybedroom


label ch2partyhallwayoffice:
    show bg ch2partyhallway14 with dissolve
    p "(Bien, está desbloqueado.)"
    show bg ch2partyellen1 with dissolve
    p "(Ahh, su oficina. Probablemente haya algo aquí.)"
    menu:
        "Mira a tu alrededor":
            p "(Veamos qué podemos encontrar.)"
            show bg ch2partyhallway15 with dissolve
            if not persistent.ch2card3:
                $ renpy.notify(['Posible pista', 'alert'])
                show screen hidden_item("ch2card3", "ch2card3", 95, 132, 320, 164)
            p "(Vaya vista.)"
            p "(Hmm, un montón de libros viejos. Ya no se ven tan a menudo.)"
            if persistent.ch2card3:
                p "(Ya tengo todo lo que necesito.)"
                hide screen hidden_item
                return
            else:
                p "(Debo haber pasado algo por alto. Revisaré otra puerta.)"
                hide screen hidden_screen
                return
        "Volver al pasillo":
            return
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
