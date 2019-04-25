'''
    A script for the file renaming iteration
'''

import sys, os, re, shutil

source_root = "P:\\Temp_Test" # The original file pool for query
direction = "P:\\Test"         # Which folder we want to put the renamed file in


# Func will create the multiple folders/files for testing
def folder_creation():
    head = "manga_"
    count = 100
    i = 0
    while i < count:
        name = os.path.join(source_root, (head+str(i)))
        os.mkdir(name)
        in_count = 0
        while in_count < 5:
            with open(os.path.join(name, str(in_count + '.txt')), "w", encoding="utf-8") as f:
                f.write("placeholder + " + i)
            in_count += 1
        i += 1


# Take the numeric value/s from the string of dir path by regular expression
def get_numeric(string):
    result = re.findall(r'\d+', string)
    return result


# Go through the files from the pool to get the path, then rename the file name
# in memory, recombine the direction path with new name and move it
for dirpath, dirnames, filenames in os.walk(source_root):
    for file in filenames:
        source = os.path.join(dirpath, file)
        covertedname = ''.join(re.findall(r'\d+', dirpath)) + '-' + file
        output = os.path.join(direction, covertedname)
        shutil.copy2(source, output)