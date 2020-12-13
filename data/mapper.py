import matplotlib.pyplot as plt

hfont = { 'fontname' : 'arial' }

years = [1992, 1994, 1998, 2002, 2006, 2010, 2014]

pops = [7, 10, 12, 7, 19, 18, 14]

plt.plot(years, pops, color=(0/255, 100/255, 100/255), linewidth=3.0)

plt.ylabel("Medals")

plt.xlabel("Year of Competition")

plt.title("Korean Medal Count", pad="20", **hfont)

plt.show()