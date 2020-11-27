from os import walk


class GraphVisualizer:

    def __init__(self, path):
        self.path = path
        # Set up dict with file as key and path as value
        self.name_path_dict = {}
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


def main():
    path_ = input("Please enter a path that you want to investigate: ")

    a = GraphVisualizer(path_)
    print(a.gather_files())
    print()
    print(a.gather_files().keys())


if __name__ == '__main__':
    main()
