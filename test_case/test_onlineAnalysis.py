# -*- coding:utf-8 -*-  
# @ Time     : 2021/4/6 11:37
# @ Author   : shanshan.zhang
# @ FileName : test_videAnalysis.py
# @ Software : PyCharm
import allure
import pytest
import requests
import ast
from common.deal_excel import *

@allure.feature("线上报警记录")
class TestVideoAnaly:
    @allure.story("历史报警记录查询接口")
    @allure.title("调用的函数：test_getHistoryAlarm")
    @pytest.mark.parametrize('url,header,body,expResult', read_excel('alarmRecord', 'getHistoryAlarm'))  # 数据驱动装饰器
    def test_getHistoryAlarm(self, url, header, body, expResult):
        res = requests.post(url=url, headers=header, json=body)  # body是data格式
        assert res.json()['code'] == int(expResult)

    @allure.story("查询当前报警记录分页列表")
    @allure.title("调用的函数：test_getDayAlarm")
    @pytest.mark.parametrize('url,header,body,expResult', read_excel('alarmRecord', 'getHistoryAlarm'))  # 数据驱动装饰器
    def test_getDayAlarm(self, url, header, body, expResult):
        res = requests.post(url=url, headers=header, json=body)  # body是data格式
        assert res.json()['code'] == int(expResult)



# if __name__ == '__main__':
#     # pytest.main(['test_sysUser.py','-s','--html=../report/html/bridge.html'])
#     # pytest.main(['test_sysUser.py', '-s','--lf','--html=../report/html/bridge.html']) # 只执行上次失败的测试用例
#     # pytest.main(['-s','-v','test_videAnalysis.py::TestVideoAnalysis::test_videoUpload',   '--alluredir', '../reports/allure'])
#     pytest.main(['-s', '-v', 'test_onlineAnalysis.py::TestVideoAnaly::test_getDayAlarm', '--alluredir', '../reports/allure'])