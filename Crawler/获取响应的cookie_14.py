import requests

url = "http://www.baidu.com"

resp = requests.get(url=url)
cookieJar = resp.cookies

cookie = requests.utils.dict_from_cookiejar(cookieJar)
print(cookie)