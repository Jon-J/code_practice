import sys
import math 

def is_prime(num):
	for j in range(2,int(math.sqrt(num)+1)):
		if (num % j) == 0: 
			return False
	return True

def main(argv):

	i = 0
	num = 2
	nth = int(argv)
		
	while i < nth:
		if is_prime(num): 
			i += 1
			if i == nth:
				print('The ' + str(nth) + ' prime number is: ' + str(num))
		num += 1 
	
if __name__ == "__main__":
	main(600851475143)
