image bg ch1alley1 = "ch1alley1"
image bg ch1alley2 = "ch1alley2"
image bg ch1alley3 = "ch1alley3"
image bg ch1alley4 = "ch1alley4"
image bg ch1alley5 = "ch1alley5"
image bg ch1alley6 = "ch1alley6"
image bg ch1alley7 = "ch1alley7"
image bg ch1alley8 = "ch1alley8"
image bg ch1alley9 = "ch1alley9"
image bg ch1alley10 = "ch1alley10"
image bg ch1alley11 = "ch1alley11"
image bg ch1alley12 = "ch1alley12"
image bg ch1alley13 = "ch1alley13"
image bg ch1alley14 = "ch1alley14"
image bg ch1alley15 = "ch1alley15"
image bg ch1alley16 = "ch1alley16"
image bg ch1alley17 = "ch1alley17"
image bg ch1alley18 = "ch1alley18"

image bg ch1alleyblow movie = Movie(play="video/chapter-1-video/ch1alleyblow.webm")
image bg ch1alleybehind movie = Movie(play="video/chapter-1-video/ch1alleybehind.webm")


label ch1alley:
    if _in_replay:
        play music audio.aftermath fadein 2.0 fadeout 2.0
        $ setReplay()
    $ extraevents.append("ch1chandra")
    $ renpy.music.set_volume(0.6, 0, 'music')
    show bg ch1alley2 with Dissolve(1)
    c "Sigue la luz, agente."
    p "La sigo."
    show bg ch1alley1 with dissolve
    c "Mmm, siempre he querido esto."
    p "Y siempre conseguías lo que querías."
    show bg ch1alley3 with dissolve
    c "¿Cómo fue que me llamaste? Pendeja malcriada? Pero tú nunca me has malcriado, ¿verdad?"
    show bg ch1alley4 with dissolve
    p "¿Así que eso es lo que quieres?"
    c "Sí, consiénteme, [p]."
    p "Quizá si eres una buena chica."
    c "¿Seguro que no quieres que sea mala?"
    $ resetmenu()
    jump ch1alleymenu

label ch1alleymenu:
    menu:
        "Inclínate":
            $ menu1 = False
            jump ch1alleybend
        "De rodillas":

            $ menu1 = False
            jump ch1alleyblow

        "Eyacular" if menu1 == False:
            jump ch1alleycum


label ch1alleyblow:
    p "De rodillas."
    show bg ch1alley10 with dissolve
    c "Sí, trae esa verga aquí."
    show bg ch1alley11 with dissolve
    p "No, tú haz el trabajo, Chandra."
    show bg ch1alley12 with vpunch
    c "*Tiene arcadas cuando tu pene se desliza profundamente por su boca*"
    show bg ch1alleyblow movie with dissolve
    c "¡Oh! ¡Mmm!{w} ¡Dame tu verga!"
    p "¡Dios! ¿Cuánto tiempo llevas en esto?"
    c "Mmm..."
    show bg ch1alley13 with dissolve
    p "Olvida lo que te he preguntado."
    jump ch1alleymenu

label ch1alleybend:
    p "Inclínate y ponte junto a la pared. Vas a tener que sujetarte."
    show bg ch1alley5 with dissolve
    c "Y dijiste que no me ibas a consentir."
    play sound audio.slapeffect
    show bg ch1alley6 with hpunch
    "{size=+8}¡TOMA NALGADA!{/size}"
    show bg ch1alley7 with dissolve
    p "Mierda, estás apretada."
    c "Mejor que esas viejas zorras con las que sueles estar. {w} Soy joven y apretada, justo como te gusta."
    show bg ch1alleybehind movie with dissolve
    c "Cógeme, [pl]."
    c "¡Trátame como la puta rica y mimada que soy!"
    show bg ch1alley8 with dissolve
    c "¡Sí! ¡Haz que me corra!"
    show bg ch1alley9 with dissolve
    c "Mmm..."
    p "Ves, al final siempre consigues lo que quieres."
    jump ch1alleymenu


label ch1alleycum:
    p "Ahora, pruébalo, niña."
    show bg ch1alley14 with dissolve
    c "Sí, alimenta..."
    show bg ch1alley15 with quickflash
    $ renpy.pause(0.5)
    show bg ch1alley16 with dissolve
    c "me..."
    show bg ch1alley17 with dissolve
    c "¡Fue divertido! Deberíamos repetirlo."
    p "Probablemente no. {w} Vete a casa, Chandra. Tienes lo que querías.{w} Tengo cosas que hacer."
    $ renpy.end_replay()
    if not persistent.ch1chan:
        $ renpy.notify(['Escena desbloqueada', 'unlock'])
        $ persistent.ch1chan = True
    pt "(Es hora de reunirse con Ellen.)"
    jump ch1afterback
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
