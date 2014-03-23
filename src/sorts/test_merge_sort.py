# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="rasmadeus"
__date__ ="$Mar 9, 2014 3:12:53 PM$"

import unittest
import sorts.merge_sort as ms
from test_tools import *

class TestMergeSort(unittest.TestCase):
    
    @unittest.skip("Test view for online debug")
    def test_view_merge(self):
        array = [2, 1]
        print_separator()
        ms._merge(array, 0, 1, len(array))
        print('Merged', end=': ')
        print_array(array)
    
    @unittest.skip("Test view for online debug")
    def test_view_merge_sort(self):
        array = [3, 4, 1, -2, 1, 5, -1, 4, 9, 0]
        ms.merge_sort(array)
        print('Sorted', end=': ')
        print_array(array)
    
    def test_random_merge_sort(self):
        self.assertTrue(test_random_sort(ms.merge_sort))