from PIL import Image,ImageGrab

import time
import pyautogui

def press(button):
    pyautogui.keyDown(button)
    return

def identifier(data):

    for i in range(160, 200): #you have to adjust this parameters accorrding to frame size of your computer (x- axis)
        for j in range(390, 460):#you have to adjust this parameters accorrding to frame size of your computer (y- axis)
            if data[i, j] < 100:
                press("up")
                return



    for i in range(160, 200):
        for j in range(250, 390):
            if data[i, j] < 100:
                press('down')
                return
    return





if __name__ == '__main__':


    print('move to Chrome window')
    time.sleep(2)
    #press('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        identifier(data)
        #image.show()
        #break






