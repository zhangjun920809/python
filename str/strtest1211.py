#字符串的比较
s1='hello'
s2='hello3'
print(s1 > s2) #false
print(s1 < s2) # true
print(s1 == s2)
print(s1 != s2)

# ord()转为ASCII码对应得数字  chr() 相反
print(ord('a')) #97
print(chr(97))  # a

#字符串的切片,和列表的切片操作相同。 s[start:end:step]
s3='nishiyizhixiaomiaolv'
print(s3[:8])

#格式化字符串  3种方式
name='yonggge'
age=99
print('你是%s,现在%d' %  (name,age))        #你是yonggge,现在99
print('你是{0}，今年{1}'.format(name,age))  #你是yonggge，今年99
print(f'你是{name},今年{age}')              #你是yonggge,今年99   前面要加 f