# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import sorts.counting_sort as cs
from test_tools import *

class  TestCountingSort(unittest.TestCase):

    def test_counting_sort(self):
        for item in (([], 0), ([1], 2), ([2, 1, 0, 1], 3), ([9, 8, 8, 4, 9, 2, 1, 0], 10)):     
            self.assertTrue(is_sorted(cs.counting_sort(item[0], item[1])))


