import argparse
import os
from src.getAllFiles import getAllFiles
from src.getAllFileFormats import getAllFileFormats

argParser = argparse.ArgumentParser()
argParser.add_argument("main_branch", type=str, help="the starting branch. any files in this branch will be organized")

args = argParser.parse_args()

FILEPATH = args.main_branch.replace("/", "//")
