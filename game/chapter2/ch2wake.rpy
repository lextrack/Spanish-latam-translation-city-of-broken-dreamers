image bg ch2dream1 = "ch2dream1"
image bg ch2dream2 = "ch2dream2"

image bg ch2wake1 = "ch2wake1"
image bg ch2wake2 = "ch2wake2"
image bg ch2wake3 = "ch2wake3"

image bg chapter2 movie = Movie(play='video/intros/chapter2.webm')


label ch2wake:
    scene black with Dissolve(3)
    stop music fadeout 2.0
    show bg chapter2 movie with dissolve
    $ renpy.pause(2.5)
    scene black with Dissolve(3)
    show bg ch1dream3 with Dissolve(3)
    j "No hay otro camino."
    p "No me importa... haremos esto... no hay que sentirse mal."
    show bg ch1dream4 with dissolve
    j "*Se ahoga*{w} Lo sé..."
    j "Mira a tu alrededor, no tenemos otra opción."
    show bg ch2dream1 with dissolve
    p "Tiene que haber algo. Podemos hacer algo más... cualquier cosa."
    show bg ch2dream2 with dissolve
    p "¡Maldita seas, Meredith!"
    scene black with Dissolve(3)
    play music audio.calm fadein 2.0 fadeout 2.0
    show bg ch2wake1 with Dissolve(2)
    p "*Se aclara la garganta* Buenos días, Sam. ¿Qué tan temprano es?"
    s "Son las 7:40 am. Para usted, es demasiado temprano, señor."
    show bg ch2wake2 with dissolve
    p "Bueno, de todos modos estoy levantado. Sam, entra en la base de datos de la policía de Los Ángeles. ¿Dónde tienen a Hudson y su equipo?"
    s "Conectando..."
    s "Actualmente se encuentran en el centro de Los Cerritos en Lakewood."
    p "¿Lakewood?"
    s "Sí, señor."
    p "Espera, ¿todavía tienen los cuerpos y los están almacenando en Mil-town?"
    s "Si usted lo dice, señor. ¿Necesita más información?"
    p "No. Es extraño, ¿no crees? No respondas a eso."
    show bg ch2wake3 with dissolve
    p "*Se truena el cuello* Bueno, a la doctora le gusta trabajar con Milchers. Solo espero que no se ponga demasiado nerviosa."
    p "Sam, envía a la doctora Hamilton un mensaje de que estaré en su casa en unos cuarenta minutos."
    s "Hecho, señor. ¿Quiere que le prepare un café?"
    p "Por favor, y que no falte cafeína."
    jump ch2katie
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
