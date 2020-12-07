# 集合的创建
#方式1
se ={'zhnag',55,'nimei'}
print(se,type(se))
#{'zhnag', 55, 'nimei'} <class 'set'>

#方式2
# set 里面可以是列表，元组，字典，集合
se1 = set({'junjun','wang',246})
se2 = set([88,89,250])
se3 = set((55,66,77))
se4 = set({'55':55,'66':"jun",'77':99})
print(se1,type(se1))
print(se2,type(se2))
print(se3,type(se3))
print(se4,type(se4))
"""
{'wang', 246, 'junjun'} <class 'set'>
{88, 89, 250} <class 'set'>
{66, 77, 55} <class 'set'>
{'77', '55', '66'} <class 'set'>
"""

#定义一个空集合
se5 = set()

#判断某个元素是否在集合中 in,not in
se ={'zhnag',55,'nimei'}
print('zhnag' in se) #true
print('zhnag' not in se) # false

#集合的添加 add():一次添加一个,update()：一次至少添加一个,可以使可迭代对象
se ={'zhnag',55,'nimei'}
se.add('wang')
print(se)
#{'wang', 'nimei', 'zhnag', 55}
se.update(['列表','列表2'])
se.update(('元组','元组2'))
print(se)
#{'元组2', 'nimei', '元组', '列表2', 55, 'wang', 'zhnag', '列表'}

# 集合的删除方法 remove(),discard(), pop
se ={'zhnag',55,'nimei',66,'wangba','shouji'}
se.remove(55)  # 当要删除的元素不存在时，会报错
se.discard(66) # 当要删除的元素不存在时，不会报错
print(se)
#{'nimei', 'wangba', 'zhnag', 'shouji'}
se.pop()   # 会删除集合中最左边的元素
print(se)
{'wangba', 'zhnag', 'shouji'}

#清空集合
se.clear()
print(se)
#set()

# 判断两个集合是否相等 ==, !=。比较的是两个集合中元素是否相同
se6 ={22,66,88,33}
se7 ={33,88,66,22}
print(se6 == se7) # true
print(se6 != se7) # false

# 判断是否是子集 issubset()
se6 ={22,66,88,33}
se7 ={33,88,66,22,87,99}
print(se6.issubset(se7)) # true
print(se7.issubset(se6)) # false

# 判断是否是超集 issuperset(). (和上面的方法相反)
se6 ={22,66,88,33}
se7 ={33,88,66,22,87,99}
print(se7.issuperset(se6)) # true
print(se6.issuperset(se7)) # False

# 判断两个集合有没有交集 (是否包含相同的元素) 没有返回true  有返回false
se6 ={22,88}
se7 ={33,88,66,87,99}
se8 ={101,103}
print(se6.isdisjoint(se7))  # 有交集--> false
print(se7.isdisjoint(se8))  # 无交集 -->true