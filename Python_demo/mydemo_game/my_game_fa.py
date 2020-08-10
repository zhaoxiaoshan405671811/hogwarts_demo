#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:xiaoshan
# datetime:2020-08-10 16:27
# software: PyCharm
"""

    定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，

    see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
                如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”

    fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
                需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

    定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
    加入模块化改造

"""
class TongLao():
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power
    def see_people(self,name):
        if name=='无崖子':
            print("师弟！！！")
        elif name == '李秋水':
            print("呸，贱人")
        elif name == '丁春秋':
            print("叛徒！我杀了你")
    def fight_zms(self,your_hp,your_power):
        self.power = self.power*10
        self.hp = self.hp-self.hp*0.2
        print(self.power)
        print(self.hp)
        #while True:
        self.hp = self.hp - your_power
        your_hp = your_hp - self.power
        print(f"我的剩余血量{self.hp}")
        print(f"你的的剩余血量{your_hp}")
        if self.hp <your_hp:
            print("我输了")
        elif self.hp>your_hp:
            print("你输了")
