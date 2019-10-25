def max_repition(arr):
    max = 0
    max_index = 0

    length = len(arr)

    for i in range(length):
        arr[arr[i]%length] += length

    for i in range(length):
        if arr[i]/length > max:
            max = arr[i]//length
            max_index = i
    print("Max index - {}, max times - {}".format(max_index, max))

a = [1,2,2,3,4,2,5,3,4,6,6,6,6,6,6]
max_repition(a)
