def find_0_starts(arr):
    high = len(arr)
    low = 0
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == 0 and (mid == 0 or arr[mid - 1] == 1):
            return mid
        elif arr[mid] == 0:
            high = high - 1
        else:
            low += 1

    return False

a = [1,1,1,0,0,0]
print(find_0_starts(a))
a = [1,1,1,1,1,1,1,0,0]
print(find_0_starts(a))
a = [0,0,0]
print(find_0_starts(a))
