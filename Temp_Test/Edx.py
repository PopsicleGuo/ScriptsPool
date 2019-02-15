

'''
Edx Problem 1 W1
'''


s = 'azcbobobegghakl'
count = 0
for i in s:
    if i in 'aeiou':
        count += 1
print("Number of vowels: %d " % count)


'''
Edx Problem 2 W1
'''

f = 'azcbobobegghakl'
count1 = 0

for i in range(len(f)-2):
    if f[i] == 'b' and f[i+1] == 'o' and f[i+2] == 'b':
        count1 += 1
print("Number of vowels: %d " % count1)


'''
Edx Problem 3 W1
'''

s = 'azcbobobegghakl'
count = 0
max_count = 0
#result = 0
substring = ''

for i in range(len(s) - 1):
    if s[i] <= s[i + 1]:
        count += 1
        if count > max_count:
            max_count = count
            #result = i + 1
            substring = s[i + 1 - max_count:i+2]
    else:
        count = 0

#start_position = result - max_count
#print('Longest substring in alphabetical order is: ', s[start_position:result + 1])
print('Longest substring in alphabetical order is: ', substring)


'''
Edx W2 Exercise: square
'''

def suqare(x):
    return x**2


'''
Edx W2 Exercise: eval quadratic
'''

def evalQuadratic(a, b, c, x):
    return (a*(x**2) + b*x + c)