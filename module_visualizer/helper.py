import networkx as nx
import matplotlib.pyplot as plt

def clean_filename(file):
    """Removes the filename extension"""

    return file.split('.')[0]


def clean_filepath(path):
    """Removes the path and returns python file"""

    return path.split("/")[-1]


def clean_imports(import_list):
    """Puts all imports in standard format
    
    If import is import a, b, c puts a, b, and c in separate entries
    If import is from a import b puts a.b in list
    True for from _ as _ too. 
    Also removes as _ so that there is no ambiguity
    """

    mod_lst = []

    while(import_list != []):
        if(',' in import_list[0]):
            if(import_list[0][0:6] == 'import'):
                temp_ = import_list[0][6:].split(',')
                for i in temp_:
                    import_list.append('import ' + i)

                import_list[0] = 'Fixed'

            if(import_list[0][0:4] == 'from'):
                temp_ = import_list[0].split('import')
                part_1 = temp_[0]
                part_2 = temp_[1].lstrip().rstrip().split(',')
                for i in part_2:
                    import_list.append(str(part_1) + ' import ' + str(i))

                import_list[0] = 'Fixed'

        temp = import_list[0].split()

        if(len(temp) == 2 and temp[0] == 'import'):
            mod_lst.append(temp[1])
            import_list[0] = 'Fixed'

        elif(len(temp) == 4 and temp[0] == 'import' and temp[2] == 'as'):
            mod_lst.append(temp[1])
            import_list[0] = 'Fixed'

        elif(len(temp) == 4 and temp[0] == 'from'):
            if(temp[3] != '*'):
                mod_lst.append(str(temp[1]) + '.' + str(temp[3]))
            else:
                mod_lst.append(str(temp[1]))
            import_list[0] = 'Fixed'

        del import_list[0]

    return mod_lst


def draw_graph_default(graph):
    """Draw the default networkx graph"""

    nx.draw_networkx(graph, with_labels=True)
    plt.show()


def gather_nodes(filename):
    """Gathers all imports that will be nodes for graph

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

    # make sure to change the hleper
    list_of_nodes = helper.clean_imports(all_imports)

    return list_of_nodes

def find_subgraph(node, graph, draw_graph=True, save_graph=False):
    """ Shows the subgraph of a larger graph given a node

    """
    try:
        stack = [node]

        # the list that stores the nodes
        result = []

        while(stack):
            for i in graph.edges():
                if(stack[0] == i[0]):
                    result.append(i)
                    stack.append(i[1])
            stack.pop(0)

        # build the new graph
        N = nx.Graph()
        N.add_edges_from(result)

        # draw the graph
        if(draw_graph):
            nx.draw_networkx(N)
            plt.show()
        
        if(save_graph):
            return N

    except:
        print("The node you are looking for is not in the graph. Try again")
