from math import sqrt
def prime(x):
    c=0
    if x<2:
        return False
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            return 0
    return True
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i)==0:
            c+=1
print(c)