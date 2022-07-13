image bg ch2miltown1 = "ch2miltown1"
image bg ch2miltown2 = "ch2miltown2"
image bg ch2miltown3 = "ch2miltown3"
image bg ch2miltown4 = "ch2miltown4"
image bg ch2miltown5 = "ch2miltown5"
image bg ch2miltown6 = "ch2miltown6"
image bg ch2miltown7 = "ch2miltown7"
image bg ch2miltown8 = "ch2miltown8"
image bg ch2miltown9 = "ch2miltown9"
image bg ch2miltown10 = "ch2miltown10"
image bg ch2miltown11 = "ch2miltown11"
image bg ch2miltown12 = "ch2miltown12"
image bg ch2miltown13 = "ch2miltown13"
image bg ch2miltown14 = "ch2miltown14"
image bg ch2miltown15 = "ch2miltown15"
image bg ch2miltown16 = "ch2miltown16"
image bg ch2miltown17 = "ch2miltown17"
image bg ch2miltown18 = "ch2miltown18"
image bg ch2miltown19 = "ch2miltown19"
image bg ch2miltown20 = "ch2miltown20"
image bg ch2miltown21 = "ch2miltown21"
image bg ch2miltown22 = "ch2miltown22"
image bg ch2miltown23 = "ch2miltown23"
image bg ch2miltown24 = "ch2miltown24"
image bg ch2miltown25 = "ch2miltown25"
image bg ch2miltown26 = "ch2miltown26"
image bg ch2miltown27 = "ch2miltown27"
image bg ch2miltown28 = "ch2miltown28"
image bg ch2miltown29 = "ch2miltown29"
image bg ch2miltown30 = "ch2miltown30"
image bg ch2miltown31 = "ch2miltown31"
image bg ch2miltown32 = "ch2miltown32"
image bg ch2miltown33 = "ch2miltown33"
image bg ch2miltown34 = "ch2miltown34"
image bg ch2miltown35 = "ch2miltown35"
image bg ch2miltown36 = "ch2miltown36"
image bg ch2miltown37 = "ch2miltown37"
image bg ch2miltown38 = "ch2miltown38"
image bg ch2miltown39 = "ch2miltown39"
image bg ch2miltown40 = "ch2miltown40"


image ch2miltown = Movie(play='video/chapter-2-video/ch2miltown.webm', loop=False)
image bg ch2miltown movie:
    "ch2miltown"
    pause 5.68
    "ch2miltown-end"


label ch2miltown:

    play music audio.stress fadein 2.0 fadeout 2.0

    scene black with Dissolve(2)
    show text "{=trans}UN TIEMPO DESPUÉS, EN LO MÁS PROFUNDO DE MIL-TOWN{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    show bg ch2miltown1 with dissolve
    p "Relájate, Doc. Quédate cerca y trata de no sobresalir demasiado."
    window hide
    show bg ch2miltown movie with dissolve
    $ renpy.pause()
    window show
    k "Es peor de lo que imaginaba."
    p "Es lo que hay."
    show bg ch2miltown2 with dissolve
    k "Me pone furiosa. ¿Cómo podemos dejar que la gente viva así? ¿Solo porque se enfermaron?"
    p "Enfurecéte todo lo que quieras, Doc. Aquí... no importa lo que pienses, solo eres un recordatorio para esta gente de lo mierda que es su vida."
    p "Y eso es lo último que necesitan."
    show bg ch2miltown3 with dissolve
    k "Tienes razón. Acabemos con esto."
    show bg ch2miltown4 with dissolve
    p "¡Oye! ¿Qué parte de \"mantente cerca\"..."
    show bg ch2miltown5 with dissolve
    k "[p], es horrible aquí fuera. Son solo personas..."
    p "Ahora no, Doc."
    show bg ch2miltown6 with dissolve
    k "Dije que tenías razón... y..."
    p "¡Doc, ponte detrás de mí!"
    show bg ch2miltown7 with dissolve
    k "[p]!"
    p "¿Qué pasa?"
    show bg ch2miltown8 with dissolve
    "Mujer pandillera" "Bueno, bueno, bueno, un par de advenedizos decidieron entrar en la guarida para jugar... Los imbéciles ricos nunca aprenden."
    p "Aléjate."
    show bg ch2miltown9 with dissolve
    "Gran pandillero" "¿Por qué iba a hacerlo si aún no hemos cogido tu dinero?"
    p "Vete a la mierda."
    "Gran pandillero" "Espera, yo te conozco."
    p "Oh... mierda."
    "Gran pandillero" "Eres el cabrón que insultó a la mujer de Marcus la otra noche."
    show bg ch2miltown10 with dissolve
    "Mujer pandillera" "¿Así que este es el idiota que hizo llorar a Julie?"
    p "Para ser justos, se lo merecía."
    "Mujer pandillera" "Pusiste a mi novio en el hospital."
    p "Era un estúpido."
    "Mujer pandillera" "Sesh... Yo digo que los matemos a ambos."
    show bg ch2miltown11 with dissolve
    "Sesh" "¿Así que este es el Fantasma? No parece tan duro."
    p "Última oportunidad. Aléjate."
    if not persistent.glos_bolters:
        $ persistent.glos_bolters = True
        $ renpy.notify(['Glosario actualizado', 'glossary'])
    "Sesh" "Ahora estás territorio  {color=#359eff}Bolter{/color}, no le hablas así a Sesh."
    show bg ch2miltown15 with dissolve
    p "Todo saldrá bien, Doc."
    k "[p], ¡son tres!"
    show bg ch2miltown17 with dissolve
    p "Si pasa algo, corre directamente por donde hemos venido. ¿Entiendes?"
    show bg ch2miltown12 with dissolve
    "Sesh" "No corras, guapa. Te atraparemos de todos modos."
    show bg ch2miltown13 with dissolve
    "Sesh" "Después, te arrojaremos a \"La Fosa\", a ver cuánto duras."
    show bg ch2miltown16 with dissolve
    k "[p], ni siquiera sé que es La Fosa."
    show bg ch2miltown14 with dissolve
    "Sesh" "Veamos de qué estás hecho Fantasma."
    show bg ch2miltown18 with dissolve
    "Sesh" "¡Atrapen al cabrón!"
    "*Los dos hombres se abalanzan hacia el paso subterráneo*"
    show bg ch2miltown19 with dissolve
    "*Mientras tu respiración se ralentiza. Esperas que los atacantes se acercan*"
    menu:
        "Termina con esto rápido":
            jump ch2miltownendit
        "Presume":
            $ k_lust += 1
            jump ch2miltownshowoff

label ch2miltownendit:
    p "Es como si atrajera a estos imbéciles."
    show bg ch2miltown20 with dissolve
    play sound audio.guneffect
    show bg ch2miltown21 with hpunch
    "*El disparo de la pistola crear un eco en el paso subterráneo*"
    show bg ch2miltown22 with dissolve
    "Mujer pandillera" "¡Agh! ¡Mierda!"
    show bg ch2miltown23 with dissolve
    "Mujer pandillera" "¡¿Cómo...?!"
    show bg ch2miltown24 with dissolve
    "Sesh" "¡Una mierda! ¿Cómo hiciste ese tiro?"
    p "Supongo que es suerte."
    "Sesh" "¿Qué?"
    p "Esa bala no te dio. ¿Quieres ver si tu suerte se mantiene de nuevo?"
    show bg ch2miltown25 with dissolve
    "Gran pandillero" "Sesh, Julie es pura basura después de todo... No vale la pena."
    show bg ch2miltown26 with dissolve
    p "Eso pensé. Ahora, la señorita y yo nos vamos. ¿Hemos terminado aquí, Sesh?"
    "Sesh" "Por supuesto, Fantasma. Vete."
    scene black with dissolve
    show bg ch2miltown37 with dissolve
    k "Podrías haberlos matado..."
    p "No. Además, si fallaba y le daba a uno de ellos, te tenía a ti para remendarlos."
    k "Graciosillo."
    jump ch2miltownstation



label ch2miltownshowoff:
    show bg ch2miltown27 with dissolve
    pt "(Primero)"
    "Gran pandillero" "¡Es hora de arreglarte esa bonita cara!"
    show bg ch2miltown28 with vpunch
    play sound audio.puncheffect
    n "Tu puño conecta con el pecho del pandillero y sientes cómo sus costillas se rompen por el impacto."
    show bg ch2miltown29 with dissolve
    "Gran pandillero" "*Grita de dolor*"
    p "Voy a tomar esto por un segundo, Guerrero del Camino."
    show bg ch2miltown30 with dissolve
    "Sesh" "¡ARRGH! ¡Vas a caer, Fantasma!"
    play sound audio.metalpunch
    show bg ch2miltown31 with hpunch
    "*En un movimiento fluido, coges el casco del pandillero caído y golpeas la cara de Sesh.*"
    p "(Segundo)"
    show bg ch2miltown32 with dissolve
    p "*Gruñes y arrojas el casco.*"
    play sound audio.puncheffect
    show bg ch2miltown33 with dissolve
    n "Cuando el casco choca con el rostro de la mujer, se cae con moto y todo."
    p "(Tercero)"
    show bg ch2miltown34 with dissolve
    p "Katie, ¿estás bien? ¿Katie?"
    show bg ch2miltown35 with dissolve
    k "¿Estás bromeando?"
    p "No. Katie, ¿estás bien?"
    k "Sí... Estoy bien."
    show bg ch2miltown36 with dissolve
    k "Podría habernos disparado..."
    p "No tenían ni idea. Aficionados."
    k "Siempre pensé que el \"cinco contra uno\" era un simple alarde machista. Pero... Dios..."
    p "Tenemos que movernos, Katie. No se quedarán allí mucho tiempo y los pandilleros siempre vuelven en mayor número."
    jump ch2miltownstation


label ch2miltownstation:
    scene black with Dissolve(3)
    show bg ch2miltown38 with dissolve
    k "¿Es esa la estación de policía? Parece un viejo centro comercial."
    p "Lo fue hace tiempo tal vez. Después de la última recesión, el Estado lo compró."
    show bg ch2miltown39 with dissolve
    "Robot policial" "Está entrando en una zona restringida. Muestre la identificación de la policía de Los Ángeles o la autorización requerida."
    p "Sam, haz lo tuyo, ¿sí?"
    s "Enviando autorización de seguridad, señor."
    show bg ch2miltown40 with dissolve
    "Robot policial" "Acceso concedido, Agente [p] [pl]. Puede entrar."
    jump ch2miltownstationinside
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
