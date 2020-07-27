from helper import gather_nodes
import networkx as nx
import matplotlib.pyplot as plt
from os import walk
from pylab import rcParams

# Set the size of the plot
rcParams['figure.figsize'] = 26, 18


def fill_graph(node_list, file, graph):
    """Takes a list of nodes and adds them to the network graph

    Args:
        node_list: list of nodes
        file: name of python file
        graph: networkx graph

    Returns:
        Network graph
    """

    for i in node_list:
        if '.' in i:
            temp = i.split('.')
            graph.add_edge(file[:-3], temp[0])
            for j in range(0, len(temp)-1):
                graph.add_edge(temp[j], temp[j+1])
        else:
            graph.add_edge(file[:-3], i)


def get_files(path):
    """Gathers all python files from a folder

    Args:
        path (str): path to desired folder

    Returns:
        Dictionary with python file as key and the path to it as the value
    """

    # Set up dict with file as key and path as value
    name_path_dict = {}

    # get all the files from the folder
    for (dirpath, dirnames, filenames) in walk(mypath):
        for file in filenames:
            name_path_dict[file] = dirpath

    return name_path_dict


def make_graph(path):
    """Make the network graph
    
    Args:
        path (str): path to desired folder

    Returns:
        Network graph
    """

    # make the graph
    g = nx.DiGraph()

    name_path_dict = get_files(path)

    # now check to see if files in dictionary keys are .py files
    for file in name_path_dict.keys():
        if file.lstrip().rstrip()[-3:] == '.py' and file != '__init__.py':
            node_list = gather_nodes(name_path_dict[file] + '\\' + file)
            fill_graph(node_list, file, g)

    return g
