#
# 注释
'''
注释
'''

""" 注释
注释
"""
# 输入默认是string
a = input("请输入一个王八")
print(a)

#int 类型需要强制转换
# b = int(input("输入数字1："))
# c = int(input("输入数字2："))
# print(b+c)
a = 1/3
print(a)
print(5//2)

#解构赋值
b,a=10,20
print(a)
print(b)
#交换两个变量的值
b,a=a,b
print(a)
print(b)

#比较运算符
a = 56
b = 56
print(a == b)  #比较value
print(a is b)  #比较id的类型  is not
print(id(a))

c = range(10)
print(list(c))

# 布尔运算符
# and --》&&
# or  --》||
# not --》 ！ 取反
# in  --》判断一个字符串是否被另外一个字符串包含
a = 'Wang'
b = 'a'
print(a in b)
print(b in a)

# bool() 函数。python每个对象都有一个布尔类型属性，通过bool()获取
# 只有极少数特殊值是false,其余都是true
ste = 'Essa'
print(bool(ste)) # true

print(bool(0))  #false
print(bool({}))  #false
print(bool([]))  #false






