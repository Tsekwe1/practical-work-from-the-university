#this is for test
def bubble_sort(array):
    n = len(array)
    for pass_num in range(n - 1, 0, -1):
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        
    return array

a = [1, 5, 6, 4, 90, 76, 46, 20, 8]
sort_1 = bubble_sort(a)
print('bubble_sort', sort_1,'\n')


def selection_sort(array):
    v = len(array)
    for l in range(v - 1, 0, -1):
        maxpos = 0
        for j in range(1, l + 1):
            if array[maxpos] < array[l]:
                maxpos = j
            array[l], array[maxpos] = array[maxpos], array[l]
    return array


c = [13, 5, 2, 56, 71, 34, 10, 8, 49]
sort_2 = selection_sort(c)
print('selection_sort', sort_2,'\n')


def insertion_sort(array):
    q = len(array)
    for index in range(1, q):
        currentValue = array[index]
        position = index
        while position > 0:
            if array[position - 1] > currentValue:
                array[position] = array[position - 1]
            else:
                break
            position -= 1
        array[position] = currentValue
    return array
    

p = [12, 9, 23, 89, 11, 73, 17, 7, 86]
sort_3 = selection_sort(p)
print('insertion_sort', sort_3,'\n')