import heapq
def test(k, marks):
    heapq._heapify_max(marks)
    list2 = []
    cutt_off = k
    n = len(marks)
    prev_rank = 0
    prev_ranked_ppl = 0
    count_ppl = 0
    prev_mark = -1
    for i in range(n):
        popped_elm = heapq._heappop_max(marks)
        if prev_mark < 0:
            prev_mark = popped_elm
            prev_rank += 1

        if popped_elm != prev_mark:
            prev_rank += prev_ranked_ppl
            prev_ranked_ppl = 0
            prev_mark = popped_elm

        if cutt_off < prev_rank:
            break

        count_ppl += 1
        prev_ranked_ppl += 1
    return count_ppl

print(test(4, [2,2,3,4,5]))
