import requests
import json

#请求api地址
url ="http://localhost:8000/restful"
#请求参数
data={'indexCode':'1400000XXXXXXX'}
#执行请求
response= requests.get(url)#,params=data)
#查看执行的url
print('\n查看请求执行的url:\n',response.url)
#获得请求的内容
print('\n获得请求的内容:\n' , response.text)
#解析获取的json数据
data_json = json.loads(response.text)
print('\n解析获取json中data的值:\n',data_json[:])