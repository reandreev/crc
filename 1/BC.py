import networkx as nx
import operator
import time


def get_bc_info(g, k_top= 5):
    start_time = time.time()
    BC_dict = nx.betweenness_centrality(g)
    total_time = round(time.time() - start_time, 2)

    # list of pairs (node, bc_value)
    max_BCs = list(sorted(BC_dict.items(), key=operator.itemgetter(1), reverse=True)[:k_top])

    total_BC = 0
    for bc in BC_dict.values():
        total_BC += bc
    avg_BC = total_BC / len(BC_dict)

    max_total = 0
    for bc in max_BCs:
        max_total += bc[1]
    avg_max_BCs = max_total / len(max_BCs)

    return {"BC_dict": BC_dict,
            "avg_BC": avg_BC,
            "max_BCs": max_BCs,
            "avg_max_BCs": avg_max_BCs,
            "time": total_time}



'''
dict = {"a":1, "b":2, "c":3, "d":4}
max = list(sorted(dict.items(), key=operator.itemgetter(1), reverse=True)[:2])
for v in max:
    print(v[1])
'''