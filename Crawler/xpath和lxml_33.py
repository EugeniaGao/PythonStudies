from lxml import etree

# 需要安装 lxml模块来支持xpath的操作
# 解决字符串形式html
text = '''
        <div>
            <ul>
                <li class="item-0"><a href="link1.html">张三</a></li>
                <li class="item-1"><a href="link2.html">李四</a></li>
                <li class="item-3"><a href="link3.html">王五</a></li>
                <li class="item-4"><a href="link4.html">赵六</a></li>
                <li class="item-5"><a href="link5.html">沈七</a></li>
            </ul>
        </div>
        '''

html = etree.HTML(text)
result = etree.tostring(html,encoding="utf8").decode()
print(result)