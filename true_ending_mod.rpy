label hatchery_remy_true_ending_mod:
    if renpy.python.store_dicts["store"].get("hatchling", "None") == "None":
        label hatchery_remy_true_ending_mod_no_requirements:
            pass
    else:
        if hatchling == "Amely":
            Ad annoyed b "I know her. She's been living in the orphanage all her life while you went on with yours without a care in the world."
            Ry angry "You mean the orphan who I've just adopted? You were the one who just dumped her?"
            An rage flip "I just told you I didn't have any choice in the matter!"
            Ry "Why did you even choose that name anyway? How is it in any way significant to you of all people?"
            An sad flip "It was after her mother, Amelia. I felt she at least deserved the respect of having her child named after her after dying  in the cold."
            Ry shy "You mean I've just adopted my own daughter?"
            An "I guess so."
            Ry smile "That makes me feel so much better; I'll have a part of Amelia living with me forever now."
            Ry "It's like she's never left."
            Br stern flip "We should be focusing on Reza right now. This can wait until after he's been dealt with"
            Ry "You're right. This is more important - I need to ensure that I can be there for my daughter after this is all over."
            Lo think "That's definitely important."
        else:
            Ad disappoint b "..."
            Ad annoyed b "I know her. She's been living in the orphanage all her life while you went on with yours without a care in the world."
            Ry "Why even that name?"
            An "After the mother, I guess."
            Br "Now that you mention it, I think the victim's name was a bit different..."
            Br "A... Am..."
            Br stern flip "Amelia, that was it. Froze to death during a winter night, if I recall correctly."
            Ry shy "What...?"
            Ad disappoint b "Remy, I never told you this, but... shortly before she died, Amelia found out that she was pregnant."
            Ad sad b "That means... you..."
            Ry "Adine, I've changed my mind. I'll be adopting both of them. It's not against the rules either because I'm the father."
            Ad "I guess that can be arranged."
            Br stern flip "After this though, we should be focusing on Reza right now."
            Lo think "Agreed."
            Ry shy "..."

    label hatchery_remy_true_ending_mod_end:
        pass
