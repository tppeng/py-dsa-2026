from __future__ import annotations
import ctypes
from typing import Any

class DynamicArray:
    def __init__(self, initial_capacity: int = 4) -> None:
        if initial_capacity < 1:
            raise ValueError("initial_capacity must be >= 1")
        self._capacity = initial_capacity 
        self._size = 0
        self._data = self._make_array(self._capacity)

    def __len__(self) -> int:
            return self._size

    def capacity(self) -> int:
            return self._capacity
        
    def append(self, value: Any) -> None:
        if self._size == self._capacity: 
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1
        
    def get(self, index: int) -> Any:
        self._check_index(index)
        return self._data[index]
        
    def set(self, index: int, value: Any) -> None:
        self._check_index(index)
        self._data[index] = value
        
    def _check_index(self, index: int) -> None:
        if index <0 or index >= self._size:
            raise IndexError("index out of range")
        
    def _resize(self, new_capacity: int) -> None:
        new_data = self._make_array(new_capacity)
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity
        
    @staticmethod
    def _make_array(capacity: int):
        return (ctypes.py_object * capacity)()

    def __repr__(self) -> str:
        items = ", ".join(repr(self._data[i]) for i in range(self.size))
        return f"DynamicArray([{items}]) size = {self._size} capacity = {self._capacity}"
