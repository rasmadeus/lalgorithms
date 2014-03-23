# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="rasmadeus"
__date__ ="$Mar 1, 2014 5:20:02 PM$"

from time import time
def how_long(comment, f, *args):
    begin = time()
    f_res = f(*args)
    end = time()
    print('Finish execute ' + comment + ' in {}'.format(end - begin))
    return f_res    
    
from random import randint
def create_random_array(left, right, size):
    return [randint(left, right) for _ in range(size)]

def print_array(array):
    for item in array:
        print(item, end=' ')
    print('')

def print_prefix(prefix):
    print(prefix, end = ' ')

def print_separator(size = 10):
    for _ in range(size):
        print('*', end='')
    print('')

def is_sorted(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            return False
    return True

def _more(item, array, border, end):
    for i in range(border, end):
        if array[i] < item:
            return True
    return False    

def is_partition(array, begin, end, border):
    for i in range(begin, border):
        if _more(array[i], array, border, end):
            return False
    return True

from copy import copy
def sort_in_time(first_algorithm, second_algorithm, first_name, second_name):
    array1 = create_random_array(0, 1000, 100000)
    array2 = copy(array1)
    array3 = copy(array1)
    print_separator()
    how_long(first_name, first_algorithm, array1)
    how_long(second_name, second_algorithm, array2)
    how_long('Native sort', array3.sort)
    
def call_f_for_random_array(f, *args):
    for _ in range(10):
        array = create_random_array(-1000, 1000, 100)
        f(array, *args)      
    
def test_random_sort(sort_algorithm):
    def _array_is_sorted_by(array, sort_algorithm):    
        sort_algorithm(array)
        if is_sorted(array):
            return True
        return False 
    for _ in range(10):
        array = create_random_array(-1000, 1000, 100)
        if not _array_is_sorted_by(array, sort_algorithm):
            return False
    return True


