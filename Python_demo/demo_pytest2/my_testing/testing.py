#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:xiaoshan
# datetime:2020-08-17 21:03
# software: PyCharm
import pytest
import yaml
# from hogwarts_demo.Python_demo.demo_pytest2.my_Calculation.calculation import Calculation
def get_datas():
    with open('/Users/xiaoshan/PycharmProjects/hogwarts_demo/Python_demo/demo_pytest2/datas/data.yml',encoding='utf-8') as f:
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
#获取数据
# @pytest.fixture(params=get_datas()[0],ids=get_datas()[])
# def get_datas(request):
#     return request.param
class Testings():
    # def setup_class(self):
    #     print("开始计算")
    #     self.cal = Calculation()
    # def teardown_class(self):
    #     print("结束计算")
    @pytest.mark.parametrize(('a','b','re'),get_datas()[0],ids=get_datas()[1])
    @pytest.mark.run(order=1)
    def test_add(self,get_cla,a,b,re):
        print("相加")
        result = round(get_cla.add(a,b),2)
        print(f"结果是{result}")
        assert re  == result
    @pytest.mark.parametrize(['a','b','re'],get_datas()[2],ids=get_datas()[3])
    @pytest.mark.run(order=4)
    def test_div(self,get_cla,a,b,re):
        print("相除")
        result = round(get_cla.div(a, b), 2)
        print(f"结果是{result}")
        assert re == result
    @pytest.mark.parametrize(['a', 'b', 're'], get_datas()[4],ids=get_datas()[5])
    @pytest.mark.run(order=2)
    def test_sub(self,get_cla,a,b,re):
        print("相减")
        result = round(get_cla.sub(a, b), 2)
        print(f"结果是{result}")
        assert result == result
    @pytest.mark.parametrize(['a', 'b', 're'], get_datas()[6],ids=get_datas()[7])
    @pytest.mark.run(order = 3)
    def test_mul(self,get_cla,a,b,re):
        print("相乘")
        result = round(get_cla.mul(a, b), 2)
        print(f"结果是{result}")
        assert re == result