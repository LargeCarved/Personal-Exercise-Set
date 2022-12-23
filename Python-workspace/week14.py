# import json
import os
# ddd = {'name': 'LYZ', 'age': 20, 'hometown': '海南'}
# data = json.dumps(ddd, indent=3)
# print(data)

# print(os.getcwd())
# os.makedirs('D:/HB/21soft306.2/textssss/wavsdaca')
# os.chdir('D:/HB/21soft306.2/textssss')
# print(os.listdir('D:/HB/21soft306.2/textssss'))
# os.rmdir('D:/HB/21soft306.2/textssss/aaa')
# print(os.listdir('D:/HB/21soft306.2/textssss'))

# with open('D:/HB/21soft306.2/Python-workspace/ssss/test.txt', 'r') as file:
#     t = file.read().split(',')
# t = [int(i) for i in t]
# print(sum(t)/len(t))

# with open('D:/HB/21soft306.2/Python-workspace/ssss/english.txt', 'r') as file1, open('D:/HB/21soft306.2/Python-workspace/ssss/test.txt', 'a') as file2:
#     file2.write(file1.read().swapcase())

os.chdir('D:/HB/21soft306.2/Python-workspace/ssss')
list = [name for name in os.listdir()
        if name.endswith('.docx')]
for name in list:
    newname = name[:-5] + '_new.docx'
    os.rename(name, newname)
