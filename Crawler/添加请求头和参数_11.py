import requests
import re

url = "http://www.baidu.com/s?"

word = {"wd":"大北京"}

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/74.0.3729.157 Safari/537.36"
}

# params=word 相当于urllib.parse.urlencode({"wd":word})
resp = requests.get(url=url,params=word,headers=header).content.decode()
pat = "<title>(.*?)</title>"
data = re.findall(pat,resp)
print(data[0])

