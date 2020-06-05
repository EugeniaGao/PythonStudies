import re

# 匹配固定次数
# {n} 前面的原子出现了几次
# {n,} 至少出现了几次
# {n,m} 前面原子出现次数介于n到m之间

d = "1237ls895sa"
pat1 = "\S{8,10}"   # 匹配8到10个非空字符
pat2 = "\d{4}"      # 匹配前4位数字

print(re.search(pat1,d))
print(re.search(pat2,d))