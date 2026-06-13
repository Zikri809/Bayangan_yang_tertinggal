# Main entry point for the game.

label start:

    stop music fadeout 1.0

    jump adventure_start


label after_load:

    $ playing_ambient = renpy.music.get_playing(channel="ambient")
    if playing_ambient == audio.amb_village_morning_present:
        $ renpy.music.set_volume(1.0, delay=0.0, channel="ambient")

    elif playing_ambient == "audio/ambience/amb_village_morning_present.wav":
        $ renpy.music.set_volume(1.0, delay=0.0, channel="ambient")
        stop ambient fadeout 0.1
        play ambient audio.amb_village_morning_present fadein 0.1 volume adv_bg_ambient_volume

    return
