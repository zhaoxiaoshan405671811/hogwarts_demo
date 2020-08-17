#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:xiaoshan
# datetime:2020-08-17 21:03
# software: PyCharm
import pytest
import yaml
from hogwarts_demo.Python_demo.demo_pytest.my_calculator.calculator import Calculators

def get_datas():
    with open('/Users/xiaoshan/PycharmProjects/hogwarts_demo/Python_demo/demo_pytest/datas/data.yml',encoding='utf-8') as f:
       result = yaml.safe_load(f)
       mydatas = result['add']['mydata']
       myids = result['add']['myids']
    return [mydatas,myids]
#print(get_datas())
class Testings():
    def setup_class(self):
        print("开始计算")
        self.cal = Calculators()
    def teardown_class(self):
        print("结束计算")
    @pytest.mark.parametrize(('a','b','re'),get_datas()[0],ids=get_datas()[1])
    def test_add(self,a,b,re):
        print("相加")
        print(self.cal)
        result = round(self.cal.add(a,b),2)
        print(f"结果是{result}")
        assert re  == result