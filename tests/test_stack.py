import pytest
from src.stack import Stack

def test_push_and_pop_lifo():
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)

	assert len(s) == 3
	assert s.pop() == 3
	assert s.pop() == 2
	assert s.pop() == 1
	assert len(s) == 0

def test_peek_does_not_remove():
	s = Stack()
	s.push("a")
	s.push("b")

	assert s.peek() == "b"
	assert len(s) == 2
	assert s.pop() == "b"
	assert len(s) == 1

def test_pop_empty_raises():
	s = Stack()
	with pytest.raises(IndexError):
		s.pop()

def test_peek_empty_raises():
	s = Stack()
	with pytest.raises(IndexError):
		s.peek()

def test_len_updates_correctly():
	s = Stack()
	assert len(s) == 0

	s.push(10)
	assert len(s) == 1

	s.push(20)
	assert len(s) == 2
	
	s.pop()
	assert len(s) == 1

