from shutil import copy, copytree, rmtree


class Setter(object):

    def __init__(self):
        self.save_dir = None
        self.error_ext = []

    def set_files(self, files):
        for file in files:
            try:
                copy(src=file, dst=self.save_dir)
            except FileNotFoundError:
                print("File '{}' not found!".format(file))

    def set_folders(self, folders):
        for folder in folders:
            fp = folder.split("\\")[-1]
            path = "{}\\{}".format(self.save_dir, fp)

            try:
                rmtree(path)
            except FileNotFoundError:
                try:
                    copytree(src=folder, dst=path)
                except FileNotFoundError:
                    error_msg = "The system can't find the path '{}'."
                    option = "Make sure path to copy is available!"
                    print(error_msg.format(folder), option)
                    return
            except PermissionError:
                error_msg = "ERROR: Can't delete read-only files!"
                option = "Manually delete '{}' and try again."
                print(error_msg, option.format(self.save_dir))
                return
            else:
                copytree(src=folder, dst=path)

            print("Successfully copied {} to {}".format(folder, self.save_dir))

    def set_settings(self, settings):
        for setting in settings:
            if setting[0] == "save_dir":
                self.save_dir = setting[1]

    def run(self, data):
        print("Backing up data...\n")
        files, folders, settings = data
        if settings:
            self.set_settings(settings)
        if files:
            self.set_files(files)
        if folders:
            self.set_folders(folders)
