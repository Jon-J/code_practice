def check_duplicate(arr):
    for elem in arr:
        if elem < 0 :
            print("Duplicate - {}".format(abs(elem)))
        else:
            arr[elem] = -arr[elem]
    return

a = [1, 2, 5, 3, 2, 3, 4]
check_duplicate(a)
