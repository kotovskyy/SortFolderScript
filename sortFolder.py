import os
import sys
import shutil

dirpath = sys.argv[1]
files = os.listdir(dirpath)
regular_files = [file for file in files if os.path.isfile(dirpath + "/" + file)]
directories = [file for file in files if os.path.isdir(dirpath + "/" + file)]
file_extensions = [file.split(sep='.', maxsplit=1)[1] for file in regular_files]
file_extensions_set = set(file_extensions)

for ext in file_extensions_set:
    if not os.path.exists(dirpath + "/" + ext):
        os.mkdir(path=dirpath+"/"+ext)
    for file in regular_files:
        if file.split(sep='.', maxsplit=1)[-1] != ext:
            continue
        source_filepath = dirpath+"/"+file
        destination_filepath = dirpath+"/"+ext
        shutil.move(src=source_filepath,dst=destination_filepath)

for dir in directories:
    if os.listdir(path=dirpath+"/"+dir) == []:
        os.rmdir(dirpath+"/"+dir)
