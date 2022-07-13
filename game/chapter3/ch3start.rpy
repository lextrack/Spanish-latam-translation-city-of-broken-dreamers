

image bg ch3road1 = "ch3road1"
image bg ch3road2 = "ch3road2"
image bg ch3road3 = "ch3road3"
image bg ch3road4 = "ch3road4"
image bg ch3road5 = "ch3road5"
image bg ch3road6 = "ch3road6"
image bg ch3road7 = "ch3road7"
image bg ch3road8 = "ch3road8"
image bg ch3road9 = "ch3road9"
image bg ch3road10 = "ch3road10"
image bg ch3road11 = "ch3road11"
image bg ch3road12 = "ch3road12"
image bg ch3road13 = "ch3road13"
image bg ch3road14 = "ch3road14"
image bg ch3road15 = "ch3road15"
image bg ch3road16 = "ch3road16"

image bg ch3gloriawake0 = "ch3passout1"
image bg ch3gloriawake1 = "ch3gloriawake1"
image bg ch3gloriawake2 = "ch3gloriawake2"
image bg ch3gloriawake3 = "ch3gloriawake3"
image bg ch3gloriawake4 = "ch3gloriawake4"
image bg ch3gloriawake5 = "ch3gloriawake5"


image ch3theroad = Movie(play='video/chapter-3-video/ch3road.webm', loop=False)
image bg ch3theroad movie:
    "ch3theroad"
    pause 8.73
    "ch3road17"


label ch3start:
    g "Uhhh..."
    n "Gloria está apunto de desmayarse"
    show bg ch3gloriawake0 with dissolve
    $ renpy.pause(1)
    show bg ch3gloriawake1 with hpunch
    scene black with Dissolve(5)
    stop music fadeout 2.0
    $ renpy.pause(2)
    "Helena" "¿Te has divertido?"
    show bg ch3road1 with dissolve
    g "Al principio, pero luego Tommy se puso pesado."
    "Helena" "¿Qué paso?"
    g "Fue... chicos estúpidos..."
    show bg ch3road2 with dissolve
    "Helena" "Bueno, pueden serlo. ¿Pero qué ha dicho?"
    g "Dijo que los conciertos eran una tontería y que Ellen era una tonta y que quién iba a querer ir a un concierto si se podía transmitir todo por streaming."
    "Helena" "¿Le has contado lo del fin de semana pasado?"
    g "¡Eh! ¡Fue genial! Pero luego, él empezó a decir todas estas cosas malas."
    "Helena" "Estoy segura de que no lo dijo en serio. Solo estaba celoso de que te lo estuvieras pasando tan bien."
    g "Luego se burló de Donut."
    show bg ch3road3 with dissolve
    "Helena" "Eso sí que no se puede soportar, Guisante Dulce. Pero estoy seguro de que se disculpará pronto. Tal vez podamos invitarlo la próxima vez."
    g "¿Deberíamos?"
    "Helena" "Lo dejaré a tu criterio."
    g "Oye, mamá, ¿cómo es que no dejas que el auto se conduzca solo como hace papá?"
    show bg ch3road4 with dissolve
    "Helena" "Porque a veces, tu papá puede ser aburrido, Guisante Dulce."
    g "*Riendo* ¡Papá no es aburrido!"
    "Helena" "Cuando no es..."
    show bg ch3road5 with dissolve
    "Helena" "¿Qué ocurre?"
    g "¿Qué dijiste, mamá?"
    $ renpy.music.set_volume(0.6, 0, 'music')
    play music gunfire fadein 3.0
    n "Los gritos quiebran la calma del cielo nocturno; se le unen colisiones y disparos"
    "Helena" "¡Cariño, baja la cabeza!"
    show bg ch3road6 with dissolve
    $ renpy.music.set_volume(0.8, 0, 'music')
    n "Los gritos se hacen más fuertes a medida que la gente pasa corriendo por delante del auto, tratando desesperadamente de escapar de lo que sea que esté por delante"
    "Helena" "¿Qué es...? Gloria, espera..."
    play sound audio.explosioneffect
    show bg ch3road7 with hpunch
    play music audio.stress fadein 2.0 fadeout 2.0
    $ renpy.pause(0.5)
    show bg ch3road8 with dissolve
    "Helena" "¡¡GLORIA, AGUANTA!!"
    g "*Comienza a gritar* ¿¡MAMÁ!?"
    show bg ch3road9
    "Helena" "¡Cariño, todo irá bien! ¡Agacha la cabeza!"
    "Helena" "*En voz baja* Padre nuestro que estás en el cielo, santificado sea tu nombre. Venga tu reino, hágase tu voluntad..."
    n "Helena pone marcha atrás y pisa el acelerador. Los neumáticos chirrían mientras el auto se tambalea hacia atrás entre el tráfico detenido."
    show bg ch3road10
    "Helena" "¡Ahhh!"
    play sound audio.metalcrash
    n "La cabina se tambalea cuando otro vehículo choca contra ella, Helena se queda sin aliento por la fuerza del impacto"
    scene black with Dissolve(2)
    "Helena" "*Respiración agitada* Bebé..."
    show ch3road11 with Dissolve(3)
    g "¿Eh?"

    n "Los disparos en la distancia son más intensos que nunca. Al igual que los gritos."
    "Entidad desconocida" "*Ruge con un extraño sonido gutural*"
    g "*Rompe a llorar* ¡Mamá! ¿Qué está pasando?"
    g "¡¡MAMÁ!! ¡Levántate!"
    show bg ch3road12 with dissolve
    g "Mamá... *La voz de Gloria se quiebra de miedo, sus gritos son apenas audibles*"
    n "Una mano inhumana agarra el lateral del auto, otro se acerca a Helena"
    show bg ch3road13 with hpunch
    $ renpy.pause(0.5)
    show bg ch3road14 with dissolve
    n "Gloria observa aterrorizada cómo su madre es arrancada del asiento del conductor y lanzada por los aires como si fuera una simple muñeca"
    "Entidad desconocida" "*Continúa respirando rápidamente*"
    show bg ch3road15 with dissolve
    n "Gloria esta inmóvil, congelada por el miedo mientras la criatura le lanza una extraña mirada al pasar"
    scene black with Dissolve(2)
    n "El sonido de los disparos y los gritos de terror están ahora casi apagados, como si se reprodujeran en una pantalla de vídeo lejana"
    show bg ch3road16 with Dissolve(3)
    g "¿Mamá...? ¡Mamá! Por favor..."
    "Helena" "Está bien... todo estará bien... no llores..."
    show bg ch3theroad movie with dissolve
    "Helena" "Yo..."
    "..."
    g "Quién... ¿Quién eres?"
    stop music fadeout 2.0
    show bg ch3gloriawake1 with Dissolve(2)
    play music audio.calmmorning fadein 2.0 fadeout 2.0
    g "*Gime de susto*"
    show bg ch3gloriawake2 with dissolve
    h "¿Gloria? ¡Gloria! ¿Estás bien?"
    h "¡Vamos!"
    show bg ch3gloriawake3 with dissolve
    g "¿Henry?"
    h "¿Qué pasó?"
    g "Mamá... oh Dios... ¿Mamá?"
    show bg ch3gloriawake4 with dissolve
    h "Shh... está bien. Es sólo un sueño."
    g "Yo... no me había pasado esto en mucho tiempo, Bigs. Yo sólo..."
    h "No pasa nada, cariño."
    g "Sé lo que estoy soñando, pero no puedo cambiar nada. Siempre hay una parte de mí, que espera que {i}esta vez {/i} ella estará bien."
    h "Lo sé. Pero no puedes cambiar el pasado, Gloria."
    h "Y los sueños nunca cambia."
    show bg ch3gloriawake5 with dissolve
    g "Pero esa es la cuestión, Henry..."
    g "Esta vez, fue diferente... Alguien {i}estaba allí.{/i}"
    jump ch3wake
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
