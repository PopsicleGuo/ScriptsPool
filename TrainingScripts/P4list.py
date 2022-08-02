'''
This script will try to get both server & local deport files full path for future comparing
'''
import sys
from P4 import P4, P4Exception
from datetime import datetime

doc_name = datetime.now().strftime("%Y%m%d%H%M%S") + ".txt"
p4 = P4()


def get_depot_path(depot_path):
    result = []
    with p4.connect():
        output = p4.run("files", "-e", depot_path + '...')
        for x in range(len(output)):
            result.append(output[x]["depotFile"])
    return result


def get_client_path():
    local_result = []
    with p4.connect():
        output = p4.run("files", "-e", "//" + p4.client + '/...')
        for i in range(len(output)):
            local_result.append(output[i]["depotFile"])
    return local_result


def control_processer(input):
    f = open(doc_name, "w")
    try:
        p4.exception_level = 2  # default value is 2

        list_svr = get_depot_path(input)
        list_loc = get_client_path()
        final_list = []

        for item in list_svr:
            if item not in list_loc:
                final_list.append(item)
                f.write(item + "\n")
    except P4Exception:
        for e in p4.errors:
            print(e)
    f.close()


if __name__ == "__main__":
    input = str(sys.argv[1])
    local_path = str(sys.argv[2])

    control_processer(input)