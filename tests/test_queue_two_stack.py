import pytest
from dsa.queue_two_stack import QueueTwoStack

def test_enqueue_dequeue_fifo():
	q = QueueTwoStack()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)

	assert len(q) == 3
	assert q.dequeue() == 1
	assert q.dequeue() == 2
	assert q.dequeue() == 3
	assert len(q) == 0

def test_peek_does_not_remove():
	q = QueueTwoStack()
	q.enqueue("a")
	q.enqueue("b")

	assert q.peek() == "a"
	assert len(q) == 2
	assert q.dequeue() == "a"
	assert q.peek() == "b"
	assert len(q) == 1

def test_dequeue_empty_raises():
	q = QueueTwoStack()
	with pytest.raises(IndexError):
		q.dequeue()

def test_peek_empty_raises():
	q = QueueTwoStack()
	with pytest.raises(IndexError):
		q.peek()

def test_interleaved_operations():
	q = QueueTwoStack()
	q.enqueue(1)
	q.enqueue(2)
	assert q.dequeue() == 1
	q.enqueue(3)
	assert q.dequeue() == 2
	assert q.dequeue() == 3
