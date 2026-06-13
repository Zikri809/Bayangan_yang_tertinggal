label adv_chapter5:

    call adv_card_ch5

    $ adv_final_pattern_used = False
    $ adv_final_identity_used = False
    $ adv_final_release_used = False
    $ adv_final_force_used = False

    scene bg_adv_final_grave
    with fade

    play music audio.mus_final_confrontation fadein 1.5 volume adv_bg_music_volume

    show spr_mc focused at adv_right
    show spr_pocong present at adv_left
    with dissolve

    narrator "Pukul 2:47 pagi, Aris sampai di kubur itu."
    narrator "Pocong tu menunggu di sana."
    narrator "Kain di kakinya tertarik ketat, seolah-olah tanah sendiri belum mahu melepaskan dia."
    narrator "Kali ni, buku nota bukan sekadar catatan."
    narrator "Setiap petunjuk mungkin jadi cara untuk terus hidup."
    narrator "Aris teringat suara Mak Ros."
    narrator "Jangan lari kalau mahu baca rentaknya."
    narrator "Dia teringat tanah kubur yang tak rata."
    narrator "Jangan potong kalau simpulan itu perlu dibuka."
    narrator "Dia teringat ibu tua itu."
    narrator "Mulakan dengan nama dia."

    $ adv_step_movement_choices = []
    if adv_observed_pattern:
        $ adv_step_movement_choices.append((_("Tahan diri daripada lari"), "pattern"))
    $ adv_step_movement_choices.append((_("Suluh kain di bahagian kakinya"), "light"))
    $ adv_step_movement_choices.append((_("Angkat keris supaya dia berundur"), "keris"))
    $ adv_step_movement_choices.append((_("Lari ke belakang batu nisan"), "run"))

    $ adv_final_move = renpy.call_screen("adv_timed_choice", _("Dia mula melompat ke arah Aris. Apa Aris buat?"), adv_step_movement_choices, "freeze", 14)

    if adv_final_move == "pattern":
        stop music fadeout 0.7
        play rhythm audio.mus_rhythm_game fadein 0.2 volume adv_bg_rhythm_volume
        $ adv_still_result = renpy.call_screen("adv_stillness", _("Pocong tu datang lurus ke arah Aris. Kalau Aris bergerak, rentak dia pecah."), 4)
        stop rhythm fadeout 1.0
        play music audio.mus_final_confrontation fadein 1.0 volume adv_bg_music_volume
        if adv_still_result == "still":
            narrator "Aris tahan diri daripada lari."
            narrator "Duk. Jeda. Duk. Jeda."
            narrator "Betul kata Mak Ros: bila Aris tak panik, gerak pocong tu boleh dibaca."
            $ adv_final_pattern_used = True
            $ adv_understanding += 1
        else:
            narrator "Aris bergerak sedikit, cukup untuk pecahkan jeda itu."
            play sound audio.sfx_body_hit volume 1.25
            narrator "Pocong tu melompat terlalu dekat sebelum Aris sempat tarik nafas."
            $ adv_damage += 1
            $ adv_fear += 1

    elif adv_final_move == "light" and adv_known_burial_problem():
        play sound audio.sfx_flashlight_on volume 1.0
        narrator "Cahaya lampu jatuh tepat pada simpulan kain di kakinya."
        narrator "Bukan sekadar serangan. Ada sesuatu yang masih terikat."
        $ adv_understanding += 1

    elif adv_final_move == "light":
        play sound audio.sfx_flashlight_on volume 1.0
        narrator "Cahaya lampu terkena kain putih, tapi Aris belum faham apa yang patut dicari."
        narrator "Pocong tu menghentam tanah terlalu dekat."
        $ adv_fear += 1

    elif adv_final_move == "keris":
        play sound audio.sfx_keris_draw volume 1.0
        narrator "Aris mengangkat keris sebelum sempat menyebut nama arwah."
        narrator "Pocong tu menggigil, lebih marah daripada takut."
        $ adv_aggressive_prepare = True
        $ adv_final_force_used = True
        $ adv_pocong_anger += 1

    elif adv_final_move == "freeze" and adv_observed_pattern:
        narrator "Aris hampir terkaku."
        narrator "Tapi dia teringat satu benda: jangan lari."
        narrator "Dia diam dengan sengaja, dan pocong tu hilang rentak sekejap."
        $ adv_final_pattern_used = True
        $ adv_understanding += 1

    else:
        narrator "Aris bergerak tanpa membaca rentaknya."
        play sound audio.sfx_body_hit volume 1.25
        narrator "Bahu dia terkena hentaman kain dan tulang."
        $ adv_damage += 1
        $ adv_fear += 1

    $ adv_step_identity_choices = []
    if adv_known_identity():
        $ adv_step_identity_choices.append((_("Panggil nama Azlan"), "identity"))
    if adv_has_old_letter:
        $ adv_step_identity_choices.append((_("Baca surat Azlan"), "letter"))
    if adv_has_tasbih:
        $ adv_step_identity_choices.append((_("Baca doa"), "generic_pray"))
    $ adv_step_identity_choices.append((_("Paksa dia tunduk dengan keris"), "force"))
    $ adv_step_identity_choices.append((_("Diam dan tunggu dia berhenti sendiri"), "silent"))

    $ adv_final_identity = renpy.call_screen("adv_timed_choice", _("Dia berhenti dekat kubur, cukup dekat untuk mendengar suara Aris."), adv_step_identity_choices, "freeze", 14)

    if adv_final_identity == "identity":
        mc "Azlan."
        mc "Aku tahu kau abang Melur."
        mc "Ibu kau masih ingat. Dia tak pernah buang nama kau."
        mc "Orang kampung padam nama tu sebab mereka takut dengan salah sendiri."
        narrator "Kain putih tu tak lagi bergerak macam benda yang diburu."
        narrator "Ia bergerak seperti orang yang akhirnya didengar."
        $ adv_final_identity_used = True
        $ adv_understanding += 1

    elif adv_final_identity == "letter":
        play sound audio.sfx_paper_unfold volume 1.4
        narrator "Aris buka surat lama dengan tangan yang menggigil."
        mc "Azlan, kau mati bukan sebab bawa bala."
        mc "Kau mati sebab hentikan bomoh yang kampung ni takut nak sebut."
        mc "Anak kau masih ada. Dia berhak tahu bapanya bukan punca bala."
        mc "Surat kau tak patut tinggal dalam kotak sampai reput."
        narrator "Tanah kubur tu senyap, seolah-olah ayat itu sudah lama tunggu untuk dibaca."
        $ adv_final_identity_used = True
        $ adv_understanding += 1

    elif adv_final_identity == "generic_pray":
        narrator "Doa itu menahan takut dalam dada Aris, tapi doa itu tak memanggil dia dengan namanya."
        narrator "Pocong tu masih tak tahu sama ada Aris datang untuk faham, atau untuk hukum."
        $ adv_fear += 1

    elif adv_final_identity == "force":
        play sound audio.sfx_keris_draw volume 1.0
        narrator "Aris buka ruang dengan keris."
        narrator "Untuk sekejap, pocong tu tunduk."
        narrator "Tapi tunduk bukan sama dengan reda."
        $ adv_aggressive_prepare = True
        $ adv_final_force_used = True
        $ adv_pocong_anger += 1

    else:
        narrator "Aris tunggu terlalu lama."
        narrator "Tanpa nama, senyap itu cuma jadi satu lagi cara meninggalkan dia."
        $ adv_fear += 1

    narrator "Simpulan di kaki pocong itu menegang."
    narrator "Benang kafan dalam beg Aris terasa ringan, tapi maknanya makin berat."
    narrator "Ini bukan lagi soalan tentang cara menang."
    narrator "Ini soalan sama ada Aris cukup berani untuk dekat tanpa niat nak hukum."

    $ adv_step_release_choices = []
    if adv_ready_for_final_release():
        $ adv_step_release_choices.append((_("Buka simpulan perlahan-lahan"), "release"))
    if adv_has_kafan_thread and adv_has_tasbih:
        $ adv_step_release_choices.append((_("Tarik simpulan itu terus"), "partial_release"))
    if adv_known_burial_problem():
        $ adv_step_release_choices.append((_("Periksa simpulan di kaki dulu"), "inspect_knot"))
    if adv_has_salt:
        $ adv_step_release_choices.append((_("Tabur garam pada kain"), "salt"))
    $ adv_step_release_choices.append((_("Potong kain dengan keris"), "keris"))
    $ adv_step_release_choices.append((_("Berundur dari kubur"), "leave"))

    $ adv_final_release = renpy.call_screen("adv_timed_choice", _("Simpulan itu menegang. Pocong itu menggigil di depan Aris."), adv_step_release_choices, "freeze", 16)

    if adv_final_release == "release":
        play sound audio.sfx_knot_pull volume 1.0
        $ adv_final_release_used = True
        jump adv_release_ending

    elif adv_final_release == "inspect_knot" and adv_ready_for_final_release():
        narrator "Aris berhenti sekejap dan ingat semula semua petunjuk yang dia kumpul."
        narrator "Nama. Simpulan. Tasbih. Bukan senjata."
        $ adv_final_release_used = True
        jump adv_release_ending

    elif adv_final_release == "inspect_knot":
        narrator "Aris nampak simpulan itu, tapi dia belum cukup faham cara membukanya."
        narrator "Faham separuh jalan pun boleh melukakan."
        jump adv_ignorance_ending

    elif adv_final_release == "partial_release":
        play sound audio.sfx_knot_pull volume 1.0
        narrator "Aris cuba membuka simpulan itu."
        narrator "Tasbih ada di tangannya, tapi hati Aris masih belum pasti siapa yang sedang dia lepaskan."
        $ adv_fear += 1
        jump adv_ignorance_ending

    elif adv_final_release == "salt":
        narrator "Garam menyentuh kain kafan."
        narrator "Pocong tu tersentak, sakit, dan seluruh kawasan kubur macam menahan jerit."
        $ adv_final_force_used = True
        $ adv_pocong_anger += 1
        jump adv_ignorance_ending

    elif adv_final_release == "keris":
        play sound audio.sfx_keris_draw volume 1.0
        play cutting audio.sfx_cloth_cut volume 1.0
        narrator "Keris memotong kain, tapi bukan semua ikatan boleh diputuskan dengan bilah."
        $ adv_final_force_used = True
        $ adv_pocong_anger += 1
        if adv_damage >= 1 or adv_fear >= 3 or adv_pocong_anger >= 3:
            jump adv_death_ending
        jump adv_ignorance_ending

    elif adv_final_release == "freeze":
        narrator "Aris terkaku di depan simpulan terakhir."
        if adv_damage >= 1 or adv_fear >= 2 or adv_pocong_anger >= 3:
            jump adv_death_ending
        jump adv_abandon_ending

    else:
        jump adv_abandon_ending


label adv_release_ending:

    narrator "Aris turunkan keris."
    mc "Azlan."
    mc "Aku tahu siapa kau."
    mc "Melur ingat kau. Ibu kau ingat kau."
    mc "Anak kau masih ada, dan cerita sebenar kau tak patut tertanam lagi."
    mc "Dia hidup lama dengan cerita yang salah. Lepas malam ni, itu tak patut jadi warisan dia."
    mc "Malam ni, aku buka simpulan tu."

    show spr_pocong stilled at adv_left
    with dissolve

    narrator "Pocong tu tak tunduk."
    narrator "Ia berhenti."
    narrator "Beza itu kecil, tapi Aris rasa seluruh malam berubah."
    narrator "Aris melangkah satu tapak."
    narrator "Duk."
    narrator "Pocong tu menggigil."
    narrator "Aris berhenti, ikut jeda yang dia belajar dari Mak Ros."
    narrator "Bila kain putih tu diam semula, dia melangkah lagi."
    narrator "Tasbih bergerak perlahan di jari Aris."
    narrator "Setiap butir bantu dia jangan panik."
    narrator "Surat Azlan berada dalam buku nota, terbuka pada nama yang akhirnya disebut dengan betul."
    narrator "Benang kafan yang Aris jumpa di kubur diletakkan dekat simpulan lama tu."
    narrator "Bukan sebab benang itu sakti."
    narrator "Tapi sebab dari situlah masalahnya bermula."
    narrator "Simpulan lama tu melawan sekejap, kemudian longgar."
    narrator "Tanah di bawah kaki Aris terasa bernafas keluar."
    narrator "Kain putih tu akhirnya diam."
    stop music fadeout 2.0

    azlan "Terima kasih."
    azlan "Jaga anak saya."
    if adv_knows_child:
        mc "Saya akan pastikan anak kau dengar cerita yang betul."
        narrator "Janji itu terasa lebih berat daripada benang kafan di tangan Aris."
    narrator "Suara tu perlahan."
    narrator "Tapi untuk pertama kali malam itu, ia bukan jeritan."

    hide spr_pocong
    with dissolve

    narrator "Dia pergi perlahan-lahan, macam akhirnya dibenarkan pergi."
    if adv_hafiz_drives:
        narrator "Di luar kampung, Hafiz masih menunggu dengan enjin kereta yang hampir mati."
        hafiz "Kau berjaya?"
        mc "Dia yang berjaya pergi. Kita cuma kena pastikan cerita dia sampai."

    hide screen adv_inventory
    scene bg_ending_released
    with fade

    play music audio.mus_ending_positive fadein 1.0 volume adv_bg_music_volume noloop
    narrator "Melepaskan bukan sama dengan melupakan."
    narrator "Kadang-kadang, itulah cara paling jujur untuk menjaga orang yang masih hidup."
    play music audio.mus_credits fadein 1.0 volume adv_bg_music_volume noloop
    $ adv_report_result = renpy.call_screen("adv_ending_report", _("PENAMAT: DILEPASKAN"), _("Petunjuk yang Aris kumpul digunakan untuk kenal Azlan dan buka simpulan dengan niat yang betul."))
    call adv_positive_credits
    return


label adv_ignorance_ending:

    if adv_final_force_used or adv_aggressive_prepare:
        narrator "Aris pilih cara yang buat pocong tu tunduk."
    else:
        narrator "Aris cuba buat benda yang betul, tapi petunjuk di tangannya belum cukup."
    play sound audio.sfx_pocong_cry volume 1.45
    narrator "Pocong tu menjerit, tubuhnya melipat, lalu jatuh."
    narrator "Kampung jadi senyap."
    narrator "Tapi senyap tak semestinya tenang."
    if adv_knows_child:
        narrator "Aris teringat anak Azlan, dan rasa pahit itu datang lambat: ada kebenaran yang masih belum cukup berani dia bawa pulang."
    if adv_hafiz_drives:
        narrator "Hafiz jumpa Aris di tepi jalan sebelum subuh."
        hafiz "Dia dah lepas?"
        narrator "Aris tak mampu jawab dengan yakin."

    stop music fadeout 1.0
    hide screen adv_inventory
    scene bg_ending_ignorance
    with fade

    play music audio.mus_ending_positive fadein 1.0 volume adv_bg_music_volume noloop
    narrator "Tak semua yang menakutkan datang untuk membunuh."
    narrator "Bila takut dijadikan jawapan, kebenaran pun ikut tertanam."
    play music audio.mus_credits fadein 1.0 volume adv_bg_music_volume noloop
    $ adv_report_result = renpy.call_screen("adv_ending_report", _("PENAMAT: TIDAK FAHAM"), _("Aris selamat, tapi tak semua petunjuk digunakan dengan betul. Pocong tu dihentikan, bukan dilepaskan."))
    call adv_positive_credits
    return


label adv_positive_credits:

    scene black
    with fade

    $ renpy.call_screen("adv_credits_roll")
    stop music fadeout 2.0
    pause 2.0

    return


label adv_abandon_ending:

    narrator "Aris berundur dari kubur."
    narrator "Di belakangnya, bunyi melompat bermula semula."
    narrator "Duk."
    narrator "Duk."
    narrator "Duk."
    if adv_hafiz_drives:
        narrator "Hafiz buka pintu kereta tanpa banyak tanya, tapi matanya tetap mencari jawapan di muka Aris."
        hafiz "Kita tinggalkan macam ni?"
    if adv_knows_child:
        narrator "Di belakang keputusan itu, anak Azlan masih mewarisi cerita yang salah."

    stop music fadeout 1.0
    hide screen adv_inventory
    scene bg_ending_abandoned
    with fade

    play music audio.mus_ending_negative fadein 1.0 volume adv_bg_music_volume loop
    narrator "Benda yang ditinggalkan tak semestinya hilang."
    narrator "Kadang-kadang ia cuma tunggu orang lain tanggung akibatnya."
    play music audio.mus_credits fadein 1.0 volume adv_bg_music_volume noloop
    $ renpy.call_screen("adv_ending_report", _("PENAMAT: DITINGGALKAN"), _("Aris pilih hidup, tapi siasatan tak diselesaikan. Batu Layar masih menyimpan simpulan itu."))
    call adv_positive_credits
    return


label adv_death_ending:

    narrator "Untuk satu saat, Aris tak boleh bergerak."
    narrator "Itu saja yang Batu Layar perlukan."
    if adv_hafiz_drives:
        narrator "Telefon Hafiz menyala di luar kampung, memanggil nama Aris sampai baterinya makin lemah."
    if adv_knows_child:
        narrator "Anak Azlan masih hidup dengan cerita yang belum sempat dibetulkan."

    stop music fadeout 1.0
    hide screen adv_inventory
    scene bg_ending_buried
    with flash

    play music audio.mus_ending_negative fadein 1.0 volume adv_bg_music_volume loop
    narrator "Di tempat yang terlalu lama menyimpan luka, ragu yang sesaat pun boleh jadi terlalu mahal."
    narrator "Apa yang Aris tak berani faham akhirnya datang menuntut bayaran, senyap-senyap."
    play music audio.mus_credits fadein 1.0 volume adv_bg_music_volume noloop
    $ renpy.call_screen("adv_ending_report", _("PENAMAT: TERKUBUR BERSAMA"), _("Takut dan petunjuk yang diabaikan buat Aris hilang ruang untuk memilih."))
    call adv_positive_credits
    return
