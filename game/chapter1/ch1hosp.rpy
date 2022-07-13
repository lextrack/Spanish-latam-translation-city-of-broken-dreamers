

image bg ch1hosp1 = "ch1hosp1"
image bg ch1hosp2 = "ch1hosp2"
image bg ch1hosp3 = "ch1hosp3"
image bg ch1hosp4 = "ch1hosp4"
image bg ch1hosp5 = "ch1hosp5"
image bg ch1hosp6 = "ch1hosp6"
image bg ch1hosp7 = "ch1hosp7"
image bg ch1hosp8 = "ch1hosp8"
image bg ch1hosp9 = "ch1hosp9"
image bg ch1hosp10 = "ch1hosp10"
image bg ch1hosp11 = "ch1hosp11"
image bg ch1hosp12 = "ch1hosp12"
image bg ch1hosp13 = "ch1hosp13"
image bg ch1hosp14 = "ch1hosp14"
image bg ch1hosp15 = "ch1hosp15"
image bg ch1hosp16 = "ch1hosp16"
image bg ch1hosp17 = "ch1hosp17"
image bg ch1hosp18 = "ch1hosp18"
image bg ch1hosp19 = "ch1hosp19"
image bg ch1hosp20 = "ch1hosp20"

image bg ch1aftermeeting = "ch1aftermeeting1"



label ch1hosp:
    show bg ch1aftermeeting with Dissolve(1)

    p "(Si voy a hacer esto, necesitaré información y no tengo tiempo que perder.)"
    p "(La casa de Katie no está lejos, le haré una visita. Tal vez ella pueda ayudarme a averiguar exactamente cómo Hudson y su equipo fueron eliminados. Necesito saber con qué estoy tratando.)"
    scene black with Dissolve(1)
    play music audio.calm fadein 2.0 fadeout 2.0
    show text "{=trans}UNA HORA MÁS TARDE, EN LA CLÍNICA DE LA DRA. HAMILTON{/=trans}" with Dissolve(1)
    show bg ch1hosp9 with Dissolve(2)
    if not persistent.ch1card3:
        $ renpy.notify(['Posible pista', 'alert'])
        show screen hidden_item("ch1card3", "ch1card3", 787, 290, 69, 134)
    k "Quédate quieto, grandullón."
    "Chico" "Vale..."
    p "(Le daré un segundo, espero que su trato sea más amable con los niños.)"
    hide screen hidden_item
    show bg ch1hosp6 with dissolve
    k "Sé que eres un tipo duro, pero la próxima vez avísale a tu mamá de inmediato. ¿De acuerdo?"
    "Chico" "De acuerdo..."
    show bg ch1hosp7 with dissolve
    k "Bien. Ahora, eso fue bastante asqueroso, ¿eh? ¡Todo ese pus!"
    "Chico" "Sí..."
    k "Sin embargo, fue bastante genial, ¿no?"
    "Chico" "¡Sí!"
    k "Fue como reventar un grano gigante."
    "Chico" "¡Ugh! ¡Sí!"
    show bg ch1hosp8 with dissolve
    k "Muy bien, sal a ver a tu madre. Puedes decirle que estás mejor."
    show bg ch1hosp1 with dissolve
    p "Veo que tu trato con los niños es mejor."
    k "Los niños siempre están de acuerdo. Lo hace mucho más fácil."
    k "¿Puedo preguntar a qué se debe esta visita sorpresa?"
    p "Unos Fantasmas fueron eliminados la otra noche. Esperaba que pudieras ayudarme."
    show bg ch1hosp2 with dissolve
    k "Me enteré de eso. ¿Qué necesitas?"
    p "No me fío de la información que recibo. Prefiero que sea de alguien externo. Alguien como tú."
    show bg ch1hosp4 with dissolve
    k "Supongo que puedo ayudar. Entonces, ¿es un nuevo trabajo?"
    p "Correcto."
    menu:
        "Dile que has quedado con Victoria esta noche":
            $ extraevents.append("ch1katieknowsvic")
            p "Tengo que reunirme con una tal Victoria Shields esta noche, para arreglar asuntos."
            show bg ch1hosp3 with dissolve
            k "[p], tienes que tener cuidado con ella."
            p "Lo sé."
            k "De verdad. La he visto por ahí. No confío en ella. Ni en lo más mínimo."
            menu:
                "Seré cuidadoso":
                    p "No te preocupes, tendré cuidado."
                    show bg ch1hosp1 with dissolve
                    k "Eso espero."
                "Solo iremos beber.":
                    $ extraevents.append("ch1tellkatie")
                    p "No te preocupes; solo son bebidas."
                    show bg ch1hosp5 with dissolve
                    k "Oh..."
        "Dile que vas a discutir el pago esta noche":


            p "Discutiré el pago esta noche."
            k "Bueno, ya es hora de que aceptes un trabajo."

    show bg ch1hosp10 with dissolve
    k "¿Puedo preguntar de qué trata el trabajo?"
    p "Una chica desaparecida, aparentemente es muy importante."
    show bg ch1hosp11 with dissolve
    k "¿La misma que busca la policía?"
    p "Sí, creo que sí. No he estado prestando atención a las noticias."
    show bg ch1hosp12 with dissolve
    k "Bueno, espero poder ayudar."
    show bg ch1hosp13 with dissolve
    k "Ahora, si me disculpas, tengo una cita con la ducha sónica. Ese chico tenía pus por todas partes."
    if k_score >= 1:
        show bg ch1hosp14 with dissolve
        n "El sonido de la ducha sónica invade la habitación mientras la barrera de vidrio se eleva desde el suelo hasta sus pechos."
        show bg ch1hosp15 with dissolve
        k "*Suspira* Otra bata de laboratorio destruida. Te veo mañana, [p]."
        p "Ummm. *Se aclara la garganta* Por supuesto."
        menu:
            "Mira un poco":
                show bg ch1hosp16 with dissolve
                n "La ducha sónica está en funcionamiento y levanta el cabello de Katie."
                show bg ch1hosp17 with dissolve
                p "(Realmente debería irme, pero ¡guau!)"
                show bg ch1hosp18 with dissolve
                p "(Maldita sea, quienquiera que haya inventado el vidrio esmerilado, lo odio.)"
                if k_score >= 2:
                    show bg ch1hosp19 with dissolve
                    k "[p], pensé que te habías ido."
                    p "Lo siento, ya me voy."
                    k "Je, está bien. Te veré mañana."
                    jump ch1hospend
                else:
                    $ k_score -= 1
                    show bg ch1hosp20 with dissolve
                    k "Umm, probablemente deberías irte, [p]..."
                    p "Lo siento ..."
                    jump ch1hospend
            "Irte":
                jump ch1hospend
    else:
        k "Te veré mañana."
        p "Cuídete, Doc."

        jump ch1hospend

label ch1hospend:
    scene black with Dissolve(1)
    p "(Me alistare para esta noche.)"
    jump ch1gloriaapart
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
