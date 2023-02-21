import matplotlib.pyplot as plt

x=range(10)
y=[]
for i in x:
    y.append(2*i+1)
plt.scatter(x,y)
plt.show()
