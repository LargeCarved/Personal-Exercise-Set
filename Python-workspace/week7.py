for i in range(10, 0, -2):
    print(i, end=" ")
print()

for ch in "good":
    print(ch)
# 创建列表
a = []
b = [2, 4, 6, '435', 5.5555, 'fesfew34234']
#c = input().split()
#d = list(range(2,100,3))

# 列表的输出
# print(b)

# 列表元素的输出
d = list(range(2, 100, 3))
'''print(d[3])
print(d[-3])

for i in d:
    print(i,end=",")

for i in range(4,10):
    print(d[i])

for i in range(-2,-10,-1):
    print(d[i],end="-")'''

# 删除列表 del命令
#del b
# print(b)

# 删除列表元素1：del，pop(),remove()
del d[3]
d.pop()  # 栈 出栈
d.remove(44)  # 根据值
# print(d)

# 插入元素append(),insert(),extend(),"+","*"
d.append(100)
d.insert(-1, 200)
# d.extend(b)     #原地址修改
# print(d+b)   #创建了新列表
# print(b*3)  #创建了新列表

# 列表其他常用计算，统计，逆序，排序。。。。。
e = [2, 4, 5, 6, 7, 4, 2, 2, 3, 4, 1, 6, 4, 3, 3]
print(e.count(2))
print(e.index(4))   # 那个元素第一次出现的位置
print(sum(e))
e.reverse()  # 原地逆置
print(e)
# 两种排序
e.sort()  # 升序
print(e)
e.sort(reverse=True)
print(e)
f = e.sorted()  # 形成新列表
