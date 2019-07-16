# Python3 program to 
# Check if the string is pangram 
import string 

alphabet = set(string.ascii_lowercase) 

def ispangram(str): 
	return not set(alphabet) - set(str) 
	
# Driver code 
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True): 
	print("Yes") 
else: 
	print("No") 

