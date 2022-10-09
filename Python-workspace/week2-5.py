print('123','321','213','132',sep='****')

name = 'keging'
number = 114514
sex = 'woman'
age = 17
print('你的名字',name,'一个数字',number,'性别',sex,'年龄',age,sep='++++')

import math
# a = eval(input())
# b = eval(input())
# c = eval(input())
# s = (a+b+c)/2
# print('area=%.2f;perimeter=%.2f'%(math.sqrt(s*(s-a)*(s-b)*(s-c)),(a+b+c)))

a = 7927149
b = 'apple pen papne apple'

print(a,b)
print(5.44444)
print("wow")

# name = input()
# favorite = input()
# print(name,"\n",favorite)

# 八，十，十六进制
# x = int(input('请输入一个整数:'))
# print('%o,%d,%x'%(x,x,x))

# x = float(input('请输入小数:'))
# print('%.2f'%x)

a = '海南'
b = '大海'
c = 365
print(f'{b}包围着{a}。在{a}{c}天都可以感受{b}')

# a,b,c=input().split()
# a,b,c=eval(a),eval(b),eval(c)
# if a+b>c and a+c>b and b+c>a:
#     print("yes")
# else:
#     print("no")
#
# a = int(input())
# if (a%4==0 and a%100!=0) or a%400==0:
#     print(f'{a}是闰年')
# else:
#     print(f'{a}不是闰年')

#格式化输出
max,min,ave,fail=0,100,0,0
print('Max: {}\nMin: {}\nAve: {:.1f}\nFail: {}' .format(max, min, ave, fail))

string = 'programming is More fun!'
s = 'm'
n = 0
for a in string:
    if a == s:
        n += 1
if n == 0:
    print('输入的字符不存在！')
else:
    print(n)

m = 6
for i in range(1,m+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()