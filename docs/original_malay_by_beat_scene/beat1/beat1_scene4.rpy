label beat1_scene4:

    # BEAT 1 - SCENE 4: The Folklore Discussion
    # Bayangan yang Tertinggal - The Shadow Left Behind
    #
    # The case is accepted. This scene is the inside of a trade: three people
    # comparing notes calmly before the MC enters something dangerous.

    # SCENE ASSETS NEEDED
    #
    # TODO art: bg_old_restaurant_day
    # TODO art: optional bg_old_restaurant_evening
    # TODO art: spr_mc neutral, thinking
    # TODO art: spr_hafiz neutral, curious, serious
    # TODO art: spr_owner neutral, serious, distant
    #
    # TODO audio: amb_restaurant_day
    # TODO audio: optional amb_restaurant_evening
    # TODO audio: sfx_cup_set_down

    scene bg_old_restaurant_day
    with dissolve

    # TODO audio: restore amb_restaurant_day to 0.4 volume on ambient channel.

    show spr_mc neutral at right
    show spr_hafiz neutral at left
    with dissolve

    pause 2.0

    # Abang Zulkifli comes from the back. Not summoned. He just appears at
    # the right time, with no particular reason given.

    show spr_owner neutral at center
    with dissolve

    owner "Nak tambah minum?"

    hafiz "Boleh, Abang Zul."

    # TODO audio: play sfx_cup_set_down volume 0.4
    pause 1.0

    # THE TOPIC OPENS

    hafiz "Pocong ke tadi?"

    mc "Nampaknya."

    hafiz "Mana?"

    mc "Kampung Nelayan Batu Layar."

    pause 1.0

    show spr_owner serious at center
    with dissolve

    owner "East coast."

    mc "Ha."

    pause 1.5

    # LORE POINT [3] - APPEARANCE

    show spr_hafiz curious at left
    with dissolve

    hafiz "Orang nampak dia melompat?"

    mc "Itulah cerita yang sampai kat saya."

    hafiz "Ha, memang macam tu lah."
    hafiz "Kaki dia terikat. Dalam kafan."
    hafiz "Sebab tu dia tak boleh jalan. Melompat je la."

    owner "Ada yang kata ia boleh terbang."

    hafiz "Ada jugak yang kata macam tu."

    owner "Bergantung siapa yang cerita."

    # LORE POINT [2] - KAFAN AND THE KNOT

    hafiz "Yang pasti - ia pakai kafan putih."
    hafiz "Kain tu ikat kat kepala, kat kaki."
    hafiz "Standard untuk pengebumian Islam."

    pause 0.5

    show spr_owner distant at center
    with dissolve

    owner "Tapi ada satu benda yang kena buat lepas pengebumian."
    owner "Simpulan tu kena dibuka."

    hafiz "Ha. Lepas dah dikebumikan."

    owner "Kalau tak dibuka-"

    # TODO audio: play sfx_cup_set_down volume 0.3
    pause 0.5

    owner "-roh dia tak lepas."

    pause 1.5

    # LORE POINT [1] - ORIGIN

    hafiz "Tu lah sebab dia jadi pocong."
    hafiz "Bukan sebab jahat. Bukan sebab dia nak kacau orang."
    hafiz "Terikat je. Tak boleh pergi mana-mana."

    show spr_mc thinking at right
    with dissolve

    mc "Simpulan yang tak pernah dibuka."

    hafiz "Ha."

    pause 1.0

    # LORE POINT [4] - BEHAVIOUR

    mc "Dia berkeliaran sebab apa?"

    hafiz "Berkait dengan tempat dia dikebumikan."
    hafiz "Atau tempat dia mati. Bergantung kes."

    owner "Ada yang cakap ia berkait dengan orang yang rapat dengan dia."
    owner "Yang ia rasa ada urusan yang belum selesai."

    owner "Bukan semua pocong sama."

    # Important: "Bukan semua pocong sama" is Abang Zulkifli's professional
    # knowledge. He has seen more than one.

    mc "Ini yang berkeliaran dah berapa lama?"

    hafiz "Kau tahu lagi baik dari kami."

    pause 1.5

    # LORE POINT [5] - MYTHS

    show spr_owner neutral at center
    with dissolve

    owner "Ada banyak cerita pasal pocong."
    owner "Yang saya dengar masa muda dulu-"
    owner "Orang tua cakap, kalau nampak pocong-"
    owner "-jangan lari."

    hafiz "Sebab dia lagi laju?"

    owner "Sebab kalau lari, dia akan kejar."
    owner "Tapi kalau berdiri diam, kadang-kadang ia berhenti jugak."
    owner "Kadang-kadang."

    hafiz "Air mengalir."

    owner "Ha?"

    hafiz "Orang kata pocong tak boleh lintasi air mengalir."

    owner "Ada yang percaya macam tu."
    owner "Saya tak pernah nak uji."

    hafiz "Ada yang kata ia akan datang balik ke tempat yang sama."
    hafiz "Tempat ia mati. Atau tempat ia dikebumikan."
    hafiz "Macam ada tali yang tarik dia balik."

    owner "Bukan tali."
    owner "Lebih kepada - tidak tahu nak pergi mana lagi."

    pause 2.0

    # KEY LINE - NEVER CHANGE:
    # "Tidak tahu nak pergi mana lagi."
    # This is the emotional definition of a pocong. Not evil. Just lost.

    # LORE POINT [6] - RESOLUTION

    mc "Cara nak lepaskan dia?"

    hafiz "Standard - buka simpulan kafan. Bacakan doa."
    hafiz "Bagi dia pergi dengan betul."

    # "Bagi dia pergi dengan betul" echoes Melur's words intentionally.

    mc "Kalau ia dah dalam keadaan kuat?"

    hafiz "Kena kerjakan dulu."
    hafiz "Lemahkan dia. Halang dia. Baru boleh buat upacara tu."

    owner "Ada pocong yang tak boleh dilepas dengan cara biasa."
    owner "Yang terlalu lama terikat."
    owner "Atau yang matinya - tidak tenang."
    owner "Itu kes yang lebih rumit."

    mc "Ha."

    pause 2.0

    # THE PLAYER CHOICE POINT

    menu:
        "\"Kalau pengebumian tergesa-gesa - ada bezanya?\"":
            jump beat1_scene4_ask_burial

        "\"Apa yang ia nak, sebenarnya?\"":
            jump beat1_scene4_ask_want

        "Diam. Simpan semua dalam kepala.":
            jump beat1_scene4_stay_quiet

label beat1_scene4_ask_burial:

    mc "Kalau pengebumian tergesa-gesa - ada bezanya?"

    hafiz "Beza besar."
    hafiz "Pengebumian Islam ada tertib dia. Ada urutan."
    hafiz "Kalau tergesa-gesa, banyak benda yang terlepas."

    owner "Simpulan tu salah satu."
    owner "Tapi bukan satu-satunya."
    owner "Doa yang tak habis. Niat yang tak betul."
    owner "Semua tu bagi kesan."

    hafiz "Kalau pengebumian tergesa-gesa sebab mereka nak cepat-"

    show spr_hafiz serious at left
    with dissolve

    hafiz "-sebab mereka marah, atau takut, atau malu-"
    hafiz "-itu lagi teruk."

    owner "Roh tu rasa."

    pause 1.5

    $ learned_rushed_burial = True

    jump beat1_scene4_converge

label beat1_scene4_ask_want:

    mc "Apa yang ia nak, sebenarnya?"

    hafiz "Bergantung pada pocong."
    hafiz "Ada yang cuma nak dilepaskan. Nak pergi."
    hafiz "Tak kisah pun pasal orang hidup."

    owner "Ada yang lain."

    show spr_owner distant at center
    with dissolve

    owner "Ada yang ada benda yang belum selesai."
    owner "Orang yang dia sayang. Tempat yang dia nak tengok."
    owner "Kesilapan yang tak sempat diperbetulkan."

    pause 1.0

    owner "Tapi ia tetap terikat. Walaupun ia ada kehendak."
    owner "Itu yang menyedihkan."

    hafiz "Nak buat apa pun tak boleh."
    hafiz "Sebab ia terikat."

    pause 1.5

    $ learned_pocong_want = True

    jump beat1_scene4_converge

label beat1_scene4_stay_quiet:

    narrator "Dia tak tanya apa-apa lagi."
    narrator "Cukup untuk sekarang."

    hafiz "Boleh handle sorang ke?"

    mc "Tengok dulu macam mana."

    pause 1.5

    jump beat1_scene4_converge

label beat1_scene4_converge:

    show spr_owner neutral at center
    with dissolve

    pause 1.0

    owner "Kau nak bertolak bila?"

    mc "Malam ni. Atau pagi esok."

    hafiz "Jauh. Bawak cukup-cukup."

    mc "Ha."

    pause 1.0

    show spr_owner serious at center
    with dissolve

    owner "Pocong yang lama - yang dah bertahun-tahun terikat-"
    owner "-ia bukan sekadar terikat secara fizikal."
    owner "Ada sesuatu yang berat dalam dirinya."

    pause 1.0

    owner "Kau kena faham benda tu dulu."
    owner "Baru boleh bagi ia pergi."

    # KEY LINE - NEVER CHANGE:
    # "Ada sesuatu yang berat dalam dirinya."
    # Abang Zulkifli's thematic close.

    hide spr_owner
    with dissolve

    pause 2.0

    # THE MC PREPARES TO LEAVE

    hafiz "Aku boleh drive sekali kalau kau nak."

    menu:
        "\"Tak payah. Aku pergi sorang.\"":
            jump beat1_scene4_go_alone

        "\"Boleh. Kau drive.\"":
            jump beat1_scene4_hafiz_drives

label beat1_scene4_go_alone:

    mc "Tak payah. Aku pergi sorang."

    hafiz "Okay."
    hafiz "Kalau ada apa-apa, call."

    mc "Ha."

    narrator "Dia keluar sorang."
    narrator "Macam biasa."

    $ mc_travels_alone = True

    jump beat1_scene4_end

label beat1_scene4_hafiz_drives:

    mc "Boleh. Kau drive."

    show spr_hafiz neutral at left
    with dissolve

    hafiz "Ha. Jom."

    narrator "Mereka keluar bersama."
    narrator "Hafiz tak tanya lebih. Itu pun cukup."

    $ hafiz_drives = True

    jump beat1_scene4_end

label beat1_scene4_end:

    scene black
    with fade

    pause 1.0

    show text "BAB DUA\nKampung Nelayan Batu Layar" with fade
    pause 3.5
    hide text with fade

    pause 1.5

    jump beat2_scene1
