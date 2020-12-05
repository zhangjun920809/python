
# 循环正常结束，没有执行break的时候，会执行else
for it in range(3):
    input('请输入密码：')
    if it == '888':
        print('输入正确')
        break
    else:
        print('输入错误：')
else:
    print('三次均输错')
"""
请输入密码：44
输入错误：
请输入密码：44
输入错误：
请输入密码：44
输入错误：
三次均输错
"""