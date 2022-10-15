n=int(input())
f=[]
for i in range(1,n):
    if n%i==0:
        f.append(i)
k=sum(f)
if k>n:
    print("True")
else:
    print("False")