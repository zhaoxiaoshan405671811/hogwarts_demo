#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:xiaoshan
# datetime:2020-08-05 19:10
# software: PyCharm
"""
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""
#定义方法
def games():
    # 定义变量
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 199
    #循环计算血量
    while True:
        my_hp = my_hp - your_power#定义我的血量公式
        your_hp = your_hp - my_power#定义你的血量公式
        print(my_hp)#打印出我的血量
        #判断，如果我的血量小于等于0时代表我输了，你的血量小于等于0时代表你输了
        if my_hp <= 0:
            print("我输了")
            break
        elif your_hp <= 0:
            print("你输了")
            break
games()#调用games方法