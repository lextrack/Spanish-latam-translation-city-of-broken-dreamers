



define pf = False

define p = Character("[pf]", who_color="#0072ff")
define pt = Character("[pf]", who_color="#0072ff")
define n = Character("", who_color="#ffffff")

define e = Character("Ellen", who_color="#00a06a")
define g = Character("Gloria", who_color="#fff993")
define v = Character("Victoria", who_color="#ff008a")
define k = Character("Katie", who_color="#74b2ff")
define m = Character("Meredith", who_color="#f3a600")
define c = Character("Chandra", who_color="c0ff00")
define s = Character("Sam", who_color="#baf4ff")
define j = Character("Sonja", who_color="#ff7026")
define klx = Character("Kleo Love Xavier", who_color="#ff00fc")
define sh = Character("Shanlon", who_color="#ff45b7")
define ve = Character("Venus", who_color="#fcd3ff")
define b = Character("Betty", who_color="#ffeaa5")
define ab = Character("Abby", who_color="#ff00c0")
define t = Character("Tex", who_color="#cdc8a8")
define gl = Character("Glenn", who_color="#eedba2")
define sa = Character("[sa_name]", who_color="#cd00d4")
define ca = Character("Carli", who_color="#f147d0")



define a = Character("Alexis", who_color="#3366aa")
define h = Character("Henry", who_color="#44bb33")

define dr = Character("Dr. Lavalle", who_color="#ffd52f")

define dev = Character("PhillyGames", who_color="#ff00b7")


define pl = False
default dep = False


default e_met = False
default e_score = 0
default e_lust = 0

default g_met = False
default g_score = 0
default g_lust = 0

default v_met = False
default v_score = 0
default v_lust = 0

default k_met = False
default k_score = 0
default k_lust = 0
default k_dirty = 0

default s_met = False
default s_score = 0
default s_lust = 0
default s_break = 0

default j_score = 0


default sa_name = "Bolter"
default sa_met = False
default sa_score = 0
default sa_lust = 0
default sa_int = 0

default c_met = False
default c_score = 0
default c_lust = 0

default h_score = 0

default ab_score = 0
default ab_lust = 0

default k_bio = "Tras obtener rápidamente su doctorado en medicina, Katie ha estado haciendo trabajos por encargo con Industrias Baynard. Durante el día, dirige un centro médico sin ánimo de lucro cerca de Mil-town."
default e_bio = "Una antigua estrella del rock que tenía un contrato con Alexis Conner. Tras la ruptura, debe el pago de los atrasos al magnate de los medios de comunicación. Para llegar a fin de mes, utilizó su conocimiento adquirido en las calles para convertirse en una contratista de Fantasmas."
default v_bio = "Una misteriosa mujer que trabaja junto a Meredith White. Sus verdaderas intenciones son desconocidas."
default g_bio = "Una mujer joven, abandonada y dejada atrás. Con su protector, Henry Gibson, huye para salvar su vida. La persiguen por el raro don que posee."
default c_bio = "Hija de Meredith White. Una vez formó parte de tu equipo de seguridad hace unos años. Siempre ha tenido una actitud rebelde a causa de las discusiones con su madre."



define flash = Fade(0.25, 0.5, 0.75, color="#fff")
define quickflash = Fade(.1, 0.1, 0.25, color="#fff")
define lightning = Fade(0.1,0.1,0.5, color="#fff")




default vicsexname = False
default ellensexname = False
default katiesexname = False
default gloriasexname = False
default chandrasexname = False
default menu1 = True
default menu2 = True
default menu3 = True
default menu4 = True
default menu5 = True
default menu6 = True
default menu7 = True

default sexmenu1 = True
default sexmenu2 = True
default sexmenu3 = True
default sexmenu4 = True
default sexmenu5 = True
default sexmenu6 = True
default sexmenu7 = True

default pcap = False
default pdastart = False

default extraevents = []
default ch4battleevents = []
default ch4battlescore = False
default vicsexcount = 0


default ch5dream = 0

define cards = []
default insult = ""
default insults = ["estúpido","cabrón","comepollas","retrasado","imbécil","maricón","puto"]





label after_load:

    if not hasattr(renpy.store,"s_score"):
        $ s_score = 0
    if not hasattr(renpy.store,"s_lust"):
        $ s_lust = 0
    if not hasattr(renpy.store,"s_met"):
        $ s_met = False
    if not hasattr(renpy.store,"shanlonsexname"):
        $ shanlonsexname = False
    if not hasattr(renpy.store,"s_break"):
        $ s_break = 0

    if not hasattr(renpy.store,"c_score"):
        $ c_score = 0
    if not hasattr(renpy.store,"c_lust"):
        $ c_lust = 0
    if not hasattr(renpy.store,"c_met"):
        $ c_met = False
    if not hasattr(renpy.store, "chandrasexname"):
        $ chandrasexname = False
    if not hasattr(renpy.store, "ch4battlescore"):
        $ ch4battlescore = 0
    if not hasattr(renpy.store, "ch4battleevents"):
        $ ch4battleevents = []

    if not hasattr(renpy.store, "h_score"):
        $ h_score = 0

    if not hasattr(renpy.store, "ab_score"):
        $ h_score = 0
    if not hasattr(renpy.store, "ab_lust"):
        $ h_score = 0
    if not hasattr(renpy.store, "ch5dream"):
        $ ch5dream = 0
    if not hasattr(renpy.store, "sa_int"):
        $ sa_int = 0
    if not hasattr(renpy.store, "k_dirty"):
        $ ch5dream = 0
    return



init python:
    cobd = MultiPersistent("phillygames.cobd.org")




if renpy.variant("pc"):
    define config.hw_video = True
else:
    define config.hw_video = False
init:
    python:
        class MovieLooped(renpy.display.video.Movie):
            """Play Movie Sprites without loops. Until Ren'Py permits that by default, this can be used.
            """
            def __init__(self, *args, **kwargs):
                super(MovieLooped, self).__init__(*args, **kwargs)
                self.loops = kwargs.get("loops", 1)
            
            def play(self, old):
                if old is None:
                    old_play = None
                else:
                    old_play = old._play
                
                if self._play != old_play:
                    if self._play:
                        renpy.audio.music.play([self._play]*self.loops, channel=self.channel, loop=False, synchro_start=True)
                        
                        if self.mask:
                            renpy.audio.music.play([self.mask]*self.loops, channel=self.mask_channel, loop=False, synchro_start=True)
                    
                    else:
                        renpy.audio.music.stop(channel=self.channel)
                        
                        if self.mask:
                            renpy.audio.music.stop(channel=self.mask_channel)


        def resetmenu():
            global menu1
            global menu2
            global menu3
            global menu4
            global menu5
            global menu6
            global menu7
            menu1, menu2, menu3, menu4, menu5, menu6, menu7 = True, True, True, True, True, True, True

        def resetsexmenu():
            global sexmenu1
            global sexmenu2
            global sexmenu3
            global sexmenu4
            global sexmenu5
            global sexmenu6
            global sexmenu7
            sexmenu1, sexmenu2, sexmenu3, sexmenu4, sexmenu5, sexmenu6, sexmenu7 = True, True, True, True, True, True, True


        def setReplay():
            global p
            global pl
            global pt
            global vicsexname
            global shanlonsexname
            global ellensexname
            global katiesexname
            global chandrasexname
            global e_score
            global k_lust
            pt = ""
            if persistent.p:
                p = persistent.p
            else:
                p = "Jack"
            
            if persistent.pl:
                pl = persistent.pl
            else:
                pl = "Murphey"
            
            if persistent.ch5ellenkiss:
                e_score = 5
            
            if persistent.k6_lust:
                k_lust = persistent.k6_lust
            
            
            if persistent.vicsexname:
                vicsexname = persistent.vicsexname
            else:
                vicsexname = p
            
            if persistent.katiesexname:
                katiesexname = persistent.katiesexname
            else:
                katiesexname = p
            
            if persistent.shanlonsexname:
                shanlonsexname = persistent.shanlonsexname
            else:
                shanlonsexname = p
            
            if persistent.chandrasexname:
                chandrasexname = persistent.chandrasexname
            else:
                chandrasexname = p
            
            if persistent.ellensexname:
                ellensexname = persistent.ellensexname
            else:
                ellensexname = p

        def play_movie_only_once_callback(old,new):
            renpy.music.play(new._play, channel=new.channel, loop=False, synchro_start=True)
            if new.mask:
                renpy.music.play(new.mask, channel=new.mask_channel, loop=False, synchro_start=True)






image bg warning = "warning"


label splashscreen:
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            _preferences.volumes['music'] *= .80


    scene black
    show bg warning with dissolve
    with Pause(5)

    scene black with dissolve
    with Pause(1)

    show text "{=trans}PHILLY GAMES PRESENTA...{/=trans}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "{=trans}THE CITY OF BROKEN DREAMERS{/=trans}" with dissolve
    with Pause(4)

    hide text with dissolve
    with Pause(1)

    $ renpy.transition(dissolve)
    return






image tuteyes = Movie(play='video/chapter-1-video/eyes.webm', loop=False)




image bg tut1 = "tut1"
image bg tut2 = "tut2"
image bg tut3 = "tut3"
image bg tut4 = "tut4"
image bg tut5 = "tut5"
image bg tut6 = "tut6"


image tuteyes = Movie(play='video/chapter-1-video/eyes.webm', loop=False)
image bg tuteyesmovie movie:
    "tuteyes"
    pause 2.56
    "eyes_1"


label start:

    $ renpy.clear_game_runtime()
    stop music fadeout 5.0
    scene black with dissolve
    show bg tuteyesmovie movie
    "Mujer desconocida" "Me dijeron que alguien se presentaría."
    "Mujer desconocida" "Ahora, no tengo mucho tiempo. El trabajo me llama como puedes ver. ¿Qué tal si hacemos esto rápido?"
    "Mujer desconocida" "Primero, necesito tu nombre."


    python:
        pf = renpy.input("¿Cuál es tu nombre?")
        pf = pf.strip()

        if not pf:
            pf = "Jake"

        persistent.p = pf
    "¿Y el apellido?"

    python:
        pl = renpy.input("¿Cuál es tu apellido?")
        pl = pl.strip()

        if not pl:
            pl = "Murphey"
        persistent.pl = pl

    show bg tut1 with dissolve
    "Mujer desconocida" "Encantada de conocerte agente, [pf] [pl]."
    show bg tut2 with dissolve
    "Mujer desconocida" "¿Quién soy yo?{w} Nos conoceremos pronto. {w}Por ahora, déjame enseñarte cómo se hacen las cosas por aquí."
    show bg tut3 with dissolve
    $ pdastart = True
    show screen control
    "Mujer desconocida" "Primero lo primero. Aquí están tus estadísticas y tu diario. Te permitirá ver tus estadísticas actuales."
    "Mujer desconocida" "Así como un glosario y una recapitulación de los eventos actuales."
    "Mujer desconocida" "¿Lo entiendes? Perfecto."
    show bg tut6 with dissolve
    $ renpy.notify(['Posible pista', 'alert'])

    $ renpy.notify(['Posible pista', 'alert'])
    show screen hidden_item("ch1tut", "ch1tut", 1422, 425, 266, 158)
    "Mujer desconocida" "Segundo. De vez en cuando, verás esta alerta en tu pantalla. Cuando suceda, significa que hay un \"secreto\" cerca."
    "Mujer desconocida" "Mira a tu alrededor, es decir, pasa el cursor por encima de algún punto exacto de la pantalla. Cuando se destaque un objeto, haz clic en él. Después de hacerlo, puedes comprobar la pestaña \"Información\" para verlo en tu galería."

    "Mujer desconocida" "Mira mi ojo izquierdo para entender lo que quiero decir. (Pasa el cursor por encima y luego haz clic en su ojo izquierdo)"
    "Mujer desconocida" "Si avanzas sin más, perderás la bonificación."
    "Mujer desconocida" "¿Ya lo encontraste?"
    "Mujer desconocida" "Bien, ¿seguimos?"
    hide screen hidden_item


    show bg tut5 with dissolve
    $ renpy.notify(['Glosario actualizado', 'glossary'])
    "Mujer desconocida" "Tercero. Aquí abajo aparecerán todos los mensajes que informen de nuevas entradas o cambios en el diario."
    $ renpy.notify(['Escena desbloqueada', 'unlock'])
    "Mujer desconocida" "Y, si sientes que los diálogos te estorban..."
    "Mujer desconocida" "Puedes pulsar H para ocultarlos."
    show bg tut6 with dissolve
    "Mujer desconocida" "Elige tu camino con cuidado. En el mundo real, las elecciones importan. Lo que eliges no solo te define a ti, sino también a los acontecimientos del mundo que te rodea. Ten cuidado ahí fuera y no te dejes matar."
    "Mujer desconocida" "Sería una lástima."
    "Mujer desconocida" "Cuídate, agente [pl]."
    jump prologue












label versionend:
    hide screen control
    scene black
    show bg tobe
    $ renpy.pause(6)
    show screen patreon_link_end
    show bg endscreen with dissolve
    $ renpy.pause(3)

    dev "Gracias por tomarse el tiempo de jugar. Espero que se hayan divertido."

    "Apóyanos en {a=https://www.patreon.com/phillygames}{color=#359eff}https://www.patreon.com/phillygames{/color}{/a}"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
