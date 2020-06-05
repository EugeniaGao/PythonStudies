from lxml import etree

html = etree.parse("F:\html\html\index.html")  # 本地html文件

result = etree.tostring(html,encoding="utf8").decode()

print(result)

