"""

Description: Creates Data for Charts and Graph Functionality

"""

import flot

class MySeries(flot.Series):
    data = [(1,2),(2,5),(3,7),(4,9),]

class MyGraph(flot.Graph):
    my_series = MySeries()


my_graph = MyGraph()
print my_graph.json_data
print my_graph.options
