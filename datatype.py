# python数据类型
# 整数类型 integer 简写为int
# 浮点类型 float
# 布尔类型 bool
# 字符串类型 str
# 可通过属性的 type() id() 函数，获取属性的类型和内存地址
n1 = 90;
print(n1, type(n1))

# 0b 0o 0x分别代表二进制，八进制，十六进制
print('二进制', 0b111100)
print('十进制', 28)
print('八进制', 0o176)
print('十六进制', 0x180)

# 浮点类型
# 浮点型计算是不精确的
a = 2.3325
print('类型', type(a))

# 浮点型运算需要引入Decimal
from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))

# python中的boolean类型可以转换为 0(false) 和 1(true)
f1 = True
f2 = False
print(f1 + f2)
print(f1 + f1)

# python字符串表示形式： ''  ""  """"""  ‘’‘’‘’，三个单双引号的可以不在同一行。
str1 = '人生苦短'
str2 = "人生苦短"
str3 = """人生苦短
我用jj"""
print(str1)
print(str2)
print(str3)

# 数据类型转换
name = "小王八"
age = 20
print(type(name), type(age))
# 下面写法会报错  python 不能把int类型和str类型拼接.需要转型 str()函数
# 类似的 int() float()
# print('我叫王二' + name + '今年：' + age +'岁')
print('我叫王二' + name + '今年：' + str(age) + '岁')
