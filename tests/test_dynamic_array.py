import pytest
from src.dynamic_array import DynamicArray

def test_append_and_len():
	arr = DynamicArray(initial_capacity=2)
	assert len(arr) == 0
	arr.append(10)
	arr.append(20)
	assert len(arr) == 2
	assert arr.get(0) == 10
	assert arr.get(1) == 20

def test_resize_doubles_capacity():
	arr = DynamicArray(initial_capacity = 2)
	assert arr.capacity() == 2
	arr.append(1)
	arr.append(2)
	arr.append(3) # triggers resize to 4
	assert len(arr) == 3
	assert arr.capacity() == 4
	assert [arr.get(i) for i in range(len(arr))] == [1, 2, 3]

def test_set_updates_value():
	arr = DynamicArray()
	arr.append("a")
	arr.append("b")
	arr.set(1, "z")
	assert arr.get(1) == "z"

def test_get_out_of_range_raises():
	arr = DynamicArray()
	with pytest.raises(IndexError):
		arr.get(0)
	arr.append(1)
	with pytest.raises(IndexError):
		arr.get(1)
	with pytest.raises(IndexError):
		arr.get(-1)

def test_set_out_of_range_raises():
	arr = DynamicArray()
	with pytest.raises(IndexError):
		arr.set(0,99)
