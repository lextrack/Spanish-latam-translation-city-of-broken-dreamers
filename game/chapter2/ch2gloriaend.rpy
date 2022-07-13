
image bg ch2cer1 = "ch2cer1"
image bg ch2cer2 = "ch2cer2"
image bg ch2cer3 = "ch2cer3"
image bg ch2cer4 = "ch2cer4"
image bg ch2cer5 = "ch2cer5"
image bg ch2cer6 = "ch2cer6"
image bg ch2cer7 = "ch2cer7"
image bg ch2cer8 = "ch2cer8"
image bg ch2cer9 = "ch2cer9"
image bg ch2cer10 = "ch2cer10"




label ch2gloriaend:
    play music audio.calm fadein 2.0 fadeout 2.0
    scene black with Dissolve(3)
    show bg ch2cer1 with dissolve
    h "Lo siento, princesa, no hay mucha variedad."
    g "¿Coco Crunchers? Nunca tienes que disculparte por eso. Me trae recuerdos."
    g "¡Sooon muy buenos!"
    show bg ch2cer2 with dissolve
    h "Es difícil dejarlos una vez que empiezas."
    g "No me culpes por tu adicción, Bigs."
    h "Bigs... Hacía tiempo que no oía eso."
    show bg ch2cer3 with dissolve
    g "Tampoco había escuchado princesa en mucho tiempo."
    h "Tengo que hacer otro barrido de la vigilancia. ¿Estarás bien durante un rato?"
    show bg ch2cer5 with dissolve
    g "Esta vez no me escaparé."
    n "El silbido de un tranvía cercano resuena en la habitación"
    show bg ch2cer6 with Dissolve(2)
    g "Mmmm..."
    show bg ch2cer7 with dissolve
    n "Gloria mira fijamente el vaso, centrándose en la refracción de la luz."
    show bg ch2cer8 with dissolve
    $ renpy.pause(1)
    show bg ch2cer9 with Dissolve(2)
    n "El vaso se empieza a deslizar, ella tararea una canción distraídamente."
    play sound audio.shatter
    play music audio.metalheavy
    show bg ch2cer10 with dissolve
    n "Con un sonido estremecedor, el vaso se revienta en cientos de pedazos."

    g "*Se queda sorprendida luego del estruendo*"
    jump ch3start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
