n=int(input())
a=0
b=1
d=[0,1]
for i in range(n-2):
  c=a+b
  a,b=b,c
  d.append(c)
print(*d,end='')

