import re

# 贪婪模式和非贪婪模式
# 贪婪模式：在整个表达式匹配成功的情况下，尽可能多的匹配
# 非贪婪模式：在整个表达式匹配成功的情况下，尽可能少的匹配(?)
# python 默认是贪婪模式

str = "aa<div>test1</div>bb<div>test2</div>cc"

pat1 = "<div>.*</div>"
pat2 = "<div>.*?</div>"     # 加?号表示非贪婪模式

print(re.search(pat1,str))  # 默认贪婪模式
print(re.search(pat2,str))

