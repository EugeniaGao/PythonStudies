import re

name = "python--python---python----python"

pat = re.compile("python")

data = re.finditer(pat,name)   # 将数据存入跌代器中

for i in data:
    print(i.group())           # 取出跌代器中的数据
