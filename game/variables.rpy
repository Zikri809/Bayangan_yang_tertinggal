# Save-game variables.

default learned_rushed_burial = False
default learned_pocong_want = False
default mc_travels_alone = False
default hafiz_drives = False
default villager_2_safe = False
default b2_tried_wood = False
default b2_pak_zul_advice_used = False
default shriek_covered = False
default arm_injured = False
default arm_injured_severe = False
default mc_shaken = False
default villager_1_hurt = False
default fc_stood_ground = False
default learned_attack_detail = False
default learned_sound_detail = False
default learned_pocong_pattern = False
default found_bomoh_site = False
default devil_noted = False
default devil_thread_deepened = False
default devil_sample_taken = False
default learned_pact_partial = False
default found_burial_site = False
default son_mentioned_father = False
default found_mother = False
default mother_told_truth = False
default learned_pact = False
default learned_wife_fate = False
default abandoned = False
default mc_damage = 0
default mc_condition = ""
default mc_condition_b4 = ""
default b4_pattern_read = False
default b4_advantage = False
default b4_close_range = False
default b4_r3_clean = False
default b4_pocong_weakened = False

# Adventure route variables.

default adv_has_flashlight = True
default adv_has_camera = True
default adv_has_keris = True
default adv_has_kafan_thread = False
default adv_has_old_letter = False
default adv_has_tasbih = False
default adv_has_salt = False

default adv_understanding = 0
default adv_fear = 0
default adv_damage = 0
default adv_pocong_anger = 0
default adv_case_notes = []

default adv_observed_pattern = False
default adv_burial_clue = False
default adv_identity_clue = False
default adv_release_ready = False
default adv_aggressive_prepare = False
default adv_final_pattern_used = False
default adv_final_identity_used = False
default adv_final_release_used = False
default adv_final_force_used = False

default adv_mak_ros_done = False
default adv_burial_done = False
default adv_house_done = False

init python:
    def adv_add_note(note):
        if note not in adv_case_notes:
            adv_case_notes.append(note)
            renpy.notify("Nota kes ditambah: " + note)

    def adv_inventory_items():
        items = ["Buku Nota"]
        if adv_has_flashlight:
            items.append("Lampu suluh")
        if adv_has_camera:
            items.append("Kamera telefon")
        if adv_has_keris:
            items.append("Keris kecil")
        if adv_has_kafan_thread:
            items.append("Benang kafan")
        if adv_has_old_letter:
            items.append("Surat lama")
        if adv_has_tasbih:
            items.append("Tasbih")
        if adv_has_salt:
            items.append("Garam")
        return items

    def adv_inventory_icon(item):
        icons = {
            "Buku Nota": "gui/adventure/book_icons/32x32/notebook_01.png",
            "Lampu suluh": "gui/adventure/item_icons/flashlight.svg",
            "Kamera telefon": "gui/adventure/item_icons/camera.svg",
            "Keris kecil": "gui/adventure/inventory_icons/sword.png",
            "Benang kafan": "gui/adventure/item_icons/thread.svg",
            "Surat lama": "gui/adventure/item_icons/letter.svg",
            "Tasbih": "gui/adventure/item_icons/tasbih.svg",
            "Garam": "gui/adventure/item_icons/salt.svg",
        }
        return icons.get(item, None)

    def adv_yes_no(value):
        return "Ya" if value else "Tidak"

    def adv_known_identity():
        return adv_identity_clue or adv_has_old_letter

    def adv_known_burial_problem():
        return adv_burial_clue or adv_has_kafan_thread

    def adv_can_release():
        return adv_observed_pattern and adv_known_identity() and adv_known_burial_problem() and adv_has_kafan_thread and adv_has_tasbih

    def adv_case_summary_lines():
        lines = []

        if adv_observed_pattern:
            lines.append("Gerak-geri: Pocong ada jeda kecil bila mangsa tak lari.")
        else:
            lines.append("Gerak-geri: Belum jelas. MC belum tahu bila perlu diam dan bila perlu bergerak.")

        if adv_known_identity():
            lines.append("Identiti: Dia bukan sekadar makhluk. Dia ada keluarga, dan namanya perlu diakui.")
        else:
            lines.append("Identiti: Belum jelas. Tanpa nama, MC cuma boleh melawan benda yang dia tak faham.")

        if adv_known_burial_problem():
            lines.append("Kubur: Pengebumian tergesa-gesa dan simpulan kafan belum selesai.")
        else:
            lines.append("Kubur: Belum jelas. Punca ikatan roh masih kabur.")

        if adv_has_kafan_thread:
            lines.append("Bukti fizikal: Benang kafan dibawa sebagai petunjuk simpulan.")
        else:
            lines.append("Bukti fizikal: Tiada benang kafan. Simpulan mungkin susah dibuka dengan betul.")

        if adv_has_tasbih:
            lines.append("Cara melepaskan: Tasbih boleh menenangkan tangan dan niat MC.")
        else:
            lines.append("Cara melepaskan: Belum cukup lembut. Keris dan garam hanya sesuai untuk bertahan.")

        return lines

    def adv_release_status_text():
        if adv_can_release():
            return "Nota lengkap: MC sudah faham cara mendekati, mengenali, dan melepaskan arwah."
        return "Nota belum lengkap: MC mungkin boleh hidup, tapi belum tentu boleh melepaskan arwah."

    def adv_ending_report_lines():
        return [
            "Gerak-geri difahami: " + adv_yes_no(adv_observed_pattern or adv_final_pattern_used),
            "Identiti arwah diketahui: " + adv_yes_no(adv_known_identity() or adv_final_identity_used),
            "Masalah simpulan/kubur difahami: " + adv_yes_no(adv_known_burial_problem()),
            "Benang kafan ditemui: " + adv_yes_no(adv_has_kafan_thread),
            "Tasbih dibawa: " + adv_yes_no(adv_has_tasbih),
            "Kekerasan digunakan: " + adv_yes_no(adv_aggressive_prepare or adv_final_force_used),
        ]
