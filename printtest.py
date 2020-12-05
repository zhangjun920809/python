
print("hello\nword")

# 输出内容到指定文件   a+ 表示如果文件不存在就创建，如果存在就把内容追加到后面
fdl = open('C:/workspace/pyworkspace/text.txt', 'a+')
print('nimalegebi-----11111-------', file=fdl)
fdl.close()

#不换行输出
print('helle', 'nimei' ,'nidaye')
#helle nimei nidaye

# \t 制表符
print("nimei\thehe")

#输出的字符前面加 r 或者 R  表示字符串中转义字符不转义，原样输出。 注意：字符串结尾不能用 \ 结尾
print(r'nimeihe\rnige')

# 0b 开头表示二进制数据
print(chr(0b100111001011000))
# 结果：乘
print(ord('乘'))
# 结果：20056  即转成2进制的100111001011000

#输出python的关键字
import keyword
print(keyword.kwlist)

name = '俊哥'
print('类型', type(name))
print('所在内存中的地址', id(name))
print('值', name)