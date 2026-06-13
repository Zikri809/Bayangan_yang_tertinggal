label adv_chapter2:

    call adv_card_ch2

    scene bg_adv_village_gate
    with fade

    play ambient audio.amb_nayan_night fadein 1.5

    show screen adv_inventory

    show spr_mc alert at adv_right
    with dissolve

    if adv_hafiz_drives:
        narrator "Hafiz tunggu dekat kereta, enjin masih hidup, macam dia pun rasa kampung ni belum habis dengan sesiapa."

    narrator "Batu Layar menunggu dengan pintu berkunci dan lampu yang padam."
    play sound audio.sfx_villager_scream volume 1.35
    narrator "Lepas tu ada orang menjerit."

    show spr_villager_1 terrified at adv_left
    with dissolve

    narrator "Seorang lelaki kampung terhuyung-hayang keluar dari gelap."
    narrator "Di belakangnya, ada sesuatu yang pucat dengan kaki terikat."
    narrator "Satu tubuh yang tak sepatutnya bergerak."

    menu:
        "Jerit amaran dan tarik dia ke tepi.":
            mc "Masuk rumah! Cepat!"
            narrator "Lelaki tu jatuh masuk ke pintu rumah."
            narrator "Benda tu terus berpaling ke arah Aris."
            $ adv_villager_helped = True
            $ adv_fear += 1
            $ adv_add_note("Pocong berpaling kepada orang yang menghalang")

        "Berdiri diam dan perhatikan geraknya.":
            play rhythm audio.mus_rhythm_game fadein 0.2 volume 1.35
            $ adv_still_result = renpy.call_screen("adv_stillness", "Pocong tu melompat makin dekat. Aris paksa badan dia jangan ikut panik.", 4)
            stop rhythm fadeout 1.0
            if adv_still_result == "still":
                narrator "Aris tahan diri daripada bergerak."
                narrator "Lelaki kampung itu sempat merangkak masuk ke rumah."
                narrator "Pocong tu mula perlahan."
                narrator "Sekejap je. Tapi cukup untuk nampak coraknya."
                $ adv_villager_helped = True
                $ adv_observed_pattern = True
                $ adv_understanding += 1
                $ adv_add_note("Diam sekejap buat pocong hilang rentak")
            else:
                narrator "Jari Aris tersentak sebelum dia sempat kawal diri."
                narrator "Pocong tu terus melompat ke arah gerakan kecil itu."
                play sound audio.sfx_body_hit volume 1.25
                narrator "Lelaki kampung sempat masuk, tapi bahu Aris terkena hentaman kain dan tulang."
                $ adv_villager_helped = True
                $ adv_damage += 1
                $ adv_fear += 1
                $ adv_add_note("Pocong lebih cepat mengejar gerakan panik")

        "Terus angkat keris.":
            play sound audio.sfx_keris_draw volume 1.0
            narrator "Bilah keris menangkap cahaya bulan."
            narrator "Pocong tu berhenti, kemudian menggigil lebih kuat."
            $ adv_pocong_anger += 1
            $ adv_aggressive_prepare = True

    play sound audio.sfx_pocong_cry volume 1.45
    $ adv_first_attack = renpy.call_screen("adv_timed_choice", "Pocong tu macam menarik nafas. Satu kampung terus senyap.", [("Tutup telinga", "cover"), ("Guna kamera telefon", "camera"), ("Berdiri teguh dan perhati", "watch")], "freeze", 10)

    if adv_first_attack == "cover":
        narrator "Aris sempat tutup telinga."
        play sound audio.sfx_body_hit volume 1.25
        play earring audio.sfx_ear_ringing volume 1.25 fadein 0.15
        narrator "Sesuatu yang berat menghentam bahu dia dalam gelap."
        narrator "Untuk beberapa saat, dunia tinggal bunyi darah berdenyut dalam kepala."
        stop earring fadeout 1.4
        $ adv_damage += 1
        $ adv_add_note("Jeritan boleh ditahan, tapi tetap bahaya")

    elif adv_first_attack == "camera":
        narrator "Dia angkat kamera telefon tepat masa jeritan tu pecah di jalan."
        scene black
        play camera audio.sfx_camera_shutter volume 2.7
        with flash
        scene bg_adv_village_gate
        with fade
        show spr_mc alert at adv_right
        show spr_pocong present at adv_left
        with dissolve
        narrator "Mula-mula gambar tu nampak macam tak berguna."
        narrator "Lepas tu dia nampak: kain tertarik ketat di bahagian kaki."
        narrator "Dalam satu bingkai kabur, ada juga tanah basah melekat pada simpulan itu."
        narrator "Bukan sekadar benda muncul dari gelap. Macam ada kubur yang masih menariknya balik."
        $ adv_understanding += 1
        $ adv_add_note("Kamera rakam kain kafan yang masih terikat")

    elif adv_first_attack == "watch":
        play creature audio.sfx_creature_scream volume 1.0
        narrator "Dia perhati terlalu lama."
        stop creature fadeout 0.8
        narrator "Jeritan tu masuk terus ke kepala."
        $ adv_fear += 2
        $ adv_add_note("Jeritan buat badan hilang arah")

    else:
        narrator "Aris terkaku."
        narrator "Jeritan tu buat dia jatuh tersungkur."
        play sound audio.sfx_body_hit volume 1.25
        $ adv_damage += 1
        $ adv_fear += 1

    if adv_villager_helped:
        villager_1 "Dia... dia datang ikut jalan yang sama."
        villager_1 "Malam-malam sebelum ni pun macam tu. Kalau orang lari, dia kejar."
        villager_1 "Kalau semua tutup pintu, dia tunggu."
        narrator "Lelaki tu bercakap sambil menggigil, tapi kata-katanya melekat dalam kepala Aris."
        $ adv_add_note("Penduduk nampak pocong ulang laluan yang sama")

    else:
        narrator "Pintu rumah di sekeliling tertutup rapat."
        narrator "Tak ada sesiapa berani keluar untuk tanya sama ada Aris masih hidup."
        narrator "Di Batu Layar, takut dah jadi bahasa harian."

    narrator "Pocong tu berundur sebelum subuh."
    narrator "Bukan macam ia kalah."
    narrator "Macam ia cuma terganggu."
    narrator "Aris buka buku nota dengan tangan yang belum berhenti menggigil."
    narrator "Serangan itu bukan rawak."
    narrator "Ada laluan. Ada jeda. Ada simpulan."

    if adv_hafiz_drives:
        narrator "Telefon Hafiz masuk, skrin menyala dalam gelap."
        play sound audio.sfx_phone_ring loop
        $ renpy.call_screen("adv_incoming_call", "Hafiz")
        stop sound fadeout 0.2

        scene bg_adv_village_gate
        show spr_hafiz neutral at adv_phone_left
        show spr_mc alert at adv_phone_right
        with dissolve

        hafiz "Aku nampak dari jauh. Kau masih boleh teruskan?"
        mc "Boleh. Tapi benda ni bukan kes serang dan habis."
        hafiz "Jadi cari sebab dia masih ulang benda sama."

        hide spr_hafiz
        hide spr_mc
        with dissolve

    hide spr_villager_1
    hide spr_pocong
    with dissolve

    stop ambient fadeout 1.0

    jump adv_chapter3
