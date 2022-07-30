import pyautogui
import keyboard

savedir = r'C:\\'

i = 0

while True:
    if keyboard.is_pressed("q"): #returns True if "q" is pressed
        print("You pressed q")
        break #break the while loop is "q" is pressed
    if keyboard.is_pressed("s"): #returns True if "q" is pressed
        print("taking schreenshoot ...")
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(savedir + str(i) + '.png')
        i += 1
        print("toke screenshot wiht index :" + str(i))