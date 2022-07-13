
image bg ch2elevator0 = "ch2elevator0"
image bg ch2elevator1 = "ch2elevator1"
image bg ch2elevator2 = "ch2elevator2"
image bg ch2elevator3 = "ch2elevator3"
image bg ch2elevator4 = "ch2elevator4"
image bg ch2elevator5 = "ch2elevator5"
image bg ch2elevator6 = "ch2elevator6"
image bg ch2elevator7 = "ch2elevator7"
image bg ch2elevator8 = "ch2elevator8"
image bg ch2elevator9 = "ch2elevator9"
image bg ch2elevator10 = "ch2elevator10"





label ch2elevator:
    scene black with Dissolve(2)
    show bg ch2elevator0 with dissolve
    "Robot de seguridad" "Invitación, por favor."
    p "Sam, transmite la invitación."
    s "Enviando invitación, señor. Diviértase."
    p "Claro, Sam."
    "Robot de seguridad" "Invitación aceptada para [p] [pl] y un invitado. Tenga en cuenta que esta invitación solo da acceso al ático."
    scene black with Dissolve(1)

    if "ch2choosekatie" in extraevents:
        show bg ch2elevator1 with dissolve
        k "Dios mío, ¿puedes tener esa vista?"
        p "Es bastante impresionante, lo sé."
        show bg ch2elevator2 with dissolve
        k "Impresionante. Es... bueno, todo es muy bonito."
        k "Vale, bonito es un eufemismo. Es como un mundo diferente."
        p "Pagan mucho dinero para que se sienta así. En fin ¿Estás lista?"
        show bg ch2elevator3 with dissolve
        k "¡Oh, claro! Preparada. Quiero decir, ¿por qué no iba a estar lista?"
        k "¿No parezco preparada?"
        p "Te ves muy bien."
        k "Claro... y por el lado bueno, nadie va a intentar robarnos."
        p "Roban a la gente todo el año; esta noche será un extraño día de descanso."



    if "ch2chooseellen" in extraevents:
        show bg ch2elevator6 with dissolve
        e "No puedo creer que esté haciendo esto."
        p "Piensa en ello como una actuación. Y no te metas en líos."
        show bg ch2elevator5 with dissolve
        e "Creí que querías que me lo tomara en serio."
        p "Un error de mi parte."
        show bg ch2elevator4 with dissolve
        e "Trataré de no golpear a Alex si lo veo."
        p "Eso sería estupendo."
        e "No obstante, no prometo nada."
        p "Tendré que creerte."


    if "ch2choosevic" in extraevents:
        show bg ch2elevator7 with dissolve
        p "¿También vives por aquí?"
        v "No es un ático, pero mi casa está justo ahí."
        p "Por supuesto que sí."
        show bg ch2elevator8 with dissolve
        v "¿Estás resentido por eso?"
        menu:
            "No hay problema con {i}eso{/i}":
                p "No tanto como el problema de para quién trabajas."
                show bg ch2elevator9 with dissolve
                v "Bueno, mi superior es mi preocupación, agente."
            "No":
                $ v_score += 1
                p "No, no es de mi incumbencia."
                show bg ch2elevator10 with dissolve
                if v_score >= 2:
                    v "No, no lo es, pero entiendo tu sentimiento."
                    p "¿Cómo?"
                    v "Ya casi hemos llegado [p]. Centrémonos."
                else:
                    v "Está bien. Debemos concentrarnos, ya casi llegamos."

    jump ch2party
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
