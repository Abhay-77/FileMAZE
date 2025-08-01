import os

path = "dog"

def renameFile(path):
    for i in os.listdir(path):
        curPath = path + "/" + i
        if os.path.isdir(curPath):
            print(curPath)
            renameFile(curPath)
        else:
            print("File" + curPath)

print(renameFile(path))