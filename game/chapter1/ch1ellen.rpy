image bg ch1ellen1 = "ch1ellen1"
image bg ch1ellen2 = "ch1ellen2"
image bg ch1ellen3 = "ch1ellen3"
image bg ch1ellen4 = "ch1ellen4"
image bg ch1ellen5 = "ch1ellen5"
image bg ch1ellen6 = "ch1ellen6"
image bg ch1ellen7 = "ch1ellen7"
image bg ch1ellen8 = "ch1ellen8"
image bg ch1ellen9 = "ch1ellen9"
image bg ch1ellen10 = "ch1ellen10"
image bg ch1ellen11 = "ch1ellen11"
image bg ch1ellen12 = "ch1ellen12"
image bg ch1ellen13 = "ch1ellen13"
image bg ch1ellen14 = "ch1ellen14"
image bg ch1ellen15 = "ch1ellen15"
image bg ch1ellen16 = "ch1ellen16"
image bg ch1ellen17 = "ch1ellen17"
image bg ch1ellen18 = "ch1ellen18"
image bg ch1ellen19 = "ch1ellen19"
image bg ch1ellen20 = "ch1ellen20"
image bg ch1ellen21 = "ch1ellen21"
image bg ch1ellen22 = "ch1ellen22"
image bg ch1ellen23 = "ch1ellen23"
image bg ch1ellen24 = "ch1ellen24"
image bg ch1ellen25 = "ch1ellen25"
image bg ch1ellen26 = "ch1ellen26"
image bg ch1ellen27 = "ch1ellen27"
image bg ch1ellen28 = "ch1ellen28"
image bg ch1ellen29 = "ch1ellen29"
image bg ch1ellen30 = "ch1ellen30"
image bg ch1ellen31 = "ch1ellen31"
image bg ch1ellen32 = "ch1ellen32"
image bg ch1ellen33 = "ch1ellen33"
image bg ch1ellen34 = "ch1ellen34"
image bg ch1ellen35 = "ch1ellen35"
image bg ch1ellen36 = "ch1ellen36"
image bg ch1ellen37 = "ch1ellen37"
image bg ch1ellen38 = "ch1ellen38"
image bg ch1ellen39 = "ch1ellen39"
image bg ch1ellen40 = "ch1ellen40"
image bg ch1ellen41 = "ch1ellen41"
image bg ch1ellen42 = "ch1ellen42"
image bg ch1ellen43 = "ch1ellen43"
image bg ch1ellen44 = "ch1ellen44"
image bg ch1ellen45 = "ch1ellen45"
image bg ch1ellen46 = "ch1ellen46"
image bg ch1ellen47 = "ch1ellen47"
image bg ch1ellen48 = "ch1ellen48"
image bg ch1ellen49 = "ch1ellen49"
image bg ch1ellen50 = "ch1ellen50"
image bg ch1ellen51 = "ch1ellen51"
image bg ch1ellen52 = "ch1ellen52"
image bg ch1ellen53 = "ch1ellen53"
image bg ch1ellen54 = "ch1ellen54"
image bg ch1ellen55 = "ch1ellen55"
image bg ch1ellen56 = "ch1ellen56"
image bg ch1ellen57 = "ch1ellen57"
image bg ch1ellen58 = "ch1ellen58"
image bg ch1ellen59 = "ch1ellen59"
image bg ch1ellen60 = "ch1ellen60"
image bg ch1ellen61 = "ch1ellen61"
image bg ch1ellen62 = "ch1ellen62"
image bg ch1ellen63 = "ch1ellen63"
image bg ch1ellen64 = "ch1ellen64"
image bg ch1ellen65 = "ch1ellen65"
image bg ch1ellen66 = "ch1ellen66"
image bg ch1ellen67 = "ch1ellen67"



image bg ch1ellenride1 movie = Movie(play="video/chapter-1-video/ch1ellenride-1a.webm")
image bg ch1ellenride2 movie = Movie(play="video/chapter-1-video/ch1ellenride-2.webm")
image bg ch1ellenride3 movie = Movie(play="video/chapter-1-video/ch1ellenride-3.webm")
image bg ch1ellenride4 movie = Movie(play="video/chapter-1-video/ch1ellenride-4.webm")

image bg ch1ellenblowmovie movie = Movie(play="video/chapter-1-video/ch1ellenblow.webm")
image bg ch1ellenblow2movie movie = Movie(play="video/chapter-1-video/ch1ellenblow2.webm")

image bg ch1ellenplow movie = Movie(play="video/chapter-1-video/ch1ellenplow.webm")
image bg ch1ellenplow2 movie = Movie(play="video/chapter-1-video/ch1ellenplow2.webm")



image ch1ellenpan = Movie(play='video/chapter-1-video/ch1ellenpan.webm', loop=False)
image bg ch1ellenpanmovie movie:
    "ch1ellenpan"
    pause 5
    "ch1ellenpan-end"

label ch1ellen:
    if _in_replay:
        $ setReplay()
    stop music fadeout 2.0

    scene black with fade
    $ renpy.music.set_volume(1, 0, 'music')
    show text "{=trans}DE VUELTA EN EL DEPARTAMENTO{/=trans}" with Dissolve(1)
    play music audio.black fadein 2.0 fadeout 2.0
    $ renpy.pause(2)
    hide text with Dissolve(1)
    show bg ch1ellen1 with dissolve
    e "Finalmente."
    show bg ch1ellen2 with dissolve
    e "Recu??rdame por qu?? no tomamos un taxi."
    p "Estamos bastante cerca, adem??s me gusta pasear."
    show bg ch1ellen3 with dissolve
    e "Y por eso eleg?? el Aftermath."
    p "Pens?? que quer??as que sufriera."
    show bg ch1ellen4 with dissolve
    e "??Yo? Nunca. ??Por qu?? piensas eso?"
    show bg ch1ellen5 with dissolve
    p "Porque s?? lo que quieres."
    e "Muy bien, Fantasma, ??qu?? es lo que quiero?"
    p "Un mont??n de cosas, pero podemos empezar con..."
    show bg ch1ellen6 with hpunch
    p "Esto."
    e "No pierdes ni un puto segundo, [p]."
    show bg ch1ellen7 with dissolve
    p "??Desperdiciar {i}tu{/i} tiempo? {w} Me gusta vivir, gracias."
    show bg ch1ellen8 with dissolve
    e "Y por eso nos llevamos bien."
    show bg ch1ellen9 with dissolve
    e "Ahora, ap??rate. Estos pantalones no se quitar??n solos."
    show bg ch1ellen10 with dissolve
    e "Y estos son mis calzones para las noches de juego. Quer??a estar preparada."
    show bg ch1ellen11 with dissolve
    p "Me alegro de que lo hayas planeado con antelaci??n."
    e "Siempre es una posibilidad que volvamos aqu??."
    show bg ch1ellen12 with dissolve
    e "Ahora vamos a poner un poco de m??sica."
    p "Sam, pon algo apropiadamente sexy."
    s "S?? se??or, tocando el cl??sico de su lista de reproducci??n, {w}\"Tr??o de colegialas depravadas.\""
    p "No es lo que quise decir, Sam."
    show bg ch1ellen13 with dissolve
    e "Sabes qu??, d??jalo. Los tr??os me calientan un mont??n."
    show bg ch1ellen14 with dissolve
    e "Oh, he echado de menos esta verga. ????l tambi??n me extra?????"
    p "Ha pasado una semana."
    show bg ch1ellen15 with dissolve
    e "No arruines el ambiente."
    n "*Los sonidos de la lujuria llenan la habitaci??n desde la holopantalla*"
    p "No hay peligro en eso."
    show bg ch1ellen16 with dissolve
    e "Mmm, no lo hay."
    e "Ahora rel??jate y deja que haga mi magia."
    show bg ch1ellenblow2movie movie with dissolve
    e "*Hace mucho ruido mientras la chupa*"
    p "Ohh, mierda..."
    p "Solo porque me chupes la verga, no significa que acepte el trabajo..."
    show bg ch1ellen18 with dissolve
    e "Me esforzar?? m??s entonces."
    show bg ch1ellen17 with dissolve

    e "Oye, Fantasma, ??qu?? es lo primero?"
    p "Calzones."
    show bg ch1ellen19 with dissolve
    e "Casi lo olvido."
    show bg ch1ellen20 with dissolve
    p "Lev??ntate. Quiero ver ese cuerpo."
    show bg ch1ellenpanmovie movie with dissolve
    e "Nunca te cansas de ver esto, ??verdad?"
    p "No, por supuesto que no."
    p "Ahora ven aqu?? y..."

    $ resetmenu()
    jump ch1ellenmenu1


label ch1ellenmenu1:
    menu:
        "Si??ntate encima m??.":
            jump ch1ellencowgirl
        "Volt??ate":
            jump ch1ellenreverse
        "Ch??pamela":
            jump ch1ellenblow
        "A la cama":
            jump ch1ellenbed

label ch1ellencowgirl:
    p "Ven aqu?? y s??bete. Quiero ver esas tetas en mi cara."
    show bg ch1ellen21 with dissolve
    e "Ser?? mejor que sea la atracci??n principal."
    show bg ch1ellen22 with dissolve
    p "??Ahora qu???"
    show bg ch1ellen23 with dissolve
    e "Los ojos en m??. No en la pantalla."
    p "Bueno, est??s bloqueando la vista."
    e "??Oh, vete a la mierda!"
    p "Solo ponte en mi verga, Ellen."
    show bg ch1ellen24 with dissolve
    e "Mmm, s??..."
    show bg ch1ellenride2 movie with dissolve
    p "Ya est??."
    e "Soy la ??nica aqu??. No hay chicas j??venes y calientes cogiendo detr??s de m??."
    p "Jurar??a que s??."
    show bg ch1ellen25 with dissolve
    p "M??s profundo, Ellen."
    show bg ch1ellen26 with dissolve
    e "Dalo todo, pervertido. {w} Empuja ese pene dentro de m??."
    show bg ch1ellen27 with dissolve
    e "*Se estremece* Ohh, mmm, nalgu??ame el culo."
    show bg ch1ellen28 with dissolve
    e "Mira mis tetas mientras yo..."
    show bg ch1ellen29 with dissolve
    e "????Me corro!!"
    p "Mierda, Ellen. Est??s muy cachonda."
    jump ch1ellenmenu1

label ch1ellenreverse:
    p "Volt??ate mientras ves a esas chicas en la pantalla."
    show bg ch1ellen32 with dissolve
    e "Eres una sucia. Me gusta."
    show bg ch1ellen33 with dissolve
    e "??Vamos, m??telo!"
    p "Lo estoy intentando, pero est??s muy apretada."
    show bg ch1ellen31 with dissolve
    e "S??, [p], llena bien esa vagina."
    show bg ch1ellenride1 movie with dissolve
    p "??Mmm, genial!"
    e "S??, f??llame. F??llame mientras miro a esas putas."
    p "Sigue mene??ndote encima de m??."
    show bg ch1ellen34 with dissolve
    e "??Dame fuerte! ??Mira c??mo van esas dos!"
    show bg ch1ellenride1 movie with dissolve
    p "Consigue un amiga y tal vez puedas intentarlo alg??n d??a."
    e "??No quiero estropearlo!"
    e "??Oh, Dios, estoy cerca, [p]!"
    show bg ch1ellen30 with hpunch
    e "??Oh, carajo!"
    p "Verlas te moja."
    show bg ch1ellen35 with dissolve
    e "Por eso me gusta ver..."
    jump ch1ellenmenu1

label ch1ellenblow:
    p "Rod??ame la poronga con tus labios."
    show bg ch1ellen36 with dissolve
    e "Bien."
    show bg ch1ellen37 with dissolve
    e "S?? que te gustan las chicas de rodillas."
    show bg ch1ellen38 with dissolve
    e "??No es as??? Necesitas sentir que tienes el control. Solo recuerda que puede que yo quiera tomar el control en alg??n momento."
    e "Solo estoy un poco m??s sumisa de lo usual esta noche."
    show bg ch1ellen38 with dissolve
    e "??Tu pene est?? preparado para mi boca?"
    show bg ch1ellen39 with dissolve
    p "Siempre. Ya lo sabes."
    show bg ch1ellen40 with dissolve
    e "Mmm... sabe muy bien."
    show bg ch1ellen41 with dissolve
    p "Pon toda la boca en mi verga."
    show bg ch1ellenblowmovie movie with dissolve
    p "Bien, Ellen."
    e "*Contin??a con movimientos suaves*"
    p "Dios, vas a hacer que me corra."
    show bg ch1ellen42 with dissolve
    p "Espero que est??s listo."
    show bg ch1ellen43 with dissolve
    e "Aseg??rate de que hay m??s despu??s de esto."
    p "Oh, soy bueno para eso."
    e "Bien. Ahora c??rrete para m??."
    show bg ch1ellen44 with quickflash
    p "??Arggh!"
    show bg ch1ellen45 with dissolve
    e "Hijo de puta. L??nzalo en las tetas la pr??xima vez."
    p "T?? estabas apuntando. ??Yo no!"
    p "No te preocupes, todav??a hay m??s de donde vino eso."
    jump ch1ellenmenu1

label ch1ellenbed:
    e "Vamos a la cama."
    show bg ch1ellen46 with dissolve
    e "??Te gusta esta?"
    p "Creo que te gusta m??s que yo."
    show bg ch1ellen47 with dissolve
    e "Puede que tengas raz??n."
    show bg ch1ellen48 with dissolve
    e "Nos vemos en el otro lado, [p]."
    show bg ch1ellen49 with Dissolve(1)
    e "Ven aqu??."
    show bg ch1ellen50 with dissolve
    e "Y c??geme."
    show bg ch1ellen51 with dissolve
    p "Con mucho gusto."
    show bg ch1ellenplow movie with dissolve
    e "??Oh, mierda! S??."
    p "Ohhh. Me est??s cansando."
    e "Y una mierda, t?? sigue."
    show bg ch1ellen54 with dissolve
    e "*Gime extasiada*"
    show bg ch1ellen53 with dissolve
    e "??M??temelo m??s fuerte!"
    show bg ch1ellenplow2 movie with dissolve
    e "??S??!"
    p "??Oh, mierda, s??!"
    show bg ch1ellen52 with hpunch
    e "DIOS, HIJO DE PUTA, ??ME ESTOY CORRIENDO!"
    e "*Jadea*"
    p "Me has hecho polvo, [e]. Ahora es tu turno. ??Arriba!"
    show bg ch1ellen55 with dissolve
    e "Est?? bien, pero solo porque me has dejado loca."
    show bg ch1ellen56 with dissolve
    e "Terminemos con una nota alta."
    show bg ch1ellen57 with dissolve
    e "Te voy a culiar hasta que aceptes este contrato, Fantasma."
    show bg ch1ellen58 with dissolve
    e "Mmm..."
    show bg ch1ellenride3 movie with dissolve
    p "Realmente me quieres en este trabajo, ??no?"
    e "Claro que s??."
    show bg ch1ellenride4 movie with dissolve
    e "??Ahora!{w} ??Toma{w} el puto{w} trabajo!"
    p "??He dicho que lo decidir?? por la ma??ana!"
    e "[p], ??cabr??n! Podr??a detenerme."
    p "??T?? y yo sabemos que amas esto demasiado como para detenerte!"
    e "Sigue so??ando, Fantasma. ??Ahora haz que me corra!"
    show bg ch1ellen59 with dissolve
    e "??DIOS! [p]!"
    p "Ahora acu??state."
    show bg ch1ellen60 with dissolve
    e "En la cara no, por favor."
    show bg ch1ellen61 with dissolve
    p "Esta vez, yo apuntar??."
    show bg ch1ellen62 with dissolve
    p "*Gru??e de placer*"
    show bg ch1ellen64 with dissolve
    e "??Mucho mejor!"
    p "Uf, eso estuvo bien."
    e "Tengo que descansar."
    show bg ch1ellen65 with Dissolve(2)
    $ renpy.end_replay()
    if not persistent.ch1ellen:
        $ renpy.notify(['Escena desbloqueada', 'unlock'])
        $ persistent.ch1ellen = True
    e "No vas a aceptar el trabajo, ??verdad?"
    p "Ellen, no lo s??. Lo har??a... pero algo parece estar mal."
    e "Lo s??...{w} De verdad, trat?? de encontrar algo m??s."
    show bg ch1ellen66 with dissolve
    e "Mira, [p], lo entiendo. Es casi imposible encontrar un contrato que no sea un poco sucio. Y eso no hace m??s que acumular toda la mierda con la que tenemos que lidiar."
    e "A veces desear??a..."
    show bg ch1ellen67
    "Desconocido" "*Se aclara la garganta*"

    e "??Qu?? mierda!"
    $ extraevents.append("ch1ellen")
    jump ch1sonja
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
