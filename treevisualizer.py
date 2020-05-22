# Load the libraries
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
from pylab import rcParams
import os
import util

rcParams['figure.figsize'] = 30, 20

file = input("Input the name of the file you want to investigate.")

# Get this all in a function

# print out the filename
print("The name of the file you chose was " + util.clean_filename(file))
print()

list_of_nodes = util.gather_nodes(file)
print(list_of_nodes)

"""

# let's make a dictionary to store the nodes
color_dic = {'green': [util.clean_filename(file)], 'yellow': [], 'red': []}

G = nx.Graph()

for i in list_of_nodes:
    if('.' in i):
        temp = i.split('.')
        # make the below a function later in
        # refactoring
        G.add_edge(file[:-3], temp[0])
        color_dic['red'].append(temp[-1])
        for j in range(0, len(temp)-1):
            G.add_edge(temp[j], temp[j+1])
            color_dic['yellow'].append(temp[j])

    else:
        G.add_edge(file[:-3], i)
        color_dic['red'].append(i)

print(color_dic)
print()
print(util.color_key_dic(color_dic))
# now we want to print the graph in this area
#util.draw_graph_default(G)
print()
print("First graph done")
util.draw_graph_colored(G, color_dic)

print()
print("We are done bitches!!")
print()
print("Yes we are done bitches!!")
print("That is how we do it.")
"""