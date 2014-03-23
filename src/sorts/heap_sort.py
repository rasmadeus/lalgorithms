# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="rasmadeus"
__date__ ="$Mar 13, 2014 8:01:52 PM$"

def _left(i):
    return ((i + 1) << 1) - 1

def _right(i):
    return _left(i) + 1

def _parent(i):
    return i >> 1

def _is_not_heap(array, n, i, child):
    return True if child < n and array[i] < array[child] else False

def is_heap(array, top):
    n = len(array)
    if n < 2:
        return True
    i = top
    while True:
        left = _left(i)
        right = _right(i)
        if left >= n and right >= n:
            break
        if _is_not_heap(array, n, i, left) or _is_not_heap(array, n, i, right):
            return False
        i += 1
    return True

def _do_heapify_step(array, size, top, child, n):
    if array[child] > array[top]:
        array[child], array[top] = array[top], array[child]
        _max_heapify(array, child, n)

def _max_heapify(array, top, n):    
    left = _left(top)
    right = _right(top)
    if left >= n and right >= n:
        return
    if left < n and right < n:
        _do_heapify_step(array, n, top, left if array[left] > array[right] else right, n)
    if left < n and right >= n:
        _do_heapify_step(array, n, top, left, n)
        return
    if left >=n and right < n:
       _do_heapify_step(array, n, top, right, n)
       return

def _build_max_heap(array, begin, n):
    for i in range((n >> 1) - 1, begin - 1, -1):
        _max_heapify(array, i, len(array))
   
def build_max_heap(array):
    _build_max_heap(array, 0, len(array))
    
def heap_sort(array):
    build_max_heap(array)
    for heap_size in range(len(array) - 1, -1, -1):
        array[heap_size], array[0] = array[0], array[heap_size]
        _max_heapify(array, 0, heap_size - 1)
        
class PriorityQueue:
    
    def __init__(self):
        self._data = []
        
    def getFirst(self):
        return self._data[0](1)
    
    def insert(self, key, value):
        pass
    
    def extractFirst(self):
        pass
    
    
        

