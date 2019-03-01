# Python 3 program to find k'th 
# largest element in BST 

# A BST node 
class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.key = data 
		self.left = None
		self.right = None

# A function to find 
def KSmallestUsingMorris(root, k): 
	
	# Count to iterate over elements 
	# till we get the kth smallest number 
	count = 0

	ksmall = -9999999999 # store the Kth smallest 
	curr = root # to store the current node 

	while curr != None: 
		
		# Like Morris traversal if current does 
		# not have left child rather than 
		# printing as we did in inorder, we 
		# will just increment the count as the 
		# number will be in an increasing order 
		if curr.left == None: 
			count += 1

			# if count is equal to K then we 
			# found the kth smallest, so store 
			# it in ksmall 
			if count == k: 
				ksmall = curr.key 

			# go to current's right child 
			curr = curr.right 
		else: 
			
			# we create links to Inorder Successor 
			# and count using these links 
			pre = curr.left 
			while (pre.right != None and
				pre.right != curr): 
				pre = pre.right 

			# building links 
			if pre.right == None: 
				
				# link made to Inorder Successor 
				pre.right = curr 
				curr = curr.left 

			# While breaking the links in so made 
			# temporary threaded tree we will check 
			# for the K smallest condition 
			else: 
				
				# Revert the changes made in if part 
				# (break link from the Inorder Successor) 
				pre.right = None

				count += 1

				# If count is equal to K then we 
				# found the kth smallest and so 
				# store it in ksmall 
				if count == k: 
					ksmall = curr.key 
		
				curr = curr.right 
	return ksmall # return the found value 

# A utility function to insert a new 
# node with given key in BST 
def insert(node, key): 
	
	# If the tree is empty, 
	# return a new node 
	if node == None: 
		return Node(key) 

	# Otherwise, recur down the tree 
	if key < node.key: 
		node.left = insert(node.left, key) 
	elif key > node.key: 
		node.right = insert(node.right, key) 

	# return the (unchanged) node pointer 
	return node 

# Driver Code 
if __name__ == '__main__': 
	
	# Let us create following BST 
	#	 50 
	#	 / \ 
	#	 30 70 
	# / \ / \ 
	# 20 40 60 80 
	root = None
	root = insert(root, 50) 
	insert(root, 30) 
	insert(root, 20) 
	insert(root, 40) 
	insert(root, 70) 
	insert(root, 60) 
	insert(root, 80) 

	for k in range(1,8): 
		print(KSmallestUsingMorris(root, k), 
								end = " ") 

# This code is contributed by PranchalK 

