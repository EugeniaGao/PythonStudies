import re

names = "杨过、令狐冲、独孤求败、卓不凡、叶尘"
pat = "败"
result = re.search(pat,names)
print(result)
