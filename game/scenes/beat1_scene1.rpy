label beat1_scene1:

    # BEAT 1 - SCENE 1: Cold Open (Village)
    # Bayangan yang Tertinggal - The Shadow Left Behind
    #
    # Placeholder assets are used in this pass. Do not enable audio playback
    # until the matching files exist in game/audio/.

    # POCONG AUDIO SYSTEM
    #
    # Layer 1 - Theme music:
    # TODO audio: mus_pocong_theme
    # Soft traditional Malay spirit music when the Pocong is near but unseen.
    #
    # Layer 2 - Presence signals:
    # TODO audio: sfx_pocong_hop
    # TODO audio: sfx_pocong_cry
    # Heavy rhythmic hopping plus muffled weeping, hollow moan, and child-like tone.
    #
    # Layer 3 - Attack sound:
    # TODO audio: sfx_pocong_shriek
    # Attack only. Short, distorted, physically devastating shriek.

    # OPEN ON BLACK

    scene black
    with fade

    # Timestamp card. Silence. No music.
    show text "Kampung Nelayan Batu Layar\nPukul 2:47 pagi" with fade
    pause 3.0
    hide text with fade

    pause 1.0

    # THE VILLAGE PATH

    scene bg_village_path_night
    with fade

    # TODO audio: play amb_village_night fadein 2.5

    narrator "Malam tu, Kampung Batu Layar sunyi macam biasa."
    narrator "Angin laut bertiup perlahan. Lampu-lampu rumah dah lama padam."
    narrator "Semua orang tidur."

    pause 1.0

    narrator "Semua orang... kecuali Nayan."

    # NAYAN WALKS HOME

    scene bg_village_path_night
    show spr_nayan neutral at left
    with dissolve

    nayan "Aduh, lambatnya aku balik malam ni..."
    nayan "Abah kalau tau confirm kena bebel esok pagi."
    nayan "Nasib baik rumah dah dekat."

    narrator "Dia berjalan sorang-sorang."
    narrator "Macam banyak malam-malam sebelum ni."

    # THE FIRST WRONG THING
    # TODO audio: gradually lower amb_village_night over 4 seconds, then stop.

    pause 0.5
    pause 0.5

    show spr_nayan nervous at left
    with dissolve

    nayan "Eh..."

    narrator "Nayan berhenti."
    narrator "Tiba-tiba... sunyi."
    narrator "Bunyi-bunyi katak dah hilang. Cengkerik pun takde."

    nayan "Pelik la pulak..."
    nayan "Eh... kenapa senyap je tiba-tiba?"

    # POCONG THEME ENTERS
    # TODO audio: play mus_pocong_theme fadein 3.0 volume 0.2

    narrator "Angin berhenti."
    narrator "Dia pandang kiri. Pandang kanan."
    narrator "Jalan tu kosong."
    narrator "Dan dalam senyap tu..."
    narrator "...ada bunyi."

    pause 1.5

    # THE CRY
    # TODO audio: play sfx_pocong_cry volume 0.3

    show spr_nayan terrified at left
    with dissolve

    nayan "Bunyi... bunyi apa tu?"

    narrator "Macam orang menangis."
    narrator "Tapi lain. Macam suara tu datang dari balik sesuatu yang tebal."
    narrator "Macam ditahan."

    show spr_nayan terrified at left
    with flash

    nayan "Siapa tu?!"

    narrator "Takde jawapan."

    pause 1.0

    # THE THUMPING
    # TODO audio: play sfx_pocong_hop volume 0.4
    pause 2.0
    # TODO audio: play sfx_pocong_hop volume 0.55
    pause 2.0
    # TODO audio: play sfx_pocong_hop volume 0.7

    narrator "Dan lepas tu dia dengar."
    narrator "Duk."

    pause 1.5

    narrator "Duk."

    pause 1.5

    narrator "Duk."

    pause 1.0

    narrator "Sesuatu sedang melompat."
    narrator "Perlahan-perlahan. Ke arah dia."

    # NAYAN SEES IT
    # Do not show the Pocong directly yet. Suggest a white shape through narration only.

    narrator "Dia pusing."
    narrator "Dan dia nampak."

    pause 1.0

    narrator "Putih."

    pause 0.5

    narrator "Sesuatu yang putih."

    pause 0.5

    narrator "Berdiri jauh hujung jalan tu."

    pause 1.5

    narrator "Ia tidak bergerak."

    pause 1.0

    narrator "Tapi Nayan rasa... ia tengok dia."

    # TODO audio: raise mus_pocong_theme to 0.4 and play sfx_pocong_cry volume 0.5

    nayan "Ya... Ya Allah..."

    # TODO audio: sfx_pocong_hop now fires faster and louder.
    pause 1.2
    pause 1.2

    nayan "Lari- lari- kenapa kaki ni tak nak gerak."

    narrator "Kakinya beku."
    narrator "Mulutnya terbuka tapi suara tak keluar."

    # TODO audio: play sfx_pocong_hop volume 1.0
    pause 1.0

    narrator "Ia datang lagi dekat."

    # TODO audio: play sfx_pocong_hop volume 1.0
    pause 0.8

    narrator "Dekat lagi."

    # TODO audio: play sfx_pocong_hop volume 1.0
    pause 0.6

    narrator "Dan dekat lagi."

    # THE SHRIEK
    # TODO audio:
    # 1. Stop all music and ambience immediately.
    # 2. Hold one second of silence.
    # 3. Fire sfx_pocong_shriek at full volume.
    # 4. Pair with screen shake and a white flash.
    # 5. Cut to black and silence.

    stop music
    stop sound

    pause 1.0

    show effect_flash_white
    pause 0.3
    hide effect_flash_white

    scene black
    with flash

    pause 0.8

    # AFTERMATH
    # Black screen. Full silence.

    pause 2.0

    # TODO audio: play sfx_villager_scream volume 0.6
    pause 1.5
    # TODO audio: stop sfx_villager_scream fadeout 0.3

    pause 2.0

    narrator "Seseorang menjerit."

    pause 1.0

    narrator "Satu jeritan sahaja."
    narrator "Lepas tu senyap balik."

    pause 2.5

    # THE MORNING AFTER

    narrator "Pagi tu, orang kampung jumpa Nayan."

    pause 1.0

    narrator "Dia dah takde."

    pause 1.5

    narrator "Telinga dia berdarah."

    pause 1.0

    narrator "Dia bukan yang pertama."

    pause 1.0

    narrator "Dan semua orang tahu..."

    pause 1.0

    narrator "...dia bukan yang terakhir."

    pause 2.0

    # CHAPTER CARD

    show text "BAB SATU\nBayangan yang Tertinggal" with fade
    pause 3.5
    hide text with fade

    pause 1.5

    jump beat1_scene2
