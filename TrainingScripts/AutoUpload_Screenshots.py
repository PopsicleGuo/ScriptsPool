import os, shutil,sys, errno
from datetime import date


# Trough datetime to make suitable dir
today = date.today()
get_date = ''.join(str(today).split('-'))

dst_root = "\\\\xxxx-fs2\\xxxx\\Projects\\xxxx\\Performance_Test_logs"
upload_root = "p:\\Works\\screenshots\\Performance_test"

src_path = upload_root + "\\" + get_date
dst_path = dst_root + "\\" + get_date


def create_localdir(src):
    try:
        os.makedirs(src)
    except OSError as e:
        # directory already exists
        if e.errno == errno.EEXIST:
            print("Source directory already exists!!")
        else:
            raise


def create_leveldirs(src):
    level_1 = "Cheesemine"
    level_2 = "Suburbs"
    try:
        os.makedirs(src+"\\"+level_1)
        os.makedirs(src+"\\"+level_2)
    except OSError as e:
        if e.errno == errno.EEXIST:
            print("Folders already exist!!")
        else:
            raise


def create_fileserverdir(dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    else:
        print("The destination path already had a same name directory in it!!")


# Move all the files recursively
def dir_mover(src, dst):
    create_fileserverdir(dst)

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            dir_mover(s, d)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)


if __name__ == "__main__":
    processer_id = str(sys.argv[1])
    if processer_id == "false":
        create_localdir(src_path)
        create_leveldirs(src_path)
        print("The folder has been created!!!")
    elif processer_id == "true":
        dir_mover(src_path, dst_path)
        print("Upload process has been finished!!")