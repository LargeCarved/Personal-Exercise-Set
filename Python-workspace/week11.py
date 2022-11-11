# str1 = input().split()
# str = ["the", "United", "States", "of", "America"]
# for i in str1:
#     if i[0]>= 'A' and i[0] <= 'Z':
#         print(i[0], end="")

# print(''.join([i[0] for i in str1 if i[0]>= 'A' and i[0] <= 'Z']))
# the United States of America

str2 = input()
num = len(str2)-3
print(str2[0]+num*str2[1]+str2[0])
print(str2[2]+str2[3:]+str2[2])
print(str2[0]+num*str2[1]+str2[0])

a=input()
b=input()
s=0
for c in a:
    if c in b:
        s=s+1
print(s)

t = input()
s = ""
for i in range(len(t)):
    if t[i] >= "A" and t[i] <= "Z":
        s += chr(155-ord(t[i]))
    else:
        s += t[i]
print(s)
