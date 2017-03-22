import os
from shutil import copy, copytree, rmtree
import stat

from .updater import Updater


class Setter(object):

    def __init__(self):
        self.updater = Updater()
        self.save_dir = None
        self.error_ext = []

    @staticmethod
    def del_read_only(action, name, exc):
        os.chmod(name, stat.S_IWRITE)
        os.remove(name)

    def create_save_dir(self):
        try:
            os.mkdir(self.save_dir)
        except FileExistsError:
            pass

    def set_files(self, files):
        for file in files:
            print(self.updater.working.format(file))
            try:
                copy(src=file, dst=self.save_dir)
            except FileNotFoundError:
                print(self.updater.file_not_found_error)
                continue

            print(self.updater.success.format(files, self.save_dir))

    def set_folders(self, folders):
        for folder in folders:
            print(self.updater.working.format(folder))
            name = folder.split("\\")[-1]
            path = "{}\\{}".format(self.save_dir, name)

            try:
                rmtree(path, onerror=self.del_read_only)
            except FileNotFoundError:
                copytree(src=folder, dst=path)
            else:
                copytree(src=folder, dst=path)

            print(self.updater.success.format(folder, self.save_dir))

    def set_settings(self, settings):
        for setting in settings:
            if setting[0] == "save_dir":
                self.save_dir = setting[1]

    def run(self, data):
        print(self.updater.header)

        files, folders, settings = data

        if settings:
            self.set_settings(settings)
            self.create_save_dir()
        if files:
            self.set_files(files)
        if folders:
            self.set_folders(folders)

        print(self.updater.end)
