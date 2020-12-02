from os import walk

# C:\Users\Michael\Desktop\desktop0\Code_Project\module_visualizer\module_visualizer


class GraphVisualizer:

    def __init__(self, path):
        self.path = path
        # Set up dict with file as key and path as value
        self.name_path_dict = dict()

        print("We set up the class")

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    # Add a add, remove, and view methods for name_path_dict

    def gather_files(self):
        """TODO fix the documentation here

        Args:
            path (str): path to desired folder

        Returns:
            Dictionary with python file as key and the path to it as the value
        """

        # TODO add try except later and check to make sure path exists

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
        print(all_imports)
        print()

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
        pass


def main():
    path_ = input("Please enter a path that you want to investigate: ")

    a = GraphVisualizer(path_)
    a.gather_files()
    print(a.name_path_dict)
    print()
    print(a.name_path_dict.keys())
    print()
    print()
    print(a.gather_nodes(a.name_path_dict['helper.py'] + '//' + 'helper.py'))
    print()


if __name__ == '__main__':
    main()
