screen musicbox() tag menu:



    python:
        musiclist = []
        musiclist.append(["A Noon", "Collapsed Spaces", audio.prepare, None])
        musiclist.append(["A Noon", "Edge of the Abyss", audio.creepy, None])
        musiclist.append(["Alex Zavesa", "Ambient Space", audio.space, None])
        musiclist.append(["Anitek", "Little Monsters", audio.jazz, None])

        musiclist.append(["Grégoire Lourme", "Pioneers of Space", audio.epicuncut, None])

        musiclist.append(["Linturaven", "Visitors", audio.visitors, None])
        musiclist.append(["Lena Orsa", "Meditation", audio.verycalm, None])
        musiclist.append(["Professor Kliq", "Sacreligious", audio.party, None])
        musiclist.append(["Hartwig Media", "Cyber Twilight", audio.cybernight, None])
        musiclist.append(["Kai Engel", "Modum", audio.da, None])
        musiclist.append(["Andrey Avkhimovich", "Package", audio.tense, "https://open.spotify.com/track/5H36HSNdX0eYmaFm4BDW8V?si=pa8R_zQUR9GyXEX0p2mQhA"])
        musiclist.append(["MG Rizzello", "Ambient Underwater", audio.calm, None])
        musiclist.append(["ROE Audio News", "Sindrome", audio.stress, None])
        musiclist.append(["ROE Audio News", "Doppio Sogno", audio.worried, None])
        musiclist.append(["ROE Audio News", "Nebula", audio.calmmorning, None])
        musiclist.append(["Ostenvegr", "Lost In Space", audio.intro, None])
        musiclist.append(["Ostenvegr", "Toward Alpha Centauri", audio.darkclub, None])
        musiclist.append(["Timur Scott", "Black", audio.black, None])
        musiclist.append(["Sol", "Internal Eye", audio.sol, "https://open.spotify.com/track/3LyGPauW6BajHMm91Kowjd?si=s8jkPStmTTKOqlSAcz33rw"])
        musiclist.append(["Titan Slayer", "Guerilla Warfare", audio.industrial, "https://open.spotify.com/track/4vAXehWkSn61IpqvRfJAoz?si=yz41TUQRTeql9-79ShU7pQ"])
        musiclist.append(["Titan Slayer", "Hyperion", audio.redmoon, None])
        musiclist.append(["Strange Zero", "Burning Star", audio.burningstars, "https://open.spotify.com/track/1NO7YOdGC6SejfHrdBweTu?si=SXcfoHfpShCeyP1ZlzgG9w"])
        musiclist.append(["Strange Zero", "Moments", audio.moments, "https://open.spotify.com/track/1c7wqmAwtYHEfEwtr6OSF6?si=ukWaU6VTQ-2qtDfENFJhZg"])
        musiclist.append(["Strange Zero", "Plastic Console", audio.console, None])
        musiclist.append(["We Are All Astronauts", "Doves", audio.doves, "https://open.spotify.com/track/52C7TZcyZPcl39JWziyrx4?si=60Eai924TSaD7GruCld75Q"])
        musiclist.append(["We Are All Astronauts", "Violent Delights", audio.delights, "https://open.spotify.com/track/26474IqdAPMsK6uGS26pbw?si=vKA1K4adSjKVpITrQZ9u-w"])

        musiclistlength = len(musiclist)







    use game_menu(_("Playlist musical"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label _("Playlist musical")
            text _("Aquí hay una selección de las canciones, los artistas y los enlaces para encontrar su música.")

            null height 20

            grid 3 musiclistlength:
                spacing 10

                for i in musiclist:

                    hbox:
                        imagebutton:
                            idle "musicplay"
                            hover "musichover"
                            selected_idle "musicstop"
                            selected_hover "musicstophover"
                            action Play("music", i[2])









                    label _(i[0])


                    text _(i[1])










define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
