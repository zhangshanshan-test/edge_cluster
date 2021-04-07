# -*- coding:utf-8 -*-
# @ Time     : 2021/4/6 11:37
# @ Author   : shanshan.zhang
# @ FileName : test_videAnalysis.py
# @ Software : PyCharm

import pytest
import requests
import allure
from common.deal_excel import *
from common.deal_sql import *
from config.conf import *


@allure.feature("首页中各种统计接口")  # 说明需求
class TestSysCount:

    @allure.story("查找摄像头总数和在线摄像头总数")
    @allure.title("调用的函数：test_cameraCount")
    @pytest.mark.parametrize('url, expResult', get_excel('sysCount', 'cameraCount'))  # 数据驱动装饰器
    def test_cameraCount(self, url, expResult):
        res = requests.get(url=url)
        assert res.json()['code'] == int(expResult)
        print('main res.text  01---', res.text)

    @allure.story("查找盒子数量和在线数量")
    @allure.title("调用的函数：test_edgeCount")
    @pytest.mark.parametrize('url, expResult', get_excel('sysCount', 'edgeCount'))  # 数据驱动装饰器
    def test_edgeCount(self, url, expResult):
        res = requests.get(url=url)
        assert res.json()['code'] == int(expResult)
        print('main res.text 02---', res.text)

    @allure.story("查找当天新增摄像头数量")
    @allure.title("调用的函数：test_cameraDayCount")
    @pytest.mark.parametrize('url, expResult', get_excel('sysCount', 'cameraDayCount'))  # 数据驱动装饰器
    def test_cameraDayCount(self, url, expResult):
        res = requests.get(url=url)
        assert res.json()['code'] == int(expResult)
        print('main res.text 03---', res.text)

    @allure.story("查找当天的报警总数")
    @allure.title("调用的函数：test_alarmDayCount")
    @pytest.mark.parametrize('url, expResult', get_excel('sysCount', 'cameraDayCount'))  # 数据驱动装饰器
    def test_alarmDayCount(self, url, expResult):
        res = requests.get(url=url)
        assert res.json()['code'] == int(expResult)
        print('main res.text 04---', res.text)


# if __name__ == '__main__':
#     # pytest.main(['test_sysUser.py','-s','--html=../report/html/bridge.html'])
#     # pytest.main(['test_sysUser.py', '-s','--lf','--html=../report/html/bridge.html']) # 只执行上次失败的测试用例
#     pytest.main(['-s','-v','test_sysCount.py::TestSysCount',   '--alluredir', '../reports/allure'])
#     # pytest.main(['test_sysUser.py', '-s', '--alluredir','./report/xml'])
