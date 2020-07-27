import networkx as nx
import matplotlib.pyplot as plt


def clean_filename(file):
    """Removes the filename extension

    Args:
        file (str): filename

    Returns:
        The filename (i.e. a python file would be returned without the .py)
    """

    return file.split('.')[0]


def clean_file_path(path):
    """Removes the path and returns the python file

    Args:
        path (str): file path

    Returns:
        The python file
    """

    return path.split("/")[-1]


def clean_imports(import_list):
    """Puts all imports in a standard format

    If import is "import a, b, c" then method will put a, b, and c in
    separate entries. If import is "from a import b" then method will
    put a.b into the list. This is also true for "from _ as _". Also
    removes "as _" at the end of imports so there is no ambiguity.

    Args:
        import_list: A list of strings from python file

    Returns:
        A list of strings that have the imports in standard format

    """

    mod_lst = []

    while import_list:
        if ',' in import_list[0]:
            if import_list[0][0:6] == 'import':
                temp_ = import_list[0][6:].split(',')
                for i in temp_:
                    import_list.append('import ' + i)

                import_list[0] = 'Fixed'

            if import_list[0][0:4] == 'from':
                temp_ = import_list[0].split('import')
                part_1 = temp_[0]
                part_2 = temp_[1].lstrip().rstrip().split(',')
                for i in part_2:
                    import_list.append(str(part_1) + ' import ' + str(i))

                import_list[0] = 'Fixed'

        temp = import_list[0].split()

        if len(temp) == 2 and temp[0] == 'import':
            mod_lst.append(temp[1])
            import_list[0] = 'Fixed'

        elif len(temp) == 4 and temp[0] == 'import' and temp[2] == 'as':
            mod_lst.append(temp[1])
            import_list[0] = 'Fixed'

        elif len(temp) == 4 and temp[0] == 'from':
            if temp[3] != '*':
                mod_lst.append(str(temp[1]) + '.' + str(temp[3]))
            else:
                mod_lst.append(str(temp[1]))
            import_list[0] = 'Fixed'

        del import_list[0]

    return mod_lst


def draw_graph_default(graph):
    """Draw the default networkx graph

    Args:
        graph: networkx graph
    """

    nx.draw_networkx(graph, with_labels=True)
    plt.show()


def gather_nodes(filename):
    """Gathers all imports that will be nodes for the graph

    Takes a file as input and from there processes the file so that the
    output is a list of all the possible nodes as well as their paths. An
    example of this would be having numpy and linspace as the two nodes in
    the graph and it would be displayed in the list as numpy.linspace

    Args:
        filename (str): The filename for the

    Returns:
        A list of strings that contains all the nodes for the network graph
    """

    # process the file
    with open(filename) as f:
        content = f.readlines()

    # remove any extra whitespace from both ends
    content = [i.lstrip().rstrip() for i in content]

    # gather just the import lines
    all_imports = [line for line in content if line[0:6] == 'import' or
                   line[0:4] == 'from']

    list_of_nodes = clean_imports(all_imports)

    return list_of_nodes


def find_subgraph(node, graph, draw_graph=True, save_graph=False):
    """ Shows the sub-graph for a larger graph given a node

    Args:
        node (str): node to search for sub-graph
        graph: full network graph
        draw_graph: if True then plot graph
        save_graph: if True then save network graph

    Returns:
        If save_graph is True then will the sub-graph
    """

    try:
        stack = [node]

        # the list that stores the nodes
        result = []

        while stack:
            for i in graph.edges():
                if stack[0] == i[0]:
                    result.append(i)
                    stack.append(i[1])
            stack.pop(0)

        # build the new graph
        n = nx.Graph()
        n.add_edges_from(result)

        # draw the graph
        if draw_graph:
            nx.draw_networkx(n)
            plt.show()
        
        if save_graph:
            return n

    except:
        print("The node you are looking for is not in the graph. Try again")
