import os

def createFiles(listofformats: list) -> None:
    for format in listofformats:
        try:
            os.mkdir(format)
        except FileExistsError:
            pass
