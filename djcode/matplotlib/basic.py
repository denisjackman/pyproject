'''
    a basic matplotlib
'''

import matplotlib.pyplot as plt
year = [1958, 1976, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.scatter(year, pop)
plt.xlabel("year")
plt.ylabel("population")
plt.title("world population projections")
plt.yticks([0, 2, 4, 6, 8, 10], ['0', '2B', '4B', '6B', '8B', '10B'])
plt.show()
