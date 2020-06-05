from urllib import request
import random as rand
import re

url = "http://www.baidu.com"

agent1 = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 " \
         "MicroMessenger/6.7.3(0x16070321) NetType/WIFI Language/zh_CN"

agent2 = "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 " \
         "(KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"

agent3 = "Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) " \
         "Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.10 (Baidu; P1 6.0.1)"

agentList = [agent1,agent2,agent3]

agent = rand.choice(agentList)
header = {
    "User-Agent":agent
}

req = request.Request(url=url,headers=header)
resp = request.urlopen(req).read().decode()
part = "<title>(.*?)</title>"
data = re.findall(part,resp)
print(agent)
print(data[0])