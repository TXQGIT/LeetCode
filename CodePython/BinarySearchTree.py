#!/usr/bin/env python

class BST(object):
	def __init__(self,k=None, p=None, l=None, r=None):
		self.key = k 
		self.parent = p
		self.left = l
		self.right = r

	def inorder_tree_walk(self, root):
		if root!=None:
			self.inorder_tree_walk(root.left)
			print(root.key, end=',')
			self.inorder_tree_walk(root.right)

	def tree_search(self, root, k):
		if root==None or root.key==k:
			return root
		if k<root.key:
			return self.tree_search(root.left, k)
		else:
			return self.tree_search(root.right, k)

	def tree_minimum(self, root):
		if root.left!=None:
			root = root.left
		return root

	def tree_maximum(self, root):
		if root.right!=None:
			root = root.right
		return root

	def tree_successor(self, node):
		if node.right!=None:  #case 1
			return self.tree_minimum(node.right)
		p = node.parent       #case 2
		while p!=None and node==p.right:
			node = p
			p = p.parent
		return p

	def tree_predecessor(self, node):
		if node.left!=None:  #case 1
			return self.tree_maximum(node.left)
		p = node.parent      #case 2
		if p!=None and node==p.left:
			node = p
			p = p.parent
		return p

	def tree_insert_recursion(self, root, node):
		if root==None:
			root = node
			return
		if node.key<=root.key:
			if root.left!=None:
				self.tree_insert_recursion(root.left, node)
			else:
				node.parent = root
				root.left = node
		else:
			if root.right!=None:
				self.tree_insert_recursion(root.right, node)
			else:
				node.parent = root
				root.right = node

	def tree_insert_iteration(self, root, node):
		if root==None:
			root = node
			return
		while root!=None:
			p = root
			if node.key<=root.key:
				root = root.left
			else:
				root = root.right
		node.parent = p
		if node.key<=p.key:
			p.left = node
		else:
			p.right = node

	def tree_delete(self, root, node):
		if node.left==None and node.right==None: #case1: node without children
			if node==node.parent.left:
				node.parent.left = None
			else:
				node.parent.right = None
			node.parent = None
			return

		if node.left == None: #case2.1: node without left child
			if node == node.parent.left:
				node.parent.left = node.right
			else:
				node.parent.right = node.right
			node.right.parent = node.parent
			node.parent = None
			node.right = None
			return

		if node.right==None: #case2.2: node without right child
			if node==node.parent.left:
				node.parent.left = node.left
			else:
				node.parent.right = node.left
			node.left.parent = node.parent
			node.parent = None
			node.left = None
			return

		#case3: node with left and right children
		#in this case, 
		#   the successor of node without left child
		#   the predecessor of node without right child
		node_successor = node.tree_successor(node)
		if node_successor==node_successor.parent.left:
			node_successor.parent.left = node_successor.right
		else:
			node_successor.parent.right = node_successor.right
		node.key = node_successor.key
		node_successor = None
		return


def init_BST():
	            #           15
	            #      6         18
	            #   3     7   17    20
	            # 2   4 /   13
	            #         9    /
	root = BST(15)
	node_6 = BST(6)
	node_3 = BST(3)
	node_2 = BST(2)
	root.left = node_6
	node_6.parent = root

	node_6.left = node_3
	node_3.parent = node_6

	node_3.left = node_2
	node_2.parent = node_3 

	root.tree_insert_recursion(root,BST(4))
	root.tree_insert_recursion(root,BST(7))
	root.tree_insert_recursion(root,BST(13))
	root.tree_insert_recursion(root,BST(9))

	root.tree_insert_iteration(root,BST(18))
	root.tree_insert_iteration(root,BST(17))
	root.tree_insert_iteration(root,BST(20))

	return root

if __name__=='__main__':

	root = init_BST()

	root.inorder_tree_walk(root)
	print('')

	LastNode = Convert2List(root)

	print(root.tree_successor(root.tree_search(root, 13)).key)
	print(root.tree_predecessor(root.tree_search(root, 9)).key)

	root.tree_delete(root, root.tree_search(root, 7))
	root.tree_delete(root, root.tree_search(root, 6))
	print('end')

	path = FindPath(root, 50)