from urllib import request
import urllib
import re

url = "http://www.baidu.com/s?"
word = {"wd":"武汉"}
wd = urllib.parse.urlencode(word)
url = url + wd
print(url)

req = request.Request(url)
resp = request.urlopen(req).read().decode()
part = "<title>(.*?)</title>"
data = re.findall(part,resp)
print(data[0])
