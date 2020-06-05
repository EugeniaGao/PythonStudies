from urllib import request

url = "http://i.baidu.com"

# 加上 Cookie 等效于用账号密码登录
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/74.0.3729.157 Safari/537.36",

    "Cookie":"BAIDUID=D74F21D5B9A919D3EF4F2F9C1E693EC2:FG=1; BIDUPSID=D74F21D5B9A919D3EF4F2F9C1E693EC2; "
             "PSTM=1574227585; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=kF0dlJ5cVhMWEdYN0ZCZHp1NmpOR3V5clpQe"
             "DdZeXhjUzhQenBTdDJxbXVYZnhkRVFBQUFBJCQAAAAAAAAAAAEAAACtj~G3AAAAAAAAAAAAAAAAAAAAAAAAA"
             "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK7Q1F2u0NRdR; "
             "H_PS_PSSID=1451_21101_29568_29220_26350; delPer=0; PSINO=2; ZD_ENTRY=empty; "
             "PHPSESSID=5v50kpa9v5sb9jp1p8kmek1385; Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1574319952; "
             "Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1574319952"
}

req = request.Request(url=url,headers=header)
resp = request.urlopen(req).read().decode()
print(resp)