import requests
from lxml import etree

url = "https://www.qiushibaike.com/"

header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/74.0.3729.157 Safari/537.36"
}

resp = requests.get(url=url,headers=header).text

html = etree.HTML(resp)

result = html.xpath("//div//a[@class='recmd-content']/href")

print(result)