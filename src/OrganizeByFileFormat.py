import os

class OrganizeByFileFormat:
    def __init__(self, basepath):
        self.basepath = basepath
        self.files = []
        self.filenames = []
        self.fileformats = []

    def getAllFiles(self):
        os.chdir(self.basepath)

        FILE_TREE = list(os.walk(".", topdown=True)) #gets all the files, still needs to be collected
        base = os.getcwd() #base file path that will be used when moving files

        files, filenames = [], []
        for directory_tup in FILE_TREE:
            files.extend([f"{base}{directory_tup[0][1::]}\\{file}" for file in directory_tup[2]])
            filenames.extend([file for file in directory_tup[2]])

        self.files = files
        self.filenames = filenames

    def getAllFileFormats(self):
        self.fileformats = [os.path.splitext(x)[1] for x in self.files]

    def createFiles(self):
        for format in self.fileformats:
            try:
                os.mkdir(format)
            except FileExistsError:
                pass
            except FileNotFoundError:
                print("File Cannot Be Transferred: File Format Not Found")

    def moveFiles(self, basefile):
        for file, format, name in zip(self.files, self.fileformats, self.filenames):
            os.replace(file, f"{basefile}\\{format}\\{name}")

    def print_test(self):
        print("self.basepath -> ", self.basepath)
        print("self.files -> ", self.files)
        print("self.filenames -> ", self.filenames)
        print("self.fileformats -> ", self.fileformats)
