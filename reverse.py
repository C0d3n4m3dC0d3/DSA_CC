#Reverse a linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class SinglyLinkedList:
	def __init__(self, head):
		self.head = head

	def print_list(self):
		if self.head == None:
			print("Empty List!")
		else:
			temp = self.head
			while temp != None:
				print(temp.data, end=' ')
			 	temp = temp.next
			print()

	def reverse_sll(self):
		curr = self.head
		prev = None
		while current != None:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		self.head = prev
	 	return self

#Normal Case - more than n nodes in the list
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

sll = SinglyLinkedList(a)
sll = sll.reverse_sll()
sll.print_list()

a = None
sll = SinglyLinkedList(a)
sll = sll.reverse_sll()
sll.print_list()

a = Node('A')
sll = SinglyLinkedList(a)
sll = sll.reverse_sll()
sll.print_list()
