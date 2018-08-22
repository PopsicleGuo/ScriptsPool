import sys
from P4 import P4, P4Exception
# set up instance
p4 = P4()

'''
Try to get folder structure from //depot folder
'''
def getFolder():
    try:
        p4.client = 'EASH-wenqiguo-picinc-dev'
        p4.user = 'EASAP\wenqiguo'
        p4.port = 'vgsproxy04:1666'
        # p4.password = ''
        p4.exception_level = 1
        p4.connect()
        info = p4.run("dirs", "//pvz/*/*/*/*/*")
        for i in info:
            print(i)
    except P4Exception:
        for e in p4.errors:
            print(e)
    finally:
        p4.disconnect()



'''
Try to get files from depot folder and output the result to another file
'''
def getFiles():
    try:
        p4.client = 'EASH-wenqiguo-picinc-dev'
        p4.user = 'EASAP\wenqiguo'
        p4.port = 'vgsproxy04:1666'
        # p4.password = ''
        p4.exception_level = 1
        p4.connect()
        info = p4.run("files", "//pvz/...#head")
        f = open('p:\originallist.txt', 'w')
        for i in info:
            #print(i['depotFile'].encode(sys.stdout.encoding, errors='replace'))
            f.writelines(str(i['depotFile'].encode(sys.stdout.encoding, errors='replace')))
        f.close()
    except P4Exception:
        for e in p4.errors:
            print(e)
    finally:
        p4.disconnect()


# getFolder()

getFiles()