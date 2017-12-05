
# Try to make sql table into dictionaries

f = open("account.txt", "r")

accountdicts = {}

for line in f:
    entry = line.strip().split("\t")
userid = entry[0]
username = entry[1]
accountdicts[userid] = username

f.close()

print(accountdicts)

# Try to search the user's want
# searchdata = list(accountdicts.keys())
# print(searchdata)

accountguess = input("What is you want to search: ")

for loopdata in accountdicts.iteritems():
    if accountguess == loopdata:
        print("Here you are ", loopdata)
    else:
        print("Sorry, no results")
        