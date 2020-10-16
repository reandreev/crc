import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from graph import get_graph
from clustering_coefficient import uniform_wedge


TRIANGLE_COUNT = 3056386
SAMPLE_SIZES = [500, 1000]
SAMPLE_PERCENTS = [0.001, 0.005]
ITERATIONS = 15
COLORS = ["blue", "red", "green", "orange"]

G = get_graph("com-youtube.ungraph.txt")

results = {}

# for sample_size in SAMPLE_SIZES:
#     print(f"Sample size:{sample_size}")
#     aux = []

#     for i in range(ITERATIONS):
#         print(i)
#         aux.append(uniform_wedge(G, sample_size))

#     results[sample_size] = aux

for percent in SAMPLE_PERCENTS:
    print(f"Sample size:{percent}")
    aux = []

    for i in range(ITERATIONS):
        print(i)
        aux.append(uniform_wedge(G, None, sample_percent=percent))

    results[percent] = aux

print("Graphs")

meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='firebrick')
meanlineprops = dict(linestyle='--', linewidth=2.5, color='purple')

plt.boxplot(results.values(), showmeans=True, meanline=True, meanprops=meanlineprops)
plt.xticks(ticks=[*range(1, len(SAMPLE_PERCENTS)+1)], labels=[f"{i*100}%" for i in SAMPLE_PERCENTS])
plt.axhline(y=TRIANGLE_COUNT, linestyle='--', color='k')
plt.show()
