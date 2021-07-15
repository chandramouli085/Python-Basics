import numpy as np
import matplotlib.pyplot as plt
import sys

file1 = open(sys.argv[1],"r")
li=file1.readlines()
#print(li)

x=[]
y=[]
for i in li:
    i=i[:-1]
    a=i.split(",")
    x.append(float(a[0]))
    y.append(float(a[1]))
    
x=np.array(x)
y=np.array(y)

plt.scatter(x, y)
plt.xticks(np.arange(-15, 16))
plt.yticks(np.arange(-15, 16))
plt.savefig("out.png")

