from pygame import mixer
from datetime import datetime
from time import time, sleep

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        global a
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()} \n")

if __name__ == '__main__':
    # musiconloop('safari-official-video.mp3', 'off')

    init_water = time()
    init_eyes = time()
    init_exercise = time()

    watersecs = 5
    eyessecs = 10
    exsecs = 20

    while True:

        if time() - init_water > watersecs:
            print('Water Dringng time. enter donewater for stop') 
            musiconloop('safari-official-video.mp3', 'donewater')
            init_water = time()
            log_now('Drank water at - ')

        if time() - init_eyes > eyessecs:
            print('Eye Exersics Times enter doneeye for stop') 
            musiconloop('safari-official-video.mp3', 'doneeye')
            init_eyes = time()
            log_now('Eyes Relaxed at - ')
        
        if time() - init_exercise > exsecs:
            print('Physical Activity Time. enter doneph for stop') 
            musiconloop('safari-official-video.mp3', 'doneph')
            init_exercise = time()
            log_now('Drank water at - ')
