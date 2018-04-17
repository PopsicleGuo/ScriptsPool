import os
from PIL import Image

def search_resize():
    rootDir = "c:\document\censorship\may"
    outDir = "c:\dirtest"
    # put all files with its path into a list
    files = [os.path.relpath(os.path.join(dirpath, file), rootDir)
         for (dirpath, dirnames, filenames) in os.walk(rootDir) for file in filenames]
    # iterate the whole list to choose *.png files
    for i in files:
        if i.endswith('.png'):
            oriPath = os.path.join(rootDir, i) #combine the rootDir folder with rest path and fileName
            im = Image.open(oriPath)
            outfile = os.path.join(outDir, i)
            im.resize((512, 512)).save(outfile)
        else:
            break
# execute the previously function and print success result
if __name__ == '__main__':
    search_resize()
    print("Script has been updated")