class BT: # node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def print_tree(t, level):
	if t == None:
		if level == 0:
			print("Tree is Empty")
			return
		else:
			return
	for i in range(level):
		print(" ", end = "")

	print(t.data)
	print_tree(t.left, level+1)
	print_tree(t.right, level+1)

def height(tree):
	if tree == None:
		return 0
	else:
		return (1 + max(height(tree.left), height(tree.right)))

if __name__ == '__main__':
	a = BT('A')
	b = BT('B')
	c = BT('C')
	d = BT('D')
	e = BT('E')
	f = BT('F')

	a.left = b
	b.left = c
	b.right = d
	c.left = e
	d.right = f

	print_tree(a, 0)
	print_tree(None, 0)

	print(height(None))
	print(height(a))
	print(height(c))
	print(height(b))
