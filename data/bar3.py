import matplotlib.pyplot as plt
import numpy as np

hfont = { 'fontname' : 'arial' }

x = np.array(["Skiing", "Skating"])
y = np.array([35, 28])

plt.ylabel("Medals")
colors = ['lightskyblue', 'red']

plt.title("Skiing vs. Skating Medal Count", pad="20", **hfont)

plt.bar(x,y)
plt.show()
