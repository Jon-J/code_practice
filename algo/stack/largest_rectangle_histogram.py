from stack_impl import Stack

def find_max_rect_histogram(histogram):
    max_area = 0
    stack = Stack()
    index = 0

    while index < len(histogram):
        if stack.is_empty() or histogram[index] >= histogram[stack.peek()]:
            stack.push(index)
            index += 1
        else:
            top_stack = stack.pop()

            area = histogram[top_stack] * ((index - stack.peek() - 1) if not stack.is_empty() else index)

            max_area = max(area, max_area)

    while not stack.is_empty():
        top_stack = stack.pop()

        area = histogram[top_stack] * ((index - stack.peek() - 1) if not stack.is_empty() else index)
        max_area = max(max_area, area)

    return max_area

A = [6, 2, 5, 4, 5, 1, 6]
print("largestRectangleArea: ", find_max_rect_histogram(A))
A = [3, 2, 5, 6, 1, 2]
print("largestRectangleArea: ", find_max_rect_histogram(A))
