# 字典的创建
# 方式1
scores = {"zhang": 100, 200: "wang"}
print(scores)
print(type(scores))
# <class 'dict'>
# 第二种 dict() 函数
person = dict(name="zhang", age=20)
print(person)
# 创建一个空字典
d = {}

# 从dict中获取数据
# 元素不存在时不报错，输出None
print(scores.get("zhang1"))
# 元素不存在时报错
print(scores["zhang"])
# 元素不存在时 输出100
print(scores.get("zhang1", 100))

# key是否存在判断
print('zhang' in scores)
print('zhang' not in scores)

# 字典元素的删除
del scores["zhang"]
print(scores)
# 清空
scores.clear()

# 添加
scores1 = {"zhang": 100, "wang": 200}
scores1['wang2'] = 988
print(scores1)
# 修改
scores1["zhang"] = 109
print(scores1)

# 获取key  value  item
scores2 = {"zhang": 100, "wang": 200}
key=scores2.keys()
print(key)
print(list(key))
#dict_keys(['zhang', 'wang'])
#['zhang', 'wang']

val = scores2.values()
print(val)
print(list(val))
#dict_values([100, 200])
#[100, 200]

#包含的结果是元组类型 ('wang', 200)
ite = scores2.items()
print(list(ite))
#dict_items([('zhang', 100), ('wang', 200)])
#[('zhang', 100), ('wang', 200)]

