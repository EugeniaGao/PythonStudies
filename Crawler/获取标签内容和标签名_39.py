from lxml import etree

html = etree.parse("F:\html\html\index.html")

#　获取倒数第二个li元素下a的内容
result = html.xpath("//li[last()-1]/a")
print(result[0].text)
result2 = html.xpath("//li/a")
print(result2[-2].text)

# 获取class值为bold的标签名

result3 = html.xpath("//*[@class='bold']")

print(result3[0].tag)  # tag 获取标签名

