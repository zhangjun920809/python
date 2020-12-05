
# if elif else
a = 55

if a == 55:
    print("a等于55")
elif a > 55:
    print("a大于55")
else:
    print("a小于55")

# 类似三元表达式的简单写法
print('a大于55' if a > 55 else 'a小于等于55')

#pass语句只是一个占位符，什么都不做，只是在需要些语句的地方使用。 一般在没有 想好 代码怎么写的时候使用

b = 'xiaowangba'
if 'bac' in b:
    pass
else:
    print('xiaowangbachiduole')

if 'xiao' in b:
    print("this id xaiomi ")
elif 'wan' in b:
    print ("this is wangbadan ")
else:
    print ("this is other")

# for 循环
for iter1 in range(0,10):
    if iter1%2 == 0:
        print(iter1)
        continue


lis = range(0,11)
# 打印时需要list()函数才能输出
print(list(lis))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lis2 = range(0,11,2)
print(list(lis2))
#[0, 2, 4, 6, 8, 10]

lis3 = range(4,11,2)
print(list(lis3))
#[4, 6, 8, 10]

print(8 in lis3)

print(8 not in lis3)