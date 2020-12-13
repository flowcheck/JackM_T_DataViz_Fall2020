import matplotlib.pyplot as plt
import numpy as np

hfont = { 'fontname' : 'arial' }

x = np.array(["Korea", "Japan"])
y = np.array([87, 63])

plt.ylabel("Medals")

plt.xlabel("Countries")

plt.title("Korea vs. Japan Medal Count", pad="20", **hfont)

plt.bar(x,y)
plt.show()
