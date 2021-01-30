from os import walk
import matplotlib.pyplot as plt
import networkx as nx

import default_mods.built_in_modules as bim
import third_party_mods.popular_third_party_libraries as tpm


class GraphVisualizer:
    """Summary of class here

    Longer class information

    Attributes:
        path (str): path where 
        name_path_dict (dict): path to
        name_nodes_dict (dict): path to
        g (networkx graph): graph containing module dependencies
    """

    def __init__(self, path):
        """Inits GraphVisualizer class with path"""
        self.path = path
        # Set up dict with file as key and path as value
        self.name_path_dict = dict()
        # Set up dict with file as key and imports as values
        self.name_nodes_dict = dict()
        self.g = nx.DiGraph()

    def get_path(self):
        """Returns path of python project"""
        return self.path

    def get_graph_nodes(self):
        """Returns nodes in graph"""
        return self.g.nodes()

    def get_graph_edges(self):
        """Returns edges in graph"""
        return self.g.edges()

    def gather_files(self):
        """Finds and saves all py files in the path

        This method loops over all the files in the given path in order to
        find all the files ending in .py, and stores those files along with
        their path in the name_path_dict.
        """

        # get all the files from the folder
        for (dirpath, dirnames, filenames) in walk(self.path):
            for file in filenames:
                if file.lstrip().rstrip()[-3:] == '.py' and file != '__init__.py':
                    self.name_path_dict[file] = dirpath

    def gather_nodes(self, filename):
        """Gathers all imports that will be nodes for the graph

        Takes a file as input and from there processes the file so that the
        output is a list of all the possible nodes as well as their paths. An
        example of this would be having numpy and linspace as the two nodes in
        the graph and it would be displayed in the list as numpy.linspace

        Args:
            filename (str): The filename

        Returns:
            A list of strings that contains all the nodes that will eventually
            end up in the network graph
        """

        # process the file
        with open(filename) as f:
            content = f.readlines()

        # remove any extra whitespace from the end
        content = [i.rstrip() for i in content]

        # gather just the import lines
        all_imports = [line for line in content if line[0:6] == 'import' or
                       line[0:4] == 'from']

        list_of_nodes = self.clean_imports(all_imports)

        return list_of_nodes

    def clean_imports(self, import_list):
        """Puts all imports in a standard format

        If import is "import a, b, c" then method will put a, b, and c in
        separate entries. If import is "from a import b" then method will
        put a.b into the list. This is also true for "from _ as _". Also
        removes "as _" at the end of imports so there is no ambiguity.

        Args:
            import_list (str): A list of strings from python file 

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

    def gather_all_nodes(self):
        """T"""
        # right now assuming the dict is not empty
        for key in self.name_path_dict.keys():
            self.name_nodes_dict[key] = self.gather_nodes(
                self.name_path_dict[key] + '/' + key)

    def fill_graph(self):
        """Takes a list of nodes and adds them to the network graph"""

        for file in self.name_nodes_dict.keys():
            # edge case of no dependencies and not connected to another node
            if self.name_nodes_dict[file] == list() and file[:-3] not in list(self.g):
                self.g.add_node(file[:-3])
                continue

            for node in self.name_nodes_dict[file]:
                if '.' in node:
                    temp = node.split('.')
                    self.g.add_edge(file[:-3], temp[0])
                    for j in range(0, len(temp)-1):
                        self.g.add_edge(temp[j], temp[j+1])
                else:
                    self.g.add_edge(file[:-3], node)

    def draw_graph_default(self):
        nx.draw_networkx(self.g, with_labels=True)
        plt.show()

    def draw_graph_colored(self):

        file_list = [i[:-3] for i in self.name_path_dict.keys()]

        # dictionary with colors for each library
        # blue is b
        # green is g
        # red is r
        # yellow is y
        color_dict = {}

        for i in self.g.edges():
            if i[0] not in color_dict.keys():
                if i[0] in bim:
                    color_dict[i[0]] = 'g'
                elif i[0] in tpl:
                    color_dict[i[0]] = 'y'
                elif i[0] in file_list:
                    color_dict[i[0]] = 'b'

            if i[1] not in color_dict.keys():
                if i[1] in file_list:
                    color_dict[i[1]] = 'b'
                elif i[1] in bim:
                    color_dict[i[1]] = 'g'
                elif i[1] in tpl:
                    color_dict[i[1]] = 'y'
                else:
                    color_dict[i[1]] = color_dict[i[0]]

        # make the node and color list
        node_list = []
        color_list = []
        for val in color_dict.keys():
            node_list.append(val)
            color_list.append(color_dict[val])

        nx.draw_networkx(self.g, with_labels=True, nodelist=node_list,
                         node_color=color_list)
        plt.show()
