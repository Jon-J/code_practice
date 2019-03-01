def test(k, marks):
    marks = sorted(marks)
    cutt_off = k
    n = len(marks)
    prev_rank = 0
    prev_ranked_ppl = 0
    count_ppl = 0
    prev_mark = -1
    for i in range(n):
        popped_elm = marks.pop()
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

print(test(4, [1,2,3,4,5]))
