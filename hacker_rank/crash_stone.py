import heapq
def test(marks):
    diff = 0
    heapq._heapify_max(marks)
    while len(marks) > 1:
        popped_elm_1 = heapq._heappop_max(marks)
        popped_elm_2 = heapq._heappop_max(marks)
        diff = popped_elm_1 - popped_elm_2
        if diff > 0:
            marks.append(diff)
            heapq._heapify_max(marks)
            diff = 0
    final_elem = heapq._heappop_max(marks)
    result = final_elem - diff
    return result

def test2(marks):
    diff = 0
    marks = sorted(marks)
    while len(marks) > 1:
        popped_elm_1 = marks.pop()
        popped_elm_2 = marks.pop()
        diff = popped_elm_1 - popped_elm_2
        if diff > 0:
            marks.append(diff)
            marks = sorted(marks)
            diff = 0
    final_elem = marks.pop()
    result = final_elem - diff
    return result
print(test([969764608, 923288873, 884145908, 843435009, 842456591, 801915058, 792103686, 742976890, 717833291, 668431192, 624279391, 586679703, 586374055, 554066040, 553121267, 508221973, 459765367, 437034793, 410257930, 399188845, 393898202, 361066046, 339992587, 333998862, 292845117, 246993674, 199416087, 134274127, 85425451, 82956997, 46188086, 16561419]))
