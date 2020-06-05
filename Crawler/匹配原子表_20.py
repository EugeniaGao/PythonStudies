import re

#　原子表
#　定义一组平等的原子

phone = "15580465758"

pat = "1[3578]\d\d\d\d\d\d\d\d\d"   # [3578] 每个数值都是平等的，独立的，不能组合

ret = re.findall(pat,phone)
print(ret)