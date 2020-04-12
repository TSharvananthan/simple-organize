import argparse
from src.OrganizeByFileFormat import OrganizeByFileFormat

'Arguments'
argParser = argparse.ArgumentParser()
argParser.add_argument("main_branch", type=str, help="the starting branch. any files in this branch will be organized")

args = argParser.parse_args()

'FileFormatOrganization'
def main():
    global args
    BASEFILEPATH = args.main_branch.replace("/", "//")

    object = OrganizeByFileFormat(BASEFILEPATH)
    object.getAllFiles()
    object.print_test()
    object.getAllFileFormats()
    object.print_test()
    object.createFiles()
    object.print_test()
    object.moveFiles(BASEFILEPATH)
    object.print_test()

main()
