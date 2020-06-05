import re

# 匹配多个表达式 |
phone = "13580465756"
b = "020-1234567"
pat1 = "1[3578]\d{9}"
pat2 = "\d{3}-\d{7}"

pat3 = "1[3578]\d{9}|\d{3}-\d{7}"  # 将两个表达式用|连接起来

# print(re.search(pat1,phone))
print(re.search(pat3,phone))

