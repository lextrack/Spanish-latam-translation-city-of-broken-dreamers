image bg ch4sonja1 = "ch4sonja1"
image bg ch4sonja2 = "ch4sonja2"
image bg ch4sonja3 = "ch4sonja3"
image bg ch4sonja4 = "ch4sonja4"
image bg ch4sonja5 = "ch4sonja5"
image bg ch4sonja6 = "ch4sonja6"
image bg ch4sonja7 = "ch4sonja7"
image bg ch4sonja8 = "ch4sonja8"
image bg ch4sonja9 = "ch4sonja9"
image bg ch4sonja10 = "ch4sonja10"


label ch4sonja:
    scene black with Dissolve(2)
    j "Well, fuck me sideways. You idiots made a hell of a mess of the place."
    show bg ch4sonja1 with dissolve
    j "How'd you even know to come here?"
    "Ghost" "I had a spike into the city cameras. Thought it would be smart to keep an eye on any Ghost-friendly doctors."
    j "Don't act like you didn't get lucky."
    "Ghost" "Your husband seemed pretty tight with the Doc, if you know what I mean."
    j "Why the fuck should I care? How are your buddies doing?"
    "Ghost" "They're still breathing."
    j "Lucky them. Wake one of them up, Tex."
    show bg ch4sonja2 with dissolve
    t "Christ, Sonja, enough with that Tex bullshit. It's Charlie. I'm not even from Texas. I'm from Vermont."
    j "Whatever, Tex. You dress like a gay porn Cowboy, you get the nickname. Now, I got the one on the table."
    show bg ch4sonja3 with dissolve
    j "Why didn't you call us in?"
    "Ghost" "What the fuck... We did! We had the doctor gagged in the back, waiting for you!"
    j "Your excuse is, \"The call didn't go through\"?"
    "Ghost" "Uh... we were about to call."
    j "You tried to cut us out. That was fucking dumb. But, what really pisses me off is that you attacked a Doc. They're off limits."
    "Ghost" "We didn't hurt her... just roughed her up a little and put her in the back."
    j "*sighs* Just tell me what the fuck happened."
    "Ghost" "[pl] was here, but he wasn't alone. That fucking monster Charlie tipped us off about, he was here, too."
    show bg ch4sonja4 with dissolve
    j "The fuck you say! They were working together?"
    "Ghost" "Looks like it. Had each other's back and everything. The mark was with them."
    if "ch4docfigthback" not in extraevents:
        "Ghost" "That guy... he's not human. I shot him and it did nothing."
    show bg ch4sonja5 with dissolve
    t "Wait. Why the hell would this bodyguard guy be working with the Ghost trying to bring the target in?"
    j "How the fuck should I know?"
    show bg ch4sonja6 with dissolve
    t "Out of the way, shithead, the grown-ups need a heart to heart."
    j "Not now, Tex."
    t "Yeah, now, over here."
    show bg ch4sonja7 with dissolve
    t "Look, [p]'s a damn legend. He's saved my ass more than once."
    j "You asking my permissions to fuck him?"
    t "But you and I know he's been off his game lately. It'd be nice to let him have a win."
    j "So he got one. Throw him a party tomorrow, drinks are on you."
    t "What I'm getting at is, this doesn't make any sense. Him stopping here with the girl?"
    j "Why are we even talking about this? Mark's lost. He's probably at Baynard as we speak."
    t "I don't think so. The youngins say he was working with that beast, Gibson. "
    j "What are you getting at?"
    t "He's not going to Baynard. He's gone native."
    show bg ch4sonja8 with dissolve
    j "You don't know what the fuck you're talking about."
    t "This is going to be a clusterfuck. So I need to know where we stand."
    j "Right the fuck here."
    t "We're a team now, Sonja."
    show bg ch4sonja9 with dissolve
    t "Like I said, [p] is a good man. So I can understand wanting to give him a head start."
    t "But if he becomes the target, you have to know, you tip him off, slow us down or hold back, you'll catch a bullet just before he does."
    t "We clear?"
    show bg ch4sonja10 with dissolve
    j "Yeah, perfectly clear, Tex. And if you threaten me again I'll shove Stella so far up your ass you'll be coughing bullets."
    t "Fuck, I missed working with you!"
    j "Yeah, you too, buddy. Not like it matters. There is no way that [p] went native. Trust me, we'll be getting the message that the contract was pulled any minute now."
    show bg ch4sonja9 with dissolve
    t "That happens, I'll be buying tonight."
    j "Ha, you're going to regret that, Tex."
    t "It's not going to happen, though."
    j "Then we haul his ass in and make {i}him{/i} buy."
    t "Sounds good to me."
    jump ch4ellens
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
