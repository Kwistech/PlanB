# PlanB (PlanBackup) - Johnathon Kwisses (Kwistech)
from os import listdir
from shutil import copy, copytree
from tkinter import Label, Entry, Button, Tk


class App:
    """Class for desktop application."""

    def __init__(self, root):
        """Initialize sub_text and interface().

        Args:
            root (tkinter.Tk): Tk() object.
        """
        self.sub_text = "Enter the appropriate directories and press Submit"
        self.interface(root)

    def interface(self, root):
        """Define interface Tkinter widgets.

        Args:
            root (tkinter.Tk): Tk() object.
        """
        main_label = Label(root, text="Plan B - Backup Solution")
        main_label.grid(row=0, column=0, columnspan=2)

        sub_label = Label(root, text=self.sub_text)
        sub_label.grid(row=1, column=0, columnspan=3)

        copy_label = Label(root, text="Directory to copy: ")
        copy_label.grid(row=2, column=0, pady=10)

        paste_label = Label(root, text="Directory to paste: ")
        paste_label.grid(row=3, column=0)

        copyright_label = Label(root, text="© 2016 Kwistech")
        copyright_label.grid(row=4, column=0, pady=5, sticky="SW")

        copy_entry = Entry(root, width=30)
        copy_entry.grid(row=2, column=1, padx=5)

        paste_entry = Entry(root, width=30)
        paste_entry.grid(row=3, column=1)

        info = [copy_entry, paste_entry]  # To get user info

        submit_button = Button(root, text="Submit", width=5, height=1,
                               command=lambda: self.copy_paste(info, root))
        submit_button.grid(row=4, column=1, padx=10, pady=10, sticky="E")

    @staticmethod
    def copy_paste(info, root):
        """Get user-entered directories and copy files to paste directory.

        Args:
            info (list): Contains tkinter.Entry objects.
            root (tkinter.Tk): Tk() object.

        Raises:
            PermissionError: If copy attempts to copy a directory.
        """
        copy_dir, paste_dir = [x.get() for x in info]
        [x.delete(first=0, last=139) for x in info]

        for file in listdir(copy_dir):
            directory = "{}\\{}"
            src = directory.format(copy_dir, file)
            dst = directory.format(paste_dir, file)

            try:
                copy(src=src, dst=dst)
            except PermissionError:
                copytree(src=src, dst=dst)

        done_label = Label(root, text="Backup Complete!")
        done_label.grid(row=4, column=1, sticky="W")


def main():
    """Set Tkinter object and initiate class App."""
    root = Tk()
    root.title("Plan B")

    App(root)

    root.mainloop()

if __name__ == "__main__":
    main()
