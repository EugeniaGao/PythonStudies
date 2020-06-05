import re

# compile函数-- 将正则表达式转换成内部结构，提高内部效率

str = "PYTHON666java"

pat = re.compile("python",re.I)  # re.I 忽略大小写
# pat = re.compile("\d{3}")

print(pat.search(str))

