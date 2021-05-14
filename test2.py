from PIL import Image,ImageGrab

import time
import pyautogui



time.sleep(3)
image = ImageGrab.grab()
data = image.load()

for i in range(160, 200):
    for j in range(390, 460):
        data[i, j] = 1

for i in range(160, 200):
    for j in range(250, 390):
        data[i, j] = 77

image.show()

