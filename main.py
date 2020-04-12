import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("main_branch", type="str", help="the starting branch. any files in this branch will be organized")

args = argParser.parse_args()
