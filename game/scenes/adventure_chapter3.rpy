label adv_chapter3:

    call adv_card_ch3

    scene bg_village_path_day
    with fade

    show spr_mc neutral at center
    with dissolve

    narrator "Waktu siang buat Batu Layar nampak macam kampung biasa."
    narrator "Itu yang buat rasa makin tak sedap."

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
                narrator "Kalau dia teruskan sekarang, mungkin dia cuma cukup bersedia untuk bertahan."
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
    mak_ros "Saya dah lama tak tidur betul-betul."
    mak_ros "Kalau terlelap pun, bunyi duk tu masuk mimpi dulu."
    mc "Malam Nayan mati, Mak Ros nampak apa?"
    mak_ros "Tak nampak jelas. Tapi saya tahu satu benda."
    mak_ros "Dia bukan cari Nayan dari awal. Nayan cuma bergerak masa benda tu lalu."

    $ adv_pick = renpy.call_screen("adv_inspection", "Rumah Mak Ros", "Rumah saksi yang menghadap jalan tempat Nayan mati.", [("Guna kamera telefon di tingkap", "camera"), ("Minta Mak Ros ulang bunyi yang dia dengar", "sound"), ("Periksa calar dekat pintu", "scratches")])

    if adv_pick == "camera":
        narrator "Dalam kamera, bayang pucat lalu di jalan yang sama, berkali-kali."
        narrator "Bila jalan kosong, bayang tu berhenti sekejap sebelum melompat lagi."
        $ adv_observed_pattern = True
        $ adv_understanding += 1
        $ adv_add_note("Pocong ulang laluan yang sama dan berhenti bila tiada mangsa bergerak")

    elif adv_pick == "sound":
        mak_ros "Bunyi tu tak datang terus."
        mak_ros "Ada jeda. Macam sesuatu dalam kain tu perlu kumpul tenaga sebelum melompat lagi."
        mak_ros "Kalau orang lari, dia makin laju. Kalau orang diam, kadang-kadang dia berhenti."
        $ adv_observed_pattern = True
        $ adv_understanding += 1
        $ adv_add_note("Lompatan pocong ada jeda yang boleh dibaca")

    elif adv_pick == "scratches":
        narrator "Calar tu bukan bekas kuku."
        narrator "Macam kain dan tulang bergeser pada kayu."
        narrator "Jarak calar tu tak sama. Ada ruang kosong, macam kesan lompatan yang selalu berhenti sekejap."
        $ adv_observed_pattern = True
        $ adv_understanding += 1
        $ adv_add_note("Gerakan terikat tinggalkan kesan kain")

    mak_ros "Nayan tak ada kena-mengena dengan dosa lama tu."
    mak_ros "Dia cuma lalu dekat laluan yang benda tu ulang setiap malam."
    mak_ros "Orang kampung suka cakap jangan keluar malam."
    mak_ros "Tapi mereka jarang tanya kenapa benda tu masih berjalan di jalan yang sama."
    $ adv_add_note("Nayan jadi mangsa laluan pocong yang berulang")

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
    narrator "Tanahnya tak rata, macam kerja yang dibuat cepat-cepat lepas tu semua orang pura-pura lupa."
    narrator "Kubur lain ada batu yang dibersihkan, rumput yang dipotong, bekas doa orang yang datang."
    narrator "Kubur ni cuma ada tanah berat dan kesan ditinggalkan."
    narrator "MC rasa macam berdiri depan rahsia yang sengaja dibiarkan reput."
    narrator "Dia angkat lampu suluh dan biarkan cahayanya bergerak perlahan atas tanah."

    $ adv_grave_hotspots = [("Tanah tak rata", "soil", 140, 700, 420, 190, "Bekas gali lama."), ("Benang putih", "thread", 940, 780, 330, 170, "Kain kafan tersangkut di bawah batu."), ("Batu nisan", "marker", 1520, 330, 300, 330, "Nama yang hampir hilang bawah lumut.")]
    $ adv_found_grave = renpy.call_screen("adv_flashlight_search", "Kawasan Kubur", "Lampu suluh cuma cukup terang untuk satu bahagian pada satu masa.", adv_grave_hotspots, 2)

    if "soil" in adv_found_grave:
        narrator "Lampu suluh nampakkan bekas gali lama."
        narrator "Bukan kerja yang dibuat dengan tertib."
        narrator "Kerja orang yang nak cepat siap."
        $ adv_burial_clue = True
        $ adv_understanding += 1
        $ adv_add_note("Jenazah diurus kelam-kabut")

    if "thread" in adv_found_grave:
        narrator "MC tarik sehelai benang longgar dari tanah."
        narrator "Kain kafan."
        narrator "Simpulannya masih ketat."
        $ adv_has_kafan_thread = True
        $ adv_burial_clue = True
        $ adv_understanding += 1
        $ adv_add_note("Simpulan kafan tak pernah dibuka")

    if "marker" in adv_found_grave:
        narrator "Tulisan pada batu tu jadi jelas selepas beberapa saat."
        narrator "Huruf yang pudar tu tersusun perlahan-lahan."
        narrator "AZLAN."
        narrator "Lepas tu nama tu hilang balik bawah lumut dan tanah."
        $ adv_identity_clue = True
        $ adv_add_note("Nama pada kubur: Azlan")

    if not adv_has_kafan_thread:
        narrator "Sebelum MC berundur, lampu suluhnya menangkap sehelai benang putih tersangkut di bawah batu."
        narrator "Dia simpan benang kafan tu. Bukti kecil yang simpulan itu belum selesai."
        $ adv_has_kafan_thread = True
        $ adv_add_note("Benang kafan jadi bukti simpulan")

    $ adv_burial_clue = True
    narrator "Angin lalu perlahan di kawasan kubur."
    narrator "Benang kafan di tangan MC terasa kering, tapi bau tanah basah masih melekat."
    narrator "Buat pertama kali, kes ni tak terasa macam memburu benda seram."
    narrator "Ia terasa macam membetulkan sesuatu yang orang hidup pernah rosakkan."

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
    mother "Melur masih ingat rumah ni?"
    mc "Dia ingat cukup untuk takut, tapi cukup juga untuk minta tolong."
    mother "Budak tu pergi sebab saya suruh dia pergi."
    mother "Kalau dia tinggal, kampung ni akan telan dia sekali."

    mother "Nama dia Azlan."
    mother "Orang kampung ingat Azlan yang bawa bala."
    mother "Mereka tak tahu dia mati sebab hentikan bala yang sebenar."
    mother "Ada bomoh lama yang guna ketakutan kampung ni. Azlan hentikan dia, tapi orang cuma nampak dua mayat, lepas tu salahkan keluarga kami."
    mother "Sebelum tu, ternakan mati, budak kecil demam tiba-tiba, orang balik meracau lepas jumpa bomoh tu malam-malam."
    mother "Azlan jumpa tempat dia buat kerja. Itu sebab bomoh tu cari dia dulu."
    mother "Azlan bukan orang alim besar. Dia cuma anak yang degil."
    mother "Tapi bila semua orang tutup pintu, dia yang keluar tengok apa sebenarnya jadi."
    $ adv_identity_clue = True
    $ adv_knows_bala_truth = True
    $ adv_add_note("Pocong itu Azlan, abang Melur")
    $ adv_add_note("Azlan dituduh membawa bala selepas menghentikan bomoh lama")

    $ adv_pick = renpy.call_screen("adv_inspection", "Rumah Keluarga Lama", "Bilik ni penuh dengan duka lama: kotak berkunci, tasbih, dan surat yang dilipat terlalu banyak kali.", [("Baca surat lama", "letter"), ("Ambil tasbih", "tasbih"), ("Cari garam untuk bertahan", "salt")])

    if adv_pick == "letter":
        narrator "Surat tu cerita tentang dia sebagai anak, suami, dan ayah."
        narrator "Surat tu juga ceritakan harga yang dia bayar untuk hentikan bomoh itu."
        narrator "Ayat terakhirnya bukan pasal mati."
        narrator "Ayat terakhirnya minta sesiapa yang jumpa surat tu jangan biarkan anaknya membesar dengan nama ayah yang dipijak."
        $ adv_has_old_letter = True
        $ adv_knows_child = True
        $ adv_knows_bala_truth = True
        $ adv_understanding += 2
        $ adv_add_note("Dia mati melindungi kampung")
        $ adv_add_note("Azlan tinggalkan seorang anak")

    elif adv_pick == "tasbih":
        mother "Ambillah. Kalau kamu nak buka simpulan tu, jangan datang macam kamu nak hukum dia."
        $ adv_has_tasbih = True
        $ adv_understanding += 1
        $ adv_add_note("Doa perlu mengiringi pelepasan")

    elif adv_pick == "salt":
        narrator "Ada sebungkus kecil garam dalam kabinet."
        narrator "Mungkin berguna kalau MC cuma mahu hidup sampai subuh."
        mother "Garam boleh buat dia berundur."
        mother "Tapi kalau kamu cuma mahu dia sakit, kamu takkan faham kenapa dia masih terikat."
        narrator "Pilihan tu terasa macam jalan orang yang takut, bukan orang yang sudah faham."
        $ adv_has_salt = True
        $ adv_fear += 1
        $ adv_add_note("Garam membantu bertahan, bukan melepaskan")

    if adv_has_old_letter and not adv_has_tasbih:
        mother "Surat saja tak cukup. Tangan kamu pun kena tenang."
        mother "Ambil tasbih ni. Kalau kamu sebut nama dia, sebut macam orang yang datang nak tolong."
        $ adv_has_tasbih = True
        $ adv_understanding += 1
        $ adv_add_note("Tasbih dibawa untuk pelepasan")

    elif adv_has_tasbih and not adv_has_old_letter:
        mother "Dan satu lagi. Jangan bawa tasbih tu tanpa tahu siapa yang kamu doakan."
        narrator "Dia menyerahkan surat lama yang sudah berkali-kali dilipat."
        narrator "Dalam surat tu, Azlan menulis tentang isterinya, anaknya, dan keputusan yang makan nyawanya."
        $ adv_has_old_letter = True
        $ adv_knows_child = True
        $ adv_knows_bala_truth = True
        $ adv_understanding += 1
        $ adv_add_note("Surat Azlan dibawa bersama tasbih")
        $ adv_add_note("Azlan tinggalkan seorang anak")

    if adv_burial_clue or adv_has_kafan_thread:
        mother "Mereka kebumikan dia cepat-cepat. Masa tu semua marah. Semua takut."
        mother "Simpulan kafan tu tak pernah dibuka."
        mother "Saya minta mereka berhenti sekejap."
        mother "Saya minta mereka sebut nama dia elok-elok."
        mother "Mereka kata jangan panjang-panjangkan bala lagi."
        $ adv_understanding += 1
        $ adv_add_note("Ibu sahkan pengebumian tak selesai")

    mother "Kalau kamu jumpa dia malam ni, jangan mulakan dengan keris."
    mother "Mulakan dengan nama dia."
    mother "Kalau Azlan masih dengar apa-apa, biar benda pertama yang sampai bukan takut."

    hide spr_mother
    with dissolve

    jump adv_investigation_hub
