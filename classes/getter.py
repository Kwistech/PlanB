import json


class Getter(object):

    def __init__(self):
        self.files_path = "./data/files.json"
        self.folders_path = "./data/folders.json"
        self.settings_path = "./data/settings.json"

        self.files = self.read_json(self.files_path)
        self.folders = self.read_json(self.folders_path)
        self.settings = self.read_json(self.settings_path)

    @staticmethod
    def read_json(filename):
        with open(filename) as f:
            f = json.load(f)
        return f

    @staticmethod
    def unpack(files, folders, settings):
        data_files = []
        data_folders = []
        data_settings = []

        for file in list(files):
            data_files.append(file)
        for folder in list(folders):
            data_folders.append(folder)
        for setting in list(settings):
            data_settings.append(setting)

        data = data_files, data_folders, data_settings
        return data

    def get_files(self):
        for file in self.files["FilePaths"]:
            yield file

    def get_folders(self):
        for folder in self.folders["FolderPaths"]:
            yield folder

    def get_settings(self):
        for key in self.settings:
            setting = self.settings[key]
            yield key, setting

    def run(self):
        files = self.get_files()
        folders = self.get_folders()
        settings = self.get_settings()
        data = self.unpack(files, folders, settings)
        return data
