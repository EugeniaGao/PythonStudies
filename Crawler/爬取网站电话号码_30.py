import re
import requests

url = "http://changyongdianhuahaoma.51240.com/"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/74.0.3729.157 Safari/537.36"
}

resp = requests.get(url=url,headers=header).text
print(resp)
pat = '<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?</tr>'
pat2 = '<tr bgcolor="#EFF7F0">[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>'

name = re.findall(pat,resp)
num = re.findall(pat2,resp)

for i in range(0,len(name)):
    print(name[i]+" --> "+num[i])

