



image bg ch4docmorndown1 = "ch4docmorndown1"
image bg ch4docmorndown2 = "ch4docmorndown2"
image bg ch4docmorndown3 = "ch4docmorndown3"
image bg ch4docmorndown4 = "ch4docmorndown4"
image bg ch4docmorndown5 = "ch4docmorndown5"
image bg ch4docmorndown6 = "ch4docmorndown6"
image bg ch4docmorndown7 = "ch4docmorndown7"
image bg ch4docmorndown8 = "ch4docmorndown8"
image bg ch4docmorndown9 = "ch4docmorndown9"
image bg ch4docmorndown10 = "ch4docmorndown10"
image bg ch4docmorndown11 = "ch4docmorndown11"
image bg ch4docmorndown12 = "ch4docmorndown12"
image bg ch4docmorndown13 = "ch4docmorndown13"
image bg ch4docmorndown14 = "ch4docmorndown14"
image bg ch4docmorndown15 = "ch4docmorndown15"
image bg ch4docmorndown16 = "ch4docmorndown16"
image bg ch4docmorndown17 = "ch4docmorndown17"
image bg ch4docmorndown18 = "ch4docmorndown18"
image bg ch4docmorndown19 = "ch4docmorndown19"
image bg ch4docmorndown20 = "ch4docmorndown20"
image bg ch4docmorndown21 = "ch4docmorndown21"
image bg ch4docmorndown22 = "ch4docmorndown22"
image bg ch4docmorndown23 = "ch4docmorndown23"

image ch4gloriapanmovie = Movie(play='video/chapter-4-video/ch4gloriapan.webm', loop=False)
image bg ch4gloriapan movie:
    "ch4gloriapanmovie"
    pause 10.0
    "ch4gloriapanend"



label ch4morning:
    scene black with Dissolve(2)
    g "Ugh..."
    g "I feel like hell..."
    show bg ch4docmorndown1 with dissolve
    g "(Wait... Where am I?)"
    g "Henry?"
    show bg ch4docmorndown2 with dissolve
    g "Henry! Where are we?! What's going on?!"
    g "What is this place?! Are you okay? God, did I..."
    show bg ch4docmorndown4 with dissolve
    h "Gloria, calm down. It's alright."
    if "ch4fightkill" in extraevents:
        g "That man, he was about to kill you!"
        h "He didn't. You stopped him."
    elif "ch4fightspare" in extraevents:
        $ g_score += 1
        g "That man, he was going to hurt you!"
        h "You stopped him. I'm fine."
    else:
        g "You were about to kill someone. Henry... did you..."
        h "You stopped me from making that mistake. Thank you. "
    show bg ch4docmorndown5 with dissolve
    g "But... where are we? Did he take us in?"
    h "Just calm down, princess. He may have saved your life."
    g "What..?"
    show bg ch4docmorndown6 with dissolve
    h "*Sigh* After the fight you passed out. And we came here."
    g "But where is here?"
    show bg ch4docmorndown7 with dissolve
    k "\"Here\" is my home and office, but not really in that order. Hi, I'm Doctor Hamilton. You're Gloria, right?"
    g "Yeah. But..."
    k "I know you're scared. I promise, no one is going to hurt you here."
    show bg ch4docmorndown9 with dissolve
    g "What about that man. The one from my dream? Is he here?"
    show bg ch4docmorndown8 with dissolve
    k "Your dream?"
    g "He attacked us."
    k "If you mean [p], he isn't going to hurt you. He's not like that."
    if k_score >= 3:
        show bg ch4docmorndown12 with dissolve
        k "He can be pretty sweet at times."
    else:
        k "He can be an ass, but besides that, he's a decent person."
    k "He and Henry brought you in. You were having a seizure of some sort. I gave you something to calm you down; that's why you feel light-headed."
    show bg ch4docmorndown11 with dissolve
    g "I feel fine, but thank you."
    k "No need."
    g "So, am I okay? I'm good to go?"
    k "I can't stop you from leaving, Gloria, but I'd prefer you stay."
    show bg ch4docmorndown10 with dissolve
    g "Why?"
    k "I just don't think it's the best idea, Gloria."
    g "What's going on? Am I in danger?"
    k "... not that I can see."
    g "So, why can't we leave then?"
    k "I want to understand what's wrong with you."
    g "Katie, I know you mean well, but you have no idea how many times I've heard that."
    k "I understand..."
    g "I'll stay for a moment, long enough to talk to [p]..."
    "Katie turns and sees you walking up to them and pulls you aside as you arrive"
    show bg ch4docmorndown14 with Dissolve(1)
    k "That tranq should have her talking in circles right now. But she's more alert than I am."
    p "Well, that doesn't sound like a big deal."
    k "Well, maybe not. Also... did you ever mention my name to her before?"
    p "We've never talked."
    k "Oh. Well, that's just weird. Anyway, at least she wants to talk to you."
    p "I am not sure she'll be receptive to me, but I'll try."
    $ g_met = True
    if "ch4fightkill" in extraevents:
        show bg ch4docmorndown15 with dissolve
        g "It's you. You know, without the mask, you're really not that scary."
        p "Well, I'm not out to frighten you."
        g "When you aren't attacking me?"
        p "Well, not now... anyway."
        show bg ch4docmorndown16 with dissolve
        g "Am I your prisoner?"
        p "No."
        g "Then why won't you let us leave?"
        p "Because I don't want to see this escalate any more than it already has."
        p "There are a lot of people after you. After what you did last night, I now know why."
    else:
        show bg ch4docmorndown16 with dissolve
        g "I like you more without the mask."
        p "I do too. Sorry if I scared you."
        g "I have a feeling I scared you more. It's why we're here and not in jail or whatever. Right?"
        p "More or less. But you have to know, it's not safe to leave. Not yet, at least. And certainly not on your own."
    g "This is the weirdest kidnapping ever."
    p "Heh, yeah, it probably is."
    g "So, are you helping us now? I don't understand."
    p "..."
    g "From kidnapper to protector. Feels like a movie."
    show bg ch4docmorndown17 with dissolve
    g "*Stomach begins to growl* Do you have anything to eat?"
    p "Not so much here..."
    show bg ch4docmorndown19 with dissolve
    h "Any place close by? Something quiet where we won't bring attention to ourselves?"
    p "There's a dive down the alley. It's shit, but nobody will see us. Nobody that cares at least."
    show bg ch4docmorndown18 with dissolve
    g "I don't care if Shanlon Russell is broadcasting from there. I'm starving."
    p "That would be something to see."
    g "Let's go then."
    show bg ch4docmorndown21 with dissolve
    k "If you guys are going out, I have a spare top she can wear, at least."
    k "Come on, Gloria, let's get you out of that thing."
    g "I don't want to impose."
    k "Nonsense. Come on. You two wait down here."
    g "I was a little rude to you before, Katie. Sorry about that. I can tell you mean well."
    k "Already forgotten, kiddo. Come on. I think I have just the shirt."
    show bg ch4docmorndown22 with dissolve
    p "..."
    h "..."
    p "How do they do that?"
    h "Gloria was always great at making friends."
    p "And Doc's Doc."
    h "And while they're gone. I'll say this once. I'm watching you. You do anything that endangers her and this truce is over."
    menu:
        "Do what you need to":
            $ h_score += 1
            p "Do what you need to do, Henry. I'll do the same."
            h "You may have helped Gloria. But I don't trust you, not by a longshot."
        "Don't try to scare me":
            p "Don't try to intimidate me, Henry, you're not going to like where it goes."
            h "Is that a threat?"
            p "Yes."
            p "But in the spirit of openness:"

    p "I have no intention of screwing you over. She is too important for that."
    show bg ch4gloriapan movie with dissolve
    g "If I'm gonna have to break you two up again, can it at least wait until after breakfast?"
    h "Sorry."
    p "You ready to go?"
    show bg ch4docmorndown23 with dissolve
    g "My God, yes! I've eaten nothing but Coco-Crunchers for the last few days."
    h "I thought those were your favorite!"
    g "*Laughs* They are! I love 'em, but a girl can't live off carbs alone, Bigs!"
    jump ch4bar
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
