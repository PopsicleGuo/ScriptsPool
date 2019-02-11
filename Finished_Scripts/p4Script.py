
from P4 import P4, P4Exception
# set up instance
p4 = P4()

# Try to get the client info, like client root attribute
# p4.client = 'alvin.guo.laptop'
# p4.connect()
# client = p4.fetch_client()
# print(client)
# p4.disconnect()

# Start to sync the special path from branch
try:
    p4.client = 'alvin.guo_xxx-IDL276_6020'
    p4.user = 'alvin.guo'
    p4.port = 'perforce:1666'
    # p4.password = ''
    p4.exception_level = 1
    p4.connect()
    for syncFileInfo in p4.run_sync("//depot/BuildSystem/Bin/Deployed/BuildSystemClient/...#head"):
        print(syncFileInfo['clientFile'])
except P4Exception:
    for e in p4.errors:
        print(e)
finally:
  p4.disconnect()