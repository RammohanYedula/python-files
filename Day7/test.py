import os


folders = input("Please provide list of folders names with spaces in between:").split()


for folders in folders:
    try:
        files = os.listdir(folders)
    except FileNotFoundError:
        print("Please provide a valid folder name")
        continue
    except PermissionError:
        print("No access to this folder:" + folders)
    print("=====listing fies for the folder -" + folders)

    for files in files:
        print(files)