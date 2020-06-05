from lxml import etree

html = etree.parse("F:\html\html\index.html")

# result = html.xpath("//span")   # 获取所有span标签的信息，result是一个列表

result = html.xpath("//a")        # 获取 a 标签信息

print(result[4].text)