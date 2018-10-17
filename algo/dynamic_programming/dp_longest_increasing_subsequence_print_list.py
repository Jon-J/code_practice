# Dynamic programming Python implementation of LIS problem 
#Solution:
#if(arr[i] > arr[j]) { T[i] = max(T[i], T[j] + 1 }
#
#Time Complexity is O(n^2)
#Space Complexity is O(n)
#
#http://en.wikipedia.org/wiki/Longest_increasing_subsequence
#

# lis returns length of the longest increasing subsequence 
# in arr of size n 
def lis(arr): 
    n = len(arr) 
  
    # Declare the list (array) for LIS and initialize LIS 
    # values for all indexes 
    lis = [1]*n 

    prev = [0]*n
    for i in range(0, n):
        prev[i] = i

  
    # Compute optimized LIS values in bottom up manner 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
                prev[i] = j
  
    # Initialize maximum to 0 to get the maximum of all 
    # LIS 
    maximum = 0
    idx = 0

    # Pick maximum of all LIS values 
    for i in range(n): 
        if maximum < lis[i]:
            idx = i
        maximum = max(maximum , lis[i]) 
        

    seq = [arr[idx]]
    while idx != prev[idx]:
        idx = prev[idx]
        seq.append(arr[idx])

    return (maximum, reversed(seq))

# end of lis function 
  
# Driver program to test above function 
arr = [10, 22, 9, 33, 21, 50, 41, 60] 
result = lis(arr)
print("Length of lis is")
print(result[0])
print("The longest sequence is", ", ".join(str(x) for x in result[1]))
