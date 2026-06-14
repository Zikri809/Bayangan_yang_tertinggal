# Audio aliases for the active adventure route.
#
# Keep these commented until the matching .ogg files exist.
# Current path:
# script.rpy -> adventure_start -> scenes/adventure_route.rpy

init python:
    renpy.music.register_channel("ambient", "sfx", loop=True)
    renpy.music.register_channel("rhythm", "sfx", loop=True)
    renpy.music.register_channel("earring", "sfx", loop=False)
    renpy.music.register_channel("camera", "sfx", loop=False)
    renpy.music.register_channel("creature", "sfx", loop=False)
    renpy.music.register_channel("cutting", "sfx", loop=False)
    renpy.music.register_channel("prayer", "sfx", loop=False)

# Shared ambience and music:
define audio.amb_nayan_night = "audio/ambience/amb_nayan_night.ogg"
define audio.amb_restaurant_crowd = "audio/ambience/amb_restaurant_crowd.ogg"
define audio.amb_village_morning = "audio/ambience/amb_village_morning.wav"
define audio.amb_village_morning_loud = "audio/ambience/amb_village_morning_loud.wav"
define audio.amb_village_morning_present = "audio/ambience/amb_village_morning_present_quiet.wav"
define audio.mus_credits = "audio/music/mus_credits.mp3"
define audio.mus_ending_positive = "audio/music/mus_ending_positive.mp3"
define audio.mus_ending_negative = "audio/music/mus_ending_negative.mp3"
define audio.mus_final_confrontation = "audio/music/mus_main_menu_try_to_survive.ogg"
define audio.mus_rhythm_game = "audio/music/mus_rhythm_game_16.wav"

# Background mix targets. Prologue and Chapter 1 use normal channel volume;
# later chapters should use these instead of one-off loud values.
define adv_bg_ambient_volume = 1.0
define adv_bg_music_volume = 0.45
define adv_bg_rhythm_volume = 0.75
# define audio.amb_village_night = "audio/ambience/amb_village_night.ogg"
# define audio.amb_village_day = "audio/ambience/amb_village_day.ogg"
# define audio.amb_restaurant_evening = "audio/ambience/amb_restaurant_evening.ogg"
# define audio.amb_family_house_int = "audio/ambience/amb_family_house_int.ogg"
# define audio.amb_burial_ground = "audio/ambience/amb_burial_ground.ogg"
# define audio.mus_pocong_theme = "audio/music/mus_pocong_theme.ogg"

# UI:
define audio.sfx_chapter_stinger = "audio/sfx/sfx_chapter_stinger.ogg"
define audio.sfx_clue_obtained = "audio/sfx/sfx_clue_obtained_loud.wav"
define audio.sfx_rhythm_tap_horror = "audio/sfx/sfx_rhythm_tap_horror_loud.wav"
define audio.ui_button_hover = "audio/sfx/ui_button_hover_satisfying.wav"
define audio.ui_button_select = "audio/sfx/ui_button_select.ogg"

# adv_prologue:
define audio.sfx_nayan_scream = "audio/sfx/sfx_nayan_scream.ogg"
define audio.sfx_nayan_scream_loud = "audio/sfx/sfx_nayan_scream_loud.wav"
# define audio.sfx_pocong_hop = "audio/sfx/sfx_pocong_hop.ogg"
define audio.sfx_pocong_cry = "audio/sfx/sfx_pocong_cry.mp3"
# define audio.sfx_pocong_shriek = "audio/sfx/sfx_pocong_shriek.ogg"

# adv_chapter1:
define audio.sfx_phone_ring = "audio/sfx/sfx_phone_ring.wav"

# adv_chapter2:
define audio.sfx_camera_shutter = "audio/sfx/sfx_camera_shutter.wav"
define audio.sfx_creature_scream = "audio/sfx/sfx_creature_scream.wav"
define audio.sfx_villager_scream = "audio/sfx/sfx_villager_scream_loud.wav"
define audio.sfx_ear_ringing = "audio/sfx/sfx_ear_ringing.mp3"
# define audio.sfx_distant_scream = "audio/sfx/sfx_distant_scream.ogg"
define audio.sfx_body_hit = "audio/sfx/sfx_body_hit_loud.wav"

# adv_burial_ground:
# define audio.sfx_thread_pull = "audio/sfx/sfx_thread_pull.ogg"

# adv_old_family_house:
define audio.sfx_door_open = "audio/sfx/sfx_door_open.wav"
define audio.sfx_flashlight_on = "audio/sfx/sfx_flashlight_on.wav"
define audio.sfx_item_grab = "audio/sfx/sfx_item_grab.wav"
define audio.sfx_paper_unfold = "audio/sfx/sfx_paper_unfold.wav"
# define audio.sfx_tasbih_beads = "audio/sfx/sfx_tasbih_beads.ogg"

# adv_chapter4:
define audio.sfx_keris_draw = "audio/sfx/sfx_keris_draw.wav"
define audio.sfx_prayer_low = "audio/sfx/sfx_prayer_low.ogg"
# define audio.sfx_salt_throw = "audio/sfx/sfx_salt_throw.ogg"

# adv_chapter5 and endings:
define audio.sfx_cloth_cut = "audio/sfx/sfx_cloth_cut.wav"
define audio.sfx_knot_pull = "audio/sfx/sfx_knot_pull.wav"
# define audio.sfx_keris_strike = "audio/sfx/sfx_keris_strike.ogg"
# define audio.sfx_arwah_cry_pain = "audio/sfx/sfx_arwah_cry_pain.ogg"
# define audio.sfx_arwah_final = "audio/sfx/sfx_arwah_final.ogg"
