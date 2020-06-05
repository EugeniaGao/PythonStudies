import re

str = "!@#$%aaaaaa^python1111@@java%$#$#%13580465756!!!!!"

s = "!@#$%aaaaaa^python1111@@java%$#$#%%我要自学网!!!!!"

# pat = "(python).*(java).*(1[3578]\d{9})"  # pat中加上括号

# pat2 = "%%(.*?)!!"  # 匹配 我要自学网

# print(re.search(pat,str).group(2))   # group(2) 2表示匹配第二个括号

# print(re.findall(pat2,s))

pat = "(python).*(java).*(135\d{8})"

print(re.search(pat,str).group(3))
