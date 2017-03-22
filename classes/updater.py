class Updater(object):

    def __init__(self):
        self.header = "Backing up data...\n"
        self.working = "Currently backing up '{}'..."
        self.success = "Successfully backed up '{}' to '{}'.\n"
        self.file_exists_error = "File Exists Error!\n"
        self.file_not_found_error = "File Not Found Error!\n"
        self.end = "Backup Done!"
