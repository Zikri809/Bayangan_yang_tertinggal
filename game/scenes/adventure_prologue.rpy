label adv_prologue:

    call adv_card_prologue

    scene bg_village_path_night
    with fade

    show spr_nayan neutral at adv_left
    with dissolve

    narrator "Nayan balik seorang diri malam tu."
    narrator "Malam di Kampung Batu Layar sunyi."
    narrator "Sunyi yang buat hati rasa tak sedap."

    menu:
        "Toleh ke belakang.":
            narrator "Yang ada cuma gelap."
            narrator "Dan sesuatu yang pucat, jauh di hujung jalan."

        "Panggil ke dalam gelap.":
            nayan "Siapa tu?"
            narrator "Tak ada orang jawab."
            narrator "Senyap tu yang menjawab."

        "Terus jalan.":
            narrator "Dia pujuk diri sendiri."
            narrator "Rumah dah dekat. Sikit je lagi."

    narrator "Lepas tu dia dengar."
    narrator "Duk."
    narrator "Duk."
    narrator "Duk."

    show spr_nayan terrified at adv_left
    with dissolve

    narrator "Sesuatu dalam kain putih bergerak ke arah dia."
    narrator "Bukan berjalan."
    narrator "Melompat."

    scene black
    with flash

    narrator "Jeritan tu tak sampai sesaat."
    narrator "Esok paginya, Nayan dah tak bernyawa."
    narrator "Telinga dia berdarah."

    jump adv_chapter1
