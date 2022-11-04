import random
number = [1, 2, 3, 4, 5, 6, 7]
del number[-1]
print(number)

number = [1, 2, 3, 4, 5, 6, 7]
number.pop()
print(number)

x = [1, 3, 5]
print(x[-1::-1])

y = (3, "wc", "w", [1, 2, 3, 4, 4], ("w", 3, 4), 23, 4)
y[3].append(6)
print(y)

fruit = ('苹果', '香蕉', '橘子', '枣')
food = ('瓜子', '奥利奥', '辣条', '薯片')
# fruit_sum = tuple((i, j)for i in fruit for j in fruit if i != j)
# food_sum = tuple((i, j)for i in food for j in food if i != j)
# liwu = tuple((i, j)for i in fruit for j in food)
a = tuple((i, j, k, l)
          for i in fruit
          for j in fruit
          for k in food
          for l in food
          if i != j and k != l)
print(random.choice(a))

# 剪刀石头布游戏
guess_list = ['剪刀', '石头', '布']
win_list = [('布', '石头'), ('石头', '剪刀'), ('剪刀', '布')]
print('欢迎加入石头剪刀布游戏，开始游戏吧！\n')
while True:
    computer = random.choice(guess_list)
    people = input('请输入：石头、剪刀或布\n').strip()
    if people == computer:
        print('平局，再来！')
    elif (computer, people) in win_list:
        print('电脑获胜，再玩，人类获胜才可以退出游戏')
    else:
        print('电脑出：', computer)
        print('你出：', people)
        print('你获胜啦!')
        break
