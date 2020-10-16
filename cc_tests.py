import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from graph import get_graph
from clustering_coefficient import uniform_wedge


TRIANGLE_COUNT = 3056386
SAMPLE_SIZES = [500, 1000, 2000, 5000]
ITERATIONS = 15
COLORS = ["blue", "red", "green", "orange"]

G = get_graph("com-youtube.ungraph.txt")

results = []

for sample_size in SAMPLE_SIZES:
    print(f"Sample size:{sample_size}")
    aux = []

    for i in range(ITERATIONS):
        print(i)
        aux.append(uniform_wedge(G, sample_size))

    results.append(aux)

print("Graphs")
fig, axs = plt.subplots(2, 2, figsize=(9, 3))

for i in range(len(SAMPLE_SIZES)):
    axs[int(i/2), int(i%2)].plot(np.arange(ITERATIONS), results[i], '-o', color=f"tab:{COLORS[i]}")
    axs[int(i/2), int(i%2)].axhline(y=np.mean(results[i]), linestyle='--', color=f"tab:{COLORS[i]}")
    axs[int(i/2), int(i%2)].axhline(y=TRIANGLE_COUNT, linestyle='--', color='k')
    axs[int(i/2), int(i%2)].legend(["Iterations", "Mean", "Real"])
    axs[int(i/2), int(i%2)].set_title(f"Sample Size: {SAMPLE_SIZES[i]}" )
    axs[int(i/2), int(i%2)].set_xlabel("Iteration" )
    axs[int(i/2), int(i%2)].set_ylabel("Triangle count")

plt.show()
