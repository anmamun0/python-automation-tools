from pytube import YouTube
import time

a='https://youtu.be/vunhMBRfhL8'
b='https://youtu.be/g3nmq9mHgmg'
c='https://youtu.be/5C7x_9ZFU60'
d='https://youtu.be/7Gqh51HGSUw'
e='https://youtu.be/_eYJyRK-yaY'
f="https://youtu.be/26XUuvGPKl8"
g="https://youtu.be/3_OC6bJr5bc"
h="https://youtu.be/Vl4Gl-ut1XI"
i="https://youtu.be/Bqi2iEn1l4E"
j="https://youtu.be/BcFoLD6acOM"
k="https://youtu.be/nUMwqxhJSew"

list= [a,b,c,d,e,f,g,h,i,j,k]

for count, link in enumerate(list):
    start  = time.time()
    
    yt = YouTube(link)
    video = yt.streams.filter(progressive=True, file_extension='mp4', res = '720p').first()
    video.download()

    stop = time.time()
    enisial_time = stop - start
    if enisial_time>= 60:
        minit = enisial_time/60
        print(f"{count} NO is Done! Downloeaded - { minit} minuter")
    else:
        print(f"{count} NO is Done! Downloeaded - {enisial_time} sec")
print('successfull')
