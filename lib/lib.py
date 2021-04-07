import random
# st = "/user/remove/99999999"
# a = "/99999999"
# re = a not in st
# print(re)
import requests
import json
def file():
    header={"Content-Type":"application/json;charset=UTF-8/json"}
    # header ={"Content-Type":"application/x-www-form-urlencoded"}
    body = [{"videoFolder":"1617774499258","sysAlgorithmList":[{"algorithmId":9,"algorithmName":"尾箱看管","algorithmCode":"AttendTailBox","algorithmTypeId":2,"createTime":"2021-02-02 11:17:05","editTime":"2021-02-02 11:17:05","alertLeve":"一级","sysEdgeAlgorithms":""},{"algorithmId":10,"algorithmName":"人离箱锁","algorithmCode":"PeopleLeaveBoxUnlock","algorithmTypeId":3,"createTime":"2021-02-02 11:17:54","editTime":"2021-02-02 11:17:54","alertLeve":"二级","sysEdgeAlgorithms":""}],"videoName":"RenLiXiangSuo.mp4"}]
    url= "http://192.168.1.100:8889/api/video/analysis"
    print('body的类型---', type(body))
    # print('body的类型---', type(files))

    print( 'body[0]...',body[0])
    print('body[0]的类型---', type(body[0]))
    b0 = body[0]
    bb= b0['sysAlgorithmList']
    print('bb的类型---', type(bb))
    print('bb---', bb)
    b0['sysAlgorithmList']=json.dumps(b0['sysAlgorithmList'])
    b2= json.dumps(b0)
    print('bb2的类型---', type(b0['sysAlgorithmList']))
    print('bb2---', b0['sysAlgorithmList'])
    # print( 'body[0][sysAlgorithmList]...',b0['sysAlgorithmList'])
    # print('body[0]的类型---', type(b0[''])
    # body[0]['sysAlgorithmList']= json.dumps(body[0]['sysAlgorithmList'])


    # print('d的类型---', type(body))
    # print('body---', body)
    # res= requests.post(url=url , headers= header, data=json.dumps(body))
    res = requests.post(url=url,headers= header, data=b2)
    return res.text

f = file()
print("f:____",f)

