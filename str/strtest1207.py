#字符串查询操作,f返回第一个字符的下标
# index() 查不到时会报错  find()  会返回-1
s1 ='hello,java,java'
print(s1.index('ja')) # 6   第一个
print(s1.rindex('ja'))# 11  最后一个
print(s1.find('ja'))  # 6  第一个
print(s1.rfind('ja'))# 11  最后一个

# 大小写转换
s1 ='hEllo,JAVA,java'
print(s1.upper())   # HELLO,JAVA,JAVA
print(s1.lower())   # hello,java,java
print(s1.swapcase()) # HeLLO,java,JAVA  大小写互转
print(s1.title())   # Hello,Java,Java  每个单词第一个字母大写，其余小写
print(s1.capitalize()) # Hello,java,java  第一个字符转大写，其余小写

# 字符串对齐
s1 ='hEllo,JAVA,java'
print(s1.center(25,'*'))  # *****hEllo,JAVA,java*****  长度25，居中，不够的使用 * 替代。 * 不写时，默认空格
print(s1.ljust(25,'*'))   # hEllo,JAVA,java**********
print(s1.rjust(25,'*'))  # **********hEllo,JAVA,java**
print(s1.zfill(25))      # print(s1.zfill(25)) 右对齐，使用0 填充

# 字符串劈分操作，返回结果是一个列表
s1 ='hEllo,JAVA,java'
print(s1.split())       # ['hEllo,JAVA,java']  默认使用空格
print(s1.split(','))    # ['hEllo', 'JAVA', 'java']  指定 ‘，’
s2 ='hEllo|JAVA|java|haha'
print(s2.split(sep='|',maxsplit=2))  # 使用 | 分隔，maxsplit=2 表示只分2次
# 等效上面方法
print(s2.split('|',2))

#字符串的替换与合并
s1 ='hEllo,JAVA,java'
print(s1.replace('java','c++'))  # hEllo,JAVA,c++   java 替换为 c++
print('*'.join(s1))   # h*E*l*l*o*,*J*A*V*A*,*j*a*v*a   以 * 作为分隔符，将s1字符串合并成一个新字符创

# 字符串的判断