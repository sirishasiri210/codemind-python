n=int(input())
s=n*n
c=0
k=0
while n!=0:
  r=n%10
  c=c*10+r
  n=n//10
j=c**2
while j!=0:
    r1=j%10
    k=k*10+r1
    j=j//10
if k==s:
    print("True")
else:
    print("False")