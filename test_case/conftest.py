# -*- coding:utf-8 -*-  
# @ Time     : 2021/4/1 11:18
# @ Author   : shanshan.zhang
# @ FileName : conftest.py
# @ Software : PyCharm
import pytest
import allure
import random
from common.deal_sql import get_sql

# 根据特定用户名访问登录接口，获取token
@allure.title("前置：登录")
@pytest.fixture(scope='session')
def login():
    # print(u'调用登录接口及数据')
    username = "admin"
    token = ""
    yield username,token
    # print("==登录成功，返回用户名和token==")

# name是随机产生不重复，调用新增用户接口，获取用户的id，用来关联删除用户接口和更新用户接口
@allure.title("前置：新增用户")
@pytest.fixture(scope="function")
def get_userId():
    userId = ()
    userName = ""
    while userId ==(): # 如果查询
        userName = f"用户名{random.randint(10000000, 99999999)}"  # 配置的用户名是“用户名+8位随机数据”组成的
        userSql = f"select id from sys_user where user_name='{userName}'"  # 根据生成的用户名来查询用户id的sql
        id = get_sql(userSql)  # 从数据库中查询出来的数据格式是元组格式，需要进一步处理
    id = userId[0][0]   # 从元组中取出用户id的格式是整数
    print("用户的id",id)
    yield userName,id




# 实际代码中使用的方法
# @pytest.fixture(autouse=True)
# def get_userinfo(login):
#     username,token = login
#     print(f"==打印用户名username：{username}和token:{token}==")