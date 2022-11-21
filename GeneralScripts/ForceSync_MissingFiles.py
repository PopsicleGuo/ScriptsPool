'''
 This script will check both server and workspace files and force sync the missing file of workspace
'''

import sys, os
import pprint as p
from P4 import P4, P4Exception
from datetime import datetime

p4 = P4()


# Function returns the depot/workspace list by different list, then return tuple value
# p4 command fstat will return depot path and workspace path (p4 have also can do)
def get_depot_path(depotpath, changelist):
    client_paths = []
    server_paths = []
    try:
        with p4.connect():
            output = p4.run("fstat", "-Olhp", "-F ^headAction=delete & ^headAction=move/delete", depotpath + changelist)
            for dic in output:
                if 'path' in dic:
                    server_paths.append(dic['depotFile'])
                    client_paths.append(dic['path'])
    except P4Exception:
        for e in p4.errors:
            print(e)
    tuple_list = zip(server_paths, client_paths)
    return tuple_list


# Function will return a filtered list. Also created a txt for those filtered file path
def func_compare(depot_path, changelist):
    tuple_list = get_depot_path(depot_path, changelist)
    compared_list = []
    doc_name = datetime.now().strftime("%Y%m%d%H%M%S") + "_compared" + ".txt"
    with open(doc_name, "w", encoding="utf-8") as f:
        for item in tuple_list:
            if not os.path.exists(item[-1]):
                compared_list.append(item[0])
                f.write(item[0] + '\n')
    if len(compared_list) > 1:
        print("The missing file has been located!")
    else:
        print("Didn't find any missing files")
    return compared_list


# Func will force sync the missing file through the result list which is come from the comparing function
def force_sync(missing_file_path):
        p4.run("sync", "-f", missing_file_path)

# This func is a control flow for the whole script
def processer(depot_path, changelist):
    fsync_list = func_compare(depot_path, changelist)
    try:
        with p4.connect():
            for item in fsync_list:
                force_sync(item)
            print("All files have been force synced!!")
    except P4Exception:
        for e in p4.errors:
            print(e)


if __name__ == "__main__":
    server = str(sys.argv[1])
    changelist = str(sys.argv[2])
    print(datetime.now().strftime("%Y%m%d%H%M%S"))
    processer(server, changelist)
    print(datetime.now().strftime("%Y%m%d%H%M%S"))
