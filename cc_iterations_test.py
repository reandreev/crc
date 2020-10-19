import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.lines import Line2D
from graph import get_graph
from clustering_coefficient import uniform_wedge

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

TRIANGLE_COUNT = 3056386
SAMPLE_SIZE = 0.01
ITERATIONS = [5, 10, 20, 50, 100]

G = get_graph("com-youtube.ungraph.txt")

results = []

for iteration in ITERATIONS:
    print(f"Iteration:{iteration}")
    aux = []

    for i in range(iteration):
        print(i)
        aux.append(uniform_wedge(G, None, sample_percent=SAMPLE_SIZE))

    results.append(aux)

print("Txt")

for i, result in enumerate(results):
    with open(f"results_{ITERATIONS[i]}.txt", "w", encoding="utf-8") as f:
        for v in result:
            f.write(f"{v}\n")

print("Graph")

meanpointprops = dict(
    marker='D',
    markeredgecolor='black',
    markerfacecolor='firebrick'
)

medianprops = dict(linestyle='-', linewidth=1.5, color='orange')

custom_labels = [
    Line2D([0], [0], color='k', linestyle='--', lw=1.5, label="Real value"),
    Line2D([0], [0], color='orange', linestyle='-', lw=1.5, label="Median"),
    Line2D([0], [0], marker='D', markeredgecolor='black',
           markerfacecolor='firebrick', lw=0, label="Mean"),
]

plt.boxplot(results, showmeans=True, meanprops=meanpointprops, medianprops=medianprops)
plt.xticks(
    ticks=[*range(1, len(ITERATIONS)+1)],
    labels=ITERATIONS
)
plt.axhline(y=TRIANGLE_COUNT, linestyle='--', color='k')
plt.legend(handles=custom_labels)
plt.xlabel("Iterations")
plt.ylabel("Triangle count")
plt.savefig("results_iterations.pgf")
# plt.show()
