from math import sqrt
def prime(x):
    c=0
    if x<2:
        return False
    for j in range(2,int(sqrt(x))+1):
        if x%j==0:
            return False
    return True
n=int(input())
m=int(input())
v=n+m
s=n+m
while True:
    s=s+1
    if prime(s):
        v=s-v
        print(v)
        break