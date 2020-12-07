# 元组的生成方式
#方式1
tu = ('hello',98,'zhnag')
print(tu ,type(tu))
#('hello', 98, 'zhnag') <class 'tuple'>

# 当元组只有一个元素时，必须使用下面的方法声明：
tu1=('jun',)
print(tu1 ,type(tu1))
#('jun',) <class 'tuple'>

#方式2  使用内置函数tuple()
tu2 = tuple(('hello',999,'nimei'))
print(tu2,type(tu2))
#('hello', 999, 'nimei') <class 'tuple'>

#创建一个空元组
te3 = tuple()
print(te3,type(te3))
#() <class 'tuple'>

#获取元组的元素 tu[下标]
tu4 = ('hello',98,'zhnag')
print(tu[2])
#zhnag

#元组的遍历
tu5 = ('hello',98,'zhnag')
for it in tu5:
    print(it)
"""
hello
98
zhnag
"""

#
tu6=('zhnag',[88,99],100)
lis = tu6[1]
print(lis)
lis.insert(1,109)
print(tu6)
#[88, 99]
#('zhnag', [88, 109, 99], 100)