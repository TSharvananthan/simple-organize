import argparse
from src.OrganizeByFileFormat import OrganizeByFileFormat
from src.OrganizeByDate import OrganizeByDate

'Arguments'
argParser = argparse.ArgumentParser()
argParser.add_argument("main_branch", type=str, help="the starting branch. any files in this branch will be organized")

args = argParser.parse_args()

'FileFormatOrganization'
def main():
    global args
    BASEFILEPATH = args.main_branch.replace("/", "//")

    object = OrganizeByDate(BASEFILEPATH)
    object.getAllFiles()
    object.getAllDays()
    object.getAllPossibleDates()
    object.createFiles()
    object.moveFiles()

main()
