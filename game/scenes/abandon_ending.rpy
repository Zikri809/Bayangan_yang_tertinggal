label abandon_ending:

    # ABANDON ENDING
    # Triggers from Beat 3 when the player chooses to leave Batu Layar.

    scene bg_road_leaving
    with fade

    # TODO audio: play amb_road_driving on ambient channel fadein 2.0

    show spr_mc neutral at center
    with dissolve

    pause 3.0

    narrator "Dia memandu."

    pause 1.5

    narrator "Kampung tu mengecil dalam cermin pandang belakang."

    pause 1.5

    narrator "Dia tidak berhenti."

    pause 2.0

    narrator "Batu Layar hilang."

    pause 1.0

    narrator "Pokok-pokok berlalu."

    pause 1.0

    narrator "Jalan berterusan."

    pause 2.0

    narrator "Dia bernafas."

    pause 1.5

    narrator "Kerja dia bukan untuk mati kat sana."

    pause 1.0

    narrator "Benda tu terlampau kuat."

    pause 1.0

    narrator "Dia buat keputusan yang betul."

    pause 4.0

    jump abandon_scene2

label abandon_scene2:

    scene black
    with fade

    pause 1.0

    show text "Beberapa hari kemudian." with fade
    pause 3.0
    hide text with fade

    pause 1.0

    scene bg_mc_city_apartment
    with fade

    # TODO audio: play amb_city_day on ambient channel fadein 3.0

    show spr_mc neutral at center
    with dissolve

    pause 2.0

    narrator "Bilik dia."

    pause 1.0

    narrator "Dekat bandar."

    pause 1.0

    narrator "Bising yang biasa."

    pause 2.0

    narrator "Dia hampir percaya semuanya okay."

    pause 1.5

    narrator "Hampir."

    pause 2.0

    narrator "Dia tidak telefon sesiapa."

    pause 1.0

    narrator "Dia tidak tengok berita."

    pause 1.0

    narrator "Dia buat kerja."

    pause 1.0

    narrator "Dia tidur."

    pause 1.0

    narrator "Dia makan."

    pause 2.0

    narrator "Setiap hari yang berlalu membuatkan ia terasa lebih mudah untuk percaya."

    pause 1.5

    narrator "Bahawa ia okay."

    pause 1.5

    narrator "Bahawa ia akan okay."

    pause 2.0

    narrator "Hari ni dia nak keluar."
    narrator "Benda biasa."

    pause 1.5

    jump abandon_scene3

label abandon_scene3:

    scene bg_petrol_station
    with dissolve

    # TODO audio: play amb_petrol_station on ambient channel fadein 2.0

    show spr_mc neutral at center
    with dissolve

    narrator "Dia berhenti di stesen minyak."

    pause 1.0

    narrator "Benda biasa."

    pause 2.0

    narrator "Dia nampak akhbar."

    pause 1.0

    narrator "Secara tak sengaja."

    pause 1.5

    show text "KAMPUNG BATU LAYAR MUSNAH\nSEMUA PENDUDUK HILANG / MATI\nPolis Buntu. Tiada Penjelasan." with fade
    pause 4.0
    hide text with fade

    show spr_mc still at center
    with dissolve

    pause 3.0

    narrator "Dia ambil akhbar tu."

    # TODO audio: play sfx_newspaper_pick_up volume 0.3

    pause 1.0

    narrator "Dia baca."

    pause 3.0

    narrator "Dia baca lagi."

    pause 2.0

    narrator "Tangannya bergetar."

    pause 2.0

    narrator "Dia fikir tentang keputusan yang dia buat."

    pause 1.0

    narrator "Keputusan yang betul."

    pause 1.5

    narrator "Benda tu terlampau kuat."

    pause 1.0

    narrator "Kerja dia bukan untuk mati kat sana."

    pause 2.0

    narrator "Dia keluar dari kedai tu."

    pause 1.5

    narrator "Dia duduk dalam kereta."

    pause 2.0

    narrator "Telefon dia ada dalam tangan."

    pause 1.5

    narrator "Dia tengok nombor Melur."

    pause 2.0

    narrator "Dia tekan call."

    jump abandon_scene4

label abandon_scene4:

    # TODO audio: play sfx_phone_ring volume 0.6

    pause 1.0

    narrator "Telefon berbunyi."

    pause 2.0

    narrator "Sekali."

    pause 1.5

    narrator "Dua kali."

    pause 1.5

    narrator "Tiga kali."

    pause 1.5

    # TODO audio: play sfx_phone_static volume 0.3

    pause 1.0

    melur "..."
    melur "Encik..."

    pause 1.0

    mc "Melur. Melur dengar tak-"

    melur "Encik dah-"

    pause 1.5

    melur "Encik dah pergi kan."

    pause 5.0

    melur "Takpe."

    pause 2.0

    # TODO audio: play sfx_pocong_cry_phone volume 0.4

    pause 3.5

    # TODO audio: play sfx_call_end volume 0.6
    # TODO audio: stop sound fadeout 0.3

    pause 1.0

    stop ambient fadeout 1.0

    pause 4.0

    narrator "Talian terputus."

    pause 3.0

    narrator "Dia duduk."

    pause 2.0

    narrator "Telefon masih dalam tangan dia."

    pause 2.0

    narrator "Dia terdiam."

    pause 3.0

    jump abandon_scene5

label abandon_scene5:

    scene black
    with fade

    pause 3.0

    narrator "Kampung Nelayan Batu Layar."

    pause 2.0

    narrator "Semua penduduk hilang atau mati."

    pause 2.0

    narrator "Tiada penjelasan."

    pause 3.0

    narrator "Dia tahu penjelasannya."

    pause 2.0

    narrator "Dia satu-satunya orang yang tahu."

    pause 2.0

    narrator "Dan dia tidak ada kat sana."

    pause 9.0

    return
