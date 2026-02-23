from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

@dataclass
class ListNode:
	val:int
	next: ListNode | None = None

def from_list(values: Iterable[int]) -> ListNode | None:
	head: ListNode | None = None
	tail: ListNode | None = None

	for x in values:
		node = ListNode(x)
		if head is None:
			head = node
			tail = node
		else:
			assert tail is not None
			tail.next = node
			tail = node

	return head

def to_list(head: ListNode | None) -> list[int]:
	out: list[int] = []
	cur = head
	while cur is not None:
		out.append(cur.val)
		cur = cur.next
	return out

def reverse_list(head: ListNode | None) -> ListNode | None:
	prev: ListNode | None = None
	cur = head

	while cur is not None:
		nxt = cur.next
		cur.next = prev
		prev = cur
		cur = nxt

	return prev

def has_cycle(head: ListNode | None) -> bool:
	slow = head
	fast = head

	while fast is not None and fast.next is not None:
		slow = slow.next
		fast = fast.next.next
		if slow is fast:
			return True
	return False
