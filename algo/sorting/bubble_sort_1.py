
def sort_function(input_list):
    l_len = len(input_list)
    for i in range(l_len):
        swapped = False
        for j in range(0, l_len-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                swapped = True
        if swapped is False:
            break
    return input_list

if __name__ == "__main__":
    array_list = [2,1,4,5,7,3,6,9,0]
    print(array_list)
    output_list = sort_function(array_list)
    print(output_list)
