label adv_chapter2:

    call adv_card_ch2

    scene bg_adv_village_gate
    with fade

    show screen adv_inventory

    show spr_mc alert at adv_right
    with dissolve

    narrator "Batu Layar menunggu dengan pintu berkunci dan lampu yang padam."
    narrator "Lepas tu ada orang menjerit."

    show spr_villager_1 terrified at adv_left
    with dissolve

    narrator "Seorang penduduk kampung terhuyung-hayang keluar dari gelap."
    narrator "Di belakangnya, ada sesuatu yang pucat dengan kaki terikat."
    narrator "Satu tubuh yang tak sepatutnya bergerak."

    menu:
        "Jerit amaran dan tarik dia ke tepi.":
            mc "Masuk rumah! Cepat!"
            narrator "Lelaki tu jatuh masuk ke pintu rumah."
            narrator "Makhluk tu terus berpaling ke arah MC."
            $ adv_fear += 1
            $ adv_add_note("Pocong berpaling kepada orang yang menghalang")

        "Berdiri diam dan perhatikan geraknya.":
            narrator "MC tahan diri daripada bergerak."
            narrator "Pocong tu mula perlahan."
            narrator "Sekejap je. Tapi cukup untuk nampak coraknya."
            $ adv_observed_pattern = True
            $ adv_understanding += 1
            $ adv_add_note("Diam sekejap buat pocong hilang rentak")

        "Terus angkat keris.":
            narrator "Bilah keris menangkap cahaya bulan."
            narrator "Pocong tu berhenti, kemudian menggigil lebih kuat."
            $ adv_pocong_anger += 1
            $ adv_aggressive_prepare = True

    $ adv_first_attack = renpy.call_screen("adv_timed_choice", "Pocong tu macam menarik nafas. Satu kampung terus senyap.", [("Tutup telinga", "cover"), ("Guna kamera telefon", "camera"), ("Berdiri teguh dan perhati", "watch")], "freeze", 10)

    if adv_first_attack == "cover":
        narrator "MC sempat tutup telinga."
        narrator "Sesuatu yang berat menghentam bahu dia dalam gelap."
        $ adv_damage += 1
        $ adv_add_note("Jeritan boleh ditahan, tapi tetap bahaya")

    elif adv_first_attack == "camera":
        narrator "Dia angkat kamera telefon tepat masa jeritan tu pecah di jalan."
        scene black
        with flash
        scene bg_adv_village_gate
        with fade
        show spr_mc alert at adv_right
        show spr_pocong present at adv_left
        with dissolve
        narrator "Mula-mula gambar tu nampak macam tak berguna."
        narrator "Lepas tu dia nampak: kain tertarik ketat di bahagian kaki."
        $ adv_understanding += 1
        $ adv_add_note("Kamera rakam kain kafan yang masih terikat")

    elif adv_first_attack == "watch":
        narrator "Dia perhati terlalu lama."
        narrator "Jeritan tu masuk terus ke kepala."
        $ adv_fear += 2
        $ adv_add_note("Jeritan buat badan hilang arah")

    else:
        narrator "MC terkaku."
        narrator "Jeritan tu buat dia jatuh tersungkur."
        $ adv_damage += 1
        $ adv_fear += 1

    narrator "Pocong tu berundur sebelum subuh."
    narrator "Bukan macam ia kalah."
    narrator "Macam ia cuma terganggu."

    hide spr_villager_1
    hide spr_pocong
    with dissolve

    jump adv_chapter3
