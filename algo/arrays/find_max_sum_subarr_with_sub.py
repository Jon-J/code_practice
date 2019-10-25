from sys import maxsize

def find_max_sum_with_sub(arr):
    max_final = -maxsize-1
    curr_max = 0
    size = len(arr)

    start = end = s = 0

    for i in range(0, size):
        curr_max += arr[i]

        if max_final < curr_max:
            max_final = curr_max
            start = s
            end = i

        if curr_max < 0:
            curr_max = 0
            s += 1

    print("Max sum = {}, start index = {} and end index = {}".format(max_final, start, end))

a = [-2, -3, 4, -1, -2, 1, 5, -3]
find_max_sum_with_sub(a)

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
find_max_sum_with_sub(a)
