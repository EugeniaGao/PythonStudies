from urllib import request
import urllib

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/73.0.3683.103 Safari/537.36"
}

# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100

def loadPage(url,filename):
    print("正在下载",filename)
    req = request.Request(url=url,headers=header)
    resp = request.urlopen(req).read()
    return resp

def writePage(html,filename):
    print("正在保存...")
    with open(filename,"wb") as f:
        f.write(html)
    print("保存成功！")
    print("---------")

def tiebaSpider(url,begin,end):
    for page in range(begin,end+1):
        pn = (page-1)*50
        full_url = url + "&ie=utf-8&pn=" + str(pn)
        filename = "F:\第"+str(page)+"页.html"
        html = loadPage(full_url,filename)
        writePage(html,filename)

if __name__ == '__main__':

    word = input("请输入贴吧名：")
    begin = int(input("请输入起始页："))
    end = int(input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw":word})
    url = url + key

    tiebaSpider(url,begin,end)
    print("感谢您的使用！")
