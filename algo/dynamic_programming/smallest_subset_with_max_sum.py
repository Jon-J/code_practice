# Pyhton3 code to find minimum number of 
# elements such that their sum is greater 
# than sum of remaining elements of the array. 

# function to find minimum elements needed. 
def minElements(arr , n): 

	# calculating HALF of array sum 
	halfSum = 0
	for i in range(n): 
		halfSum = halfSum + arr[i] 
	
	halfSum = int(halfSum / 2) 
	
	# sort the array in descending order. 
	arr.sort(reverse = True) 
	val = []
	res = 0
	curr_sum = 0
	for i in range(n): 
		curr_sum += arr[i] 
		res += 1
		val.append(arr[i])
		# current sum greater than sum 
		if curr_sum > halfSum: 
			print(halfSum)
			return res,val 
	
	return res,val 
	
# driver code 
arr = [3, 1, 7, 1] 
arr = [3, 7, 4, 6, 5]
arr = [2, 1, 5, 8, 4]
arr = [3, 5, -7, 8, 10]
arr = [2,1,2]
n = len(arr) 
a,b = minElements(arr, n)
print(a)
print(b)

# This code is cntributed by "Sharad_Bhardwaj". 

