import os


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
    return test_path


'''
Remove the folder list 
'''
def remove_files():
    path = check_path()
    try:
        os.rmdir(path)
        print("Folder has been removed")
    except SystemError:

