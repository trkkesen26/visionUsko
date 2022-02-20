import pyautogui
import pydirectinput
import time
import numpy as np
import cv2
import multiprocessing

time.sleep(2)
k = 0


def checkSkills():
    global k
    while True:
        skillScreenShot = pyautogui.screenshot()
        skillScreenShot.save(r'C:\Users\trkke\PycharmProjects\visionUsko\skill.png')
        skillImg = cv2.imread("skill.png")
        crop_wolf = skillImg[0:250, 1550:1919]
        grayWolfImg = cv2.cvtColor(crop_wolf, cv2.COLOR_BGR2GRAY)
        template = cv2.imread("wolf.png", 0)
        methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED,
                   cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
        i = 0
        for method in methods:
            imgCopy = grayWolfImg.copy()
            result = cv2.matchTemplate(imgCopy, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if max_loc == (338, 92) or min_loc == (338, 92):
                i = i + 1
        if i > 0:
            k = 0
            pass
        else:
            k = k + 1
            if k > 0:
                pydirectinput.press("9")
                time.sleep(1.5)


def checkHealty():
    while True:
        hpmpScreenShot = pyautogui.screenshot()
        hpmpScreenShot.save(r'C:\Users\trkke\PycharmProjects\visionUsko\can.png')
        img = cv2.imread("can.png")
        image = img[33:66, 25:220]
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        low_red = np.array([170, 155, 84])
        high_red = np.array([179, 255, 255])
        mask = cv2.inRange(hsv, low_red, high_red)
        resultRed = cv2.bitwise_and(image, image, mask=mask)

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


def atack():
    while True:
        pydirectinput.press("z")
        pydirectinput.press("7")
        time.sleep(.2)


mpSkill = multiprocessing.Process(target=checkSkills)
mpHpMp = multiprocessing.Process(target=checkHealty)
mpAtack = multiprocessing.Process(target=atack)

if __name__ == '__main__':
    mpSkill.start()
    mpHpMp.start()
    mpAtack.start()

    while True:
        time.sleep(3131)
