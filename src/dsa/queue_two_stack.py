class QueueTwoStack:
	def __init__(self):
		self._in = []
		self._out = []

	def __len__(self):
		return len(self._in) + len(self._out)

	def enqueue(self, value):
		self._in.append(value)

	def _move_in_to_out(self):
		while self._in:
			self._out.append(self._in.pop())

	def dequeue(self):
		if not self._out:
			self._move_in_to_out()
		if not self._out:
			raise IndexError("dequeue from empty queue")
		return self._out.pop()

	def peek(self):
		if not self._out:
			self._move_in_to_out()
		if not self._out:
			raise IndexError("peek from empty queue")
		return self._out[-1]

