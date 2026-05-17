label beat2_scene1:

    # BEAT 2 - SCENE 1: The First Confrontation
    # Bayangan yang Tertinggal - The Shadow Left Behind
    #
    # The MC reaches Kampung Nelayan Batu Layar unprepared. This scene plays
    # regardless of whether he travelled alone or Hafiz drove him.
    #
    # SCENE ASSETS NEEDED
    #
    # Backgrounds:
    # TODO art: bg_car_interior_night
    # TODO art: bg_village_road_night
    # TODO art: bg_village_path_dawn
    #
    # Sprites:
    # TODO art: spr_mc alert, shaken, injured
    # TODO art: spr_hafiz concerned
    # TODO art: spr_villager_1 terrified, shocked
    #
    # Audio:
    # TODO audio: amb_car_idle
    # TODO audio: amb_village_night
    # TODO audio: amb_village_dawn
    # TODO audio: mus_pocong_theme
    # TODO audio: sfx_car_door_open
    # TODO audio: sfx_distant_scream
    # TODO audio: sfx_pocong_hop
    # TODO audio: sfx_pocong_cry
    # TODO audio: sfx_pocong_shriek
    # TODO audio: sfx_object_small_crash
    # TODO audio: sfx_object_heavy_crash
    # TODO audio: sfx_body_hit
    # TODO audio: sfx_car_engine_start

    # THE ARRIVAL

    scene bg_car_interior_night
    with fade

    # TODO audio: play amb_car_idle on ambient channel fadein 2.0

    show spr_mc neutral at right
    with dissolve

    if hafiz_drives:
        show spr_hafiz neutral at left
        with dissolve

    pause 2.0

    narrator "Kampung Nelayan Batu Layar."

    pause 1.0

    narrator "Pukul 11 lebih malam."
    narrator "Gelap."

    pause 1.0

    narrator "Bukan gelap sebab tak ada lampu."
    narrator "Gelap macam tempat yang dah biasa dengan gelap."

    pause 1.5

    mc "Senyap."

    if hafiz_drives:
        hafiz "Ha."

        pause 1.0

        hafiz "Nak masuk terus?"
        mc "Jap. Rehat dulu."
        hafiz "Ha."

        pause 2.0

        hafiz "Aku nak pi toilet jap. Nampak tadi ada surau tepi jalan."
        mc "Ha. Pergi."

        hide spr_hafiz
        with dissolve

    else:
        narrator "Dia rehat dulu sebelum masuk."

        pause 2.0

        narrator "Jap lagi."

    pause 3.0

    narrator "Dia rasa penat perjalanan dalam tulang-tulangnya."
    narrator "Jap lagi baru masuk."
    narrator "Jap lagi."

    pause 2.0

    # THE SOUND

    # TODO audio: stop ambient fadeout 2.0

    pause 1.0

    narrator "Tiba-tiba senyap."

    show spr_mc alert at right
    with dissolve

    # TODO audio: play sfx_distant_scream volume 0.8

    pause 0.5

    narrator "Seseorang menjerit."

    pause 1.0

    # TODO audio: play sfx_distant_scream volume 1.0

    narrator "Lebih dari seorang."

    pause 0.5

    narrator "Dia buka pintu kereta."

    # TODO audio: play sfx_car_door_open volume 0.6

    narrator "Dia tak ambil beg."
    narrator "Dia tak fikir pasal tu."
    narrator "Dia lari ke arah suara tu."

    # INTO THE VILLAGE

    scene bg_village_path_night
    with flash

    # TODO audio: play amb_village_night on ambient channel fadein 1.0

    show spr_mc alert at right
    with dissolve

    # TODO audio: play mus_pocong_theme fadein 2.0 volume 0.25

    narrator "Dia nampak orang pertama."

    show spr_villager_1 terrified at left
    with dissolve

    villager_1 "Ada... ada... kat sana..."

    mc "Berapa orang kat depan?"

    villager_1 "Mak Cik Ros... dia ada kat depan..."

    narrator "MC terus lari."

    hide spr_villager_1
    with dissolve

    # THE POCONG IS ALREADY THERE
    # Do not show the Pocong sprite yet. The player sees its effects only.

    # TODO audio: play sfx_pocong_hop volume 0.8
    pause 1.0
    # TODO audio: play sfx_pocong_hop volume 0.9
    pause 0.8
    # TODO audio: play sfx_pocong_cry volume 0.6

    narrator "Dia dengar ia sebelum dia nampak ia."
    narrator "Bunyi tu."
    narrator "Macam tangisan. Macam sesuatu yang menangis dalam kain."
    narrator "Dan bunyi lompatan tu."
    narrator "Perlahan. Kuat. Dekat."

    pause 1.5

    mc "Hei!"

    narrator "Ia pusing."
    narrator "Ke arah dia."

    pause 1.0

    # ROUND 1 - POCONG APPROACHES

    # TODO audio: play sfx_pocong_hop volume 0.9
    pause 1.0
    # TODO audio: play sfx_pocong_hop volume 1.0
    pause 0.8

    narrator "Ia menghampiri."
    narrator "Perlahan-perlahan. Tapi MC tahu - bagi pocong, perlahan dah cukup laju."

    menu:
        "Jerit kuat untuk bagi amaran kat orang kampung lain.":
            jump b2_r1_shout

        "Ambil apa-apa yang ada di tepi jalan - kayu, batu.":
            jump b2_r1_grab

        "Berdiri teguh. Jangan gerak. Tengok dulu.":
            jump b2_r1_hold

label b2_r1_shout:

    mc "Semua orang masuk rumah! Kunci pintu! Jangan keluar!"

    narrator "Mak Cik Ros berjaya masuk ke dalam rumah jiran."
    narrator "Satu nyawa selamat."

    $ villager_2_safe = True

    # TODO audio: play sfx_pocong_hop volume 1.0
    pause 0.6
    # TODO audio: play sfx_pocong_hop volume 1.0

    narrator "Tapi sekarang ia datang terus ke arah MC."
    narrator "Tiada lagi orang lain antara mereka."

    jump b2_round2

label b2_r1_grab:

    narrator "Dia tengok tepi. Sepotong kayu lama. Patah."
    narrator "Bukan senjata. Tapi ada dalam tangan lebih baik dari kosong."

    mc "Okay."

    narrator "Dia hayun kayu tu."
    narrator "Ia lalu terus melalui - macam pukul angin."
    narrator "Tapi ia buat ia berhenti sekejap."

    $ b2_tried_wood = True
    $ villager_2_safe = True

    narrator "Mak Cik Ros merangkak masuk ke dalam pagar jiran."

    jump b2_round2

label b2_r1_hold:

    narrator "Dia berdiri diam."
    narrator "Abang Zul cakap tadi - jangan lari."
    narrator "Dia ingat tu."

    pause 1.5

    narrator "Ia melambatkan langkah."
    narrator "Masih datang. Tapi perlahan."

    $ b2_pak_zul_advice_used = True
    $ villager_2_safe = True

    narrator "Orang kampung yang lain tarik Mak Cik Ros ke dalam rumah."

    jump b2_round2

label b2_round2:

    # The Pocong is close now. The MC has no weapon.
    stop music
    stop ambient
    stop sound

    pause 1.0

    narrator "Senyap."

    pause 0.5

    narrator "Dan dia rasa - sesuatu akan berlaku."

    pause 0.5

    menu:
        "Tutup telinga.":
            jump b2_shriek_cover

        "Tahan diri. Jangan tunduk.":
            jump b2_shriek_take

label b2_shriek_cover:

    # TODO audio: play sfx_pocong_shriek volume 1.0

    scene black
    with flash

    # TODO audio: stop sound fadeout 0.3

    pause 0.8

    # TODO audio: play sfx_object_heavy_crash volume 1.0

    narrator "Sesuatu yang berat hentam badannya dari tepi."
    narrator "Dia tak nampak dari mana."
    narrator "Ia hanya rasa."

    scene bg_village_path_night
    with fade

    show spr_mc injured at right
    with dissolve

    # TODO audio: play amb_village_night on ambient channel fadein 1.5

    narrator "MC terpelanting. Jatuh ke tanah."
    narrator "Bahu dia. Rusuk dia."
    narrator "Ada yang tidak betul."

    $ shriek_covered = True
    $ arm_injured = True

    jump b2_round3

label b2_shriek_take:

    # TODO audio: play sfx_pocong_shriek volume 1.0

    scene black
    with flash

    # TODO audio: stop sound fadeout 0.3

    pause 1.5

    scene bg_village_path_night
    with fade

    show spr_mc injured at right
    with dissolve

    # TODO audio: play amb_village_night on ambient channel fadein 2.0

    narrator "MC jatuh ke lutut."
    narrator "Telinga dia berbunyi."
    narrator "Bukan bunyi biasa - bunyi yang duduk dalam kepala"
    narrator "dan tak mahu pergi."

    pause 1.0

    narrator "Dia nampak tanah. Dia nampak tangan dia sendiri."
    narrator "Dia tak nampak yang lain-lain dengan betul."

    $ shriek_covered = False
    $ mc_shaken = True

    jump b2_round3

label b2_round3:

    # TODO audio: play sfx_pocong_cry volume 0.5

    narrator "Dan kemudian ia buat sesuatu yang lain."
    narrator "MC nampak sesuatu bergerak."
    narrator "Berat. Gelap. Dari tepi."

    menu:
        "Halang dengan tangan.":
            jump b2_block_arm

        "Gerak tepi. Biar ia lalu.":
            jump b2_roll_aside

label b2_block_arm:

    # TODO audio: play sfx_object_heavy_crash volume 1.0

    show spr_mc injured at right
    with flash

    narrator "Dia angkat tangan."
    narrator "Ia hentam."
    narrator "Bunyi yang salah keluar dari lengan dia."

    pause 1.0

    narrator "Dia tahu bunyi tu."
    narrator "Dia pernah dengar ia sebelum ni - pada orang lain."

    pause 1.0

    if arm_injured:
        narrator "Lengan yang sama."
        narrator "Dua kali dalam satu malam."
        $ arm_injured_severe = True
    else:
        $ arm_injured = True

    # TODO audio: play sfx_object_small_crash volume 0.8
    # TODO audio: play sfx_body_hit volume 0.7

    narrator "Seorang lelaki - orang kampung yang MC tak kenal -"
    narrator "berlari keluar nak tolong."
    narrator "Ia kena dia."
    narrator "Ia yang patut kena MC."

    pause 1.5

    $ villager_1_hurt = True

    jump b2_round4

label b2_roll_aside:

    narrator "Dia tolak dirinya ke tepi."
    narrator "Benda tu lalu. Terhantuk ke dinding rumah orang."

    # TODO audio: play sfx_object_heavy_crash volume 0.8

    narrator "Dinding tu retak."

    pause 0.5

    narrator "MC bergolek ke atas batu tajam."
    narrator "Tidak serius. Tapi sakit."

    jump b2_round4

label b2_round4:

    # TODO audio: stop sound fadeout 1.0
    # TODO audio: play mus_pocong_theme fadein 2.0 volume 0.15

    narrator "Ia berhenti."

    pause 1.5

    narrator "Masih ada. Tapi tak bergerak."

    pause 1.0

    narrator "Dan kemudian - perlahan-lahan - ia berundur."

    # TODO audio: play sfx_pocong_hop volume 0.5
    pause 2.0
    # TODO audio: play sfx_pocong_hop volume 0.3
    pause 2.5
    # TODO audio: play sfx_pocong_hop volume 0.15
    pause 3.0

    # TODO audio: stop music fadeout 3.0
    # TODO audio: stop sound fadeout 2.0

    pause 2.0

    narrator "Ia pergi."
    narrator "Entah ke mana."

    pause 1.5

    $ fc_stood_ground = True

    narrator "Dia nampak sesuatu malam tu."
    narrator "Sebelum ia pergi."
    narrator "Bukan sesuatu yang boleh dia ceritakan dengan kata-kata."
    narrator "Tapi dia simpan."

    pause 2.0

    jump b2_aftermath

label b2_aftermath:

    scene bg_village_path_night
    with dissolve

    show spr_mc injured at center
    with dissolve

    # TODO audio: play amb_village_night on ambient channel fadein 2.0

    narrator "MC duduk di atas tanah."
    narrator "Dia kira."
    narrator "Dua orang cedera. Mungkin lebih."
    narrator "Satu yang hampir mati."
    narrator "Dia masuk tanpa senjata."
    narrator "Itu kesilapan dia."

    pause 2.0

    show spr_villager_1 shocked at left
    with dissolve

    villager_1 "Encik ni siapa?"

    mc "Orang luar. Baru sampai."

    villager_1 "..."
    villager_1 "Encik okay?"

    mc "Ha."

    hide spr_villager_1
    with dissolve

    pause 2.0

    if hafiz_drives:
        # TODO audio: play sfx_car_door_open volume 0.5
        show spr_hafiz serious at left
        with dissolve

        hafiz "Apa jadi?"

        show spr_mc shaken at right
        with dissolve

        mc "Ia dah ada dekat sini."

        pause 1.0

        hafiz "Kau okay?"
        mc "Masih boleh jalan."

        narrator "Hafiz bantu dia bangun."
        narrator "Dia tak tanya apa-apa lagi."
        narrator "Ada masa untuk tu."

        pause 2.0

        jump b2_dawn_with_hafiz

    else:
        show spr_mc shaken at center
        with dissolve

        narrator "Dia berseorangan."

        pause 1.0

        narrator "Orang kampung tu menyembunyikan diri."
        narrator "Dia faham tu."

        pause 1.5

        narrator "Dia bangun sendiri."
        narrator "Perlahan. Sakit."

        pause 2.0

        jump b2_dawn_alone

label b2_dawn_with_hafiz:

    scene bg_village_path_dawn
    with fade

    # TODO audio: play amb_village_dawn on ambient channel fadein 3.0

    show spr_mc injured at right
    show spr_hafiz neutral at left
    with dissolve

    pause 3.0

    hafiz "Kau tak bawak apa-apa masuk tadi?"
    mc "Ha."

    pause 1.5

    hafiz "Kuat jugak dia."
    mc "Lebih dari yang aku sangka."

    pause 1.5

    hafiz "Aku boleh teman kau."
    mc "Tak payah."
    hafiz "Kau pasti?"
    mc "Kerja ni kena buat sorang."

    pause 1.0

    hafiz "..."
    hafiz "Aku tunggu kau balik."

    mc "Ha."

    pause 1.0

    narrator "MC ambil beg dari kereta sebelum Hafiz bertolak."

    pause 1.0

    narrator "Hafiz masuk kereta."

    # TODO audio: play sfx_car_door_open volume 0.5

    pause 1.0

    hafiz "Jaga diri."

    # TODO audio: play sfx_car_engine_start volume 0.6

    hide spr_hafiz
    with dissolve

    narrator "MC tengok kereta tu sampai ia hilang dalam gelap."

    pause 2.0

    narrator "Dia sorang sekarang."
    narrator "Macam selalu."

    pause 1.5

    jump b2_dawn_converge

label b2_dawn_alone:

    scene bg_village_path_dawn
    with fade

    # TODO audio: play amb_village_dawn on ambient channel fadein 3.0

    show spr_mc injured at center
    with dissolve

    pause 4.0

    narrator "Pukul empat lebih pagi."

    pause 1.5

    narrator "Dia duduk bersendirian."

    pause 1.0

    narrator "Dua orang cedera."

    pause 0.8

    narrator "Satu hampir mati."

    pause 0.8

    narrator "Dan dia tak buat apa pun untuk hentikannya."

    pause 2.5

    narrator "Dia tahu dia salah."
    narrator "Bukan salah sebab tergesa-gesa."
    narrator "Salah sebab dia datang dengan tangan kosong."
    narrator "Salah sebab dia fikir dia boleh rehat dulu."
    narrator "Salah sebab dia rasa ia boleh tunggu."

    pause 3.0

    narrator "Dia tengok tangannya."

    pause 1.0

    narrator "Tangan yang kosong."

    pause 1.5

    narrator "Langit mula berubah."
    narrator "Perlahan sangat."
    narrator "Macam ia pun tak pasti nak terus atau tidak."

    pause 2.0

    narrator "Dia ingat bunyi tu."
    narrator "Bunyi yang keluar dari dalam kain putih tu."

    pause 1.5

    narrator "Macam tangisan."

    pause 1.0

    narrator "Dia dah dengar bunyi macam tu sebelum."
    narrator "Selalu dari orang yang kehilangan sesuatu."
    narrator "Bukan dari yang kita datang untuk hentikan."

    pause 3.0

    narrator "Dia rasa sesuatu yang dia tak biasa rasa."

    pause 1.0

    narrator "Macam dia datang ke sini untuk buat kerja."
    narrator "Tapi malam tadi bukan tentang kerja."

    pause 1.5

    narrator "Dia tak tahu lagi ia tentang apa."
    narrator "Tapi dia rasa - ia lebih dari tu."

    pause 3.0

    narrator "Dia bangun."

    pause 0.8

    narrator "Kaki dia sakit."

    pause 0.5

    narrator "Dia jalan jugak."

    pause 1.5

    narrator "Dia sorang."

    pause 1.0

    narrator "Macam selalu."

    pause 1.0

    narrator "Tapi malam ni rasa lain sikit."

    pause 1.0

    narrator "Lebih berat."

    pause 2.5

    jump b2_dawn_converge

label b2_dawn_converge:

    if hafiz_drives:
        narrator "Dia pegang beg yang dia ambil sebelum Hafiz bertolak."
    else:
        narrator "Dia berjalan balik ke kereta."
        narrator "Masih di tepi jalan. Masih terkunci."
        narrator "Dia buka pintu. Dia ambil beg dari tempat duduk belakang."

    pause 1.0

    narrator "Dia bukak zip tu."
    narrator "Dia tengok apa yang ada dalam tu."
    narrator "Cukup."

    pause 2.0

    scene black
    with fade

    pause 1.0

    show text "BAB DUA\nMalam Pertama" with fade
    pause 3.5
    hide text with fade

    pause 1.5

    jump beat3_scene1
