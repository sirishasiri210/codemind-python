x=int(input())
k=1
for i in range(x):
    z=int(input())
    for j in range(1,z+1):
        k=k*j
    print(k)
    k=1