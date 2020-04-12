import os

def getAllFileFormats(files):
    return ([os.path.splitext(x)[1] for x in files])
