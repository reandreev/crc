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
SAMPLE_SIZES = [0.001, 0.005, 0.01, 0.05, 0.1]
ITERATIONS = 20

G = get_graph("com-youtube.ungraph.txt")

results = []
times = {}

for sample_size in SAMPLE_SIZES:
    print(f"Sample size:{sample_size}")
    aux = []
    aux_t = []

    for i in range(ITERATIONS):
        print(i)
        start_time = time.process_time()
        aux.append(uniform_wedge(G, None, sample_percent=sample_size))
        aux_t.append(time.process_time() - start_time)

    results.append(aux)
    times[sample_size] = aux_t

print("Txt")

for k, v in times.items():
    with open(f"time_{k}.txt", "w", encoding="utf-8") as f:
        for time in v:
            f.write(f"{time}\n")

for i, result in enumerate(results):
    with open(f"results_{SAMPLE_SIZES[i]}.txt", "w", encoding="utf-8") as f:
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
    ticks=[*range(1, len(SAMPLE_SIZES)+1)],
    labels=[f"{i*100}%" for i in SAMPLE_SIZES]
)
plt.axhline(y=TRIANGLE_COUNT, linestyle='--', color='k')
plt.legend(handles=custom_labels)
plt.xlabel("Sample size")
plt.ylabel("Triangle count")
plt.savefig("results_sample_size.pgf")
# plt.show()
