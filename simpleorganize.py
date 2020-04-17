import src.simple_organize_classes as soc

def organize_by_date(basefile):
    obj = soc.OrganizeByDate(basefile.replace("/", "//"))
    obj.getAllFiles()
    obj.getAllDays()
    obj.getAllPossibleDates()
    obj.createFiles()
    obj.moveFiles()

def organize_by_file_format(basefile):
    obj = soc.OrganizeByFileFormat(basefile.replace("/", "//"))
    obj.getAllFiles()
    obj.getAllFileFormats()
    obj.createFiles()
    obj.moveFiles(basefile)

def move_to_single_file(basefile, final_dir):
    obj = soc.MoveToSingleFile(basefile, final_dir)
    obj.getAllFiles()
    obj.moveFiles()
