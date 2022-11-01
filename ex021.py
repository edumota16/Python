from pygame import mixer
import playsound

mixer.init()
mixer.music.load('ex021.mp3.mp3')
mixer.music.play()
input('Agora você escuta?')