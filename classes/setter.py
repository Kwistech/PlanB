import os
from shutil import copy, copytree, rmtree
import stat

from .updater import Updater


class Setter(object):
    """Class object for Setter.

    Setter holds all of the variables and methods for setting the data
    retrieved from the Getter class.

    This class is the class that copies all of the users files from one
    directory to another.
    """

    def __init__(self):
        """Initialize Updater object and save_dir variable."""
        self.updater = Updater()
        self.save_dir = None

    @staticmethod
    def del_read_only(action, name, exc):
        """Static method that removes 'read only' from name and deletes name.

        This method is called when shutil.rmtree (found in self.set_folders())
        raises an error.

        Note: Do not remove the action and exc parameters as they are used
        by rmtree!

        Args:
            action (builtin_function_or_method): Action to take from rmtree
            name (str): Name of file to be modified and deleted.
            exc (tuple): Executable(s) to run upon error.
        """
        os.chmod(name, stat.S_IWRITE)
        os.remove(name)

    def create_save_dir(self):
        """Create the save directory for backup.

        Raises:
            FileExistsError: If directory already exists.
        """
        try:
            os.mkdir(self.save_dir)
        except FileExistsError:
            pass

    def set_files(self, files):
        """Set files to save directory.

        self.updater variables are printed to update the user on the
        programs progress.

        Args:
            files (list): Files to be backed up.

        Raises:
            FileNotFoundError: If file can not be found.
        """
        for file in files:
            print(self.updater.working.format(file))

            try:
                copy(src=file, dst=self.save_dir)
            except FileNotFoundError:
                print(self.updater.file_not_found_error)
                continue

            print(self.updater.success.format(files, self.save_dir))

    def set_folders(self, folders):
        """Set folders to save directory.

        self.updater variables are printed to update the user on the
        programs progress.

        Note: rmtree will call self.del_read_only on error.

        Args:
            folders (list): Folders to be backed up.

        Raises:
            FileNotFoundError: If folder can not be found.
        """
        for folder in folders:
            print(self.updater.working.format(folder))

            # Get folder name and place it in save directory path
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
        """Set settings for backup.

        Note: settings MUST include a save directory (save_dir)
        key and value!

        Args:
            settings (list): All settings for backup.
        """
        for setting in settings:
            if setting[0] == "save_dir":
                self.save_dir = setting[1]

    def run(self, data):
        """Run Setter on all settings, files, and folders.

        Note: 'if settings' statement MUST be the first condition as it
        sets all of the settings on how the class will implement the backup.

        Args:
            data (list): Contains all files, folders, and settings.
        """
        print(self.updater.header)

        files, folders, settings = data

        # settings MUST be first in condition ladder (see doctring)!
        if settings:
            self.set_settings(settings)
            self.create_save_dir()
        if files:
            self.set_files(files)
        if folders:
            self.set_folders(folders)

        print(self.updater.end)
