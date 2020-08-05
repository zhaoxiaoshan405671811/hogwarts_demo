#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:xiaoshan
# datetime:2020-08-05 20:24
# software: PyCharm
import random

def games():
    #初始化血量
    my_hp = 1000
    your_hp = 1000
    while True:
        #随机生成战力值
        my_power = random.randint(1, 200)
        your_power = random.randint(1, 200)
        print("我的血量",my_hp,"你的攻击力",your_power)
        print("你的血量",your_hp,"我的攻击力",my_power)
        my_hp = my_hp - your_power
        print("我的剩余血量",my_hp)
        your_hp = your_hp - my_power
        print("你的剩余血量",your_hp)
        if my_hp <= 0:
            print("我输了")
            break
        elif your_hp <= 0:
            print("你输了")
            break
games()