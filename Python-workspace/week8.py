

# 切片
a = [15, 34, 63, 86, 23, 57, 10, 54, 2, 76, 43, 4, 65, 38]

print(a[2:5:1])
'''print(a[-3:-9:-1])

print(a[0:7:1])
print(a[:7])
print(a[7: :1])
print(a[7:])
print(a[-1:-8:-1])
print(a[:-8:-1])

print(a[-11::-1])
print(a[-11:])
print(a[6::-2])
print(a[1::2])
print(a[-11:-16:-1])
print(a[1:100:2])'''
# 列表推导式---以原有列表为模板，构造新列表
'''a = [15,34,63,86,23,57,10,54,2,76,43,4,65,38]
#挑出a小于 30的,在减去100构成新列表
b = []
for i in a:
    if i < 30:
       b.append(i)
print(b)
e = [ i-100 for i in a if i < 30]
print(e)
f = [2,5,'ddsf',[3,4,3,2],3,[3,4,'r','f']]'''

# 64个格子放大米
'''sum = 0
for i in range(0,64):
   sum += 2**i
print(sum)'''

'''a = []
for i in range(0,64):
   a.append(2**i)
print(sum(a))'''

#print( sum([2**i for i in range(0,64)] ))
