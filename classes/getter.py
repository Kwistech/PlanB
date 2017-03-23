import json


class Getter(object):
    """Class for Getter object.

    All variables and methods that are used for retrieving data is stored
    in this class. Specific datum should not be stored here.
    """

    def __init__(self):
        """Initiate instance variables and get data from data directory."""
        # Paths to data files
        self.files_path = "./data/files.json"
        self.folders_path = "./data/folders.json"
        self.settings_path = "./data/settings.json"

        # Read JSON files and saves info in instance variables
        self.files = self.read_json(self.files_path)
        self.folders = self.read_json(self.folders_path)
        self.settings = self.read_json(self.settings_path)

    @staticmethod
    def read_json(filename):
        """Get data from .json filename.

        Args:
            filename (str): JSON file to be opened and read.

        Returns:
            dict: Data from filename.
        """
        with open(filename) as f:
            f = json.load(f)
        return f

    @staticmethod
    def unpack(files, folders, settings):
        """Unpack yield files. folders, and settings.

        Args:
            files (generator): Contains all file paths to backup.
            folders (generator): Contains all folder paths to backup.
            settings (generator): Contains all settings for backup.

        Returns:
            tuple: Unpacked files, folders, and settings.
        """
        data_files = [file for file in list(files)]
        data_folders = [folder for folder in list(folders)]
        data_settings = [setting for setting in list(settings)]
        return data_files, data_folders, data_settings

    def get_files(self):
        """Get all file paths from self.files['FilePaths'].

        Yields:
            str: File path for file.
        """
        for file in self.files["FilePaths"]:
            yield file

    def get_folders(self):
        """Get all folder paths from self.files['FolderPaths'].

        Yields:
            str: Folder path for folder.
        """
        for folder in self.folders["FolderPaths"]:
            yield folder

    def get_settings(self):
        """Get all settings from self.settings and set key, value.

        Yields:
            tuple: [0] = setting (key)
                   [1] = value for setting (value)
        """
        for key in self.settings:
            setting = self.settings[key]
            yield key, setting

    def run(self):
        """Run Getter and return all files, folders, and settings.

        Returns:
            tuple: Contains all files, folders, and settings.
        """
        files = self.get_files()
        folders = self.get_folders()
        settings = self.get_settings()
        data = self.unpack(files, folders, settings)
        return data
