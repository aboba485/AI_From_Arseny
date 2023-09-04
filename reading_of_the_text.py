
def reading_of_text():
    import sqlite3 as sq
    import pygame
    def play_sound(file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick()
        pygame.mixer.quit()

    pygame.mixer.pre_init(44100, -16, 2, 512)


    consonants_with_softening = ["б", "в", "г", "д", "з", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х"]
    vowels = ["е", "ё", "и", "ю", "я"]

    db = sq.connect("Sounds_base.db")
    cursor = db.cursor()

    FilePath = "C:\\Users\\User\\Desktop\\AI_from_arseny\\text_to_read_txt.txt"
    ListOfChars = []

    with open(FilePath, 'r', encoding='utf-8') as file:
        FileData = file.read()
    FileData = FileData.lower()

    ListOfChars = list(FileData)


    for i in range(len(ListOfChars)):
        if i < len(ListOfChars) - 1:
            next_char = ListOfChars[i + 1]
            if next_char == "ь":
                if i in vowels:
                    letter = ListOfChars[i]
                    cursor.execute("SELECT link_to_sound FROM consonants_with_soft_sound WHERE letters=?", (letter,))
                    sound_file_path = cursor.fetchone()
                    if sound_file_path:
                        play_sound(sound_file_path[0])
                elif i not in vowels: 
                    letter = ListOfChars[i]
                    cursor.execute("SELECT link_to_sound FROM sounds_of_letters WHERE letters=?", (letter,))
                    sound_file_path = cursor.fetchone()
                    if sound_file_path:
                        play_sound(sound_file_path[0])

            elif ListOfChars[i] in consonants_with_softening and next_char in vowels:
                letter = ListOfChars[i]
                cursor.execute("SELECT link_to_sound FROM consonants_with_soft_sound WHERE letters=?", (letter,))
                sound_file_path = cursor.fetchone()
                if sound_file_path:
                    play_sound(sound_file_path[0])

            elif ListOfChars[i] == ".":
                import time
                time.sleep(0.6)

            elif ListOfChars == ",":
                import time
                time.sleep(0.3)

            elif ListOfChars[i] == " ":
                import time
                time.sleep(0.15)

            else:
                letter = ListOfChars[i]
                cursor.execute("SELECT link_to_sound FROM sounds_of_letters WHERE letters=?", (letter,))
                sound_file_path = cursor.fetchone()
                if sound_file_path:
                    play_sound(sound_file_path[0])
            

        elif i == len(ListOfChars) - 1:
            letter = ListOfChars[i]
            cursor.execute("SELECT link_to_sound FROM sounds_of_letters WHERE letters=?", (letter,))
            sound_file_path = cursor.fetchone()
            if sound_file_path:
                play_sound(sound_file_path[0])
  

    db.close()

reading_of_text()