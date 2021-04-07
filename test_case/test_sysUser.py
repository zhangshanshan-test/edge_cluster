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


@allure.feature("用户管理接口")  # 说明需求
class TestSysUser:

    # 生成一个随机却不能重复的用户名
    def get_randName(self):
        id = (1)    # 将用户的id定义成一个元组(因为查询数据库返回的数据格式是元组)
        userName = ""
        while id:  #
            userName = f"用户名{random.randint(99, 111111111)}"  # 配置的用户名是“用户名+8位随机数据”组成的
            userSql = f"select id from sys_user where user_name='{userName}'"  # 查询用户id的sql
            id = get_sql(userSql)  # 从数据库中查询出来的数据格式是双层元组格式，需要进一步处理
        print("前置的获取随机用户名：----",userName)
        return userName

    @allure.step("前置：新增一个名字不能重复的用户名")
    def addRelUser(self):
        excelData = read_excel('sysUser','addSysUesr_01')  # 读取的数据是格式是 列表里面套元组
        randName = self.get_randName() # 更新接口请求参数的值
        excelData[0][2]['userName'] = randName
        res = requests.post(url=excelData[0][0], headers=excelData[0][1], json=excelData[0][2])
        if res.json()['code'] == int(excelData[0][3]):
            newSql= f"select id from sys_user where user_name='{randName}'"   # 新增用户成功后，查询到该数据的id
            newId = get_sql(newSql)   # 从数据库取出的数据格式是双层元祖格式：((282,),)
            print("前置：新增用户成功")
            return newId[0][0], randName
        else:
            pass
            print("Error:前置：新增用户失败")

    @allure.story("新增用户接口")
    @allure.title("调用的函数：test_addUser")
    @pytest.mark.parametrize('url,header,body,expResult', read_excel('sysUser','addSysUesr'))  # 数据驱动装饰器
    def test_addUser(self, url, header, body, expResult):
        res = requests.post(url=url, headers=header, json=body)
        assert res.json()['code'] == int(expResult)

    @allure.story("获取用户列表接口")
    @allure.title("调用的函数：test_getUserList")
    @pytest.mark.parametrize('url,header,body,expResult', read_excel('sysUser','userList'))  # 数据驱动装饰器
    def test_getUserList(self, url, header, body, expResult):
        # print('inbody22---', body)
        # print('bodyt的类型---', type(body))
        res = requests.post(url=url, headers=header, json=body)
        # print('expResult---', int(expResult))
        # print('expResult的类型---', type(expResult))
        # print('res.text---', res.text)
        # print('res.json22---', res.json())
        assert res.json()['code'] == int(expResult)

    # @pytest.mark.dependency(depends=['test_addUser'])
    @allure.story("删除用户接口")
    @allure.title("调用的函数：test_delUser")
    @pytest.mark.parametrize('url,header,body,expResult', read_excel('sysUser','delUser'))  # 数据驱动装饰器
    def test_delUser(self, url, header,body,expResult):
        # print("开始执行删除用户接口")
        # strs = MaxId
        if MaxId not in url:  # 判断id是否存在于数据库中，默认maxId = 99999999 是不存在数据库中的
            mySql = 'select id from sys_user ORDER BY id DESC limit 1 '
            userId = get_sql(mySql)[0][0]  # 从数据库中取出的数据格式是元祖，提取值是整数
            print("返回的id的类型是：：",type(userId))
            if userId :
                url = url + str(userId)  # 拼接成新的url
                print("url33---", url)
            else:
                print("error:--删除用户数据时没有找到对应的用户id")
        else:
            url = url
            #print("url44---", url)
        #print("最终的url--", url)
        res = requests.post(url=url, headers=header)   # 如果excel表中url含有字符串“/99999999”则直接使用原来的url
        assert res.json()['code'] == int(expResult)

    @allure.story("更新用户接口")
    @allure.title("调用的函数：test_updateUser")
    @pytest.mark.parametrize('url,header,body,relParam,expResult', read_relParam_excel('sysUser', 'updateSysUesr'))  # 数据驱动装饰器
    def test_updateUser(self, url, header, body, relParam,expResult):
        if relParam == "":
            print("依赖数据为空：",body)
            userId, userName = self.addRelUser()  # 新增一条数据并返回查询出来用户id 和 name
            body['id'] = userId  # 将请求参数中的id修改成新增数据中的id
            body[relParam] = userName  # 根据表中依赖的参数，修改对应的键值
        elif relParam == "userName" and body[relParam]: # 依赖的数据是 userName 且不为空
            userId, userName = self.addRelUser()  # 新增一条数据并返回查询出来用户id 和 name
            body['id'] = userId  # 将请求参数中的id修改成新增数据中的id
            body['userName'] = self.get_randName()  # 将请求题中的用户名设置成一个随机且不重复的名称
        elif body[relParam] == "": # 依赖的数据是 userName 且不为空
            userId, userName = self.addRelUser()  # 新增一条数据并返回查询出来用户id 和 name
            body['id'] = userId  # 将请求参数中的id修改成新增数据中的id
        else:
            pass
        res = requests.post(url=url, headers=header, json=body)  # 不更改任何数据，再次用相同数据请求一次，不会报错
        assert res.json()['code'] == int(expResult)
#
# if __name__ == '__main__':
# #     # pytest.main(['test_sysUser.py','-s','--html=../report/html/bridge.html'])
# #     # pytest.main(['test_sysUser.py', '-s','--lf','--html=../report/html/bridge.html']) # 只执行上次失败的测试用例
# #     pytest.main(['-s','-v','test_sysUser.py::TestSysUser::test_updateUser',   '--alluredir', '../reports/allure'])
# #     # pytest.main(['test_sysUser.py', '-s', '--alluredir','./report/xml'])
#    pytest.main(['../test_case/','--html = ../reports/reports.html'])