import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# this class is to plot a graph of average fitnesses per generation.
gen = 0
x = []
y = []
for line in open("fitness.txt", "r"):
    gen += 1
    y.append(float(line))
    x.append(gen)
plt.title("Fitness over Generations")
plt.xlabel('Generation')
plt.ylabel("Average Fitness")
plt.plot(x, y)

plt.show()