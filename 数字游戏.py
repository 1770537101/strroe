'''
    猜数字游戏：
        1.系统随机产生一个随机数字（0~1000）
        2.用户从键盘输入数字，与随机数字进行比对 （让用户循环输入20）
            若大了：温馨提示，大了
            若小了：温馨提示，小了
            猜中
        3.循环：一直到猜中为止，退出程序。
    技术分析：
    1.随机数
        random
    2.input
    3.判断
        if ...elif ...else
    4.循环
        while : 当型循环条件型循环
    5.退出程序
        break
    任务：
        加入初始化金币功能，猜错1次扣500金币。
        猜中直接奖励10000，询问是否继续第二轮随机数猜测。

        10次没猜中，系统直接锁定。
'''
cs = 5000
cw = -500
zong = 10000
# 1.让系统随机产生一个随机数
import random
num = random.randint(0,1000)
count = 0
# 10此没猜中，系统直接锁定
i = 1
while i <= 10:
    count = count + 1
    # 2. 让用户数据
    chose = input("请输入本次猜的数字：")
    chose = int(chose)

    # 3.判断是否猜中
    if chose > num:
        cs = cs+cw
        print("大了！","剩余金币为",cs)
    elif chose < num:
        cs = cs+cw
        print("小了！","剩余金币为",cs)
    else:
        cs = cs+zong
        print("恭喜，本次猜中，本次幸运数字为：",num,"，本次猜了",count,"次","您现在有",cs,"金币", "是否进入下一轮随机猜数字游戏？？")
        break
    i = i + 1






