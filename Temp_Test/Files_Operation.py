import sys, os, re, shutil

root = "P:\\Temp_Test"
target = "P:\\Test"


# Create the folder and files for testing
def folderCreation():
    head = "manga_"
    count = 100
    i = 0
    while i < count:
        name = os.path.join(root, (head+str(i)))
        os.mkdir(name)
        in_count = 0
        while in_count < 5:
            with open(os.path.join(name, str(in_count + '.txt')), "w", encoding="utf-8") as f:
                f.write("placeholder + " + i)
        i += 1


# Take the numeric from dir path string
def get_numeric(string):
    result = re.findall(r'\d+', string)
    return result


# for dirpath, dirnames, filenames in os.walk(root):
#     newfile_name = ''.join(get_numeric(dirnames)) + '-' + ''.join(filenames)
#     print(newfile_name)
#     output = os.path.join(target, newfile_name)
#     print(output)
#     orginaldirpath = os.path.join(dirpath, filenames)
#     #shutil.copy2(orginaldirpath, output)

# Go through the whole resource folder to get renamed files with path, then move it
for dirpath, dirnames, filenames in os.walk(root):
    for file in filenames:
        source = os.path.join(dirpath, file)
        covertedname = ''.join(re.findall(r'\d+', dirpath)) + '-' + file
        output = os.path.join(target, covertedname)
        shutil.copy2(source, output)