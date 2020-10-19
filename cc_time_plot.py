import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

sample_sizes = [0.001, 0.005, 0.01, 0.05, 0.1]
x = [i*100 for i in sample_sizes]
times = []

for sample_size in sample_sizes:
    with open(f"time_{sample_size}.txt", "r", encoding="utf-8") as f:
        values = [float(i) for i in f.readlines()]
        times.append(np.mean(values))


plt.plot(x, times, '-o', color="tab:blue")
plt.xticks(ticks=x, labels=x)
plt.xlabel("Sample size (%)")
plt.ylabel("Execution time (s)")
plt.savefig("times_mean.pgf")
