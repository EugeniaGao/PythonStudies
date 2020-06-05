import requests
import re

url = "http://www.baidu.com"

# requests.get(url).text 返回的是字符串，requests.get(url).content 返回的是二进制数据
resp = requests.get(url).content.decode()
pat = "<title>(.*?)</title>"
result = re.findall(pat,resp)
print(result[0])