import pytest

from dsa.linked_list import from_list, to_list, reverse_list

def test_reverse_empty():
	assert reverse_list(None) is None

def test_reverse_single():
	head = from_list([1])
	assert to_list(reverse_list(head)) == [1]

def test_reverse_multiple():
	head = from_list([1, 2, 3, 4])
	assert to_list(reverse_list(head)) == [4, 3, 2, 1]
