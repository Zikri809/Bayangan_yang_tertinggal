label adv_chapter4:

    call adv_card_ch4

    scene bg_adv_preparation
    with fade

    show spr_mc focused at center
    with dissolve

    narrator "Matahari mula tenggelam di belakang Batu Layar."
    narrator "MC susun semua barang dari beg kecilnya."

    $ renpy.call_screen("adv_case_summary")

    if adv_can_release():
        $ adv_release_ready = True
        narrator "Benang kafan. Surat lama. Tasbih."
        narrator "Kali ni, semua petunjuk bawa MC ke satu arah: melepaskan, bukan melawan."
    else:
        narrator "Dia ada cukup barang untuk hidup."
        narrator "Mungkin belum cukup untuk faham."

    menu:
        "Bersedia untuk lepaskan dia." if adv_release_ready:
            narrator "MC biarkan keris dalam sarung."
            narrator "Tasbih dililit di pergelangan tangan."
            $ adv_understanding += 1

        "Bersedia untuk paksa dia berundur.":
            narrator "MC pegang keris dekat tangan."
            narrator "Bila takut, rancangan paling kasar pun rasa paling selamat."
            $ adv_aggressive_prepare = True
            $ adv_pocong_anger += 1

        "Bersedia untuk lari kalau semua gagal.":
            narrator "MC tengok jalan keluar dari kampung."
            narrator "Fikiran itu terasa pahit."
            $ adv_fear += 1

    $ adv_ch4_choices = [("Suluh dengan lampu", "light")]
    if adv_has_tasbih:
        $ adv_ch4_choices.append(("Baca doa sambil pegang tasbih", "pray"))
    if adv_has_salt:
        $ adv_ch4_choices.append(("Tabur garam", "salt"))
    $ adv_ch4_choices.append(("Angkat keris", "keris"))
    if adv_observed_pattern:
        $ adv_ch4_choices.append(("Berdiri diam ikut jeda geraknya", "still"))
    else:
        $ adv_ch4_choices.append(("Berdiri diam", "still"))

    $ adv_night_attack = renpy.call_screen("adv_timed_choice", "Makhluk itu muncul di hujung kampung. MC nak guna petunjuk mana dulu?", adv_ch4_choices, "freeze", 12)

    if adv_night_attack == "light":
        narrator "Cahaya lampu suluh jatuh pada kain dan simpulan di kakinya."
        narrator "Pocong tu berhenti, macam baru pertama kali ada orang nampak dia betul-betul."
        $ adv_understanding += 1

    elif adv_night_attack == "pray" and adv_has_tasbih:
        narrator "Doa tu menenangkan tangan MC."
        narrator "Pocong tu menggigil, tapi tak menyerang."
        $ adv_understanding += 1

    elif adv_night_attack == "salt" and adv_has_salt:
        narrator "Garam bertabur di atas jalan."
        narrator "Pocong tu tersentak ke belakang."
        narrator "Nampak macam dia sakit, bukan sekadar terhalang."
        $ adv_pocong_anger += 1

    elif adv_night_attack == "keris":
        narrator "Bilah keris diangkat."
        narrator "Makhluk tu menjerit."
        $ adv_aggressive_prepare = True
        $ adv_pocong_anger += 1

    elif adv_night_attack == "still":
        if adv_observed_pattern:
            narrator "MC ingat kata Mak Ros."
            narrator "Dia berdiri diam, bukan sebab takut, tapi sebab dia faham rentak gerak makhluk itu."
            narrator "Untuk satu detik, pocong tu pun diam."
            $ adv_understanding += 1
        else:
            narrator "MC berdiri diam, tapi dia tak tahu kenapa itu patut berkesan."
            narrator "Ragu itu cukup untuk buat tubuhnya lambat bergerak."
            $ adv_fear += 1

    elif adv_night_attack == "freeze" and adv_observed_pattern:
        narrator "MC hampir terkaku, tapi dia teringat jeda kecil dalam gerakan pocong tu."
        narrator "Dia diam dengan sengaja."
        $ adv_understanding += 1

    else:
        narrator "MC teragak-agak."
        narrator "Hentaman tu buat nafas dia putus sekejap."
        $ adv_damage += 1

    jump adv_chapter5
