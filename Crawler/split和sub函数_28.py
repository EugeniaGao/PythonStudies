import re

course = "hello--java---python--------html"

str = "hello 123, hello 45678"

pat = re.compile("-+")

pat2 = re.compile("\d+")

data1 = re.split(pat,course)

data2 = re.sub(pat2,"python",str)

print(data1)

print(data2)