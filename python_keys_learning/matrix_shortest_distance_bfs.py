matrix = []
n = int(input())
for i in range(n):
    lt = list(map(int, input().split()))
    matrix.append(lt)
from pprint import pprint
import copy
pprint(matrix)
m = len(matrix[0])
false_matrix = []
for i in range(len(matrix)):
    row_mat_temp = []
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            row_mat_temp.append(True)
        if matrix[i][j] == 1:
            row_mat_temp.append(False)
    false_matrix.append(row_mat_temp)
src = list(map(int, input().split()))
dst = list(map(int, input().split()))
src.append(0)
queue = []
queue.append(src)
false_matrix[src[0]][src[1]] = True
def BFS(queue, dst, false_matrix):
    
    while queue:
        #import pdb;pdb.set_trace()
        front = queue[0]
        queue.pop(0)   
        if front[0] == dst[0] and front[1] == dst[1]:
            return front[2]
        if front[0] + 1 < n and false_matrix[front[0] + 1][front[1]] == False:
            queue.append([front[0] + 1, front[1], front[2] + 1])
            false_matrix[front[0] + 1][front[1]] = True
        if front[1] + 1 < m and false_matrix[front[0]][front[1] + 1] == False:
            queue.append([front[0], front[1] + 1, front[2] + 1])
            false_matrix[front[0]][front[1] + 1] = True
        if front[0] - 1 > -1 and false_matrix[front[0] - 1][front[1]] == False:
            queue.append([front[0] - 1, front[1], front[2] + 1])
            false_matrix[front[0] - 1][front[1]] = True
        if front[1] - 1 > -1 and false_matrix[front[0]][front[1] - 1] == False:
            queue.append([front[0], front[1] - 1, front[2] + 1])
            false_matrix[front[0]][front[1] - 1] = True
print(BFS(queue, dst, false_matrix))
