# 配置文件
import logging

excelDir = "../testData/edgeClusterData.xls"
MaxId = "99999999" # 将最大id号设置成常量

# def server_ip():
#     """
#     不同环境需要配置的ip地址
#     sit_ip：是sit环境的ip地址
#     dev_ip：是dev环境的ip地址
#     :return:
#     """
#     sit_ip="http://47.111.116.44:8001/api"
#     dev_ip="http://47.111.116.44:8001/api"
#     return sit_ip

# 字典格式保存的地址
def server_ip():
    server_address={
        "sit_ip": "http://192.168.1.100:8889/api",  # 银行设备管理平台的主机地址
        "dev_ip": "http://192.168.1.137"
    }
    return server_address['sit_ip']

# 数据库配置
def sql_conf():
    """
    host：数据库的ip地址
    user：数据库连接的用户名
    password：数据库连接密码
    database:连接的数据库名
    port:数据库连接端口
    charset:连接数据库字符编码格式 中文utf-8
    :return:返回数据库连接信息
    """
    host = "192.168.1.100"
    user = "root"
    password = "SHyunhua1234567890123"
    database = "visual_perception_platform"
    port = 3306
    charset= 'utf-8'
    return host,user,password,database,port,charset

# 日志文件的配置
LogDir = '../log/log.txt'       # 日志的存放目录
logging.basicConfig(level=logging.DEBUG,            # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',    # 日期格式
                    filename=LogDir,   # 日志输出文件
                    filemode='a')  # 追加模式