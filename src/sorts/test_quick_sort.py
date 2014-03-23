# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sorts.quick_sort as qs
from test_tools import *
import unittest

class TestQuickSort(unittest.TestCase):
    
    def test_middle_border(self):
        for data in [(5, 0, 10), (8, 6, 10), (0, 0, 1), (1, 0, 2), (4, 3, 5)]:
            self.assertEquals(data[0], qs._middle_border(data[1], data[2]));
    
    @unittest.skip("Test view for online debug")        
    def test_view_partition_lomuto(self):
        for array in ([0, 1], [1, 0], [1, 1], [1, 1, 1], [2, 0, 1], [1, 3, 2], [1, 3, 2, 0]):
            print_separator()
            print('Border: ', qs._middle_border(0, len(array)))
            print_prefix('Sourse:')
            print_array(array)
            print('End part one: ', qs._partition_lomuto(array, 0, len(array), qs._middle_border))
            print_prefix('Partition array:')
            print_array(array)
            
    @unittest.skip("Test view for online debug")         
    def test_view_quick_sort_with_middle_border(self):
        array = [3, 2, 1, -6, 0 ,8, -5]
        print_separator()
        print_prefix('Source:')
        print_array(array)
        qs.quick_sort_with_middle_border(array)
        print_prefix('Sorted:')
        print_array(array)
    
    @unittest.skip("Test view for online debug")       
    def test_sorts_in_time(self):
        sort_in_time(qs.quick_sort_with_middle_border, qs.quick_sort_with_random_border, 'Middle border', 'Random border')
        
    def test_quick_sort_with_middle_border(self):
        self.assertTrue(test_random_sort(qs.quick_sort_with_middle_border))
        self.assertTrue(test_random_sort(qs.quick_sort_with_random_border))