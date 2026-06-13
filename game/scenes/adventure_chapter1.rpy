label adv_chapter1:

    call adv_card_ch1

    scene bg_adv_restaurant
    with fade

    play ambient audio.amb_restaurant_crowd fadein 1.0

    show spr_hafiz neutral at adv_trio_left
    show spr_mc neutral at adv_trio_right
    with dissolve

    hafiz "Kampung Batu Layar. Kau pernah dengar pasal tempat tu?"
    mc "Pocong?"
    hafiz "Itulah yang orang cakap. Ada benda melompat dekat kawasan kubur."
    hafiz "Tapi cerita orang kampung ni pelik sikit."
    hafiz "Dia tak muncul merata. Dia ulang jalan yang sama, macam ada benda yang belum selesai."

    narrator "Masa tu, telefon Aris berbunyi."

    play sound audio.sfx_phone_ring loop
    $ renpy.call_screen("adv_incoming_call", "Melur")
    stop sound fadeout 0.2

    scene bg_adv_restaurant
    show spr_melur phone at adv_phone_left
    show spr_mc neutral at adv_phone_right
    with dissolve

    melur "Encik... saya nak minta tolong pasal abang saya."
    melur "Abang saya dah lama meninggal. Tapi... dia masih ada dekat sana."
    melur "Anak abang saya masih di kampung tu. Dia pun tak tahu cerita penuh."
    melur "Saya bukan minta encik bunuh dia."
    melur "Saya cuma tak sanggup dengar orang panggil dia bala sampai hari ni."
    melur "Tolong lepaskan dia dengan cara yang betul."
    $ adv_knows_child = True

    hide spr_melur
    hide spr_mc
    scene bg_adv_restaurant
    with dissolve

    show spr_hafiz neutral at adv_trio_left
    show spr_owner serious at adv_trio_center
    show spr_mc neutral at adv_trio_right
    with dissolve

    owner "Kalau pocong tu masih terikat, tengok simpulan kafan dulu."
    owner "Kalau jenazah diurus masa semua orang marah, atau semua nak cepat habis, roh boleh tersangkut."
    owner "Tapi jangan fikir simpulan tu cuma kain."
    owner "Kadang-kadang simpulan yang paling ketat datang dari fitnah, takut, dan nama yang orang sengaja padam."

    narrator "Abang Zul menghulur satu beg kecil kepada Aris."
    narrator "Lampu suluh. Kamera telefon. Keris kecil. Buku nota kosong."
    narrator "Dia letak beg tu perlahan-lahan, macam isinya bukan barang lawan, tapi tanggungjawab."

    $ adv_add_note("Melepaskan tak sama dengan membunuh")

    menu:
        "Tanya pasal pengebumian tergesa-gesa.":
            mc "Kalau pengebumian dibuat tergesa-gesa?"
            owner "Itu yang bahaya. Banyak benda boleh terlepas pandang. Simpulan kafan pun boleh tak sempat dibuka."
            owner "Bila orang urus jenazah dalam marah, mereka tutup tanah cepat-cepat."
            owner "Tapi benda yang tak disebut, tak semestinya ikut tertanam."
            $ adv_understanding += 1
            $ adv_add_note("Jenazah diurus tergesa-gesa boleh perangkap roh")

        "Tanya apa yang pocong tu nak.":
            mc "Apa yang dia nak sebenarnya?"
            owner "Bukan semua nak balas dendam. Ada yang cuma tak tahu nak pergi mana."
            owner "Kalau dia pernah jadi manusia sebelum jadi cerita seram, cari dulu siapa dia."
            owner "Nama kadang-kadang lebih kuat daripada bilah."
            $ adv_understanding += 1
            $ adv_add_note("Pocong itu mungkin sesat, bukan jahat")

        "Tanya cara nak hentikan dia.":
            mc "Kalau dia serang?"
            owner "Bertahan dulu. Jangan terus ingat semua benda boleh selesai dengan senjata."
            owner "Keris boleh buka ruang. Tapi kalau dalam kepala kau cuma nak menang, kau balik dengan jawapan yang salah."
            $ adv_add_note("Perhati dulu sebelum menyerang")

    hide spr_owner
    with dissolve

    hafiz "Kau nak aku ikut?"

    menu:
        "Pergi seorang. Lagi cepat.":
            mc "Aku pergi sorang."
            narrator "Jalan ke Batu Layar terasa lebih jauh daripada sepatutnya."
            $ adv_hafiz_drives = False

        "Biar Hafiz drive.":
            mc "Kau drive."
            narrator "Hafiz tak tanya lebih."
            narrator "Sebab itulah Aris percayakan Hafiz."
            $ adv_hafiz_drives = True
            $ adv_fear -= 1

    stop ambient fadeout 1.0

    jump adv_chapter2
