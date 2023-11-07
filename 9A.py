import numpy as np
data1=[]
data2=[]
for i in range(0,2):
  a = int(input("Enter the first data value"))
  data1.append(a)
for j in range(0,2):
  b = int(input("Enter the second data values"))
  data2.append(b)
array = np.array([data1,data2])
print(array)
