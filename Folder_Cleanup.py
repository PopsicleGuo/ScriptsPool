import os
import shutil

'''
Get user input info    
'''

def user_input(foldername):
    string = str(foldername)
    return string


'''
Get computer info
'''

def get_info():
    command = os.popen('echo %USERNAME%')
    result = command.read()
    return result


'''
Check absolute path of input folder name
'''

def check_path():
    name = get_info()
    frost_cache1 = "C:\ProgramData\FrostEd"
    frost_cache2 = '''C:\\Users\{}\AppData\Roaming\FrostEd'''.format(name)
    test_path = 'p:\\test'
    final = [frost_cache1, frost_cache2, test_path]
    return final


'''
Remove the folder list 
'''
def remove_files():
    path = check_path()
    try:
        for i in path:
            if os.path.isfile(i):
                os.remove(i)
            elif os.path.isdir(i):
                shutil.rmtree(i)
            print("Removed %s" % (i))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

