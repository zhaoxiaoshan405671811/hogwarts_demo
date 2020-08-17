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
       datas_div = result['div']['datas_div']
       myids_div = result['div']['myids_div']
       mydata_sub = result['sub']['mydata_sub']
       myids_sub = result['sub']['myids_sub']
       mydata_mul = result['mul']['mydata_mul']
       myids_mul = result['mul']['myids_mul']
    return [mydatas,myids,datas_div,myids_div,mydata_sub,myids_sub,mydata_mul,myids_mul]
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
        result = round(self.cal.add(a,b),2)
        print(f"结果是{result}")
        assert re  == result
    @pytest.mark.parametrize(['a','b','re'],get_datas()[2],ids=get_datas()[3])
    def test_div(self,a,b,re):
        print("相除")
        result = round(self.cal.div(a,b),2)
        print(f"结果是{result}")
        assert re == result
    @pytest.mark.parametrize(['a', 'b', 're'], get_datas()[4],ids=get_datas()[5])
    def test_sub(self,a,b,re):
        print("相减")
        result = round(self.cal.sub(a, b),2)
        print(f"结果是{result}")
        assert re == result
    @pytest.mark.parametrize(['a', 'b', 're'], get_datas()[6],ids=get_datas()[7])
    def test_mul(self,a,b,re):
        print("相乘")
        result = round(self.cal.sub(a, b), 2)
        print(f"结果是{result}")
