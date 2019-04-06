#合并或扩展字符串
s1 = 'I love'
s2 = 'Python'
str1 = ' '.join([s1,s2])
str2 = s1 + s2
str3 = s2*3
msg = """
str1:%s
str2:%s
str3:%s
"""%(str1,str2,str3)
print(msg)

#查找
print(str1.find('o'))
print(str1.lfind('o'))
print(str1.rfind('o'))
print(str1.count('o'))

#替换或拆分字符串
print(str1.replace('Python','PYTHON'))
list1 = str1.split()
list2 = str1.partition('love')  #指定字符为分隔符

#删除
s3 = ' I love Python '
s3 = s3.strip() #删除两端的空格符、换行符
print(s3)
print(s3.strip('I')) #删除指定字符，‘I’必须在首位否则删除失败

#大小写转换
print(str1.upper())
print(str1.lower())
print(str1.title()) #每个单词首字母大写
print(str1.capitalize()) #字符串首字母的首字符大写
print(str1.swapcase()) #大小写互换

#类型判断
print(str1.isalnum()) #是否为数字或字母组合
print(str1.isalpha()) #是否为纯字母组合
print(str1.isdigit()) #是否为纯数字组合
print(str1.isupper()) #是否大写
print(str1.islower()) #是否小写
print(str1.isspace()) #是否空白符

#内置函数eval()
print(eval('3+4'))

#练习
a = 'aAs7efag9yu6FJg7hgYYU1'
#将字符串a的数字提出组成新的字符串
print(''.join([i for i in a if i.isdigit()]))

#删除字符串中重复的字符同时不改变各个字符的位置
list1 = list(set(a))
list1 = sorted(list1,key=a.index)
print(''.join(list1))

#统计各个字符出现的次数,并输出出现频率最高的字符和次数
list2 = [(x,a.count(x)) for x in set(a)]
list2 = sorted(list2,key=lambda x:x[1],reverse=True)
print(list2[0])

#判断字符串'boy'是否出现在a里
print('boy' in a)

#判断字符串'boy'的每个字符是否都出现在a里
a_set = set(a)
b_set = set('boy')
print(a_set&b_set == b_set)
