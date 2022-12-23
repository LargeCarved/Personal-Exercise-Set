# b = 4
# try:
#     a = eval(input("输入一个数"))
#     print(a+b)
# except NameError:
#     print("需要输入的是数值")
# else:
#     print("加法计算中未出现问题")
# print("计算继续")

import datetime
time = datetime.date.today()
today = str(time).replace('-', '/')
athletes = []
age = []
try:
    with open('D:/HB/21soft306.2/Python-workspace/运动员生日信息.txt', encoding='utf-8') as f:
        athletes = f.readlines()
except FileNotFoundError:
    print("文件未找到")
# else:
#     print(athletes)
athletes = [i.replace('\n', '') for i in athletes]
for i in athletes:
    n = i.index(',')
    birth = i[n+1:]
    age.append(i[:n] + '-'+str(int(today[:4]) - int(birth[:4]))+'\n')

with open('D:/HB/21soft306.2/Python-workspace/运动员年龄信息.txt', 'w') as f:
    athletes = f.writelines(age)
