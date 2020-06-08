import networkx as nx
import matplotlib.pyplot as plt


def clean_filename(file):
    """Removes the filename extension"""

    return file.split('.')[0]


def clean_filepath(path):
    """Removes the path and returns python file"""

    return path.split("/")[-1]


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
