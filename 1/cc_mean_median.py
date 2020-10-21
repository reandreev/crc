import numpy as np

sample_sizes = [0.001, 0.005, 0.01, 0.05, 0.1]
iterations = [5, 10, 20, 50, 100]
tc = 3056386

print("Execution times")
for sample_size in sample_sizes:
    with open(f"results/time_{sample_size}.txt", "r", encoding="utf-8") as f:
        values = [float(i) for i in f.readlines()]
        print(f"{sample_size}\t{np.mean(values)}")

print("Results")
for sample_size in sample_sizes:
    with open(f"results/results_{sample_size}.txt", "r", encoding="utf-8") as f:
        values = [float(i) for i in f.readlines()]
        print(f"{sample_size}\t{np.mean(values)}\t{np.median(values)}\t{100*abs(1- (np.mean(values)/tc))}")

for iteration in iterations:
    with open(f"results/results_{iteration}.txt", "r", encoding="utf-8") as f:
        values = [float(i) for i in f.readlines()]
        print(f"{iteration}\t{np.mean(values)}\t{np.median(values)}\t{100*abs(1- (np.mean(values)/tc))}")

