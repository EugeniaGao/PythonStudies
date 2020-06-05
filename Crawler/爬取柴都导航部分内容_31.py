import re
import requests

url = "http://www.chaidu.com/"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/74.0.3729.157 Safari/537.36"
}

resp = requests.get(url=url,headers=header).text
print(resp)

pat = '<div id="submit" class="submit">[\s\S]*?<input[\s\S]*?value="(.*?)"[\s\S]*?<input[\s\S]*?value="(.*?)"[\s\S]*?' \
      '<input[\s\S]*?value="(.*?)"[\s\S]*?<input[\s\S]*?value="(.*?)"[\s\S]*?<input[\s\S]*?value="(.*?)"[\s\S]*?' \
      '<input[\s\S]*?value="(.*?)"[\s\S]*?<input[\s\S]*?value="(.*?)"[\s\S]*?<input[\s\S]*?value="(.*?)"[\s\S]*?' \
      '<input[\s\S]*?value="(.*?)"[\s\S]*?<input[\s\S]*?value="(.*?)"[\s\S]*?<input[\s\S]*?value="(.*?)"[\s\S]*?' \
      '<input[\s\S]*?value="(.*?)"[\s\S]*?'

p1 = re.compile(pat)
data = re.findall(p1,resp)
print(data[0])