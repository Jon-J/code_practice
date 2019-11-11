def find_max_diff(arr):
    max_diff = -1
    max_right = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > max_right:
            max_right = arr[i]
        else:
            diff = max_right - arr[i]
            if diff > max_diff:
                max_diff = diff
    return max_diff

a = [1,3,9,4,5,10]
print(find_max_diff(a))
a = [1, 2, 90, 10, 110]
print(find_max_diff(a))
