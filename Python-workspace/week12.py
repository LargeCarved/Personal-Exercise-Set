# lesson = []
# score = []
# while True:
#     s = input()
#     if s:
#         x = s.split(":")
#         lesson.append(x[0])
#         score.append(x[1])
#     else:
#         break

# zipped = zip(lesson, score)
# dict1 = dict(zipped)
# s = input("请输入要查询的课程：\n")
# print(dict1.get(s, "没有该门课程"))

hotLesson = {}
while 1:
    x = input()
    if x:
        hotLesson[x] = hotLesson.get(x, 0)+1
    else:
        break
print(hotLesson.keys())
print(max(hotLesson, key=hotLesson.get))

# d = {}
# s = input()
# for i in s:
#     d[i] = d.get(i, 0)+1
# print(d)
# for i in d.items():
#     print(i)
# for i in d.items():
#     print('%s : %d' % i)
