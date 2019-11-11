def get_frequencies(arr):
    pos = 0
    n = len(arr)
    while pos < n:
        expected_pos = arr[pos] - 1
        if arr[pos] > 0 and arr[expected_pos] > 0:
            arr[pos], arr[expected_pos] = arr[expected_pos], arr[pos]
            arr[expected_pos] = -1
        elif arr[pos] > 0:
            arr[expected_pos] -= 1
            arr[pos] = 0
        else:
            pos += 1

    for i in range(n):
        print("{} frequency is {}".format(i+1, abs(arr[i])))

a = [1,2,2,3,4,5,3,4,1,1,3,2,4,6,3,2,7,8,9]
get_frequencies(a)
