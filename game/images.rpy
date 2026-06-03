# Image aliases.
#
# Replace these placeholders with real files as your art comes in.

image bg_village_path_night = Solid("#080a0d")
image bg_village_road_night = Solid("#050608")
image bg_village_path_night_2 = Solid("#090b0f")
image bg_village_path_dawn = Solid("#2a3034")
image bg_car_interior_night = Solid("#0b0d10")
image bg_village_path_day = Solid("#59665b")
image bg_village_house_ext = Solid("#4f5a50")
image bg_village_centre = Solid("#626257")
image bg_fight_site = Solid("#1e2920")
image bg_burial_ground = Solid("#30352f")
image bg_family_house_ext = Solid("#3b342c")
image bg_family_house_int = Solid("#241f1a")
image bg_road_leaving = Solid("#252b24")
image bg_mc_city_apartment = Solid("#303239")
image bg_petrol_station = Solid("#4a4a42")
image bg_nayan_house_inside = Solid("#101010")
image bg_old_restaurant_day = Solid("#2a2118")
image bg_old_restaurant_evening = Solid("#241811")

image bg_adv_chapter_card = Solid("#080809")
image bg_adv_restaurant = Solid("#2a2118")
image bg_adv_village_gate = Solid("#11151a")
image bg_adv_mak_ros_house = Solid("#343a35")
image bg_adv_grave_inspect = Solid("#252923")
image bg_adv_old_house = Solid("#1c1815")
image bg_adv_preparation = Solid("#121416")
image bg_adv_final_grave = Solid("#10130f")

image item_flashlight = Solid("#777777", xysize=(120, 70))
image item_camera = Solid("#6c6c6c", xysize=(120, 70))
image item_keris = "gui/adventure/inventory_icons/sword.png"
image item_thread = Solid("#bbbbbb", xysize=(120, 70))
image item_letter = Solid("#aaa090", xysize=(120, 70))
image item_tasbih = Solid("#77706a", xysize=(120, 70))
image item_salt = Solid("#dadada", xysize=(120, 70))

image ui_adv_notebook_icon = "gui/adventure/book_icons/32x32/notebook_01.png"
image ui_adv_open_book_icon = "gui/adventure/book_icons/32x32/open_book_01.png"
image ui_adv_notebook_parchment = "gui/adventure/notebook_parchment.jpg"
image ui_adv_backpack_icon = "gui/adventure/backpack_icon.svg"

image spr_mc neutral = Transform("images/characters/mc/mc_default_transparent.png", zoom=0.36)
image spr_mc listening = Transform("images/characters/mc/mc_default_transparent.png", zoom=0.36)
image spr_mc thinking = Transform("images/characters/mc/mc_default_transparent.png", zoom=0.36)
image spr_mc alert = Transform("images/characters/mc/mc_scared_transparent.png", zoom=0.36)
image spr_mc focused = Transform("images/characters/mc/mc_determined_transparent.png", zoom=0.36)
image spr_mc angry = Transform("images/characters/mc/mc_angry_transparent.png", zoom=0.36)
image spr_mc determined = Transform("images/characters/mc/mc_determined_transparent.png", zoom=0.36)
image spr_mc shaken = Transform("images/characters/mc/mc_scared_transparent.png", zoom=0.36)
image spr_mc injured = Transform("images/characters/mc/mc_injured_transparent.png", zoom=0.36)
image spr_mc deaf = Transform("images/characters/mc/mc_injured_transparent.png", zoom=0.36)
image spr_mc scared = Transform("images/characters/mc/mc_scared_transparent.png", zoom=0.36)
image spr_mc still = Transform("images/characters/mc/mc_injured_transparent.png", zoom=0.36)
image spr_nayan neutral = Transform("images/characters/nayan/nayan_default.png", zoom=0.36)
image spr_nayan terrified = Transform("images/characters/nayan/nayan_terrified.png", zoom=0.36)
image spr_hafiz neutral = Transform("images/characters/hafiz/hafiz_neutral.png", zoom=0.72)
image spr_melur phone = Transform("images/characters/melur/melur_phone.png", zoom=0.56)
image spr_owner serious = Transform("images/characters/zulkifli/zulkifli_serious.png", zoom=0.64)
image spr_villager_1 terrified = Placeholder("boy")
image spr_mak_ros nervous = Transform("images/characters/mak_ros/mak_ros_nervous.png", zoom=0.64)
image spr_mother neutral = Placeholder("girl")
image spr_pocong present = Placeholder("boy")
image spr_pocong stilled = Placeholder("boy")
image effect_flash_white = Solid("#ffffff")

define flash = Fade(0.1, 0.0, 0.3, color="#ffffff")

transform adv_left:
    xalign 0.28
    yalign 1.0

transform adv_right:
    xalign 0.72
    yalign 1.0

transform adv_trio_left:
    xalign 0.18
    yalign 1.0

transform adv_trio_center:
    xalign 0.50
    yalign 1.0

transform adv_trio_right:
    xalign 0.82
    yalign 1.0

transform adv_phone_left:
    xalign 0.25
    yalign 1.0

transform adv_phone_right:
    xalign 0.75
    yalign 1.0
