def shuffle_list(arr, low, high):

    if high < low:
        return

    if high - low == 1:
        return

    n = len(arr)
    mid = int((low + high)//2)

    temp = mid + 1

    mmid  = int((low + mid)//2)

    for i in range(mmid + 1, mid + 1):
        arr[i], arr[temp] = arr[temp], arr[i]
        temp +=1

    shuffle_list(arr, low, mid)
    shuffle_list(arr, mid+1, high)

a = [1,3,5,7,2,4,6,8]
shuffle_list(a, 0, len(a)-1)
print(a)
