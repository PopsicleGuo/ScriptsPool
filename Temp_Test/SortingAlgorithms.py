
'''
    Selection Sort Algo
'''


def Sort(array):
    for i in range(len(array)):
        mixIndex = i
        mixValue = array[i]

        for j in range(i +1, len(array)):
            if array[j] < mixValue:
                mixValue = array[j]
                mixIndex = j

        Swap(array, i, mixIndex)


def Swap(array, first, second):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp



'''
    Insertion Sort Algo
'''


def InsertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            Swap(array, j, j -1)
            j -= 1



integerValues1 = [-11, 12, -42, 0, 1, 90, 68, 6, -9]
integerValues2 = [-11, 12, -42, 0, 1, 90, 68, 6, -9]
Sort(integerValues1)
InsertionSort(integerValues2)
print(integerValues1)
print(integerValues2)