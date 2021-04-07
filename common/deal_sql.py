import pymysql  # 导包，目的建立数据库的连接
import random
import pytest
import requests
from config.conf import sql_conf  # 导入数据库连接的参数



def get_sql(sql):
    '''
    :param sql: 运行查询的sql语句
    :return: 返回查询出来的数据
    '''
    host,user,password,database,port,charset=sql_conf() # 导入值保存到对应的参数变量
    # print("host__:",host)
    #建立一个连接对象
    db=pymysql.connect(host=host,user=user,password= password,database =database,port=3306,charset='utf8')
    #建立一个游标
    cursor=db.cursor()
    # 运行sql语句
    cursor.execute(sql)
    # 把sql运行数据保存在data变量里
    data=cursor.fetchall() # 获取查询出的所有的值
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()
    # print('get_sql中返回的查询数据：---','data')
    return data

# if __name__ == '__main__':
# userName = "用户名39157831"
# newSql = f"select id from sys_user where user_name='{userName}'"  # 新增用户成功后，查询到该数据的id
# newId = get_sql(newSql)
# print("newId")



    # print(type(id))
    # id = userId[0]   # 从元组中取出用户id的格式是整数
    # print("用户的id",id)


