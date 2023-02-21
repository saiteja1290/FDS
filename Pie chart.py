import matplotlib.pyplot as plt

labels=['A','B','AB','O']
rf=[0.3125,0.25,0.25,0.1875]
plt.pie(rf, labels=labels)
plt.legend()
plt.show()
