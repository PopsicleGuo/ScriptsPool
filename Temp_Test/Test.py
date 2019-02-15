
''''
 A temp test py file for random password creation
'''

import random as rd
import string as str

def GenerateChar(l):
    return ''.join(rd.choice(str.ascii_letters) for i in range(l))


def GenerByDec(l):
    return ''.join(chr(rd.randrange(33, 122, 2)) for i in range(l))


'''
 Output 20 length random password
'''
def key_strings():
    return str.ascii_letters + str.digits


def key_gen(amount):
    outlist = [rd.choice(key_strings()) for x in range(amount)]
    return ''.join(outlist)

#print(key_gen(20))

'''
Yield knowledge
'''
# encoding:UTF-8
def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)
    print("do something.")
    print("end.")


def call(x):
    return x * 2


for i in yield_test(5):
    print(i, ",")