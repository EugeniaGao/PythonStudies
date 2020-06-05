import re

file = "F:\天龙八部.txt"

with open(file,"rb") as f:
    data = f.read().decode()
    pat1 = "乔峰"
    pat2 = "萧峰"
    pat3 = "段誉"
    pat4 = "虚竹"

    n1 = re.findall(pat1,data)
    n2 = re.findall(pat2,data)
    n3 = re.findall(pat3,data)
    n4 = re.findall(pat4,data)

    print("乔峰出现次数：",len(n1+n2),"\n""段誉出现次数：",len(n3),"\n""虚竹出现次数：",len(n4))