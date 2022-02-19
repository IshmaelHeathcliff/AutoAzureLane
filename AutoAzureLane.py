from img import *


def WeighAnchor():
    CheckAndClickImg("img\weigh_anchor.png")


def Mainline():
    CheckAndClickImg("img\mainline.png")


def StartBattle():
    CheckAndClickImg("img\start.png")


def Back():
    CheckAndClickImg("img\\back.png")


def StartAgain():
    WaitImgLongTime("img\start_again.png")


def Exit_Notification():
    time.sleep(10)
    CheckAndClickImg("img\exit_notification.png")


def Home():
    CheckAndClickImg("img\home.png")


def Confirm():
    CheckAndClickImg("img\confirm.png")


def Skip():
    DoKeyDown("j")


def HardMode():
    WeighAnchor()
    Mainline()
    CheckAndClickImg("img\hard\hardmode.png")
    CheckAndClickImg("img\hard\hardmode12-1.png")
    StartBattle()
    StartBattle()
    Exit_Notification()
    for i in range(3):
        StartAgain()
    Home()


def ChallengeAt(n):
    if(CheckAndClickImg("img\challenge\challenge%d.png" % (n))):
        CheckAndClickImg("img\challenge\challenge%d-1.png" % (n))
        CheckAndClickImg("img\challenge\quick_battle.png")
        Skip()
        Back()
    CheckAndClickImg("img\challenge\\next_challenge.png")


def Challenge():
    WeighAnchor()
    CheckAndClickImg("img\challenge\challenge.png")

    for i in range(1, 6):
        ChallengeAt(i)

    Home()


def Fleet():
    CheckAndClickImg("img\\fleet\\fleet.png")
    CheckAndClickImg("img\\fleet\logistics.png")
    CheckAndClickImg("img\\fleet\\receive_reward.png")
    Skip()
    for i in range(3):
        CheckAndClickImg("img\\fleet\submit.png")
        Confirm()
        Skip()
    Home()


def ExecuteOperationTask():
    if(not CheckAndClickImg("img\operation\enter.png")):
        return
    time.sleep(2)
    CheckAndClickImg("img\operation\\auto.png")
    WaitImgLongTime("img\operation\leave.png", 20)
    CheckAndClickImg("img\operation\details.png")


def Intelligence():
    CheckAndClickImg("img\operation\intelligence.png")
    for i in range(2):
        CheckAndClickImg("img\operation\\battle_start.png")
        CheckAndClickImg("img\operation\\weigh_anchor.png")
        WaitImgLongTime("img\operation\confirm.png")
    CheckAndClickImg("img\operation\collect_reward.png")
    Skip()


def Operation():
    WeighAnchor()
    CheckAndClickImg("img\operation\operation.png")
    CheckAndClickImg("img\operation\details.png")
    CheckAndClickImg("img\operation\operation_tasks.png")
    CheckAndClickImg("img\operation\\accept_all.png")
    Back()
    while(CheckAndClickImg("img\operation\\find.png")):
        time.sleep(2)
        ExecuteOperationTask()
    Home()


def CatHouse():
    CheckAndClickImg("img\\cat\\living_area.png")
    CheckAndClickImg("img\\cat\\cat.png")
    CheckAndClickImg("img\\cat\\confirm.png")
    CheckAndClickImg("img\\cat\\cat_house.png")
    CheckAndClickImg("img\\cat\\cat_clean1.png")
    time.sleep(1)
    CheckAndClickImg("img\\cat\\cat_clean2.png")
    time.sleep(1)
    CheckAndClickImg("img\\cat\\cat_clean3.png")
    time.sleep(1)
    Skip()
    time.sleep(1)
    CheckAndClickImg("img\\cat\\cat_close.png")
    CheckAndClickImg("img\\cat\\cat_shop.png")
    CheckAndClickImg("img\\cat\\buy_cat.png")
    CheckAndClickImg("img\\cat\\confirm_buy_cat.png")
    time.sleep(2)
    Skip()
    Skip()
    CheckAndClickImg("img\\cat\\exit_cat.png")


def ReceiveAward():
    CheckAndClickImg("img\\tasks\\missions.png")
    CheckAndClickImg("img\\tasks\\receive_award.png")
    Skip()
    Home()


def DailyTasks():
    HardMode()
    Challenge()
    Fleet()
    Operation()
    CatHouse()
    ReceiveAward()

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
    # print('Wait to start...')
    # for i in range(30):
    #     print('%ds left...' % (30-i))
    #     time.sleep(1)
    print('=== Start ===')
    # Skip()
    # time.sleep(2)
    # Skip()
    # time.sleep(1)
    # Skip()
    # Home()
    # CheckAndClickImg("img\exit_notification.png")
    # 日常
    DailyTasks()
    print('=== end ===')
    os._exit(0)


if __name__ == '__main__':
    RunAutoAL()
