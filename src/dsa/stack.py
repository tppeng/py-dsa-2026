from dsa.dynamic_array import DynamicArray

class Stack:
	def __init__(self):
		self._data = DynamicArray()
	
	def push(self, value):
		self._data.append(value)

	def pop(self):
		if len(self._data) == 0:
			raise IndexError("pop from empty stack")
		return self._data.pop()

	def peek(self):
		if len(self._data) == 0:
			raise IndexError("peek from empty stack")
		return self._data.get(len(self._data) -1)

	def __len__(self):
		return len(self._data)

