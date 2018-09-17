from sys import getrecursionlimit, setrecursionlimit

def partition(input_array, start, end):
    pivot = input_array[end]
    p_index = ( start - 1 )
    for index in range(start, end):
        if input_array[index] <= pivot:
            p_index += 1
            input_array[index], input_array[p_index] = input_array[p_index], input_array[index]
    input_array[p_index+1], input_array[end] = input_array[end], input_array[p_index+1]
    return p_index+1

def quick_sort(input_array, start, end):
    if start < end:
        p_index = partition(input_array, start, end)
        quick_sort(input_array, start, p_index-1)
        quick_sort(input_array, p_index+1, end)
    return    

test_list = [8, 2,6,4,1,3,5, 9]
print(test_list)
setrecursionlimit(3500)
quick_sort(test_list, 0, len(test_list)-1)
print(test_list)
