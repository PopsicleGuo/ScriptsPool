from random import randint
'''  Selection Sort Algorithm  '''


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


'''  Insertion Sort Algorithm  '''


def InsertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            Swap(array, j, j -1)
            j -= 1


'''  Bubble Sort Algorithm  '''


def BubbleSort(array):
    for i in range(len(array)):
        trigger = False
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                trigger = True
                Swap(array, j, j+1)

        if not trigger:
            break


''' Quick Sort Algorithm '''


def QuickSort(array):
    if len(array) <= 1:
        return

    pivot = array[0]


''' Sort list 1st example  '''
integerValues = [-11, 12, -42, 0, 1, 90, 68, 6, -9]


''' Sort list 2nd example '''


def random_list(number):
    sort_list = [randint(0, 1000000) for n in range(0, number)]
    return sort_list
