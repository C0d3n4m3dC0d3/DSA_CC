'''
Two ways to traverse trees:
	1. DFS - Depth First Search - using Stack
	2. BFS - Breadth First Search - using Queue

Types of Tree Traversals:
	1. Inorder - LeftSelfRight
	2. Preorder - SelfLeftRight
	3. Postorder - LeftRightSelf

Construction of trees with traversal pattern:
pre+in = unique tree can be constructed
post+in = unique tree can be constructed
post+pre = unique tree cannot be constructed

Applications of Trees:
	1. Vision Tree Classifier
	2. Heirarchy
	3. Parse Tree

Binary Tree is like a tree
A node can have only two children
left child and right child are explicitly marked
can have either a left child, or a right child or both

Features of Trees:
	1. Root node does not have a parent
	2. All other nodes have only a single parent
	3. No cycles
'''

class TreeNode:
	def __init__(self, data):
		self.data = data
		self.children = []

	def add_child(self, child):
		self.children.append(child)

	def print(self, level):
		for i in range(level):
			print(' ', end='')
		print(self.data)
		for child in self.children:
			child.print(level+1)


def height(t):
	if t == None:
		return 0
	count = 0  #max height of child
	for child in t.children:
		count = max(count, height(child))
	return 1 + count

if __name__ == '__main__':
	a = TreeNode('A')
	b = TreeNode('B')
	c = TreeNode('C')
	d = TreeNode('D')
	e = TreeNode('E')
	f = TreeNode('F')
	g = TreeNode('G')

	a.add_child(b)
	a.add_child(c)
	a.add_child(d)
	c.add_child(e)
	d.add_child(f)
	d.add_child(g)

	print(height(None))
	print(height(a))
	print(height(c))
	print(height(b))
