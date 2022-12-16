from graph import City, load_graph
from graph import connected

nodes, graph = load_graph("roadmap.dot", City.from_dict)

print(connected(graph, nodes["belfast"], nodes["glasgow"]))

print(connected(graph, nodes["belfast"], nodes["derry"]))