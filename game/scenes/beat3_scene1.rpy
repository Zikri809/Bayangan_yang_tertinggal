label beat3_scene1:

    # BEAT 3 - THE INVESTIGATION
    # Bayangan yang Tertinggal - The Shadow Left Behind
    #
    # Five investigation nodes visited in sequence. The player changes the
    # texture of the investigation through choices inside each node.
    #
    # ABANDON OPTION
    # From this beat onward, the MC can quietly choose to leave.

    scene bg_village_path_day
    with fade

    # TODO audio: play amb_village_day on ambient channel fadein 3.0

    show spr_mc neutral at center
    with dissolve

    narrator "Pagi datang macam ia selalu datang."

    pause 1.0

    narrator "Tanpa meminta izin sesiapa."

    pause 1.5

    narrator "MC dah pegang beg dia. Senjata dah dikeluarkan."
    narrator "Prepared items, tools, notes - everything laid out the night before."

    pause 1.0

    narrator "Kerja bermula."

    pause 2.0

    jump beat3_node1

label beat3_node1:

    scene bg_village_house_ext
    with dissolve

    show spr_mak_ros nervous at left
    show spr_mc neutral at right
    with dissolve

    narrator "Dia berada di luar rumah."
    narrator "Mungkin takut nak masuk dalam."

    pause 1.5

    mc "Mak Cik okay?"

    mak_ros "..."
    mak_ros "Encik yang malam tadi tu kan."

    mc "Ya. Maaf sebab tak berjaya hentikan dia."

    show spr_mak_ros serious at left
    with dissolve

    mak_ros "Dah lama benda ni berlaku."
    mak_ros "Bukan salah encik."

    pause 1.5

    menu:
        "\"Mak Cik nampak apa malam tadi?\"":
            jump b3_n1_saw

        "\"Mak Cik dengar apa sebelum ia datang?\"":
            jump b3_n1_heard

        "\"Dah berapa kali benda ni berlaku sebelum ni?\"":
            jump b3_n1_pattern

label b3_n1_saw:

    mak_ros "Saya nampak ia dari jauh dulu."
    mak_ros "Putih. Besar. Melompat."
    mak_ros "Tapi yang paling - yang paling buat saya takut-"

    show spr_mak_ros sad at left
    with dissolve

    mak_ros "Benda itu bukan tengok saya macam binatang tengok mangsanya."

    pause 1.0

    mak_ros "Ia tengok saya macam - macam ia kenal saya."

    pause 2.0

    narrator "MC catat pernyataan itu."

    $ learned_attack_detail = True

    jump b3_n1_close

label b3_n1_heard:

    mak_ros "Bunyi tu."
    mak_ros "Saya dengar bunyi tu dulu sebelum saya nampak apa-apa."

    mc "Bunyi macam mana?"

    mak_ros "Macam orang nangis."

    pause 1.0

    mak_ros "Tapi bukan nangis biasa."
    mak_ros "Macam nangis dalam bantal. Dalam sesuatu."

    pause 1.0

    mak_ros "Saya dengar tu - saya fikir ada orang dalam kesusahan."
    mak_ros "Saya keluar nak tengok siapa."

    pause 1.5

    mak_ros "Bodoh kan."

    mc "Bukan bodoh."

    $ learned_sound_detail = True

    jump b3_n1_close

label b3_n1_pattern:

    mak_ros "Dah lama."
    mak_ros "Dua bulan lebih."

    mc "Berapa orang?"

    mak_ros "Yang mati - empat."

    pause 1.0

    mak_ros "Yang cedera - lebih dari tu."

    pause 1.0

    mak_ros "Tapi yang pelik -"

    show spr_mak_ros serious at left
    with dissolve

    mak_ros "Ia tak serang semua orang."
    mak_ros "Ada orang yang ia lalu je. Tak buat apa-apa."

    mc "Siapa yang ia lalu je tu?"

    mak_ros "Orang yang tak ada kena-mengena dengan keluarga tu."

    $ learned_pocong_pattern = True

    jump b3_n1_close

label b3_n1_close:

    pause 1.5

    mc "Baiklah terima kasih, Mak Cik."

    mak_ros "Encik hati-hati."

    pause 1.0

    mak_ros "Ia bukan macam yang orang selalu cerita dalam buku."
    mak_ros "Ia lebih lagi - ia lebih sedih dari tu."

    pause 2.0

    hide spr_mak_ros
    with dissolve

    menu:
        "Teruskan siasatan.":
            jump beat3_node2

        "Tinggalkan kampung ni.":
            jump beat3_abandon

label beat3_node2:

    scene bg_village_centre
    with dissolve

    show spr_mc neutral at right
    with dissolve

    narrator "Kampung kecik."
    narrator "Semua orang kenal masing-masing."
    narrator "Dan semua orang tahu MC sedang tanya soalan."

    pause 1.5

    show spr_villager_a neutral at left
    with dissolve

    villager_a "Encik dari luar kan?"

    mc "Ha."

    villager_a "Saya dengar encik tanya-tanya pasal benda tu."

    mc "Haah."

    pause 1.0

    villager_a "Ada seorang ni - kalau encik jumpa dia-"
    villager_a "Jangan terlalu banyak tanya pasal benda tu."

    mc "Siapa?"

    villager_a "Orang kampung panggil dia Atan."
    villager_a "Bapak dia - ada kaitan dengan benda tu."

    pause 1.0

    villager_a "Dia memang tak suka orang cakap pasal benda tu."
    villager_a "Lagi-lagi orang luar."

    show spr_villager_a nervous at left
    with dissolve

    villager_a "Tapi kalau encik nak tahu - dia ada kat kawasan kubur tu setiap pagi."

    hide spr_villager_a
    with dissolve

    pause 2.0

    narrator "Orang-orang tengok dia lalu."
    narrator "Macam tengok seseorang pergi buat sesuatu"
    narrator "yang mereka sendiri tak berani buat."

    pause 2.0

    menu:
        "Teruskan ke kawasan kubur.":
            jump beat3_node3_approach

        "Tinggalkan kampung ni.":
            jump beat3_abandon

label beat3_node3_approach:

    scene bg_fight_site
    with dissolve

    # TODO audio: play amb_fight_site on ambient channel fadein 2.0

    show spr_mc neutral at center
    with dissolve

    narrator "Dia berhenti."

    pause 1.0

    narrator "Tempat ni lain."
    narrator "Bukan pasal rupa. Rupa dia biasa je."
    narrator "Tapi ada sesuatu dalam hawa dia."
    narrator "Berat. Seperti sesuatu yang berlaku di sini belum selesai lagi."

    pause 2.0

    menu:
        "Periksa kesan tenaga gelap yang ada kat sini.":
            jump b3_n3_examine_energy

        "Tengok kesan pertarungan - bekas tapak kaki, kesan tanah.":
            jump b3_n3_examine_fight

        "Tengok sekeliling - apa yang ada dekat tempat ni.":
            jump b3_n3_examine_surroundings

label b3_n3_examine_energy:

    narrator "Dia duduk berlutut."
    narrator "Tangan dia dekat tapi tak sentuh."
    narrator "Ada sesuatu yang ditinggal kat sini."
    narrator "Bukan sesuatu yang semulajadi."

    pause 1.5

    narrator "MC pernah rasa benda macam ni sebelum."
    narrator "Bukan banyak kali."
    narrator "Tapi cukup untuk kenal."

    pause 1.0

    narrator "Ia."

    pause 1.0

    narrator "Sama."

    show spr_mc thinking at center
    with dissolve

    mc "..."

    pause 2.0

    $ found_bomoh_site = True
    $ devil_noted = True

    jump b3_n3_choice2

label b3_n3_examine_fight:

    narrator "Tanah kat sini lain."
    narrator "Dua puluh tahun dah berlalu."
    narrator "Tapi tempat di mana sesuatu yang mengerikan berlaku -"
    narrator "ia tersemat disitu."

    pause 1.5

    narrator "Dua orang bertempur disini."
    narrator "MC boleh baca semua itu daripada tanah."
    narrator "Tiada yang berjaya keluar hidup-hidup."

    pause 1.5

    mc "Tapi satu daripada mereka - yang satu ni -"

    narrator "Dia melihat ke arah bekas tapak kaki yang lebih dalam."
    narrator "Orang yang lawan dengan sepenuh tenaga."

    mc "Dia datang sini dengan kesedaran penuh yang dia tak akan dapat keluar dengan selamat."

    pause 2.0

    $ learned_pact_partial = True
    $ found_bomoh_site = True

    jump b3_n3_choice2

label b3_n3_examine_surroundings:

    narrator "Dia tengok sekeliling."
    narrator "Tempat ni sedikit jauh dari kawasan kampung."
    narrator "Jeritla sekuat mana pun - orang kampung tak akan dengar dengan jelas."

    pause 1.5

    narrator "Seseorang datang ke sini dengan sengaja."
    narrator "Bukan tanpa sengaja."
    narrator "Bukan tersesat."
    narrator "Tetapi datang dengan sengaja. Untuk sesuatu yang dia tak nak orang lain nampak."

    pause 1.0

    narrator "Atau untuk lindungi orang lain daripada nampak sesuatu."

    pause 2.0

    $ found_bomoh_site = True

    jump b3_n3_choice2

label b3_n3_choice2:

    pause 1.0

    narrator "Ada sesuatu yang lain."
    narrator "Sesuatu yang dia kenal."

    pause 1.5

    menu:
        "Simpan dalam kepala. Jangan cakap kuat-kuat.":
            jump b3_n3_devil_silent

        "Sebut nama dalam hati. Pastikan memori tu betul.":
            jump b3_n3_devil_noted

        "Ambil sample. Bawa bukti.":
            jump b3_n3_devil_sample

label b3_n3_devil_silent:

    narrator "Dia diam."
    narrator "Ada perkara yang lebih baik disimpan sorang diri."
    narrator "Buat masa ni."

    $ devil_noted = True

    jump b3_n3_end

label b3_n3_devil_noted:

    mc "..."

    narrator "Dia dah cari benda ni lama."
    narrator "Bukan ini yang dia cari - tetapi ia mempunyai kesan yang sama."
    narrator "Ia pernah ada dekat sini."
    narrator "Dua puluh tahun lepas."

    pause 1.5

    narrator "Dia simpan itu. Dan teruskan."

    $ devil_noted = True
    $ devil_thread_deepened = True

    jump b3_n3_end

label b3_n3_devil_sample:

    narrator "Dia keluarkan kotak kecil dari beg."
    narrator "Ambil sedikit sampel. Bungkus dan simpan."
    narrator "Ini mungkin berguna suatu hari nanti."
    narrator "Bukan hari ni. Mungkin juga bukan tahun ni."
    narrator "Tapi suatu hari nanti."

    $ devil_noted = True
    $ devil_sample_taken = True

    jump b3_n3_end

label b3_n3_end:

    pause 1.5

    narrator "Dia tinggalkan tempat tu."
    narrator "Tanpa menoleh ke belakang."

    pause 1.0

    menu:
        "Teruskan ke kawasan kubur.":
            jump beat3_node4

        "Tinggalkan kampung ni.":
            jump beat3_abandon

label beat3_node4:

    scene bg_burial_ground
    with dissolve

    # TODO audio: play amb_burial_ground on ambient channel fadein 2.0

    show spr_mc neutral at right
    with dissolve

    narrator "Kawasan perkuburan kampung."
    narrator "Batu-batu lama. Nama-nama yang dah pudar."
    narrator "Dan satu kubur yang lain dari yang lain."

    pause 1.5

    narrator "Ia ada disitu. Tapi macam orang letak dia kat situ sebab terpaksa."
    narrator "Tiada nama yang jelas. Tiada penghormatan penuh."
    narrator "Dikebumikan dengan tergesa-gesa. Ini yang MC fikir."

    pause 2.0

    show spr_son hostile at left
    with dissolve

    pause 2.0

    son "Orang luar."

    mc "Ya."

    son "Kau datang pasal benda tu."

    mc "Ya."

    pause 1.0

    show spr_son cold at left
    with dissolve

    son "Bunuh je lah."
    son "Jangan banyak tanya. Takyah cuba nak faham-faham."
    son "Bunuh je. Habis cerita."

    pause 1.5

    menu:
        "\"Kubur siapa ni?\"":
            jump b3_n4_ask_grave

        "Diam. Perhatikan saja.":
            jump b3_n4_silent

        "\"Kau kenal benda tu?\"":
            jump b3_n4_ask_know

label b3_n4_ask_grave:

    mc "Kubur siapa ni?"

    show spr_son hostile at left
    with dissolve

    son "Bukan urusan kau."

    pause 1.0

    mc "Ia mungkin berkaitan dengan kerja saya."

    son "Kerja kau adalah untuk bunuh benda tu."
    son "Kubur ni tak ada kaitan."

    pause 1.5

    narrator "MC tengok kubur tu lagi."
    narrator "Dia nampak sesuatu yang dia patut kesan dari awal."
    narrator "Cara ia dikebumikan."
    narrator "Tergesa-gesa. Dan lama."
    narrator "Lebih dari 10 tahun."

    $ found_burial_site = True
    $ learned_rushed_burial = True

    jump b3_n4_close

label b3_n4_silent:

    narrator "MC diam."
    narrator "Dia hanya tengok."

    pause 2.0

    son "Apa yang kau tengok?"

    mc "Kubur."

    pause 1.0

    son "Ya memang kubur."
    son "Bunuh benda tu dan pergi dari sini."

    narrator "MC lihat keadaan kubur tu."
    narrator "Cara orang yang gali dan tanam macam dibuat dengan tergesa-gesa, tak ikhlas."

    $ found_burial_site = True

    jump b3_n4_close

label b3_n4_ask_know:

    mc "Kau kenal benda tu?"

    son "Kenal?"

    pause 1.0

    son "Benda tu dah ada kat kampung ni lama dah."
    son "Sejak - sejak bapak aku mati."
    son "Bapak aku yang bawak benda tu."

    pause 1.5

    show spr_son cold at left
    with dissolve

    son "Sebab tu aku cakap - bunuh je."
    son "Patut bunuh dari dulu lagi."

    pause 2.0

    $ son_mentioned_father = True
    $ found_burial_site = True

    jump b3_n4_close

label b3_n4_close:

    pause 1.5

    hide spr_son
    with dissolve

    narrator "MC tinggalkan kawasan perkuburan."

    pause 1.0

    narrator "Lelaki tu masih kekal disana."
    narrator "Tengok kubur yang dia kenal dan jaga dari kecil lagi."
    narrator "MC tak tahu siapa yang dikebumikan kat situ."
    narrator "Tapi dia rasa ia penting."

    pause 2.0

    menu:
        "Teruskan ke rumah lama di hujung kampung.":
            jump beat3_node5

        "Tinggalkan kampung ni.":
            jump beat3_abandon

label beat3_node5:

    scene bg_family_house_ext
    with dissolve

    show spr_mc neutral at center
    with dissolve

    narrator "Rumah tu ada kat hujung kampung."

    pause 1.0

    narrator "Orang lain dah lama tak lalu di kawasan sini."
    narrator "Tapi rumah tu masih ada."
    narrator "Ada tanda-tanda orang tinggal. Samar-samar."

    pause 1.5

    narrator "Pintu tak berkunci."

    pause 1.0

    narrator "MC tolak masuk."

    scene bg_family_house_int
    with dissolve

    # TODO audio: play amb_family_house_int on ambient channel fadein 2.0

    pause 3.0

    narrator "Dia dah ada kat situ."

    pause 1.0

    narrator "Duduk kat kerusi tepi tingkap."

    pause 1.0

    narrator "Tak terkejut."

    pause 1.0

    narrator "Macam dia tahu ada orang akan datang."

    pause 2.0

    show spr_mother neutral at left
    with dissolve

    pause 2.0

    mother "Lama dah saya tunggu."

    mc "Saya datang nak tanya pasal benda yang berlaku kat kampung ni."

    mother "Saya tahu."

    pause 1.5

    mother "Duduk lah."

    mother "Anak saya."

    pause 1.0

    mother "Dia orang yang baik."

    pause 0.8

    mother "Orang kampung tak faham tu."

    pause 0.8

    mother "Dah lama mereka salah faham."

    pause 2.0

    mc "Apa yang berlaku?"

    mother "Ada sesuatu yang datang ke kampung ni."
    mother "Dua puluh tahun lepas."
    mother "Sesuatu yang jahat. Betul-betul jahat."

    pause 1.0

    mother "Anak saya - dia tahu."
    mother "Dia nampak apa yang orang lain tak nampak."
    mother "Dia sentiasa macam tu."

    pause 1.5

    mc "Dan dia buat apa?"

    show spr_mother distant at left
    with dissolve

    mother "Dia buat apa yang patut dia buat."
    mother "Walaupun dia tahu apa yang akan jadi pada dia."

    pause 2.0

    menu:
        "\"Bagaimana dia tahu apa yang akan jadi?\"":
            jump b3_n5_c1_how

        "\"Apa yang jadi pada dia?\"":
            jump b3_n5_c1_what

label b3_n5_c1_how:

    mother "Dia tahu sebab dia yang pilih."
    mother "Bukan terpaksa. Tapi atas pilihan."

    pause 1.5

    mother "Ada harga yang kena bayar."
    mother "Dan dia bayar."

    jump b3_n5_c2_menu

label b3_n5_c1_what:

    mother "Dia mati."

    pause 1.0

    mother "Dia dan benda jahat tu - dua-dua mati."

    pause 1.0

    mother "Orang kampung nampak dua-dua mati."
    mother "Mereka tak selidik lebih."
    mother "Mereka ambil kesimpulan sendiri."

    pause 2.0

    jump b3_n5_c2_menu

label b3_n5_c2_menu:

    pause 1.0

    mother "Anak tahu - orang kampung ni -"
    mother "Mereka bukan orang jahat."
    mother "Mereka cuma - takut."

    pause 1.5

    menu:
        "\"Saya faham.\" Biar dia tentukan bila nak cakap.":
            jump b3_n5_c2_safe_a

        "\"Kita ada masa lagi?\" Bimbang pasal malam ni.":
            jump b3_n5_c2_safe_b

        "\"Beritahu saya semua. Sebelum malam ni.\"":
            jump b3_n5_c2_truth

label b3_n5_c2_safe_a:

    mc "Saya faham."

    mother "Anak saya - dia buat benda yang betul."
    mother "Satu hari orang akan tahu."

    pause 2.0

    $ found_mother = True
    $ mother_told_truth = False

    jump b3_n5_close

label b3_n5_c2_safe_b:

    mc "Kita ada masa lagi?"

    mother "Ia datang pada waktu malam."
    mother "Sementara siang - kita masih selamat."

    pause 1.0

    mother "Tapi makcik penat, nak."
    mother "Cerita ni berat."
    mother "Saya dah simpan dua puluh tahun."

    pause 1.5

    mother "Mungkin lain kali."

    $ found_mother = True
    $ mother_told_truth = False

    jump b3_n5_close

label b3_n5_c2_truth:

    mc "Beritahu saya semua. Sebelum malam ni."

    pause 3.0

    show spr_mother speaking at left
    with dissolve

    mother "..."

    pause 1.5

    mother "Baik."

    pause 1.0

    mother "Ada bomoh."
    mother "Dia datang ke kampung ni dua puluh tahun lepas."
    mother "Kami tak tahu dari mana. Kami tak tahu kenapa."
    mother "Dia jahat. Betul-betul jahat. Bukan kerana miskin atau sakit atau marah."
    mother "Hanya jahat tanpa alasan."

    pause 1.5

    mother "Anak saya - dia nampak apa yang bomoh tu buat."
    mother "Dia nampak orang-orang kampung dalam bahaya."

    pause 1.0

    mother "Tapi bomoh tu kuat sangat."
    mother "Bukan kuat biasa. Kuat sebab dia dapat kuasa dari sesuatu yang lebih besar."

    pause 1.5

    mother "Anak saya - dia tahu dia tak boleh lawan tanpa melakukan sesuatu."
    mother "Sesuatu yang ada harganya."

    pause 2.0

    show spr_mother grieving at left
    with dissolve

    mother "Dia buat perjanjian."

    pause 1.0

    mother "Dengan sesuatu yang gelap."
    mother "Untuk dapat kuasa yang cukup."
    mother "Untuk hentikan bomoh tu."

    pause 2.0

    mother "Dia tahu harganya."
    mother "Nyawa dia."

    pause 1.5

    mother "Dia tetap buat."

    pause 3.0

    mc "Dan kampung ni -"

    mother "Mereka nampak dua-dua mati."
    mother "Mereka nampak anak saya dan bomoh tu mati bersama."
    mother "Mereka tak tahu pasal perjanjian tu."
    mother "Mereka tak faham kenapa anak saya boleh lawan bomoh sekuat tu."
    mother "Mereka fikir - mereka fikir anak saya yang bawak bomoh tu."

    pause 2.0

    mother "Mereka salahkan dia."

    pause 1.0

    mother "Mereka salahkan keluarga kami."

    pause 1.0

    mother "Mereka bunuh menantu saya."

    pause 2.5

    mother "Cucu saya masih kat sini."
    mother "Dia benci bapaknya."
    mother "Dia tak tahu."

    pause 2.0

    mother "Anak saya - dia mati untuk selamatkan orang-orang yang kemudiannya bunuh isteri dia sendiri."

    pause 3.0

    mc "..."

    pause 2.0

    mother "Pengebumiannya dibuat tergesa-gesa."
    mother "Simpulan kafan tu - tak pernah dibuka."
    mother "Saya cuba. Mereka tak bagi."

    pause 2.0

    mother "Itu sebab dia masih ada."
    mother "Bukan sebab dia jahat."
    mother "Sebab tak ada sesiapa yang tolong dia pergi."

    pause 3.0

    $ found_mother = True
    $ mother_told_truth = True
    $ learned_pact = True
    $ learned_wife_fate = True
    $ learned_rushed_burial = True

    narrator "MC terdiam."

    pause 1.5

    narrator "Dia tengok perempuan tua yang duduk kat kerusi tu."
    narrator "Yang dah simpan semua ni sorang diri."
    narrator "Dua puluh tahun."

    pause 2.0

    mc "Terima kasih."

    pause 2.0

    show spr_mother neutral at left
    with dissolve

    mother "Tolong dia pergi dengan betul."

    pause 3.0

    jump b3_n5_close

label b3_n5_close:

    scene bg_family_house_ext
    with fade

    show spr_mc neutral at center
    with dissolve

    pause 2.0

    narrator "MC keluar dari rumah tu."

    if mother_told_truth:
        narrator "Dia bawa sesuatu keluar bersamanya."
        narrator "Nama yang tak pernah disebut. Cerita yang tak pernah diceritakan."
        narrator "Dan permintaan wanita tua yang dah lama penat menunggu."

        pause 2.0

        narrator "Dia tahu sekarang."
        narrator "Sebelum malam tiba."
    else:
        narrator "Dia keluar dengan lebih banyak soalan dari jawapan."
        narrator "Wanita tua tu tahu lebih dari apa yang dia cakap."
        narrator "Tapi dia tak boleh paksa."

        pause 2.0

        narrator "Malam ni dia kena buat dengan apa yang ada."

    pause 2.0

    menu:
        "Bersiap untuk malam ni.":
            jump beat3_end

        "Tinggalkan kampung ni.":
            jump beat3_abandon

label beat3_end:

    scene bg_village_path_day
    with dissolve

    narrator "MC sediakan segala keperluan."
    narrator "Senjata yang betul. Perlindungan yang betul."
    narrator "Semua yang patutnya dibawa malam tadi - dah ada sekarang."

    pause 2.0

    narrator "Dia tunggu."

    pause 3.0

    stop ambient fadeout 3.0

    pause 2.0

    # TODO audio: play mus_pocong_theme fadein 3.0 volume 0.2

    narrator "Ia datang."

    pause 2.0

    # TODO audio: play sfx_pocong_hop volume 0.5
    pause 2.0
    # TODO audio: play sfx_pocong_hop volume 0.7

    narrator "MC berdiri menunggu."

    pause 1.0

    if mother_told_truth:
        narrator "Dia tahu siapa yang datang."
        narrator "Dia tahu ceritanya."
        narrator "Cerita yang dia tahu tu berat."
        narrator "Lebih berat dari senjata yang dia pegang."
    else:
        narrator "Dia tak tahu semua."
        narrator "Tapi dia tahu cukup untuk buat kerja yang patut dilakukan."

    pause 2.0

    # TODO audio: play sfx_pocong_hop volume 0.9

    narrator "Ia semakin dekat."

    pause 1.5

    jump beat4_open

label beat3_abandon:

    $ abandoned = True

    scene black
    with fade

    stop ambient fadeout 2.0

    pause 2.0

    narrator "MC pergi ke keretanya."

    pause 1.0

    narrator "Dia masuk, start enjin."

    pause 1.5

    narrator "Tanpa melihat ke belakang dia tinggalkan kawasan kampung itu."

    pause 2.0

    jump abandon_ending
