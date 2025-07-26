from gtts import gTTS
import pygame
import time

def speak(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='ar')
    tts.save(filename)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.5)