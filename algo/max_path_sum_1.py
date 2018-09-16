def max_sum_path(triangle):
    depth = len(triangle)
    tt = range(depth-2,-1,-1)
    for i in range(depth-2,-1,-1): #This will create backward index from 98,97,96 to 0.
        for j in range(0,len(triangle[i])):
            triangle[i][j] += max([triangle[i+1][j], triangle[i+1][j+1]]) # Find which number is greater between two numbers.

    print("Result: " + str(triangle[0][0]))

if __name__ == '__main__':
    # Read the problem matrix into a triangle array in python
    filename = 'euler67.txt'
    with open(filename, "r") as ins:
        array = []
        for line in ins:
            array.append(line)
    # Convert the triangle arry entries into integers
    newArray = []
    for i in array:
        j = i.split(' ')
        k = [int(n) for n in j]
        newArray.append(k)
    l = len(newArray)
    result = max_sum_path(newArray)
