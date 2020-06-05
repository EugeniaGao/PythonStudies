import requests
import re

proxy = {
    "http":"http://123.139.56.238:9999"
}

url = "http://www.baidu.com"

resp = requests.get(url=url,proxies=proxy).content.decode()
pat = "<title>(.*?)</title>"
data = re.findall(pat,resp)
print(data[0])