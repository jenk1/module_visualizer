
class GraphVisualizer:

    def __init__(self, path):
        self.path = path

    def get_files(self):
        """Gathers all python files from a folder

        Args:
            path (str): path to desired folder

        Returns:
            Dictionary with python file as key and the path to it as the value
        """

        # do try except later but keep if for now
        if self.path is None:
            return "You big dummy"

        # Set up dict with file as key and path as value
        name_path_dict = {}

        # get all the files from the folder
        for (dirpath, dirnames, filenames) in walk(path):
            for file in filenames:
                name_path_dict[file] = dirpath

        return name_path_dict


def main():
    pass


if __name__ == '__main__':
    main()
