import pyautogui
import time
import random


time.sleep(4)
# massage = 15
# while massage > 0 :
#     pyautogui.typewrite(f' {massage}Sorry! 😘😘😘 {random.randint(1,100)}')
#     pyautogui.press('enter')
#     massage -= 1
for i in range(1,100):
    if(i%10 == 0):
        pyautogui.typewrite(f"\nLove You Maria !!! :)\n")
    else:
        pyautogui.typewrite(f"Happy BirthDay MARIA :)")

    pyautogui.press('enter')





