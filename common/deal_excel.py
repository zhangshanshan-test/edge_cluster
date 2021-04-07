# excel数据的读处理
import xlrd  # 导入读取excel操作的包
import json  # 字符串和字典进行转化
from config.conf import *

def get_excel(sheetName,caseName):
    '''
    # 读取文件的excel表中的数据,获取2个参数：url,checkData,主要是get请求
    :param sheetName: 表名
    :param caseName: 用例名
    :return:一个列表的嵌套元祖[(请求1:期望值1)，(请求2:期望值2)]
    '''
    resList = [] # 列表存放结果
    excel = xlrd.open_workbook(excelDir,formatting_info=True) # 打开excel
    # 根据sheet名获取sheet对象,formatting_info=True保持表的格式
    sheet = excel.sheet_by_name(sheetName)
    # print('sheet---',sheet)
    # 获取值，第3,10列
    idx = 0
    for one in sheet.col_values(0):
        if caseName in one:  # 说明这条用例是所需要了
            reqPath = sheet.cell(idx,3).value
            reqUrl = server_ip() + reqPath
            reqCheckData = sheet.cell(idx, 9).value
            # print('reqUrl---', reqPath)
            # print('reqPath的类型---', type(reqPath))
            # print('json.loads(reqHeader)....',json.loads(reqHeader))
            # 从excel中读取的是字符串格式（{}外带有引号），不能用键值去取值
            resList.append((reqUrl, reqCheckData))
            # reqUrl reqCheckData 是字符串格式
        idx += 1
        # print('idx---', idx)
    # print('读取标excel表中的list格式数据：',resList)
    return resList

def read_excel(sheetName,caseName):
    '''
    # 读取文件的excel表中的数据,获取4个参数：url,header,body,checkData
    :param sheetName: 表名
    :param caseName: 用例名
    :return:一个列表的嵌套元祖[(请求1:期望值1)，(请求2:期望值2)]
    '''
    resList = [] # 列表存放结果
    excel = xlrd.open_workbook(excelDir,formatting_info=True) # 打开excel
    # 根据sheet名获取sheet对象,formatting_info=True保持表的格式
    sheet = excel.sheet_by_name(sheetName)
    # print('sheet---',sheet)
    # 获取值，第3,6、7、10列
    idx = 0
    for one in sheet.col_values(0):
        if caseName in one:  # 说明这条用例是所需要了
            reqPath = sheet.cell(idx,3).value
            reqUrl = server_ip() + reqPath
            reqHeader = sheet.cell(idx, 5).value
            reqBody = sheet.cell(idx, 6).value
            reqCheckData = sheet.cell(idx, 9).value
            # print('reqBody：---', reqBody)
            # print('reqBody的类型---', type(reqBody))
            # print('json.loads(reqBody)....',json.loads(reqBody))
            # 从excel中读取的是字符串格式（{}外带有引号），不能用键值去取值
            resList.append((reqUrl, json.loads(reqHeader), json.loads(reqBody), reqCheckData))
            # reqUrl reqCheckData 是字符串格式
        idx += 1
        #print('idx---', idx)
    print('读取标excel表中的list格式数据：',resList)
    return resList

# 读取文件的excel表中的数据,获取5个参数:url,header,body,checkData,relatParam
def read_relParam_excel(sheetName,caseName):
    '''
    :param sheetName: 表名
    :param caseName: 用例名
    :return:一个列表的嵌套元祖[(请求1:期望值1)，(请求2:期望值2)]
    '''
    resList = [] # 列表存放结果
    excel = xlrd.open_workbook(excelDir,formatting_info=True) # 打开excel
    # 根据sheet名获取sheet对象,formatting_info=True保持表的格式
    sheet = excel.sheet_by_name(sheetName)
    # 获取值，第3,6、7、8、10列
    idx = 0
    for one in sheet.col_values(0):
        if caseName in one:  # 说明这条用例是所需要了
            reqPath = sheet.cell(idx,3).value
            reqUrl = server_ip() + reqPath
            reqHeader = sheet.cell(idx, 5).value
            reqBody = sheet.cell(idx, 6).value
            reqRelParam = sheet.cell(idx, 7).value
            reqCheckData = sheet.cell(idx, 9).value
            # 从excel中读取的是字符串格式（{}外带有引号），不能用键值去取值
            # print('reqUrl的类型---', type(reqUrl))
            # print('reqUrl---', reqUrl)
            # print('reqRelParam的类型---', type(reqRelParam))
            # print('reqRelParam---', reqRelParam)
            resList.append((reqUrl, json.loads(reqHeader), json.loads(reqBody), reqRelParam, reqCheckData))
            # reqUrl reqCheckData 是字符串格式
        idx += 1
        # print('idx---', idx)
    print('读取excel表中的list格式数据：', resList)
    return resList  # 格式是列表套元组

def read_file_excel(sheetName,caseName):
    '''
    文件上传数据的读取，包括path、body,文件参数fileParam，检验值checkData
    :param sheetName: 表名
    :param caseName: 用例名称
    :return: 一个列表的嵌套元祖[(请求1:期望值1)，(请求2:期望值2)]
    '''
    resList = [] # 列表存放结果
    excel = xlrd.open_workbook(excelDir,formatting_info=True) # 打开excel
    # 根据sheet名获取sheet对象,formatting_info=True保持表的格式
    sheet = excel.sheet_by_name(sheetName)
    # 获取值，第3、6、7、9、10列
    idx = 0
    for one in sheet.col_values(0):
        if caseName in one:  # 说明这条用例是所需要了
            reqPath = sheet.cell(idx,3).value
            reqUrl = server_ip() + reqPath
            # reqHeader = sheet.cell(idx, 5).value
            reqBody = sheet.cell(idx, 6).value
            reqFileParam = sheet.cell(idx, 8).value
            reqCheckData = sheet.cell(idx, 9).value
            # 从excel中读取的是字符串格式（{}外带有引号），不能用键值去取值
            print('excel函数reqUrl的类型---', type(reqUrl))
            print('reqUrl---', reqUrl)
            resList.append((reqUrl, json.loads(reqBody), json.loads(reqFileParam), reqCheckData)) # reqFileParam、reqBody的格式是字典
        idx += 1
        #print('idx---', idx)
    # print('读取excel表中的list格式数据：---', resList)
    return resList  # 格式是列表套元组