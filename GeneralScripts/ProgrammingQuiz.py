

""" Solution 1  """

input = [1, 2, 3, 4, 5, 6]

print(input[int(len(input)/2):len(input)]  +  input[0:int(len(input)/2)])



""" Solution 2  """

input1 = [1, 2, 3, 4, 5, 6]
p = []
y = len(input1) -1

for index in range(len(input1)):
    if index >= int(len(input1)/2):
        m = input1[y]
        p.append(m)
        y -= 1
    else:
        m = input[index]
        p.append(m)

print(p)