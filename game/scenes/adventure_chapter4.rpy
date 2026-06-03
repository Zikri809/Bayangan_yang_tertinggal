label adv_chapter4:

    call adv_card_ch4

    scene bg_adv_preparation
    with fade

    show spr_mc focused at center
    with dissolve

    narrator "Matahari mula tenggelam di belakang Batu Layar."
    narrator "MC susun semua barang dari beg kecilnya."

    $ renpy.call_screen("adv_case_summary")
    narrator "Buku nota itu bukan lagi senarai petunjuk."
    narrator "Ia mula nampak macam peta salah orang hidup."
    narrator "Satu halaman untuk gerak pocong."
    narrator "Satu halaman untuk kubur yang dibuat tergesa-gesa."
    narrator "Satu halaman untuk nama Azlan."

    if adv_hafiz_drives:
        narrator "Telefon Hafiz masuk sekejap: dia masih tunggu di luar kampung, siap kalau MC perlu keluar cepat."

    if adv_villager_helped:
        narrator "Lelaki yang MC bantu semalam tinggalkan air dan kain bersih dekat pintu. Tak ada ucapan, cuma tanda dia masih hidup."

    if adv_can_release():
        $ adv_release_ready = True
        narrator "Benang kafan. Surat lama. Tasbih."
        narrator "Kali ni, semua petunjuk bawa MC ke satu arah: melepaskan, bukan melawan."
        narrator "Masalahnya, faham waktu senja belum tentu cukup bila benda tu melompat tepat depan mata."
        narrator "Malam nanti, nota lengkap belum cukup. MC masih kena ikut rentak, sebut nama Azlan, dan dekat tanpa memaksa."
    else:
        narrator "Dia ada cukup barang untuk hidup."
        narrator "Mungkin belum cukup untuk faham."
        narrator "Dan untuk kes macam ni, hidup saja mungkin bukan menang."

    menu:
        "Bersedia untuk lepaskan dia." if adv_release_ready:
            narrator "MC biarkan keris dalam sarung."
            narrator "Tasbih dililit di pergelangan tangan."
            narrator "Surat Azlan dilipat dan diselitkan dalam buku nota, dekat dengan benang kafan."
            narrator "Kalau tangan MC menggigil nanti, sekurang-kurangnya dia tahu kenapa dia datang sini."
            $ adv_understanding += 1

        "Bersedia untuk paksa dia berundur.":
            narrator "MC pegang keris dekat tangan."
            narrator "Bila takut, rancangan paling kasar pun rasa paling selamat."
            narrator "Tapi makin lama bilah tu ada di tangan, makin senang lupa yang Azlan pernah jadi manusia."
            if adv_release_ready:
                narrator "Semua petunjuk masih ada, tapi pilihan itu buat jalan melepaskan dia jadi rapuh sebelum bermula."
            $ adv_aggressive_prepare = True
            $ adv_pocong_anger += 1

        "Bersedia untuk lari kalau semua gagal.":
            narrator "MC tengok jalan keluar dari kampung."
            narrator "Fikiran itu terasa pahit."
            narrator "Ada beza antara hidup untuk sambung siasatan, dengan lari sebab tak mahu faham."
            if adv_release_ready:
                narrator "Nota mungkin lengkap, tapi niat untuk lari boleh buat MC gagal mendekat bila simpulan perlu dibuka."
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
        narrator "Bukan macam cerita seram."
        narrator "Tapi macam seseorang yang ditinggalkan dalam keadaan salah."
        $ adv_understanding += 1

    elif adv_night_attack == "pray" and adv_has_tasbih:
        narrator "Doa tu menenangkan tangan MC."
        narrator "Pocong tu menggigil, tapi tak menyerang."
        narrator "Untuk beberapa saat, bunyi duk di jalan kampung berhenti."
        narrator "Senyap tu tak aman, tapi ia bagi ruang."
        $ adv_understanding += 1

    elif adv_night_attack == "salt" and adv_has_salt:
        narrator "Garam bertabur di atas jalan."
        narrator "Pocong tu tersentak ke belakang."
        narrator "Nampak macam dia sakit, bukan sekadar terhalang."
        if adv_release_ready:
            narrator "MC rasa ruang untuk melepaskan Azlan makin sempit."
        $ adv_pocong_anger += 1

    elif adv_night_attack == "keris":
        narrator "Bilah keris diangkat."
        narrator "Makhluk tu menjerit."
        if adv_release_ready:
            narrator "Semua jawapan dalam buku nota terasa jauh bila malam dibuka dengan bilah."
        $ adv_aggressive_prepare = True
        $ adv_pocong_anger += 1

    elif adv_night_attack == "still":
        $ adv_still_result = renpy.call_screen("adv_stillness", "Bunyi duk berhenti betul-betul depan MC.", 4)
        if adv_still_result == "still":
            if adv_observed_pattern:
                narrator "MC ingat kata Mak Ros."
                narrator "Dia berdiri diam, bukan sebab takut, tapi sebab dia faham rentak benda tu."
                narrator "Untuk satu detik, pocong tu pun diam."
                $ adv_understanding += 1
            else:
                narrator "MC berdiri diam, tapi dia tak tahu kenapa itu patut berkesan."
                narrator "Ragu itu cukup untuk buat tubuhnya lambat bergerak."
                $ adv_fear += 1
        else:
            narrator "MC tersentak sebelum jeda itu habis."
            narrator "Pocong tu menangkap gerakan kecil itu seperti jawapan."
            narrator "Hentaman kain dan tulang buat lutut MC hampir jatuh."
            $ adv_damage += 1
            $ adv_fear += 1

    elif adv_night_attack == "freeze" and adv_observed_pattern:
        narrator "MC hampir terkaku, tapi dia teringat jeda kecil dalam gerakan pocong tu."
        narrator "Dia diam dengan sengaja."
        $ adv_understanding += 1

    else:
        narrator "MC teragak-agak."
        narrator "Hentaman tu buat nafas dia putus sekejap."
        $ adv_damage += 1

    narrator "Malam belum selesai."
    narrator "Apa yang muncul di jalan tadi cuma amaran."
    narrator "Simpulan terakhir masih menunggu di kubur Azlan."

    jump adv_chapter5
