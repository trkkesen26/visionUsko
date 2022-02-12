import pyautogui
import pydirectinput
import time
import numpy as np
import cv2


time.sleep(1)
k = 0
startTime = time.time()
pydirectinput.press("9")
time.sleep(1)
while True:
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:\Users\trkke\PycharmProjects\visionUsko\can.png')
    img = cv2.imread("can.png")
    crop_img = img[33:66, 25:220]
    crop_wolf = img[0:250, 1550:1919]
    image = crop_img

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    low_red = np.array([170, 155, 84])
    high_red = np.array([179, 255, 255])
    mask = cv2.inRange(hsv, low_red, high_red)
    resultRed = cv2.bitwise_and(image, image, mask=mask)

    hsv1 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    mask1 = cv2.inRange(hsv, low_blue, high_blue)
    resultBlue = cv2.bitwise_and(image, image, mask=mask1)

    colorRed = resultRed[14, 100]
    if colorRed[0] == 0 and colorRed[1] == 0 and colorRed[2] == 0:
        pydirectinput.press("0")

    colorBlue = resultBlue[30, 70]
    if colorBlue[0] == 0 and colorBlue[1] == 0 and colorBlue[2] == 0:
        pydirectinput.press("4")

    grayWolfImg = cv2.cvtColor(crop_wolf, cv2.COLOR_BGR2GRAY)
    template = cv2.imread("wolf.png", 0)
    h, w = template.shape
    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED,
               cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
    i = 0
    tempTime = time.time()
    if tempTime > startTime + 120:
        startTime = time.time()
        for method in methods:
            imgCopy = grayWolfImg.copy()
            result = cv2.matchTemplate(imgCopy, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if max_loc == (338, 92) or min_loc == (338, 92):
                i = i+1
        if i > 0:
            pass
        else:
            k = k + 1
            if k > 2:
                k = 0
                pydirectinput.press("9")
                time.sleep(1)

    pydirectinput.press("z")
    pydirectinput.press("7")
    time.sleep(.5)
