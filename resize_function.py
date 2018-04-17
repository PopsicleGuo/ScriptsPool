from PIL import Image
import os

def fileResize():
    path = 'C:\Document\PNG'
    for infile in os.listdir(path):
        if infile.endswith(".png"):
            im = Image.open(infile)
            width, height = im.size
            outfile = os.path.join("C:\\test", infile)
            #halfsize = os.path.join("C:\\", infile)
            im.resize((512, 512)).save(outfile)
            im.resize((width//2, height//2)).save("c:\halfsize.png")

if __name__ == '__main__':
    fileResize()
