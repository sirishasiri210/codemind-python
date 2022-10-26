from math import sqrt
def fun(x):
    c=0
    if x<2:
        return 0
    for j in range(2,int(sqrt(x))+1):
        if x%j==0:
            return 0
    return 1
            
m=int(input())
n=int(input())
s=0
for i in range(m,n+1):
    if fun(i)==1:
        s+=1
print(s)
