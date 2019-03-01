print "Program to find the number of composite numbers between 1 and 100."
def isprime(n): # Function returns True if n is prime, False if not. 
    flag = True
    for j in range(2,n+1):
        if (n % j ==0 and j<>n): # n is composite (not prime).
            flag = False
            return flag
        else:
            if n ==j: # all possible divisors checked. Number,n is prime.
 
                return flag
print ""            
print " Here is the list:"
count = 0
for n in range(2,100):
    if not isprime(n):
        count +=1
        print count,".",n," ",
print ""
print "There are",count,"composite numbers between 1 and 100."
