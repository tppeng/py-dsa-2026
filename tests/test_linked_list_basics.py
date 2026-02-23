import pytest

from dsa.linked_list import ListNode, from_list, to_list

def test_from_list_empty():
	assert from_list([]) is None

def test_from_list_single():
	head = from_list([1])
	assert isinstance(head, ListNode)
	assert head.val == 1
	assert head.next is None

def test_round_trip():
	head = from_list([1, 2, 3])
	assert to_list(head) == [1, 2, 3]

def test_to_list_none():
	assert to_list(None) == []
