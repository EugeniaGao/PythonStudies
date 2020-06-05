import requests
import re
import time

# 第一页 http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20
# 第二页 http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
# 播放地址 http://f2.htqyy.com/play7/206/m4a/11
#         http://f2.htqyy.com/play7/211/mp3/11

songName = []
songId = []
for i in range(0,1):
    url = "http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"
    resp = requests.get(url).text
    pat1 = 'title="(.*?)" sid'
    pat2 = 'sid="(.*?)"'

    titleList = re.findall(pat1,resp)
    sidList = re.findall(pat2,resp)

    songName.extend(titleList)
    songId.extend(sidList)


for i in range(0,len(songId)):
    songUrl = "http://f2.htqyy.com/play7/"+str(songId[i])+"/mp3/11"
    name = songName[i]
    print("开始下载第",i+1,"首歌")
    data = requests.get(songUrl).content

    with open("E:\music\{}.mp3".format(name),"wb") as f:
        f.write(data)
    time.sleep(0.5)

print("下载完成，欢迎您的使用！")