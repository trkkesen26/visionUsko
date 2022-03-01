import pyautogui
import pydirectinput
import time
import numpy as np
import cv2
import multiprocessing

time.sleep(2)
IsFlagRaised = 0


def checkSkills():
    while True:
        skillScreenShot = pyautogui.screenshot()
        skillScreenShot.save(r'C:\Users\trkke\PycharmProjects\visionUsko\skill.png')
        skillImg = cv2.imread("skill.png")
        crop_wolf = skillImg[0:250, 1550:1920]
        grayWolfImg = cv2.cvtColor(crop_wolf, cv2.COLOR_BGR2GRAY)
        template = cv2.imread("wolf.png", 0)
        result = cv2.matchTemplate(grayWolfImg, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        location, location2 = np.where(result >= threshold)

        if len(location) == 0 and len(location2) == 0:
            global IsFlagRaised
            IsFlagRaised = 1
            time.sleep(1)
            while len(location) == 0 and len(location2) == 0:
                pydirectinput.press("9")
                if len(location) > 0 and len(location2) > 0:
                    break
            IsFlagRaised = 0
            time.sleep(119)
        else:
            pass


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
    global IsFlagRaised
    while True:
        if IsFlagRaised == 0:
            pydirectinput.press("z")
            pydirectinput.press("7")
            time.sleep(.32)


mpSkill = multiprocessing.Process(target=checkSkills)
mpHpMp = multiprocessing.Process(target=checkHealty)
mpAtack = multiprocessing.Process(target=atack)

if __name__ == '__main__':
    mpSkill.start()
    mpHpMp.start()
    mpAtack.start()

    while True:
        time.sleep(3131)
