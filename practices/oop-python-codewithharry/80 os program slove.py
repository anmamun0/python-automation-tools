# # import os ,sys
# # import random

# # # os.chdir('flowerful')
# # # di = os.listdir()
# # # for k , i in enumerate(di):
# # #          txt = i.split('.')
# # #          if txt[1] == 'jpg':
# # #               os.rename(i,f'This is {k}.jpg')

# # # fd = os.open('newfile.txt', os.O_RDWR|os.O_CREAT)
# # # b= str.encode('adsfaee')
# # # os.write(fd,b)
# # # os.close(fd)
# # print(os.repl)

# from emoji import emojize
# print(emojize(":thumbs_up:"))



from ppadb.client import Client as AdbClient

if __name__ == '__main__':
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')