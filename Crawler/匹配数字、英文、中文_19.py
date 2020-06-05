import re

#　数字 [0-9]
#  英文 [a-z][A-Z]
#  中文 [\u4e00-\u9fa5]

d = "@#$天华%$%#@hua##$30@@$%%$@#"
pat1 = r"[\u4e00-\u9fa5][\u4e00-\u9fa5]"
pat2 = "[a-z][a-z][a-z]"
pat3 = "[0-9][0-9]"

r1 = re.findall(pat1,d)
r2 = re.findall(pat2,d)
r3 = re.findall(pat3,d)

print(r1,r2,r3)