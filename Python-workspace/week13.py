# import random
# def numbers(i:int,j:int)->list:
#     nums=[]
#     while i>0:
#         x = random.randint(0,j)
#         if x % 2 != 0 and x not in nums:
#             nums.append(x)
#             i -= 1
#     return nums
#
# print(numbers(5,100))

def istriangle(n1, n2, n3):
    '''判断三边是否可以构成三角形'''
    if n1+n2 > n3 and n1+n3 > n2 and n2+n3 > n1:
        return True
    else:
        return False


n = [int(i) for i in input().split()]
print(istriangle(*n))
