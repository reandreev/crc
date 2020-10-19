from BC import get_bc_info
from graph import get_graph

files=["facebook.txt", "twitch.csv"]

for file in files:
    file_tokens = file.split(".")
    file_name = file_tokens[0]
    file_type = file_tokens[1]

    g = get_graph("graphs/"+file, file_type)
    info_dict = get_bc_info(g)

    path = "results_BC/" + file_name + "_results.txt"
    with open(path, 'w') as f:
        f.write("GRAPH: " + file_name)
        f.write("Average BC:\t\t\t\t " + str(info_dict["avg_BC"])+"\n")
        f.write("Max BC values:\n")
        for i,pair in enumerate(info_dict["max_BCs"]):
            f.write("\t\t\t\t\t\t\t" + str(i+1)+". "+str(pair[1])+"\n")
        f.write("\n")
        f.write("Average of max Bc values:   " + str(info_dict["avg_max_BCs"])+"\n")

        f.write("time:   \t\t\t\t\t" + str(info_dict["time"])+"s\n\n")

