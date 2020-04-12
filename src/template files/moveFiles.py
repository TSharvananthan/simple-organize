import os

def moveFiles(files: list, formats: list, basefile: str, filenames: list) -> None:
    for file, format, name in zip(files, formats, filenames):
        os.replace(file, f"{basefile}\\{format}\\{name}")
