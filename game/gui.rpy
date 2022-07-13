









init -2 python:
    gui.init(1920, 1080)













define -2 gui.accent_color = '#6bc1fe'


define -2 gui.idle_color = '#999999'



define -2 gui.idle_small_color = '#aaaaaa'


define -2 gui.hover_color = '#ffffff'



define -2 gui.selected_color = '#ffffff'


define -2 gui.insensitive_color = '#ffffff7f'



define -2 gui.muted_color = '#003d51'
define -2 gui.hover_muted_color = '#005b7a'


define -2 gui.text_color = gui.preference("diacolor", '#ffffff')
define -2 gui.name_text_color = '#ffffff'
define -2 gui.interface_text_color = '#ffffff'





define -2 gui.text_font = "fonts/GOTHIC.ttf"


define -2 gui.name_text_font = "fonts/Futura.ttc"


define -2 gui.interface_text_font = "fonts/GOTHIC.ttf"


define -2 gui.text_size = 28


define -2 gui.name_text_size = 36


define -2 gui.interface_text_size = 19


define -2 gui.label_text_size = 22


define -2 gui.notify_text_size = 16
define -2 gui.alert_text_size = 16


define -2 gui.title_text_size = 40




define -2 gui.main_menu_background = "gui/cover.jpg"

define -2 gui.game_menu_background = "gui/covermenu.jpg"


define -2 gui.show_name = False









define -2 gui.textbox_height = 165



define -2 gui.textbox_yalign = 1.0




define -2 gui.name_xpos = 255
define -2 gui.name_ypos = -10



define -2 gui.name_xalign = 0.0



define -2 gui.namebox_width = None
define -2 gui.namebox_height = None



define -2 gui.namebox_borders = Borders(5, 5, 5, 5)



define -2 gui.namebox_tile = False





define -2 gui.dialogue_xpos = 300
define -2 gui.dialogue_ypos = 50


define -2 gui.dialogue_width = 1300



define -2 gui.dialogue_text_xalign = 0.0
define -2 gui.name_text_outlines = [(2, "#000",0,0)]
define -2 gui.dialogue_text_outlines = [(2, "#000",0,0)]
define -2 gui.thought_text_outlines = [(2, "#000",0,0)]







define -2 gui.button_width = None
define -2 gui.button_height = None


define -2 gui.button_borders = Borders(30, 30, 30, 30, 10, -5, 10, -5)



define -2 gui.button_tile = False


define -2 gui.button_text_font = gui.interface_text_font


define -2 gui.button_text_size = gui.interface_text_size


define -2 gui.button_text_idle_color = gui.idle_color
define -2 gui.button_text_hover_color = gui.hover_color
define -2 gui.button_text_selected_color = gui.selected_color
define -2 gui.button_text_insensitive_color = gui.insensitive_color



define -2 gui.button_text_xalign = 0.0








define -2 gui.radio_button_borders = Borders(30, 30, 30, 30, 10, -5, 10, -5)

define -2 gui.check_button_borders = Borders(30, 30, 30, 30, 10, -5, 10, -5)

define -2 gui.confirm_button_text_xalign = 0.5

define -2 gui.page_button_borders = Borders(10, 4, 10, 4)

define -2 gui.quick_button_borders = Borders(10, 4, 10, 0)
define -2 gui.quick_button_text_size = 14
define -2 gui.quick_button_text_idle_color = gui.idle_small_color
define -2 gui.quick_button_text_selected_color = gui.accent_color












define -2 gui.choice_button_width = 450
define -2 gui.choice_button_height = None
define -2 gui.choice_button_tile = False
define -2 gui.choice_button_borders = Borders(30, 30, 30, 30, 10, -5, 10, -5)
define -2 gui.choice_button_text_font = gui.text_font
define -2 gui.choice_button_text_size = 21
define -2 gui.choice_button_text_xalign = 0.5
define -2 gui.choice_button_text_idle_color = "#cccccc"
define -2 gui.choice_button_text_hover_color = "#ffffff"









define -2 gui.slot_button_width = 276
define -2 gui.slot_button_height = 206
define -2 gui.slot_button_borders = Borders(10, 10, 10, 10)
define -2 gui.slot_button_text_size = 14
define -2 gui.slot_button_text_xalign = 0.5
define -2 gui.slot_button_text_idle_color = gui.idle_small_color


define -2 config.thumbnail_width = 256
define -2 config.thumbnail_height = 144


define -2 gui.file_slot_cols = 4
define -2 gui.file_slot_rows = 3
define -2 config.autosave_slots = 12








define -2 gui.navigation_xpos = 100


define -2 gui.skip_ypos = 830
define -2 gui.skip_xpos = 900

define -2 gui.notify_ypos = 45
define -2 gui.alert_ypos = 45

define -2 gui.choice_spacing = 15


define -2 gui.navigation_spacing = 4


define -2 gui.pref_spacing = 20


define -2 gui.pref_button_spacing = 4


define -2 gui.page_spacing = 10
define -2 gui.page_borders = Borders(40, 40, 40, 40)

define -2 gui.slot_spacing = 10


define -2 gui.main_menu_text_xalign = 1.0








define -2 gui.frame_borders = Borders(4, 4, 4, 4)


define -2 gui.confirm_frame_borders = Borders(40, 40, 40, 40)



define -2 gui.skip_frame_borders = Borders(30, 30, 30, 30, 10, -5, 10, -5)


define -2 gui.notify_frame_borders = Borders(16, 5, 40, 5)

define -2 gui.alert_frame_borders = Borders(16, 5, 40, 5)


define -2 gui.frame_tile = False










define -2 gui.bar_size = 36
define -2 gui.scrollbar_size = 12
define -2 gui.slider_size = 30


define -2 gui.bar_tile = False
define -2 gui.scrollbar_tile = False
define -2 gui.slider_tile = False


define -2 gui.bar_borders = Borders(4, 4, 4, 4)
define -2 gui.scrollbar_borders = Borders(4, 4, 4, 4)
define -2 gui.slider_borders = Borders(4, 4, 4, 4)


define -2 gui.vbar_borders = Borders(4, 4, 4, 4)
define -2 gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define -2 gui.vslider_borders = Borders(4, 4, 4, 4)



define -2 gui.unscrollable = "hide"







define -2 config.history_length = 250



define -2 gui.history_height = 140



define -2 gui.history_name_xpos = 150
define -2 gui.history_name_ypos = 0
define -2 gui.history_name_width = 150
define -2 gui.history_name_xalign = 1.0


define -2 gui.history_text_xpos = 170
define -2 gui.history_text_ypos = 5
define -2 gui.history_text_width = 740
define -2 gui.history_text_xalign = 0.0







define -2 gui.nvl_borders = Borders(0, 10, 0, 20)



define -2 gui.nvl_height = 115



define -2 gui.nvl_spacing = 10



define -2 gui.nvl_name_xpos = 430
define -2 gui.nvl_name_ypos = 0
define -2 gui.nvl_name_width = 150
define -2 gui.nvl_name_xalign = 1.0


define -2 gui.nvl_text_xpos = 450
define -2 gui.nvl_text_ypos = 8
define -2 gui.nvl_text_width = 590
define -2 gui.nvl_text_xalign = 0.0



define -2 gui.nvl_thought_xpos = 240
define -2 gui.nvl_thought_ypos = 0
define -2 gui.nvl_thought_width = 780
define -2 gui.nvl_thought_xalign = 0.0


define -2 gui.nvl_button_xpos = 450
define -2 gui.nvl_button_xalign = 0.0







define -2 gui.language = "unicode"






init -2 python:



    if renpy.variant("touch"):
        
        gui.quick_button_borders = Borders(40, 14, 40, 0)



    if renpy.variant("small"):
        
        
        gui.text_size = 40
        gui.name_text_size = 44
        gui.notify_text_size = 28
        gui.alert_text_size = 28
        gui.interface_text_size = 28
        gui.button_text_size = 30
        gui.label_text_size = 28
        
        gui.textbox_height = 200
        gui.name_xpos = 77
        gui.name_ypos = 0
        gui.text_xpos = 90
        gui.text_width = 1100
        gui.dialogue_ypos = 55
        gui.dialogue_xpos = 80
        
        gui.dialogue_width = 1440
        
        gui.name_text_outlines = [(4, "#000",0,0)]
        gui.dialogue_text_outlines = [(4, "#000",0,0)]
        gui.thought_text_outlines = [(4, "#000",0,0)]
        
        
        
        gui.choice_button_width = 800
        gui.choice_button_height = None
        gui.choice_button_tile = False
        gui.choice_button_borders = Borders(20, 8, 20, 8)
        gui.choice_button_text_font = gui.text_font
        gui.choice_button_text_size = 30 
        gui.choice_spacing = 34
        
        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10
        
        gui.history_height = 190
        gui.history_text_width = 690
        
        
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        
        
        gui.nvl_height = 170
        
        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325
        
        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5
        
        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20
        
        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
        
        
        gui.quick_button_text_size = 30
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
