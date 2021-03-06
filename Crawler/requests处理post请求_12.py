import requests
import re

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/74.0.3729.157 Safari/537.36"
}

def translate(word):
    formData = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": "15743852053759",
            "sign": "ed321b7a1a272d40683db656b14101f2",
            "ts": "1574385205375",
            "bv": "8abad98ac3cc0d8b8b9110b5dac6fe6a",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
    }

    # post请求用data, get请求用param
    resp = requests.post(url=url,headers=header,data=formData).text
    pat = '"tgt":"(.*?)"'
    data = re.findall(pat,resp)
    print(data[0])


if __name__ == '__main__':
    word = input("请输入要翻译的内容：")
    translate(word)
