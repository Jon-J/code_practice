import sys
def partition(arr, l, r):
    i = l-1
    pivot = arr[r]

    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quick_sort(sort_list, l, h):
    if l<h:
        part = partition(sort_list, l, h)
        quick_sort(sort_list, l, part-1)
        quick_sort(sort_list, part+1, h)


def find_min_sum_closet_zero(arr):
    curr_sum, min_sum = 0, sys.maxsize
    l = 0
    r = len(arr) - 1

    min_l = l
    min_r = r

    quick_sort(arr, l, r)

    while l<r:
        curr_sum = arr[l] + arr[r]

        if abs(curr_sum) < abs(min_sum):
            min_sum = curr_sum
            min_l = l
            min_r = r
        if curr_sum < 0:
            l +=1 
        else:
            r -= 1
    print("Sum {} is closest to zero for {} and {}.".format(min_sum, arr[min_l], arr[min_r]))

a = [1,2,3,4,5,6]
find_min_sum_closet_zero(a)
a = [-1,2,3,4,5,6]
find_min_sum_closet_zero(a)
a = [6,4,-5,1,9]
find_min_sum_closet_zero(a)
