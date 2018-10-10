def partition(array, start, end):
    p_index = (start-1 )
    pivot = array[end]
    for i in range(start, end):
        if array[i] <= pivot:
            p_index += 1
            array[p_index], array[i] = array[i], array[p_index]
    array[p_index+1], array[end] = array[end], array[p_index+1]
    return p_index+1

def quick_sort(array, start, end):
    if start < end:
        p_indx = partition(array, start, end)

        quick_sort(array, start, p_indx-1)
        quick_sort(array, p_indx+1, end)

t = [3,1,5,7,9,8,6,4,2]
quick_sort(t, 0, len(t)-1)
print(t)
