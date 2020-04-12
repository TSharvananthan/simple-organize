import os

def getAllFiles(mainpath: str) -> list:
    os.chdir(mainpath)

    FILE_TREE = list(os.walk(".", topdown=True)) #gets all the files, still needs to be collected
    base = os.getcwd() #base file path that will be used when moving files

    files = []
    for directory_tup in FILE_TREE:
        files.extend([f"{base}{directory_tup[0][1::]}\\{file}" for file in directory_tup[2]])

    return files
