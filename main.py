##########################################LIBRARIES##################################################
import pyautogui
import pydirectinput
import time
import numpy as np
import cv2
import multiprocessing
from PIL import Image
import queue
######################################################################################################
######################################################################################################

##########################################DEFINATIONS#################################################
useDef = False
######################################################################################################
######################################################################################################

###########################################VARIABLES##################################################
wolfCounter = 0
######################################################################################################
######################################################################################################


def checkSkills():
    while True:
        global wolfCounter
        skillScreenShot = pyautogui.screenshot()
        skillScreenShot.save(r'C:\Users\trkke\PycharmProjects\visionUsko\ss.png')
        skillImg = cv2.imread("ss.png")
        crop_wolf = skillImg[0:250, 1550:1920]
        grayWolfImg = cv2.cvtColor(crop_wolf, cv2.COLOR_BGR2GRAY)
        template = cv2.imread("wolf.png", 0)
        result = cv2.matchTemplate(grayWolfImg, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        location, location2 = np.where(result >= threshold)

        if len(location) == 0 and len(location2) == 0:
            wolfCounter = wolfCounter + 1
            if wolfCounter == 1:
                pydirectinput.press("s")
                pydirectinput.press("9")
                time.sleep(1.75)

            if wolfCounter == 2:
                pydirectinput.press("w")
                pydirectinput.press("9")
                wolfCounter = 0
                time.sleep(1.75)
        else:
            time.sleep(121)


def checkHealty():
    while True:
        hpmpScreenShot = pyautogui.screenshot()
        hpmpScreenShot.save(r'C:\Users\trkke\PycharmProjects\visionUsko\can.png')
        img2 = cv2.imread("can.png")
        img = Image.open('can.png')
        pix = img.load()
        image = img2[33:66, 25:220]
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        low_blue = np.array([94, 80, 2])
        high_blue = np.array([126, 255, 255])
        mask1 = cv2.inRange(hsv, low_blue, high_blue)
        resultBlue = cv2.bitwise_and(image, image, mask=mask1)

        if pix[155, 42] == (0, 0, 0):
            pydirectinput.press("0")

        colorBlue = resultBlue[30, 70]
        if colorBlue[0] == 0 and colorBlue[1] == 0 and colorBlue[2] == 0:
            pydirectinput.press("4")


def atack():
    while True:
        pydirectinput.press("z")
        pydirectinput.press("7")
        time.sleep(.32)


def rpr(q):
    IsTownNeed = 0
    while True:
        rprScreenShoot = pyautogui.screenshot()
        rprScreenShoot.save(r'C:\Users\trkke\PycharmProjects\visionUsko\rpr.png')
        rprSs = cv2.imread("rpr.png")
        im = Image.open('rpr.png')
        pix = im.load()
        crop_Inn = rprSs[400:620, 1530:1900]
        grayInn = cv2.cvtColor(crop_Inn, cv2.COLOR_BGR2GRAY)
        crop_Rpr = rprSs[240:300, 1830:1910]
        grayRprImg = cv2.cvtColor(crop_Rpr, cv2.COLOR_BGR2GRAY)

        templateRpr = cv2.imread("ironBow.png", 0)
        threshold = 0.90
        result = cv2.matchTemplate(grayRprImg, templateRpr, cv2.TM_CCORR_NORMED)
        location, location2 = np.where(result >= threshold)
        if len(location) != 0 and len(location2) != 0:
            template = cv2.imread("ironBow_Repaired.png", 0)
            result = cv2.matchTemplate(grayInn, template, cv2.TM_CCORR_NORMED)
            location, location2 = np.where(result >= threshold)
            if len(location) != 0 and len(location2) != 0:
                pydirectinput.mouseDown(button='right', x=location2[0] + 1550, y=location[0] + 420)
                time.sleep(0.02)
                pydirectinput.mouseUp(button='right', x=location2[0] + 1550, y=location[0] + 420)

            else:
                IsTownNeed = IsTownNeed + 1
                if IsTownNeed > 5:
                    pydirectinput.mouseDown(button='left', x=1665, y=1058)
                    time.sleep(0.02)
                    pydirectinput.mouseUp(button='left', x=1665, y=1058)
                    pydirectinput.press("i")
                    q.put("KILL ATACK")
                    q.put("KILL WOLF")

        if pix[265, 63] == (10, 10, 10):
            pydirectinput.press("p")
            time.sleep(0.2)
            pydirectinput.mouseDown(button='left', x=1738, y=45)
            time.sleep(0.02)
            pydirectinput.mouseUp(button='left', x=1738, y=45)
            pydirectinput.mouseDown(button='left', x=1870, y=400)
            time.sleep(0.02)
            pydirectinput.mouseUp(button='left', x=1870, y=168)
            pydirectinput.mouseDown(button='left', x=1746, y=243)
            time.sleep(0.02)
            pydirectinput.mouseUp(button='left', x=1746, y=243)
            time.sleep(.20)
            pydirectinput.press("s")
            pydirectinput.press("i")


def defenseCheck():
    while True:
        if useDef:
            IsDef200Done = False
            skillScreenShot = pyautogui.screenshot()
            skillScreenShot.save(r'C:\Users\trkke\PycharmProjects\visionUsko\ssForDefense.png')
            skillImg = cv2.imread("ssForDefense.png")
            croppedDefense = skillImg[0:250, 1550:1920]
            bg2ToGraySkillBar = cv2.cvtColor(croppedDefense, cv2.COLOR_BGR2GRAY)
            template = cv2.imread("defense200.png", 0)
            result = cv2.matchTemplate(bg2ToGraySkillBar, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.90
            location, location2 = np.where(result >= threshold)

            if len(location) == 0 and len(location2) == 0:
                pydirectinput.press("s")
                pydirectinput.press("6")
            else:
                IsDef200Done = True
                time.sleep(14)

            if IsDef200Done:
                while True:
                    skillScreenShot = pyautogui.screenshot()
                    skillScreenShot.save(r'C:\Users\trkke\PycharmProjects\visionUsko\ssForDefense.png')
                    skillImg = cv2.imread("ssForDefense.png")
                    croppedDefense = skillImg[0:250, 1550:1920]
                    bg2ToGraySkillBar = cv2.cvtColor(croppedDefense, cv2.COLOR_BGR2GRAY)
                    template = cv2.imread("defense400.png", 0)
                    result = cv2.matchTemplate(bg2ToGraySkillBar, template, cv2.TM_CCOEFF_NORMED)
                    location, location2 = np.where(result >= threshold)

                    if len(location) == 0 and len(location2) == 0:
                        pydirectinput.press("w")
                        pydirectinput.press("5")
                    else:
                        time.sleep(14)
                        break
        else:
            pass


if __name__ == '__main__':
    q = multiprocessing.Queue()
    q.put("START ALL")
    while True:
        msg = q.get()
        if msg == "KILL WOLF":
            mpSkill.terminate()
            time.sleep(0.1)
        elif msg == "START WOLF":
            mpSkill = multiprocessing.Process(target=checkSkills)
            mpSkill.start()
            time.sleep(0.1)
        elif msg == "KILL ATACK":
            mpAtack.terminate()
            time.sleep(0.1)
        elif msg == "START ATACK":
            mpAtack = multiprocessing.Process(target=atack)
            mpAtack.start()
            time.sleep(0.1)
        elif msg == "KILL DEFENSE":
            mpDef.terminate()
            time.sleep(0.1)
        elif msg == "START DEFENSE":
            mpDef = multiprocessing.Process(target=defenseCheck)
            mpDef.start()
            time.sleep(0.1)
        elif msg == "KILL RPR":
            mpRpr.terminate()
            time.sleep(0.1)
        elif msg == "START RPR":
            mpRpr = multiprocessing.Process(target=rpr, args=(q,))
            mpRpr.start()
            time.sleep(0.1)
        elif msg == "KILL HPMP":
            mpHpMp.terminate()
            time.sleep(0.1)
        elif msg == "START HPMP":
            mpHpMp = multiprocessing.Process(target=checkHealty)
            mpHpMp.start()
            time.sleep(0.1)
        elif msg == "KILL ALL":
            mpSkill.terminate()
            time.sleep(0.1)
            mpAtack.terminate()
            time.sleep(0.1)
            mpDef.terminate()
            time.sleep(0.1)
            mpRpr.terminate()
            time.sleep(0.1)
            mpHpMp.terminate()
            time.sleep(0.1)
        elif msg == "START ALL":
            mpDef = multiprocessing.Process(target=defenseCheck)
            mpSkill = multiprocessing.Process(target=checkSkills)
            mpHpMp = multiprocessing.Process(target=checkHealty)
            mpAtack = multiprocessing.Process(target=atack)
            mpRpr = multiprocessing.Process(target=rpr, args=(q,))
            mpSkill.start()
            time.sleep(0.1)
            mpAtack.start()
            time.sleep(0.1)
            mpRpr.start()
            time.sleep(0.1)
            mpDef.start()
            time.sleep(0.1)
