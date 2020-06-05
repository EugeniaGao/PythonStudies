from lxml import etree

html = etree.parse("F:\html\html\index.html")

# result = html.xpath("//li[@class='item-8']")   # 获取li标签下属性为 "item-8"的值
#
# print(result[0].text)

result = html.xpath("//li/a[@href='link2.html']")   # 获取li标签下子标签a的属性 /后面跟子标签
print(result[0].text)

