def separate_0_1(arr):
    j = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            j += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

a = [0,1,1,1,0,0,1,0,1]
separate_0_1(a)
print(a)
