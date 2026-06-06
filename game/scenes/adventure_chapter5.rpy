label adv_chapter5:

    call adv_card_ch5

    $ adv_final_pattern_used = False
    $ adv_final_identity_used = False
    $ adv_final_release_used = False
    $ adv_final_force_used = False

    scene bg_adv_final_grave
    with fade

    show spr_mc focused at adv_right
    show spr_pocong present at adv_left
    with dissolve

    narrator "Pukul 2:47 pagi, MC sampai di kubur itu."
    narrator "Pocong tu menunggu di sana."
    narrator "Kain di kakinya tertarik ketat, seolah-olah tanah sendiri belum mahu melepaskan dia."
    narrator "Kali ni, buku nota bukan sekadar catatan."
    narrator "Setiap petunjuk mungkin jadi cara untuk terus hidup."
    narrator "MC teringat suara Mak Ros."
    narrator "Jangan lari kalau mahu baca rentaknya."
    narrator "Dia teringat tanah kubur yang tak rata."
    narrator "Jangan potong kalau simpulan itu perlu dibuka."
    narrator "Dia teringat ibu tua itu."
    narrator "Mulakan dengan nama dia."

    $ adv_step_movement_choices = []
    if adv_observed_pattern:
        $ adv_step_movement_choices.append(("Tahan diri daripada lari", "pattern"))
    $ adv_step_movement_choices.append(("Suluh kain di bahagian kakinya", "light"))
    $ adv_step_movement_choices.append(("Angkat keris supaya dia berundur", "keris"))
    $ adv_step_movement_choices.append(("Lari ke belakang batu nisan", "run"))

    $ adv_final_move = renpy.call_screen("adv_timed_choice", "Dia mula melompat ke arah MC. Apa MC buat?", adv_step_movement_choices, "freeze", 14)

    if adv_final_move == "pattern":
        $ adv_still_result = renpy.call_screen("adv_stillness", "Pocong tu datang lurus ke arah MC. Kalau MC bergerak, rentak dia pecah.", 4)
        if adv_still_result == "still":
            narrator "MC tahan diri daripada lari."
            narrator "Duk. Jeda. Duk. Jeda."
            narrator "Betul kata Mak Ros: bila MC tak panik, gerak pocong tu boleh dibaca."
            $ adv_final_pattern_used = True
            $ adv_understanding += 1
        else:
            narrator "MC bergerak sedikit, cukup untuk pecahkan jeda itu."
            narrator "Pocong tu melompat terlalu dekat sebelum MC sempat tarik nafas."
            $ adv_damage += 1
            $ adv_fear += 1

    elif adv_final_move == "light" and adv_known_burial_problem():
        narrator "Cahaya lampu jatuh tepat pada simpulan kain di kakinya."
        narrator "Bukan sekadar serangan. Ada sesuatu yang masih terikat."
        $ adv_understanding += 1

    elif adv_final_move == "light":
        narrator "Cahaya lampu terkena kain putih, tapi MC belum faham apa yang patut dicari."
        narrator "Pocong tu menghentam tanah terlalu dekat."
        $ adv_fear += 1

    elif adv_final_move == "keris":
        narrator "MC mengangkat keris sebelum sempat menyebut nama arwah."
        narrator "Pocong tu menggigil, lebih marah daripada takut."
        $ adv_aggressive_prepare = True
        $ adv_final_force_used = True
        $ adv_pocong_anger += 1

    elif adv_final_move == "freeze" and adv_observed_pattern:
        narrator "MC hampir terkaku."
        narrator "Tapi dia teringat satu benda: jangan lari."
        narrator "Dia diam dengan sengaja, dan pocong tu hilang rentak sekejap."
        $ adv_final_pattern_used = True
        $ adv_understanding += 1

    else:
        narrator "MC bergerak tanpa membaca rentaknya."
        narrator "Bahu dia terkena hentaman kain dan tulang."
        $ adv_damage += 1
        $ adv_fear += 1

    $ adv_step_identity_choices = []
    if adv_known_identity():
        $ adv_step_identity_choices.append(("Panggil nama Azlan", "identity"))
    if adv_has_old_letter:
        $ adv_step_identity_choices.append(("Baca surat Azlan", "letter"))
    if adv_has_tasbih:
        $ adv_step_identity_choices.append(("Baca doa", "generic_pray"))
    $ adv_step_identity_choices.append(("Paksa dia tunduk dengan keris", "force"))
    $ adv_step_identity_choices.append(("Diam dan tunggu dia berhenti sendiri", "silent"))

    $ adv_final_identity = renpy.call_screen("adv_timed_choice", "Dia berhenti dekat kubur, cukup dekat untuk mendengar suara MC.", adv_step_identity_choices, "freeze", 14)

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
        narrator "MC buka surat lama dengan tangan yang menggigil."
        mc "Azlan, kau mati bukan sebab bawa bala."
        mc "Kau mati sebab hentikan bomoh yang kampung ni takut nak sebut."
        mc "Anak kau masih ada. Dia berhak tahu bapanya bukan punca bala."
        mc "Surat kau tak patut tinggal dalam kotak sampai reput."
        narrator "Tanah kubur tu senyap, seolah-olah ayat itu sudah lama tunggu untuk dibaca."
        $ adv_final_identity_used = True
        $ adv_understanding += 1

    elif adv_final_identity == "generic_pray":
        narrator "Doa itu menahan takut dalam dada MC, tapi doa itu tak memanggil dia dengan namanya."
        narrator "Pocong tu masih tak tahu sama ada MC datang untuk faham, atau untuk hukum."
        $ adv_fear += 1

    elif adv_final_identity == "force":
        narrator "MC buka ruang dengan keris."
        narrator "Untuk sekejap, pocong tu tunduk."
        narrator "Tapi tunduk bukan sama dengan reda."
        $ adv_aggressive_prepare = True
        $ adv_final_force_used = True
        $ adv_pocong_anger += 1

    else:
        narrator "MC tunggu terlalu lama."
        narrator "Tanpa nama, senyap itu cuma jadi satu lagi cara meninggalkan dia."
        $ adv_fear += 1

    narrator "Simpulan di kaki pocong itu menegang."
    narrator "Benang kafan dalam beg MC terasa ringan, tapi maknanya makin berat."
    narrator "Ini bukan lagi soalan tentang cara menang."
    narrator "Ini soalan sama ada MC cukup berani untuk dekat tanpa niat nak hukum."

    $ adv_step_release_choices = []
    if adv_ready_for_final_release():
        $ adv_step_release_choices.append(("Buka simpulan perlahan-lahan", "release"))
    if adv_has_kafan_thread and adv_has_tasbih:
        $ adv_step_release_choices.append(("Tarik simpulan itu terus", "partial_release"))
    if adv_known_burial_problem():
        $ adv_step_release_choices.append(("Periksa simpulan di kaki dulu", "inspect_knot"))
    if adv_has_salt:
        $ adv_step_release_choices.append(("Tabur garam pada kain", "salt"))
    $ adv_step_release_choices.append(("Potong kain dengan keris", "keris"))
    $ adv_step_release_choices.append(("Berundur dari kubur", "leave"))

    $ adv_final_release = renpy.call_screen("adv_timed_choice", "Simpulan itu menegang. Pocong itu menggigil di depan MC.", adv_step_release_choices, "freeze", 16)

    if adv_final_release == "release":
        $ adv_final_release_used = True
        jump adv_release_ending

    elif adv_final_release == "inspect_knot" and adv_ready_for_final_release():
        narrator "MC berhenti sekejap dan ingat semula semua petunjuk yang dia kumpul."
        narrator "Nama. Simpulan. Tasbih. Bukan senjata."
        $ adv_final_release_used = True
        jump adv_release_ending

    elif adv_final_release == "inspect_knot":
        narrator "MC nampak simpulan itu, tapi dia belum cukup faham cara membukanya."
        narrator "Faham separuh jalan pun boleh melukakan."
        jump adv_ignorance_ending

    elif adv_final_release == "partial_release":
        narrator "MC cuba membuka simpulan itu."
        narrator "Tasbih ada di tangannya, tapi hati MC masih belum pasti siapa yang sedang dia lepaskan."
        $ adv_fear += 1
        jump adv_ignorance_ending

    elif adv_final_release == "salt":
        narrator "Garam menyentuh kain kafan."
        narrator "Pocong tu tersentak, sakit, dan seluruh kawasan kubur macam menahan jerit."
        $ adv_final_force_used = True
        $ adv_pocong_anger += 1
        jump adv_ignorance_ending

    elif adv_final_release == "keris":
        narrator "Keris memotong kain, tapi bukan semua ikatan boleh diputuskan dengan bilah."
        $ adv_final_force_used = True
        $ adv_pocong_anger += 1
        if adv_damage >= 1 or adv_fear >= 3 or adv_pocong_anger >= 3:
            jump adv_death_ending
        jump adv_ignorance_ending

    elif adv_final_release == "freeze":
        narrator "MC terkaku di depan simpulan terakhir."
        if adv_damage >= 1 or adv_fear >= 2 or adv_pocong_anger >= 3:
            jump adv_death_ending
        jump adv_abandon_ending

    else:
        jump adv_abandon_ending


label adv_release_ending:

    narrator "MC turunkan keris."
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
    narrator "Beza itu kecil, tapi MC rasa seluruh malam berubah."
    narrator "MC melangkah satu tapak."
    narrator "Duk."
    narrator "Pocong tu menggigil."
    narrator "MC berhenti, ikut jeda yang dia belajar dari Mak Ros."
    narrator "Bila kain putih tu diam semula, dia melangkah lagi."
    narrator "Tasbih bergerak perlahan di jari MC."
    narrator "Setiap butir bantu dia jangan panik."
    narrator "Surat Azlan berada dalam buku nota, terbuka pada nama yang akhirnya disebut dengan betul."
    narrator "Benang kafan yang MC jumpa di kubur diletakkan dekat simpulan lama tu."
    narrator "Bukan sebab benang itu sakti."
    narrator "Tapi sebab dari situlah masalahnya bermula."
    narrator "Simpulan lama tu melawan sekejap, kemudian longgar."
    narrator "Tanah di bawah kaki MC terasa bernafas keluar."
    narrator "Kain putih tu akhirnya diam."

    azlan "Terima kasih."
    azlan "Jaga anak saya."
    if adv_knows_child:
        mc "Saya akan pastikan anak kau dengar cerita yang betul."
        narrator "Janji itu terasa lebih berat daripada benang kafan di tangan MC."
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

    narrator "Melepaskan bukan sama dengan melupakan."
    narrator "Kadang-kadang, itulah cara paling jujur untuk menjaga orang yang masih hidup."
    $ renpy.call_screen("adv_ending_report", "PENAMAT: DILEPASKAN", "Petunjuk yang MC kumpul digunakan untuk kenal Azlan dan buka simpulan dengan niat yang betul.")
    return


label adv_ignorance_ending:

    if adv_final_force_used or adv_aggressive_prepare:
        narrator "MC pilih cara yang buat pocong tu tunduk."
    else:
        narrator "MC cuba buat benda yang betul, tapi petunjuk di tangannya belum cukup."
    narrator "Pocong tu menjerit, tubuhnya melipat, lalu jatuh."
    narrator "Kampung jadi senyap."
    narrator "Tapi senyap tak semestinya tenang."
    if adv_knows_child:
        narrator "MC teringat anak Azlan, dan rasa pahit itu datang lambat: ada kebenaran yang masih belum cukup berani dia bawa pulang."
    if adv_hafiz_drives:
        narrator "Hafiz jumpa MC di tepi jalan sebelum subuh."
        hafiz "Dia dah lepas?"
        narrator "MC tak mampu jawab dengan yakin."

    hide screen adv_inventory
    scene bg_ending_ignorance
    with fade

    narrator "Tak semua yang menakutkan datang untuk membunuh."
    narrator "Bila takut dijadikan jawapan, kebenaran pun ikut tertanam."
    $ renpy.call_screen("adv_ending_report", "PENAMAT: TIDAK FAHAM", "MC selamat, tapi tak semua petunjuk digunakan dengan betul. Pocong tu dihentikan, bukan dilepaskan.")
    return


label adv_abandon_ending:

    narrator "MC berundur dari kubur."
    narrator "Di belakangnya, bunyi melompat bermula semula."
    narrator "Duk."
    narrator "Duk."
    narrator "Duk."
    if adv_hafiz_drives:
        narrator "Hafiz buka pintu kereta tanpa banyak tanya, tapi matanya tetap mencari jawapan di muka MC."
        hafiz "Kita tinggalkan macam ni?"
    if adv_knows_child:
        narrator "Di belakang keputusan itu, anak Azlan masih mewarisi cerita yang salah."

    hide screen adv_inventory
    scene bg_ending_abandoned
    with fade

    narrator "Benda yang ditinggalkan tak semestinya hilang."
    narrator "Kadang-kadang ia cuma tunggu orang lain tanggung akibatnya."
    $ renpy.call_screen("adv_ending_report", "PENAMAT: DITINGGALKAN", "MC pilih hidup, tapi siasatan tak diselesaikan. Batu Layar masih menyimpan simpulan itu.")
    return


label adv_death_ending:

    narrator "Untuk satu saat, MC tak boleh bergerak."
    narrator "Itu saja yang Batu Layar perlukan."
    if adv_hafiz_drives:
        narrator "Telefon Hafiz menyala di luar kampung, memanggil nama MC sampai baterinya makin lemah."
    if adv_knows_child:
        narrator "Anak Azlan masih hidup dengan cerita yang belum sempat dibetulkan."

    hide screen adv_inventory
    scene bg_ending_buried
    with flash

    narrator "Di tempat yang terlalu lama menyimpan luka, ragu yang sesaat pun boleh jadi terlalu mahal."
    narrator "Apa yang MC tak berani faham akhirnya datang menuntut bayaran, senyap-senyap."
    $ renpy.call_screen("adv_ending_report", "PENAMAT: TERKUBUR BERSAMA", "Takut dan petunjuk yang diabaikan buat MC hilang ruang untuk memilih.")
    return
