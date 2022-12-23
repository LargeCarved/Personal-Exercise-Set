
print("ab" in "acgcd")

ls = [1,2,3]
ls.insert(1,"a")
print(ls)

wt = ["abcd"]
print(wt[0:2])

for s in "PYTHON":
    if s == "T":
        break
print(s)

print("%s-%d" %("python",3))

print(10%3)

a=(1,2,3)
print(len(a))

tt="python"
print(tt[::2])

lt = [1,2,3]
lt[:2]=["x"]
print(lt)

S = {1,2,"python"}
S.add("python")
print(S)

N = list(range(1,6))
print(N)

def F(a,b):
    a=6
    return a+b
print(F(8,4))

a = ['a','b','c','d']
a[1:2]=[10,20]
print(a)

n = 5
s = 1
for i in range(1,n):
    s *= i
    print(s)
