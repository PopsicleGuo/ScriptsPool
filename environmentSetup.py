import subprocess

command = "dir p:\software"
result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

print(result)