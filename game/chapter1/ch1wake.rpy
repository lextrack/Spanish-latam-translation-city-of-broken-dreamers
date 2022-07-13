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
    p "¡Esto es una mierda!"
    show bg ch1dream2 with dissolve
    "Mujer desconocida" "Nos quedamos sin opciones, [p]."
    p "No podemos hacerlo."
    scene black with Dissolve(3)
    "Voz femenina desconocida" "¡Oye! [p], Ya he terminado. Despierta."
    show bg ch1wake1 with Dissolve(3)
    play music audio.calm fadein 2.0
    p "*Gruñe* Entonces, ¿cuál es el pronóstico [k]? ¿Viviré?"
    show bg ch1wake2 with dissolve
    $ k_met = True
    k "Es Doctora Hamilton para ti, y sí, estarás bien. ¿Qué pasó? No estabas trabajando."
    p "Unos tipos decidieron empezar."
    show bg ch1wake3 with dissolve
    k "Déjame adivinar, ¿te has ligado a una de sus esposas?"
    p "Les insulte, según ellos. Solo dije la verdad."
    show bg ch1wake4 with dissolve
    k "Debí haberlo imaginado."
    p "¿Qué significa eso?"
    if not persistent.glos_ghost:
        $ persistent.glos_ghost = True
        $ renpy.notify(['Glosario actualizado', 'glossary'])
    k "Bueno, ustedes los {color=#359eff}Fantasmas{/color} no son conocidos por ser de buen corazón."
    menu:
        "Casi siempre es cierto":
            $ k_score += 1
            p "No voy a discutir eso. Ser un fantasma puede cagarte, pero al final del día, es solo un trabajo."
            show bg ch1wake3 with dissolve
            k "Lo siento, tienes razón. No debería juzgar. Además, ciertamente eres más fácil de tratar que la última chica que tuve que remendar."
        "No es verdad":
            p "Vamos. Es un trabajo, como cualquier otro."
            k "Vaya trabajo. Oigo bastantes fanfarronadas sobre cacerías exitosas. Un tipo estaba encantado de traer a una chica porque ganó una apuesta."
            p "*Suspira* Sí, algunos somos imbéciles."
            k "Aun así, tengo que decir que tratar contigo es mucho más fácil que con la mayoría."
        "Dale la razón":
            $ k_score += 1
            p "Probablemente tengas razón. Cazar gente no es un trabajo de ensueño. Nos arruina, no importa lo que diga la gente."
            p "Aun así, es lo que se hacer. Y puedo elegir a quién persigo. Mis objetivos… el mundo está mejor con ellos fuera de las calles."
            p "Terminé con la mierda sombría."

    show bg ch1wake4 with dissolve
    k "Bueno, déjame sacar esto..."
    show bg ch1wake5 with dissolve
    p "¡Puta madre, doctora!"
    k "Lo siento."
    p "Modales básicos, Doc, tienes que aprenderlos."
    show bg ch1wake7 with dissolve
    k "Y tú tienes que aprender a que no te pateen el culo."
    p "Fueron cinco contra uno y fui el único que salió bien."
    show bg ch1wake6 with dissolve
    k "Estoy segura de que todos eran el doble de tu tamaño. La victoria no suele venir con una puñalada."
    p "Oye, me acaban de apuñalar un poco."
    k "¿Un poco...?"
    show bg ch1wake8 with dissolve
    k "¿Por qué estás viendo esta mierda?"
    p "¿Qué mierda?"
    show bg ch1wake33 with dissolve
    p "Oh, eso..."
    if not persistent.glos_gds:
        $ persistent.glos_gds = True
        $ renpy.notify(['Glosario actualizado', 'glossary'])
    "*Personalidad de la TV*" "Con esta nueva propuesta de ley, que apoyo plenamente, podremos por fin controlar la propagación de {color=#359eff}SDG{/color}."
    "*Personalidad de la TV*" "Algunos consideran que limitar la procreación de estas personas es una violación de sus derechos humanos. Pero, ¿quién sabe qué amenaza pueden representar sus hijos?"
    "*Personalidad de la TV*" "Los infectados por SDG pueden seguir solicitando tener hijos. Pero habrá que vigilar a esta nueva generación. Y gracias a Dios que Industrias Baynard ha intervenido para aportar su experiencia científica."
    "*Personalidad de la TV*" "¿Quién mejor para proteger y criar a esta nueva generación?"
    show bg ch1wake9 with dissolve
    k "*Gruñe* ¡Corta esa mierda!"
    p "¿No haces trabajos por encargo para Industrias Baynard?"
    k "Como tú, un trabajo es un trabajo."
    show bg ch1wake11 with dissolve
    "*Personalidad de la TV*" "Esperemos que, con el tiempo, la investigación les ayude a descubrir lo que está mal con los Mil...{w} población con SDG y hacer de nuestra ciudad un lugar más seguro."
    show bg ch1wake10 with dissolve
    k "¡Un lugar más seguro! ¿Qué mierda le pasa? ¿¡Un lugar más seguro!?"
    show bg ch1wake12 with dissolve
    if not persistent.glos_milcher:
        $ persistent.glos_milcher = True
        $ renpy.notify(['Glosario actualizado', 'glossary'])
    k "¿Y por qué no lo dice? Casi se le escapa una vez. No es que a nadie le importe que digas {color=#359eff}Milcher{/color} en lugar de SDG."
    p "Maldita sea, suenas como Ellen."
    k "No sé quién es, pero ya me agrada."
    show bg ch1wake14 with dissolve
    k "Quiero decir, escucha a esta perra. Es propaganda. Pura propaganda."
    p "Vaya, creo que nunca te había visto tan irritada."
    show bg ch1katiepanmovie movie with dissolve
    k "*Suspira* Lo siento."
    k "Odio que la gente diga cosas así."
    show bg ch1wake21 with dissolve
    k "Si ella no tuviera estas, nadie la escucharía."
    show bg ch1wake22 with dissolve
    k "¿No?"
    p "Perdón, ¿qué? ¿Estabas diciendo algo?"
    show bg ch1wake15 with dissolve
    k "¡Oh, venga!"
    p "Solo estaba bromeando, Doc. Fue una pesima broma, lo siento."
    show bg ch1wake19 with dissolve
    k "Lo dejaré pasar. Solo por esta vez."
    show bg ch1wake18 with dissolve
    k "Pero no es la única. Por la forma en que la gente habla, ¿tal vez ella tiene razón y yo soy la loca?"
    k "¿Qué opinas?"
    menu:
        "No creo que estés loca":
            $ k_score += 1
            p "No estás loca. Todo el mundo sabe que los medios de comunicación están comprados y pagados. Eso no es un secreto."
            p "Aun así, algunos Mil... {w} SDG han demostrado ser peligrosos."
            p "¿Recuerdas el ataque de Santa Mónica?"
            show bg ch1wake24 with dissolve
            k "Sí, todo el mundo lo recuerda. Pero, ¿cuántas veces ha ocurrido eso?"
            p "No lo sé, dímelo tú. Hay gente que muta y algunos se vuelven locos. Nadie sabe por qué. Así que, sí, la gente está asustada."
            p "Y, si Baynard puede encontrar una cura para ellos, ¿eso es algo malo?"
            k "Tal vez no. Aun así, el modo en que se les trata es simplemente incorrecto."
            p "Estoy de acuerdo..."
        "No importa":

            p "No importa lo que yo piense. Mi opinión no cambiará nada."
            p "La gente se ha decidido. Va a suceder queramos o no."
            show bg ch1wake24 with dissolve
            k "Eso es un poco derrotista de tu parte."
            p "No es derrotismo, es realismo."
            k "La realidad es que son ciudadanos de segunda clase, en el mejor de los casos, y a nadie parece importarle."
            p "¿No es verdad?"

    show bg ch1wake23 with dissolve
    k "Me alegro de que estemos de acuerdo en algo."
    show bg ch1wake25 with dissolve
    k "Debería volver a casa... has interrumpido mi noche."
    show bg ch1wake28 with dissolve
    k "Y realmente necesitas apagar eso."
    show bg ch1wake27 with dissolve
    k "Órdenes del doctor."
    p "Solo lo veré por diversión."
    k "Eh, seguro que sí."
    show bg ch1wake26 with dissolve
    k "Buenas noches, [p]."
    p "Buenas noches, doctora."
    show bg ch1wake29 with dissolve
    k "Tómatelo con calma durante un par de días, ¿de acuerdo? Deja que ese brazo se cure."
    show bg ch1wake30 with dissolve
    p "Lo haré."
    show bg ch1wake32 with dissolve
    pt "*Gruñe* (Otro corazón sangrante.)"
    show bg ch1wake31 with hpunch
    k "¡Eh! Una cosa más."
    p "¿Qué?"
    k "La próxima vez que necesites un parche nocturno fuera del trabajo, ¡cobraré el doble!"
    p "Sí, sí, cobra lo que quieras, no significa que vaya a pagar. ¡Ahora vete a casa, Doc!"
    show bg ch1wake32 with dissolve
    p "Ahh, mierda. [s], ¿Qué hora es?"
    s "*Una suave voz masculina con acento británico emite desde la habitación* Son las 11:23 pm, señor."
    p "De acuerdo, baja la mesa [s]."
    show bg ch1wake34 with dissolve
    s "Bajando, señor."
    p "Gracias, [s]."
    show bg ch1wake35 with dissolve
    p "*Se truena el cuello* Ahhh... probablemente debería tomarlo con calma."
    show bg ch1wake36 with dissolve
    "*Personalidad de la TV*" "Este es Shanlon Russell despidiéndose. Que tengan una buena noche, Los Ángeles."
    p "Sí, tú también."
    show bg ch1ellencall2 with dissolve
    s "Señor, tiene una llamada entrante."
    p "¿Quién es, Sam?"
    s "No está en la lista, señor, no se puede verificar."
    p "Contesta."
    show bg ch1ellencall3 with dissolve
    e "Hola [p], ¿qué pasa?"
    p "Tú eres la de la llamada nocturna, así que dímelo tú, [e]. Si quieres venir, no necesitas una invitación."
    show bg ch1ellencall4 with dissolve
    e "Esta noche no, [p], esto es un negocio, no un placer. No puedo darte detalles aquí por razones obvias."
    p "Conozco la rutina."
    show bg ch1ellencall5 with dissolve
    e "Así que, lleva tu culo a Aftermath y reúnete conmigo en nuestro lugar habitual. Tienes treinta minutos, Fantasma. No vuelvas a llegar tarde."
    show bg ch1ellencall6 with dissolve
    pt "(Bueno, ahí va esa idea de tomárselo con calma.)"
    jump ch1aftermath
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
