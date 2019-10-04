#https://www.geeksforgeeks.org/find-zeroes-to-be-flipped-so-that-number-of-consecutive-1s-is-maximized/
def find_zeroes(arr, m):
    length = len(arr)

    window_l = window_r = 0

    best_left = best_window = 0
    zero_count = 0

    while window_r < length:

        if zero_count <= m:
            if arr[window_r] == 0:
                zero_count += 1
            window_r += 1

        if zero_count > m:
            if arr[window_l] == 0:
                zero_count -= 1
            window_l += 1

        if (window_r - window_l) > best_window and zero_count == m:
            best_window = window_r - window_l
            best_left = window_l


    for i in range(0, best_window):
        if arr[best_left + i] == 0:
            print("index - {}".format(best_left+i))

a = [1,1,0,1,0,1,1,1,0,1,1]
find_zeroes(a, 1)
a = [0,1,1,1,1,0,0,1,0,1,1]
find_zeroes(a, 1)
a = [0,1,0,1,0,0,1,1,1,0,1]
find_zeroes(a, 1)
