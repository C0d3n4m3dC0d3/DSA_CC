class ArrayQueue:
	def __init__(self, max_size):
		self.__arr = [None]*max_size
		self.__max_size = max_size
		self.__head = 0
		self.__tail = 0

	def enqueue(self, data):
		if self.__tail == self.__max_size:
			raise Exception("Queue Full!")
		self.__arr[self.__tail] = data
		self.__tail += 1

	def dequeue(self):
		if self.__head == self.__tail:
			raise Exception("Queue Empty!!")
		ret = self.__arr[self.__head]
		self.__head += 1
		return ret

	def is_empty(self):
		return self.__head == self.__tail

	

if __name__ == '__main__':
	queue = ArrayQueue(5)
	for i in range(3):
		queue.enqueue(chr(ord('A')+i))
	print(queue.dequeue())
	print(queue.dequeue())
	for i in range(4, 7):
		try:
			queue.enqueue(chr(ord('A')+i))
		except:
