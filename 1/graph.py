import networkx as nx


def get_graph(file, file_type="txt"):
    if file_type == "txt":
        sep = None
    elif file_type == "csv":
        sep = ','

    G = nx.Graph()

    with open(file, "r", encoding="utf-8") as graph:
        lines = graph.readlines()

        for line in lines[4:]:
            edge = [int(i) for i in line.split(sep)]
            G.add_edge(edge[0], edge[1])

    return G
