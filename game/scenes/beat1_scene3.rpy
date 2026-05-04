label beat1_scene3:

    # BEAT 1 - SCENE 3: The Sibling's Call
    # Bayangan yang Tertinggal - The Shadow Left Behind
    #
    # Melur is voice only in this scene. No sprite should appear for her.
    # Her face is deliberately withheld.
    #
    # The MC says very little. He listens. This is his professional mode.
    # The scene belongs to Melur.

    # CONTINUOUS FROM SCENE 2
    # The MC has just answered. The restaurant ambience is still present in
    # story terms, but lower now. The world narrows to the phone.

    scene bg_old_restaurant_day
    show spr_mc listening at right
    with fade

    # TODO audio: fade amb_restaurant_day to 0.15 volume on ambient channel.
    # TODO audio: subtle sfx_phone_static under Melur's voice throughout call.

    pause 1.5

    melur "Encik yang selalu handle kes-kes... luar biasa?"

    # Careful. Testing the water before she commits.

    mc "Ya. Saya."

    pause 1.0

    melur "Saya dapat nombor encik daripada orang yang encik pernah tolong dulu."

    # She does not say who. The MC does not ask.
    # This is how referrals work in this world.

    mc "Okay. Ada apa?"

    # SHE TAKES A BREATH
    # She is deciding how to begin something she has rehearsed for a while.

    pause 2.0

    melur "Saya nak cakap pasal abang saya."

    pause 1.0

    melur "Dia dah lama meninggal."

    pause 0.5

    melur "Tapi... dia masih ada. Di sana."

    # A statement of fact. Delivered without drama.

    narrator "MC diam. Mendengar."

    melur "Kampung Nelayan Batu Layar."

    # This is the first time the village name is spoken aloud to the MC.

    melur "Encik mungkin tak pernah dengar."

    mc "Saya dengar nama tu hari ni."

    # A small beat. She did not expect that.

    melur "..."
    melur "Dah ada orang mati ke?"

    mc "Beberapa orang. Mengikut cerita yang saya dapat."

    pause 1.5

    melur "Saya minta maaf."

    # Not to the MC. To no one in particular.
    # Or to someone who is not on this call.

    mc "Ceritakan apa yang encik tahu."

    # MELUR BEGINS
    # She does not tell the full truth here. She gives the MC the shape of it:
    # enough to bring him there. The rest is for the village.

    melur "Abang saya... Kami dari kampung tu."
    melur "Dia meninggal lebih kurang dua puluh tahun lepas."
    melur "Keadaan dia meninggal... tidak baik."

    mc "Maksud Cik?"

    melur "Orang kampung tidak faham apa yang berlaku."
    melur "Mereka salah faham. Mereka marah."
    melur "Mereka salahkan keluarga kami."

    pause 1.0

    melur "Pengebumian abang saya... tergesa-gesa."

    pause 1.0

    melur "Saya terpaksa pergi lepas tu."

    # She did not choose to leave for a better life. The village made it
    # impossible to stay. This is expulsion, not abandonment.

    pause 2.0

    mc "Keluarga lain?"

    melur "Isteri abang saya... dah tiada."

    # She does not say how. The MC does not push.

    melur "Ibu kami masih hidup. Tua. Sorang-sorang."

    # "Ibu kami" - OUR mother. Melur left her own mother behind.

    melur "Anak abang saya... masih di kampung tu."

    # The Son's existence is seeded here, but not connected yet.

    mc "Dan encik sendiri?"

    melur "Saya terpaksa pergi. Dah lama."

    pause 1.5

    # WHY SHE IS CALLING NOW

    melur "Saya dengar pasal kematian-kematian tu."
    melur "Orang cakap ada pocong."
    melur "Dan mereka cakap ia berkaitan dengan keluarga kami."

    pause 1.0

    melur "Saya tahu ia abang saya."

    # Not a question. Not a theory. She knows.

    mc "Encik nak saya buat apa?"

    # THE ASK

    melur "Saya nak encik pergi ke sana."
    melur "Tengok apa yang berlaku."

    pause 1.0

    melur "Dan... tolong dia."

    # She has just asked a demon hunter to help a pocong.
    # She knows what that sounds like. She says it anyway.

    pause 2.5

    mc "Pocong tidak boleh diselamatkan."

    # The MC is honest. He does not soften it.

    melur "Saya tahu."

    pause 1.0

    melur "Tapi dia boleh... dilepaskan."

    pause 1.0

    melur "Biar dia pergi dengan betul."

    # KEY LINE - NEVER CHANGE:
    # "Biar dia pergi dengan betul."
    #
    # KEY LANGUAGE DISTINCTION - NEVER CHANGE:
    # "Dilepaskan" (released) vs "diselamatkan" (saved).
    # These are two different things.

    narrator "Bukan soal menang."
    narrator "Soal melepaskan."

    mc "Saya akan pergi tengok."

    # Not a promise. Not a guarantee. But he will go.

    melur "Terima kasih."

    # Two words. Held very still. There is a lifetime behind them.

    # THE CALL ENDS

    # TODO audio: play sfx_call_end volume 0.5
    pause 1.0

    # TODO audio: return amb_restaurant_day to 0.4 volume on ambient channel.
    # The restaurant returns slightly, but the MC is somewhere else now.

    show spr_mc neutral at right
    with dissolve

    narrator "Dia letak telefon."

    pause 1.0

    show spr_hafiz neutral at left
    with dissolve

    hafiz "Kerja ke?"

    mc "Ha."

    hafiz "Kampung tu?"

    # The MC does not answer. That is answer enough.

    hafiz "Hmm.."

    hide spr_hafiz
    with dissolve

    pause 2.0

    jump beat1_scene4
