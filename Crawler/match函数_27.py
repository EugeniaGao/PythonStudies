import re

str = "python666java"

pat = re.compile("java")

data = re.match(pat,str)      # match从字符串的开始位置匹配，因开始位置是 py故匹配不上
data2 = re.findall(pat,str)   # findall 从任意位置开始匹配

print(data)
print(data2)