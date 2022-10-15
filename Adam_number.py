n=int(input())
s=n**2
x=0
d=0
while n>0:
    r=n%10
    x=x*10+r
    n=n//10
y=x**2
while y>0:
    r=y%10
    d=d*10+r
    y=y//10
print(d==s)    