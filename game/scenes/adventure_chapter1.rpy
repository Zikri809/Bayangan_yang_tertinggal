label adv_chapter1:

    call adv_card_ch1

    scene bg_adv_restaurant
    with fade

    show spr_hafiz neutral at adv_trio_left
    show spr_mc neutral at adv_trio_right
    with dissolve

    hafiz "Kampung Batu Layar. Kau pernah dengar pasal tempat tu?"
    mc "Pocong?"
    hafiz "Itulah yang orang cakap. Ada benda melompat dekat kawasan kubur."

    narrator "Masa tu, telefon MC berbunyi."

    $ renpy.call_screen("adv_incoming_call", "Melur")

    scene bg_adv_restaurant
    show spr_melur phone at adv_phone_left
    show spr_mc neutral at adv_phone_right
    show screen adv_phone_call_overlay
    with dissolve

    melur "Encik... saya nak minta tolong pasal abang saya."
    melur "Abang saya dah lama meninggal. Tapi... dia masih ada dekat sana."
    melur "Tolong lepaskan dia dengan cara yang betul."

    hide screen adv_phone_call_overlay
    hide spr_melur
    hide spr_mc
    scene bg_adv_restaurant
    with dissolve

    show spr_hafiz neutral at adv_trio_left
    show spr_owner serious at adv_trio_center
    show spr_mc neutral at adv_trio_right
    with dissolve

    owner "Kalau pocong masih terikat, tengok simpulan kafan dulu."
    owner "Kalau orang kebumikan dia masa semua tengah marah, atau semua nak cepat selesai, roh boleh tersangkut."

    narrator "Abang Zul menghulur satu beg kecil kepada MC."
    narrator "Lampu suluh. Kamera telefon. Keris kecil. Buku nota kosong."

    $ adv_add_note("Melepaskan tak sama dengan membunuh")

    menu:
        "Tanya pasal pengebumian tergesa-gesa.":
            mc "Kalau pengebumian dibuat tergesa-gesa?"
            owner "Itu yang bahaya. Banyak benda boleh terlepas pandang. Simpulan kafan pun boleh tak sempat dibuka."
            $ adv_understanding += 1
            $ adv_add_note("Pengebumian tergesa-gesa boleh perangkap roh")

        "Tanya apa yang pocong tu nak.":
            mc "Apa yang dia nak sebenarnya?"
            owner "Bukan semua nak balas dendam. Ada yang cuma tak tahu nak pergi mana."
            $ adv_understanding += 1
            $ adv_add_note("Pocong itu mungkin sesat, bukan jahat")

        "Tanya cara nak hentikan dia.":
            mc "Kalau dia serang?"
            owner "Bertahan dulu. Jangan terus ingat semua benda boleh selesai dengan senjata."
            $ adv_add_note("Perhati dulu sebelum menyerang")

    hide spr_owner
    with dissolve

    hafiz "Kau nak aku ikut?"

    menu:
        "Pergi seorang. Lagi cepat.":
            mc "Aku pergi sorang."
            narrator "Jalan ke Batu Layar terasa lebih jauh daripada sepatutnya."

        "Biar Hafiz drive.":
            mc "Kau drive."
            narrator "Hafiz tak tanya lebih."
            narrator "Sebab itulah MC percayakan Hafiz."
            $ adv_fear -= 1

    jump adv_chapter2
