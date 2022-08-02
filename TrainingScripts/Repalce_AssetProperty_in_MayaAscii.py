'''
    Try to create a new asset file with new asset name/values purpose
'''
import re, sys

'''
Open a MA file and reads the line one by one.
Iterate the content 1 by 1 for regular expression checking
Create another empty file to write down the un-updated/updated line
'''
def replace(file_path, cname, name):
    with open(file_path, 'r', encoding='ascii') as f:
        with open(name+'.ma', 'w', encoding='ascii') as a:
            total = f.readlines()
            ditgits_re = r'\b' + cname
            for item in total:
                result = re.findall(ditgits_re, item)
                if not len(result) == 0:
                    a.writelines(re.sub(ditgits_re, name, item))
                else:
                    a.write(item)


if __name__ == "__main__":
    file_path = str(sys.argv[1])
    cname = str(sys.argv[2])
    name = str(sys.argv[3])

    replace(file_path, cname, name)
    print('The updated MA file has been created!!')