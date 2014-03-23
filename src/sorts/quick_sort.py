# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="rasmadeus"
__date__ ="$Mar 4, 2014 10:22:03 PM$"

def _middle_border(begin, end):
    return begin + int((end - begin) / 2)

from random import randint
def _random_border(begin, end):
    return randint(begin, end - 1)

def _partition_lomuto(array, begin, end, f_border):
    i_border = f_border(begin, end)
    item = array[i_border]
    end_part_one = begin
    for i in range(begin, end):
        if array[i] < item:
            array[i], array[end_part_one] = array[end_part_one], array[i]
            end_part_one += 1
    if end_part_one == begin:
        array[i_border], array[begin] = array[begin], array[i_border]
        end_part_one += 1
    return end_part_one

def _quick_sort(array, begin, end, f_border):
    if end - begin < 2:
        return
    end_part_one = _partition_lomuto(array, begin, end, f_border)
    if end_part_one - begin > 1:
        _quick_sort(array, begin, end_part_one, f_border)
    if end - end_part_one > 1:
        _quick_sort(array, end_part_one, end, f_border)
    
def _quick_sort_for_whole_array(array, f_border):
    _quick_sort(array, 0, len(array), f_border)
         
def quick_sort_with_middle_border(array):
    _quick_sort_for_whole_array(array, _middle_border)
    
def quick_sort_with_random_border(array):
    _quick_sort_for_whole_array(array, _random_border)
        
    

