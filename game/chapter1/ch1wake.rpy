image bg ch1wake1 = "ch1wakeredo1"
image bg ch1wake2 = "ch1wakeredo2"
image bg ch1wake3 = "ch1wakeredo3"
image bg ch1wake4 = "ch1wakeredo4"
image bg ch1wake5 = "ch1wakeredo5"
image bg ch1wake6 = "ch1wakeredo6"
image bg ch1wake7 = "ch1wakeredo7"
image bg ch1wake8 = "ch1wakeredo8"
image bg ch1wake9 = "ch1wakeredo9"
image bg ch1wake10 = "ch1wakeredo10"
image bg ch1wake11 = "ch1wakeredo11"
image bg ch1wake12 = "ch1wakeredo12"
image bg ch1wake13 = "ch1wakeredo13"
image bg ch1wake14 = "ch1wakeredo14"
image bg ch1wake15 = "ch1wakeredo15"
image bg ch1wake16 = "ch1wakeredo16"
image bg ch1wake17 = "ch1wakeredo17"
image bg ch1wake18 = "ch1wakeredo18"
image bg ch1wake19 = "ch1wakeredo19"
image bg ch1wake20 = "ch1wakeredo20"
image bg ch1wake21 = "ch1wakeredo21"
image bg ch1wake22 = "ch1wakeredo22"
image bg ch1wake23 = "ch1wakeredo23"
image bg ch1wake24 = "ch1wakeredo24"
image bg ch1wake25 = "ch1wakeredo25"
image bg ch1wake26 = "ch1wakeredo26"
image bg ch1wake27 = "ch1wakeredo27"
image bg ch1wake28 = "ch1wakeredo28"
image bg ch1wake29 = "ch1wakeredo29"
image bg ch1wake30 = "ch1wakeredo30"
image bg ch1wake31 = "ch1wakeredo31"
image bg ch1wake32 = "ch1wakeredo32"



image bg ch1wake33 = "ch1wake12"
image bg ch1wake34 = "ch1wake24"
image bg ch1wake35 = "ch1wake25"
image bg ch1wake36 = "ch1wake26"
image bg ch1wake37 = "ch1wake27"

image bg ch1ellencall2 = "ch1ellencall2"
image bg ch1ellencall3 = "ch1ellencall3"
image bg ch1ellencall4 = "ch1ellencall4"
image bg ch1ellencall5 = "ch1ellencall5"
image bg ch1ellencall6 = "ch1ellencall6"


image bg ch1intro:
    "ch1intro"
    yalign 0.5
    zoom 0.5
    alpha 1.0
    pause 1.0
    easeout 3.0 zoom 0.6 alpha 0.0


image ch1katiepanmov = Movie(play='video/chapter-1-video/ch1katiepan3.webm', loop=False)
image bg ch1katiepanmovie movie:
    "ch1katiepanmov"
    pause 6.0
    "ch1katiepan2"

image bg chapter1 movie = Movie(play='video/intros/chapter1.webm')


label ch1wake:
    stop music
    show bg chapter1 movie with dissolve
    $ renpy.pause(2.1)
    scene black with Dissolve(3)
    show bg ch1dream1 with Dissolve(3)
    p "??Esto es una mierda!"
    show bg ch1dream2 with dissolve
    "Mujer desconocida" "Nos quedamos sin opciones, [p]."
    p "No podemos hacerlo."
    scene black with Dissolve(3)
    "Voz femenina desconocida" "??Oye! [p], Ya he terminado. Despierta."
    show bg ch1wake1 with Dissolve(3)
    play music audio.calm fadein 2.0
    p "*Gru??e* Entonces, ??cu??l es el pron??stico [k]? ??Vivir???"
    show bg ch1wake2 with dissolve
    $ k_met = True
    k "Es Doctora Hamilton para ti, y s??, estar??s bien. ??Qu?? pas??? No estabas trabajando."
    p "Unos tipos decidieron empezar."
    show bg ch1wake3 with dissolve
    k "D??jame adivinar, ??te has ligado a una de sus esposas?"
    p "Les insulte, seg??n ellos. Solo dije la verdad."
    show bg ch1wake4 with dissolve
    k "Deb?? haberlo imaginado."
    p "??Qu?? significa eso?"
    if not persistent.glos_ghost:
        $ persistent.glos_ghost = True
        $ renpy.notify(['Glosario actualizado', 'glossary'])
    k "Bueno, ustedes los {color=#359eff}Fantasmas{/color} no son conocidos por ser de buen coraz??n."
    menu:
        "Casi siempre es cierto":
            $ k_score += 1
            p "No voy a discutir eso. Ser un fantasma puede cagarte, pero al final del d??a, es solo un trabajo."
            show bg ch1wake3 with dissolve
            k "Lo siento, tienes raz??n. No deber??a juzgar. Adem??s, ciertamente eres m??s f??cil de tratar que la ??ltima chica que tuve que remendar."
        "No es verdad":
            p "Vamos. Es un trabajo, como cualquier otro."
            k "Vaya trabajo. Oigo bastantes fanfarronadas sobre cacer??as exitosas. Un tipo estaba encantado de traer a una chica porque gan?? una apuesta."
            p "*Suspira* S??, algunos somos imb??ciles."
            k "Aun as??, tengo que decir que tratar contigo es mucho m??s f??cil que con la mayor??a."
        "Dale la raz??n":
            $ k_score += 1
            p "Probablemente tengas raz??n. Cazar gente no es un trabajo de ensue??o. Nos arruina, no importa lo que diga la gente."
            p "Aun as??, es lo que se hacer. Y puedo elegir a qui??n persigo. Mis objetivos??? el mundo est?? mejor con ellos fuera de las calles."
            p "Termin?? con la mierda sombr??a."

    show bg ch1wake4 with dissolve
    k "Bueno, d??jame sacar esto..."
    show bg ch1wake5 with dissolve
    p "??Puta madre, doctora!"
    k "Lo siento."
    p "Modales b??sicos, Doc, tienes que aprenderlos."
    show bg ch1wake7 with dissolve
    k "Y t?? tienes que aprender a que no te pateen el culo."
    p "Fueron cinco contra uno y fui el ??nico que sali?? bien."
    show bg ch1wake6 with dissolve
    k "Estoy segura de que todos eran el doble de tu tama??o. La victoria no suele venir con una pu??alada."
    p "Oye, me acaban de apu??alar un poco."
    k "??Un poco...?"
    show bg ch1wake8 with dissolve
    k "??Por qu?? est??s viendo esta mierda?"
    p "??Qu?? mierda?"
    show bg ch1wake33 with dissolve
    p "Oh, eso..."
    if not persistent.glos_gds:
        $ persistent.glos_gds = True
        $ renpy.notify(['Glosario actualizado', 'glossary'])
    "*Personalidad de la TV*" "Con esta nueva propuesta de ley, que apoyo plenamente, podremos por fin controlar la propagaci??n de {color=#359eff}SDG{/color}."
    "*Personalidad de la TV*" "Algunos consideran que limitar la procreaci??n de estas personas es una violaci??n de sus derechos humanos. Pero, ??qui??n sabe qu?? amenaza pueden representar sus hijos?"
    "*Personalidad de la TV*" "Los infectados por SDG pueden seguir solicitando tener hijos. Pero habr?? que vigilar a esta nueva generaci??n. Y gracias a Dios que Industrias Baynard ha intervenido para aportar su experiencia cient??fica."
    "*Personalidad de la TV*" "??Qui??n mejor para proteger y criar a esta nueva generaci??n?"
    show bg ch1wake9 with dissolve
    k "*Gru??e* ??Corta esa mierda!"
    p "??No haces trabajos por encargo para Industrias Baynard?"
    k "Como t??, un trabajo es un trabajo."
    show bg ch1wake11 with dissolve
    "*Personalidad de la TV*" "Esperemos que, con el tiempo, la investigaci??n les ayude a descubrir lo que est?? mal con los Mil...{w} poblaci??n con SDG y hacer de nuestra ciudad un lugar m??s seguro."
    show bg ch1wake10 with dissolve
    k "??Un lugar m??s seguro! ??Qu?? mierda le pasa? ????Un lugar m??s seguro!?"
    show bg ch1wake12 with dissolve
    if not persistent.glos_milcher:
        $ persistent.glos_milcher = True
        $ renpy.notify(['Glosario actualizado', 'glossary'])
    k "??Y por qu?? no lo dice? Casi se le escapa una vez. No es que a nadie le importe que digas {color=#359eff}Milcher{/color} en lugar de SDG."
    p "Maldita sea, suenas como Ellen."
    k "No s?? qui??n es, pero ya me agrada."
    show bg ch1wake14 with dissolve
    k "Quiero decir, escucha a esta perra. Es propaganda. Pura propaganda."
    p "Vaya, creo que nunca te hab??a visto tan irritada."
    show bg ch1katiepanmovie movie with dissolve
    k "*Suspira* Lo siento."
    k "Odio que la gente diga cosas as??."
    show bg ch1wake21 with dissolve
    k "Si ella no tuviera estas, nadie la escuchar??a."
    show bg ch1wake22 with dissolve
    k "??No?"
    p "Perd??n, ??qu??? ??Estabas diciendo algo?"
    show bg ch1wake15 with dissolve
    k "??Oh, venga!"
    p "Solo estaba bromeando, Doc. Fue una pesima broma, lo siento."
    show bg ch1wake19 with dissolve
    k "Lo dejar?? pasar. Solo por esta vez."
    show bg ch1wake18 with dissolve
    k "Pero no es la ??nica. Por la forma en que la gente habla, ??tal vez ella tiene raz??n y yo soy la loca?"
    k "??Qu?? opinas?"
    menu:
        "No creo que est??s loca":
            $ k_score += 1
            p "No est??s loca. Todo el mundo sabe que los medios de comunicaci??n est??n comprados y pagados. Eso no es un secreto."
            p "Aun as??, algunos Mil... {w} SDG han demostrado ser peligrosos."
            p "??Recuerdas el ataque de Santa M??nica?"
            show bg ch1wake24 with dissolve
            k "S??, todo el mundo lo recuerda. Pero, ??cu??ntas veces ha ocurrido eso?"
            p "No lo s??, d??melo t??. Hay gente que muta y algunos se vuelven locos. Nadie sabe por qu??. As?? que, s??, la gente est?? asustada."
            p "Y, si Baynard puede encontrar una cura para ellos, ??eso es algo malo?"
            k "Tal vez no. Aun as??, el modo en que se les trata es simplemente incorrecto."
            p "Estoy de acuerdo..."
        "No importa":

            p "No importa lo que yo piense. Mi opini??n no cambiar?? nada."
            p "La gente se ha decidido. Va a suceder queramos o no."
            show bg ch1wake24 with dissolve
            k "Eso es un poco derrotista de tu parte."
            p "No es derrotismo, es realismo."
            k "La realidad es que son ciudadanos de segunda clase, en el mejor de los casos, y a nadie parece importarle."
            p "??No es verdad?"

    show bg ch1wake23 with dissolve
    k "Me alegro de que estemos de acuerdo en algo."
    show bg ch1wake25 with dissolve
    k "Deber??a volver a casa... has interrumpido mi noche."
    show bg ch1wake28 with dissolve
    k "Y realmente necesitas apagar eso."
    show bg ch1wake27 with dissolve
    k "??rdenes del doctor."
    p "Solo lo ver?? por diversi??n."
    k "Eh, seguro que s??."
    show bg ch1wake26 with dissolve
    k "Buenas noches, [p]."
    p "Buenas noches, doctora."
    show bg ch1wake29 with dissolve
    k "T??matelo con calma durante un par de d??as, ??de acuerdo? Deja que ese brazo se cure."
    show bg ch1wake30 with dissolve
    p "Lo har??."
    show bg ch1wake32 with dissolve
    pt "*Gru??e* (Otro coraz??n sangrante.)"
    show bg ch1wake31 with hpunch
    k "??Eh! Una cosa m??s."
    p "??Qu???"
    k "La pr??xima vez que necesites un parche nocturno fuera del trabajo, ??cobrar?? el doble!"
    p "S??, s??, cobra lo que quieras, no significa que vaya a pagar. ??Ahora vete a casa, Doc!"
    show bg ch1wake32 with dissolve
    p "Ahh, mierda. [s], ??Qu?? hora es?"
    s "*Una suave voz masculina con acento brit??nico emite desde la habitaci??n* Son las 11:23 pm, se??or."
    p "De acuerdo, baja la mesa [s]."
    show bg ch1wake34 with dissolve
    s "Bajando, se??or."
    p "Gracias, [s]."
    show bg ch1wake35 with dissolve
    p "*Se truena el cuello* Ahhh... probablemente deber??a tomarlo con calma."
    show bg ch1wake36 with dissolve
    "*Personalidad de la TV*" "Este es Shanlon Russell despidi??ndose. Que tengan una buena noche, Los ??ngeles."
    p "S??, t?? tambi??n."
    show bg ch1ellencall2 with dissolve
    s "Se??or, tiene una llamada entrante."
    p "??Qui??n es, Sam?"
    s "No est?? en la lista, se??or, no se puede verificar."
    p "Contesta."
    show bg ch1ellencall3 with dissolve
    e "Hola [p], ??qu?? pasa?"
    p "T?? eres la de la llamada nocturna, as?? que d??melo t??, [e]. Si quieres venir, no necesitas una invitaci??n."
    show bg ch1ellencall4 with dissolve
    e "Esta noche no, [p], esto es un negocio, no un placer. No puedo darte detalles aqu?? por razones obvias."
    p "Conozco la rutina."
    show bg ch1ellencall5 with dissolve
    e "As?? que, lleva tu culo a Aftermath y re??nete conmigo en nuestro lugar habitual. Tienes treinta minutos, Fantasma. No vuelvas a llegar tarde."
    show bg ch1ellencall6 with dissolve
    pt "(Bueno, ah?? va esa idea de tom??rselo con calma.)"
    jump ch1aftermath
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
