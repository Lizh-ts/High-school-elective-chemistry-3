import math
import numpy as np
import matplotlib.pyplot as plt
print("github/Lizh-ts")
print("(1)強vs強")
print("(2)強vs弱")
lev = int(input("選擇滴定等級(1 or 2):"))#1H-H,2H-L
print("(1)酸滴定鹼")
print("(2)鹼滴定酸")
sel = int(input("選擇滴定順序(1 or 2):"))#1a2b,2b2a
if lev==2:
    k = float(input("輸入被滴定物K(小於1):"))
a = float(input("輸入被滴定物濃度:"))
b = float(input("輸入滴定物濃度:"))
v=1000
for i in range(1,2001,1):
    dm=abs(i*a-v*b)
    if i*a-v*b>0:
        y=dm/(v+i)
    
    if lev==2:#H-L
        if i*a-v*b<0:
            y=(10**-14)/(dm*k)*(i*a)
        if i*a==v*b:
            y=((b*v)/(i+v)*(10**-14)/k)**0.5
    else:#H-H
        if i*a-v*b<0:
            y=(10**-14)/(dm/(v+i))
        elif i*a==v*b:
            y=(10**-7)
    if sel==2:
        ans=14+math.log10(y)
    if sel==1:
        ans=abs(math.log10(y))
    plt.plot(i, ans, 'ro--', linewidth=1, markersize=2)
    plt.xlabel('ml')
    plt.title('pH-ml')
plt.show()
