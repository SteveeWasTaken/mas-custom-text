init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_text",
            prompt="Custom Text",
            category=["Custom Text"],
            pool=True,
            unlocked=True
        )
    )

label monika_text:
    m "What do you want me to say, [player]?{nw}"
    $ moniText = mas_input(
            "What do you want me to say, [player]?"
        )
    m "What expression should I do?{nw}"
    $ _history_list.pop()
    menu:
        m "What expression should I do?{fast}"

        "Default":
            m 1eua "[moniText]"
            return

        "Default (Mouth)":
            m 1eub "[moniText]"
            return

        "Worried":
            m 1ekc "[moniText]"
            return

        "Worried (Mouth)":
            m 1ekc "[moniText]"
            return

        "Surprised":
            m 1euc "[moniText]"
            return

        "Surprised (Mouth)":
            m 1eud "[moniText]"
            return

        "Confused":
            m 1etc "[moniText]"
            return

        "Confused (Mouth)":
            m 1etd "[moniText]"
            return

        "Angry":
            m 1efc "[moniText]"
            return

        "Next":
            m "{nw}"

        "Custom":
            m 1eud "[moniText]"
            return

    $ _history_list.pop()
    menu:
        m "What expression should I do?{fast}"

        "Angry (Mouth)":
            m 1efd "[moniText]"
            return

        "Happy":
            m 1hua "[moniText]"
            return

        "Happy (Mouth)":
            m 1hub "[moniText]"
            return

        "Smug":
            m 1tua "[moniText]"
            return

        "Smug (Mouth)":
            m 1tub "[moniText]"
            return

        "Sparkling":
            m 1sua "[moniText]"
            return

        "Sparkling (Mouth)":
            m 1sub "[moniText]"
            return

        "Wink (Left)":
            m 1nua "[moniText]"
            return

        "Wink (Left & Mouth)":
            m 1nub "[moniText]"
            return

        "Wink (Right)":
            m 1kua "[moniText]"
            return

        "Next":
            m "{nw}"

    $ _history_list.pop()
    menu:
        m "What expression should I do?{fast}"

        "Wink (Right & Mouth)":
            m 1kub "[moniText]"
            return

        "Smug (Left)":
            m 1gua "[moniText]"
            return

        "Smug (Left & Mouth)":
            m 1gub "[moniText]"
            return

        "Smug (Right)":
            m 1mua "[moniText]"
            return

        "Smug (Right & Mouth)":
            m 1mub "[moniText]"
            return
    return