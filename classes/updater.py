class Updater(object):
    """Command-line Updater class."""

    def __init__(self):
        """Initialize all updates to be displayed in the command-line."""
        self.header = "Backing up data...\n"
        self.working = "Currently backing up '{}'..."
        self.success = "Successfully backed up '{}' to '{}'.\n"
        self.file_exists_error = "ERROR: File Exists!\n"
        self.file_not_found_error = "ERROR: File Not Found!\n"
        self.end = "Backup Done!"
