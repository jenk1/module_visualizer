import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

def clean_filename(file):
    """Removes the filename extension"""

    return file.split('.')[0]

def clean_imports(lst):
    """Add the documentation later Comment"""

    mod_lst = []

    while(lst != []):
        if(',' in lst[0]):
            if(lst[0][0:6] == 'import'):
                temp_ = lst[0][6:].split(',')
                for i in temp_:
                    lst.append('import ' + i)

                lst[0] = 'Fixed'

            if(lst[0][0:4] == 'from'):
                temp_ = lst[0].split('import')
                part_1 = temp_[0]
                part_2 = temp_[1].lstrip().rstrip().split(',')
                for i in part_2:
                    lst.append(str(part_1) + ' import ' + str(i))

                lst[0] = 'Fixed'

        temp = lst[0].split()

        if(len(temp) == 2 and temp[0] == 'import'):
            mod_lst.append(temp[1])
            lst[0] = 'Fixed'

        elif(len(temp) == 4 and temp[0] == 'import' and temp[2] == 'as'):
            mod_lst.append(temp[1])
            lst[0] = 'Fixed'

        elif(len(temp) == 4 and temp[0] == 'from'):
            if(temp[3] != '*'):
                mod_lst.append(str(temp[1]) + '.' + str(temp[3]))
            else:
                mod_lst.append(str(temp[1]))
            lst[0] = 'Fixed'

        del lst[0]

    return mod_lst

def create_color_key_dic(file, node_list, graph):
    """Assigns nodes to a color depending on their location and builds graph
    
    This method assigns all the nodes to one of three colors.
    The "root" node is the value for the green key. The nodes that 
    are intermediate between the "root" and the leaf (actual imports)
    are yellow and the imports are the red ones
    """    
    
    color_dic = {'green': [clean_filename(file)], 'yellow': [], 'red': []}
    
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

    color_dic = {clean_filename(file): 'green'}

    # Needs some work
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

def color_key_dic(dictionary):
    """Summary

    Takes in a dictioary with colors as keys
    and a list of nodes that are under the
    color as a value and returns a new dictionary
    where the keys are the nodes and the colors
    are the values"""
    new_dict = {}

    for colors in dictionary.keys():
        # first need to get list of nodes
        lst = dictionary[colors]
        # iterate over nodes and add to dictioary
        for node in lst:
            new_dict[node] = colors

    return new_dict

def color_val_dic(dictionary):
    """
    Switches the values of the dictioary which
    are colors and returns it where the keys
    are the colors and the values are lists of
    the nodes
    """
    new_dict = {}

    # makes an empty list for each color
    for color in dictionary.values():
        new_dict[color] = []

    # adds the node to the corresponding
    # color
    for node in dictionary.keys():
        new_dict[dictionary[node]].append(node)

    return new_dict

def draw_graph_colored(graph, color_dic):
    """Draws a graph with colored node_list

    Inputs:
    graph is the networkx graph
    color_list is the dictioary where you know which colors go with each node
    """

    node_list = list(graph.nodes())
    color_list = []

    # check to see which format the color_dic is
    color_dic = color_key_dic(color_dic)
    for i in node_list:
        if(color_dic[i] == 'green'):
            color_list.append('g')
        elif(color_dic[i] == 'yellow'):
            color_list.append('y')
        elif(color_dic[i] == 'red'):
            color_list.append('r')

    # used by the draw_networkx method
    nx.draw_networkx(graph, with_labels=True, nodelist=node_list, node_color=color_list)
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
    all_imports = [line for line in content if line[0:6] == 'import' or line[0:4] == 'from']

    list_of_nodes = clean_imports(all_imports)
    
    return list_of_nodes

def find_subgraph(node, graph, draw_graph=True, save_graph=False):
    
    # Later exception handle this too for node not in Graph
    if(node not in graph.nodes()):
        print("The node you are looking for is not in the graph. Try another one.")
    
    stack = [node]
    # list that stores the nodes
    result = []

    # possibly make this a method later if reused
    while(stack):
        for i in graph.edges():
            if(stack[-1] == i[0]):
                result.append(i)
                stack.append(i[1])

    # see if we can make a temporary color dic
    
    
    # build the graph
    if(draw_graph):
        pass


# Add a method to go back to the full tree

# Add a method to make dispaly the tree