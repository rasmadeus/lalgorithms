# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import sorts.heap_sort as hs
from tests.test_tools import *
from random import randint

class  TestHeapSort(unittest.TestCase):
 
    def test_index(self):
        series = ([0, 1, 2, 0], [1, 3, 4, 0], [2, 5, 6, 1])
        for values in series:
            self.assertEquals(hs._left(values[0]), values[1])
            self.assertEquals(hs._right(values[0]), values[2])
            self.assertEquals(hs._parent(values[0]), values[3])
 
    def test_is_heap(self):
        series = ([], [1], [3, 1], [5, 4, 3, 2, 1])
        for array in series:
            self.assertTrue(hs.is_heap(array, 0)) 
        self.assertFalse(hs.is_heap([1, 3], 0))
        
    def test_max_heapify(self):
        series = ([], [1], [1, 2], [0, 5, 4, 3, 2, 1])
        for array in series:
            hs._max_heapify(array, 0, len(array))
            self.assertTrue(hs.is_heap(array, 0))
    
    @unittest.skip("Test view for online debug")    
    def test_view_build_max_heap(self):
        array = create_random_array(-100, 100, 10)
        print_array(array)
        hs.build_max_heap(array)
        print_array(array)
        print(hs.is_heap(array, 0))
        
    def test_build_max_heapify(self):
        for _ in range(50):
            array = create_random_array(-100, 100, randint(50, 100))
            hs.build_max_heap(array)
            self.assertTrue(hs.is_heap(array, 0))
        
    def test_heap_sort(self):
        test_random_sort(hs.heap_sort)