from dsa.linked_list import ListNode, has_cycle

def test_has_cycle_none():
	assert has_cycle(None) is False

def test_has_cycle_single_no_cycle():
	a= ListNode(1)
	assert has_cycle(a) is False

def test_has_cycle_single_cycle():
	a = ListNode(1)
	a.next = a
	assert has_cycle(a) is True

def test_has_cycle_multi_no_cycle():
	a = ListNode(1)
	b = ListNode(2)
	c = ListNode(3)
	a. next = b
	b. next = c
	assert has_cycle(a) is False

def test_has_cycle_multi_cycle():
	a = ListNode(1)
	b = ListNode(2)
	c = ListNode(3)
	d = ListNode(4)
	a.next = b
	b.next = c
	c.next = d
	d.next = b #cycle back to b
	assert has_cycle(a) is True
