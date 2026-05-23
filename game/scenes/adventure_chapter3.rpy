label adv_chapter3:

    call adv_card_ch3

    scene bg_village_path_day
    with fade

    show spr_mc neutral at center
    with dissolve

    narrator "Waktu siang buat Batu Layar nampak macam kampung biasa."
    narrator "Itu yang buat rasa lagi tak sedap."

    jump adv_investigation_hub


label adv_investigation_hub:

    scene bg_village_path_day
    with dissolve

    if adv_mak_ros_done and adv_burial_done and adv_house_done:
        jump adv_chapter4

    narrator "MC semak buku notanya."
    narrator "Masih ada masa sebelum malam."

    menu:
        "Pergi ke rumah Mak Ros." if not adv_mak_ros_done:
            jump adv_mak_ros_house

        "Periksa kawasan kubur." if not adv_burial_done:
            jump adv_burial_ground

        "Masuk rumah keluarga lama." if not adv_house_done:
            jump adv_old_family_house

        "Bersiap sekarang, walaupun siasatan belum habis.":
            if not adv_can_release():
                narrator "MC tengok buku notanya."
                narrator "Masih ada benda yang belum lengkap: gerak-geri, identiti, atau cara melepaskan."
                narrator "Kalau dia teruskan sekarang, dia mungkin cuma bersedia untuk bertahan."
            jump adv_chapter4


label adv_mak_ros_house:

    $ adv_mak_ros_done = True

    scene bg_adv_mak_ros_house
    with fade

    show spr_mak_ros nervous at adv_left
    show spr_mc neutral at adv_right
    with dissolve

    mak_ros "Saya dengar bunyi tu dulu, sebelum benda tu sampai."
    mak_ros "Macam orang menangis. Tapi jauh. Dalam kain."

    $ adv_pick = renpy.call_screen("adv_inspection", "Rumah Mak Ros", "Rumah saksi yang menghadap jalan tempat Nayan mati.", [("Guna kamera telefon di tingkap", "camera"), ("Minta Mak Ros ulang bunyi yang dia dengar", "sound"), ("Periksa calar dekat pintu", "scratches")])

    if adv_pick == "camera":
        narrator "Dalam kamera, bayang pucat lalu di jalan yang sama, berkali-kali."
        narrator "Setiap kali jalan kosong, bayang tu berhenti sekejap sebelum melompat lagi."
        $ adv_observed_pattern = True
        $ adv_understanding += 1
        $ adv_add_note("Pocong ulang laluan yang sama dan berhenti bila tiada mangsa bergerak")

    elif adv_pick == "sound":
        mak_ros "Bunyi tu tak datang terus."
        mak_ros "Ada jeda. Macam sesuatu dalam kain tu perlu kumpul tenaga sebelum melompat lagi."
        mak_ros "Kalau orang lari, dia makin laju. Kalau orang diam, kadang-kadang dia berhenti sekejap."
        $ adv_observed_pattern = True
        $ adv_understanding += 1
        $ adv_add_note("Lompatan pocong ada jeda yang boleh dibaca")

    elif adv_pick == "scratches":
        narrator "Calar tu bukan bekas kuku."
        narrator "Macam kain dan tulang bergeser pada kayu."
        $ adv_add_note("Gerakan terikat tinggalkan kesan kain")

    hide spr_mak_ros
    with dissolve

    jump adv_investigation_hub


label adv_burial_ground:

    $ adv_burial_done = True

    scene bg_adv_grave_inspect
    with fade

    show spr_mc thinking at center
    with dissolve

    narrator "Kubur tu terletak jauh sikit daripada yang lain."
    narrator "Namanya pun dah kabur. Kubur tu macam dijaga asal cukup syarat saja."
    narrator "Tak ada rasa tenang."
    narrator "Tanahnya tak rata, macam kerja yang dibuat cepat-cepat dan tak mahu dikenang."

    $ adv_pick = renpy.call_screen("adv_inspection", "Kawasan Kubur", "Tanah kubur tak rata. Ada sesuatu yang putih tersangkut bawah batu lama.", [("Suluh tanah kubur", "soil"), ("Tarik benang putih perlahan-lahan", "thread"), ("Ambil gambar batu nisan", "marker")])

    if adv_pick == "soil":
        narrator "Lampu suluh nampakkan bekas gali lama."
        narrator "Bukan kerja yang dibuat dengan tertib."
        narrator "Kerja orang yang nak cepat siap."
        $ adv_burial_clue = True
        $ adv_understanding += 1
        $ adv_add_note("Pengebumian dibuat tanpa tertib")

    elif adv_pick == "thread":
        narrator "MC tarik sehelai benang longgar dari tanah."
        narrator "Kain kafan."
        narrator "Simpulannya masih ketat."
        $ adv_has_kafan_thread = True
        $ adv_burial_clue = True
        $ adv_understanding += 1
        $ adv_add_note("Simpulan kafan tak pernah dibuka")

    elif adv_pick == "marker":
        narrator "Gambar tu jadi jelas selepas beberapa saat."
        narrator "Ada nama yang hampir nampak, kemudian hilang balik."
        $ adv_add_note("Nama pada kubur sengaja dibiarkan hilang")

    jump adv_investigation_hub


label adv_old_family_house:

    $ adv_house_done = True

    scene bg_adv_old_house
    with fade

    show spr_mother neutral at adv_left
    show spr_mc neutral at adv_right
    with dissolve

    mother "Melur yang suruh kamu datang?"
    mc "Dia minta saya tolong abang dia."

    mother "Orang kampung ingat anak saya yang bawa bala."
    mother "Mereka tak tahu dia mati sebab hentikan bala yang sebenar."
    $ adv_identity_clue = True
    $ adv_add_note("Pocong itu abang Melur")

    $ adv_pick = renpy.call_screen("adv_inspection", "Rumah Keluarga Lama", "Bilik ni penuh dengan duka lama: kotak berkunci, tasbih, dan surat yang dilipat terlalu banyak kali.", [("Baca surat lama", "letter"), ("Ambil tasbih", "tasbih"), ("Cari dalam kabinet dapur", "salt")])

    if adv_pick == "letter":
        narrator "Surat tu menyebut dia sebagai anak, suami, dan ayah."
        narrator "Surat tu juga ceritakan harga yang dia bayar."
        $ adv_has_old_letter = True
        $ adv_understanding += 2
        $ adv_add_note("Dia mati melindungi kampung")

    elif adv_pick == "tasbih":
        mother "Ambillah. Kalau kamu nak buka simpulan tu, jangan buat macam kamu tengah menghukum dia."
        $ adv_has_tasbih = True
        $ adv_understanding += 1
        $ adv_add_note("Doa perlu mengiringi pelepasan")

    elif adv_pick == "salt":
        narrator "Ada sebungkus kecil garam dalam kabinet."
        narrator "Mungkin berguna."
        narrator "Tapi benda tu terasa macam pilihan orang yang takut, bukan orang yang faham."
        $ adv_has_salt = True

    if adv_burial_clue or adv_has_kafan_thread:
        mother "Mereka kebumikan dia cepat-cepat. Masa tu semua marah. Semua takut."
        mother "Simpulan kafan tu tak pernah dibuka."
        $ adv_understanding += 1
        $ adv_add_note("Ibu sahkan pengebumian tak selesai")

    hide spr_mother
    with dissolve

    jump adv_investigation_hub
