# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import sorts.order_statistic as ost
from test_tools import *
import random

class  Test_order_statisticTestCase(unittest.TestCase):

    @unittest.skip("Test view for online debug")
    def test_view_partition_lomuto(self):
        for array in ([], [1], [1, 2], [2, 1], [1, 2, 3], [3, 2, 1], [3, 1, 2], [2, 1, 3]):
            print_separator()
            print_array(array)
            print(ost.partition_lomuto(array, 0, len(array)))
            print_array(array)
            
    def test_partition_lomuto_random(self):
        def test_one(array):
            n = len(array)
            middle = ost.partition_lomuto_randomized(array, 0, n)
            self.assertTrue(is_partition(array, 0, middle, n))
            self.assertFalse(middle == 0)
            self.assertFalse(middle == n)
        call_f_for_random_array(test_one)          
 
    def test_order_statistic(self):
        def test_one(array):
            n = len(array)
            i = random.randint(0, n - 1)
            found = ost.order_statistic(array, i)
            array.sort()
            truly = array[i]
            self.assertTrue(found == truly)
        call_f_for_random_array(test_one)
