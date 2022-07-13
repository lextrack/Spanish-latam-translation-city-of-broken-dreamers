

image bg ch1corpvisit4 = "ch1corpvisit4"
image bg ch1corpvisit5 = "ch1corpvisit5"
image bg ch1corpvisit6 = "ch1corpvisit6"
image bg ch1corpvisit7 = "ch1corpvisit7"
image bg ch1corpvisit8 = "ch1corpvisit8"
image bg ch1corpvisit9 = "ch1corpvisit9"
image bg ch1corpvisit10 = "ch1corpvisit10"
image bg ch1corpvisit11 = "ch1corpvisit11"
image bg ch1corpvisit12 = "ch1corpvisit12"
image bg ch1corpvisit13 = "ch1corpvisit13"
image bg ch1corpvisit14 = "ch1corpvisit14"
image bg ch1corpvisit15 = "ch1corpvisit15"
image bg ch1corpvisit16 = "ch1corpvisit16"
image bg ch1corpvisit17 = "ch1corpvisit17"
image bg ch1corpvisit18 = "ch1corpvisit18"
image bg ch1corpvisit19 = "ch1corpvisit19"
image bg ch1corpvisit20 = "ch1corpvisit20"
image bg ch1corpvisit21 = "ch1corpvisit21"
image bg ch1corpvisit22 = "ch1corpvisit22"
image bg ch1corpvisit23 = "ch1corpvisit23"
image bg ch1corpvisit24 = "ch1corpvisit24"
image bg ch1corpvisit25 = "ch1corpvisit25"
image bg ch1corpvisit26 = "ch1corpvisit26"
image bg ch1corpvisit27 = "ch1corpvisit27"
image bg ch1corpvisit28 = "ch1corpvisit28"
image bg ch1corpvisit29 = "ch1corpvisit29"
image bg ch1corpvisit30 = "ch1corpvisit30"
image bg ch1corpvisit31 = "ch1corpvisit31"
image bg ch1corpvisit32 = "ch1corpvisit32"
image bg ch1corpvisit33 = "ch1corpvisit33"
image bg ch1corpvisit34 = "ch1corpvisit34"
image bg ch1corpvisit35 = "ch1corpvisit35"
image bg ch1corpvisit36 = "ch1corpvisit36"
image bg ch1corpvisit37 = "ch1corpvisit37"
image bg ch1corpvisit38 = "ch1corpvisit38"
image bg ch1corpvisit39 = "ch1corpvisit39"
image bg ch1corpvisit40 = "ch1corpvisit40"
image bg ch1corpvisit41 = "ch1corpvisit41"
image bg ch1corpvisit42 = "ch1corpvisit42"
image bg ch1corpvisit43 = "ch1corpvisit43"
image bg ch1corpvisit44 = "ch1corpvisit44"
image bg ch1corpvisit45 = "ch1corpvisit45"
image bg ch1corpvisit46 = "ch1corpvisit46"
image bg ch1corpvisit47 = "ch1corpvisit47"
image bg ch1corpvisit48 = "ch1corpvisit48"
image bg ch1corpvisit49 = "ch1corpvisit49"
image bg ch1corpvisit50 = "ch1corpvisit50"
image bg ch1corpvisit51 = "ch1corpvisit51"
image bg ch1corpvisit52 = "ch1corpvisit52"
image bg ch1corpvisit53 = "ch1corpvisit53"
image bg ch1corpvisit54 = "ch1corpvisit54"
image bg ch1corpvisit55 = "ch1corpvisit55"

image bg ch1rec1 = "ch1rec1"
image bg ch1rec2 = "ch1rec2"
image bg ch1rec3 = "ch1rec3"
image bg ch1rec4 = "ch1rec4"
image bg ch1rec5 = "ch1rec5"
image bg ch1rec6 = "ch1rec6"
image bg ch1rec7 = "ch1rec7"
image bg ch1rec8 = "ch1rec8"
image bg ch1rec9 = "ch1rec9"

image ch1viclookmov = Movie(play='video/chapter-1-video/ch1viclook.webm', loop=False)
image bg ch1viclookmovie movie:
    "ch1viclookmov"
    pause 3.6
    "ch1viclook"

image ch1officepanmov = Movie(play='video/chapter-1-video/ch1officepan.webm', loop=False)
image bg ch1officepanmovie movie:
    "ch1officepanmov"
    pause 6
    "ch1officepan"

label ch1meredith:
    scene black with dissolve
    play music audio.futurenoir fadein 2.0 fadeout 2.0
    show bg ch1corpvisit4 with dissolve
    m "Bienvenido, [p], me alegro de que te hayas pasado por aquí."
    p "No actúes como si tuviera elección, Meredith."
    show bg ch1corpvisit5 with dissolve
    m "Deja de refunfuñar y toma asiento."
    p "No me das órdenes, ya no."
    show bg ch1corpvisit6 with dissolve
    m "¿Quieres hacer esto rápido o no? Sé que preferirías estar en cualquier otro sitio ahora mismo, así que {i}siéntate.{/i}"
    menu:
        "Confróntala":

            p "¿Qué estás tramando? ¿Te has quedado sin agentes prescindibles en tu nómina otra vez?"
            show bg ch1corpvisit7 with dissolve
            m "Tranquilo, [p]. Sé que no siempre coincidimos, pero ambos somos profesionales."
            menu:
                "Enójate":
                    $ dep += 1
                    p "¿Profesional? Me pregunto si sería profesional si te partiera la cabeza con esta mesa de cristal."
                    show bg ch1corpvisit8 with dissolve
                    m "No me gustan las amenazas, agente."
                    p "A mí no me gusta que intentes molestarme."
                    show bg ch1corpvisit9 with dissolve
                    m "Última oportunidad, [pl]. Siéntate y compórtate o llamo a seguridad."
                    $ extraevents.append("ch1threat")
                    p "Bien. Escupe lo que tienes que decir."
                    jump ch1meredith2
                "Alivia la situación":
                    p "Bien. Escupe lo que tienes que decir."
                    show bg ch1corpvisit8 with dissolve
                    m "Ahora, siéntate."
                    jump ch1meredith2
        "Siéntate":
            jump ch1meredith2

label ch1meredith2:
    show bg ch1corpvisit10 with dissolve
    m "Ya está, ahora podemos hablar como adultos."
    p "Muy bien, hazlo rápido. Cuanto antes lo digas, antes podré decir que no."
    show bg ch1corpvisit11 with dissolve
    m "Ya está."
    m "No me digas que hemos terminado antes de escucharme."
    p "Escúpelo"
    show bg ch1corpvisit12 with dissolve
    m "Esta chica... podemos tener una cura para ella. Desarrollamos la cura después de que viniera el año pasado a hacerse pruebas."
    p "Qué suerte tiene."
    m "Necesitamos que la traigas por su propio bien."
    p "Deja de actuar como una santurrona. ¿Desde cuándo te importa proteger a una chica cualquiera?"
    m "No es una cualquiera. Si esto funciona para ella, podría funcionar en otros."
    p "Ah, y llenarte los bolsillos también. Si curas a la hija de Alexis Conner... eso sería bastante bueno para la prensa."
    show bg ch1corpvisit13 with dissolve
    m "Un beneficio añadido. Por supuesto que buscamos el beneficio, pero, ¡piensa en ello! ¿Una cura para el SDG? ¡Por fin!"
    p "¿Y por qué esta chica es tan especial? Con solo llamar la atención en Mil-Town y todos estarán en fila a la espera de recibir la cura."
    m "Se ofreció como voluntaria para el mapeo genético el año pasado. La bioingeniería ha estado trabajando en su secuencia genética... es prometedor, pero actualmente, solo se puede trabajar en ella."
    p "Tu aliento huele a mierda, Meredith. ¿Cuál es tu verdadera intención? ¿Otro Caracas?"
    show bg ch1corpvisit14 with dissolve
    m "Pedí un traslado después de ese incidente. Ahora estoy en la división médica."
    show bg ch1corpvisit17 with dissolve
    p "Estoy seguro de que el técnico de armas te echa mucho de menos. Por cierto, ya lo he visto eso."
    m "Quiero asegurarme de que recuerdes su rostro, porque esa chica podría ser la diferencia entre el sufrimiento o una vida normal."
    show bg ch1corpvisit15 with dissolve
    m "Podemos ayudarla. Podemos protegerla."
    p "¿Protegerla de quién?"
    if not persistent.glos_vostok:
        $ persistent.glos_vostok = True
        $ renpy.notify(['Glosario actualizado', 'glossary'])
    m "{color=#359eff}Vostok{/color} Biotehnologija."
    p "¿Se están desviando de la robótica? ¿Por qué carajo querrían rastrearla?"
    m "No lo sabemos con seguridad. Vostok ha estado moviéndose en la biotecnología desde hace unos años, bajo el radar, por supuesto."
    p "¿Alguien les vendió tu investigación?"
    m "Es posible. Pero la quieren, mucho. Y, para que no lo olvides, no son tan amables con sus sujetos de prueba como nosotros."
    p "¿Qué más sabes?"
    m "*Suspira* Tal vez mi asistente podría ser más útil. Ella ha estado siguiendo esto muy de cerca."
    show bg ch1corpvisit16 with dissolve
    m "Victoria, puedes entrar y tomar asiento, por favor."
    show bg ch1officepanmovie movie with dissolve
    pt "(Maldita sea... No me extraña que quisiera que entrara.)"
    v "¿Sí, Sra. White?"
    m "Ven a sentarte, Victoria."
    show bg ch1corpvisit19 with dissolve
    v "Hola."
    show bg ch1corpvisit20 with dissolve
    v "¿Me necesitaba, señora?"
    show bg ch1corpvisit21 with dissolve
    m "Sí Victoria, este es el agente [p] [pl]."
    m "Necesito que respondas a cualquier pregunta que tenga sobre la situación de \"Conner.\""
    show bg ch1corpvisit22 with dissolve
    v "Por supuesto."
    m "Bien."
    show bg ch1corpvisit23 with dissolve
    m "Asegúrate de que lo entiende todo. Responde a todas sus preguntas. Dile lo que sabemos."
    v "Sí, señora."
    show bg ch1corpvisit24 with dissolve
    m "*Le algo susurra al oído*"
    v "Entiendo..."
    show bg ch1corpvisit25 with dissolve
    m "Bien. Tengo la sensación de que será más receptivo contigo."
    show bg ch1corpvisit26 with dissolve
    m "Los dejaré para que discutan estos asuntos. Si me disculpas, agente [pl]."
    show bg ch1corpvisit27 with dissolve
    v "..."
    p "¿Estás bien?"
    show bg ch1viclookmovie movie with dissolve
    v "..."
    v "Sí, agente, estoy bien. ¿Empezamos?"
    $ v_met = True
    show bg ch1corpvisit28 with dissolve
    v "Seguro que tiene muchas preguntas. Estaré encantada de responderlas."
    p "Desde luego."
    show bg ch1corpvisit18 with dissolve
    v "Pregunte."
    $ resetmenu()
    jump ch1corpquestions

label ch1corpquestions:
    show bg ch1corpvisit18 with dissolve
    menu:
        "¿Quién eres?" if menu1 == True:
            $ menu1 = False
            p "¿Y tú eres?"
            v "Me llamo Victoria Shields. Soy la asistente de la Sra. White."
            p "Pareces ser más que eso."
            show bg ch1corpvisit30 with dissolve
            v "En cierto modo lo soy. Me aseguro de que su día transcurra sin problemas."
            menu:
                "Interrógala":
                    $ v_score += 1
                    p "Eh, sí. Déjate de tonterías. Eres mucho más."
                    v "No sé a qué se refiere, agente."
                    p "Creo que sí. Te vi en Aftermath. No pensaste que una pequeña capucha se me escaparía, ¿verdad?"
                    show bg ch1corpvisit32 with dissolve
                    v "Empiezo a entender por qué Meredith le buscó."
                    v "Sí, estuve allí. Queríamos ver si era necesario traerle o no."
                    v "Su reputación de terquedad no es, al parecer, injustificada. Una vez que eso quedó claro, nos movimos para que se reuniera con nosotros aquí, directamente."
                    p "Correcto. Muy bien, más preguntas."
                "Déjala":
                    p "Muy bien, otra pregunta."
            jump ch1corpquestions
        "¿Qué le pasa?" if menu2 == True:
            $ menu2 = False
            p "¿Qué te pasa?"
            v "Es una pregunta extraña."
            p "Lo digo en serio... no eres una simple asistente. De hecho, ¿qué eres?"
            v "¿Qué crees que soy?"
            p "No estoy seguro; podrías ser una robot."
            v "¿Por qué crees que no soy humana? Te aseguro que no soy uno de los juguetes de Vostok."
            p "Sospecho de cualquiera que esté cerca de Meredith."
            v "Bueno, agente. Soy muy real, solo mira."
            show bg ch1corpvisit29 with dissolve
            v "No te quedes mirando demasiado tiempo. Podría tener una impresión equivocada."
            p "Lo siento... No puedo evitarlo."
            menu:
                "Oblígate a mirar":
                    $ v_score += 1
                "Baja la vista":
                    show bg ch1corpvisit33 with dissolve
                    v "¿Te gusto?"
                    menu:
                        "Sí...":
                            p "Sí..."
                            $ extraevents.append("ch1spellbound")
                            $ v_lust += 1
                            show bg ch1corpvisit34 with dissolve
                            v "Bien. Esperaba que así fuera."
                            p "..."
                            v "Ahora, mírame a los ojos."
                            show bg ch1corpvisit18 with dissolve
                            v "Estoy segura de que hay otras cosas que deberíamos discutir. Eso... se puede dejar para más adelante."
                        "Evádela":
                            p "¿Qué?"
                            v "Nada, agente."

            show bg ch1corpvisit18 with dissolve
            p "Espera... Por supuesto... Debería haberme dado cuenta. Sé lo que eres."
            v "Ilumíname."
            if not persistent.glos_augment:
                $ persistent.glos_augment = True
                $ renpy.notify(['Glosario actualizado', 'glossary'])
            p "Eres una {color=#359eff}augment{/color}. Meredith debe tener mucha influencia ahora mismo si eres su mano derecha."
            v "Su reputación le hace justicia de nuevo, agente [pl]. No muchos saben que existimos. Eres muy perspicaz."
            p "¿Eso significa que has estado con Baynard desde que eras una niña?"
            v "Entré en el programa durante la adolescencia en realidad."

            menu:
                "Pide más detalles":
                    $ extraevents.append("ch1vicparents")
                    p "¿Tus padres te dejaron ser un conejillo de indias para una corporación?"
                    show bg ch1corpvisit31 with dissolve
                    v "Me doy cuenta de que esto debe ser fascinante para usted, pero prefiero no discutirlo. ¿Podemos, por favor, hablar de la tarea que tenemos entre manos?"
                    pt "(Bueno, eso ha dado en el clavo. Supongo que al menos no es un robot.)"
                    p "Sí, hagámoslo."
                "Déjala":
                    p "Muy bien, tengo más preguntas."

            jump ch1corpquestions
        "¿Es verdad lo de la cura?" if menu3 == True:
            $ menu3 = False
            p "Esta cura. Suena a algo muy descabellado. ¿Qué sabes al respecto?"
            show bg ch1corpvisit28 with dissolve
            v "Mis conocimientos en ese ámbito son limitados, pero sé que lleva más de una década en desarrollo. Este es el primer gran avance en mucho tiempo."
            v "Por lo tanto, es importante que la traigamos antes de que otros se hagan con ella."
            v "Si la cura funciona, ayudará a muchos."
            p "Mmm... Muy bien, más preguntas."
            jump ch1corpquestions

        "Háblame de la chica" if menu4 == True:
            p "Quiero saber sobre esta chica. Que pasa con la gente que la persigue y lo más importante, ¿por qué?"

            if menu1 == True or menu2 == True or menu3 == True:
                v "Eso llevará tiempo. ¿Ha terminado con sus otras preguntas?"
                menu:
                    "No, tengo más preguntas":
                        p "No, tengo más preguntas para ti."
                        jump ch1corpquestions
                    "Sí, cuéntame sobre la chica":
                        p "Está bien, háblame de ella."
                        jump ch1corp2
            jump ch1corp2

label ch1corp2:
    v "Muy bien."
    show bg ch1corpvisit35 with dissolve
    v "Déjeme mostrarle."
    show bg ch1corpvisit36 with dissolve
    v "Nos las arreglamos para conseguir algo de información de nuestros... \"competidores.\""
    p "Te refieres a Vostok."
    v "Entre otros."
    show bg ch1corpvisit37 with dissolve
    p "¿Son los que contrataron a Hudson y su equipo?"
    v "Es muy probable que así sea."
    show bg ch1corpvisit38 with dissolve
    p "¿Qué hay de Jhong Sun? Es el contratista de Hudson. Él podría saber algo."
    show bg ch1corpvisit39 with dissolve
    v "Sí, en cuanto a eso, lo localizamos esta mañana."
    show bg ch1corpvisit40 with dissolve
    v "Sin embargo, esa línea de interrogación está muerta."
    p "*suspira* Mierda. ¿Qué hay del otro grupo, de hace un par de noches? Aparentemente también se deshicieron de ellos."
    show bg ch1corpvisit41 with dissolve
    v "Sí, por eso creemos que hay al menos otra parte involucrada."
    show bg ch1corpvisit42 with dissolve
    v "El suceso ocurrió en Lakewood."
    if not persistent.glos_miltown:
        $ persistent.glos_miltown = True
        $ renpy.notify(['Glosario actualizado', 'glossary'])
    p "{color=#359eff}Mil-town{/color}..."
    show bg ch1corpvisit43 with dissolve
    v "Creemos que había estado viviendo allí durante algún tiempo."
    p "¿Cómo le perdiste la pista?"
    show bg ch1corpvisit44 with dissolve
    v "Hace unos meses desapareció tras mudarse de su anterior residencia. Desde entonces no hemos podido localizarla."
    p "Chica lista."
    v "Sí, pero para mal."
    v "¿Quiere ver una grabación que adquirimos del incidente de Lakewood?"
    p "Sí."
    v "Como desees."
    call ch1botchjob from _call_ch1botchjob
    p "¿Qué es eso?"
    p "Me dijeron que estaban incapacitados. Eso se veía mucho peor."
    show bg ch1corpvisit46 with dissolve
    v "El informe lo minimizó. Un agente muerto. El otro está en coma."
    p "¿Esa cosa, ese es el tercero al que te refieres?"
    show bg ch1corpvisit47 with dissolve
    v "Sí, no sabemos quién o qué es. Nos ha eludido en todo momento. Vostok también."
    p "No muchas corporaciones que puedan reunir a alguien tan bueno, alguien tan bueno de quien nunca había oído hablar."
    v "Su astucia está a la altura de su fuerza. No lo subestimes."
    p "¿Después de ver eso? Es poco probable."
    v "Tienes que encontrarla antes que él. El reloj está corriendo para la señorita Conner."
    p "Hablando de ella, la tienes marcada como peligrosa. ¿Por qué?"
    v "Creemos que sus síntomas pueden perjudicar a la población en general de alguna manera. Su incidente involucró la muerte de un adolescente."
    p "¿Super fuerte?"
    v "No estoy autorizada para decir eso."
    p "Yo... seguro..."
    p "*sacude la cabeza* Así que tenemos múltiples partes, con el apoyo de la corporación, todos siguiendo el mismo objetivo. Un objetivo que tú y las autoridades marcan como extremadamente peligroso."
    p "Y quieres que vaya en medio de ese espectáculo de mierda y te la traiga."
    v "Básicamente, sí."
    p "Lo admito. Estoy intrigado. Aunque, si quieres que me ocupe de {i}eso{/i}. Necesitas pagarme mucho más que mi tarifa estándar."
    show bg ch1corpvisit48 with dissolve
    v "Eso se puede discutir más adelante."
    if "ch1spellbound" in extraevents:
        show bg ch1corpvisit52 with dissolve
        v "Estoy seguro de que te gustaría."
        p "..."
        show bg ch1corpvisit54 with dissolve
        v "Tal unos tragos. ¿Le viene bien a las 20:00?"
        p "Sí..."
        show bg ch1corpvisit53 with dissolve
        v "Bien, podemos encontrarnos en el Sky Lounge."
    else:
        v "Haga lo que tenga que hacer para prepararse, agente."
        v "Podemos discutir su pago esta noche mientras tomamos una copa. ¿Te sirve el Sky Lounge?"
        p "Es un poco caro."
        v "Yo me encargaré de eso. Solo tiene que presentarse."
    show bg ch1corpvisit55 with dissolve
    v "Ahora, haga lo que quiera. Le veré esta noche."
    v "Adiós, agente."

    pt "(Una maldita Augment. No me extraña que Meredith quisiera que participara. Tengo que tener cuidado.)"

    jump ch1hosp






define gh1 = Character('Fantasma 1', color="#bb0000")
define gh2 = Character('Fantasma 2', color="#bb0000")
define ove = Character('Overwatch', color="#bbbb00")

label ch1botchjob:

    show bg ch1rec1 with dissolve
    ove "¿Me lo repites?"
    gh1 "He dicho... Que he perdido de vista el objetivo."
    show bg ch1rec2 with dissolve
    ove "Las cámaras de tráfico no captan nada. Espera... aguanta. ¡Allá más abajo en el callejón!"
    show bg ch1corpvisit45 with dissolve
    "*Estática*"
    v "Perdimos la transmisión por un momento... pero la recuperé unos minutos después."
    show bg ch1rec3 with dissolve
    ove "Michelle, ¿qué mierda le ha pasado a Tommy?"
    gh2 "No tengo ni puta idea... ¿salió de la nada?"
    ove "¿Un Milcher?"
    show bg ch1rec4 with dissolve
    gh2 "*Le tiembla la voz* ¿Cómo mierda voy a saberlo? ¡Era más bien un maldito tanque!"
    gh2 "¿Ves a Tommy en algún lugar?"
    ove "Estás en un punto ciego. No puedo ver una mierda con este dron."
    show bg ch1rec5 with dissolve
    gh2 "¡Me voy a la mierda de aquí!"
    ove "No podemos dejar atrás a Tommy."
    gh2 "Claro que sí."
    ove "Tenemos que encontrar a la chica, ¡estás cerca!"
    gh2 "¡Me importa una mierda! No vale la pena morir por esto."
    gh2 "¡MIERDA! Por esto odio Mil-town."
    ove "Espera... Movimiento al sur."
    gh2 "¿Es Tommy?"
    ove "Mmm... mierda no... es mucho más grande."
    show bg ch1rec6 with dissolve
    ove "¡Michelle! ¡CORRE!"
    gh2 "¿Qué carajo? ¿Qué demonios eres tú?"
    show bg ch1rec7 with dissolve
    gh2 "¡¡AAAAH!!"
    show bg ch1rec8 with dissolve
    ove "¡Michelle! ¡Michelle!"
    show bg ch1rec9 with dissolve
    ove "¡Vamos! ¡Responde!"
    ove "Joder... mierda... mierda..."
    show bg ch1corpvisit45 with dissolve
    "Estática"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
