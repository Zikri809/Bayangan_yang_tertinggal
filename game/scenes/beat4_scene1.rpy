label beat4_open:

    # BEAT 4 - THE FINAL CONFRONTATION
    # Bayangan yang Tertinggal - The Shadow Left Behind
    #
    # The MC fights prepared this time. What he learned in Beat 3 decides
    # whether this becomes a release or only a defeat.

    scene bg_village_path_night_2
    with fade

    # TODO audio: play amb_village_night on ambient channel fadein 2.0
    # TODO audio: play mus_pocong_theme fadein 3.0 volume 0.3

    show spr_mc focused at right
    with dissolve

    narrator "Ia datang dari arah yang telah dijangkakan."

    pause 1.5

    narrator "Kali ni dia bersedia."

    pause 1.0

    # TODO audio: play sfx_pocong_hop volume 0.6
    pause 1.5
    # TODO audio: play sfx_pocong_hop volume 0.7
    pause 1.2
    # TODO audio: play sfx_pocong_cry volume 0.4

    show spr_pocong present at left
    with dissolve

    pause 3.0

    if mother_told_truth:
        narrator "MC menatap arwah."
        pause 1.0
        narrator "Dia tahu siapa di dalam kain putih tu."
        pause 1.0
        narrator "Pengetahuan yang sangat berat."
        pause 1.5
        narrator "Dia menggenggam kerisnya."
        # TODO audio: play sfx_keris_draw
        narrator "Tangan dia stabil."
        pause 1.0
        narrator "Tetapi hatinya tidak."
    else:
        narrator "MC terus menatap erat arwah."
        pause 1.0
        narrator "Kehadiran dirinya adalah untuk ini."
        pause 1.0
        # TODO audio: play sfx_keris_draw
        narrator "Dia menggenggam kerisnya lebih erat."

    pause 2.0

    $ mc_damage = 0
    $ mc_condition = ""
    $ mc_condition_b4 = ""
    $ b4_pattern_read = False
    $ b4_advantage = False
    $ b4_close_range = False
    $ b4_r3_clean = False
    $ b4_pocong_weakened = False

    if arm_injured_severe:
        $ mc_damage = 2
        narrator "Lengannya cedera teruk masih belum sembuh."
        narrator "Dia tak ada pilihan lain selain teruskan."
        pause 1.0
    elif arm_injured:
        $ mc_damage = 1
        narrator "Lengannya cedera tapi masih boleh digunakan."
        pause 1.0

    if mc_shaken:
        narrator "Telinga dia masih berdengung dari kejadian semalam."
        pause 1.0

    jump beat4_r1

label beat4_r1:

    # TODO audio: play sfx_pocong_hop volume 0.8
    pause 0.8
    # TODO audio: play sfx_pocong_hop volume 0.9

    narrator "Ia bergerak."
    narrator "Lebih laju dari semalam."
    narrator "Atau mungkin ingatan tersebut salah."

    pause 1.5

    menu:
        "Tidak berganjak. Baca ayat perlindungan dulu.":
            jump b4_r1_protect

        "Serang terlebih dahulu - halang sebelum ia mendekat.":
            jump b4_r1_strike

        "Beranjak ke tepi. Tengok corak pergerakannya dulu.":
            jump b4_r1_observe

label b4_r1_protect:

    # TODO audio: play sfx_prayer_low volume 0.6

    narrator "Dia baca ayat perlindungan."
    narrator "Cepat. Tepat. Dah hafal lama dah."
    narrator "Ia melambat."
    narrator "Sikit. Tapi cukup."

    pause 1.0

    narrator "MC dapat ruang untuk bersedia."

    jump beat4_r2

label b4_r1_strike:

    narrator "MC meluru ke hadapan."

    # TODO audio: play sfx_keris_strike

    narrator "Keris berjaya menembus."
    narrator "Bukan macam kena benda fizikal."
    narrator "Lebih macam - ada yang bergetar."
    narrator "Ia berundur dua langkah."

    pause 1.0

    narrator "MC rasa lengannya."

    if arm_injured:
        narrator "Sakit."
        $ mc_damage += 1
        if mc_damage >= 3:
            jump beat4_death
    else:
        narrator "Tiada apa yang berlaku."

    jump beat4_r2

label b4_r1_observe:

    narrator "Dia beranjak ke tepi."
    narrator "Ia lalu."

    pause 1.0

    narrator "MC perhatikan cara ia bergerak."
    narrator "Cara ia mendarat. Cara ia berpusing."

    if b2_pak_zul_advice_used:
        narrator "Abang Zulkifli betul."
        narrator "Kalau diam, ia lambat sikit sebelum menyerang balik."
        narrator "Ada jeda. Kecil. Tapi ada."
        $ b4_pattern_read = True

    pause 1.0

    narrator "Maklumat yang berguna."

    jump beat4_r2

label beat4_r2:

    # TODO audio: play sfx_pocong_cry volume 0.6

    narrator "Ia meraung kuat."
    narrator "Bukan serangan. Belum lagi."
    narrator "Macam - sesuatu yang marah kerana diganggu."

    pause 1.5

    # TODO audio: play sfx_object_small_crash volume 0.7

    narrator "Sesuatu terbang dari tepi."

    menu:
        "Elak dengan bergolek ke tanah.":
            jump b4_r2_roll

        "Halang dengan lengan.":
            jump b4_r2_block

        "Maju - pendekkan jarak sebelum benda lain dilempar.":
            jump b4_r2_advance

label b4_r2_roll:

    narrator "Dia bergolek."
    narrator "Benda yang terbang tu lalu atas kepala dia."
    narrator "MC bangun semula. Berlutut di atas batu kerikil."

    pause 1.0

    if arm_injured:
        narrator "Lengan dia terhentak tanah semasa bergolek."
        narrator "Dia tahan bunyi yang nak terkeluar."
        $ mc_damage += 1
        if mc_damage >= 3:
            jump beat4_death

    jump beat4_r2b_check

label b4_r2_block:

    # TODO audio: play sfx_body_hit volume 0.7

    if arm_injured:
        narrator "Dia angkat lengan yang cedera."
        narrator "Benda tu menghantam tepat kat tempat yang sama."
        pause 1.0
        narrator "Bunyi yang tidak diingini terhasil dari lengannya."
        narrator "Dia jatuh berlutut."
        $ mc_damage += 1
        $ arm_injured_severe = True
        if mc_damage >= 3:
            jump beat4_death
    else:
        narrator "Hentaman kena lengan dia."
        narrator "Sakit. Tapi dia masih berdiri."
        $ mc_damage += 1
        $ arm_injured = True
        if mc_damage >= 3:
            jump beat4_death

    jump beat4_r2b_check

label b4_r2_advance:

    narrator "Dia maju ke depan."
    narrator "Tidaklah laju - terkawal."

    # TODO audio: play sfx_prayer_low volume 0.4

    narrator "Bacaan ayat setia di bibir dia."
    narrator "Pocong tu - ia berhenti melempar."
    narrator "Macam ada sesuatu yang menghalang."

    pause 1.5

    narrator "MC dapat masuk dalam jarak serangan."

    $ b4_close_range = True

    jump beat4_r2b_check

label beat4_r2b_check:

    if b2_pak_zul_advice_used and b4_pattern_read:
        jump beat4_r2b
    else:
        jump beat4_r3

label beat4_r2b:

    pause 1.0

    narrator "Dan kemudian MC nampak ia."
    narrator "Jeda macam yang Abang Zulkifli cakap."
    narrator "Kecil. Tapi ada."

    pause 1.5

    menu:
        "Gunakan jeda tu - serangan tepat ke titik kelemahan.":
            jump b4_r2b_use

        "Tahan. Jangan terburu-buru.":
            jump b4_r2b_hold

label b4_r2b_use:

    # TODO audio: play sfx_keris_strike

    narrator "Keris ditikam tepat."
    narrator "Pocong tu terhuyung-hayang."
    narrator "Lebih dari tadi."

    $ b4_advantage = True

    jump beat4_r3

label b4_r2b_hold:

    narrator "Dia menahan diri."
    narrator "Jeda berlalu."
    narrator "Okay. Lain kali."

    jump beat4_r3

label beat4_r3:

    stop music
    stop sound

    pause 1.0

    narrator "Senyap."

    pause 0.5

    narrator "Ia sedang bersiap sedia."

    pause 0.5

    if mc_condition == "deaf":
        narrator "MC tak dengar kesunyian tu."
        narrator "Tapi dia nampak ia berubah."
        narrator "Pergerakan badan tu. Cara ia menarik nafas."
        narrator "Dia tahu."
        pause 1.0

    if b4_advantage:
        narrator "Dia dah nampak corak ni."

    if b4_advantage:
        menu:
            "Tutup telinga. Tahan impak serangan.":
                jump b4_r3_cover

            "Baca ayat perlindungan kuat-kuat - potong serangan.":
                jump b4_r3_recite

            "Melompat terus ke arahnya sebelum ia lepaskan serangan.":
                jump b4_r3_lunge
    else:
        menu:
            "Tutup telinga. Tahan impak serangan.":
                jump b4_r3_cover

            "Baca ayat perlindungan kuat-kuat - potong serangan.":
                jump b4_r3_recite

            "Melompat terus ke arahnya sebelum ia lepaskan serangan.":
                jump b4_r3_lunge_failed

label b4_r3_cover:

    # TODO audio: play sfx_pocong_shriek volume 0.8

    scene black
    with flash

    # TODO audio: stop sound fadeout 0.3

    pause 1.0

    scene bg_village_path_night_2
    with fade

    show spr_mc focused at right
    show spr_pocong present at left
    with dissolve

    # TODO audio: play amb_village_night on ambient channel fadein 1.0

    narrator "Dia bertahan."
    narrator "Telinga dia - okay. Lebih kurang."

    if mc_damage >= 2:
        $ mc_condition = "deaf"
        show spr_mc deaf at right
        with dissolve
        narrator "Tapi ada sesuatu yang tidak betul."
        narrator "Dia sedar - dunia jadi senyap."
        narrator "Bukan senyap biasa. Senyap yang kekal."
    else:
        # TODO audio: play mus_pocong_theme fadein 2.0 volume 0.25
        pass

    jump beat4_r4

label b4_r3_recite:

    # TODO audio: play sfx_prayer_low volume 1.0

    narrator "Dia baca kuat-kuat."
    narrator "Suara dia lawan suara yang akan datang."

    pause 0.8

    # TODO audio: play sfx_pocong_shriek volume 0.5

    scene black
    with flash

    # TODO audio: stop sound fadeout 0.2

    pause 0.5

    scene bg_village_path_night_2
    with fade

    show spr_mc focused at right
    show spr_pocong present at left
    with dissolve

    # TODO audio: play amb_village_night on ambient channel fadein 1.0

    narrator "Ia kena. Tapi tak teruk."
    narrator "Bacaan itu - ia buat sesuatu."

    # TODO audio: play mus_pocong_theme fadein 2.0 volume 0.25

    $ b4_r3_clean = True

    jump beat4_r4

label b4_r3_lunge:

    narrator "MC meluru ke hadapannya."
    narrator "Sebelum ia sempat melepaskan."

    # TODO audio: play sfx_keris_strike

    narrator "Keris ditikam di tengah."
    narrator "Pocong tu terhuyung-hayang teruk."
    narrator "Jeritan keramat terganggu."

    pause 1.5

    narrator "MC hampir tak percaya ia berhasil."

    $ b4_close_range = True
    $ b4_r3_clean = True

    # TODO audio: play mus_pocong_theme fadein 2.0 volume 0.25

    jump beat4_r4

label b4_r3_lunge_failed:

    narrator "Dia cuba meluru."
    narrator "Tapi kali ini dia belum cukup membaca coraknya."

    $ mc_damage += 1
    if mc_damage >= 3:
        jump beat4_death

    jump b4_r3_cover

label beat4_r4:

    # TODO audio: play sfx_pocong_hop volume 0.8
    pause 0.8
    # TODO audio: play sfx_pocong_hop volume 0.9

    narrator "Ia masih ada disitu."

    pause 1.0

    narrator "Tapi ia berbeza sekarang."

    if mother_told_truth:
        narrator "Atau mungkin MC yang berbeza."
        narrator "Dia tengok ia dan nampak lebih dari sekadar benda putih yang menakutkan."
        pause 1.5
    else:
        narrator "Lebih tersepit. Lebih putus asa."
        pause 1.5

    narrator "Sesuatu yang berat bergerak di tepi."

    menu:
        "Halang dengan lengan.":
            jump b4_r4_block

        "Lompat ke tepi. Biar ia langgar dinding.":
            jump b4_r4_dodge

        "Gunakan keris - potong trajektori benda tu.":
            jump b4_r4_cut

label b4_r4_block:

    # TODO audio: play sfx_object_heavy_crash volume 1.0
    # TODO audio: play sfx_body_hit volume 0.8

    if arm_injured_severe:
        narrator "Dia angkat lengan dia."
        narrator "Untuk kali terakhir."
        pause 1.0
        narrator "Bunyi tulang yang patah adalah bunyi yang dia kenal."
        narrator "Dia pernah dengar ia pada orang lain."
        narrator "Sekarang giliran dia."
        pause 1.5
        $ mc_condition = "arm_lost"
        $ mc_damage += 1
        if mc_damage >= 3:
            jump beat4_death
        narrator "Lengan itu tidak berguna lagi."
        narrator "Dia masih berdiri."
    elif arm_injured:
        narrator "Hentaman kena lengan yang cedera."
        $ mc_damage += 1
        $ arm_injured_severe = True
        if mc_damage >= 3:
            jump beat4_death
        narrator "Sakit semakin teruk. Tapi boleh diguna lagi."
    else:
        narrator "Hentaman kena lengan dia."
        $ mc_damage += 1
        $ arm_injured = True
        if mc_damage >= 3:
            jump beat4_death
        narrator "Sakit tapi masih berdiri."

    jump beat4_r4_close

label b4_r4_dodge:

    narrator "Dia melompat ke tepi."

    # TODO audio: play sfx_object_heavy_crash volume 0.9

    narrator "Benda tu melanggar dinding rumah lama di tepi jalan."
    narrator "Dinding tu retak."

    pause 1.0

    narrator "Tapi MC selamat."

    jump beat4_r4_close

label b4_r4_cut:

    # TODO audio: play sfx_keris_strike

    narrator "Keris dia memotong udara."
    narrator "Benda tu - terbelah."

    pause 1.0

    narrator "MC tak pernah cuba buat tu sebelum ni."
    narrator "Dia pun tak tahu ia akan berhasil."

    pause 1.0

    narrator "Tapi berhasil."

    $ b4_pocong_weakened = True

    jump beat4_r4_close

label beat4_r4_close:

    if mc_damage >= 2 and not b4_pocong_weakened:
        # TODO audio: play sfx_object_heavy_crash volume 1.0
        # TODO audio: play sfx_body_hit volume 1.0

        narrator "Pocong tu serang balik."
        narrator "Dengan semua yang ia ada."

        pause 1.0

        narrator "MC kena dihempas ke dinding."

        scene black
        with flash

        pause 1.0

        scene bg_village_path_night_2
        with fade

        show spr_mc injured at right
        show spr_pocong present at left
        with dissolve

        narrator "Dia cuba bangun."

        menu:
            "Bangun. Teruskan.":
                jump b4_r4_struggle_up

            "Diam dulu. Kumpul kekuatan.":
                jump b4_r4_wait
    else:
        jump beat4_r4b_check

label b4_r4_struggle_up:

    narrator "Dia bangun."
    narrator "Lutut dia menggigil."
    narrator "Tapi dia tetap bangun."

    if mc_damage >= 2:
        narrator "Ada benda yang tak kena dengan kakinya."
        narrator "Dia boleh berdiri. Tapi tidak boleh lari."
        narrator "Tidak boleh kejar."
        $ mc_condition = "paralysed"

    jump beat4_r4b_check

label b4_r4_wait:

    narrator "Dia diam."
    narrator "Pocong tu mendekati."
    narrator "Perlahan."

    pause 1.5

    narrator "MC kumpul segala yang dia ada."
    narrator "Satu peluang lagi."

    $ mc_damage += 1
    if mc_damage >= 3:
        jump beat4_death

    jump beat4_r4b_check

label beat4_r4b_check:

    if mother_told_truth:
        jump beat4_r4b
    else:
        jump beat4_r5

label beat4_r4b:

    pause 2.0

    narrator "Pocong tu berhenti."
    narrator "Bukan sebab ia kalah."
    narrator "Tapi seperti ia - penat."

    pause 2.0

    narrator "MC tengok ia."
    narrator "Dia fikir tentang apa yang perempuan tua tu cakap."
    narrator "Tentang anak dia."
    narrator "Tentang dua puluh tahun lalu."

    pause 2.0

    menu:
        "Teruskan serangan. Habiskan sekarang.":
            jump b4_r4b_fight

        "Berhenti. Bercakap dengannya.":
            jump b4_r4b_speak

label b4_r4b_fight:

    narrator "MC teruskan."
    narrator "Ini kerja dia."

    jump beat4_r5

label b4_r4b_speak:

    # TODO audio: play sfx_prayer_low volume 0.3

    narrator "MC turunkan kerisnya."

    pause 2.0

    narrator "Pocong tu - ia masih ada. Masih dekat."
    narrator "Tapi ia tidak menyerang."

    pause 2.0

    mc "Aku tahu nama kau."

    pause 1.5

    mc "Aku tahu apa yang kau buat untuk kampung ni."

    pause 1.5

    mc "Aku tahu harga yang kau bayar."

    pause 2.0

    mc "Ibu kau - dia cerita."

    pause 3.0

    mc "Dua puluh tahun kau kat sini."

    pause 1.0

    mc "Bukan sebab kau jahat."

    pause 1.0

    mc "Sebab simpulan tu tak pernah dibuka."

    pause 2.0

    mc "Malam ni aku akan buka."

    pause 2.0

    show spr_pocong stilled at left
    with dissolve

    pause 3.0

    narrator "MC berjalan ke arahnya."
    narrator "Perlahan. Tanpa senjata."

    # TODO audio: play sfx_prayer_low volume 0.5

    narrator "Dia baca doa dengan perlahan."
    narrator "Bukan untuk lawan ia."
    narrator "Tetapi untuk teman ia."

    pause 2.0

    narrator "Dan kemudian dia buka simpulan tu."

    # TODO audio: play sfx_knot_untied

    pause 3.0

    stop music fadeout 3.0
    stop sound fadeout 2.0

    pause 2.0

    arwah "Terima kasih."

    pause 2.0

    arwah "Jaga anak saya."

    pause 3.0

    hide spr_pocong
    with dissolve

    # TODO audio: play sfx_arwah_final volume 0.3

    pause 4.0

    # TODO audio: play amb_village_night on ambient channel fadein 3.0

    narrator "Ia pergi."

    pause 2.0

    narrator "Bukan macam sesuatu yang dikalahkan."
    narrator "Macam sesuatu yang akhirnya boleh pergi."

    pause 3.0

    $ mc_condition_b4 = "knowledge_ending"

    jump beat4_close

label beat4_r5:

    # TODO audio: play sfx_pocong_cry volume 0.8

    narrator "Ia menjerit."

    if mother_told_truth:
        narrator "MC dengar sesuatu dalam jeritan tu yang dia tak boleh abaikan."
        narrator "Dia tetap teruskan."
    else:
        narrator "Bunyi yang menyakitkan telinga."

    pause 1.5

    menu:
        "Serangan penuh - habiskan.":
            jump b4_r5_full_attack

        "Baca doa penutup - halang ia dari lari lagi.":
            jump b4_r5_prayer

        "Gunakan semua yang ada - keris dan bacaan serentak.":
            jump b4_r5_combined

label b4_r5_full_attack:

    if mc_condition == "arm_lost":
        narrator "Dia serang dengan sebelah tangan."
        narrator "Lebih susah. Tapi dia buat jugak."
    elif mc_condition == "paralysed":
        narrator "Dia serang dari bawah."
        narrator "Dari lutut. Dari tanah."
        narrator "Ia kena."
    else:
        narrator "Dia bagi semua."

    # TODO audio: play sfx_keris_strike
    # TODO audio: play sfx_pocong_cry volume 1.0

    pause 1.0

    narrator "Pocong tu menjerit."
    narrator "Bukan bunyi serangan."
    narrator "Bunyi kesakitan."

    pause 1.5

    # TODO audio: play sfx_arwah_cry_pain volume 0.8

    pause 2.0

    narrator "Ia jatuh."

    pause 1.0

    narrator "Perlahan-lahan."

    pause 1.0

    narrator "Seperti sesuatu yang tak faham kenapa ia jatuh."

    pause 2.0

    $ mc_condition_b4 = "ignorance_ending"

    jump beat4_r5_close

label b4_r5_prayer:

    # TODO audio: play sfx_prayer_low volume 1.0

    narrator "Dia baca doa."
    narrator "Kuat. Jelas. Tanpa berhenti."

    pause 2.0

    narrator "Pocong tu - ia terhuyung-hayang."
    narrator "Macam ada dinding yang semakin menghimpit."

    pause 1.5

    # TODO audio: play sfx_arwah_cry_pain volume 0.6

    narrator "Ia menjerit sekali lagi."

    pause 1.0

    narrator "Kemudian diam."

    pause 2.0

    $ mc_condition_b4 = "ignorance_ending"

    jump beat4_r5_close

label b4_r5_combined:

    # TODO audio: play sfx_prayer_low volume 0.7
    # TODO audio: play sfx_keris_strike

    narrator "Keris dan bacaan - serentak."

    pause 1.0

    narrator "Ia bukan benda yang mudah dilakukan."
    narrator "Tapi MC dah lama buat kerja ni."

    pause 1.5

    narrator "Pocong tu - ia rebah."

    # TODO audio: play sfx_arwah_cry_pain volume 0.5

    pause 1.5

    narrator "Diam."

    pause 2.0

    $ mc_condition_b4 = "ignorance_ending"

    jump beat4_r5_close

label beat4_r5_close:

    stop music fadeout 2.0
    stop sound fadeout 1.5

    show spr_pocong present at left

    pause 3.0

    narrator "Ia terbaring di tanah."
    narrator "Masih."

    pause 2.0

    narrator "MC berdiri atasnya."

    pause 1.5

    if mother_told_truth:
        narrator "Dia tahu nama yang ada dalam kain putih tu."
        narrator "Dia tetap bunuh jugak."
        pause 1.5
        narrator "Bukan sebab dia tak kisah."
        narrator "Dia cuma - tak tahu cara lain."
    else:
        narrator "Dia tak tahu nama yang ada dalam kain putih tu."
        narrator "Dia tak tahu ceritanya."
        narrator "Dia hanya buat kerja dia."

    pause 2.0

    hide spr_pocong
    with dissolve

    # TODO audio: play amb_village_night on ambient channel fadein 3.0

    narrator "Ia pergi."

    pause 2.0

    narrator "Bukan macam sesuatu yang dilepaskan."
    narrator "Macam sesuatu yang dihentikan."

    pause 3.0

    jump beat4_close

label beat4_death:

    stop music
    stop ambient
    stop sound

    scene black
    with fade

    pause 2.0

    narrator "MC terjatuh."

    pause 1.5

    narrator "Dia cuba untuk bangun."

    pause 1.0

    narrator "Dia tidak berjaya."

    pause 2.0

    narrator "Kampung Nelayan Batu Layar."

    pause 1.0

    narrator "Pukul 2:47 pagi."

    pause 2.0

    return

label beat4_close:

    show spr_mc neutral at center
    with dissolve

    pause 3.0

    narrator "Kawasan kampung tu senyap."
    narrator "Bukan senyap yang pelik dari malam-malam sebelum ni."
    narrator "Senyap yang biasa."

    pause 2.0

    narrator "Ia dah pergi."

    pause 1.5

    if mc_condition_b4 == "knowledge_ending":
        narrator "MC duduk kat tanah."
        pause 1.0
        narrator "Dia pegang kerisnya."
        pause 1.0
        narrator "Dia fikir tentang apa yang Arwah cakap."
        pause 1.0
        narrator "Jaga anak saya."
        pause 2.0
        narrator "Dia akan cuba."
    elif mc_condition_b4 == "ignorance_ending":
        narrator "MC duduk kat tanah."
        pause 1.0
        narrator "Dia pegang kerisnya."
        pause 1.0
        narrator "Dia rasa sesuatu yang dia tak boleh definisikan."
        pause 1.5
        narrator "Macam ada sesuatu yang dia patut tahu."
        pause 1.0
        narrator "Tapi terlambat sekarang."

    pause 3.0

    jump beat5_open

label beat5_open:

    # Beat 5 is not implemented yet. This keeps the Beat 4 handoff playable.

    scene black
    with fade

    return
