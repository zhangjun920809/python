#创建列表
#方式1
lis=['hello',90,333,'张']
print(lis)
# 方式2  使用list()函数
lis1 = list(['python',888,'nimei',888])
print(lis1)
#列表生成式
list6 = [i*i for i in range(2,7)]
print(list6)

# 获取指定元素的索引。 可指定开始查找的位置
ind = lis1.index(888)
ind1 = lis1.index(888,2)
print(ind)
print(ind1)

#list[2]  函数 获取指定索引位置的元素。 类似java
print(lis1[2])
#逆序索引  -1，代表最后一个元素
print(lis1[-1])

#列表切片，类似java从数组中复制一个新数组
# 语法list1[start:end:step] 开始：结束：步长
# 从下标0开始，3结束，不包含3
list2 = lis1[0:3]
list3 = lis1[::2]
list4 = lis1[1::2]
print(list2)
print(list3)
print(list4)

#判断元素是否存在
print(8888 in lis1)
print(8888 not in lis1)

#修改
lis1[2] = 777
print(lis1)
# 修改 0-1之间的元素
lis1[0:1]=[999,"000",444]
print(lis1)

#添加
#在下标1的位置插入555，原来的元素整体后移
lis1.insert(1,55555555)
#在list的末尾添加元素
lis1.append("wangba")
print(lis1)
# 将列表list2追加的list末尾
lis1.extend(list2)
print(lis1)

#删除
# 删除列表中第一个 “nimei”
lis1.remove("nimei")
print(lis1)
# pop删除指定下标的元素，如果不指定下标，则默认删除最后一个元素
lis1.pop(0)
print(lis1)
#clear 清空列表
#lis1.clear()
#print(lis1)
#del 列表名 --删除一个列表
print(list2)
del list2

#排序  如有无法排序的类型 报错
list5=[666,99,2,100]
list5.sort()
print(list5)


