image bg ch1gloria1 = "ch1gloria1"
image bg ch1gloria2 = "ch1gloria2"
image bg ch1gloria3 = "ch1gloria3"
image bg ch1gloria4 = "ch1gloria4"
image bg ch1gloria5 = "ch1gloria5"
image bg ch1gloria6 = "ch1gloria6"
image bg ch1gloria7 = "ch1gloria7"
image bg ch1gloria8 = "ch1gloria8"
image bg ch1gloria9 = "ch1gloria9"
image bg ch1gloria10 = "ch1gloria10"
image bg ch1gloria11 = "ch1gloria11"
image bg ch1gloria12 = "ch1gloria12"
image bg ch1gloria13 = "ch1gloria13"



image bg ch1gloriaclub1 = "ch1gloriaclub1"
image bg ch1gloriaclub2 = "ch1gloriaclub2"
image bg ch1gloriaclub3 = "ch1gloriaclub3"
image bg ch1gloriaclub4 = "ch1gloriaclub4"
image bg ch1gloriaclub5 = "ch1gloriaclub5"
image bg ch1gloriaclub6 = "ch1gloriaclub6"
image bg ch1gloriaclub7 = "ch1gloriaclub7"
image bg ch1gloriaclub8 = "ch1gloriaclub8"
image bg ch1gloriaclub9 = "ch1gloriaclub9"
image bg ch1gloriaclub10 = "ch1gloriaclub10"
image bg ch1gloriaclub11 = "ch1gloriaclub11"
image bg ch1gloriaclub12 = "ch1gloriaclub12"
image bg ch1gloriaclub13 = "ch1gloriaclub13"
image bg ch1gloriaclub14 = "ch1gloriaclub14"
image bg ch1gloriaclub15 = "ch1gloriaclub15"
image bg ch1gloriaclub16 = "ch1gloriaclub16"
image bg ch1gloriaclub17 = "ch1gloriaclub17"
image bg ch1gloriaclub18 = "ch1gloriaclub18"
image bg ch1gloriaclub19 = "ch1gloriaclub19"
image bg ch1gloriaclub20 = "ch1gloriaclub20"
image bg ch1gloriaclub21 = "ch1gloriaclub21"


label prologueclub:
    play music audio.darkclub fadein 4.0 fadeout 2.0
    scene black with Dissolve(2)
    show bg ch1gloriaclub2 with Dissolve(2)
    "Presentador" "Por favor, tomen asiento y no olviden sus bebidas."
    show bg ch1gloriaclub1 with dissolve
    "Presentador" "El espectáculo comenzará en breve."
    show bg ch1gloriaclub4 with dissolve
    "Joven" "*Suspira*"
    show bg ch1gloriaclub3 with dissolve
    "Joven" "¿Dónde están?"
    show bg ch1gloriaclub19 with dissolve
    "Mujer desconocida" "Te enviaré la información. Ellen, ¿puedes conseguir a alguien esta noche?"
    show bg ch1gloriaclub18 with dissolve
    e "Ya he dicho que sí. Solo vete. Me están esperando afuera."
    show bg ch1gloriaclub20 with dissolve
    "Mujer desconocida" "Lo sé, a mí también. Buena suerte, señorita Lane."
    show bg ch1gloriaclub21 with dissolve
    "Presentador" "¡Damas y caballeros! ¡La conocen! ¡La aman! ¡ELLEN LANE!"
    show bg ch1gloriaclub8 with dissolve
    "Hombre misterioso" "Me imaginé que te encontraría aquí."
    show bg ch1gloriaclub7 with dissolve
    "Hombre misterioso" "Deberías haber tenido más cuidado."
    show bg ch1gloriaclub15 with dissolve
    e "¡¿Cómo se encuentran esta noche?! ¿Listos para divertirse?"
    show bg ch1gloriaclub14 with dissolve
    e "Este es uno de mis favoritos. De mi primer álbum."
    show bg ch1gloriaclub16 with dissolve
    e "¡Dalen, chicos!"
    show bg ch1gloriaclub9 with dissolve
    "Fantasma Alfa" "La chica está aquí en alguna parte. ¡Encuéntrala!"
    show bg ch1gloriaclub17 with dissolve
    "Fantasma Alfa" "¡Dispérsense!"
    show bg ch1gloriaclub11 with dissolve
    "Fantasma Beta" "¡Gloria Conner! ¡Muéstrate!"
    show bg ch1gloriaclub10 with dissolve
    "Fantasma Alfa" "¡Allí está!"
    show bg ch1gloriaclub12 with dissolve
    "Fantasma Beta" "Lo siento, chica."
    show bg ch1gloriaclub13 with dissolve
    "Fantasma Beta" "No es nada personal."
    show bg ch1gloriaclub5 with dissolve
    $ renpy.pause(0.75)
    show bg ch1gloriaclub6 with dissolve
    g "Yo..."

    scene black with Dissolve(3)
    play sound audio.silencer1
    "Fantasma Alfa" "¿Qué mierda?"
    "Fantasma Alfa" "¿Quién mierda eres tú?"
    play sound audio.silencer1
    "Fantasma Beta" "¡No! ¡Espera! ¡Por favor!"
    play sound audio.silencer1
    "Fantasma Beta" "¡AAAAH!"
    show bg ch1gloria8 with dissolve
    n "Los gritos estallan mientras la gente huye del club."
    show bg ch1gloria7 with dissolve
    n "La chica baja las escaleras a trompicones."
    show bg ch1gloria9 with dissolve
    $ renpy.pause(1)

    show bg ch1gloria10 with dissolve
    n "Apenas nota el pánico a su alrededor."
    show bg ch1gloria11 with dissolve
    $ renpy.pause(1)


    show bg ch1gloria12 with dissolve
    $ renpy.pause(1)


    show bg ch1gloria13 with dissolve
    $ renpy.pause(1)


    play music audio.windeffect fadein 2.0 fadeout 2.0
    show bg ch1gloria1 with dissolve
    n "Conmocionada, corre tan rápido como puede. Lejos del club."
    show bg ch1gloria2 with dissolve
    n "Los gritos detrás de ella pronto se mezclan con las sirenas de la policía."
    show bg ch1gloria3 with dissolve
    n "Se tropieza."
    show bg ch1gloria4 with dissolve
    g "No... tengo que seguir..."
    show bg ch1gloria5 with dissolve
    g "Corriendo..."
    n "La chica se termina desmayando en las frías calles de Los Ángeles."
    show bg ch1gloria6 with Dissolve(3)
    $ renpy.pause(1)
    scene black with Dissolve(3)

    $ renpy.movie_cutscene("video/chapter-1-video/cobd-intro.webm", stop_music=True)
    jump ch1wake
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
