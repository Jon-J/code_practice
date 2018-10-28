# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = [int(i)  for i in raw_input().split()] 
print n,m
#Create the datastructure, It shall be a list of list.
list_of_sequence = []
for i in xrange(n):
    list_of_sequence.append([])
lastans = 0   
for i in xrange(m):
    
    p,q,r = [int(i)  for i in raw_input().split()] 
    if p == 1:
        #Calculate the index.
        index = (q ^ lastans) % n
        list_of_sequence[index].append(r)
    elif p == 2:
        index = index = (q ^ lastans) % n
        element_index = r % len(list_of_sequence[index])
        value = list_of_sequence[index][element_index]
        lastans = value   
        print value
