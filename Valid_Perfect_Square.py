x=int(input())
import math
for i in range(x):
    a=int(input())
    k=int(math.sqrt(a))
    if k*k==a:
        print("True")
    else:
        print("False")