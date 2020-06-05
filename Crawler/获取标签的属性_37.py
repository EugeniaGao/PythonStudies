from lxml import etree

html = etree.parse("F:\html\html\index.html")

result = html.xpath("//li/a/@href")  # 获取li标签的子标签a的属性

print(result[0])