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

@allure.feature("离线视频分析接口")
class TestVideoAnaly:
    @allure.story("上传视频的接口")
    @allure.title("调用的函数：test_videoUpload")
    #@allure.attach.file("上传的待分析的视频",'testJiTui.mp4',allure.attachment_type.MP4)
    @pytest.mark.parametrize('url,body,fileParam,expResult', read_file_excel('videoAnalysis', 'videoUpload'))  # 数据驱动装饰器
    def test_videoUpload(self, url, body, fileParam, expResult):
        res = requests.post(url=url, data=body, files=fileParam)  # body是data格式
        assert res.json()['code'] == int(expResult)

    # @allure.story("视频分析的接口")
    # @pytest.mark.parametrize('url,header,body,expResult', read_excel('videoAnalysis', 'videoAnalysis'))  # 数据驱动装饰器
    # def test_videoAnalysis(self, url, header, body, expResult):
    #     print('body type----',type(body))
    #     res = requests.post(url=url, headers=header, json=body)
    #     assert res.json()['code'] == int(expResult)


# if __name__ == '__main__':
#     # pytest.main(['test_sysUser.py','-s','--html=../report/html/bridge.html'])
#     # pytest.main(['test_sysUser.py', '-s','--lf','--html=../report/html/bridge.html']) # 只执行上次失败的测试用例
#     # pytest.main(['-s','-v','test_videAnalysis.py::TestVideoAnalysis::test_videoUpload',   '--alluredir', '../reports/allure'])
#     pytest.main(['-s', '-v', 'test_videAnalysis.py', '--alluredir', '../reports/allure'])