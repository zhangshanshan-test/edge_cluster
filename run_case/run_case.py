# -*- coding:utf-8 -*-  
# @ Time     : 2021/4/7 15:58
# @ Author   : shanshan.zhang
# @ FileName : run_case.py
# @ Software : PyCharm
import pytest

if __name__ == '__main__':
#     # pytest.main(['test_sysUser.py','-s','--html=../report/html/bridge.html'])
#     # pytest.main(['test_sysUser.py', '-s','--lf','--html=../report/html/bridge.html']) # 只执行上次失败的测试用例
#     pytest.main(['-s','-v','test_sysUser.py::TestSysUser::test_updateUser',   '--alluredir', '../reports/allure'])
#     # pytest.main(['test_sysUser.py', '-s', '--alluredir','./report/xml'])
   # pytest.main(['../test_case/','--html = ../reports/reports.html'])
   # pytest.main(['../test_case/test_videAnalysis.py/', '--junitxml=../reports/reports.xml'])
   # pytest.main(['../test_case/test_videAnalysis.py/', '--alluredir', '../reports/allure'])
   '''
   在浏览器中查看生成的allure报告，需要两步
   第一步：在文件中执行：pytest.main(['../test_case/', '--alluredir', '../reports/allure0'])
   第二步：在命令端，进入到reports目录下，执行命令：allure generate ./allure0/ -o ./reporthtml/ --clean
   第三步：在文件中找到reporthtml/index.html,点击进入后，即可用浏览器打开
   
   '''
   pytest.main(['../test_case/', '--alluredir', '../reports/allure0'])
   # 进入到reports目录的路径下：allure generate ./allure0/ -o ./reporthtml/ --clean
