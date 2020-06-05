import requests

list1 = [
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baiduefghe.com",
    "http://www.baidu.com",
    "http://www.baidu.com"
]

i = 0
for url in list1:
    i = i+1
    try:
        requests.get(url)
        print("第",i,"次执行成功！")
    except Exception as e:
        print(e)