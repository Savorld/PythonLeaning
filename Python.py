Python高级
1.用过的标准库和第三方库？
	
	标准库：logging/re/math/timeit/functiontools/
			threading/multiprocessing/Queue
			os/sys/
			sha/hashlib/json
	
	第三方：Django/Tornado/
			MySQLdb/Torndb/redis
			PIL/pillow/whoosh/jieba
			BeautifulSoup/requests

2.装饰器：
	2.1 命名空间：
		http://python.jobbole.com/81683/
		全局变量能够被函数访问
		如果是可变数据类型(如list, dict)甚至能够被更改,但是赋值不行
		函数调用时开辟，结束时销毁
	2.2 类装饰器：

3.迭代器：

4.Object Oriented：
	4.1 私有属性

	4.2 私有方法

5.函数：
	5.1 *args:接收参数，保存为元组，**kwargs:接收键值对，保存为字典

6.类：
    不可变基础类型:数字，字符串，元组
    可写属性的删除：del modname.attr
    命名空间的机制：
