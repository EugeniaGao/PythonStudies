from urllib import request
import re

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/74.0.3729.157 Safari/537.36"
}
req = request.Request(url=url,headers=header)
resp = request.urlopen(req).read().decode()

pat1 = '"rating":\["(.*?)","\d+"\]'    # [] 前面加一反斜杠起转译作用
pat2 = '"title":"(.*?)"'

data1 = re.findall(pat1,resp)
data2 = re.findall(pat2,resp)

for i in range(0,len(data1)):
    print("排名:",i+1,"评分:",data1[i],"电影名称:",data2[i])


