import matplotlib.pyplot as plt

labels=['A','B','AB','O']
rf=[0.3125,0.25,0.25,0.1875]
plt.bar(labels,rf)
plt.xlabel("Blood group")
plt.ylabel("Relative frequency")
plt.title("Blood group of paitents")
plt.show()
