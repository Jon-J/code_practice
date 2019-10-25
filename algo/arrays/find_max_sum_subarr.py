def find_max_sum_in_subarr(arr):
    size = len(arr)
    curr_max = arr[0]
    max_sum = arr[0]

    for idx in range(1, size):
        curr_max = max(arr[idx], curr_max + arr[idx])
        max_sum = max(max_sum, curr_max)

    return max_sum

a = [-2, -3, 4, -1, -2, 1, 5, -3] 
print(find_max_sum_in_subarr(a))

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
print(find_max_sum_in_subarr(a))
