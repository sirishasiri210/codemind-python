n=int(input())
x=[]
for i in range(1,n):
  if n%i==0:
     x.append(i)
c=sum(x)
if c>n:
   print("True")
else:
   print("False")    