image bg ch2breakfast1 = "ch2breakfast1"
image bg ch2breakfast2 = "ch2breakfast2"
image bg ch2breakfast3 = "ch2breakfast3"
image bg ch2breakfast4 = "ch2breakfast4"
image bg ch2breakfast5 = "ch2breakfast5"
image bg ch2breakfast6 = "ch2breakfast6"
image bg ch2breakfast7 = "ch2breakfast7"
image bg ch2breakfast8 = "ch2breakfast8"
image bg ch2breakfast9 = "ch2breakfast9"
image bg ch2breakfast10 = "ch2breakfast10"
image bg ch2breakfast11 = "ch2breakfast11"
image bg ch2breakfast12 = "ch2breakfast12"
image bg ch2breakfast13 = "ch2breakfast13"



label ch2breakfast:
    show bg ch2breakfast1 with Dissolve(2)

    if "ch1tellkatie" in extraevents:
        k "Esto es mejor que lo que comiste anoche con Victoria, créeme. El mejor banchan de la ciudad."
        p "Oye, los tragos no estuvieron tan malos. Confío en ti, Doc, pero si tengo que pasar el resto del día en el baño con las mierdas que sirven aquí..."
    else:
        k "Lo sé, no es mucho, pero créeme, tienen el mejor banchan de la ciudad, sin duda."
        p "Oye, los tragos no estuvieron tan malos. Confío en ti, Doc, pero si tengo que pasar el resto del día en el baño con las mierdas que sirven aquí..."
    show bg ch2breakfast3 with dissolve
    k "¡Gah, no quiero esa imagen mental!"
    p "Lo haces demasiado fácil, Doc. Por eso es tan divertido meterse contigo."
    show bg ch2breakfast2 with dissolve
    k "Bueno, deja de molestar, ¿ok?"
    p "Lo siento, no puedo evitarlo."
    show bg ch2breakfast4 with dissolve
    if k_score >= 2:
        k "En todo caso, es esto o la explosión de forúnculos llenos de pus."
        p "Entonces, ¿he vencido a esos?"
        k "Por poco."
    else:
        k "*En voz baja* Como los niños..."
        p "¿Qué?"
        k "*Suspira* Nada..."
    show bg ch2breakfast5 with dissolve
    k "Así que, obviamente no querías discutir esto en mi casa. ¿Qué está pasando?"
    show bg ch2breakfast7 with dissolve
    p "Meredith está involucrada... No me arriesgo."
    "Cocinero" "¿Qué van a ordenar?"
    show bg ch2breakfast6 with dissolve
    k "Solo dos números uno, por favor."
    p "Más vale que sea bueno."
    k "Oh, lo es."
    'Cocinero' "¡Ya mismo!"
    show bg ch2breakfast7 with dissolve
    k "Lo siento, espera. ¿Crees que mi casa tiene micrófonos?"
    p "Es posible. Siempre es mejor suponer."
    show bg ch2breakfast10 with dissolve
    k "Realmente sabes cómo empezar el día de una chica, [pl]. Lo mantienes interesante."
    p "Oh, el día acaba de empezar."
    k "Lo sé, todavía tengo cuerpos que examinar."
    if k_lust >= 1:
        show bg ch2breakfast13 with dissolve
        k "Y yo que pensaba que eras tú el que los hacía, con lo de ayer y la ducha."
        p "¡No era mi intención!"
        k "No pudiste evitarlo ¿eh?"
        p "..."
        show bg ch2breakfast12 with dissolve
        k "*Se ríe* Tengo que ponerme las vacunas en algún momento."
        p "Supongo que me lo merezco. Aunque vas a odiar lo que voy a decir a continuación."
        k "¿Qué?"
    show bg ch2breakfast11 with dissolve
    p "Los cuerpos aún están en el congelador de la policía en Lakewood."
    k "Estás de broma."
    p "¿Pasa algo con Mil-town?"
    k "No... quiero decir que mi clínica está cerca, pero... esa zona... He oído que no es muy segura."
    show bg ch2breakfast8 with dissolve
    p "Has oído bien."
    k "..."
    p "Estarás bien. Quédate cerca y haz lo que te digo."
    k "..."
    p "¿Lista para salir?"
    k "...Supongo que sí."

    jump ch2miltown
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
