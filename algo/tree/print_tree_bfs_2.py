from collections import deque
class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def traverse(rootnode):
  que = deque()
  que.append(rootnode)
  que.append("Next")
  x = ""
  while que:
    node = que.popleft()
    if node == "Next":
      print(x)
      if not que:
        que.append("Next")
      continue
    x = x+" "+str(node.value)
    print("test ", node.value)
    if node.left: que.append(node.left)
    if node.right: que.append(node.right)

t = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))

traverse(t)
