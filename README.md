# PlanB

PlanB v.1.1.0 (Python 3.5)

PlanB (Plan Backup) is a backup solution written in Python.

Check the project's [Wiki](https://github.com/Kwistech/PlanB/wiki) for more info.

## Installation & Runtime

+ Fork the repository and clone it to your local drive.
+ Open a terminal and go to the program's root directory.
+ From the program's root directory, type: `python main.py`

## How the Program Works

The program uses the JSON files in its data directory to access the files, folders, and settings for the program. Once the program has read this data, it then starts to copy and paste this data into the save directory found in the settings file. 

## How To Use

To use PlanB, a user enters all of the paths they would like to backup into the save directory. 

To backup a directory, a user enters the path to the directory into the folders.json file found in the programs data directory.
To backup a file. a user enters the path to the file into the files.json file found in the programs data directory.

Once all of the paths that the user wants to backup are entered into the appropriate files, the user can initiate the Installation & Runtime component (see Installation & Runtime above).
