#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:xiaoshan
# datetime:2020-08-17 19:26
# software: PyCharm,指定编码格式
from typing import List
import pytest
from hogwarts_demo.Python_demo.demo_pytest2.my_Calculation.calculation import Calculation
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
@pytest.fixture(scope='module')
def get_cla():
    print("开始计算")
    cal = Calculation()
    yield cal
    print("结束计算")