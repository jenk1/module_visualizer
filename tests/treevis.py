import module_visualizer.helper as helper
import matplotlib.pyplot as plt
import networkx as nx


def draw_graph_colored(graph, color_dic):
    """Draws a graph with colored node_list

    Add longer summary here

    Args fix the stuff here as well:
    graph is the networkx graph
    color_list is the dictioary where you know which colors go with each node
    """

    node_list = list(graph.nodes())
    color_list = []

    color_dic = helper.color_key_dic(color_dic)

    for i in node_list:
        if(color_dic[i] == 'green'):
            color_list.append('g')
        elif(color_dic[i] == 'yellow'):
            color_list.append('y')
        elif(color_dic[i] == 'red'):
            color_list.append('r')

    # used by the draw_networkx method
    nx.draw_networkx(graph, with_labels=True, nodelist=node_list,
                     node_color=color_list)
    plt.show()


def draw_graph_default(graph):
    """Draw the default networkx graph"""

    nx.draw_networkx(graph, with_labels=True)
    plt.show()


def gather_nodes(filename):
    """Summary

    Takes a file as input and from there
    processes the file so that the output is a list of
    all the possible nodes as well as their paths
    an example of this would be having numpy and linspace
    as the two nodes in the graph and it would be dispalyed in the
    list as numpy.linspace
    """

    # process the file
    with open(filename) as f:
        content = f.readlines()

    # remove any extra whitespace from both ends
    content = [i.lstrip().rstrip() for i in content]

    # gather just the import lines
    all_imports = [line for line in content if line[0:6] == 'import' or
                   line[0:4] == 'from']

    list_of_nodes = helper.clean_imports(all_imports)

    return list_of_nodes


def find_subgraph(node, graph, draw_graph=True, save_graph=False):
    """ Shows the subgraph of a larger graph given a node

    """

    # Later exception handle this too for node not in Graph
    if(node not in graph.nodes()):
        print("The node you are looking for is not in the graph. Try another")

    stack = [node]

    # the list that stores the noes
    result = []

    # possibly make this a method later if reused
    while(stack):
        for i in graph.edges():
            if(stack[0] == i[0]):
                result.append(i)
                stack.append(i[1])
        stack.pop(0)

    # build the new graph
    N = nx.Graph()
    N.add_edges_from(result)

    # create a color dictionary here
    # TODO: figure out how to split imports later
    color_dic = {'green': [node], 'biscuit': []}

    for i in N.nodes():
        if(i != node):
            color_dic['biscuit'].append(i)

    # draw the graph
    if(draw_graph):
        draw_graph_colored(N, color_dic)

    if(save_graph):
        return N

"""
if __name__ == "__main__":
    
    # do the stuff here you want to do
"""