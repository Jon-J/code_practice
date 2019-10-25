def find_miss(arr):
    length = len(arr)+1
    all_sum = length * (length + 1)/2
    for elem in arr:
        all_sum -= elem

    return all_sum 

a = [1,2,3,4,5,7,8]
print(find_miss(a))
