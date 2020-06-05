from lxml import etree

html = etree.parse("F:\html\html\index.html")

result1 = html.xpath("//li/a/span")  #　／　单斜杠表示紧邻的下一级子标签
result2 = html.xpath("//li//span")  # // 双斜杠表示li下所有子标签
result3 = html.xpath("//li/a//@class")  # 获取所有li标签下a标签下所有class属性

print(result1[0].text)
print(result2[1].text)
print(result3)