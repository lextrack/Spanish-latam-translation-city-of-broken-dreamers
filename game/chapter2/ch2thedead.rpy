
image bg ch2thedead1 = "ch2thedead1"
image bg ch2thedead2 = "ch2thedead2"
image bg ch2thedead3 = "ch2thedead3"
image bg ch2thedead4 = "ch2thedead4"
image bg ch2thedead5 = "ch2thedead5"
image bg ch2thedead6 = "ch2thedead6"
image bg ch2thedead7 = "ch2thedead7"
image bg ch2thedead8 = "ch2thedead8"
image bg ch2thedead9 = "ch2thedead9"
image bg ch2thedead10 = "ch2thedead10"
image bg ch2thedead11 = "ch2thedead11"
image bg ch2thedead12 = "ch2thedead12"
image bg ch2thedead13 = "ch2thedead13"
image bg ch2thedead14 = "ch2thedead14"
image bg ch2thedead15 = "ch2thedead15"
image bg ch2thedead16 = "ch2thedead16"
image bg ch2thedead17 = "ch2thedead17"
image bg ch2thedead18 = "ch2thedead18"
image bg ch2thedead19 = "ch2thedead19"
image bg ch2thedead20 = "ch2thedead20"
image bg ch2thedead21 = "ch2thedead21"
image bg ch2thedead22 = "ch2thedead22"
image bg ch2thedead23 = "ch2thedead23"
image bg ch2thedead24 = "ch2thedead24"
image bg ch2thedead25 = "ch2thedead25"
image bg ch2thedead26 = "ch2thedead26"
image bg ch2thedead27 = "ch2thedead27"

image bg ch2katieafter1 = "ch2katieafter1"
image bg ch2katieafter2 = "ch2katieafter2"
image bg ch2katieafter3 = "ch2katieafter3"
image bg ch2katieafter4 = "ch2katieafter4"


image ch2thedeadmovie = Movie(play='video/chapter-2-video/ch2thedead.webm', loop=False)
image bg ch2thedeadmov movie:
    "ch2thedeadmovie"
    pause 6.0
    "ch2thedeadmovie-end"

label ch2thedead:

    scene black with dissolve
    show bg ch2thedead1 with dissolve
    p "Aquí vamos. Hagamos esto rápido."
    show bg ch2thedead2 with dissolve
    k "Por fin. He estado esperando esto toda la mañana."
    p "Espera, ¿te emociona ver cadáveres? No creo que pueda volver a mirarte de la misma manera, Doc."
    show bg ch2thedead3 with dissolve
    k "Yo también puedo sorprenderte, [p]. Pero no... No estoy emocionada, exactamente."
    p "¿Exactamente qué eres entonces?"
    k "¿Curioso? Ya no tengo muchas oportunidades de hacer trabajos forenses y una autopsia es como resolver un rompecabezas."
    p "Te tomo la palabra."
    show bg ch2thedead4 with dissolve
    play music audio.futurenoir fadein 2.0 fadeout 2.0
    k "¿Dónde está, Sr. Hudson?... Ahí está."
    show bg ch2thedead5 with dissolve
    "Al abrirse la puerta del congelador, el aire frío se siente en toda la habitación."
    p "Trátalo con respeto. Hudson era un idiota, pero seguía su código. Nos cubrimos las espaldas unas cuantas veces."
    k "Bueno. Solo tiene que decirnos qué lo mató."
    k "¿Qué dice, Sr. Hudson? ¿Está dispuesto a hablar?"
    show bg ch2thedead6 with dissolve
    k "Lo siento, hablar con ellos me ayuda. No es demasiado raro, creo."
    p "Lo que sea que te ayude."
    show bg ch2thedead7 with dissolve
    k "Pareces un poco indispuesto. ¿Estás bien?"
    p "¿Por qué no iba a estarlo?"
    k "Estaba hablando con él."
    p "Claro... por supuesto."
    k "Bien, echemos un vistazo a la herida y veamos quien te hizo esto."
    show bg ch2thedead9 with dissolve
    k "*Jadea* Dios mío... [p]."
    p "¿Doctora? ¿Qué sucede?"
    k "Eso no está bien."
    window hide
    show bg ch2thedeadmov movie with dissolve
    $ renpy.pause()
    window show
    p "¡¿Qué?!"
    k "[p], he visto muchas cosas... pero esto no tiene ningún sentido."
    show bg ch2thedead8 with dissolve
    k "Su cráneo está hundido, como si hubiera implosionado."
    show bg ch2thedead11 with dissolve
    p "Espera, ¿qué?"
    $ resetmenu()
    jump ch2thedeadmenu

label ch2thedeadmenu:
    menu:
        "¿Implosiono?" if menu1:
            $ menu1 = False
            p "¿Implosionado? ¿Quieres decir aplastado?"
            show bg ch2thedead8 with dissolve
            k "No, casi. Es como si alguien hubiera hundido su cráneo."
            p "¿Cómo sabes que no fue aplastado simplemente?"
            k "No hay ningún trauma externo, [p]. No tiene sentido."
            jump ch2thedeadmenu
        "¿Qué pudo haberlo causado?" if menu2:
            $ menu2 = False
            p "¿Qué podría causar algo así?"
            k "Estar en el fondo de la Fosa de las Marianas."
            k "Un agujero negro apareció en su cabeza. No sé."
            jump ch2thedeadmenu
        "Solo consigue los datos":
            p "No importa, solo consigue las lecturas que necesitas."
            jump ch2thedeadcont

label ch2thedeadcont:
    show bg ch2thedead12 with dissolve
    k "Está escaneando tan rápido como puede. Pedazo de chatarra."
    p "Me pareció oír algo en el pasillo. Apúrate."
    show bg ch2thedead13 with dissolve
    k "Bien, ¡ya está hecho!"
    k "[p], de una manera u otra te vas a encontrar con el tipo que hizo esto, ¿no?"
    p "Por desgracia."
    show bg ch2thedead10 with hpunch
    n "Se escucha como alguien intenta abrir la puerta"
    show bg ch2thedead14 with dissolve
    k "¡Oh, Dios! Alguien está aquí..."
    p "¡Ya lo sé!"
    show bg ch2thedead15 with dissolve
    p "¡Rápido, hay que esconderse!"
    k "¡Allí!"
    show bg ch2thedead16 with dissolve
    k "¡Tienes que estar bromeando!"
    p "Entra."
    show bg ch2thedead17 with dissolve
    k "¡Ayúdame, [p]!"
    show bg ch2thedead18 with dissolve
    p "Arriba."
    p "¿Estás bien ahí arriba?"
    show bg ch2thedead19 with dissolve
    k "¡Dios! ¡Escóndete, [p]!"
    p "Haz sitio para mí."
    k "¡¿Qué?!"
    scene black
    k "*Susurra* Creo que tu mano está..."
    p "Lo siento... Déjame... *gruñe*"
    show bg ch2thedead22 with Dissolve(2)
    p "¿Mejor?"
    k "Sí, gracias."
    show bg ch2thedead20 with Dissolve(2)
    "Robot policial" "Actividad sospechosa detectada. Protocolo 5-4-2 activo."
    show bg ch2thedead21 with dissolve
    "Robot policial" "Escaneando área."
    show bg ch2thedead23 with dissolve
    k "*Empieza a temblar* ¿[p]?"
    p "Shhh..."
    show bg ch2thedead25 with dissolve
    "Robot policial" "Sujeto 2-4-5-4-3 no almacenado correctamente. Reprimenda emitida al doctor Turner con efecto inmediato."
    show bg ch2thedead26 with dissolve
    n "Con un fuerte chirrido la unidad de refrigeración se cierra"
    "Robot policial" "Habitación despejada, escaneando otras instalaciones."
    show bg ch2thedead22 with dissolve
    p "No es exactamente lo que tenías en mente esta mañana, ¿eh?"
    k "Ni por asomo."
    show bg ch2thedead24 with dissolve
    p "Déjame intentar hacer un poco más de... *gruñe* ...espacio."

    if k_score >= 2:
        show bg ch2thedead27 with dissolve
        p "¿Qué te parece?"
        k "No es el Vic, pero he dormido en lugares peores."
        p "Bueno, ponte cómoda, tenemos que pasar desapercibidos durante unos minutos. Solo hasta que las cosas se calmen."
        k "De acuerdo."
    else:
        show bg ch2thedead23 with dissolve
        p "¿Qué te parece?"
        k "Muy incómodo. ¿Podemos salir ya?"
        p "Todavía no, esperemos a que las cosas se calmen."
        k "Genial..."

    jump ch2afterstation

label ch2afterstation:


    scene black with Dissolve(3)
    play music audio.calm fadein 2.0 fadeout 2.0
    show text "{=trans}UNA HORA MÁS TARDE, VOLVIENDO AL CENTRO{/=trans}" with Dissolve(1)
    $ renpy.pause(2)
    hide text with Dissolve(1)
    show bg ch2katieafter4 with Dissolve(2)
    k "¿Y ahora qué?"
    p "No hay que esconderse más, pero si puedes hacerme llegar tus resultados lo antes posible... sería genial."
    k "Créeme, quiero saber qué pasó tanto como tú."
    show bg ch2katieafter1 with dissolve
    k "Sin embargo, estoy realmente preocupada. Si esto es lo que parece, no he oído nada parecido antes."
    p "Sí..."
    show bg ch2katieafter2 with dissolve
    k "¿Qué crees?"
    p "No sé, es difícil de explicar. No está relacionado, de todos modos."
    k "Cualquier cosa podría ayudar. Nunca se sabe."
    p "Solo confía en mí, Katie. Es que... no puedo."
    p "Ya te he quitado demasiado tiempo. Tengo que ir a ver al padre de la chica... y espero que tenga algo útil."
    k "Bueno, es su padre, debería saber algo."
    p "Esperemos. Llámame cuando tengas los resultados."
    show bg ch2katieafter3 with dissolve
    if k_score >= 2:
        k "Lo haré, y [p], por favor, intenta evitar otra pelea de bandas en el camino."
        p "Lo intentaré, pero ya me conoces..."
        k "Hasta luego, [p]."
    else:
        k "Lo haré. Nos vemos, [p]."

    jump ch2alexis
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
