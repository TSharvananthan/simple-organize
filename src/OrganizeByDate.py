import os
import time

class OrganizeByDate:
    def __init__(self, basepath):
        self.basepath = basepath
        self.files = []
        self.filenames = []
        self.times = []
        self.possible_dates = []

    def getAllFiles(self):
        os.chdir(self.basepath)

        FILE_TREE = list(os.walk(".", topdown=True)) #gets all the files, still needs to be collected
        base = os.getcwd() #base file path that will be used when moving files

        for directory_tup in FILE_TREE:
            self.files.extend([f"{base}{directory_tup[0][1::]}\\{file}" for file in directory_tup[2]])
            self.filenames.extend([file for file in directory_tup[2]])

    def getAllDays(self):
        for file in self.files:
            times = [x for x in time.ctime(os.path.getmtime(file)).split(" ") if not x == ""]
            self.times.append(f"{times[4]}-{times[1]}-{times[2]}")

    def getAllPossibleDates(self):
        self.possible_dates = list(set(self.times))

    def createFiles(self):
        os.chdir(self.basepath)
        for file_name in self.possible_dates:
            try:
                os.mkdir(file_name)
            except FileExistsError:
                pass
            except FileNotFoundError:
                print("File Cannot Be Transferred: File Format Not Found")

    def moveFiles(self):
        for file, time, name in zip(self.files, self.times, self.filenames):
            os.replace(file, f"{self.basepath}\\{time}\\{name}")

    def test(self):
        print(self.basepath)
        print(self.files)
        print(self.filenames)
        print(self.times)
        print(self.possible_dates)
