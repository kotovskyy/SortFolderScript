import os
import sys
import shutil

# first argument: path to dir to sort
dirpath = os.getcwd() if len(sys.argv) < 2 else sys.args[1]
# get all files from `dirpath`
files = os.listdir(dirpath)
# get all regular files from `files` list
reg_files = [file for file in files if os.path.isfile(dirpath + "/" + file)]
# get all directories from `files` list
directories = [file for file in files if os.path.isdir(dirpath + "/" + file)]
# get all files' extensions
file_extensions = [file.split(sep='.', maxsplit=1)[1] for file in reg_files]
# create a set from extensions list
file_extensions_set = set(file_extensions)

for ext in file_extensions_set:
    # if folder with extension name doesn't exist in `dirpath`
    if not os.path.exists(dirpath + "/" + ext):
        # create folder with name `ext` in `dirpath`
        os.mkdir(path=dirpath+"/"+ext)
    for file in reg_files:
        # for every regular file in `reg_files` list
        # check extension. If ext matches -> move file in `dirpath/ext`
        if file.split(sep='.', maxsplit=1)[-1] != ext:
            continue
        source_filepath = dirpath+"/"+file
        destination_filepath = dirpath+"/"+ext
        shutil.move(src=source_filepath,dst=destination_filepath)

for dir in directories:
    # check for empty directories in `dirpath` and remove them
    if os.listdir(path=dirpath+"/"+dir) == []:
        os.rmdir(dirpath+"/"+dir)
