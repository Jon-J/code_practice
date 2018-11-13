import heapq 
def MM2(N):
    m = []
    A1 = None #Type of Command 
    A2 = None #Number to be Pushed to Stack
    m2 = []
    for i in range(N):
        try:
            inn = input()
        except:
            inn = inn 
        if len(inn) > 1:
            A1 = int(inn.split()[0])
            A2 = int(inn.split()[1])
        else:
            A1 = int(inn)
        if A1 == 1:
            m.append(A2) # pushing to stack
            heapq.heappush(m2,-A2) # pushing to Priority Queue (the - to get the greatest value)
            print(m2)
        if A1 == 2:
            A2 = m.pop()
            if A2 == -m2[0]:# if value to be popped from stack is the largest value remove it from PQ
                print(-m2[0])
                heapq.heappop(m2)
            else:
                m2.remove(-A2)
                heapq.heapify(m2)
        if A1 == 3:
            #pass
            print(-m2[0])
        #print (m2)
 
        
N = int(input())
MM2(N)
