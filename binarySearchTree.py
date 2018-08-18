# BST Implementation

# each node in a tree has its value and a left and right subtree
class Node():
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	# get value of a node
	def get(self):
		return self.value

	# set value of a node
	def set(self, value):
		self.value = value


'''
Tests
>>> a = Node(5)
>>> a.value
5
>>> a.set(7)
>>> a.get()
7
'''

class BST():
	def __init__(self):
		self.root = None
	
	def setRoot(self, value):
		""" Set root for BST.

		Arguments:
		value -- data for the root
		
		
		>>> b = BST()
		>>> b.setRoot(5)
		>>> b.root()
		<__main__.Node object at 0x0000024A7DE162E8>
		>>> b.root.value
		5
		"""
		self.root = Node(value)


	def insert(self, value):
		""" Call function to insert node with data value.

		Arguments:
		value -- data for the node

		>>> b = BST()
		>>> b.setRoot(5)
		>>> b.root.value
		5
		>>> b.insert(10)
		>>> b.insert(3)
		>>> b.root.right.value
		10
		>>> b.root.left.value
		3

		This function is a helper function to the insertNode function.
		"""
		# if root is none, create a root
		if self.root is None:
			return self.setRoot(value)
		else:
			# insert a new node with value
			return self.insertNode(self.root, value)


	def insertNode(self, currentNode, value):
		""" Insert node with value following BST implementation

		arguments:
		currentNode - node which BST object is currently referring to
		value - data for node

		This function is called by the helper function insert
		"""

		# check if value is lower than or equal to value of current node
		if value <= currentNode.value:

			# the node is occupied so we traverse left down the tree
			if currentNode.left is not None:  
				# recursive call to insertNode
				# we call self because we want to refer to the same object and to retain all of its data so far	
				self.insertNode(currentNode.left, value) 
			else:
				# node is not occupied, we can insert on the left side of the current node
				currentNode.left = Node(value)     
		
		# check if value is greater than value of current node
		elif value > currentNode.value:

			# the right node is occupied so we traverse right down the tree
			if currentNode.right is not None:
				# recursive call to insertNode
				self.insertNode(currentNode.right, value) 

			# node is not occupied, so we can insert on the right side of the current node	
			else:
				currentNode.right = Node(value) 
		
	def search(self, value):
		""" Call function to search for node with specified value

		arguments:
		value - data for node
		
		>>> b = BST()
		>>> b.search(20)
		False
		>>> b.setRoot(20)
		>>> b.insert(15)
		>>> b.insert(30)
		>>> b.insert(7)
		>>> b.insert(23)
		>>> b.search(15)
		True
		>>> b.insert(23)
		True
		>>> b.insert(6)
		False
		>>> b.insert(27)
		False
		
		This function is a helper function to the searchNode function.
		"""

		# if root is empty, return
		if self.root is None: 
			return False

		# root is not empty, call searchNode function	
		else:
			return self.searchNode(self.root, value)

	
	def searchNode(self, currentNode, value):
		""" Return boolean if there is node with value in BST.

		arguments:
		currentNode - node which BST object is currently referring to 
		value - data for node

		This function uses the helper function search.
		"""

		# base case - recurse up to this 
		if currentNode is None:
			return False

		# if we found the value, return True
		elif value == currentNode.value: 
			return True

		# if value is less than the value of the current node, go down the left subtree of the current node
		elif value <= currentNode.value: 
			return self.searchNode(currentNode.left, value)

		# if value is greater than the value of the current node, go down the right subtree of the current node	
		elif value > currentNode.value:
			return self.searchNode(currentNode.right, value) 


	# delete function incomplete
	# need to write more tests
	def delete(self, value):

		# if root is empty, return
		if self.root is None: 
			return

		# root is not empty, call deleteNode	
		else:
			return self.deleteNode(self.root, value)

	
	def deleteNode(self, currentNode, value):
		
		# base case - recurse up to this 
		if currentNode is None:
			return 

		# check if value is less or equal to the value of current node
		# if it is, go down left subtree
		# in other words, make a recursive call to left subtree
		elif value <= currentNode.value:
			self.deleteNode(currentNode.left, value) 

		# check if value is greater than the value of current node
		# if it is, go down right subtree
		# in other words, make a recursive call to right subtree
		elif value > currentNode.value:
			self.deleteNode(currentNode.right, value) 

		# 3 cases: leaf node, node with one child, node with two child	
		else:
			# node is a leaf
			# delete node by setting equal to None
			if currentNode.left is None and currentNode.right is None:
				currentNode.value = None

			# node has no left child
			# set right child of parent node as right child of currentNode
			# delete right child of currentNode
			elif currentNode.left is None:
				self.root.right = currentNode.right
				currentNode.right = None

			# node has no right child
			# set left child of parent node as left child of currentNode
			# delete left child of currentNode
			elif currentNode.right is None:
				self.root.left = currentNode.left
				currentNode.left = None

			# node has both left child and right child	
			# find minimum of right subtree and set as value of current node
			# delete original right child of right subtree
			else:
				minRightSubtree = self.min()
				currentNode.value = minRightSubtree
				currentNode.right = self.deleteNode(currentNode.right, value)
				
	
	def height(self):
		""" Call function getHeight to return height of BST

		>>> b = BST()
		>>> b.height()
		-1
		>>> b.setRoot(20)
		>>> b.root.value
		20
		>>> b.height()
		0
		>>> b.insert(25)
		>>> b.height()
		1
		>>> b.insert(30)
		>>> b.height()
		2
		>>> b.insert(15)
		2

		This function is a helper function to the getHeight function.
		"""
		return self.getHeight(self.root)

	
	def getHeight(self, currentNode): 
		""" Return height of BST

		arguments:
		currentNode - node which BST object is currently referring to 

		This function is called by helper function height.
		"""

		# base case
		# assume any empty tree has height of -1
		if currentNode is None:  
			return -1

		# recursive calls: we want to recurse down both the left and right subtrees
		# and because we want the height of the tree, we take the maximum height from the left and right subtrees
		# intution: every time we move down one level of the tree, we add 1 to the total height
		else:
			return 1 + max(self.getHeight(currentNode.left), self.getHeight(currentNode.right))
	
	
	def min(self):
		""" Call function findMin to return minimum value in BST.
		
		>>> b = BST()
		>>> b.setRoot(20)
		>>> b.root.value
		20
		>>> b.insert(15)
		>>> b.insert(25)
		>>> b.insert(7)
		>>> b.insert(30)
		>>> b.min()
		7
		>>> b.max()
		30

		This function is a helper function to the findMin function.
		"""
		return self.findMin(self.root)

	
	def findMin(self, currentNode):
		""" Return minimum value in BST

		arguments:
		currentNode - node which BST object is currently referring to 

		This function is called by helper function min.
		"""
		
		# base case
		# if we cannot go any further left, 
		# the value of the current node must be the minimum
		if currentNode.left is None:
			return currentNode.value
		else:
			return self.findMin(currentNode.left)

	
	def max(self):
		""" Call function findMax to return maximum value in BST.
		
		>>> b = BST()
		>>> b.setRoot(20)
		>>> b.root.value
		20
		>>> b.insert(15)
		>>> b.insert(25)
		>>> b.insert(7)
		>>> b.insert(30)
		>>> b.min()
		7
		>>> b.max()
		30

		This function is a helper function to the findMin function.
		"""
		return self.findMax(self.root)

	
	def findMax(self, currentNode):
		""" Return maximum value in BST

		arguments:
		currentNode - node which BST object is currently referring to 

		This function is called by helper function max.
		"""

		# base case
		# if we cannot go any further right, 
		# the value of the current node must be the maximum
		if currentNode.right is None:
			return currentNode.value
		else:
			return self.findMax(currentNode.right)	






