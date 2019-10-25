def get_2_elem(arr, sum_input):
    elem_set = set()
    size = len(arr)
    for i in range(size):
        tmp = sum_input - arr[i]
        if tmp in elem_set:
            print("Pairs - {}, {} for sum - {}".format(tmp, arr[i], sum_input))
        elem_set.add(arr[i])
a = [1,2,3,4,5,6]
get_2_elem(a, 11)

a = [1,8,2,4,9,6]
get_2_elem(a, 14)
