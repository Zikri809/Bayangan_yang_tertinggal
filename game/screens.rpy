################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")
    hover_sound "audio/sfx/ui_button_hover_satisfying.wav"
    activate_sound "audio/sfx/ui_button_select.ogg"

style gui_button:
    hover_sound "audio/sfx/ui_button_hover_satisfying.wav"
    activate_sound "audio/sfx/ui_button_select.ogg"

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound "audio/sfx/ui_button_hover_satisfying.wav"
    activate_sound "audio/sfx/ui_button_select.ogg"

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Adventure route screens #####################################################

screen adv_chapter_card(chapter, title, location, time_text, characters, mood, bg="bg_adv_chapter_card", card_xalign=0.5, card_xsize=1280, card_background="#111111dd"):
    modal True
    zorder 200

    add bg

    frame:
        xalign card_xalign
        yalign 0.5
        xsize card_xsize
        ysize 520
        background card_background
        padding (48, 42)

        vbox:
            spacing 20

            text chapter:
                size 34
                color "#b9b9b9"

            text title:
                size 58
                bold True
                color "#ffffff"

            hbox:
                spacing 60

                vbox:
                    spacing 8
                    text "Tempat" size 22 color "#8f8f8f"
                    text location size 28 color "#ffffff"

                vbox:
                    spacing 8
                    text "Masa" size 22 color "#8f8f8f"
                    text time_text size 28 color "#ffffff"

            text "Watak: [characters]":
                size 26
                color "#dddddd"
                xmaximum card_xsize - 96

            text mood:
                size 26
                color "#c8c8c8"
                xmaximum card_xsize - 96

            text "Klik atau tekan Space untuk teruskan":
                size 20
                color "#777777"
                xalign 0.0

    key "dismiss" action Return()
    key "K_SPACE" action Return()
    timer 2.5 action Return()


screen adv_inventory():
    zorder 90
    default expanded = False

    if expanded:
        mousearea:
            area (1460, 44, 430, 650)
            hovered SetScreenVariable("expanded", True)
            unhovered SetScreenVariable("expanded", False)
    else:
        mousearea:
            area (1798, 216, 104, 104)
            hovered SetScreenVariable("expanded", True)
            unhovered SetScreenVariable("expanded", False)

    button:
        xpos 1812
        ypos 230
        xsize 70
        ysize 70
        background "gui/adventure/backpack_button_bg.svg"
        hover_background "gui/adventure/backpack_button_bg_hover.svg"
        padding (12, 12)
        action ToggleScreenVariable("expanded")

        add "ui_adv_backpack_icon":
            xysize (46, 46)
            xalign 0.5
            yalign 0.5

    if len(adv_case_notes) > 0:
        frame:
            xpos 1858
            ypos 222
            xsize 28
            ysize 28
            background "#6e1f16ee"
            padding (0, 0)

            text "[len(adv_case_notes)]":
                size 16
                bold True
                color "#f8efe1"
                xalign 0.5
                yalign 0.5

    if expanded:
        frame:
            xpos 1480
            ypos 64
            xsize 390
            background "#111111ee"
            padding (20, 18)

            vbox:
                spacing 10
                text "Beg Siasatan" size 26 color "#ffffff" bold True

                for item in adv_inventory_items():
                    $ item_icon = adv_inventory_icon(item)
                    if item == "Buku Nota":
                        button:
                            xfill True
                            background "#24211fee"
                            hover_background "#3a3028ee"
                            padding (10, 8)
                            action Show("adv_case_notes")

                            hbox:
                                spacing 10
                                yalign 0.5

                                add item_icon:
                                    xysize (28, 28)
                                    yalign 0.5

                                text "Buku Nota / Nota Kes":
                                    size 20
                                    color "#f0eadc"
                                    yalign 0.5
                    else:
                        hbox:
                            spacing 10
                            yalign 0.5

                            if item_icon:
                                add item_icon:
                                    xysize (26, 26)
                                    yalign 0.5
                            else:
                                frame:
                                    xsize 26
                                    ysize 26
                                    background "#4d4d4d"

                            text item size 20 color "#d8d8d8" yalign 0.5

                if adv_case_notes:
                    null height 8
                    text "Nota Terkini" size 22 color "#ffffff" bold True
                    for note in adv_case_notes[-3:]:
                        text "- [note]" size 18 color "#c9c9c9" xmaximum 340
                else:
                    null height 8
                    text "Belum ada nota kes." size 18 color "#8f8f8f"


screen adv_case_notes():
    modal True
    zorder 180

    add Solid("#050403cc")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1040
        ysize 720
        background "#1b0f09f4"
        padding (18, 18)

        fixed:
            add "ui_adv_notebook_parchment":
                xysize (1004, 684)
                alpha 0.92

            add Solid("#2a160dcc"):
                xpos 34
                ypos 22
                xysize (10, 640)

            vbox:
                xpos 58
                ypos 36
                xsize 900
                spacing 18

                hbox:
                    xfill True
                    spacing 14

                    add "ui_adv_open_book_icon":
                        xysize (42, 42)
                        yalign 0.5

                    vbox:
                        yalign 0.5
                        spacing 1

                        text "Nota Kes":
                            size 34
                            color "#24150d"
                            bold True

                        text "Catatan siasatan dan petunjuk yang dijumpai." size 17 color "#5b402b"

                    null width 0 xfill True

                    textbutton "Tutup":
                        yalign 0.5
                        background "#2d1a10cc"
                        hover_background "#4a2c1acc"
                        padding (16, 8)
                        text_color "#f2dfbd"
                        text_hover_color "#ffffff"
                        action Hide("adv_case_notes")

                add Solid("#4b2d1a66"):
                    xsize 900
                    ysize 2

                if adv_case_notes:
                    viewport:
                        mousewheel True
                        draggable True
                        ymaximum 520

                        vbox:
                            spacing 10
                            for note in adv_case_notes:
                                frame:
                                    xfill True
                                    background "#f4dfb3cc"
                                    padding (18, 12)

                                    hbox:
                                        spacing 12

                                        text "-":
                                            size 23
                                            color "#6a4328"
                                            yalign 0.0

                                        text note:
                                            size 23
                                            color "#2d1c12"
                                            xmaximum 820
                else:
                    frame:
                        xfill True
                        background "#f4dfb3aa"
                        padding (18, 14)
                        text "Belum ada nota lagi." size 24 color "#4c3826"


screen adv_case_summary():
    modal True
    zorder 180

    add Solid("#050403dd")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1080
        background "#16120fee"
        padding (34, 30)

        vbox:
            spacing 18

            text "Semakan Nota Sebelum Malam":
                size 38
                color "#ffffff"
                bold True

            text adv_release_status_text():
                size 23
                color "#d8c6a8"
                xmaximum 990

            add Solid("#6a4a2f66"):
                xsize 990
                ysize 2

            for line in adv_case_summary_lines():
                frame:
                    xfill True
                    background "#241b15ee"
                    padding (16, 12)

                    text line:
                        size 23
                        color "#f0eadc"
                        xmaximum 940

            textbutton "Teruskan":
                xalign 1.0
                background "#5b241bee"
                hover_background "#7b3124ee"
                padding (18, 9)
                text_color "#f8efe1"
                text_hover_color "#ffffff"
                action Return()

    key "dismiss" action Return()
    key "K_SPACE" action Return()


screen adv_inspection(title, description, choices):
    modal True
    zorder 150

    add Solid("#00000099")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 980
        background "#1b1b1bee"
        padding (36, 30)

        vbox:
            spacing 18

            text title size 38 color "#ffffff" bold True
            text description size 24 color "#d8d8d8" xmaximum 900

            for caption, value in choices:
                textbutton caption:
                    xfill True
                    action Return(value)

            textbutton "Selesai":
                xfill True
                action Return("done")


screen adv_flashlight_search(title, description, hotspots, required=3):
    modal True
    zorder 150
    default found = []
    default beam_value = None
    default mouse_xy = (960, 540)

    add "bg_adv_grave_inspect"
    add Solid("#000000cc")
    timer 0.03 repeat True action SetScreenVariable("mouse_xy", renpy.get_mouse_pos())

    fixed:
        xysize (1920, 1080)

        add "gui/adventure/flashlight_beam.svg":
            xpos mouse_xy[0] - 260
            ypos mouse_xy[1] - 260
            xysize (520, 520)

        for caption, value, hx, hy, hw, hh, clue in hotspots:
            $ clue_alpha = 0.95 if value in found or beam_value == value else 0.16

            if value == "soil":
                add Crop((208, 326, 2463, 994), "images/assets/clue_uneven_soil.png.png"):
                    xpos hx - 72
                    ypos hy - 16
                    xysize (560, 228)
                    alpha clue_alpha

            elif value == "thread":
                add Crop((262, 404, 2181, 793), "images/assets/clue_white_thread.png.png"):
                    xpos hx - 42
                    ypos hy - 18
                    xysize (420, 244)
                    alpha clue_alpha

            elif value == "marker":
                add Crop((821, 149, 1080, 1296), "images/assets/clue_old_grave_marker.png.png"):
                    xpos hx + 48
                    ypos hy - 18
                    xysize (210, 302)
                    alpha clue_alpha

            if beam_value == value and value not in found:
                frame:
                    xpos hx
                    ypos hy - 46
                    xsize 280
                    background "#111111cc"
                    padding (10, 6)

                    text caption:
                        size 19
                        color "#f7e7c2"
                        xmaximum 260

            if value in found:
                frame:
                    xpos hx
                    ypos hy + hh + 8
                    xsize 360
                    background "#111111dd"
                    padding (12, 8)

                    text clue:
                        size 20
                        color "#f7e7c2"
                        xmaximum 336

            button:
                xpos hx
                ypos hy
                xysize (hw, hh)
                background "#00000000"
                hover_background "#00000000"
                hovered SetScreenVariable("beam_value", value)
                unhovered SetScreenVariable("beam_value", None)
                action If(value in found, NullAction(), [SetScreenVariable("found", found + [value]), SetScreenVariable("beam_value", value)])

    frame:
        xpos 70
        ypos 58
        xsize 700
        background "#111111dd"
        padding (24, 20)

        vbox:
            spacing 8

            text title:
                size 36
                color "#ffffff"
                bold True

            text description:
                size 22
                color "#d8c6a8"
                xmaximum 640

            text "Petunjuk ditemui: [len(found)]/[required]":
                size 22
                color "#f2dfbd"

    if len(found) >= required:
        textbutton "Selesai":
            xpos 1540
            ypos 900
            xsize 260
            background "#5b241bee"
            hover_background "#7b3124ee"
            padding (18, 12)
            text_color "#f8efe1"
            text_hover_color "#ffffff"
            action Return(found)


screen adv_timed_choice(prompt, choices, timeout_value="timeout", seconds=12):
    modal True
    zorder 150
    default time_left = seconds

    add Solid("#00000099")
    add "gui/horror_ui/timed_choice_overlay.svg"
    timer 1.0 repeat True action If(time_left > 1, SetScreenVariable("time_left", time_left - 1), Return(timeout_value))

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1020
        background "#151515ee"
        padding (38, 32)

        vbox:
            spacing 18

            text prompt size 32 color "#ffffff" bold True xmaximum 930
            text "Masa tinggal: [time_left] saat" size 22 color "#d8c6a8"

            for caption, value in choices:
                textbutton caption:
                    xfill True
                    action Return(value)


screen adv_stillness(prompt, beats=4):
    modal True
    zorder 160
    default prep_left = 5
    default started = False
    default beat_pos = 0
    default hits = 0
    default beat_locked = False
    default zone_center = renpy.random.randint(28, 72)
    $ in_window = beat_pos >= zone_center - 8 and beat_pos <= zone_center + 8

    add Solid("#000000dd")
    add "gui/horror_ui/timed_choice_overlay.svg"

    if started:
        timer 0.05 repeat True action If(beat_pos >= 100, [SetScreenVariable("beat_pos", 0), SetScreenVariable("beat_locked", False), SetScreenVariable("zone_center", renpy.random.randint(28, 72))], SetScreenVariable("beat_pos", beat_pos + 4))
    else:
        timer 1.0 repeat True action If(prep_left > 1, SetScreenVariable("prep_left", prep_left - 1), [SetScreenVariable("started", True), SetScreenVariable("beat_pos", 0), SetScreenVariable("beat_locked", False), SetScreenVariable("zone_center", renpy.random.randint(28, 72))])

    key "K_SPACE" action If(started, [Play("sound", "audio/sfx/sfx_rhythm_tap_horror_loud.wav"), If(in_window and not beat_locked, If(hits + 1 >= beats, Return("still"), [SetScreenVariable("hits", hits + 1), SetScreenVariable("beat_locked", True)]), Return("moved"))], NullAction())
    key "K_RETURN" action If(started, Return("moved"), NullAction())
    key "K_KP_ENTER" action If(started, Return("moved"), NullAction())
    key "K_ESCAPE" action If(started, Return("moved"), NullAction())
    key "K_PAGEUP" action If(started, Return("moved"), NullAction())
    key "K_PAGEDOWN" action If(started, Return("moved"), NullAction())
    key "mouseup_1" action If(started, Return("moved"), NullAction())
    key "mouseup_2" action If(started, Return("moved"), NullAction())
    key "mouseup_3" action If(started, Return("moved"), NullAction())

    frame:
        xalign 0.5
        yalign 0.5
        xsize 960
        background "#111111ee"
        padding (42, 36)

        vbox:
            spacing 16

            text prompt:
                size 34
                color "#ffffff"
                bold True
                xmaximum 860

            text "Bila rentak mula, tekan Space tepat masa duk sampai. Tunggu kalau belum yakin. Salah tekan atau klik mouse akan buat Aris tersentak.":
                size 25
                color "#f2dfbd"
                xmaximum 860

            if not started:
                text "Bersedia. Rentak mula dalam [prep_left]...":
                    size 34
                    color "#f2dfbd"
                    bold True
                    xalign 0.5

                text "Letak jari dekat Space. Jangan tekan dulu.":
                    size 24
                    color "#b9b9b9"
                    xalign 0.5

            else:
                fixed:
                    xsize 760
                    ysize 86
                    xalign 0.5

                    add Solid("#26211dcc"):
                        xpos 0
                        ypos 34
                        xysize (760, 18)

                    add Solid("#7b312466"):
                        xpos int(zone_center * 7.2) - 61
                        ypos 20
                        xysize (122, 46)

                    add Solid("#f2dfbd"):
                        xpos int(beat_pos * 7.2)
                        ypos 14
                        xysize (18, 58)

                hbox:
                    xalign 0.5
                    spacing 18

                    text "Rentak kena: [hits]/[beats]":
                        size 24
                        color "#b9b9b9"

                    if in_window and not beat_locked:
                        text "DUK":
                            size 24
                            color "#f2dfbd"
                            bold True
                    elif beat_locked:
                        text "diam...":
                            size 24
                            color "#8f8f8f"
                    else:
                        text "jeda...":
                            size 24
                            color "#8f8f8f"


transform adv_phone_vibrate:
    pause 0.05
    linear 0.045 xoffset -6 yoffset 2
    linear 0.045 xoffset 6 yoffset -2
    linear 0.045 xoffset -4 yoffset -1
    linear 0.045 xoffset 4 yoffset 1
    linear 0.045 xoffset -6 yoffset 2
    linear 0.045 xoffset 6 yoffset -2
    linear 0.045 xoffset -4 yoffset -1
    linear 0.045 xoffset 4 yoffset 1
    linear 0.045 xoffset -6 yoffset 2
    linear 0.045 xoffset 6 yoffset -2
    linear 0.045 xoffset -4 yoffset -1
    linear 0.045 xoffset 4 yoffset 1
    linear 0.045 xoffset -6 yoffset 2
    linear 0.045 xoffset 6 yoffset -2
    linear 0.045 xoffset -4 yoffset -1
    linear 0.045 xoffset 4 yoffset 1
    linear 0.045 xoffset -6 yoffset 2
    linear 0.045 xoffset 6 yoffset -2
    linear 0.045 xoffset -4 yoffset -1
    linear 0.045 xoffset 4 yoffset 1
    linear 0.045 xoffset -6 yoffset 2
    linear 0.045 xoffset 6 yoffset -2
    linear 0.045 xoffset -4 yoffset -1
    linear 0.045 xoffset 4 yoffset 1
    linear 0.07 xoffset 0 yoffset 0
    pause 1.1
    linear 0.045 xoffset -5 yoffset 2
    linear 0.045 xoffset 5 yoffset -2
    linear 0.045 xoffset -3 yoffset -1
    linear 0.045 xoffset 3 yoffset 1
    linear 0.045 xoffset -5 yoffset 2
    linear 0.045 xoffset 5 yoffset -2
    linear 0.045 xoffset -3 yoffset -1
    linear 0.045 xoffset 3 yoffset 1
    linear 0.045 xoffset -5 yoffset 2
    linear 0.045 xoffset 5 yoffset -2
    linear 0.045 xoffset -3 yoffset -1
    linear 0.045 xoffset 3 yoffset 1
    linear 0.045 xoffset -5 yoffset 2
    linear 0.045 xoffset 5 yoffset -2
    linear 0.045 xoffset -3 yoffset -1
    linear 0.045 xoffset 3 yoffset 1
    linear 0.045 xoffset -5 yoffset 2
    linear 0.045 xoffset 5 yoffset -2
    linear 0.045 xoffset -3 yoffset -1
    linear 0.045 xoffset 3 yoffset 1
    linear 0.045 xoffset -5 yoffset 2
    linear 0.045 xoffset 5 yoffset -2
    linear 0.045 xoffset -3 yoffset -1
    linear 0.045 xoffset 3 yoffset 1
    linear 0.045 xoffset -5 yoffset 2
    linear 0.045 xoffset 5 yoffset -2
    linear 0.045 xoffset -3 yoffset -1
    linear 0.045 xoffset 3 yoffset 1
    linear 0.14 xoffset 0 yoffset 0
    pause 0.85
    linear 0.045 xoffset -6 yoffset 2
    linear 0.045 xoffset 6 yoffset -2
    linear 0.045 xoffset -4 yoffset -1
    linear 0.045 xoffset 4 yoffset 1
    linear 0.045 xoffset -6 yoffset 2
    linear 0.045 xoffset 6 yoffset -2
    linear 0.045 xoffset -4 yoffset -1
    linear 0.045 xoffset 4 yoffset 1
    linear 0.045 xoffset -6 yoffset 2
    linear 0.045 xoffset 6 yoffset -2
    linear 0.045 xoffset -4 yoffset -1
    linear 0.045 xoffset 4 yoffset 1
    linear 0.045 xoffset -6 yoffset 2
    linear 0.045 xoffset 6 yoffset -2
    linear 0.045 xoffset -4 yoffset -1
    linear 0.045 xoffset 4 yoffset 1
    linear 0.045 xoffset -6 yoffset 2
    linear 0.045 xoffset 6 yoffset -2
    linear 0.045 xoffset -4 yoffset -1
    linear 0.045 xoffset 4 yoffset 1
    linear 0.045 xoffset -6 yoffset 2
    linear 0.045 xoffset 6 yoffset -2
    linear 0.045 xoffset -4 yoffset -1
    linear 0.045 xoffset 4 yoffset 1
    linear 0.045 xoffset -6 yoffset 2
    linear 0.045 xoffset 6 yoffset -2
    linear 0.045 xoffset -4 yoffset -1
    linear 0.045 xoffset 4 yoffset 1
    linear 0.19 xoffset 0 yoffset 0
    pause 1.18
    repeat


screen adv_incoming_call(caller="Melur"):
    modal True
    zorder 190

    add Solid("#00000099")

    button:
        at adv_phone_vibrate
        xalign 0.5
        yalign 0.46
        xysize (420, 420)
        background None
        hover_background None
        padding (0, 0)
        action Return("answer")

        fixed:
            add "gui/adventure/phone_call_glow.svg"

            add "gui/adventure/phone_icon.svg":
                xalign 0.5
                yalign 0.5
                zoom 0.92


screen adv_phone_call_overlay():
    zorder -1

    add "gui/adventure/phone_call_line_left.svg":
        xpos 700
        ypos 370

    add "gui/adventure/phone_call_line_right.svg":
        xpos 1000
        ypos 370

    add "gui/adventure/phone_icon.svg":
        xalign 0.5
        ypos 400
        zoom 0.78


screen adv_ending_report(title, subtitle):
    modal True
    zorder 220

    if "DILEPASKAN" in title:
        add "bg_ending_released"
    elif "DITINGGALKAN" in title:
        add "bg_ending_abandoned"
    elif "TERKUBUR" in title:
        add "bg_ending_buried"
    elif "TIDAK FAHAM" in title:
        add "bg_ending_ignorance"
    else:
        add Solid("#050403")

    add Solid("#050403bb")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1040
        background "#120f0dee"
        padding (38, 34)

        vbox:
            spacing 18

            text title:
                size 44
                color "#ffffff"
                bold True

            text subtitle:
                size 24
                color "#d8c6a8"
                xmaximum 950

            add Solid("#6a4a2f66"):
                xsize 950
                ysize 2

            text "Ringkasan siasatan":
                size 28
                color "#ffffff"
                bold True

            for line in adv_ending_report_lines():
                text line:
                    size 23
                    color "#f0eadc"
                    xmaximum 940

            textbutton "Selesai":
                xalign 1.0
                background "#5b241bee"
                hover_background "#7b3124ee"
                padding (18, 9)
                text_color "#f8efe1"
                text_hover_color "#ffffff"
                action Return()

    key "dismiss" action Return()
    key "K_SPACE" action Return()

screen adv_credits_roll():
    modal True
    zorder 230

    add Solid("#050403")

    vbox:
        xalign 0.5
        ypos 0.5
        yanchor 0.0
        spacing 26
        at adv_credits_scroll

        text "Bayangan yang Tertinggal":
            xalign 0.5
            size 50
            color "#ffffff"
            bold True

        text "A Malay horror visual novel prototype":
            xalign 0.5
            size 28
            color "#d8c6a8"

        null height 30

        text "Creative Director":
            xalign 0.5
            size 28
            color "#f0eadc"

        text "Naszrul":
            xalign 0.5
            size 34
            color "#ffffff"
            bold True

        null height 22

        text "Developer & Level Design":
            xalign 0.5
            size 28
            color "#f0eadc"

        text "Zikri":
            xalign 0.5
            size 34
            color "#ffffff"
            bold True

        null height 22

        text "UI/UX":
            xalign 0.5
            size 28
            color "#f0eadc"

        text "Syabil & Haziq":
            xalign 0.5
            size 34
            color "#ffffff"
            bold True

        null height 22

        text "Documentation & Testing":
            xalign 0.5
            size 28
            color "#f0eadc"

        text "Syauqi":
            xalign 0.5
            size 34
            color "#ffffff"
            bold True

        null height 36

        text "Created for Interaction System Tools":
            xalign 0.5
            size 24
            color "#d8c6a8"

        null height 36

        text "Built With":
            xalign 0.5
            size 28
            color "#f0eadc"

        text "Ren'Py":
            xalign 0.5
            size 34
            color "#ffffff"
            bold True

        null height 22

        text "Tools Used":
            xalign 0.5
            size 28
            color "#f0eadc"

        text "VS Code & Figma":
            xalign 0.5
            size 34
            color "#ffffff"
            bold True

        null height 36

        text "Character & Asset Generation":
            xalign 0.5
            size 28
            color "#f0eadc"

        text "PixAI":
            xalign 0.5
            size 34
            color "#ffffff"
            bold True

        text "https://pixai.art/en":
            xalign 0.5
            size 22
            color "#d8c6a8"

        null height 36

        text "Audio / Sound Assets":
            xalign 0.5
            size 28
            color "#f0eadc"

        text "We Love Indies":
            xalign 0.5
            size 34
            color "#ffffff"
            bold True

        text "https://www.weloveindies.com/en/sounds-for-games":
            xalign 0.5
            size 22
            color "#d8c6a8"

        null height 42

        text "Thank you for playing":
            xalign 0.5
            size 34
            color "#ffffff"
            bold True

    timer 62.5 action Return()
    key "dismiss" action Return()
    key "K_SPACE" action Return()


transform adv_credits_scroll:
    yoffset 0
    linear 62.0 yoffset -2200


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        frame:
            style "quick_menu_frame"

            hbox:
                style_prefix "quick"
                style "quick_menu"

                textbutton _("Back") action Rollback()
                textbutton _("History") action ShowMenu('history')
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Save") action ShowMenu('save')
                textbutton _("Q.Save") action QuickSave()
                textbutton _("Q.Load") action QuickLoad()
                textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_menu_frame is frame
style quick_button is default
style quick_button_text is button_text

style quick_menu_frame:
    xalign 0.5
    yalign 1.0
    yoffset -34
    background "#05050599"
    padding (18, 2)

style quick_menu:
    xalign 0.5
    yalign 1.0
    spacing 14

style quick_button:
    properties gui.button_properties("quick_button")
    background None
    hover_background None
    padding (0, 0)
    hover_sound "audio/sfx/ui_button_hover_satisfying.wav"
    activate_sound "audio/sfx/ui_button_select.ogg"

style quick_button_text:
    properties gui.text_properties("quick_button")
    color "#9f9f9f"
    hover_color "#ffffff"
    selected_color "#ffffff"
    outlines [(1, "#000000dd", 0, 0)]


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound "audio/sfx/ui_button_hover_satisfying.wav"
    activate_sound "audio/sfx/ui_button_select.ogg"

style navigation_button_text:
    properties gui.text_properties("navigation_button")
    color "#d8d8d8"
    hover_color "#ffffff"
    selected_color "#ffffff"
    insensitive_color "#777777"
    outlines [(2, "#000000cc", 0, 0)]


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background at main_menu_background_drift
    add "gui/main_menu_fog.png" at main_menu_fog_drift
    add "gui/main_menu_bw_flicker.png" at main_menu_bw_flicker
    add Solid("#ffffff") at main_menu_exposure_pulse
    add Solid("#000000") at main_menu_dark_flicker

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    if gui.show_name:
        add "gui/main_menu_title.png" at main_menu_title_idle

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "#00000099"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
    color "#ffffff"
    outlines [(2, "#000000dd", 0, 0)]

style main_menu_title:
    properties gui.text_properties("title")
    color "#ffffff"
    outlines [(3, "#000000dd", 0, 0)]

style main_menu_version:
    properties gui.text_properties("version")
    color "#bdbdbd"
    outlines [(2, "#000000dd", 0, 0)]


transform main_menu_background_drift:
    subpixel True
    xysize (1984, 1116)
    xalign 0.5
    yalign 0.5
    xoffset -18
    yoffset -8
    ease 12.0 xoffset 18 yoffset 8
    ease 14.0 xoffset -18 yoffset -8
    repeat


transform main_menu_fog_drift:
    subpixel True
    alpha 0.24
    xpos -190
    ypos 0
    linear 18.0 xpos -25 alpha 0.34
    linear 20.0 xpos -190 alpha 0.24
    repeat


transform main_menu_title_idle:
    subpixel True
    xalign 1.0
    yalign 1.0
    xoffset -48
    yoffset -48
    zoom 0.86
    alpha 0.92
    pause 1.65
    linear 0.05 alpha 0.72
    linear 0.08 alpha 0.96
    pause 2.75
    linear 0.04 alpha 0.82
    linear 0.06 alpha 0.94
    repeat


transform main_menu_bw_flicker:
    alpha 0.04
    pause 1.15
    linear 0.06 alpha 0.20
    linear 0.08 alpha 0.04
    pause 0.18
    linear 0.03 alpha 0.16
    linear 0.05 alpha 0.06
    pause 2.10
    repeat


transform main_menu_exposure_pulse:
    alpha 0.0
    pause 2.40
    linear 0.18 alpha 0.035
    linear 0.35 alpha 0.0
    pause 3.10
    linear 0.12 alpha 0.025
    linear 0.25 alpha 0.0
    repeat


transform main_menu_dark_flicker:
    alpha 0.0
    pause 1.55
    linear 0.04 alpha 0.10
    linear 0.08 alpha 0.0
    pause 0.27
    linear 0.03 alpha 0.06
    linear 0.04 alpha 0.0
    pause 2.30
    repeat


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background at main_menu_background_drift
        add "gui/main_menu_fog.png" at main_menu_fog_drift
        add "gui/main_menu_bw_flicker.png" at main_menu_bw_flicker
        add Solid("#ffffff") at main_menu_exposure_pulse
        add Solid("#000000") at main_menu_dark_flicker
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45
    hover_sound "audio/sfx/ui_button_hover_satisfying.wav"
    activate_sound "audio/sfx/ui_button_select.ogg"


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")
    hover_sound "audio/sfx/ui_button_hover_satisfying.wav"
    activate_sound "audio/sfx/ui_button_select.ogg"

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")
    hover_sound "audio/sfx/ui_button_hover_satisfying.wav"
    activate_sound "audio/sfx/ui_button_select.ogg"

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
    hover_sound "audio/sfx/ui_button_hover_satisfying.wav"
    activate_sound "audio/sfx/ui_button_select.ogg"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    hover_sound "audio/sfx/ui_button_hover_satisfying.wav"
    activate_sound "audio/sfx/ui_button_select.ogg"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15
    hover_sound "audio/sfx/ui_button_hover_satisfying.wav"
    activate_sound "audio/sfx/ui_button_select.ogg"

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12
    hover_sound "audio/sfx/ui_button_hover_satisfying.wav"
    activate_sound "audio/sfx/ui_button_select.ogg"

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound "audio/sfx/ui_button_hover_satisfying.wav"
    activate_sound "audio/sfx/ui_button_select.ogg"

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "?" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "?" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "?" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Solid(gui.muted_color)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign
    hover_sound "audio/sfx/ui_button_hover_satisfying.wav"
    activate_sound "audio/sfx/ui_button_select.ogg"

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
