class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


# Level order traversal
def print_level_order_traversal(root):
	if root:
		# create a queue
		queue = list()
		# enqueue the root
		queue.append(root)

		while queue:
			# print the first element in the queue and then remove it
			print(queue[0].data, end=' ')
			node = queue.pop(0)

			# enqueue left child
			if node.left is not None:
				queue.append(node.left)

			# enqueue right child
			if node.right is not None:
				queue.append(node.right)


# In-order traversal
def print_in_order_traversal(root):
	if root:
		# recursively look for the left child
		print_in_order_traversal(root.left)
		# then print the data on the node
		print(root.data, end=' ')
		# then recursively look for the right child
		print_in_order_traversal(root.right)


# Pre-order traversal
def print_pre_order_traversal(root):
	if root:
		# print the data of the node
		print(root.data, end=' ')
		# then recursively look for the left child
		print_pre_order_traversal(root.left)
		# then recursively look for the right child
		print_pre_order_traversal(root.right)


# Post-order traversal
def print_post_order_traversal(root):
	if root:
		# first recursively look for the left child
		print_post_order_traversal(root.left)
		# then recursively look for the right child
		print_post_order_traversal(root.right)
		# then print the data of the node
		print(root.data, end=' ')


# testing
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal:")
print_level_order_traversal(root)
print()

print("In-Order Traversal:")
print_in_order_traversal(root)
print()

print("Pre-Order Traversal:")
print_pre_order_traversal(root)
print()

print("Post-Order Traversal:")
print_post_order_traversal(root)
print()
