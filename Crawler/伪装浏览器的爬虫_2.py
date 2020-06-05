from urllib import request
import re

url = "http://www.baidu.com"

agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) " \
        "Mobile/16A366 MicroMessenger/6.7.3(0x16070321) NetType/WIFI Language/zh_CN"
header = {
    "User-Agent":agent
}

req = request.Request(url,headers=header)
resp = request.urlopen(req).read().decode()
part = "<title>(.*?)</title>"

data = re.findall(part,resp)
print(agent)
print(data[0])