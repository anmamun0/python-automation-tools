# One way to open system music softwer

import os
os.system("path/music_name.mp3") 

# Second way to play into python code without show softwer
from pygame import mixer

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
if __name__ == '__main__':
  #if in input , user type 'off' then music will off
    musiconloop('path/music_name.mp3', 'off') 
    
