def check_pairwise_sorted(arr):
    n = len(arr)

    if n == 0 or n == 1:
        return True

    for i in range(0, n, 2):
        if arr[i] > arr[i+1]:
            return False
    return True

a = [1,2,5,6,10,12]
print(check_pairwise_sorted(a))
a = [3,2,5,6,10,12]
print(check_pairwise_sorted(a))
