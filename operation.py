#创建字典
d = {} #这是创建空字典不是集合
keys = ['a','b','c','d']
values = [1,2,3,4]
d1 = dict(zip(keys,values))
d2 = dict.fromkeys(['d','e','f'])
d3 = dict(name='alex',age=31)
msg = """
d:%s
d1:%s
d2:%s
d3:%s
"""%(d,d1,d2,d3)
print(msg)

#查找元素
print(d1['a'])
print(d1.get('c',None))
print(d1.keys())
print(d1.values())
print(d1.items())

#添加元素
d1['g'] = 7
d1.update(d2)
ret = d1.setdefault('h',8) #若字典中存在'h'键则不修改其值并返回其值，若不存在则添加该键值对并返回 值8
print('ret:',ret)

#修改元素
d1['a'] = 11

#遍历字典
for keys,values in d1.items(): #此方法较耗时
    print(keys,values)

for keys in d1: #推荐此方法
    print(keys,d1[keys])
 
#排序
print(sorted(d1)) #给字典的键排序
d1 = sorted(d1.items(),key=lambda x:x[0]) #字典按“键”升序排序并输出
d1 = dict(d1)
print(d1) 
d1 = sorted(d1.items(),key=lambda x:x[1]) #字典按“值”升序排序并输出
d1 = dict(d1)
print(d1) 
    
#删除元素
del d1['a']  #若字典中不存在'a'键会报错
print(d1.pop('b',None)) #返回'b'对应的"值"，若字典中不存在'b'键则返回None
print(d1.popitem()) #随机删除字典中的任一键值对并将其返回
d1.clear()

