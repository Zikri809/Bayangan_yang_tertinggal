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

    $ adv_step_movement_choices = []
    if adv_observed_pattern:
        $ adv_step_movement_choices.append(("Tahan diri daripada lari", "pattern"))
    $ adv_step_movement_choices.append(("Suluh kain di bahagian kakinya", "light"))
    $ adv_step_movement_choices.append(("Angkat keris supaya dia berundur", "keris"))
    $ adv_step_movement_choices.append(("Lari ke belakang batu nisan", "run"))

    $ adv_final_move = renpy.call_screen("adv_timed_choice", "Dia mula melompat ke arah MC. Apa MC buat?", adv_step_movement_choices, "freeze", 14)

    if adv_final_move == "pattern":
        narrator "MC tahan diri daripada lari."
        narrator "Duk. Jeda. Duk. Jeda."
        narrator "Betul kata Mak Ros: bila MC tak panik, gerak pocong itu boleh dibaca."
        $ adv_final_pattern_used = True
        $ adv_understanding += 1

    elif adv_final_move == "light" and adv_known_burial_problem():
        narrator "Cahaya lampu jatuh tepat pada simpulan kain di kakinya."
        narrator "Bukan sekadar serangan. Ada sesuatu yang masih terikat."
        $ adv_understanding += 1

    elif adv_final_move == "light":
        narrator "Cahaya lampu terkena kain putih, tapi MC belum faham apa yang patut dicari."
        narrator "Pocong itu menghentam tanah terlalu dekat."
        $ adv_fear += 1

    elif adv_final_move == "keris":
        narrator "MC mengangkat keris sebelum sempat menyebut nama arwah."
        narrator "Pocong itu menggigil, lebih marah daripada takut."
        $ adv_aggressive_prepare = True
        $ adv_final_force_used = True
        $ adv_pocong_anger += 1

    elif adv_final_move == "freeze" and adv_observed_pattern:
        narrator "MC hampir terkaku."
        narrator "Tapi dia teringat satu perkara: jangan lari."
        narrator "Dia diam dengan sengaja, dan pocong itu hilang rentak untuk sekejap."
        $ adv_final_pattern_used = True
        $ adv_understanding += 1

    else:
        narrator "MC bergerak tanpa membaca rentaknya."
        narrator "Bahu dia terkena hentaman kain dan tulang."
        $ adv_damage += 1
        $ adv_fear += 1

    $ adv_step_identity_choices = []
    if adv_known_identity():
        $ adv_step_identity_choices.append(("Panggil namanya", "identity"))
    if adv_has_old_letter:
        $ adv_step_identity_choices.append(("Baca isi surat lama", "letter"))
    if adv_has_tasbih:
        $ adv_step_identity_choices.append(("Baca doa", "generic_pray"))
    $ adv_step_identity_choices.append(("Paksa dia tunduk dengan keris", "force"))
    $ adv_step_identity_choices.append(("Diam dan tunggu dia berhenti sendiri", "silent"))

    $ adv_final_identity = renpy.call_screen("adv_timed_choice", "Dia berhenti dekat kubur, cukup dekat untuk mendengar suara MC.", adv_step_identity_choices, "freeze", 14)

    if adv_final_identity == "identity":
        mc "Aku tahu kau abang Melur."
        mc "Ibu kau masih ingat. Dia tak pernah buang nama kau."
        narrator "Kain putih itu tidak lagi bergerak seperti sesuatu yang diburu."
        narrator "Ia bergerak seperti orang yang akhirnya didengar."
        $ adv_final_identity_used = True
        $ adv_understanding += 1

    elif adv_final_identity == "letter":
        narrator "MC buka surat lama dengan tangan yang menggigil."
        mc "Kau mati bukan sebab bawa bala. Kau mati sebab cuba hentikan bala."
        narrator "Tanah kubur itu senyap, seolah-olah ayat itu sudah lama menunggu untuk dibaca."
        $ adv_final_identity_used = True
        $ adv_understanding += 1

    elif adv_final_identity == "generic_pray":
        narrator "Doa itu menahan takut dalam dada MC, tapi doa itu tak memanggil dia dengan namanya."
        narrator "Pocong itu masih tidak tahu sama ada MC datang untuk memahami atau menghukum."
        $ adv_fear += 1

    elif adv_final_identity == "force":
        narrator "MC buka ruang dengan keris."
        narrator "Untuk sekejap, pocong itu tunduk."
        narrator "Tapi tunduk bukan sama dengan reda."
        $ adv_aggressive_prepare = True
        $ adv_final_force_used = True
        $ adv_pocong_anger += 1

    else:
        narrator "MC tunggu terlalu lama."
        narrator "Tanpa nama, senyap itu cuma jadi satu lagi cara meninggalkan dia."
        $ adv_fear += 1

    $ adv_step_release_choices = []
    if adv_can_release() and adv_final_identity_used and adv_final_pattern_used:
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

    elif adv_final_release == "inspect_knot" and adv_can_release() and adv_final_identity_used and adv_final_pattern_used:
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
        narrator "Tasbih ada di tangannya, tapi hatinya masih belum pasti siapa yang sedang dia lepaskan."
        $ adv_fear += 1
        jump adv_ignorance_ending

    elif adv_final_release == "salt":
        narrator "Garam menyentuh kain kafan."
        narrator "Pocong itu tersentak, sakit, dan seluruh kawasan kubur seperti menahan jerit."
        $ adv_final_force_used = True
        $ adv_pocong_anger += 1
        jump adv_ignorance_ending

    elif adv_final_release == "keris":
        narrator "Keris memotong kain, tapi bukan semua ikatan boleh diputuskan dengan bilah."
        $ adv_final_force_used = True
        $ adv_pocong_anger += 1
        if adv_damage >= 1 or adv_fear >= 3:
            jump adv_death_ending
        jump adv_ignorance_ending

    elif adv_final_release == "freeze":
        narrator "MC terkaku di depan simpulan terakhir."
        if adv_damage >= 1 or adv_fear >= 2:
            jump adv_death_ending
        jump adv_abandon_ending

    else:
        jump adv_abandon_ending


label adv_release_ending:

    narrator "MC turunkan keris."
    mc "Aku tahu siapa kau."
    mc "Melur ingat kau. Ibu kau ingat kau."
    mc "Malam ni, aku buka simpulan tu."

    show spr_pocong stilled at adv_left
    with dissolve

    narrator "Tasbih bergerak perlahan di jari MC."
    narrator "Simpulan lama tu melawan sekejap, kemudian longgar."
    narrator "Kain putih itu akhirnya diam."

    arwah "Terima kasih."
    arwah "Jaga anak saya."

    hide spr_pocong
    with dissolve

    narrator "Dia pergi perlahan-lahan, macam akhirnya diberi izin untuk pergi."

    hide screen adv_inventory
    scene black
    with fade

    narrator "Melepaskan bukan sama dengan melupakan."
    narrator "Kadang-kadang, itulah cara paling jujur untuk menjaga orang yang masih hidup."
    $ renpy.call_screen("adv_ending_report", "PENAMAT: DILEPASKAN", "Petunjuk yang dikumpul digunakan untuk mengenali arwah dan membuka simpulan dengan niat yang betul.")
    return


label adv_ignorance_ending:

    if adv_final_force_used or adv_aggressive_prepare:
        narrator "MC pilih cara yang membuatkan pocong itu tunduk."
    else:
        narrator "MC cuba buat perkara yang betul, tapi petunjuk di tangannya belum cukup lengkap."
    narrator "Pocong tu menjerit, tubuhnya melipat, lalu jatuh."
    narrator "Kampung jadi senyap."
    narrator "Tapi senyap tak semestinya tenang."

    hide screen adv_inventory
    scene black
    with fade

    narrator "Tak semua yang menakutkan datang untuk membunuh."
    narrator "Bila takut dijadikan jawapan, kebenaran pun ikut tertanam."
    $ renpy.call_screen("adv_ending_report", "PENAMAT: TIDAK FAHAM", "MC selamat, tetapi tidak semua petunjuk digunakan dengan betul. Pocong itu dihentikan, bukan dilepaskan.")
    return


label adv_abandon_ending:

    narrator "MC berundur dari kubur."
    narrator "Di belakangnya, bunyi melompat bermula semula."
    narrator "Duk."
    narrator "Duk."
    narrator "Duk."

    hide screen adv_inventory
    scene black
    with fade

    narrator "Perkara yang ditinggalkan tidak semestinya hilang."
    narrator "Kadang-kadang ia cuma menunggu orang lain untuk memikul akibatnya."
    $ renpy.call_screen("adv_ending_report", "PENAMAT: DITINGGALKAN", "MC memilih hidup, tetapi siasatan tidak disambung dengan tindakan. Batu Layar masih menyimpan simpulan itu.")
    return


label adv_death_ending:

    narrator "Untuk satu saat, MC tak mampu bergerak."
    narrator "Itu saja yang Batu Layar perlukan."

    hide screen adv_inventory
    scene black
    with flash

    narrator "Di tempat yang terlalu lama menyimpan luka, ragu yang sesaat pun boleh jadi terlalu mahal."
    narrator "Apa yang tak berani difahami akhirnya menuntut bayaran dengan cara paling senyap."
    $ renpy.call_screen("adv_ending_report", "PENAMAT: TERKUBUR BERSAMA", "Ketakutan dan petunjuk yang tidak digunakan membuatkan MC hilang ruang untuk memilih.")
    return
