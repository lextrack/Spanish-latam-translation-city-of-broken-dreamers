













define config.name = _("The City of Broken Dreamers")

define website = "http://www.patreon.com/phillygames"




define gui.show_name = True




define config.version = "1.0.4"





define gui.about = _("All licensed music and sound effects are licensed via Jamemdo or Audio Jungle. Royalty free music provided by http://teknoaxe.com")






define build.name = "BrokenDreamers"







define config.has_sound = True
define config.has_music = True
define config.has_voice = False





define config.sample_sound = audio.puncheffect







define config.main_menu_music = audio.futurenoir










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 60





default preferences.afm_time = 15
















define config.save_directory = "BrokenDreamers-1521333194"
define config.autosave_slots = 12





define config.window_icon = "gui/window_icon.png"






init python:



















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.rpy', None)















    build.archive("scripts", "all")
    build.archive("shared", "all")
    build.archive("audio", "all")
    build.archive("chapter1", "all")
    build.archive("chapter2", "all")
    build.archive("chapter3", "all")
    build.archive("chapter4", "all")
    build.archive("chapter5", "all")
    build.archive("chapter6", "all")
    build.archive("chapter7", "all")


    build.archive("chapter1video", "all")
    build.archive("chapter2video", "all")
    build.archive("chapter3video", "all")
    build.archive("chapter4video", "all")
    build.archive("chapter5video", "all")
    build.archive("chapter6video", "all")
    build.archive("chapter7video", "all")



    build.classify('game/gui/**.png', 'shared')
    build.classify('game/gui/**.jpg', 'shared')
    build.classify('game/gui/**.webp', 'shared')
    build.classify('game/gui/**.webm', 'shared')


    build.classify('game/images/common/**.png', 'shared')
    build.classify('game/images/common/**.jpg', 'shared')
    build.classify('game/images/common/**.webp', 'shared')

    build.classify('game/fonts/**.ttf', 'shared')

    build.classify('game/video/intros/**.webm', 'shared')



    build.classify('game/music/**.ogg', 'audio')
    build.classify('game/music/**.mp3', 'audio')
    build.classify('game/music/**.wav', 'audio')

    build.classify('game/effects/**.ogg', 'audio')
    build.classify('game/effects/**.mp3', 'audio')
    build.classify('game/effects/**.wav', 'audio')


    build.classify('game/images/chapter1/**.png', 'chapter1')
    build.classify('game/images/chapter1/**.jpg', 'chapter1')
    build.classify('game/images/chapter1/**.webm', 'chapter1')

    build.classify('game/images/chapter2/**.png', 'chapter2')
    build.classify('game/images/chapter2/**.jpg', 'chapter2')
    build.classify('game/images/chapter2/**.webm', 'chapter2')

    build.classify('game/images/chapter3/**.png', 'chapter3')
    build.classify('game/images/chapter3/**.jpg', 'chapter3')
    build.classify('game/images/chapter3/**.webm', 'chapter3')

    build.classify('game/images/chapter4/**.png', 'chapter4')
    build.classify('game/images/chapter4/**.jpg', 'chapter4')
    build.classify('game/images/chapter4/**.webm', 'chapter4')

    build.classify('game/images/chapter5/**.png', 'chapter5')
    build.classify('game/images/chapter5/**.jpg', 'chapter5')
    build.classify('game/images/chapter5/**.webm', 'chapter5')

    build.classify('game/images/chapter6/**.png', 'chapter6')
    build.classify('game/images/chapter6/**.jpg', 'chapter6')
    build.classify('game/images/chapter6/**.webm', 'chapter6')

    build.classify('game/images/chapter7/**.png', 'chapter7')
    build.classify('game/images/chapter7/**.jpg', 'chapter7')
    build.classify('game/images/chapter7/**.webm', 'chapter7')

    build.classify('game/images/gallery/**.png', 'shared')
    build.classify('game/images/gallery/**.jpg', 'shared')
    build.classify('game/images/gallery/**.webm', 'shared')

    build.classify('game/images/bonus/**.png', 'shared')
    build.classify('game/images/bonus/**.jpg', 'shared')
    build.classify('game/images/bonus/**.webm', 'shared')

    build.classify('game/images/bonushovers/**.png', 'shared')
    build.classify('game/images/bonushovers/**.jpg', 'shared')
    build.classify('game/images/bonushovers/**.webm', 'shared')


    build.classify('game/video/chapter-1-video/**.webm', 'chapter1video')
    build.classify('game/video/chapter-2-video/**.webm', 'chapter2video')
    build.classify('game/video/chapter-3-video/**.webm', 'chapter3video')
    build.classify('game/video/chapter-4-video/**.webm', 'chapter4video')
    build.classify('game/video/chapter-5-video/**.webm', 'chapter5video')
    build.classify('game/video/chapter-6-video/**.webm', 'chapter6video')
    build.classify('game/video/chapter-7-video/**.webm', 'chapter7video')



    build.classify('game/*.rpyc', 'scripts')
    build.classify('game/chapter1/*.rpyc', 'scripts')
    build.classify('game/chapter2/*.rpyc', 'scripts')
    build.classify('game/chapter3/*.rpyc', 'scripts')
    build.classify('game/chapter4/*.rpyc', 'scripts')
    build.classify('game/chapter5/*.rpyc', 'scripts')
    build.classify('game/chapter6/*.rpyc', 'scripts')
    build.classify('game/chapter7/*.rpyc', 'scripts')






    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
