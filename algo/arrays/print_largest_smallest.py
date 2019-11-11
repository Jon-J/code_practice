import sys
def print_smallest_largest(arr):
    n = len(arr)
    largest = 0
    smallest = sys.maxsize
    for i in range(0, n, 2):
        if i+1 >= n:
            if arr[i] < smallest:
                smallest = arr[i]
            if arr[i] > largest:
                largest = arr[i]
        elif arr[i] < arr[i+1]:
            if arr[i] < smallest:
                smallest = arr[i]
            if arr[i+1] > largest:
                largest = arr[i+1]
        else:
            if arr[i+1] < smallest:
                smallest = arr[i+1]
            if arr[i] > largest:
                largest = arr[i]
    print("Largest - {}, Smallest - {}.".format(largest, smallest))

a = [3,2,1,4,5,2,8,5]
print_smallest_largest(a)
a = [5,7,3,8,8,3,90,2,3,4]
print_smallest_largest(a)
