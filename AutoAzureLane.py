
from PIL import ImageGrab
import sys
import os
import threading
import pyautogui
import time
import aircv as ac
import keyboard

# Global
print("path ", os.path.dirname(sys.executable))
# print("path " , os.getcwd())

curDir = os.path.dirname(__file__)
# 图片路径拼接


def GetFullPath(pngName):
    global curDir
    return os.path.join(curDir, pngName)


# 利用文件是否存在判断是Exe 还是 Py文件
if(os.path.exists(GetFullPath('config.ini')) == False):
    print('Exe Run')
    curDir = os.getcwd()

waitTime = 0
minMatch = 0.7  # 最低相似度匹配
warnMatch = 0.85  # 相似度小于此时, 打印黄字

tMain = threading.Thread()
t0 = threading.Thread()


def WaitImgLongTime(targetImg, interval=10):  # 等待图片出现,低频率检测
    maxTryTime = 6*3  # 默认最多等待3分钟
    longTimer = 0
    while (not CheckAndClickImg(targetImg, True, True, 1)):
        time.sleep(interval)
        longTimer += 1
        if(longTimer > maxTryTime):
            return


# 查找图片
# isClick:找到图片后是否点击
# isShip:查找失败后是否跳过
# maxTry:查找失败重新尝试次数
def CheckAndClickImg(targetImg, isClick=True, isShip=True, maxTry=1, autoExit=False):
    target_ImgPath = GetFullPath(targetImg)
    Screen_ImgPath = image_X()
    print(target_ImgPath)
    imsrc = ac.imread(Screen_ImgPath)  # 原始图像
    imsch = ac.imread(target_ImgPath)  # 带查找的部分
    match_result = ac.find_template(imsrc, imsch, minMatch)
    print('match : %s %s' % (targetImg, match_result))
    global waitTime

    if match_result != None:
        x1, y1 = match_result['result']
        if(match_result['confidence'] < warnMatch):
            print("\033[1;33m %s %s \033[0m" %
                  (targetImg, match_result['confidence']))
        waitTime = 0

        if(isClick):
            pyautogui.moveTo(x1, y1)
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(0.4)
        return True
    else:
        waitTime = waitTime+1
        print((isShip == False))
        if((isShip == False) | (waitTime < maxTry)):
            time.sleep(0.1)
            if(isShip == False):
                time.sleep(3)
            if(waitTime < maxTry & autoExit):
                DoKeyDown(exitKey)
            return CheckAndClickImg(targetImg, isClick, isShip, maxTry, autoExit)
        else:
            print("Ship >> ", targetImg)
            return False


# 屏幕截图,并返回保存路径
def image_X():
    global curDir
    img = ImageGrab.grab()
    img.save(curDir + "/temp.png")
    return curDir + "/temp.png"


# 按钮事件
def DoKeyDown(_key):
    pyautogui.press(_key)
    time.sleep(0.6)
# 快按钮事件


def FastKeyDown(_key):
    print(_key)
    time.sleep(0.03)
    pyautogui.press(_key)


def LoopKeyDown(_key):
    time.sleep(2)
    while(True):
        FastKeyDown(_key)


def WeighAnchor():
    CheckAndClickImg("img\weigh_anchor.png")
    time.sleep(0.5)


def Mainline():
    CheckAndClickImg("img\mainline.png")
    time.sleep(0.5)


def StartBattle():
    CheckAndClickImg("img\start.png")
    time.sleep(0.5)


def Back():
    CheckAndClickImg("img\\back.png")
    time.sleep(0.5)


def StartAgain():
    WaitImgLongTime("img\start_again.png")


def Home():
    CheckAndClickImg("img\home.png")
    time.sleep(0.5)


def HardMode():
    WeighAnchor()
    Mainline()
    CheckAndClickImg("img\hard\hardmode.png")
    time.sleep(0.5)
    CheckAndClickImg("img\hard\hardmode12-1.png")
    time.sleep(0.5)
    StartBattle()
    StartBattle()
    for i in range(3):
        StartAgain()
    Home()


def ChallengeAt(n):
    if(CheckAndClickImg("img\challenge\challenge%d.png" % (n))):
        time.sleep(0.5)
        CheckAndClickImg("img\challenge\challenge%d-1.png" % (n))
        time.sleep(0.5)
        CheckAndClickImg("img\challenge\quick_battle.png")
        time.sleep(0.5)
        DoKeyDown("j")
        Back()
    CheckAndClickImg("img\challenge\\next_challenge.png")
    time.sleep(0.5)


def Challenge():
    WeighAnchor()
    CheckAndClickImg("img\challenge\challenge.png")
    time.sleep(0.5)

    for i in range(1, 6):
        ChallengeAt(i)

    Home()


def DailyTasks():
    HardMode()

# 按下Esc停止


def CheckEnd(_key):
    while(True):
        keyboard.wait(_key)
        print(_key)
        os._exit(0)


endKey = 'Esc'


def RunAutoAL():
    # 按下Esc键停止
    global t0
    t0 = threading.Thread(target=CheckEnd, args=(endKey,))
    t0.start()
    print('=== Start ===')
    # 日常
    DailyTasks()
    print('=== end ===')
    os._exit(0)


if __name__ == '__main__':
    RunAutoAL()
