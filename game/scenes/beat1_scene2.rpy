label beat1_scene2:

    # BEAT 1 - SCENE 2: The City (Old Restaurant)
    # Bayangan yang Tertinggal - The Shadow Left Behind
    #
    # This scene should contrast Scene 1: daylight, noise, warmth, and ordinary
    # surfaces carrying the horror the player already knows.

    # SCENE ASSETS NEEDED
    #
    # Background:
    # TODO art: bg_old_restaurant_day
    # Interior of Restoran Zulkifli. Old wooden furniture, ceiling fans, warm
    # daylight, worn surfaces, and half-visible hunter artefacts.
    #
    # Sprites:
    # TODO art: spr_mc neutral
    # TODO art: spr_hafiz neutral
    # TODO art: spr_hafiz amused
    #
    # Audio:
    # TODO audio: amb_restaurant_day
    # TODO audio: sfx_phone_ring

    # OPEN

    scene bg_old_restaurant_day
    with fade

    # TODO audio: play amb_restaurant_day on ambient channel fadein 2.0

    # Warm. Busy in the background. Life happening.
    # The MC is already here, seated, with a drink in front of him.

    show spr_mc neutral at right
    with dissolve

    narrator "Restoran Zulkifli."

    pause 1.0

    narrator "Dah lama tempat ni berdiri."
    narrator "Kerusi lama. Kipas lama. Menu lama."
    narrator "Tuan dia pun dah pencen - tapi dia tak pernah betul-betul pergi."

    pause 1.0

    narrator "Tempat macam ni tak ramai yang tahu."
    narrator "Yang tahu, biasanya kerja yang sama."

    # HAFIZ ARRIVES OR IS ALREADY THERE
    # Hafiz can already be seated across from MC, or he walks in and sits.
    # For this playable placeholder, he enters into the frame here.

    show spr_hafiz neutral at left
    with dissolve

    pause 0.8

    # He settles. Picks up his drink. Comfortable silence first.
    # These two do not need to fill every moment.

    pause 1.5

    # THE MENTION
    # Casual. Not a briefing. Not urgent.

    hafiz "Eh. Kau dengar tak pasal kampung nelayan tu?"
    mc "Mana?"

    hafiz "East coast. Jauh sikit. Entah nama apa."
    hafiz "Orang cerita ada beberapa kematian. Dua bulan ke belakang."
    hafiz "Tiga ke empat kes. Tak sure yang terakhir kira ke tak."

    # The MC does not react visibly. He listens.

    mc "Macam mana mati?"

    hafiz "Tu lah. Orang kampung tu tak mau cakap banyak."
    hafiz "Yang keluar cuma - ada sesuatu yang putih."
    hafiz "Dekat kawasan kubur. Melompat. Bukan jalan macam biasa."

    # A beat. Neither of them makes it dramatic.

    hafiz "Entahlah. Orang kampung cakap je kot."
    hafiz "Kau tahu lah. Kampung kecik. Musim tak elok."

    # MC says nothing. He turns this over quietly.

    hafiz "Tapi - putih. Melompat. Dekat kubur."

    show spr_hafiz amused at left
    with dissolve

    hafiz "Bunyi macam kau punya jenis lah."

    # THE MC SITS WITH IT
    # Hafiz jokes, mostly. The village stays at the back of MC's mind.

    narrator "Putih. Melompat. Dekat kubur."
    narrator "Dia simpan dalam kepala."

    pause 1.5

    # THE PHONE
    # Do not rush this. The timing should feel like coincidence. It is not.

    pause 2.0

    # TODO audio: play sfx_phone_ring volume 0.7
    pause 0.7

    narrator "Nombor tak dikenali."

    pause 0.5

    narrator "Kod kawasan. East coast."

    pause 1.5

    # He picks up.

    mc "Ya."

    # TRANSITION INTO SCENE 3
    # The sibling's voice comes through the line. We do not hear it yet.
    # Hold on MC's neutral expression, then move to the call scene.

    pause 1.5

    jump beat1_scene3
