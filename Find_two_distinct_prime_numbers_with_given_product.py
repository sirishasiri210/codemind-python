def prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc=fc+1
    if fc==2:
        return True
    else:
        return False
        
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        if i!=n//i and prime(i)==True and prime(n//i)==True:
            print(i,n//i)
            break
else:
    print(-1)