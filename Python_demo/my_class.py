#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:xiaoshan
# datetime:2020-08-10 16:05
# software: PyCharm
"""
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
"""
class Dog:
    #静态变量
    dog_color = "white"
    dog_character = "mild"
    dog_eye = "blue"
    dog_size = "smaller"
    dog_hair = "curvy"
    #动态变量
    def Barking(self):
        print("汪汪")
    def run(self):
        print("来回跑")
    def __init__(self):#构造函数，实例化类的时候直接调用
        print(self.dog_character)
        print(self.dog_color)
        print(self.dog_eye)
        print(self.dog_hair)
        print(self.dog_size)
demu_dog = Dog()
demu_dog.dog_size = "大狗"
demu_dog.dog_eye ="黄色"
print(demu_dog.Barking())
print(demu_dog.run())
sugel_dog = Dog()