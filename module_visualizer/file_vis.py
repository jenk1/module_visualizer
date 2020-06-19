import helper
import matplotlib.pyplot as plt
import networkx as nx
from os import path

def draw_graph_colored(graph, color_dic):
    """Draws a graph with colored node_list

    Add longer summary here

    Args fix the stuff here as well:
    graph is the networkx graph
    color_list is the dictioary where you know which colors go with each node
    """

    node_list = list(graph.nodes())
    color_list = []

    color_dic = color_key_dic(color_dic)

    for i in node_list:
        if(color_dic[i] == 'green'):
            color_list.append('g')
        elif(color_dic[i] == 'yellow'):
            color_list.append('y')
        elif(color_dic[i] == 'red'):
            color_list.append('r')

    nx.draw_networkx(graph, with_labels=True, nodelist=node_list,
                     node_color=color_list)
    plt.show()


def color_key_dic(dictionary):
    """Switches dict keys and values

    Takes in a dictioary with colors as keys
    and a list of nodes that are under the
    color as a value and returns a new dictionary
    where the keys are the nodes and the colors
    are the values

    Args:
        dictionary (dict): dictionary with colors as keys and nodes as values
    Returns:
        new_dict (dict): new dictionary with keys and values switched
    """
    new_dict = {}

    for colors in dictionary.keys():
        lst = dictionary[colors]

        for node in lst:
            new_dict[node] = colors

    return new_dict


def color_val_dic(dictionary):
    """Switches dict keys and values

    Switches the values of the dictioary which
    are colors and returns it where the keys
    are the colors and the values are lists of
    the nodes

    Args:
        dictionary (dict): dictionary with nodes as values and colors as keys
    Returns:
        new_dict (dict): new dictionary with keys and values switched
    """
    new_dict = {}

    # makes an empty list for each color
    for color in dictionary.values():
        new_dict[color] = []

    # adds the node to the corresponding color
    for node in dictionary.keys():
        new_dict[dictionary[node]].append(node)

    return new_dict


def create_color_key_dic(file, node_list, graph):
    """Assigns nodes to a color depending on their location and builds graph

    This method assigns all the nodes to one of three colors.
    The "root" node is the value for the green key. The nodes that
    are intermediate between the "root" and the leaf (actual imports)
    are yellow and the imports are the red ones

    Args:
        file (str): name of python file
        node_list (str): list of nodes reporesenting imported modules
        graph: networkx graph
    Returns:
        color_dic (dict): Dictionary of colors and respective nodes
    """

    color_dic = {'green': [helper.clean_filename(file)], 'yellow': [], 'red': []}

    for i in node_list:
        if('.' in i):
            temp = i.split('.')
            graph.add_edge(file[:-3], temp[0])
            color_dic['red'].append(temp[-1])
            for j in range(0, len(temp)-1):
                graph.add_edge(temp[j], temp[j+1])
                color_dic['yellow'].append(temp[j])
        else:
            graph.add_edge(file[:-3], i)
            color_dic['red'].append(i)

    return color_dic


def create_color_val_dic(file, node_list, graph):
    """Assigns colors to each node depending on their location

    This method assigns all the nodes to one of three colors.
    The "root" node is the key for the green color value. The color
    yellow is assigned to the nodes that are intermediate between the
    "root" and the leaf (actual imports) have the red color assined to them

    Args:
        file (str): name of python file
        node_list (str): list of nodes reporesenting imported modules
        graph: networkx graph
    Returns:
        color_dic (dict): Dictionary of nodes with their respective colors
    """

    color_dic = {helper.clean_filename(file): 'green'}

    for i in node_list:
        if('.' in i):
            temp = i.split('.')
            graph.add_edge(file[:-3], temp[0])
            color_dic[temp[-1]] = 'red'
            for j in range(0, len(temp)-1):
                graph.add_edge(temp[j], temp[j+1])
                color_dic[temp[j]] = 'yellow'
        else:
            graph.add_edge(file[:-3], i)
            color_dic[i] = 'red'

    return color_dic
