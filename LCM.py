a,b=map(int,input().split())
i=2
big=max(a,b)
small=min(a,b)
a=big
while True:
 if big%small==0:
    print(big)
    break
 else:
   big=a*i
   i+=1