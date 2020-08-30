#!/bin/env python3

import os
import psutil  # 3rd party
import sys
import platform
import shutil


def duplicate_file(filename):
    if os.path.isfile(filename):
        new_file = filename + '.dupl'
        shutil.copy(filename, new_file)
        if os.path.exists(new_file):
            print(f"file: { filename } was copied to { new_file }")
            return True
        else:
            print("Error while copy")
            return False


def sys_info():
    print("System information: ")
    print("\tNumber of processors: ", psutil.cpu_count())
    print("\tOS Platform: ", sys.platform)
    print("\tFilesystem encoding: ", sys.getfilesystemencoding())
    print("\tCurrent workdir: ", os.getcwd())
    print("\tCurrent user: ", os.getlogin())
    return 0


def remove_duplicates(directory_name):
    f_list = os.listdir(directory_name)
    counter = 0
    for f in f_list:
        fullname = os.path.join(directory_name, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            counter += 1
    print(f"Removed: { counter } files")
    print("Files in directory:")
    for filename in os.listdir(directory_name):
        if os.path.isfile(filename):
            print(filename)


print("Hello")
answer = ''
while answer != 'q':
    answer = input("Let's do some work (Y/N/q to quit): ")
    if answer == 'Y': 
        print("What do you prefer to do: ")
        print(" [1] - list files")
        print(" [2] - system information")
        print(" [3] - process information")
        print(" [4] - create copy of files in current directory")
        print(" [5] - create copy of file in current directory")
        print(" [6] - remove dupl files in some directory")
        action = int(input("what will we do?: "))

        if action == 1:
            print(os.listdir())
        elif action == 2:
            sys_info()
        elif action == 3:
            print(psutil.pids())
        elif action == 4:
            print("Duplicate files")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                duplicate_file(file_list[i])
                i += 1
        elif action == 5:
            print("Files in current directory: \n", os.listdir())
            file_name = input("Enter file name to duplicate: ")
            duplicate_file(file_name)
            print("Files in current directory: \n", os.listdir())
        elif action == 6:
            directory = input("enter path to directory to cleanup from dupl files: ")
            remove_duplicates(directory)
    
    elif answer == 'N': 
        print("See you later then.")
    else:
        print("Unknown answer.")
        pass
