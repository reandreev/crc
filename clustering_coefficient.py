import random


def uniform_wedge(graph, sample_size):
    total_wedges = 0
    acc_wedge_count = {}

    for node in graph.nodes:
        total_wedges += graph.degree(node) * (graph.degree(node) - 1) / 2
        acc_wedge_count[node] = total_wedges

    sum = 0
    for _ in range(sample_size):
        r = random.randrange(total_wedges)
        index = search(r, acc_wedge_count)
        neighbors = list(graph[index])
        wedge = random.choices(neighbors, k=2)
        sum += 1 if graph.has_edge(wedge[0], wedge[1]) else 0

    return (total_wedges * sum) / (3 * sample_size)


def search(r, acc_wedge_count):
    for k, v in acc_wedge_count.items():
        if r <= v:
            return k
