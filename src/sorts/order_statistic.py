# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="rasmadeus"
__date__ ="$Mar 17, 2014 9:50:49 PM$"

def partition_lomuto(array, begin, end):
    if end - begin < 2:
        return begin
    last = end - 1
    if end - begin < 3:
        if array[begin] > array[last]:
            array[begin], array[last] = array[last], array[begin]
        return last
    end_left = begin
    for i in range(begin, end - 1):
        if array[i] <= array[last]:
            array[end_left], array[i] = array[i], array[end_left]
            end_left += 1
    array[end_left], array[last] = array[last], array[end_left]
    return end_left if end_left == last else end_left + 1
    
     
from random import randint
def partition_lomuto_randomized(array, begin, end):
    last = end - 1
    i_random = randint(begin, last)
    array[i_random], array[last] = array[last], array[i_random]
    return partition_lomuto(array, begin, end)

def _order_statistic(array, begin, end, i):
    if end - begin == 1:
        return array[begin]
    middle = partition_lomuto_randomized(array, begin, end)
    if i < middle:
        return _order_statistic(array, begin, middle, i)
    else:
        return _order_statistic(array, middle, end, i)

def order_statistic(array, i):
    return _order_statistic(array, 0, len(array), i)
    
    