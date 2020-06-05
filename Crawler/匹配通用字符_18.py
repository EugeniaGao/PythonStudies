import re

# \w 任意字母、数字、下划线
# \W 和小写w相反
# \d 十进制数字
# \D 非十进制数字
# \s 空白字符
# \S 非空白字符

a = "@@@@love521"
pat = "\W\w\w"
pat2 = "\w\w\w"

result = re.findall(pat,a)
result2 = re.findall(pat2,a)
print(result)
print(result2)