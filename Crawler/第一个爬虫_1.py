# from urllib import request
# import re
#
#
# url = "http://www.baidu.com"
#
# req = request.Request(url)
# resp = request.urlopen(req).read().decode()
#
# part = "<title>(.*?)</title>"
# data = re.findall(part,resp)
# print(resp)
# # print(data[0])
#

from urllib import request
url = "http://www.shigaogui.com/"
req = request.Request(url)
resp = request.urlopen(req).read().decode()

print(resp)