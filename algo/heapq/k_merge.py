import heapq
from collections import deque


def k_merge(lists):
    queues = [queue for queue in map(deque, lists)]

    heap = []
    for i, lst in enumerate(queues):
        heap.append((lst.popleft(), i))

    heapq.heapify(heap)

    result = []
    while heap:
        value, index = heapq.heappop(heap)
        result.append(value)
        print(value, '  ===  ', index)
        if queues[index]:
            heapq.heappush(heap, (queues[index].popleft(), index))

    return result


print(k_merge([[8, 10, 12], [4, 5, 9], [2, 11]]))
