label adv_prologue:

    call adv_card_prologue

    scene bg_village_path_night
    with fade

    play ambient audio.amb_nayan_night fadein 1.5

    show spr_nayan neutral at adv_left
    with dissolve

    narrator "Nayan balik seorang diri malam tu."
    narrator "Malam di Kampung Batu Layar sunyi."
    narrator "Sunyi yang buat hati rasa tak sedap."
    narrator "Lampu rumah orang kampung masih ada yang menyala, tapi tak ada satu pun tingkap terbuka."
    narrator "Macam seluruh kampung sedang menahan nafas."
    narrator "Telefon Nayan bergetar sekali, kemudian skrin jadi gelap."
    narrator "Tak ada line."

    menu:
        "Toleh ke belakang.":
            narrator "Yang ada cuma gelap."
            narrator "Dan sesuatu yang pucat, jauh di hujung jalan."
            narrator "Bila Nayan cuba tengok betul-betul, benda tu hilang celah pokok."

        "Panggil ke dalam gelap.":
            nayan "Siapa tu?"
            narrator "Tak ada orang jawab."
            narrator "Senyap tu yang menjawab."
            narrator "Lepas beberapa saat, ada bunyi macam orang menangis dari arah kubur lama."

        "Terus jalan.":
            narrator "Dia pujuk diri sendiri."
            narrator "Rumah dah dekat. Sikit je lagi."
            narrator "Tapi kaki dia mula berat, macam tanah basah cuba tarik tapaknya."

    narrator "Nayan percepatkan langkah."
    narrator "Di sebelah jalan, kain putih tersangkut pada pagar buluh, bergerak perlahan walaupun angin tak ada."
    narrator "Nayan hampir tergelak kecil, paksa diri percaya itu cuma kain orang jemur."
    narrator "Kemudian kain itu jatuh sendiri."
    narrator "Lepas tu dia dengar."
    play sound audio.sfx_pocong_cry volume 1.45
    narrator "Duk."
    narrator "Duk."
    narrator "Duk."

    show spr_nayan terrified at adv_left
    with dissolve

    narrator "Sesuatu dalam kain putih bergerak ke arah dia."
    narrator "Bukan berjalan."
    narrator "Melompat."
    narrator "Setiap lompatan ada jeda kecil."
    narrator "Cukup lama untuk Nayan sempat berharap ia berhenti."
    narrator "Cukup cepat untuk harapan tu mati balik."

    stop ambient fadeout 0.6
    scene black
    play sound audio.sfx_nayan_scream
    with flash

    narrator "Jeritan tu tak sampai sesaat."
    narrator "Esok paginya, Nayan dah tak bernyawa."
    narrator "Telinga dia berdarah."

    jump adv_chapter1
